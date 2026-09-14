"""Unit conversion. The whole point is that these numbers are never guessed."""

import math

import pytest

from swcomapi import units


class TestToTheApi:
    """Values on their way into a raw API call: metres and radians."""

    def test_millimetres_become_metres(self):
        assert units.mm(25) == 0.025
        assert units.mm(0) == 0.0
        assert units.mm(-3.5) == -0.0035

    def test_centimetres_become_metres(self):
        assert units.cm(2.5) == 0.025

    def test_inches_become_metres(self):
        # An inch is exactly 25.4 mm by definition, so this is exact.
        assert units.inch(1) == 0.0254
        assert units.inch(0.5) == 0.0127

    def test_degrees_become_radians(self):
        assert units.deg(180) == math.pi
        assert units.deg(90) == pytest.approx(math.pi / 2)
        assert units.deg(0) == 0.0


class TestFromTheApi:
    """Values coming back out of a raw API call."""

    def test_metres_become_millimetres(self):
        assert units.to_mm(0.025) == 25.0
        assert units.to_mm(0.0) == 0.0

    def test_metres_become_inches(self):
        assert units.to_inch(0.0254) == pytest.approx(1.0)

    def test_radians_become_degrees(self):
        assert units.to_deg(math.pi) == 180.0
        assert units.to_deg(math.pi / 4) == pytest.approx(45.0)

    def test_round_trip_is_stable(self):
        for value in (0, 1, 25, 25.4, 1234.5678, -7):
            assert units.to_mm(units.mm(value)) == pytest.approx(value)
            assert units.to_deg(units.deg(value)) == pytest.approx(value)


class TestMassProperties:
    """Areas, volumes and mass, the way GetMassProperties reports them."""

    def test_area(self):
        # A 10 x 10 mm face is 1e-4 m2.
        assert units.to_mm2(1e-4) == pytest.approx(100.0)

    def test_volume(self):
        # A 10 mm cube is 1e-6 m3.
        assert units.to_mm3(1e-6) == pytest.approx(1000.0)
        assert units.to_cm3(1e-6) == pytest.approx(1.0)

    def test_mass(self):
        assert units.to_g(0.275) == pytest.approx(275.0)

    def test_a_real_aluminium_block(self):
        """100 x 50 x 10 mm of 6061-T6, as the API would report it.

        Volume 5e-5 m3, density 2700 kg/m3, so 0.135 kg.
        """
        volume_m3 = 5e-5
        mass_kg = volume_m3 * 2700.0
        assert units.to_mm3(volume_m3) == pytest.approx(50000.0)
        assert units.to_g(mass_kg) == pytest.approx(135.0)


class TestSequences:
    """The flat arrays that GetBox and friends hand back."""

    def test_to_mm_all(self):
        # A GetBox result: two corners of a 25 x 40 x 10 mm box.
        box = [0.0, 0.0, 0.0, 0.025, 0.04, 0.01]
        assert units.to_mm_all(box) == [0.0, 0.0, 0.0, 25.0, 40.0, 10.0]

    def test_to_mm_all_of_empty_is_empty(self):
        assert units.to_mm_all([]) == []

    def test_mm_all(self):
        assert units.mm_all([25.0, 40.0]) == [0.025, 0.04]

    def test_to_deg_all(self):
        assert units.to_deg_all([0.0, math.pi]) == [0.0, 180.0]

    def test_accepts_any_iterable_not_just_lists(self):
        assert units.to_mm_all((0.025,)) == [25.0]
        assert units.to_mm_all(v for v in [0.025]) == [25.0]
