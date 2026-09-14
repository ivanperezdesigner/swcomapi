"""Sheets and views, against a real SOLIDWORKS.

Skipped unless ``SWCOMAPI_LIVE=1``. Builds a plate, saves it to a temporary
folder, puts three views of it on a drawing and exports a PDF. Everything is
deleted afterwards.
"""

import os
import shutil
import tempfile

import pytest

import swcomapi as swc
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
    path = tempfile.mkdtemp(prefix="swcomapi-dwg-")
    yield path
    shutil.rmtree(path, ignore_errors=True)


@pytest.fixture(scope="module")
def part_file(app, folder):
    """A 60 by 40 plate, 10 thick, saved."""
    part = app.new_part()
    with part.sketch_on("Front Plane", add_to_db=True) as sketch:
        sketch.rectangle((0, 0), (60, 40))
    part.extrude(10)
    target = os.path.join(folder, "swcomapi_plate.SLDPRT")
    part.save_as(target)
    return target


@pytest.fixture(scope="module")
def drawing(app, part_file):
    """A drawing with a front, a top and an isometric view on it."""
    made = app.new_drawing()
    made.views.add(part_file, "Front", at=(80, 150))
    made.views.add(part_file, "Top", at=(80, 80))
    made.views.add(part_file, "Isometric", at=(200, 150), scale=(1, 2))
    yield made
    app.close_all()


class TestSheets:
    def test_a_new_drawing_has_one_sheet(self, drawing):
        assert len(drawing.sheets) == 1

    def test_the_active_sheet_has_a_size_in_mm(self, drawing):
        width, height = drawing.sheets.active.size
        assert 100.0 < width < 1200.0
        assert 100.0 < height < 1200.0

    def test_the_scale_is_a_pair_of_numbers(self, drawing):
        numerator, denominator = drawing.scale
        assert numerator > 0 and denominator > 0

    def test_a_sheet_can_be_added_and_switched_between(self, drawing):
        drawing.sheets.add("swcomapi_detail", paper="A4", scale=(1, 2))
        assert "swcomapi_detail" in drawing.sheets.names()
        assert drawing.sheets.active.name == "swcomapi_detail"
        assert drawing.sheets.active.scale == (1.0, 2.0)

        drawing.sheet = "Sheet1"
        assert drawing.sheet == "Sheet1"

    def test_an_a4_sheet_measures_a4(self, drawing):
        drawing.sheets["swcomapi_detail"].activate()
        width, height = drawing.sheets.active.size
        assert (round(width), round(height)) == (297, 210)
        drawing.sheet = "Sheet1"

    def test_a_sheet_that_is_not_there_is_a_key_error(self, drawing):
        with pytest.raises(KeyError):
            drawing.sheets["nothing"]

    def test_a_paper_size_that_is_not_one_is_refused_before_the_call(self, drawing):
        with pytest.raises(ValueError):
            drawing.sheets.add(paper="A9")


class TestViews:
    def test_all_three_views_are_there(self, drawing):
        assert len(drawing.views) == 3

    def test_they_are_named_the_way_the_tree_names_them(self, drawing):
        assert drawing.views.names() == [
            "Drawing View1",
            "Drawing View2",
            "Drawing View3",
        ]

    def test_a_view_can_be_reached_by_name(self, drawing):
        assert drawing.views["Drawing View1"].name == "Drawing View1"

    def test_each_view_knows_which_model_it_is_of(self, drawing, part_file):
        model = drawing.views["Drawing View1"].model
        assert os.path.normcase(model) == os.path.normcase(part_file)

    def test_a_view_made_from_a_model_view_calls_itself_named(self, drawing):
        """Not "standard": that is what Create3rdAngleViews2 lays out."""
        assert drawing.views["Drawing View1"].kind == "named"

    def test_the_position_is_where_it_was_asked_for(self, drawing):
        assert drawing.views["Drawing View1"].position == pytest.approx(
            (80.0, 150.0), abs=1e-6
        )

    def test_a_view_starts_at_the_sheet_scale(self, drawing):
        view = drawing.views["Drawing View2"]
        assert view.uses_sheet_scale is True

    def test_setting_a_scale_detaches_the_view_from_the_sheet(self, drawing):
        """There is no separate flag: the write is what detaches it."""
        view = drawing.views["Drawing View3"]
        assert view.scale == pytest.approx(0.5)
        assert view.uses_sheet_scale is False

    def test_a_view_can_be_moved(self, drawing):
        """The position has to reach SOLIDWORKS as a SafeArray, not a tuple."""
        view = drawing.views["Drawing View1"]
        view.position = (110.0, 160.0)
        assert view.position == pytest.approx((110.0, 160.0), abs=1e-6)
        view.position = (80.0, 150.0)

    def test_a_view_can_be_activated(self, drawing):
        assert drawing.views["Drawing View1"].activate() is True

    def test_a_misspelled_view_name_is_an_error_not_a_silent_nothing(self, drawing):
        with pytest.raises(SwCallError, match="no view was created"):
            drawing.views.add(drawing.views["Drawing View1"].model, "Nonsense")


class TestExport:
    def test_the_drawing_goes_out_as_a_pdf(self, drawing, folder):
        target = drawing.export(os.path.join(folder, "plate.pdf"))
        assert os.path.isfile(target)
        assert os.path.getsize(target) > 1000
