"""The application wrapper, on a fake COM object.

`SolidWorks` is thin on purpose, so what is worth testing here is the version
arithmetic and the promise that repr() never explodes.

Every literal in here was read off a real SOLIDWORKS 2026 SP3: RevisionNumber
is ``'34.3.0'`` and GetBuildNumbers2 gives ``'sw2026_SP03'``.
"""

import pytest

from swcomapi.api.app import (
    SolidWorks,
    _service_pack_from_build,
    _version_string,
    _year_from_revision,
)


class TestYearFromRevision:
    def test_the_installed_build(self):
        """34.3.0 is SOLIDWORKS 2026, measured on the machine this was
        written on."""
        assert _year_from_revision("34.3.0") == 2026

    @pytest.mark.parametrize(
        ("revision", "year"),
        [
            ("28.0.0", 2020),
            ("29.1.0", 2021),
            ("30.0.0", 2022),
            ("31.2.0", 2023),
            ("32.0.0", 2024),
            ("33.1.0", 2025),
            ("34.3.0", 2026),
            ("35.0.0", 2027),
        ],
    )
    def test_the_whole_run_of_releases(self, revision, year):
        assert _year_from_revision(revision) == year

    def test_a_bare_major_number_still_works(self):
        assert _year_from_revision("34") == 2026

    def test_a_four_part_string_still_works(self):
        assert _year_from_revision("34.3.0.150") == 2026

    def test_before_2020_it_says_nothing_rather_than_lying(self):
        # The pre-2020 numbering does not follow this rule.
        assert _year_from_revision("27.0.0") is None

    @pytest.mark.parametrize("revision", ["", None, "weird", "v34"])
    def test_nonsense_gives_none(self, revision):
        assert _year_from_revision(revision) is None


class TestServicePackFromBuild:
    def test_the_installed_build(self):
        assert _service_pack_from_build("sw2026_SP03") == 3

    def test_sp0_is_zero_not_none(self):
        # The distinction matters: 0 means "no service pack yet", None means
        # "could not tell".
        assert _service_pack_from_build("sw2025_SP0") == 0

    def test_a_two_digit_service_pack(self):
        assert _service_pack_from_build("sw2024_SP11") == 11

    @pytest.mark.parametrize("value", ["", None, "something else", "sw2026"])
    def test_nonsense_gives_none(self, value):
        assert _service_pack_from_build(value) is None


class TestVersionString:
    def test_the_normal_case(self):
        assert _version_string(2026, 3, "34.3.0") == "SOLIDWORKS 2026 SP3 (34.3.0)"

    def test_sp0_is_still_printed(self):
        assert _version_string(2025, 0, "33.1.0") == "SOLIDWORKS 2025 SP0 (33.1.0)"

    def test_an_unknown_service_pack_is_left_out(self):
        assert _version_string(2026, None, "34.3.0") == "SOLIDWORKS 2026 (34.3.0)"

    def test_an_unrecognised_year_still_reports_the_build(self):
        assert _version_string(None, None, "27.0.0") == "SOLIDWORKS (27.0.0)"

    def test_nothing_at_all(self):
        assert _version_string(None, None, "") == "SOLIDWORKS"


class FakeSldWorks:
    """Mimics the real ISldWorks, GetBuildNumbers2's [out] parameters included."""

    def __init__(self, revision="34.3.0"):
        self.RevisionNumber = revision
        self.Visible = False

    def GetProcessID(self):
        return 4242

    def GetBuildNumbers2(self, base, current, hotfixes):
        base.value = "sw2026_SP03"
        current.value = "d260519.003"
        hotfixes.value = " - Hotfix: #HF-1530816"


class TestSolidWorks:
    def test_identity(self):
        app = SolidWorks(FakeSldWorks())
        assert app.revision_number == "34.3.0"
        assert app.year == 2026
        assert app.service_pack == 3
        assert app.version == "SOLIDWORKS 2026 SP3 (34.3.0)"
        assert app.process_id == 4242

    def test_build_numbers_come_back_in_declaration_order(self):
        assert SolidWorks(FakeSldWorks()).build_numbers == [
            "sw2026_SP03",
            "d260519.003",
            " - Hotfix: #HF-1530816",
        ]

    def test_version_survives_an_unreadable_service_pack(self):
        class NoBuildNumbers(FakeSldWorks):
            def GetBuildNumbers2(self, base, current, hotfixes):
                raise OSError("not supported on this build")

        assert SolidWorks(NoBuildNumbers()).version == "SOLIDWORKS 2026 (34.3.0)"

    def test_visible_round_trips(self):
        raw = FakeSldWorks()
        app = SolidWorks(raw)
        assert app.visible is False
        app.visible = True
        assert raw.Visible is True
        assert app.visible is True

    def test_visible_coerces_to_a_real_bool(self):
        # COM wants a VARIANT_BOOL, not a truthy Python object.
        raw = FakeSldWorks()
        SolidWorks(raw).visible = 1
        assert raw.Visible is True

    def test_the_raw_object_is_reachable(self):
        raw = FakeSldWorks()
        assert SolidWorks(raw).com is raw

    def test_repr(self):
        assert repr(SolidWorks(FakeSldWorks())) == "<SolidWorks SOLIDWORKS 2026 SP3 (34.3.0)>"

    def test_repr_survives_a_dead_connection(self):
        """A debugger printing a stale object must not raise."""

        class Dead:
            @property
            def RevisionNumber(self):
                raise OSError("the object is gone")

        assert repr(SolidWorks(Dead())) == "<SolidWorks (not responding)>"
