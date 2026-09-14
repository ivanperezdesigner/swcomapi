"""The generated enumerations and the flat constant namespace.

These run with no SOLIDWORKS involved: the data is committed to the repository
precisely so that it does not need one.

The values asserted here are anchored by hand from the official documentation,
not copied out of the generated file. That is the point: if a regeneration ever
shifts one of them, this fails instead of quietly changing what every script
means.
"""

import pytest

from swcomapi import const, enums, generated


class TestAnchoredValues:
    """Hand-checked against the SOLIDWORKS API documentation."""

    def test_document_types(self):
        assert enums.swDocumentTypes_e.swDocNONE == 0
        assert enums.swDocumentTypes_e.swDocPART == 1
        assert enums.swDocumentTypes_e.swDocASSEMBLY == 2
        assert enums.swDocumentTypes_e.swDocDRAWING == 3

    def test_save_as_version(self):
        assert enums.swSaveAsVersion_e.swSaveAsCurrentVersion == 0

    def test_save_as_options(self):
        assert enums.swSaveAsOptions_e.swSaveAsOptions_Silent == 1

    def test_rebuild_on_activation(self):
        assert enums.swRebuildOnActivation_e.swUserDecision == 0
        assert enums.swRebuildOnActivation_e.swDontRebuildActiveDoc == 1
        assert enums.swRebuildOnActivation_e.swRebuildActiveDoc == 2

    def test_the_open_document_flags_really_are_powers_of_two(self):
        """swOpenDocOptions_e is a bit field, which is why they combine."""
        assert enums.swOpenDocOptions_e.swOpenDocOptions_Silent == 1
        assert enums.swOpenDocOptions_e.swOpenDocOptions_ReadOnly == 2
        assert enums.swOpenDocOptions_e.swOpenDocOptions_ViewOnly == 4
        assert enums.swOpenDocOptions_e.swOpenDocOptions_LoadModel == 16

    def test_the_file_load_warnings(self):
        assert enums.swFileLoadWarning_e.swFileLoadWarning_IdMismatch == 1
        assert enums.swFileLoadWarning_e.swFileLoadWarning_ReadOnly == 2
        assert enums.swFileLoadWarning_e.swFileLoadWarning_NeedsRegen == 32
        assert enums.swFileLoadWarning_e.swFileLoadWarning_AlreadyOpen == 128

    def test_the_flat_namespace_agrees_with_the_enumerations(self):
        assert const.swDocPART == enums.swDocumentTypes_e.swDocPART
        assert const.swDocDRAWING == enums.swDocumentTypes_e.swDocDRAWING
        assert const.swSaveAsCurrentVersion == 0


class TestEnumBehaviour:
    def test_a_member_is_a_real_int_enum(self):
        from enum import IntEnum

        assert issubclass(enums.swDocumentTypes_e, IntEnum)
        assert isinstance(enums.swDocumentTypes_e.swDocPART, int)

    def test_repr_names_the_module_not_the_enum_module(self):
        """Without module= in the functional API this would say 'enum'."""
        assert enums.swDocumentTypes_e.__module__ == "swcomapi.enums"

    def test_lookup_by_value(self):
        assert enums.swDocumentTypes_e(3).name == "swDocDRAWING"

    def test_lookup_by_name(self):
        assert enums.swDocumentTypes_e["swDocPART"] == 1

    def test_it_can_be_iterated(self):
        names = [m.name for m in enums.swDocumentTypes_e]
        assert names[:3] == ["swDocNONE", "swDocPART", "swDocASSEMBLY"]

    def test_members_keep_their_declared_order(self):
        values = [int(m) for m in enums.swDocumentTypes_e]
        assert values == sorted(values)

    def test_bit_flags_combine_into_a_plain_int(self):
        """No IntFlag anywhere: combining still gives the API what it wants."""
        combined = (
            enums.swOpenDocOptions_e.swOpenDocOptions_Silent
            | enums.swOpenDocOptions_e.swOpenDocOptions_ReadOnly
        )
        assert isinstance(combined, int)
        assert combined == 1 | 2

    def test_the_class_is_cached_not_rebuilt(self):
        assert enums.swDocumentTypes_e is enums.swDocumentTypes_e

    def test_it_carries_a_docstring_saying_where_it_came_from(self):
        assert "SwConst" in enums.swDocumentTypes_e.__doc__

    def test_an_unknown_enumeration_says_so_helpfully(self):
        missing = "swNotAnEnum_e"
        with pytest.raises(AttributeError, match="has no enumeration"):
            getattr(enums, missing)


class TestEnumModule:
    def test_every_enumeration_actually_builds(self):
        """1,434 of them. A single malformed entry would show up here."""
        for name in enums.names():
            built = getattr(enums, name)
            assert built.__name__ == name

    def test_there_are_over_a_thousand(self):
        assert len(enums.names()) > 1000

    def test_dir_lists_them(self):
        assert "swDocumentTypes_e" in dir(enums)

    def test_find(self):
        assert enums.find("SaveAsVersion") == ["swSaveAsVersion_e"]

    def test_find_is_case_insensitive(self):
        assert "swDocumentTypes_e" in enums.find("documenttypes")

    def test_find_that_matches_nothing(self):
        assert enums.find("definitely-not-an-enum") == []

    def test_library_of(self):
        assert enums.library_of("swDocumentTypes_e") == "SwConst"

    def test_library_of_an_unknown_name(self):
        with pytest.raises(KeyError):
            enums.library_of("swNope_e")


class TestConstModule:
    def test_there_are_over_ten_thousand(self):
        assert len(const.names()) > 10000

    def test_every_constant_resolves_to_an_int(self):
        for name in const.names():
            assert isinstance(getattr(const, name), int)

    def test_find_returns_name_value_and_owner(self):
        assert const.find("swDocPART") == [("swDocPART", 1, "swDocumentTypes_e")]

    def test_find_is_case_insensitive(self):
        assert any(n == "swDocPART" for n, _, _ in const.find("swdocpart"))

    def test_enum_of(self):
        assert const.enum_of("swDocPART") == "swDocumentTypes_e"

    def test_an_unknown_constant_points_at_find(self):
        missing = "swNotAConstant"
        with pytest.raises(AttributeError, match="Try swcomapi.const.find"):
            getattr(const, missing)

    def test_dir_lists_them(self):
        assert "swDocPART" in dir(const)


class TestNamespaceIsSafe:
    def test_every_constant_name_is_unique_across_all_enumerations(self):
        """What makes a flat namespace honest.

        The generator refuses to emit if this breaks, but asserting it here
        means a hand-edited data file cannot slip past either.
        """
        from swcomapi.generated._enum_data import ENUMS

        seen = {}
        for enum_name, members in ENUMS.items():
            for member, value in members.items():
                previous = seen.get(member)
                assert previous is None or previous[1] == value, (
                    f"{member} is {previous[1]} in {previous[0]} and {value} in {enum_name}"
                )
                seen[member] = (enum_name, value)

    def test_the_flat_namespace_holds_every_member(self):
        from swcomapi.generated._enum_data import ENUMS

        expected = sum(len(m) for m in ENUMS.values())
        assert len(const.names()) == expected

    def test_every_name_is_a_valid_python_identifier(self):
        assert all(name.isidentifier() for name in const.names())
        assert all(name.isidentifier() for name in enums.names())


class TestMeta:
    def test_it_knows_which_release_it_was_built_from(self):
        assert generated.SOLIDWORKS_YEAR >= 2020

    def test_it_lists_the_libraries_it_read(self):
        files = {lib["file"].lower() for lib in generated.LIBRARIES}
        assert "sldworks.tlb" in files
        assert "swconst.tlb" in files

    def test_sldworks_major_matches_the_release_year(self):
        major = next(
            lib["major"] for lib in generated.LIBRARIES if lib["file"].lower() == "sldworks.tlb"
        )
        assert major + 1992 == generated.SOLIDWORKS_YEAR

    def test_the_counts_agree_with_the_data(self):
        assert generated.COUNTS["enums"] == len(enums.names())
        assert generated.COUNTS["constants"] == len(const.names())

    def test_unreadable_is_a_list(self):
        assert isinstance(generated.UNREADABLE, list)

    def test_there_is_no_timestamp_anywhere_in_the_generated_files(self):
        """A timestamp would make every regeneration a diff, and would make
        the determinism check worthless."""
        import pathlib
        import re

        root = pathlib.Path(generated.__file__).parent
        for path in list(root.glob("*.py")) + list(root.parent.glob("*.pyi")):
            text = path.read_text(encoding="utf-8")
            assert not re.search(r"\b20\d\d-\d\d-\d\d\b", text), path.name
            assert "generated on" not in text.lower(), path.name


class TestStubsMatchTheData:
    """The stub is what the editor believes. It has to be true."""

    @pytest.fixture(scope="class")
    @classmethod
    def stub_names(cls):
        import pathlib
        import re

        path = pathlib.Path(enums.__file__).with_suffix(".pyi")
        text = path.read_text(encoding="utf-8")
        return set(re.findall(r"^class (\w+)\(IntEnum\):", text, re.M))

    def test_the_stub_declares_every_enumeration(self, stub_names):
        assert stub_names == set(enums.names())

    def test_the_const_stub_declares_every_constant(self):
        import pathlib
        import re

        path = pathlib.Path(const.__file__).with_suffix(".pyi")
        text = path.read_text(encoding="utf-8")
        declared = set(re.findall(r"^(\w+): int = ", text, re.M))
        assert declared == set(const.names())

    def test_the_stub_values_agree_with_the_data(self):
        import pathlib
        import re

        path = pathlib.Path(const.__file__).with_suffix(".pyi")
        text = path.read_text(encoding="utf-8")
        for name, value in re.findall(r"^(\w+): int = (-?\d+)$", text, re.M):
            assert getattr(const, name) == int(value), name
