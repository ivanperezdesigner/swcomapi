"""The component wrappers, on stand-in COM objects.

What can be tested without SOLIDWORKS is the mapping work: the suppression
codes, the lookup by name, the error messages. Everything that needs a real
assembly is in `tests/live/test_assembly.py`.
"""

import pytest

from swcomapi.api.components import STATES, Component, Components, _suppression_error
from swcomapi.errors import SwCallError


class FakeComponent:
    """A stand-in for ``IComponent2``."""

    def __init__(self, name, path="C:/work/rail.SLDPRT", state=2, refuse=False):
        self.Name2 = name
        self._path = path
        self._state = state
        self._refuse = refuse
        self.Visible = 1
        self.ExcludeFromBOM = False
        self.ReferencedConfiguration = "Default"

    def GetPathName(self):
        return self._path

    def GetSuppression2(self):
        return self._state

    def IsSuppressed(self):
        return self._state == 0

    def SetSuppression2(self, state):
        if self._refuse:
            return 3  # swSuppressionChangeFailed
        self._state = state
        return 2  # swSuppressionChangeOk

    def IsFixed(self):
        return True

    def IsVirtual(self):
        return False

    def Solving(self):
        return 0

    def GetChildren(self):
        return None


class FakeAssembly:
    """Enough of a `Document` for `Components` to work on."""

    def __init__(self, components, name="frame"):
        self._components = components
        self.name = name
        self.app = None
        self.com = self

    def GetComponents(self, top_level_only):
        return tuple(self._components)


def components(*names):
    return Components(FakeAssembly([FakeComponent(name) for name in names]))


class TestStates:
    def test_both_resolved_codes_read_the_same(self):
        """swComponentResolved is what you set; FullyResolved is what you read."""
        assert STATES[2] == STATES[3] == "resolved"

    def test_both_lightweight_codes_read_the_same(self):
        assert STATES[1] == STATES[4] == "lightweight"

    def test_a_code_with_no_name_says_so_rather_than_lying(self):
        assert Component(FakeComponent("x", state=99)).state == "unknown (99)"


class TestComponent:
    def test_it_reports_name_path_and_state(self):
        component = Component(FakeComponent("rail-2"))
        assert component.name == "rail-2"
        assert component.path == "C:/work/rail.SLDPRT"
        assert component.state == "resolved"
        assert component.suppressed is False

    def test_suppressing_changes_the_state(self):
        component = Component(FakeComponent("rail-2"))
        assert component.suppress() is True
        assert component.state == "suppressed"
        assert component.suppressed is True
        assert component.resolve() is True
        assert component.state == "resolved"

    def test_a_refusal_is_an_error_that_says_why(self):
        component = Component(FakeComponent("rail-2", refuse=True))
        with pytest.raises(SwCallError, match="mated to is the usual reason"):
            component.suppress()

    def test_visible_reads_the_enumeration_not_the_truthiness(self):
        raw = FakeComponent("rail-2")
        raw.Visible = 0
        assert Component(raw).visible is False
        raw.Visible = 1
        assert Component(raw).visible is True

    def test_the_repr_carries_the_state(self):
        assert repr(Component(FakeComponent("rail-2"))) == "<Component 'rail-2' resolved>"


class TestComponents:
    def test_it_is_a_sequence(self):
        listed = components("rail-1", "rail-2", "gusset-1")
        assert len(listed) == 3
        assert listed[0].name == "rail-1"
        assert [c.name for c in listed] == ["rail-1", "rail-2", "gusset-1"]
        assert [c.name for c in listed[1:]] == ["rail-2", "gusset-1"]

    def test_it_is_also_a_lookup_by_instance_name(self):
        listed = components("rail-1", "rail-2")
        assert listed["rail-2"].name == "rail-2"
        assert "rail-2" in listed
        assert "rail-9" not in listed

    def test_a_name_that_is_not_there_says_where_to_look(self):
        listed = components("rail-1")
        with pytest.raises(KeyError, match="see .names\\(\\)"):
            listed["rail-9"]

    def test_an_empty_assembly_is_empty_not_an_error(self):
        """GetComponents returns None rather than an empty array."""

        class Empty(FakeAssembly):
            def GetComponents(self, top_level_only):
                return None

        listed = Components(Empty([]))
        assert len(listed) == 0
        assert listed.names() == []

    def test_paths_keeps_duplicates(self):
        """Two instances of one part are two entries; that is the count."""
        listed = components("rail-1", "rail-2")
        assert listed.paths() == ["C:/work/rail.SLDPRT", "C:/work/rail.SLDPRT"]

    def test_of_path_matches_on_the_file_name(self):
        listed = components("rail-1", "rail-2")
        assert len(listed.of_path("rail.SLDPRT")) == 2
        assert len(listed.of_path("C:/elsewhere/RAIL.SLDPRT")) == 2
        assert listed.of_path("gusset.SLDPRT") == []

    def test_adding_a_file_that_is_not_there_fails_before_the_com_call(self):
        listed = components("rail-1")
        with pytest.raises(FileNotFoundError):
            listed.add("C:/nowhere/nothing.SLDPRT")


class TestSuppressionError:
    def test_each_code_reads_as_a_sentence(self):
        assert "does not recognise" in _suppression_error(0)
        assert "not one a component" in _suppression_error(1)
        assert "refused the change" in _suppression_error(3)

    def test_an_unknown_code_is_reported_not_swallowed(self):
        assert _suppression_error(42) == "SetSuppression2 returned 42"
