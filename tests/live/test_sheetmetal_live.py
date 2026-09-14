"""Sheet metal, against a real SOLIDWORKS.

Skipped unless ``SWCOMAPI_LIVE=1``. Builds a 100 by 60 plate 2 mm thick,
converts it to sheet metal with a 3 mm bend radius, and reads the parameters
back. Nothing is saved.
"""

import pytest

import swcomapi as swc
from swcomapi import com

pytestmark = pytest.mark.live


@pytest.fixture(scope="module")
def app():
    try:
        return swc.attach(visible=None)
    except Exception as exc:
        pytest.skip(f"no SOLIDWORKS to talk to: {exc}")


@pytest.fixture(scope="module")
def blank(app):
    """A 2 mm plate converted to sheet metal, radius 3 mm, K-factor 0.5."""
    part = app.new_part()
    with part.sketch_on("Front Plane", add_to_db=True) as sketch:
        sketch.rectangle((0, 0), (100, 60))
    part.extrude(2)

    biggest = max(part.bodies[0].faces_of("plane"), key=lambda face: face.area)
    biggest.select()
    com.call(
        com.call(part.com, "FeatureManager"),
        "InsertConvertToSheetMetal2",
        0.002,      # Thickness, m
        False,      # ReverseThickDir
        True,       # FindBends
        0.003,      # Radius, m
        0.0,        # Gap
        0,          # ReliefType
        0.5,        # ReliefRatio
        0,          # OverlapType
        0.0,        # OverlapRatio
        False,      # KeepBody
    )
    part.clear_selection()
    yield part
    part.close()


class TestConverted:
    def test_the_part_is_sheet_metal_now(self, blank):
        assert blank.is_sheet_metal is True

    def test_the_parameters_are_reachable(self, blank):
        assert blank.sheet_metal is not None

    def test_the_thickness_is_what_was_asked_for_in_mm(self, blank):
        assert blank.sheet_metal.thickness == pytest.approx(2.0)

    def test_the_bend_radius_is_what_was_asked_for_in_mm(self, blank):
        assert blank.sheet_metal.bend_radius == pytest.approx(3.0)

    def test_the_k_factor_reads_back(self, blank):
        assert 0.0 < blank.sheet_metal.k_factor <= 1.0

    def test_the_bend_allowance_reads_as_a_name(self, blank):
        from swcomapi.api.sheetmetal import BEND_ALLOWANCE

        assert blank.sheet_metal.bend_allowance in BEND_ALLOWANCE.values()

    def test_as_dict_agrees_with_the_properties(self, blank):
        values = blank.sheet_metal.as_dict()
        assert values["thickness"] == pytest.approx(blank.sheet_metal.thickness)
        assert values["bend_radius"] == pytest.approx(blank.sheet_metal.bend_radius)

    def test_reading_twice_still_works(self, blank):
        """Which is the whole point of releasing the definition each time: a
        feature left locked answers the first read and nothing after it."""
        first = blank.sheet_metal.as_dict()
        second = blank.sheet_metal.as_dict()
        assert first == second


class TestPlainSolid:
    def test_a_solid_that_is_not_sheet_metal_says_so(self, app):
        part = app.new_part()
        try:
            with part.sketch_on("Front Plane", add_to_db=True) as sketch:
                sketch.rectangle((0, 0), (20, 20))
            part.extrude(5)
            assert part.is_sheet_metal is False
            assert part.sheet_metal is None
        finally:
            part.close()
