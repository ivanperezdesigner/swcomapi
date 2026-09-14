"""Sketching, on stand-in COM objects.

The arithmetic and the mapping work is here; anything that needs a real
sketch to exist is in `tests/live/test_modeling.py`.
"""

import pytest

from swcomapi.api.sketch import SEGMENT_TYPES, Segment, SketchSession, _point
from swcomapi.errors import SwCallError


class FakeSegment:
    def __init__(self, kind=0, length=0.06, construction=False):
        self._kind = kind
        self._length = length
        self.ConstructionGeometry = construction

    def GetType(self):
        return self._kind

    def GetLength(self):
        return self._length


class FakeManager:
    """Records what it was asked to draw, in metres, as the API would get it."""

    def __init__(self):
        self.calls = []
        self.AddToDB = False
        self._active = None

    def _record(self, name, *args):
        self.calls.append((name, args))
        return FakeSegment()

    def CreateLine(self, *args):
        return self._record("CreateLine", *args)

    def CreateCenterLine(self, *args):
        return self._record("CreateCenterLine", *args)

    def CreateCircleByRadius(self, *args):
        return self._record("CreateCircleByRadius", *args)

    def CreateArc(self, *args):
        return self._record("CreateArc", *args)

    def CreateCornerRectangle(self, *args):
        self.calls.append(("CreateCornerRectangle", args))
        return tuple(FakeSegment() for _ in range(4))

    def CreateCenterRectangle(self, *args):
        self.calls.append(("CreateCenterRectangle", args))
        return tuple(FakeSegment() for _ in range(4))

    def CreatePoint(self, *args):
        self.calls.append(("CreatePoint", args))
        return object()

    def InsertSketch(self, rebuild):
        self.calls.append(("InsertSketch", (rebuild,)))

    def Insert3DSketch(self, rebuild):
        self.calls.append(("Insert3DSketch", (rebuild,)))

    def ActiveSketch(self):
        return self._active


class FakeDocument:
    """Enough of a `Document` for a sketch session."""

    def __init__(self, selectable=("Front Plane",)):
        self.name = "Part1"
        self.manager = FakeManager()
        self.selectable = selectable
        self.cleared = 0
        self.com = self

    def SketchManager(self):
        return self.manager

    def select(self, name, kind, mark=0, append=False):
        return name in self.selectable

    def clear_selection(self):
        self.cleared += 1
        return True


def session(document=None, **options):
    return SketchSession(document or FakeDocument(), plane="Front Plane", **options)


class TestPoint:
    def test_two_values_mean_z_is_zero(self):
        assert _point((60, 40)) == (0.06, 0.04, 0.0)

    def test_three_values_are_taken_as_given(self):
        assert _point((0, 0, 10)) == (0.0, 0.0, 0.01)

    def test_anything_else_says_what_a_point_is(self):
        with pytest.raises(ValueError, match=r"\(x, y\) or \(x, y, z\) in mm"):
            _point((1, 2, 3, 4))


class TestDrawing:
    def test_a_line_arrives_in_metres(self):
        drawing = session()
        drawing.open()
        drawing.line((0, 0), (60, 0))
        name, args = drawing.document.manager.calls[-1]
        assert name == "CreateLine"
        assert args == (0.0, 0.0, 0.0, 0.06, 0.0, 0.0)

    def test_a_circle_takes_a_radius_not_a_point_on_it(self):
        """CreateCircle wants a second point; CreateCircleByRadius does not."""
        drawing = session()
        drawing.open()
        drawing.circle((30, 20), radius=6)
        name, args = drawing.document.manager.calls[-1]
        assert name == "CreateCircleByRadius"
        assert args == (0.03, 0.02, 0.0, 0.006)

    def test_a_rectangle_comes_back_as_four_segments(self):
        drawing = session()
        drawing.open()
        drawn = drawing.rectangle((0, 0), (60, 40))
        assert len(drawn) == 4
        assert all(isinstance(segment, Segment) for segment in drawn)

    def test_an_arc_sweeps_the_way_it_was_asked_to(self):
        drawing = session()
        drawing.open()
        drawing.arc((0, 0), (10, 0), (0, 10))
        assert drawing.document.manager.calls[-1][1][-1] == 1
        drawing.arc((0, 0), (10, 0), (0, 10), clockwise=True)
        assert drawing.document.manager.calls[-1][1][-1] == -1

    def test_centerline_is_the_same_method_spelled_the_other_way(self):
        assert SketchSession.centerline is SketchSession.centreline
        assert SketchSession.center_rectangle is SketchSession.centre_rectangle


class TestTheSession:
    def test_it_opens_and_closes_the_sketch(self):
        document = FakeDocument()
        with session(document):
            pass
        names = [name for name, _ in document.manager.calls]
        assert names == ["InsertSketch", "InsertSketch"]

    def test_it_closes_the_sketch_even_when_the_block_raises(self):
        """A session left in sketch mode makes every later call behave oddly."""
        document = FakeDocument()
        with pytest.raises(RuntimeError):
            with session(document) as drawing:
                drawing.line((0, 0), (10, 0))
                raise RuntimeError("boom")
        names = [name for name, _ in document.manager.calls]
        assert names.count("InsertSketch") == 2

    def test_a_plane_that_is_not_there_is_an_error_before_anything_is_drawn(self):
        document = FakeDocument(selectable=())
        with pytest.raises(SwCallError, match="The default planes are"):
            session(document).open()
        assert [name for name, _ in document.manager.calls] == []

    def test_database_mode_is_put_back_the_way_it_was(self):
        document = FakeDocument()
        document.manager.AddToDB = False
        with session(document, add_to_db=True):
            assert document.manager.AddToDB is True
        assert document.manager.AddToDB is False

    def test_a_3d_sketch_uses_the_other_call(self):
        document = FakeDocument()
        with session(document, three_d=True):
            pass
        names = [name for name, _ in document.manager.calls]
        assert names == ["Insert3DSketch", "Insert3DSketch"]


class TestSegment:
    def test_the_type_codes_read_as_names(self):
        assert SEGMENT_TYPES[0] == "line"
        assert SEGMENT_TYPES[1] == "arc"
        assert Segment(FakeSegment(kind=3)).kind == "spline"

    def test_an_unknown_code_is_reported_not_swallowed(self):
        assert Segment(FakeSegment(kind=99)).kind == "unknown (99)"

    def test_the_length_comes_back_in_mm(self):
        assert Segment(FakeSegment(length=0.06)).length == 60.0

    def test_construction_geometry_says_so_in_the_repr(self):
        assert "construction" in repr(Segment(FakeSegment(construction=True)))
        assert "construction" not in repr(Segment(FakeSegment()))
