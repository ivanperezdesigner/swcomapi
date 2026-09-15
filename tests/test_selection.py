"""The selection helper, without SOLIDWORKS.

What can be checked here is the dispatch: which of the three selection calls a
thing goes through, what mark it carries, and what happens when a name is not
found. The COM side is checked in tests/live/test_modeling.py.
"""

import pytest

from swcomapi.api import selection
from swcomapi.errors import SwCallError


class FakeEntity:
    """Something that answers Select4 and nothing else, like an IFace2."""

    def __init__(self, answer=True):
        self.answer = answer
        self.calls = []

    def Select4(self, append, data):
        self.calls.append(("Select4", append, data))
        return self.answer


class FakeFeature:
    """Something that answers GetTypeName2 and Select2, like an IFeature."""

    def __init__(self, answer=True):
        self.answer = answer
        self.calls = []

    def GetTypeName2(self):
        return "Extrusion"

    def Select2(self, append, mark):
        self.calls.append(("Select2", append, mark))
        return self.answer


class FakeDocument:
    """Just enough document for the helper: a name, select and clear."""

    def __init__(self, found=True):
        self.name = "plate.SLDPRT"
        self.com = object()
        self.found = found
        self.selected = []
        self.cleared = 0

    def select(self, name, kind, mark=0, append=False):
        self.selected.append((name, kind, mark, append))
        return self.found

    def clear_selection(self):
        self.cleared += 1


class TestAnObject:
    def test_a_feature_goes_through_select2_with_its_mark(self):
        document, feature = FakeDocument(), FakeFeature()
        assert selection.select(document, feature, mark=4) is True
        assert feature.calls == [("Select2", True, 4)]

    def test_an_entity_goes_through_select4(self):
        document, face = FakeDocument(), FakeEntity()
        assert selection.select(document, face) is True
        name, append, data = face.calls[0]
        assert (name, append) == ("Select4", True)
        # com.call turns the None into VBA's Nothing, because the generated
        # table says Select4 wants an object there.
        assert data is None or "VARIANT" in type(data).__name__

    def test_a_wrapper_is_unwrapped_to_its_com(self):
        class Wrapper:
            def __init__(self, com):
                self.com = com

        document, face = FakeDocument(), FakeEntity()
        selection.select(document, Wrapper(face))
        assert [call[0] for call in face.calls] == ["Select4"]

    def test_a_refused_selection_raises(self):
        document, face = FakeDocument(), FakeEntity(answer=False)
        with pytest.raises(SwCallError, match="would not select"):
            selection.select(document, face)

    def test_append_false_clears_first(self):
        document, face = FakeDocument(), FakeEntity()
        selection.select(document, face, append=False)
        assert document.cleared == 1


class TestAName:
    def test_a_name_and_a_kind_go_straight_through(self):
        document = FakeDocument()
        selection.select(document, ("Front Plane", "PLANE"), mark=2)
        assert document.selected == [("Front Plane", "PLANE", 2, True)]

    def test_a_bare_name_tries_each_kind_in_turn(self):
        document = FakeDocument(found=False)
        with pytest.raises(SwCallError, match="tried BODYFEATURE"):
            selection.select(document, "Nope")
        assert [kind for _, kind, _, _ in document.selected] == list(
            selection.STRING_KINDS
        )

    def test_a_named_kind_that_is_not_there_says_so(self):
        document = FakeDocument(found=False)
        with pytest.raises(SwCallError, match="as a PLANE"):
            selection.select(document, ("Nope", "PLANE"))


class TestSeveral:
    def test_the_first_replaces_and_the_rest_append(self):
        document = FakeDocument()
        faces = [FakeEntity(), FakeEntity(), FakeEntity()]
        assert selection.select_all(document, faces) == 3
        assert [face.calls[0][1] for face in faces] == [False, True, True]

    def test_append_keeps_what_was_already_selected(self):
        document = FakeDocument()
        faces = [FakeEntity(), FakeEntity()]
        selection.select_all(document, faces, append=True)
        assert [face.calls[0][1] for face in faces] == [True, True]

    def test_every_one_carries_the_same_mark(self):
        document = FakeDocument()
        features = [FakeFeature(), FakeFeature()]
        selection.select_all(document, features, mark=4)
        assert [f.calls[0][2] for f in features] == [4, 4]


class TestTheMarkTable:
    def test_mark_zero_needs_no_select_data(self):
        assert selection.selection_data(FakeDocument(), 0) is None

    def test_the_documented_marks_are_the_ones_the_code_uses(self):
        from swcomapi.api import patterns

        assert (patterns.DIRECTION_1, patterns.DIRECTION_2, patterns.FEATURES) == (
            1,
            2,
            4,
        )
