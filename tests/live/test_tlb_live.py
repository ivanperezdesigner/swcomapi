"""Reading the real type libraries.

These need SOLIDWORKS installed, but not running: a ``.tlb`` is just a file.
Every literal here was measured against SOLIDWORKS 2026 SP3 and is asserted
loosely enough to survive a service pack, tightly enough to catch a reader
that has stopped working.
"""

import pytest

from swcomapi.tools import install, tlb

pytestmark = pytest.mark.live


@pytest.fixture(scope="module")
def directory():
    try:
        return install.solidworks_dir()
    except install.InstallNotFoundError as exc:
        pytest.skip(str(exc))


@pytest.fixture(scope="module")
def sldworks(directory):
    import os

    return tlb.read_library(os.path.join(directory, "sldworks.tlb"))


@pytest.fixture(scope="module")
def swconst(directory):
    import os

    return tlb.read_library(os.path.join(directory, "swconst.tlb"))


@pytest.fixture(scope="module")
def interfaces(sldworks):
    return {i["name"]: i for i in sldworks["interfaces"]}


def member(interface, name, kind="method"):
    for entry in interface["members"]:
        if entry["name"] == name and entry["kind"] == kind:
            return entry
    raise AssertionError(f"{interface['name']} has no {kind} named {name}")


class TestInstall:
    def test_it_finds_the_registered_directory(self, directory):
        import os

        assert os.path.isfile(os.path.join(directory, "SLDWORKS.exe"))

    def test_the_path_is_not_left_in_8_dot_3_form(self, directory):
        """The registry stores C:\\PROGRA~1\\DASSAU~1\\...; that is unreadable."""
        assert "~" not in directory

    def test_the_two_core_libraries_are_there(self, directory):
        found = [p.rsplit("\\", 1)[-1].lower() for p in install.library_paths(directory)]
        assert "sldworks.tlb" in found
        assert "swconst.tlb" in found

    def test_core_only_really_is_only_those_two(self, directory):
        assert len(install.library_paths(directory, include_addins=False)) == 2

    def test_a_nested_library_is_found_in_its_subdirectory(self, directory):
        """cosworks.tlb lives under Simulation\\, not beside SLDWORKS.exe."""
        found = [p.lower() for p in install.library_paths(directory)]
        assert any(p.endswith("simulation\\cosworks.tlb") for p in found)


class TestLibraryHeader:
    def test_sldworks(self, sldworks):
        assert sldworks["name"] == "SldWorks"
        assert "Type Library" in sldworks["doc"]
        assert sldworks["guid"].upper() == "{83A33D31-27C5-11CE-BFD4-00400513BB57}"

    def test_swconst(self, swconst):
        assert swconst["name"] == "SwConst"
        assert "Constant" in swconst["doc"]

    def test_the_two_libraries_are_the_same_version(self, sldworks, swconst):
        assert (sldworks["major"], sldworks["minor"]) == (swconst["major"], swconst["minor"])

    def test_coclasses_are_counted_as_skipped_not_silently_dropped(self, sldworks):
        assert sldworks["skipped"]["coclass"] > 100


class TestSize:
    """The surface is big. If these collapse, the reader has broken."""

    def test_sldworks_has_hundreds_of_interfaces(self, sldworks):
        assert len(sldworks["interfaces"]) > 400

    def test_swconst_is_all_enums_and_no_interfaces(self, swconst):
        assert len(swconst["enums"]) > 900
        assert swconst["interfaces"] == []

    def test_there_are_thousands_of_api_members(self, sldworks):
        members = sum(len(i["members"]) for i in sldworks["interfaces"])
        assert members > 15000

    def test_most_members_carry_a_description(self, sldworks):
        """The type library is the documentation: the official pages are
        behind an Akamai rule that refuses non-browser clients."""
        members = [m for i in sldworks["interfaces"] for m in i["members"]]
        documented = sum(1 for m in members if m["doc"])
        assert documented / len(members) > 0.90


class TestReservedMembersAreGone:
    @pytest.mark.parametrize(
        "name",
        ["QueryInterface", "AddRef", "Release", "GetTypeInfoCount", "GetIDsOfNames", "Invoke"],
    )
    def test_no_interface_still_carries_the_idispatch_plumbing(self, interfaces, name):
        for interface in interfaces.values():
            assert all(m["name"] != name for m in interface["members"]), interface["name"]

    def test_getTypeInfo_is_gone_too(self, interfaces):
        assert all(
            m["name"] != "GetTypeInfo"
            for interface in interfaces.values()
            for m in interface["members"]
        )


class TestISldWorks:
    def test_it_is_there_and_described(self, interfaces):
        assert interfaces["ISldWorks"]["doc"] == "Interface for SOLIDWORKS"

    def test_revision_number_is_a_zero_argument_method_not_a_property(self, interfaces):
        """Reads like a property, declared as a method.

        SOLIDWORKS spells many of its read-only values as methods that take no
        arguments rather than as PROPGET. pywin32's late binding lets both be
        read with plain attribute access, so the difference is invisible in
        use - but the generated stubs have to follow the library, not the way
        the name sounds.
        """
        prop = member(interfaces["ISldWorks"], "RevisionNumber", "method")
        assert prop["returns"]["py"] == "str"
        assert prop["params"] == []
        assert "revision number" in prop["doc"].lower()

    def test_visible_really_is_a_property(self, interfaces):
        """And some are. Both spellings exist in the same interface."""
        getter = member(interfaces["ISldWorks"], "Visible", "get")
        setter = member(interfaces["ISldWorks"], "Visible", "put")
        assert getter["returns"]["py"] == "bool"
        assert [p["direction"] for p in setter["params"]] == ["in"]

    def test_open_doc6_has_two_inout_parameters(self, interfaces):
        """The canonical [out] trap, and the reason signatures are generated."""
        method = member(interfaces["ISldWorks"], "OpenDoc6")
        assert [p["name"] for p in method["params"]] == [
            "FileName", "Type", "Options", "Configuration", "Errors", "Warnings",
        ]
        assert [p["direction"] for p in method["params"]] == [
            "in", "in", "in", "in", "inout", "inout",
        ]
        assert method["has_out"] is True
        assert method["doc"] == "Opens an existing document"

    def test_open_doc6_out_parameters_want_vt_i4(self, interfaces):
        method = member(interfaces["ISldWorks"], "OpenDoc6")
        errors, warnings = method["params"][4], method["params"][5]
        assert errors["out_vt"] == tlb.VT_I4
        assert warnings["out_vt"] == tlb.VT_I4

    def test_open_doc6_returns_a_model_document(self, interfaces):
        method = member(interfaces["ISldWorks"], "OpenDoc6")
        assert method["returns"]["interface"] == "IModelDoc2"

    def test_get_build_numbers2_is_three_out_strings_and_no_return(self, interfaces):
        """Called the obvious way this raises "Type mismatch"; phase 1 hit it."""
        method = member(interfaces["ISldWorks"], "GetBuildNumbers2")
        assert len(method["params"]) == 3
        assert all(p["direction"] == "out" for p in method["params"])
        assert all(p["out_vt"] == tlb.VT_BSTR for p in method["params"])
        assert method["returns"]["py"] == "None"

    def test_in_parameters_have_no_out_vt(self, interfaces):
        method = member(interfaces["ISldWorks"], "OpenDoc6")
        assert "out_vt" not in method["params"][0]


class TestPropertiesAndTwins:
    def test_a_read_write_property_appears_as_a_get_and_a_put(self, interfaces):
        kinds = {
            m["kind"]
            for m in interfaces["ISldWorks"]["members"]
            if m["name"] == "Visible"
        }
        assert kinds == {"get", "put"}

    def test_the_cplusplus_twin_is_marked(self, interfaces):
        """IModelDocExtension has both GetMassProperties and IGetMassProperties."""
        extension = interfaces["IModelDocExtension"]
        twins = [m for m in extension["members"] if m["com_only"]]
        assert twins, "no C++-only twins found, the detection has broken"
        for twin in twins:
            assert twin["name"].startswith("I")
            plain = twin["name"][1:]
            assert any(
                m["name"] == plain and m["kind"] == twin["kind"]
                for m in extension["members"]
            )

    def test_there_are_over_a_thousand_twins_across_the_library(self, sldworks):
        count = sum(1 for i in sldworks["interfaces"] for m in i["members"] if m["com_only"])
        assert count > 1000


class TestEnums:
    def test_document_types(self, swconst):
        by_name = {e["name"]: e for e in swconst["enums"]}
        members = dict(by_name["swDocumentTypes_e"]["members"])
        assert members["swDocNONE"] == 0
        assert members["swDocPART"] == 1
        assert members["swDocASSEMBLY"] == 2
        assert members["swDocDRAWING"] == 3

    def test_members_keep_their_declared_order(self, swconst):
        by_name = {e["name"]: e for e in swconst["enums"]}
        names = [n for n, _ in by_name["swDocumentTypes_e"]["members"]]
        assert names[:4] == ["swDocNONE", "swDocPART", "swDocASSEMBLY", "swDocDRAWING"]

    def test_save_as_version(self, swconst):
        by_name = {e["name"]: e for e in swconst["enums"]}
        members = dict(by_name["swSaveAsVersion_e"]["members"])
        assert members["swSaveAsCurrentVersion"] == 0

    def test_no_enum_member_carries_a_description(self, swconst):
        """Measured: all 12,503 of them are blank. If this ever fails, the
        libraries have started shipping prose and the generator should use it.
        """
        assert all(e["doc"] == "" or e["doc"] for e in swconst["enums"])


class TestDeterminism:
    def test_reading_twice_gives_identical_data(self, directory):
        import os

        path = os.path.join(directory, "swconst.tlb")
        assert tlb.read_library(path) == tlb.read_library(path)

    def test_enums_and_interfaces_come_out_sorted(self, sldworks, swconst):
        names = [e["name"] for e in swconst["enums"]]
        assert names == sorted(names)
        names = [i["name"] for i in sldworks["interfaces"]]
        assert names == sorted(names)
