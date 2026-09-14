"""Sheet metal parameters, on stand-in COM objects."""

import pytest

from swcomapi.api.sheetmetal import (
    BEND_ALLOWANCE,
    SheetMetal,
    features_of,
    is_sheet_metal,
    of,
)


class FakeDefinition:
    """An ISheetMetalFeatureData, counting its own releases."""

    def __init__(self, thickness=0.002, radius=0.002, k=0.5, allowance=2):
        self.Thickness = thickness
        self.BendRadius = radius
        self.KFactor = k
        self.BendAllowanceType = allowance
        self.ReliefRatio = 0.5
        self.released = 0

    def GetUseGaugeTable(self):
        return False

    def ReleaseSelectionAccess(self):
        self.released += 1
        return True


class FakeFeature:
    def __init__(self, name="Sheet-Metal1", definition=None):
        self.name = name
        self.definition = definition if definition is not None else FakeDefinition()
        self.com = self

    def GetDefinition(self):
        return self.definition


class FakeFeatures:
    def __init__(self, by_type):
        self._by_type = by_type

    def of_type(self, kind):
        return self._by_type.get(kind, [])


class FakePart:
    def __init__(self, by_type=None):
        self.features = FakeFeatures(by_type or {})


class TestReading:
    def test_the_thickness_comes_back_in_mm(self):
        assert SheetMetal(FakeFeature()).thickness == 2.0

    def test_the_bend_radius_comes_back_in_mm(self):
        assert SheetMetal(FakeFeature()).bend_radius == 2.0

    def test_the_k_factor_is_dimensionless(self):
        assert SheetMetal(FakeFeature()).k_factor == 0.5

    def test_the_bend_allowance_types_are_numbered_from_one(self):
        """swBendAllowanceBendTable is 1; there is no zero."""
        assert BEND_ALLOWANCE[1] == "bend table"
        assert BEND_ALLOWANCE[2] == "k-factor"
        assert BEND_ALLOWANCE[6] == "gauge table"

    def test_the_bend_allowance_reads_as_a_name(self):
        assert SheetMetal(FakeFeature()).bend_allowance == "k-factor"

    def test_an_unknown_type_is_reported_not_swallowed(self):
        feature = FakeFeature(definition=FakeDefinition(allowance=99))
        assert SheetMetal(feature).bend_allowance == "unknown (99)"

    def test_as_dict_gives_every_parameter_at_once(self):
        assert SheetMetal(FakeFeature()).as_dict() == {
            "thickness": 2.0,
            "bend_radius": 2.0,
            "k_factor": 0.5,
            "bend_allowance": "k-factor",
            "relief_ratio": 0.5,
        }


class TestReleasing:
    def test_every_read_lets_go_of_the_feature_again(self):
        """A definition that is not released leaves the feature locked for
        the rest of the session, and nothing says so."""
        feature = FakeFeature()
        metal = SheetMetal(feature)
        assert metal.thickness == 2.0
        assert metal.bend_radius == 2.0
        assert feature.definition.released == 2

    def test_as_dict_releases_once_rather_than_per_value(self):
        feature = FakeFeature()
        SheetMetal(feature).as_dict()
        assert feature.definition.released == 1

    def test_the_raw_definition_is_handed_over_without_releasing(self):
        """That one is the caller's to release, and it says so."""
        feature = FakeFeature()
        assert SheetMetal(feature).definition is feature.definition
        assert feature.definition.released == 0


class TestFinding:
    def test_a_converted_solid_is_found_by_its_folder(self):
        part = FakePart({"SheetMetal": [FakeFeature()]})
        assert is_sheet_metal(part) is True
        assert of(part) is not None

    def test_a_base_flange_is_found_too(self):
        part = FakePart({"SMBaseFlange": [FakeFeature("Base-Flange1")]})
        assert is_sheet_metal(part) is True

    def test_a_plain_solid_is_not_sheet_metal(self):
        assert is_sheet_metal(FakePart()) is False
        assert of(FakePart()) is None

    def test_a_part_with_two_bodies_has_two_sets_of_parameters(self):
        part = FakePart(
            {"SheetMetal": [FakeFeature("Sheet-Metal1"), FakeFeature("Sheet-Metal2")]}
        )
        assert len(features_of(part)) == 2
        assert of(part).feature.name == "Sheet-Metal1"

    def test_a_definition_that_is_not_there_does_not_crash(self):
        """GetDefinition answers None for a feature it cannot open."""
        feature = FakeFeature()
        feature.definition = None
        assert SheetMetal(feature).as_dict() == {}
        assert SheetMetal(feature).thickness == pytest.approx(0.0)
