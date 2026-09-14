"""Components, against a real SOLIDWORKS.

Skipped unless ``SWCOMAPI_LIVE=1``. This one does change things: it creates a
part and an assembly, saves them into a temporary folder, and closes and
deletes everything afterwards. Nothing of yours is touched, but it does take
the focus while it runs.

Run it with::

    set SWCOMAPI_LIVE=1
    .venv\\Scripts\\python -m pytest tests/live/test_assembly.py -v
"""

import os
import shutil
import tempfile

import pytest

import swcomapi as swc
from swcomapi.api.components import Component
from swcomapi.errors import SwCallError

pytestmark = pytest.mark.live


@pytest.fixture(scope="module")
def app():
    try:
        return swc.attach(visible=None)
    except Exception as exc:
        pytest.skip(f"no SOLIDWORKS to talk to: {exc}")


@pytest.fixture(scope="module")
def folder():
    """A temporary folder for the files this module creates."""
    path = tempfile.mkdtemp(prefix="swcomapi-live-")
    yield path
    shutil.rmtree(path, ignore_errors=True)


@pytest.fixture(scope="module")
def part_file(app, folder):
    """An empty part, saved. Geometry is not what these tests are about."""
    part = app.new_part()
    target = os.path.join(folder, "swcomapi_rail.SLDPRT")
    part.save_as(target)
    part.close()
    return target


@pytest.fixture(scope="module")
def assembly(app, part_file):
    """An assembly with three instances of the same part in it."""
    asm = app.new_assembly()
    asm.components.add(part_file)
    asm.components.add(part_file, at=(0, 80, 0))
    asm.components.add(part_file, at=(0, 160, 0))
    asm.rebuild()
    yield asm
    app.close_all()


class TestInserting:
    def test_every_instance_is_there(self, assembly):
        assert len(assembly.components) == 3
        assert assembly.component_count == 3

    def test_the_instances_are_numbered_from_one(self, assembly):
        """Sorted, because GetComponents does not answer in insertion order."""
        names = sorted(assembly.components.names())
        assert names == ["swcomapi_rail-1", "swcomapi_rail-2", "swcomapi_rail-3"]

    def test_they_all_come_from_the_same_file(self, assembly, part_file):
        paths = assembly.components.paths()
        assert len(paths) == 3
        assert {os.path.normcase(path) for path in paths} == {os.path.normcase(part_file)}

    def test_adding_a_file_that_is_not_there_is_a_file_not_found_error(self, assembly):
        with pytest.raises(FileNotFoundError):
            assembly.components.add("C:/nowhere/nothing.SLDPRT")


class TestReading:
    def test_indexing_by_position_and_by_name_agree(self, assembly):
        first = assembly.components[0]
        assert isinstance(first, Component)
        assert assembly.components[first.name].name == first.name

    def test_a_name_that_is_not_there_is_a_key_error(self, assembly):
        with pytest.raises(KeyError):
            assembly.components["nothing-1"]

    def test_the_state_of_a_freshly_inserted_component_is_resolved(self, assembly):
        assert assembly.components[0].state == "resolved"
        assert assembly.components[0].suppressed is False

    def test_one_component_is_fixed_and_the_rest_float(self, assembly):
        """SOLIDWORKS fixes the first one inserted and leaves the others free.

        Counted rather than indexed: GetComponents does not answer in
        insertion order, so components[0] is not necessarily that one.
        """
        fixed = [c.name for c in assembly.components if c.fixed]
        assert len(fixed) == 1

    def test_the_select_id_carries_the_assembly_name(self, assembly):
        assert assembly.components[0].select_id.endswith(f"@{assembly.name}")

    def test_position_comes_back_in_mm(self, assembly):
        """Inserted 80 mm apart, so the three sit 80 mm apart.

        By value rather than by index: GetComponents does not answer in
        insertion order.
        """
        positions = [component.position for component in assembly.components]
        assert all(len(p) == 3 for p in positions)
        heights = sorted(round(p[1], 6) for p in positions)
        assert [round(h - heights[0], 6) for h in heights] == [0.0, 80.0, 160.0]

    def test_the_document_behind_an_instance_is_a_part(self, assembly):
        document = assembly.components[0].document
        assert document is not None
        assert document.kind == "part"

    def test_all_reaches_the_same_three_with_no_subassemblies(self, assembly):
        assert len(assembly.components.all()) == 3

    def test_of_path_finds_every_instance_of_the_file(self, assembly):
        found = assembly.components.of_path("swcomapi_rail.SLDPRT")
        assert len(found) == 3


class TestChanging:
    def test_suppressing_hides_the_model_and_resolving_brings_it_back(self, assembly):
        component = assembly.components[2]
        component.suppress()
        assert component.state == "suppressed"
        assert component.suppressed is True
        assert component.document is None
        assert component.name in [c.name for c in assembly.components.suppressed()]

        component.resolve()
        assert component.state == "resolved"
        assert component.document is not None

    def test_hiding_is_not_suppressing(self, assembly):
        component = assembly.components[1]
        component.visible = False
        assert component.visible is False
        assert component.suppressed is False
        assert component.document is not None
        component.visible = True
        assert component.visible is True

    def test_selecting_one_puts_it_in_the_selection(self, assembly):
        assembly.clear_selection()
        assert assembly.components[0].select() is True
        assert assembly.selection_count == 1
        assembly.clear_selection()

    def test_renaming_reports_a_refusal_rather_than_pretending(self, assembly):
        """Off by default in Tools > Options, and the API says success anyway.

        Whichever way the option is set on this machine, the wrapper has to
        agree with what the tree ends up showing.
        """
        component = assembly.components[1]
        before = component.name
        try:
            component.name = "swcomapi_renamed-1"
        except SwCallError as exc:
            assert "Allow component files to be renamed" in str(exc)
            assert component.name == before
        else:
            assert component.name == "swcomapi_renamed-1"
            component.name = before
