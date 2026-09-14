"""Custom properties, on a stand-in ICustomPropertyManager.

The interesting case is the one that looks like two: a property that is not
there, and a property that is there and empty. ``Get6`` reports both with an
empty value and ``WasResolved`` True, and only its return code tells them
apart.
"""

import pytest

from swcomapi.api.properties import Properties

NOT_PRESENT = 1        # swCustomInfoGetResult_NotPresent
RESOLVED = 2           # swCustomInfoGetResult_ResolvedValue


class FakeManager:
    """An ICustomPropertyManager over a plain dict."""

    def __init__(self, values=None):
        self.values = dict(values or {})
        self.Count = len(self.values)

    def GetNames(self):
        return tuple(self.values) or None

    def Get6(self, name, use_cached, value, resolved, was_resolved, linked):
        """The real shape: four [out] parameters and a meaningful return."""
        present = name in self.values
        value.value = self.values.get(name, "")
        resolved.value = self.values.get(name, "")
        was_resolved.value = True
        linked.value = False
        return RESOLVED if present else NOT_PRESENT

    def Add3(self, name, kind, value, overwrite):
        self.values[name] = value
        self.Count = len(self.values)
        return 1

    def Delete2(self, name):
        self.values.pop(name, None)
        self.Count = len(self.values)
        return 0


def properties(values=None):
    return Properties(FakeManager(values), "", None)


class TestReading:
    def test_a_property_that_is_there_reads_back(self):
        assert properties({"Revision": "B"})["Revision"] == "B"

    def test_a_property_that_is_not_there_is_a_key_error(self):
        with pytest.raises(KeyError):
            properties({"Revision": "B"})["Nothing"]

    def test_a_property_that_is_there_and_empty_is_not_missing(self):
        """The case Get6's [out] parameters cannot distinguish."""
        assert properties({"Empty": ""})["Empty"] == ""

    def test_get_falls_back_to_the_default_for_a_missing_one(self):
        assert properties({"Revision": "B"}).get("Nothing", "-") == "-"

    def test_get_returns_an_empty_property_rather_than_the_default(self):
        assert properties({"Empty": ""}).get("Empty", "-") == ""

    def test_contains_agrees_with_the_names(self):
        values = properties({"Revision": "B"})
        assert "Revision" in values
        assert "Nothing" not in values

    def test_it_reads_as_a_dict(self):
        assert dict(properties({"Revision": "B", "Empty": ""})) == {
            "Revision": "B",
            "Empty": "",
        }

    def test_an_empty_set_of_properties_is_empty_not_an_error(self):
        """GetNames answers None rather than an empty array."""
        assert dict(properties()) == {}
        assert len(properties()) == 0


class TestWriting:
    def test_a_property_can_be_added_and_read_back(self):
        values = properties()
        values["Revision"] = "A"
        assert values["Revision"] == "A"

    def test_a_property_can_be_deleted(self):
        values = properties({"Revision": "B"})
        del values["Revision"]
        assert "Revision" not in values

    def test_deleting_one_that_is_not_there_is_a_key_error(self):
        with pytest.raises(KeyError):
            del properties()["Nothing"]
