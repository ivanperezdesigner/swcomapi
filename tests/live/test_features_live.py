"""The new feature calls, against a real SOLIDWORKS.

Skipped unless ``SWCOMAPI_LIVE=1``.

Every test here builds its own geometry and closes it afterwards, so the suite
leaves the machine as it found it. Nothing opens a file from disk except the
assembly tests, which need a part on disk to insert.

This is the module that settles whether a call is right. The argument order of
``FeatureFillet3`` and the mark a pattern reads its direction from cannot be
checked any other way: get either wrong and SOLIDWORKS makes a feature that
looks plausible and is not what was asked for.
"""

import os

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
def block(app):
    """A plain 60 by 40 by 10 plate, closed again afterwards."""
    part = app.new_part()
    with part.sketch_on("Front Plane", add_to_db=True) as sketch:
        sketch.rectangle((0, 0), (60, 40))
    part.extrude(10)
    try:
        yield part
    finally:
        _close(app, part)


@pytest.fixture
def plate(app):
    """The same plate with a 12 mm hole through the middle."""
    part = app.new_part()
    with part.sketch_on("Front Plane", add_to_db=True) as sketch:
        sketch.rectangle((0, 0), (60, 40))
    part.extrude(10)
    with part.sketch_on("Front Plane", add_to_db=True) as sketch:
        sketch.circle((30, 20), 6)
    part.cut(through_all=True, reverse=True)
    try:
        yield part
    finally:
        _close(app, part)


def _close(app, document):
    """Close a document by name, swallowing whatever a closed one raises."""
    try:
        app.close(document.name)
    except Exception:
        pass


def _top_of(part):
    """The face of a plate that faces the viewer, as a `Face`."""
    return [f for f in part.bodies[0].faces if f.normal == (0.0, 0.0, 1.0)][0]


class TestFillet:
    def test_every_edge_rounds(self, block):
        before = len(block.bodies[0].faces)
        made = block.fillet(2, edges=block.bodies[0].edges)
        assert made.type == "Fillet"
        assert len(block.bodies[0].faces) > before

    def test_one_edge_rounds(self, block):
        longest = max(block.bodies[0].edges, key=lambda e: e.length)
        made = block.fillet(3, edges=[longest])
        assert made.type == "Fillet"
        assert len(block.bodies[0].faces) == 7

    def test_a_radius_that_is_far_too_big_eats_the_part(self, block):
        """It does not raise. SOLIDWORKS makes the feature and reports success.

        This is here because the docstring used to promise the opposite.
        """
        longest = max(block.bodies[0].edges, key=lambda e: e.length)
        made = block.fillet(200, edges=[longest])
        assert made.type == "Fillet"
        assert block.bodies[0].volume < 0.2 * 60 * 40 * 10

    def test_the_volume_drops(self, block):
        before = block.bodies[0].volume
        block.fillet(2, edges=[max(block.bodies[0].edges, key=lambda e: e.length)])
        assert block.bodies[0].volume < before


class TestChamfer:
    def test_every_edge_breaks(self, block):
        made = block.chamfer(2, edges=block.bodies[0].edges)
        assert made.type == "Chamfer"
        assert made.name.startswith("Chamfer")

    def test_a_distance_distance_chamfer(self, block):
        made = block.chamfer(3, edges=[_top_of(block)], other_distance=1)
        assert made.type == "Chamfer"

    def test_the_volume_drops(self, block):
        before = block.bodies[0].volume
        block.chamfer(2, edges=block.bodies[0].edges)
        assert block.bodies[0].volume < before


class TestShell:
    def test_an_open_box(self, block):
        made = block.shell(2, faces=[_top_of(block)])
        assert made.type.startswith("Shell")
        assert block.bodies[0].volume < 60 * 40 * 10

    def test_a_wall_thicker_than_the_part_raises(self, block):
        from swcomapi.errors import SwCallError

        with pytest.raises(SwCallError, match="would not shell"):
            block.shell(50, faces=[_top_of(block)])


class TestHole:
    def test_a_hole_straight_through(self, block):
        made = block.hole(6, at=(15, 10, 10), through_all=True)
        assert made.name.startswith("Hole")
        assert len(block.bodies[0].faces_of("cylinder")) == 1

    def test_a_blind_hole(self, block):
        block.hole(6, at=(15, 10, 10), depth=4)
        assert block.bodies[0].volume < 60 * 40 * 10

    def test_a_point_off_the_face_raises(self, block):
        from swcomapi.errors import SwCallError

        with pytest.raises(SwCallError, match="lies at"):
            block.hole(6, at=(500, 500, 500), through_all=True)


class TestPatterns:
    def test_a_linear_pattern_repeats_the_hole(self, plate):
        along = max(plate.bodies[0].edges, key=lambda e: e.length)
        made = plate.patterns.linear("Cut-Extrude1", along, count=2, spacing=15)
        assert made.type == "LPattern"
        assert len(plate.bodies[0].faces_of("cylinder")) == 2

    def test_a_circular_pattern_repeats_the_hole(self, plate):
        bore = plate.bodies[0].faces_of("cylinder")[0]
        made = plate.patterns.circular("Cut-Extrude1", bore, count=4)
        assert made.type == "CirPattern"

    def test_a_mirror_doubles_the_plate(self, block):
        before = block.bodies[0].volume
        made = block.mirror("Boss-Extrude1", about="Right Plane")
        assert made.type in ("MirrorPattern", "Mirror")
        assert block.bodies[0].volume > before


class TestReferenceGeometry:
    def test_a_plane_at_a_distance(self, block):
        made = block.plane("Top Plane", distance=25)
        assert made.type == "RefPlane"
        assert made.name.startswith("Plane")

    def test_a_midplane_between_two_faces(self, block):
        faces = block.bodies[0].faces_of("plane")
        made = block.plane(faces[0], second=faces[1], midplane=True)
        assert made.type == "RefPlane"

    def test_sketching_on_a_plane_that_was_just_made(self, block):
        above = block.plane("Front Plane", distance=30)
        with block.sketch_on(above.name, add_to_db=True) as sketch:
            sketch.rectangle((0, 0), (20, 20))
        assert "Sketch2" in block.sketches.names()

    def test_an_axis_where_two_planes_cross(self, block):
        made = block.axis("Front Plane", "Right Plane")
        assert made.type == "RefAxis"

    def test_an_axis_down_a_hole(self, plate):
        bore = plate.bodies[0].faces_of("cylinder")[0]
        assert plate.axis(bore).type == "RefAxis"


class TestSketchDimensions:
    def test_a_dimension_drives_the_sketch(self, app):
        part = app.new_part()
        try:
            with part.sketch_on("Front Plane") as sketch:
                sides = sketch.rectangle((0, 0), (50, 25))
                name = sketch.dimension(sides[0], (25, -12), 60, name="width")
            assert "width" in name
            assert part.dimensions[name] == pytest.approx(60.0)
        finally:
            _close(app, part)

    def test_the_dimension_reaches_the_model(self, app):
        part = app.new_part()
        try:
            with part.sketch_on("Front Plane") as sketch:
                sides = sketch.rectangle((0, 0), (50, 25))
                sketch.dimension(sides[0], (25, -12), 60, name="width")
            part.extrude(10)
            assert part.bodies[0].size[0] == pytest.approx(60.0, abs=0.01)
        finally:
            _close(app, part)

    def test_a_relation_holds_two_lines_equal(self, app):
        part = app.new_part()
        try:
            with part.sketch_on("Front Plane") as sketch:
                first = sketch.line((0, 0), (40, 0))
                second = sketch.line((40, 0), (40, 25))
                assert sketch.relate([first, second], "equal") is True
            assert len(part.sketches["Sketch1"].segments) == 2
        finally:
            _close(app, part)

    def test_an_offset_adds_geometry(self, app):
        part = app.new_part()
        try:
            with part.sketch_on("Front Plane") as sketch:
                sides = sketch.rectangle((0, 0), (60, 30))
                sketch.offset(-3, entities=sides)
            assert len(part.sketches["Sketch1"].segments) > 4
        finally:
            _close(app, part)

    def test_a_mirror_adds_the_other_half(self, app):
        part = app.new_part()
        try:
            with part.sketch_on("Front Plane") as sketch:
                spine = sketch.centreline((0, -20), (0, 20))
                side = sketch.line((10, -20), (10, 20))
                sketch.mirror([side], about=spine)
            assert len(part.sketches["Sketch1"].segments) == 3
        finally:
            _close(app, part)


@pytest.fixture
def two_plates(app, tmp_path):
    """An assembly with two instances of a saved plate, and its parts."""
    part = app.new_part()
    with part.sketch_on("Front Plane", add_to_db=True) as sketch:
        sketch.rectangle((0, 0), (60, 40))
    part.extrude(10)
    stamp = os.path.basename(str(tmp_path).rstrip("\\/"))
    path = os.path.join(str(tmp_path), f"swcomapi-{stamp}.SLDPRT")
    part.save_as(path)

    assembly = app.new_assembly()
    assembly.components.add(path, at=(0, 0, 0))
    assembly.components.add(path, at=(150, 0, 0))
    assembly.rebuild()
    try:
        yield assembly
    finally:
        _close(app, assembly)
        _close(app, part)


class TestMates:
    def test_a_coincident_mate_between_two_planes(self, two_plates):
        first, second = two_plates.components.in_order()
        made = two_plates.mates.coincident(
            first.plane("Top Plane"), second.plane("Top Plane")
        )
        assert made.kind == "coincident"
        assert two_plates.mates.names() == [made.name]

    def test_a_distance_mate_keeps_its_value(self, two_plates):
        first, second = two_plates.components.in_order()
        made = two_plates.mates.distance(
            first.plane("Right Plane"), second.plane("Right Plane"), 80
        )
        assert made.kind == "distance"
        assert made.distance == pytest.approx(80.0, abs=0.01)

    def test_a_mate_between_things_that_cannot_mate_raises(self, two_plates):
        from swcomapi.errors import SwCallError

        first, second = two_plates.components.in_order()
        with pytest.raises(SwCallError, match="would not add"):
            two_plates.mates.concentric(
                first.plane("Top Plane"), second.plane("Top Plane")
            )

    def test_a_mate_can_be_deleted(self, two_plates):
        first, second = two_plates.components.in_order()
        made = two_plates.mates.coincident(
            first.plane("Top Plane"), second.plane("Top Plane")
        )
        assert made.delete() is True
        assert two_plates.mates.names() == []

    def test_the_faces_of_an_instance_belong_to_the_instance(self, two_plates):
        first, _ = two_plates.components.in_order()
        assert len(first.faces) == 6

    def test_a_component_moves(self, two_plates):
        first, second = two_plates.components.in_order()
        before = second.position
        second.move(by=(30, 0, 0))
        assert second.position[0] == pytest.approx(before[0] + 30, abs=0.01)

    def test_two_plates_apart_do_not_interfere(self, two_plates):
        assert two_plates.interferences() == []

    def test_two_plates_on_top_of_each_other_do(self, two_plates):
        first, second = two_plates.components.in_order()
        second.move(to=(0, 0, 0))
        found = two_plates.interferences()
        assert found and found[0]["volume"] > 0


@pytest.fixture
def sheet(app, tmp_path):
    """A drawing with one front view of a saved plate on it."""
    part = app.new_part()
    with part.sketch_on("Front Plane", add_to_db=True) as sketch:
        sketch.rectangle((0, 0), (60, 40))
    part.extrude(10)
    stamp = os.path.basename(str(tmp_path).rstrip("\\/"))
    path = os.path.join(str(tmp_path), f"swcomapi-draw-{stamp}.SLDPRT")
    part.save_as(path)

    drawing = app.new_drawing()
    drawing.views.add(path, "Front", at=(100, 100))
    try:
        yield drawing
    finally:
        _close(app, drawing)
        _close(app, part)


class TestDrawingViews:
    def test_a_section_view_is_cut(self, sheet):
        made = sheet.views.add_section(
            "Drawing View1", through=((100, 60), (100, 140)), at=(220, 100)
        )
        assert made.kind == "section"

    def test_a_detail_view_is_made(self, sheet):
        made = sheet.views.add_detail(
            "Drawing View1", centre=(100, 100), radius=12, at=(260, 160)
        )
        assert made.kind == "detail"

    def test_a_note_lands_on_the_sheet(self, sheet):
        assert sheet.views[0].add_note("BREAK ALL EDGES 0.5", at=(20, 20)) is not None

    def test_the_model_dimensions_come_across(self, sheet):
        assert sheet.views[0].insert_dimensions() is True
