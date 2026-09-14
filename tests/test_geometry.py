"""Bodies, faces and edges, on stand-in COM objects.

The unit conversion and the type mapping are here. The geometry itself is in
`tests/live/test_geometry.py`, where there is a real solid to measure.
"""

import pytest

from swcomapi.api.geometry import (
    BODY_TYPES,
    DEFAULT_DENSITY,
    SURFACE_TYPES,
    Body,
    Edge,
    Face,
    bodies_of,
)


class FakeSurface:
    def __init__(self, identity=4001):
        self._identity = identity

    def Identity(self):
        return self._identity


class FakeFace:
    def __init__(self, area=0.0024, identity=4001, normal=(0.0, 0.0, 1.0)):
        self._area = area
        self._identity = identity
        self.Normal = normal

    def GetArea(self):
        return self._area

    def GetSurface(self):
        return FakeSurface(self._identity)

    def GetEdges(self):
        return None


class FakeBody:
    """A 60 by 40 by 10 plate, in metres, as the API would report it."""

    def __init__(self, faces=(), kind=0, name="Boss-Extrude1"):
        self.Name = name
        self._kind = kind
        self._faces = faces

    def GetType(self):
        return self._kind

    def GetFaces(self):
        return tuple(self._faces) or None

    def GetEdges(self):
        return None

    def GetVertices(self):
        return None

    def GetBodyBox(self):
        return (0.0, 0.0, 0.0, 0.06, 0.04, 0.01)

    def GetMassProperties(self, density):
        volume = 0.06 * 0.04 * 0.01
        return (0.03, 0.02, 0.005, volume, 0.0068, volume * density, 0, 0, 0)

    def GetMaterialIdName(self):
        return ""


class FakeDocument:
    def __init__(self, density=1000.0, bodies=()):
        self.name = "Part1"
        self._density = density
        self._bodies = bodies
        self.com = self

    def GetUserPreferenceDoubleValue(self, which):
        return self._density

    def GetBodies2(self, body_type, visible_only):
        return tuple(self._bodies) or None


class TestBody:
    def test_the_box_comes_back_in_mm(self):
        assert Body(FakeBody()).box == (0.0, 0.0, 0.0, 60.0, 40.0, 10.0)

    def test_size_is_the_box_measured_rather_than_located(self):
        assert Body(FakeBody()).size == (60.0, 40.0, 10.0)

    def test_volume_and_area_are_mm3_and_mm2(self):
        body = Body(FakeBody())
        assert body.volume == pytest.approx(24000.0)
        assert body.area == pytest.approx(6800.0)

    def test_mass_uses_the_documents_density_not_zero(self):
        """Density 0 gets a density of 1, so mass would equal volume."""
        body = Body(FakeBody(), FakeDocument(density=1000.0))
        assert body.mass == pytest.approx(24.0)

    def test_mass_at_answers_for_any_material(self):
        body = Body(FakeBody(), FakeDocument())
        assert body.mass_at(7800) == pytest.approx(187.2)
        assert body.mass_at(2700) == pytest.approx(64.8)

    def test_without_a_document_the_default_density_is_used(self):
        assert Body(FakeBody()).density == DEFAULT_DENSITY

    def test_a_document_with_no_density_falls_back(self):
        assert Body(FakeBody(), FakeDocument(density=0.0)).density == DEFAULT_DENSITY

    def test_the_type_codes_read_as_names(self):
        assert BODY_TYPES[0] == "solid"
        assert Body(FakeBody(kind=1)).kind == "sheet"
        assert Body(FakeBody(kind=99)).kind == "unknown (99)"

    def test_an_empty_body_lists_nothing_rather_than_failing(self):
        """GetFaces answers None, not an empty array."""
        body = Body(FakeBody())
        assert body.faces == []
        assert body.edges == []
        assert body.vertices == []

    def test_faces_of_filters_by_surface_type(self):
        body = Body(FakeBody(faces=[FakeFace(), FakeFace(identity=4002)]))
        assert len(body.faces_of("plane")) == 1
        assert len(body.faces_of("cylinder")) == 1
        assert body.faces_of("torus") == []


class TestFace:
    def test_the_surface_types_read_as_names(self):
        assert SURFACE_TYPES[4001] == "plane"
        assert Face(FakeFace(identity=4002)).kind == "cylinder"
        assert Face(FakeFace(identity=9999)).kind == "unknown (9999)"

    def test_the_area_comes_back_in_mm2(self):
        assert Face(FakeFace(area=0.0024)).area == pytest.approx(2400.0)

    def test_a_flat_face_has_a_normal(self):
        assert Face(FakeFace()).normal == (0.0, 0.0, 1.0)

    def test_a_curved_face_has_none_rather_than_a_zero_vector(self):
        """SOLIDWORKS answers (0, 0, 0), which would read as a direction."""
        assert Face(FakeFace(identity=4002, normal=(0.0, 0.0, 0.0))).normal is None


class FakeCurve:
    def __init__(self, line=True, circle=False, length=0.06):
        self._line = line
        self._circle = circle
        self._length = length

    def IsLine(self):
        return self._line

    def IsCircle(self):
        return self._circle

    def GetLength3(self, start, end):
        return self._length


class FakeParams:
    UMinValue = 0.0
    UMaxValue = 1.0


class FakeEdge:
    def __init__(self, curve=None):
        self._curve = curve if curve is not None else FakeCurve()

    def GetCurve(self):
        return self._curve

    def GetCurveParams3(self):
        return FakeParams()

    def GetStartVertex(self):
        return None

    def GetEndVertex(self):
        return None

    def GetTwoAdjacentFaces2(self):
        return None


class TestEdge:
    def test_a_straight_edge_is_a_line(self):
        assert Edge(FakeEdge()).kind == "line"

    def test_a_circular_edge_is_a_circle(self):
        curve = FakeCurve(line=False, circle=True)
        assert Edge(FakeEdge(curve)).kind == "circle"

    def test_anything_else_is_a_curve(self):
        curve = FakeCurve(line=False, circle=False)
        assert Edge(FakeEdge(curve)).kind == "curve"

    def test_the_length_comes_back_in_mm(self):
        assert Edge(FakeEdge()).length == pytest.approx(60.0)

    def test_a_closed_edge_has_no_ends(self):
        """A full circle's start and end vertices are None."""
        edge = Edge(FakeEdge())
        assert edge.start is None
        assert edge.end is None


class TestBodiesOf:
    def test_an_unknown_kind_says_what_the_kinds_are(self):
        with pytest.raises(ValueError, match=r"\['all', 'sheet', 'solid', 'wire'\]"):
            bodies_of(FakeDocument(), kind="blob")

    def test_a_part_with_no_solid_gives_an_empty_list(self):
        assert bodies_of(FakeDocument()) == []

    def test_the_bodies_carry_the_document_for_the_density(self):
        document = FakeDocument(density=7800.0, bodies=[FakeBody()])
        found = bodies_of(document)
        assert len(found) == 1
        assert found[0].density == 7800.0
