"""Equations and materials, on stand-in COM objects."""

import pytest

from swcomapi.api.equations import Equations, _name_of
from swcomapi.api.materials import (
    DEFAULT_DATABASE,
    database_names,
    material_of,
    set_material,
)
from swcomapi.errors import SwCallError


class FakeManager:
    """An ordered list of equation lines, as IEquationMgr keeps them."""

    def __init__(self, lines=()):
        self.lines = list(lines)
        self.added = []

    def GetCount(self):
        return len(self.lines)

    def Equation(self, index):
        return self.lines[index]

    def Add2(self, index, equation, solve):
        self.added.append((index, equation, solve))
        if "=" not in equation:
            return -1
        if index < 0:
            self.lines.append(equation)
            return len(self.lines) - 1
        self.lines.insert(index, equation)
        return index

    def Delete(self, index):
        if not 0 <= index < len(self.lines):
            return -1
        del self.lines[index]
        return 0

    def Value(self, index):
        return float(self.lines[index].split("=", 1)[1].strip().strip('"'))

    def GlobalVariable(self, index):
        return not self.lines[index].startswith('"D')

    def EvaluateAll(self):
        return -1


class FakeModel:
    def __init__(self, manager):
        self.manager = manager

    def GetEquationMgr(self):
        return self.manager


def equations(*lines):
    return Equations(FakeModel(FakeManager(lines)))


class TestNameOf:
    def test_the_quotes_come_off(self):
        assert _name_of('"width" = 60') == "width"

    def test_a_driven_dimension_keeps_its_whole_name(self):
        assert (
            _name_of('"D1@Sketch1@plate.SLDPRT" = "width" * 2')
            == "D1@Sketch1@plate.SLDPRT"
        )

    def test_spaces_around_the_equals_are_optional(self):
        assert _name_of('"width"=60') == "width"

    def test_a_line_with_no_equals_is_returned_as_it_is(self):
        assert _name_of("nonsense") == "nonsense"


class TestReading:
    def test_it_is_a_sequence_of_the_lines(self):
        listed = equations('"width" = 60', '"height" = 40')
        assert len(listed) == 2
        assert listed[0] == '"width" = 60'
        assert list(listed) == ['"width" = 60', '"height" = 40']

    def test_a_name_gives_the_value_and_an_index_gives_the_line(self):
        listed = equations('"width" = 60')
        assert listed["width"] == 60.0
        assert listed[0] == '"width" = 60'

    def test_a_negative_index_counts_from_the_end(self):
        listed = equations('"width" = 60', '"height" = 40')
        assert listed[-1] == '"height" = 40'

    def test_an_index_past_the_end_says_how_many_there_are(self):
        with pytest.raises(IndexError, match="has 1 equations"):
            equations('"width" = 60')[5]

    def test_a_name_that_is_not_there_is_a_key_error(self):
        with pytest.raises(KeyError, match=r"see \.names\(\)"):
            equations('"width" = 60')["depth"]

    def test_the_names_are_listed_without_their_quotes(self):
        assert equations('"width" = 60', '"height" = 40').names() == [
            "width",
            "height",
        ]

    def test_globals_and_driven_dimensions_are_told_apart(self):
        listed = equations('"width" = 60', '"D1@Sketch1" = 20')
        assert listed.is_global(0) is True
        assert listed.is_global(1) is False
        assert listed.globals() == {"width": 60.0}

    def test_index_of_ignores_the_quotes_given(self):
        listed = equations('"width" = 60')
        assert listed.index_of("width") == 0
        assert listed.index_of('"width"') == 0
        assert listed.index_of("depth") is None

    def test_contains_works_on_names_and_on_whole_lines(self):
        listed = equations('"width" = 60')
        assert "width" in listed
        assert '"width" = 60' in listed
        assert "depth" not in listed


class TestWriting:
    def test_adding_appends_by_default(self):
        listed = equations('"width" = 60')
        assert listed.add('"height" = 40') == 1
        assert listed.names() == ["width", "height"]

    def test_adding_at_an_index_inserts_before_it(self):
        listed = equations('"width" = 60')
        assert listed.add('"height" = 40', at=0) == 0
        assert listed.names() == ["height", "width"]

    def test_an_equation_solidworks_rejects_is_an_error(self):
        """The raw call returns -1 rather than raising."""
        with pytest.raises(SwCallError, match="would not add"):
            equations().add("nonsense without an equals sign")

    def test_deleting_by_index(self):
        listed = equations('"width" = 60', '"height" = 40')
        del listed[0]
        assert listed.names() == ["height"]

    def test_deleting_something_that_is_not_there_says_so(self):
        with pytest.raises(SwCallError, match="could not delete"):
            del equations()[3]

    def test_evaluate_reports_what_solidworks_returns(self):
        """Documented as a count of failures; it is not one."""
        assert equations('"width" = 60').evaluate() == -1

    def test_the_repr_counts_the_global_variables(self):
        listed = equations('"width" = 60', '"D1@Sketch1" = 20')
        assert repr(listed) == "<Equations: 2, 1 of them global variables>"


class FakePart:
    """A part that remembers what material was set on it."""

    def __init__(self, material="", database=DEFAULT_DATABASE, obeys=True):
        self._material = material
        self._database = database
        self._obeys = obeys
        self.configuration = "Default"
        self.com = self

    def GetMaterialPropertyName2(self, configuration, database):
        database.value = self._database if self._material else ""
        return self._material

    def SetMaterialPropertyName2(self, configuration, database, name):
        if self._obeys:
            self._material = name
            self._database = database


class FakeApp:
    def __init__(self, paths):
        self._paths = paths
        self.com = self

    def GetMaterialDatabases(self):
        return tuple(self._paths)


class TestMaterials:
    def test_the_name_is_the_return_value_not_the_out_parameter(self):
        """The out parameter is the database. Reading it as the material gives
        'SOLIDWORKS Materials' for every part there is."""
        part = FakePart(material="Stainless Steel (ferritic)")
        assert material_of(part) == "Stainless Steel (ferritic)"

    def test_a_part_with_no_material_reads_as_empty(self):
        assert material_of(FakePart()) == ""

    def test_setting_a_material_reads_it_back(self):
        part = FakePart()
        assert set_material(part, "6061 Alloy") == "6061 Alloy"
        assert material_of(part) == "6061 Alloy"

    def test_a_name_that_does_not_apply_is_an_error(self):
        """A misspelled name leaves the part with no material, silently."""
        part = FakePart(obeys=False)
        with pytest.raises(SwCallError, match="was not applied"):
            set_material(part, "Unobtainium")

    def test_removing_the_material_is_not_an_error(self):
        part = FakePart(material="6061 Alloy")
        assert set_material(part, "") == ""

    def test_the_database_names_lose_their_paths_and_extensions(self):
        app = FakeApp(
            [
                r"C:\lib\sldmaterials\SOLIDWORKS Materials.sldmat",
                r"C:\lib\sldmaterials\custom materials.sldmat",
            ]
        )
        assert database_names(app) == ["SOLIDWORKS Materials", "custom materials"]
