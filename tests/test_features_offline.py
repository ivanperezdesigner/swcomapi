"""The argument checking the new feature calls do before they touch COM.

Everything here is what a caller gets wrong, caught before SOLIDWORKS is asked
anything: a count that cannot mean what it says, a plane with nothing to fix
it, a hole with no depth. The calls themselves are checked in tests/live.
"""

import pytest

from swcomapi.api import drawing, mates, modeling, patterns, reference
from swcomapi.errors import SwCallError


class Refuses:
    """A document that raises if anything reaches COM.

    Every test here is about a check that happens first, so reaching COM is
    the failure.
    """

    name = "plate.SLDPRT"
    com = object()

    def clear_selection(self):
        raise AssertionError("the check should have raised before this")

    def select(self, *args, **kwargs):
        raise AssertionError("the check should have raised before this")


class TestPatternCounts:
    def test_a_linear_pattern_of_none_is_refused(self):
        with pytest.raises(SwCallError, match="at least 1"):
            patterns.linear(Refuses(), "Cut-Extrude1", "Edge", count=0, spacing=10)

    def test_a_circular_pattern_of_none_is_refused(self):
        with pytest.raises(SwCallError, match="at least 1"):
            patterns.circular(Refuses(), "Cut-Extrude1", "Axis1", count=0)

    def test_the_count_includes_the_original(self):
        """The docstring promises it; this is what stops that drifting."""
        assert "including the original" in patterns.linear.__doc__
        assert "including the original" in patterns.circular.__doc__


class TestPlanes:
    def test_an_angle_with_nothing_to_hinge_on_is_refused(self):
        with pytest.raises(SwCallError, match="needs second="):
            reference.plane(Refuses(), "Front Plane", angle=30)

    def test_a_midplane_between_one_thing_is_refused(self):
        with pytest.raises(SwCallError, match="between two things"):
            reference.plane(Refuses(), "Front Plane", midplane=True)


class TestHoles:
    def test_a_hole_with_no_depth_and_no_through_all_is_refused(self):
        with pytest.raises(SwCallError, match="depth= in mm or through_all"):
            modeling.hole(Refuses(), 6, at=(0, 0, 0))


class TestLofts:
    def test_one_profile_is_not_a_loft(self):
        with pytest.raises(SwCallError, match="at least two profiles"):
            modeling.loft(Refuses(), profiles=["Sketch1"])


class TestMateNames:
    def test_a_name_becomes_the_number_the_api_wants(self):
        assert mates._mate_type("coincident") == 0
        assert mates._mate_type("concentric") == 1
        assert mates._mate_type("distance") == 5

    def test_a_number_is_left_alone(self):
        assert mates._mate_type(11) == 11

    def test_an_unknown_kind_lists_the_ones_there_are(self):
        with pytest.raises(SwCallError, match="coincident"):
            mates._mate_type("glued")

    def test_the_alignments(self):
        assert mates._alignment("aligned") == 0
        assert mates._alignment("anti") == 1
        assert mates._alignment("closest") == 2

    def test_an_unknown_alignment_says_what_the_three_are(self):
        with pytest.raises(SwCallError, match="'aligned', 'anti' or 'closest'"):
            mates._alignment("sideways")

    def test_every_mate_type_name_is_unique(self):
        names = list(mates.MATE_TYPES.values())
        assert len(names) == len(set(names))


class TestTheLookupTables:
    def test_the_detail_styles_match_swdetviewstyle(self):
        from swcomapi import const

        assert drawing.DETAIL_STYLES["standard"] == const.swDetViewSTANDARD
        assert drawing.DETAIL_STYLES["broken"] == const.swDetViewBROKEN
        assert drawing.DETAIL_STYLES["no leader"] == const.swDetViewNOLEADER

    def test_the_bom_types_match_swbomtype(self):
        from swcomapi import const

        assert drawing.BOM_TYPES["parts only"] == const.swBomType_PartsOnly
        assert drawing.BOM_TYPES["top level"] == const.swBomType_TopLevelOnly
        assert drawing.BOM_TYPES["indented"] == const.swBomType_Indented

    def test_a_scale_is_accepted_either_way(self):
        assert drawing._ratio((1, 2)) == (1.0, 2.0)
        assert drawing._ratio(0.5) == (0.5, 1.0)

    def test_the_sketch_relations_are_all_sg_identifiers(self):
        from swcomapi.api import sketch

        assert all(name.startswith("sg") for name in sketch.RELATIONS.values())
        assert sketch.RELATIONS["horizontal"] == "sgHORIZONTAL2D"


class TestOneThingOrMany:
    def test_a_name_is_one_thing(self):
        assert modeling._as_list("Front Plane") == ["Front Plane"]

    def test_a_name_and_kind_pair_is_one_thing(self):
        assert modeling._as_list(("Front Plane", "PLANE")) == [("Front Plane", "PLANE")]

    def test_a_list_is_left_alone(self):
        assert modeling._as_list(["a", "b"]) == ["a", "b"]

    def test_an_object_is_wrapped(self):
        thing = object()
        assert modeling._as_list(thing) == [thing]
