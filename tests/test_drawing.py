"""Sheets and views, on stand-in COM objects.

The name mangling, the unit conversion and the lookups are here. Anything
that needs a real drawing is in `tests/live/test_drawing_live.py`.
"""

import pytest

from swcomapi.api.drawing import (
    PAPER_SIZES,
    VIEW_TYPES,
    Sheet,
    Sheets,
    View,
    Views,
    _as_ratio,
    _view_name,
)


class FakeView:
    def __init__(self, name, kind=7, scale=1.0, position=(0.12, 0.15)):
        self._name = name
        self.Type = kind
        self.ScaleDecimal = scale
        self.Position = position
        self.UseSheetScale = True
        self.next = None
        self.moved_to = None

    def GetName2(self):
        return self._name

    def GetNextView(self):
        return self.next

    def GetReferencedModelName(self):
        return "C:/work/plate.SLDPRT"

    def SetViewPosition(self, position, move_children):
        self.moved_to = position
        return True

    def GetDimensionCount(self):
        return 0

    def GetDisplayDimensions(self):
        return None


def chain(*views):
    """Link views the way GetNextView walks them, behind a sheet view."""
    sheet_view = FakeView("Sheet1", kind=1)
    previous = sheet_view
    for view in views:
        previous.next = view
        previous = view
    return sheet_view


class FakeSheet:
    def __init__(self, name="Sheet1", scale=(1.0, 2.0), size=(0.42, 0.297)):
        self._name = name
        self._scale = scale
        self._size = size
        self.scaled_to = None

    def GetName(self):
        return self._name

    def GetProperties2(self):
        # paper size, template, scale1, scale2, first angle, width, height, custom
        return (8, 8, self._scale[0], self._scale[1], 1, self._size[0], self._size[1], 0)

    def SetScale(self, numerator, denominator, anno_position, anno_height):
        self.scaled_to = (numerator, denominator)
        return True


class FakeDrawing:
    def __init__(self, views=(), sheets=("Sheet1",), created=None):
        self.name = "Draw1"
        self._first = chain(*views)
        self._sheets = list(sheets)
        self._created = created
        self.new_sheet_args = None
        self.created_with = None
        self.com = self

    def GetFirstView(self):
        return self._first

    def GetSheetNames(self):
        return tuple(self._sheets)

    def Sheet(self, name):
        return FakeSheet(name)

    def GetCurrentSheet(self):
        return FakeSheet(self._sheets[0])

    def CreateDrawViewFromModelView3(self, model, view, x, y, z):
        self.created_with = (model, view, x, y, z)
        return self._created

    def NewSheet4(self, *args):
        self.new_sheet_args = args
        self._sheets.append(args[0] or f"Sheet{len(self._sheets) + 1}")
        return True

    def ActivateSheet(self, name):
        return name in self._sheets


class TestViewNames:
    def test_the_standard_views_get_the_asterisk_the_api_wants(self):
        """Plain "Front" gets no view and no error: None, silently."""
        assert _view_name("Front") == "*Front"
        assert _view_name("Top") == "*Top"
        assert _view_name("Isometric") == "*Isometric"

    def test_the_spelling_does_not_have_to_match(self):
        assert _view_name("isometric") == "*Isometric"
        assert _view_name("FRONT") == "*Front"

    def test_an_asterisk_already_there_is_left_alone(self):
        assert _view_name("*Top") == "*Top"

    def test_a_view_saved_in_the_model_is_passed_through(self):
        assert _view_name("Detail A") == "Detail A"


class TestRatio:
    def test_a_reduction_reads_as_one_to_n(self):
        assert _as_ratio(0.5) == "1:2"
        assert _as_ratio(0.2) == "1:5"

    def test_an_enlargement_reads_as_n_to_one(self):
        assert _as_ratio(2.0) == "2:1"

    def test_full_size_reads_as_one_to_one(self):
        assert _as_ratio(1.0) == "1:1"

    def test_a_scale_of_zero_does_not_divide_by_it(self):
        assert _as_ratio(0.0) == "?"


class TestViews:
    def test_the_sheet_itself_is_not_counted_as_a_view(self):
        """GetFirstView answers with the sheet, not with a view."""
        drawing = FakeDrawing(views=[FakeView("Drawing View1")])
        assert len(Views(drawing)) == 1
        assert Views(drawing).names() == ["Drawing View1"]

    def test_an_empty_sheet_has_no_views(self):
        assert Views(FakeDrawing()).names() == []

    def test_views_can_be_looked_up_by_name(self):
        drawing = FakeDrawing(views=[FakeView("Drawing View1"), FakeView("Drawing View2")])
        assert Views(drawing)["Drawing View2"].name == "Drawing View2"

    def test_a_name_that_is_not_there_is_a_key_error(self):
        with pytest.raises(KeyError, match="see .names\\(\\)"):
            Views(FakeDrawing())["Drawing View9"]

    def test_adding_sends_the_asterisked_name_and_metres(self):
        drawing = FakeDrawing(created=FakeView("Drawing View1"))
        Views(drawing).add("C:/work/plate.SLDPRT", "Front", at=(120, 200))
        model, view, x, y, z = drawing.created_with
        assert view == "*Front"
        assert (x, y, z) == (0.12, 0.2, 0.0)

    def test_a_view_that_does_not_appear_is_an_error_not_a_none(self):
        drawing = FakeDrawing(created=None)
        with pytest.raises(Exception, match="no view was created"):
            Views(drawing).add("C:/work/plate.SLDPRT", "Front")

    def test_of_kind_filters_by_view_type(self):
        drawing = FakeDrawing(
            views=[FakeView("Drawing View1", kind=7), FakeView("Drawing View2", kind=2)]
        )
        assert [v.name for v in Views(drawing).of_kind("section")] == ["Drawing View2"]


class TestView:
    def test_the_position_comes_back_in_mm(self):
        assert View(FakeView("v")).position == (120.0, 150.0)

    def test_moving_sends_a_safearray_not_a_tuple(self):
        """Passed as a tuple the call returns True and the view moves wrong."""
        raw = FakeView("v")
        View(raw).position = (150, 100)
        assert not isinstance(raw.moved_to, tuple)

    def test_the_scale_can_be_set_as_a_ratio(self):
        raw = FakeView("v")
        view = View(raw)
        view.scale = (1, 2)
        assert raw.ScaleDecimal == 0.5

    def test_the_type_codes_read_as_names(self):
        assert VIEW_TYPES[2] == "section"
        assert View(FakeView("v", kind=3)).kind == "detail"
        assert View(FakeView("v", kind=99)).kind == "unknown (99)"


class TestSheets:
    def test_the_sheets_are_listed_in_order(self):
        assert Sheets(FakeDrawing(sheets=("Sheet1", "Sheet2"))).names() == [
            "Sheet1",
            "Sheet2",
        ]

    def test_a_sheet_can_be_reached_by_name_and_by_position(self):
        sheets = Sheets(FakeDrawing(sheets=("Sheet1", "Sheet2")))
        assert sheets["Sheet2"].name == "Sheet2"
        assert sheets[1].name == "Sheet2"

    def test_a_name_that_is_not_there_says_what_is(self):
        sheets = Sheets(FakeDrawing(sheets=("Sheet1",)))
        with pytest.raises(KeyError, match="it has Sheet1"):
            sheets["Nope"]

    def test_adding_a_sheet_sends_the_paper_size_twice(self):
        """PaperSize and TemplateIn are different enumerations, numbered alike."""
        drawing = FakeDrawing()
        Sheets(drawing).add("Detail", paper="A3", scale=(1, 2))
        arguments = drawing.new_sheet_args
        assert arguments[0] == "Detail"
        assert arguments[1] == arguments[2] == PAPER_SIZES["a3"]
        assert (arguments[3], arguments[4]) == (1.0, 2.0)

    def test_a_paper_size_that_is_not_one_says_what_the_sizes_are(self):
        with pytest.raises(ValueError, match="'a3'"):
            Sheets(FakeDrawing()).add(paper="A9")


class TestSheet:
    def test_the_scale_is_a_pair(self):
        assert Sheet(FakeSheet(scale=(1.0, 2.0))).scale == (1.0, 2.0)

    def test_the_size_comes_back_in_mm(self):
        assert Sheet(FakeSheet()).size == (420.0, 297.0)

    def test_the_projection_angle_is_readable(self):
        assert Sheet(FakeSheet()).first_angle is True

    def test_setting_the_scale_reaches_the_sheet(self):
        raw = FakeSheet()
        Sheet(raw).scale = (1, 5)
        assert raw.scaled_to == (1.0, 5.0)
