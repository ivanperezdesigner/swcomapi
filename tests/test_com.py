"""The raw COM layer, exercised without SOLIDWORKS.

The SafeArray helpers and the error translation are pure functions over data,
so they are testable on their own. `com_error` is faked here rather than
provoked, because provoking one needs a live application.
"""

import pytest

from swcomapi import com
from swcomapi.errors import SwCallError, SwMemberNotFoundError


class FakeComError(Exception):
    """Stands in for pywintypes.com_error, which has exactly this args shape.

    args = (hresult, source_description, excepinfo, arg_index), and excepinfo
    is itself (wcode, source, description, help_file, help_context, scode).
    """


def com_error(hresult, source="", description=None):
    excepinfo = None if description is None else (0, "SldWorks", description, None, 0, 0)
    return FakeComError(hresult, source, excepinfo, None)


class TestToList:
    def test_none_is_empty(self):
        # SOLIDWORKS returns a null VARIANT for "nothing found", not an array.
        assert com.to_list(None) == []

    def test_tuple_becomes_list(self):
        assert com.to_list((1.0, 2.0, 3.0)) == [1.0, 2.0, 3.0]

    def test_list_is_copied_not_aliased(self):
        original = [1.0]
        result = com.to_list(original)
        result.append(2.0)
        assert original == [1.0]

    def test_scalar_becomes_one_item(self):
        # Several methods return the object directly when there is only one.
        assert com.to_list(3.0) == [3.0]
        assert com.to_list("Boss-Extrude1") == ["Boss-Extrude1"]

    def test_empty_tuple_stays_empty(self):
        assert com.to_list(()) == []


class TestToTuples:
    def test_a_getbox_result(self):
        """GetBox gives two corners as six metres, here a 25x40x10 mm box."""
        box = (0.0, 0.0, 0.0, 0.025, 0.04, 0.01)
        assert com.to_tuples(box, 3) == [(0.0, 0.0, 0.0), (0.025, 0.04, 0.01)]

    def test_a_coordinate_system(self):
        """GetCoordinateSystem gives three vectors as nine numbers."""
        nine = (1, 0, 0, 0, 1, 0, 0, 0, 1)
        assert com.to_tuples(nine, 3) == [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

    def test_none_is_empty(self):
        assert com.to_tuples(None, 3) == []

    def test_a_bad_length_is_an_error_not_a_silent_truncation(self):
        with pytest.raises(ValueError, match="cannot regroup 4 values into tuples of 3"):
            com.to_tuples((1.0, 2.0, 3.0, 4.0), 3)

    def test_size_one_is_a_no_op_regroup(self):
        assert com.to_tuples((1.0, 2.0), 1) == [(1.0,), (2.0,)]


class TestUnpack:
    def test_reads_the_hresult_unsigned(self):
        hresult, _ = com._unpack(com_error(-2147352570))
        assert hresult == 0xFFFFFFFF & -2147352570 == 0x80020006

    def test_prefers_the_excepinfo_description(self):
        exc = com_error(-2147352567, "SldWorks.Application", "Feature not found")
        _, detail = com._unpack(exc)
        assert detail == "Feature not found"

    def test_falls_back_to_the_source_description(self):
        exc = com_error(-2147352570, "Unknown name.")
        _, detail = com._unpack(exc)
        assert detail == "Unknown name."

    def test_survives_an_exception_with_no_args(self):
        assert com._unpack(Exception()) == (None, "")


class TestSigned:
    def test_round_trips_a_failure_hresult(self):
        assert com._signed(0x80020006) == -2147352570

    def test_leaves_a_success_hresult_alone(self):
        assert com._signed(0) == 0
        assert com._signed(1) == 1

    def test_none_stays_none(self):
        assert com._signed(None) is None


class TestTranslate:
    def test_unknown_name_becomes_member_not_found(self):
        """The case that matters: a method a newer SOLIDWORKS added."""
        error = com._translate(com_error(com.DISP_E_UNKNOWNNAME), "SaveAs99")
        assert isinstance(error, SwMemberNotFoundError)
        assert "SaveAs99" in str(error)
        assert "this SOLIDWORKS version" in str(error)
        assert error.member == "SaveAs99"

    def test_member_not_found_too(self):
        error = com._translate(com_error(com.DISP_E_MEMBERNOTFOUND), "Nope")
        assert isinstance(error, SwMemberNotFoundError)

    def test_member_not_found_is_also_an_attribute_error(self):
        # So that hasattr() and getattr(obj, name, default) keep working.
        error = com._translate(com_error(com.DISP_E_UNKNOWNNAME), "Nope")
        assert isinstance(error, AttributeError)

    def test_anything_else_becomes_a_call_error_with_the_hresult(self):
        error = com._translate(com_error(-2147352567, "", "Bad selection"), "InsertFeature")
        assert isinstance(error, SwCallError)
        assert not isinstance(error, SwMemberNotFoundError)
        assert "0x80020009" in str(error)
        assert "Bad selection" in str(error)
        assert error.hresult == 0x80020009
        assert error.detail == "Bad selection"

    def test_a_missing_hresult_still_produces_a_readable_message(self):
        error = com._translate(Exception(), "Something")
        assert str(error) == "'Something' failed"


class TestIsBusy:
    def test_call_rejected_is_busy(self):
        """0x80010001, what SOLIDWORKS says while it is still loading."""
        assert com.is_busy(com_error(com.RPC_E_CALL_REJECTED)) is True

    def test_retry_later_is_busy(self):
        assert com.is_busy(com_error(com.RPC_E_SERVERCALL_RETRYLATER)) is True

    def test_a_disconnected_object_is_not_busy_it_is_dead(self):
        assert com.is_busy(com_error(com.RPC_E_DISCONNECTED)) is False

    def test_a_normal_failure_is_not_busy(self):
        assert com.is_busy(com_error(com.DISP_E_UNKNOWNNAME)) is False

    def test_no_hresult_is_not_busy(self):
        assert com.is_busy(Exception()) is False


class TestVartypes:
    def test_the_constants_are_re_exported_so_nobody_imports_pythoncom(self):
        import pythoncom

        assert com.VT_I4 == pythoncom.VT_I4
        assert com.VT_R8 == pythoncom.VT_R8
        assert com.VT_BSTR == pythoncom.VT_BSTR
        assert com.VT_BYREF == pythoncom.VT_BYREF


class TestByref:
    def test_defaults_to_a_variant_flagged_byref(self):
        arg = com.byref()
        assert arg.varianttype == com.VT_BYREF | com.VT_VARIANT
        assert arg.value == 0

    def test_an_int_out_parameter(self):
        """The shape of OpenDoc6's errors and warnings."""
        arg = com.byref(com.VT_I4)
        assert arg.varianttype == com.VT_BYREF | com.VT_I4
        assert arg.value == 0

    def test_a_string_out_parameter_starts_empty_not_zero(self):
        arg = com.byref(com.VT_BSTR)
        assert arg.value == ""

    def test_an_explicit_initial_value_is_kept(self):
        assert com.byref(com.VT_I4, 7).value == 7

    def test_is_byref_recognises_it(self):
        assert com.is_byref(com.byref(com.VT_I4)) is True

    def test_is_byref_rejects_a_plain_value(self):
        assert com.is_byref(0) is False
        assert com.is_byref("C:/part.SLDPRT") is False
        assert com.is_byref(None) is False


class TestFromList:
    def test_builds_a_double_array_by_default(self):
        arg = com.from_list([0.0, 0.0, 0.0, 0.025, 0.0, 0.0])
        assert arg.varianttype == com.VT_ARRAY | com.VT_R8
        assert list(arg.value) == [0.0, 0.0, 0.0, 0.025, 0.0, 0.0]

    def test_accepts_any_iterable(self):
        arg = com.from_list(v / 1000 for v in (25, 40))
        assert list(arg.value) == [0.025, 0.04]


class FakeDispatch:
    """A stand-in for a COM object, to test `call` without SOLIDWORKS."""

    def __init__(self):
        self.Visible = True
        self.calls = []
        self.mass_args = None

    def GetProcessID(self):
        self.calls.append("GetProcessID")
        return 12345

    def OpenDoc6(self, path, doc_type, options, config, errors, warnings):
        self.calls.append("OpenDoc6")
        errors.value = 0
        warnings.value = 128
        return "a-model-doc"

    def GetBuildNumbers2(self, base, current, hotfixes):
        self.calls.append("GetBuildNumbers2")
        base.value = "sw2026_SP03"
        current.value = "d260519.003"
        hotfixes.value = ""

    def GetMassProperties2(self, accuracy, status, use_selected):
        self.calls.append("GetMassProperties2")
        self.mass_args = (accuracy, use_selected)
        status.value = 0
        return [0.0, 0.0, 0.0, 5e-05, 0.01, 0.135]

    def Explodes(self):
        raise com_error(-2147352567, "", "Nope")


class TestCall:
    def test_calls_a_method(self):
        obj = FakeDispatch()
        assert com.call(obj, "GetProcessID") == 12345
        assert obj.calls == ["GetProcessID"]

    def test_reads_a_property_that_is_not_callable(self):
        assert com.call(FakeDispatch(), "Visible") is True

    def test_a_missing_member_is_a_member_not_found_error(self):
        with pytest.raises(SwMemberNotFoundError, match="no member 'Nonexistent'"):
            com.call(FakeDispatch(), "Nonexistent")


class TestCallOut:
    """`call_out` now builds the [out] arguments itself, from the generated
    signature table, so these check the interleaving rather than the plumbing.
    """

    def test_it_supplies_the_out_parameters_and_names_them(self, monkeypatch):
        """OpenDoc6's real shape: four arguments in, two [in,out] codes back.

        The caller passes four; SOLIDWORKS wants six. The warning 128 is
        swFileLoadWarning_AlreadyOpen, which is what you get opening a file
        the session already has open.
        """
        monkeypatch.setattr(com.pythoncom, "com_error", FakeComError, raising=False)

        obj = FakeDispatch()
        result, out = com.call_out(
            obj, "OpenDoc6", "C:/parts/bracket.SLDPRT", 1, 0, ""
        )
        assert result == "a-model-doc"
        assert out == {"Errors": 0, "Warnings": 128}

    def test_a_pure_out_parameter_in_the_middle_is_inserted_not_overwritten(
        self, monkeypatch
    ):
        """IModelDocExtension.GetMassProperties2(Accuracy, Status, UseSelected).

        Status sits between the two real arguments. Overwriting position 1
        instead of inserting there was a real bug: UseSelected was silently
        replaced by the output holder.
        """
        monkeypatch.setattr(com.pythoncom, "com_error", FakeComError, raising=False)

        obj = FakeDispatch()
        result, out = com.call_out(
            obj, "GetMassProperties2", 1, True, interface="IModelDocExtension"
        )
        assert out == {"Status": 0}
        assert result == [0.0, 0.0, 0.0, 5e-05, 0.01, 0.135]
        # The arguments either side arrived intact.
        assert obj.mass_args == (1, True)

    def test_no_out_parameters_gives_an_empty_dict(self):
        result, out = com.call_out(FakeDispatch(), "GetProcessID")
        assert result == 12345
        assert out == {}

    def test_the_wrong_number_of_arguments_says_what_it_wants(self):
        from swcomapi.errors import SwAmbiguousMemberError

        with pytest.raises(SwAmbiguousMemberError, match="does not take 2 argument"):
            com.call_out(FakeDispatch(), "GetBuildNumbers2", 1, 2)


class TestNeedsCalling:
    """Why `call` cannot decide with ``callable()``.

    Late binding hands back an already-evaluated value for some zero-argument
    members and a method still waiting to be called for others. A CDispatch is
    callable but must not be called; a str is not callable at all.
    """

    def test_a_value_does_not_need_calling(self):
        assert com.needs_calling(True) is False
        assert com.needs_calling("Part1.SLDPRT") is False
        assert com.needs_calling(1) is False
        assert com.needs_calling((1.0, 2.0)) is False

    def test_a_com_object_does_not_either_even_though_it_is_callable(self):
        class FakeCDispatch:
            def __call__(self):
                raise AssertionError("this must never be called")

        obj = FakeCDispatch()
        assert callable(obj) is True
        assert com.needs_calling(obj) is False

    def test_a_bound_method_does(self):
        assert com.needs_calling(FakeDispatch().GetProcessID) is True

    def test_a_builtin_does(self):
        assert com.needs_calling(len) is True


class TestCallWithAnAlreadyEvaluatedMember:
    def test_passing_arguments_to_one_is_a_clear_error(self):
        """Rather than "'bool' object is not callable" three frames down."""
        from swcomapi.errors import SwCallError

        with pytest.raises(SwCallError, match="already evaluated"):
            com.call(FakeDispatch(), "Visible", 1)
