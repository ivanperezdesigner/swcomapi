"""Every example written in a docstring has to actually work.

The docstrings are the documentation, so a stale example is a broken promise.
Add each new module here as it lands.
"""

import doctest

import pytest

from swcomapi import apidoc, com, const, doclinks, enums, signatures, units
from swcomapi.api import app, components, document, drawing, export, sketch
from swcomapi.api import dimensions as dimensions_module
from swcomapi.tools import tlb

# swcomapi.api.modeling and swcomapi.api.geometry are absent on purpose too:
# every example in them needs a running SOLIDWORKS and a solid to measure.
# Those are executed for real in tests/live/test_modeling.py and
# tests/live/test_geometry.py.
#
# swcomapi.tools.generate is absent on purpose: what it documents is the
# files it emits, and those are checked in tests/test_generate.py.
MODULES = [
    com,
    units,
    app,
    tlb,
    enums,
    const,
    signatures,
    doclinks,
    apidoc,
    document,
    export,
    dimensions_module,
    components,
    sketch,
    drawing,
]


# Several docstrings show real output that is long, wrapped, or a URL with a
# stable prefix and a very long tail, so the whole suite runs with these on.
FLAGS = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE


@pytest.mark.parametrize("module", MODULES, ids=lambda m: m.__name__)
def test_docstring_examples(module):
    results = doctest.testmod(module, verbose=False, report=True, optionflags=FLAGS)
    assert results.failed == 0, f"{results.failed} of {results.attempted} examples failed"


@pytest.mark.parametrize("module", MODULES, ids=lambda m: m.__name__)
def test_the_module_actually_has_examples(module):
    """Guards against a module quietly losing its docstring examples."""
    finder = doctest.DocTestFinder()
    found = sum(len(t.examples) for t in finder.find(module))
    assert found > 0
