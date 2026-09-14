"""Dimensions per configuration, against a real SOLIDWORKS.

Skipped unless ``SWCOMAPI_LIVE=1``. Builds a plate with three configurations
and checks that a write lands where it was aimed - which is the whole point:
the obvious route writes every configuration at once.
"""

import pytest

import swcomapi as swc

pytestmark = pytest.mark.live


@pytest.fixture(scope="module")
def app():
    try:
        return swc.attach(visible=None)
    except Exception as exc:
        pytest.skip(f"no SOLIDWORKS to talk to: {exc}")


@pytest.fixture
def plate(app):
    """A 60 by 40 plate 10 mm thick, with configurations A and B."""
    part = app.new_part()
    with part.sketch_on("Front Plane", add_to_db=True) as sketch:
        sketch.rectangle((0, 0), (60, 40))
    part.extrude(10)
    part.configurations.add("A")
    part.configurations.add("B")
    part.configuration = "Default"
    part.rebuild()
    yield part
    part.close()


@pytest.fixture
def depth(plate):
    """The extrusion's depth, whose name carries the document's name."""
    return plate.dimensions.names()[0]


class TestReading:
    def test_the_value_comes_back_in_mm(self, plate, depth):
        assert plate.dimensions[depth] == pytest.approx(10.0)

    def test_it_is_not_angular(self, plate, depth):
        assert plate.dimensions.is_angular(depth) is False

    def test_it_reads_as_a_dict(self, plate, depth):
        assert dict(plate.dimensions) == {depth: pytest.approx(10.0)}


class TestWritingPerConfiguration:
    def test_a_plain_write_changes_only_the_active_configuration(self, plate, depth):
        """The trap: IDimension.SystemValue changes all of them at once."""
        plate.configuration = "A"
        plate.dimensions[depth] = 6
        plate.rebuild()

        assert plate.dimensions.value_in(depth, "A") == pytest.approx(6.0)
        assert plate.dimensions.value_in(depth, "B") == pytest.approx(10.0)
        assert plate.dimensions.value_in(depth, "Default") == pytest.approx(10.0)

    def test_a_loop_over_configurations_leaves_each_at_its_own_value(
        self, plate, depth
    ):
        """What the first version of this package could not do."""
        wanted = {"Default": 10.0, "A": 6.0, "B": 16.0}
        for name, thickness in wanted.items():
            plate.configuration = name
            plate.dimensions[depth] = thickness
        plate.rebuild()

        for name, thickness in wanted.items():
            assert plate.dimensions.value_in(depth, name) == pytest.approx(thickness)

    def test_set_in_writes_without_switching(self, plate, depth):
        plate.configuration = "Default"
        plate.dimensions.set_in(depth, "B", 20)
        plate.rebuild()

        assert plate.dimensions.value_in(depth, "B") == pytest.approx(20.0)
        assert plate.configuration == "Default"
        assert plate.dimensions[depth] == pytest.approx(10.0)

    def test_set_everywhere_changes_all_of_them(self, plate, depth):
        plate.dimensions.set_everywhere(depth, 3)
        plate.rebuild()

        for name in ("Default", "A", "B"):
            assert plate.dimensions.value_in(depth, name) == pytest.approx(3.0)

    def test_the_mass_follows_the_configuration(self, plate, depth):
        """The reason any of this matters."""
        plate.material = "6061 Alloy"
        plate.configuration = "A"
        plate.dimensions[depth] = 5
        plate.rebuild()
        thin = plate.mass

        plate.configuration = "B"
        plate.dimensions[depth] = 20
        plate.rebuild()
        thick = plate.mass

        assert thick == pytest.approx(thin * 4, rel=0.01)
