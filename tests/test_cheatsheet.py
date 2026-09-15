"""The cheat sheet, and that it still matches the package.

A generated reference is only worth having if it cannot drift, so these check
that regenerating it produces what is committed, and that nothing in the
pythonic layer is missing from it.
"""

import os

import pytest

from swcomapi.tools import cheatsheet as cheatsheet_module

REFERENCE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "docs",
    "reference",
    "cheatsheet.md",
)


@pytest.fixture(scope="module")
def text():
    return cheatsheet_module.cheatsheet()


class TestTheContent:
    def test_it_has_a_section_for_every_module_it_orders(self, text):
        for name in cheatsheet_module.ORDER:
            assert f"## `{name}`" in text

    def test_it_names_the_three_ways_in(self, text):
        for name in ("swc.connect", "swc.attach", "swc.launch"):
            assert name in text

    def test_it_carries_the_conventions_that_hold_everywhere(self, text):
        assert "Millimetres and degrees" in text
        assert "thickness" in text, "the reserved name has to be called out"
        assert "Dimension@Feature" in text

    @pytest.mark.parametrize(
        "call",
        [
            ".extrude(",
            ".cut(",
            ".revolve(",
            ".rectangle(corner, opposite)",
            ".add(equation, at=None, solve=True)",
            ".set_everywhere(name, value)",
            ".value_in(name, configuration)",
            ".solid_features()",
            ".mass_at(density)",
        ],
    )
    def test_the_calls_that_matter_are_listed(self, text, call):
        assert call in text

    def test_signatures_leave_self_out(self, text):
        assert "(self" not in text

    def test_restructured_text_literals_became_markdown(self, text):
        assert "``" not in text

    def test_every_row_is_a_table_row(self, text):
        rows = [line for line in text.split("\n") if line.startswith("| `")]
        assert len(rows) > 150
        for row in rows:
            assert row.endswith(" |"), row
            assert row.count("|") >= 3, row


class TestItIsGenerated:
    def test_the_committed_file_is_what_the_generator_produces(self, text):
        """Run `python -m swcomapi.tools cheatsheet` if this fails."""
        committed = open(REFERENCE, encoding="utf-8").read()
        assert committed == text

    def test_generating_twice_gives_the_same_bytes(self, text):
        assert cheatsheet_module.cheatsheet() == text


class TestTheHelpers:
    def test_a_summary_is_the_first_line_only(self):
        def sample():
            """First line.

            Second paragraph, which is not wanted.
            """

        assert cheatsheet_module._summary(sample) == "First line."

    def test_a_summary_of_something_undocumented_is_empty(self):
        def sample():
            pass

        assert cheatsheet_module._summary(sample) == ""

    def test_a_pipe_is_escaped_so_it_cannot_end_a_cell(self):
        def sample():
            """Either 'part' | 'assembly'."""

        assert cheatsheet_module._summary(sample) == "Either 'part' \\| 'assembly'."

    def test_a_signature_drops_self(self):
        class Sample:
            def method(self, a, b=1):
                pass

        rendered = cheatsheet_module._signature("method", Sample.method, drop_self=True)
        assert rendered == "method(a, b=1)"

    def test_a_signature_keeps_a_plain_function_whole(self):
        def sample(a, b=1):
            pass

        assert cheatsheet_module._signature("sample", sample) == "sample(a, b=1)"
