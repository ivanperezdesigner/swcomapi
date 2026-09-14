"""Equations and materials, against a real SOLIDWORKS.

Skipped unless ``SWCOMAPI_LIVE=1``. Builds a plate, drives it with global
variables, applies materials to it, and closes it without saving.
"""

import pytest

import swcomapi as swc
from swcomapi.api.materials import database_names
from swcomapi.errors import SwCallError

pytestmark = pytest.mark.live


@pytest.fixture(scope="module")
def app():
    try:
        return swc.attach(visible=None)
    except Exception as exc:
        pytest.skip(f"no SOLIDWORKS to talk to: {exc}")


@pytest.fixture
def plate(app):
    """A fresh 60 by 40 plate for each test, since these write to it."""
    part = app.new_part()
    with part.sketch_on("Front Plane", add_to_db=True) as sketch:
        sketch.rectangle((0, 0), (60, 40))
    part.extrude(10)
    yield part
    part.close()


class TestEquations:
    def test_a_new_part_has_none(self, plate):
        assert len(plate.equations) == 0
        assert plate.equations.names() == []

    def test_a_global_variable_can_be_added_and_read(self, plate):
        plate.equations.add('"width" = 60')
        assert plate.equations.names() == ["width"]
        assert plate.equations["width"] == 60.0
        assert plate.equations.is_global(0) is True

    def test_one_equation_can_drive_another(self, plate):
        plate.equations.add('"width" = 60')
        plate.equations.add('"height" = "width" * 0.5')
        assert plate.equations["height"] == 30.0

        plate.equations["width"] = 80
        assert plate.equations["width"] == 80.0
        assert plate.equations["height"] == 40.0

    def test_a_whole_line_can_be_rewritten_by_index(self, plate):
        """Which needs an indexed property put, not an attribute assignment."""
        plate.equations.add('"width" = 60')
        plate.equations[0] = '"width" = 90'
        assert plate.equations[0] == '"width" = 90'
        assert plate.equations["width"] == 90.0

    def test_the_values_are_in_the_documents_units_not_metres(self, plate):
        """The one place in this package where that is true."""
        plate.equations.add('"width" = 60')
        assert plate.equations["width"] == 60.0

    def test_globals_lists_them_as_a_dict(self, plate):
        plate.equations.add('"width" = 60')
        plate.equations.add('"height" = 40')
        assert plate.equations.globals() == {"width": 60.0, "height": 40.0}

    def test_an_equation_can_be_deleted(self, plate):
        plate.equations.add('"width" = 60')
        plate.equations.add('"height" = 40')
        del plate.equations[0]
        assert plate.equations.names() == ["height"]

    def test_a_line_solidworks_cannot_parse_is_an_error(self, plate):
        """It is forgiving about the quotes and strict about the rest: an
        unquoted name is accepted, a reference to a variable that does not
        exist is not."""
        with pytest.raises(SwCallError, match="would not add"):
            plate.equations.add('"b" = "missing" * 2')
        with pytest.raises(SwCallError, match="would not add"):
            plate.equations.add("nonsense")

    def test_a_name_that_is_not_there_is_a_key_error(self, plate):
        with pytest.raises(KeyError):
            plate.equations["nothing"]

    def test_evaluate_runs(self, plate):
        plate.equations.add('"width" = 60')
        plate.equations.evaluate()
        assert plate.equations["width"] == 60.0


class TestMaterials:
    def test_a_new_part_has_no_material(self, plate):
        assert plate.material == ""
        assert plate.material_database == ""

    def test_a_material_can_be_applied_and_read_back(self, plate):
        plate.material = "6061 Alloy"
        assert plate.material == "6061 Alloy"
        assert plate.material_database != ""

    def test_the_material_changes_the_mass(self, plate):
        """60 * 40 * 10 mm at 2700 kg/m3 is 64.8 g."""
        plate.material = "6061 Alloy"
        assert plate.mass == pytest.approx(64.8, rel=0.02)

    def test_a_material_can_be_removed(self, plate):
        plate.material = "6061 Alloy"
        plate.material = ""
        assert plate.material == ""

    def test_a_name_the_library_does_not_have_is_an_error(self, plate):
        """The raw call applies nothing and reports nothing."""
        with pytest.raises(SwCallError, match="was not applied"):
            plate.material = "Unobtainium"

    def test_the_material_is_per_configuration(self, plate):
        plate.material = "6061 Alloy"
        assert plate.material_of(plate.configuration) == "6061 Alloy"

    def test_the_libraries_are_listed(self, app):
        names = database_names(app)
        assert names
        assert any("solidworks materials" == name.lower() for name in names)
