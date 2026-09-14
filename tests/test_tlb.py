"""The type library reader.

The pure functions - parameter direction, VARTYPE mapping, the C++-twin
detection, the reserved-member filter - are tested here with no type library
involved. Reading a real one is in `tests/live/test_tlb_live.py`.
"""

import pytest

from swcomapi.tools import tlb


class TestDirectionOf:
    def test_in(self):
        assert tlb.direction_of(tlb.PARAMFLAG_FIN) == "in"

    def test_out(self):
        """GetBuildNumbers2's three parameters carry flags == 2."""
        assert tlb.direction_of(tlb.PARAMFLAG_FOUT) == "out"

    def test_inout(self):
        """OpenDoc6's Errors and Warnings carry flags == 3."""
        assert tlb.direction_of(tlb.PARAMFLAG_FIN | tlb.PARAMFLAG_FOUT) == "inout"

    def test_no_flags_at_all_counts_as_in(self):
        # 405 parameters in sldworks.tlb have flags == 0.
        assert tlb.direction_of(0) == "in"

    def test_other_flags_do_not_confuse_it(self):
        flags = tlb.PARAMFLAG_FIN | tlb.PARAMFLAG_FOPT | tlb.PARAMFLAG_FHASDEFAULT
        assert tlb.direction_of(flags) == "in"


class TestIsReserved:
    @pytest.mark.parametrize(
        ("memid", "member"),
        [
            (0x60000000, "QueryInterface"),
            (0x60000001, "AddRef"),
            (0x60000002, "Release"),
            (0x60010000, "GetTypeInfoCount"),
            (0x60010003, "Invoke"),
        ],
    )
    def test_the_idispatch_plumbing_is_reserved(self, memid, member):
        assert tlb.is_reserved(memid), member

    @pytest.mark.parametrize(("memid", "member"), [(7, "CloseDoc"), (12, "RevisionNumber"),
                                                   (167, "OpenDoc6"), (303, "GetBuildNumbers2")])
    def test_real_api_members_are_not(self, memid, member):
        assert not tlb.is_reserved(memid), member

    def test_an_enum_member_id_is_not_reserved(self):
        # Enum members sit at 0x40000000 and up.
        assert not tlb.is_reserved(1073741824)


class TestOutVartype:
    def test_a_long_out_parameter(self):
        """OpenDoc6's Errors: PTR to VT_I4."""
        assert tlb.out_vartype((tlb.VT_PTR, tlb.VT_I4)) == tlb.VT_I4

    def test_a_string_out_parameter(self):
        """GetBuildNumbers2's three: PTR to VT_BSTR."""
        assert tlb.out_vartype((tlb.VT_PTR, tlb.VT_BSTR)) == tlb.VT_BSTR

    def test_a_double_out_parameter(self):
        assert tlb.out_vartype((tlb.VT_PTR, tlb.VT_R8)) == tlb.VT_R8

    def test_a_boolean_out_parameter(self):
        assert tlb.out_vartype((tlb.VT_PTR, tlb.VT_BOOL)) == tlb.VT_BOOL

    def test_a_variant_out_parameter(self):
        assert tlb.out_vartype((tlb.VT_PTR, tlb.VT_VARIANT)) == tlb.VT_VARIANT

    @pytest.mark.parametrize("target", [tlb.VT_INT, tlb.VT_UINT, tlb.VT_UI4])
    def test_types_with_no_variant_form_widen_to_i4(self, target):
        """VT_INT and VT_UINT cannot travel in a VARIANT; VT_I4 can."""
        assert tlb.out_vartype((tlb.VT_PTR, target)) == tlb.VT_I4

    @pytest.mark.parametrize("target", [tlb.VT_UI2, tlb.VT_I1, tlb.VT_UI1])
    def test_the_small_integers_widen_to_i2(self, target):
        assert tlb.out_vartype((tlb.VT_PTR, target)) == tlb.VT_I2

    def test_an_out_object_comes_back_as_dispatch(self):
        assert tlb.out_vartype((tlb.VT_PTR, (tlb.VT_USERDEFINED, 0))) == tlb.VT_DISPATCH

    def test_a_pointer_to_a_pointer_to_an_object_too(self):
        nested = (tlb.VT_PTR, (tlb.VT_PTR, (tlb.VT_USERDEFINED, 0)))
        assert tlb.out_vartype(nested) == tlb.VT_DISPATCH

    def test_a_bare_type_is_taken_as_the_target(self):
        # Defensive: an [out] parameter is always a pointer, but if one is not,
        # the type itself is the best answer.
        assert tlb.out_vartype(tlb.VT_I4) == tlb.VT_I4

    def test_void_becomes_variant(self):
        # PTR->VOID means "an object of unspecified type".
        assert tlb.out_vartype((tlb.VT_PTR, tlb.VT_VOID)) == tlb.VT_VARIANT


class FakeTypeInfo:
    """Stands in for an ITypeInfo, for resolving VT_USERDEFINED references."""

    def __init__(self, names=None):
        self.names = names or {}

    def GetRefTypeInfo(self, href):
        name = self.names[href]
        return FakeResolved(name)


class FakeResolved:
    def __init__(self, name):
        self.name = name

    def GetDocumentation(self, index):
        return (self.name, "", 0, "")


class TestTypeInfo:
    def test_a_bare_vartype(self):
        result = tlb.type_info(tlb.VT_BSTR, FakeTypeInfo())
        assert result == {"vt": tlb.VT_BSTR, "com": "BSTR", "py": "str"}

    def test_a_double(self):
        result = tlb.type_info(tlb.VT_R8, FakeTypeInfo())
        assert result["com"] == "double"
        assert result["py"] == "float"

    def test_a_variant_is_any_because_it_really_could_be_anything(self):
        """SOLIDWORKS puts SafeArrays, single objects and scalars in VARIANTs.

        Promising anything narrower would be a lie, which is why
        `swcomapi.com.to_list` exists.
        """
        assert tlb.type_info(tlb.VT_VARIANT, FakeTypeInfo())["py"] == "Any"

    def test_void_is_none(self):
        assert tlb.type_info(tlb.VT_VOID, FakeTypeInfo())["py"] == "None"

    def test_a_user_defined_type_resolves_to_its_name(self):
        info = FakeTypeInfo({50333824: "IModelDoc2"})
        result = tlb.type_info((tlb.VT_USERDEFINED, 50333824), info)
        assert result["com"] == "IModelDoc2"
        assert result["py"] == "IModelDoc2"
        assert result["interface"] == "IModelDoc2"

    def test_an_enum_reference_is_not_treated_as_an_interface_type(self):
        """swDocumentTypes_e is a user-defined type but not an interface."""
        info = FakeTypeInfo({1: "swDocumentTypes_e"})
        result = tlb.type_info((tlb.VT_USERDEFINED, 1), info)
        assert result["com"] == "swDocumentTypes_e"
        assert result["py"] == "Any"
        assert result["interface"] == "swDocumentTypes_e"

    def test_a_pointer_to_an_interface(self):
        """OpenDoc6's return type: PTR to USERDEFINED IModelDoc2."""
        info = FakeTypeInfo({50333824: "IModelDoc2"})
        result = tlb.type_info((tlb.VT_PTR, (tlb.VT_USERDEFINED, 50333824)), info)
        assert result["com"] == "IModelDoc2*"
        # A pointer is COM's spelling of "by reference"; Python gets the thing.
        assert result["py"] == "IModelDoc2"
        assert result["interface"] == "IModelDoc2"

    def test_a_pointer_to_a_long(self):
        result = tlb.type_info((tlb.VT_PTR, tlb.VT_I4), FakeTypeInfo())
        assert result["com"] == "long*"
        assert result["py"] == "int"

    def test_a_safearray(self):
        result = tlb.type_info((tlb.VT_SAFEARRAY, tlb.VT_R8), FakeTypeInfo())
        assert result["com"] == "SAFEARRAY(double)"
        assert result["py"] == "list[float]"

    def test_an_unknown_head_degrades_to_any_rather_than_raising(self):
        result = tlb.type_info((99, 0), FakeTypeInfo())
        assert result["py"] == "Any"


class TestMarkComOnly:
    def test_the_i_prefixed_twin_is_marked(self):
        """GetMassProperties is usable from Python; IGetMassProperties is not."""
        members = [
            {"name": "GetMassProperties", "kind": "method", "com_only": False},
            {"name": "IGetMassProperties", "kind": "method", "com_only": False},
        ]
        tlb._mark_com_only(members)
        assert members[0]["com_only"] is False
        assert members[1]["com_only"] is True

    def test_a_lone_i_name_is_left_alone(self):
        """Plenty of real methods start with I and have no twin."""
        members = [
            {"name": "InsertSketch", "kind": "method", "com_only": False},
            {"name": "IsOpenNotifySpecified", "kind": "method", "com_only": False},
        ]
        tlb._mark_com_only(members)
        assert all(m["com_only"] is False for m in members)

    def test_the_twin_must_be_the_same_kind(self):
        """A property named X does not make a method named IX a twin."""
        members = [
            {"name": "Extension", "kind": "get", "com_only": False},
            {"name": "IExtension", "kind": "method", "com_only": False},
        ]
        tlb._mark_com_only(members)
        assert members[1]["com_only"] is False

    def test_a_lowercase_second_letter_is_not_a_twin_prefix(self):
        members = [
            {"name": "sMethod", "kind": "method", "com_only": False},
            {"name": "IsMethod", "kind": "method", "com_only": False},
        ]
        tlb._mark_com_only(members)
        assert members[1]["com_only"] is False


class TestConstantTables:
    def test_every_vartype_with_a_com_name_has_a_python_name(self):
        assert set(tlb.VT_COM_NAMES) == set(tlb.VT_PY_NAMES)

    def test_the_invkinds_cover_what_the_libraries_use(self):
        # The census over sldworks.tlb found only these three.
        for invkind in (tlb.INVOKE_FUNC, tlb.INVOKE_PROPERTYGET, tlb.INVOKE_PROPERTYPUT):
            assert invkind in tlb.INVKIND_NAMES

    def test_the_reserved_range_is_the_right_way_round(self):
        assert tlb.RESERVED_MEMID_LOW < tlb.RESERVED_MEMID_HIGH
