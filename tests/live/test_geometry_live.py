"""Bodies, faces and edges, against a real SOLIDWORKS.

Skipped unless ``SWCOMAPI_LIVE=1``. The part is built here and thrown away
afterwards; no file of yours is involved.

The same 60 by 40 plate with a 12 mm hole as `tests/live/test_modeling.py`,
and every number below was worked out by hand before it was measured:

    volume  = 60 * 40 * 10 - pi * 6**2 * 10          = 22869.0 mm3
    area    = 2 * (2400 - pi * 36) + 2 * 600 + 2 * 400 + pi * 12 * 10
                                                    =  6950.8 mm2
    faces   = 6 flat + 1 cylindrical                 =       7
    edges   = 12 around the block + 2 round the hole =      14
"""

import math

import pytest

import swcomapi as swc

pytestmark = pytest.mark.live

VOLUME = 60.0 * 40.0 * 10.0 - math.pi * 6.0**2 * 10.0
AREA = (
    2 * (60.0 * 40.0 - math.pi * 6.0**2)
    + 2 * 60.0 * 10.0
    + 2 * 40.0 * 10.0
    + 2 * math.pi * 6.0 * 10.0
)


@pytest.fixture(scope="module")
def app():
    try:
        return swc.attach(visible=None)
    except Exception as exc:
        pytest.skip(f"no SOLIDWORKS to talk to: {exc}")


@pytest.fixture(scope="module")
def body(app):
    part = app.new_part()

    with part.sketch_on("Front Plane", add_to_db=True) as sketch:
        sketch.rectangle((0, 0), (60, 40))
    part.extrude(10)

    with part.sketch_on("Front Plane", add_to_db=True) as sketch:
        sketch.circle((30, 20), radius=6)
    part.cut(through_all=True, reverse=True)

    yield part.bodies[0]
    part.close()


class TestTheBody:
    def test_there_is_one_solid_and_it_is_solid(self, body):
        assert body.kind == "solid"

    def test_it_is_named_after_the_feature_that_made_it(self, body):
        assert body.name == "Cut-Extrude1"

    def test_the_box_is_the_plate(self, body):
        assert body.box == pytest.approx((0.0, 0.0, 0.0, 60.0, 40.0, 10.0), abs=1e-6)

    def test_the_size_is_what_stock_would_be_ordered_by(self, body):
        assert body.size == pytest.approx((60.0, 40.0, 10.0), abs=1e-6)

    def test_the_volume_matches_the_arithmetic(self, body):
        assert body.volume == pytest.approx(VOLUME, abs=0.5)

    def test_the_area_matches_the_arithmetic(self, body):
        assert body.area == pytest.approx(AREA, abs=0.5)

    def test_the_centre_of_mass_is_in_the_middle(self, body):
        assert body.centre_of_mass == pytest.approx((30.0, 20.0, 5.0), abs=1e-3)

    def test_mass_uses_the_documents_density(self, body):
        """Not density zero, which would make the mass equal the volume."""
        assert body.mass == pytest.approx(VOLUME * body.density / 1e6, rel=0.001)

    def test_mass_at_answers_for_another_material(self, body):
        assert body.mass_at(7800) == pytest.approx(VOLUME * 7800 / 1e6, rel=0.001)


class TestFaces:
    def test_the_plate_has_seven_faces(self, body):
        assert len(body.faces) == 7

    def test_six_are_flat_and_one_is_the_hole(self, body):
        assert len(body.faces_of("plane")) == 6
        assert len(body.faces_of("cylinder")) == 1

    def test_the_hole_wall_measures_what_it_should(self, body):
        hole = body.faces_of("cylinder")[0]
        assert hole.area == pytest.approx(2 * math.pi * 6 * 10, abs=0.1)

    def test_the_big_faces_are_the_plate_minus_the_hole(self, body):
        biggest = max(face.area for face in body.faces_of("plane"))
        assert biggest == pytest.approx(60 * 40 - math.pi * 36, abs=0.5)

    def test_a_flat_face_has_a_unit_normal(self, body):
        face = body.faces_of("plane")[0]
        assert face.normal is not None
        assert math.hypot(*face.normal) == pytest.approx(1.0)

    def test_a_cylindrical_face_has_none_rather_than_a_zero_vector(self, body):
        assert body.faces_of("cylinder")[0].normal is None

    def test_a_face_knows_its_own_edges(self, body):
        hole = body.faces_of("cylinder")[0]
        assert len(hole.edges) == 2
        assert {edge.kind for edge in hole.edges} == {"circle"}


class TestEdges:
    def test_the_plate_has_fourteen_edges(self, body):
        assert len(body.edges) == 14

    def test_they_are_lines_and_circles(self, body):
        assert sorted({edge.kind for edge in body.edges}) == ["circle", "line"]

    def test_a_circular_edge_measures_its_own_arc_not_the_whole_curve(self, body):
        circles = [edge for edge in body.edges if edge.kind == "circle"]
        assert len(circles) == 2
        for edge in circles:
            assert edge.length == pytest.approx(2 * math.pi * 6, abs=0.01)

    def test_the_straight_edges_are_the_sides_of_the_plate(self, body):
        lengths = sorted(
            round(edge.length, 3) for edge in body.edges if edge.kind == "line"
        )
        assert lengths == [10.0] * 4 + [40.0] * 4 + [60.0] * 4

    def test_a_straight_edge_has_two_ends_and_two_faces(self, body):
        edge = next(edge for edge in body.edges if edge.kind == "line")
        assert edge.start is not None
        assert edge.end is not None
        assert len(edge.faces) == 2

    def test_a_circular_edge_has_no_ends(self, body):
        """A closed curve has no start vertex, and SOLIDWORKS says None."""
        edge = next(edge for edge in body.edges if edge.kind == "circle")
        assert edge.start is None


class TestVertices:
    def test_the_plate_has_eight_corners(self, body):
        """The hole adds none: its two edges are closed circles."""
        assert len(body.vertices) == 8

    def test_they_are_the_corners_of_the_box(self, body):
        corners = {tuple(round(value, 3) for value in point) for point in body.vertices}
        assert (0.0, 0.0, 0.0) in corners
        assert (60.0, 40.0, 10.0) in corners


class TestSelection:
    def test_a_face_can_be_selected(self, body):
        """Select4 is declared on IEntity, and a face is one at run time."""
        document = body.document
        document.clear_selection()
        assert body.faces[0].select() is True
        assert document.selection_count == 1
        document.clear_selection()

    def test_selections_can_be_added_to(self, body):
        document = body.document
        document.clear_selection()
        body.faces[0].select()
        body.faces[1].select(append=True)
        assert document.selection_count == 2
        document.clear_selection()
