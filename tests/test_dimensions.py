"""Dimensions, on stand-in COM objects.

The conversion and the route a write takes are here; whether SOLIDWORKS
honours it per configuration is in `tests/live/test_dimensions_live.py`.
"""

import pytest

from swcomapi.api.dimensions import Dimensions, _names_array

THIS_CONFIGURATION = 1      # swInConfigurationOpts_e
ALL_CONFIGURATION = 2
SPECIFY_CONFIGURATION = 3

LINEAR = 2                  # swLinearDimension
ANGULAR = 3                 # swAngularDimension


class FakeDimension:
    """An IDimension that records how it was written to."""

    def __init__(self, value=0.01, kind=LINEAR):
        self.SystemValue = value
        self._kind = kind
        self.writes = []

    def GetType(self):
        return self._kind

    def SetSystemValue3(self, value, option, names):
        self.writes.append((value, option, names))
        self.SystemValue = value
        return 0

    def GetSystemValue3(self, option, names):
        return (self.SystemValue,)


class FakeModel:
    def __init__(self, dimension):
        self.dimension = dimension

    def Parameter(self, name):
        return self.dimension


def dimensions(dimension=None):
    return Dimensions(FakeModel(dimension or FakeDimension()))


class TestReading:
    def test_a_length_comes_back_in_mm(self):
        assert dimensions(FakeDimension(0.06))["D1@Sketch1"] == 60.0

    def test_an_angle_comes_back_in_degrees(self):
        raw = FakeDimension(0.7853981633974483, kind=ANGULAR)
        assert dimensions(raw)["Angle@Sketch1"] == pytest.approx(45.0)

    def test_is_angular_agrees(self):
        assert dimensions(FakeDimension(kind=ANGULAR)).is_angular("A") is True
        assert dimensions(FakeDimension(kind=LINEAR)).is_angular("D") is False


class TestWriting:
    def test_a_write_goes_to_the_active_configuration_only(self):
        """IDimension.SystemValue writes the value into every configuration,
        which turns a loop over configurations into one value for all."""
        raw = FakeDimension()
        dimensions(raw)["D1@Sketch1"] = 60
        assert raw.writes == [(0.06, THIS_CONFIGURATION, None)]

    def test_set_everywhere_says_so(self):
        raw = FakeDimension()
        dimensions(raw).set_everywhere("D1@Sketch1", 60)
        assert raw.writes == [(0.06, ALL_CONFIGURATION, None)]

    def test_set_in_names_the_configuration(self):
        raw = FakeDimension()
        dimensions(raw).set_in("D1@Sketch1", "BRK-040", 60)
        value, option, names = raw.writes[0]
        assert (value, option) == (0.06, SPECIFY_CONFIGURATION)
        assert names is not None

    def test_an_angle_is_written_in_degrees(self):
        raw = FakeDimension(kind=ANGULAR)
        dimensions(raw)["Angle@Sketch1"] = 45
        assert raw.writes[0][0] == pytest.approx(0.7853981633974483)


class TestNamesArray:
    def test_the_names_become_a_safearray_not_a_list(self):
        """Handed a list, GetSystemValue3 answers None and SetSystemValue3
        writes nothing, neither of them complaining."""
        array = _names_array(["BRK-040"])
        assert not isinstance(array, list)
        assert "BRK-040" in list(array.value)
