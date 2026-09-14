"""The generator, on made-up libraries.

Emission and the safety checks are tested against hand-built data, so they run
without SOLIDWORKS. Running the generator against the real install is in
`tests/live/test_generate_live.py`, which also proves the output is
reproducible.
"""

import pytest

from swcomapi.tools import generate


def api(enums=None, interfaces=None, libraries=None, failed=None, year=2026):
    """A minimal gather() result, for the emitters."""
    return {
        "libraries": libraries
        if libraries is not None
        else [
            {
                "name": "SldWorks",
                "file": "sldworks.tlb",
                "guid": "{83A33D31-27C5-11CE-BFD4-00400513BB57}",
                "major": 34,
                "minor": 0,
                "doc": "SldWorks 2026 Type Library",
            }
        ],
        "enums": enums if enums is not None else {},
        "interfaces": interfaces if interfaces is not None else {},
        "failed": failed if failed is not None else [],
        "year": year,
    }


def enum(members, library="SwConst", doc=""):
    return {"members": members, "library": library, "guid": "{0}", "doc": doc}


DOC_TYPES = enum([("swDocNONE", 0), ("swDocPART", 1), ("swDocASSEMBLY", 2)])


class TestReleaseYear:
    def test_it_comes_from_sldworks_tlb(self):
        libraries = [
            # Simulation versions itself separately: major 19 for the same
            # 2026 release. Taking the first library read would say nothing.
            {"file": "cosworks.tlb", "major": 19, "minor": 0, "name": "x", "guid": "", "doc": ""},
            {"file": "sldworks.tlb", "major": 34, "minor": 0, "name": "y", "guid": "", "doc": ""},
        ]
        assert generate._release_year(libraries) == 2026

    def test_the_order_of_the_libraries_does_not_matter(self):
        libraries = [
            {"file": "sldworks.tlb", "major": 34, "minor": 0, "name": "y", "guid": "", "doc": ""},
            {"file": "cosworks.tlb", "major": 19, "minor": 0, "name": "x", "guid": "", "doc": ""},
        ]
        assert generate._release_year(libraries) == 2026

    def test_without_sldworks_tlb_there_is_no_answer(self):
        libraries = [
            {"file": "cosworks.tlb", "major": 19, "minor": 0, "name": "x", "guid": "", "doc": ""}
        ]
        assert generate._release_year(libraries) is None

    def test_the_filename_match_is_case_insensitive(self):
        libraries = [
            {"file": "SLDWORKS.TLB", "major": 34, "minor": 0, "name": "y", "guid": "", "doc": ""}
        ]
        assert generate._release_year(libraries) == 2026


class TestAddEnum:
    def test_the_same_definition_twice_is_fine(self):
        """swpublished.tlb republishes parts of swconst.tlb."""
        enums = {}
        generate._add_enum(enums, {"name": "E", "members": [("A", 1)], "guid": "", "doc": ""}, "L1")
        generate._add_enum(enums, {"name": "E", "members": [("A", 1)], "guid": "", "doc": ""}, "L2")
        assert enums["E"]["library"] == "L1"

    def test_two_different_definitions_is_a_refusal_not_a_coin_toss(self):
        enums = {}
        generate._add_enum(enums, {"name": "E", "members": [("A", 1)], "guid": "", "doc": ""}, "L1")
        with pytest.raises(generate.GenerationError, match="defined differently in L1 and L2"):
            generate._add_enum(
                enums, {"name": "E", "members": [("A", 2)], "guid": "", "doc": ""}, "L2"
            )


class TestCheck:
    def test_clean_data_passes(self):
        generate.check(api(enums={"swDocumentTypes_e": DOC_TYPES}))

    def test_a_constant_that_means_two_things_is_refused(self):
        """What would make the flat namespace in swcomapi.const a lie."""
        enums = {
            "A_e": enum([("swThing", 1)]),
            "B_e": enum([("swThing", 2)]),
        }
        with pytest.raises(generate.GenerationError, match="means 1 in A_e but 2 in B_e"):
            generate.check(api(enums=enums))

    def test_the_same_constant_with_the_same_value_is_allowed(self):
        enums = {"A_e": enum([("swThing", 1)]), "B_e": enum([("swThing", 1)])}
        generate.check(api(enums=enums))

    def test_a_constant_name_that_is_not_an_identifier_is_refused(self):
        enums = {"A_e": enum([("not a name", 1)])}
        with pytest.raises(generate.GenerationError, match="not a valid Python identifier"):
            generate.check(api(enums=enums))

    def test_an_enum_name_that_is_not_an_identifier_is_refused(self):
        with pytest.raises(generate.GenerationError, match="not a valid Python identifier"):
            generate.check(api(enums={"not an enum": enum([("A", 1)])}))

    def test_a_duplicated_member_name_is_refused(self):
        enums = {"A_e": enum([("swThing", 1), ("swThing", 2)])}
        with pytest.raises(generate.GenerationError, match="declares 'swThing' twice"):
            generate.check(api(enums=enums))


class TestCounts:
    def test_it_counts_constants_across_every_enumeration(self):
        numbers = generate.counts(
            api(enums={"A_e": enum([("a", 1), ("b", 2)]), "B_e": enum([("c", 3)])})
        )
        assert numbers["enums"] == 2
        assert numbers["constants"] == 3

    def test_it_counts_members_documented_properties_and_out_parameters(self):
        interfaces = {
            "IThing": {
                "name": "IThing",
                "doc": "",
                "guid": "",
                "kind": "dispatch",
                "library": "SldWorks",
                "members": [
                    {"name": "A", "kind": "method", "doc": "does a", "has_out": True,
                     "com_only": False},
                    {"name": "B", "kind": "get", "doc": "", "has_out": False,
                     "com_only": False},
                    {"name": "IA", "kind": "method", "doc": "does a", "has_out": False,
                     "com_only": True},
                ],
            }
        }
        numbers = generate.counts(api(interfaces=interfaces))
        assert numbers["interfaces"] == 1
        assert numbers["members"] == 3
        assert numbers["documented"] == 2
        assert numbers["properties"] == 1
        assert numbers["with_out"] == 1
        assert numbers["com_only"] == 1


class TestEmitEnumData:
    @pytest.fixture
    def source(self):
        return generate.emit_enum_data(api(enums={"swDocumentTypes_e": DOC_TYPES}))

    def test_it_is_importable_python(self, source):
        namespace = {}
        exec(compile(source, "_enum_data.py", "exec"), namespace)
        assert namespace["ENUMS"]["swDocumentTypes_e"]["swDocPART"] == 1
        assert namespace["ENUM_LIBRARY"]["swDocumentTypes_e"] == "SwConst"

    def test_members_keep_their_declared_order(self, source):
        namespace = {}
        exec(compile(source, "_enum_data.py", "exec"), namespace)
        members = list(namespace["ENUMS"]["swDocumentTypes_e"])
        assert members == ["swDocNONE", "swDocPART", "swDocASSEMBLY"]

    def test_it_says_not_to_edit_it(self, source):
        assert "Do not edit" in source

    def test_negative_values_survive(self):
        source = generate.emit_enum_data(api(enums={"A_e": enum([("swBad", -1)])}))
        namespace = {}
        exec(compile(source, "_enum_data.py", "exec"), namespace)
        assert namespace["ENUMS"]["A_e"]["swBad"] == -1


class TestEmitStubs:
    def test_the_enum_stub_compiles(self):
        source = generate.emit_enums_stub(api(enums={"swDocumentTypes_e": DOC_TYPES}))
        compile(source, "enums.pyi", "exec")

    def test_enum_members_are_left_unannotated(self):
        """The typing spec requires bare assignments for enum members in a
        stub; mypy rejects `swDocPART: int = 1`."""
        source = generate.emit_enums_stub(api(enums={"swDocumentTypes_e": DOC_TYPES}))
        assert "    swDocPART = 1" in source
        assert "swDocPART: int" not in source

    def test_an_empty_enumeration_still_produces_a_valid_class(self):
        source = generate.emit_enums_stub(api(enums={"Empty_e": enum([])}))
        compile(source, "enums.pyi", "exec")
        assert "class Empty_e(IntEnum):" in source
        assert "    ..." in source

    def test_the_const_stub_compiles_and_is_annotated(self):
        source = generate.emit_const_stub(api(enums={"swDocumentTypes_e": DOC_TYPES}))
        compile(source, "const.pyi", "exec")
        assert "swDocPART: int = 1" in source

    def test_the_const_stub_says_which_enumeration_each_block_is(self):
        source = generate.emit_const_stub(api(enums={"swDocumentTypes_e": DOC_TYPES}))
        assert "# swDocumentTypes_e (SwConst)" in source


class TestEmitMeta:
    def test_it_compiles_and_reports_the_release(self):
        namespace = {}
        source = generate.emit_meta(api(enums={"swDocumentTypes_e": DOC_TYPES}))
        exec(compile(source, "_meta.py", "exec"), namespace)
        assert namespace["SOLIDWORKS_YEAR"] == 2026
        assert namespace["LIBRARIES"][0]["file"] == "sldworks.tlb"
        assert namespace["COUNTS"]["constants"] == 3

    def test_an_empty_unreadable_list_is_annotated_for_mypy(self):
        source = generate.emit_meta(api())
        assert "UNREADABLE: list[tuple[str, str]] = []" in source

    def test_a_library_that_would_not_load_is_recorded_not_hidden(self):
        source = generate.emit_meta(api(failed=[("cosworks.tlb", "Error loading")]))
        namespace = {}
        exec(compile(source, "_meta.py", "exec"), namespace)
        assert namespace["UNREADABLE"] == [("cosworks.tlb", "Error loading")]


class TestEmitGeneratedInit:
    def test_it_compiles_and_states_the_sizes(self):
        source = generate.emit_generated_init(api(enums={"swDocumentTypes_e": DOC_TYPES}))
        compile(source, "__init__.py", "exec")
        assert "3 constants" in source
        assert "Do not edit" in source


class TestProvenanceLine:
    def test_it_names_the_release_and_the_libraries(self):
        line = generate._source_line(api())
        assert "SOLIDWORKS 2026" in line
        assert "sldworks.tlb" in line

    def test_it_carries_no_path_and_no_date(self):
        """Either would make the output differ between machines or runs."""
        line = generate._source_line(api())
        assert ":\\" not in line
        assert "Program Files" not in line

    def test_a_long_list_of_libraries_is_wrapped(self):
        libraries = [
            {"name": f"L{i}", "file": f"library{i}.tlb", "guid": "", "major": 34,
             "minor": 0, "doc": ""}
            for i in range(12)
        ]
        line = generate._source_line(api(libraries=libraries))
        assert all(len(part) <= 100 for part in line.splitlines())

    def test_an_unknown_year_says_so_rather_than_guessing(self):
        assert "unknown" in generate._source_line(api(year=None))


class TestWrite:
    def test_it_writes_every_file_where_it_belongs(self, tmp_path):
        import os

        written = generate.write(api(enums={"swDocumentTypes_e": DOC_TYPES}), str(tmp_path))
        names = {os.path.relpath(path, tmp_path).replace(os.sep, "/") for path, _ in written}
        assert names == {
            "const.pyi",
            "enums.pyi",
            "generated/__init__.py",
            "generated/_enum_data.py",
            "generated/_meta.py",
        }

    def test_the_stubs_sit_beside_the_modules_they_describe(self, tmp_path):
        """A .pyi only shadows its .py when it is the same directory and name.

        enums.py and const.py are hand written and live in the package root,
        so their stubs have to go there too - not into generated/.
        """
        generate.write(api(enums={"swDocumentTypes_e": DOC_TYPES}), str(tmp_path))
        assert (tmp_path / "enums.pyi").is_file()
        assert (tmp_path / "const.pyi").is_file()
        assert not (tmp_path / "generated" / "enums.pyi").exists()

    def test_it_writes_unix_newlines_whatever_the_platform(self, tmp_path):
        """So that the committed output does not depend on git's autocrlf."""
        generate.write(api(enums={"swDocumentTypes_e": DOC_TYPES}), str(tmp_path))
        raw = (tmp_path / "generated" / "_enum_data.py").read_bytes()
        assert b"\r\n" not in raw

    def test_it_writes_utf8(self, tmp_path):
        generate.write(api(enums={"swDocumentTypes_e": DOC_TYPES}), str(tmp_path))
        (tmp_path / "generated" / "_meta.py").read_text(encoding="utf-8")

    def test_writing_twice_produces_identical_bytes(self, tmp_path):
        data = api(enums={"swDocumentTypes_e": DOC_TYPES})
        generate.write(data, str(tmp_path))
        first = (tmp_path / "generated" / "_enum_data.py").read_bytes()
        generate.write(data, str(tmp_path))
        assert (tmp_path / "generated" / "_enum_data.py").read_bytes() == first


class TestGatherRefusesNothing:
    def test_no_libraries_at_all_is_an_error_with_a_way_out(self):
        with pytest.raises(generate.GenerationError, match="SWCOMAPI_SOLIDWORKS_DIR"):
            generate.gather([])
