"""Sketching and feature creation, against a real SOLIDWORKS.

Skipped unless ``SWCOMAPI_LIVE=1``. Everything here is built from nothing in a
new part and thrown away afterwards, so no file of yours is involved. It does
take the focus while it runs.

The part it builds is a 60 by 40 plate, 10 mm thick, with a 12 mm hole through
it - chosen because every number in it can be checked by hand:

    volume = 60 * 40 * 10 - pi * 6**2 * 10 = 22869.0 mm3
"""

import math

import pytest

import swcomapi as swc
from swcomapi.errors import SwCallError

pytestmark = pytest.mark.live

PLATE_VOLUME = 60.0 * 40.0 * 10.0 - math.pi * 6.0**2 * 10.0


@pytest.fixture(scope="module")
def app():
    try:
        return swc.attach(visible=None)
    except Exception as exc:
        pytest.skip(f"no SOLIDWORKS to talk to: {exc}")


@pytest.fixture(scope="module")
def plate(app):
    """A 60 by 40 plate 10 mm thick with a 12 mm hole through it."""
    part = app.new_part()

    with part.sketch_on("Front Plane", add_to_db=True) as sketch:
        sketch.rectangle((0, 0), (60, 40))
    part.extrude(10)

    with part.sketch_on("Front Plane", add_to_db=True) as sketch:
        sketch.circle((30, 20), radius=6)
    part.cut(through_all=True, reverse=True)

    yield part
    part.close()


class TestBuilding:
    def test_the_volume_is_what_the_arithmetic_says(self, plate):
        assert plate.volume == pytest.approx(PLATE_VOLUME, abs=0.5)

    def test_both_features_are_in_the_tree(self, plate):
        names = [feature.name for feature in plate.features.solid_features()]
        assert names == ["Boss-Extrude1", "Cut-Extrude1"]

    def test_the_extrusion_knows_what_it_is(self, plate):
        assert plate.features["Boss-Extrude1"].type == "Extrusion"

    def test_a_cut_the_wrong_way_round_says_to_reverse_it(self, plate):
        """Through-all away from the material removes nothing, and SOLIDWORKS
        reports that as a bare None."""
        with plate.sketch_on("Front Plane", add_to_db=True) as sketch:
            sketch.circle((10, 10), radius=2)
        with pytest.raises(SwCallError, match="reverse=True"):
            plate.cut(through_all=True)
        # The sketch is left behind, unconsumed, and nothing else is disturbed.
        assert plate.features[-1].type == "ProfileFeature"


class TestReadingSketches:
    def test_the_sketches_are_listed_in_tree_order(self, plate):
        names = plate.sketches.names()
        assert names[:2] == ["Sketch1", "Sketch2"]

    def test_a_sketch_can_be_reached_by_name(self, plate):
        assert plate.sketches["Sketch1"].name == "Sketch1"

    def test_a_name_that_is_not_there_is_a_key_error(self, plate):
        with pytest.raises(KeyError):
            plate.sketches["Sketch99"]

    def test_the_rectangle_is_four_lines_of_the_right_length(self, plate):
        segments = plate.sketches["Sketch1"].segments
        assert len(segments) == 4
        assert {segment.kind for segment in segments} == {"line"}
        lengths = sorted(round(segment.length, 3) for segment in segments)
        assert lengths == [40.0, 40.0, 60.0, 60.0]

    def test_the_circle_is_one_arc_of_the_right_circumference(self, plate):
        segments = plate.sketches["Sketch2"].segments
        assert len(segments) == 1
        assert segments[0].kind == "arc"
        assert segments[0].length == pytest.approx(2 * math.pi * 6, abs=0.01)

    def test_the_points_come_back_in_mm(self, plate):
        points = plate.sketches["Sketch1"].points
        assert (0.0, 0.0, 0.0) in points
        assert (60.0, 40.0, 0.0) in points

    def test_a_sketch_on_a_plane_is_not_3d(self, plate):
        assert plate.sketches["Sketch1"].is_3d is False


class TestTheSession:
    def test_a_plane_that_is_not_there_is_an_error(self, app):
        part = app.new_part()
        try:
            with pytest.raises(SwCallError, match="cannot sketch on"):
                with part.sketch_on("Nonsense Plane"):
                    pass
        finally:
            part.close()

    def test_an_error_inside_the_block_still_closes_the_sketch(self, app):
        """A session left in sketch mode makes everything after it strange."""
        from swcomapi import com

        part = app.new_part()
        try:
            with pytest.raises(RuntimeError):
                with part.sketch_on("Top Plane", add_to_db=True) as sketch:
                    sketch.line((0, 0), (10, 0))
                    raise RuntimeError("boom")
            assert com.call(part.sketches.manager, "ActiveSketch") is None
        finally:
            part.close()

    def test_a_3d_sketch_reports_itself_as_one(self, app):
        part = app.new_part()
        try:
            with part.sketch_on(three_d=True, add_to_db=True) as sketch:
                sketch.line((0, 0, 0), (10, 10, 10))
            assert part.sketches[0].is_3d is True
        finally:
            part.close()


class TestRevolve:
    def test_a_revolved_rectangle_is_a_cylinder(self, app):
        """20 wide by 30 tall about the y axis: pi * 20**2 * 30."""
        part = app.new_part()
        try:
            with part.sketch_on("Front Plane", add_to_db=True) as sketch:
                sketch.centreline((0, 0), (0, 30))
                sketch.rectangle((0, 0), (20, 30))
            feature = part.revolve()
            assert feature.type == "Revolution"
            assert part.volume == pytest.approx(math.pi * 20**2 * 30, rel=0.001)
        finally:
            part.close()
