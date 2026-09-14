"""Every example written in a docstring has to actually work.

The docstrings are the documentation, so a stale example is a broken promise.
Add each new module here as it lands.
"""

import doctest

import pytest

from swcomapi import com, units
from swcomapi.api import app
from swcomapi.tools import tlb

MODULES = [com, units, app, tlb]


@pytest.mark.parametrize("module", MODULES, ids=lambda m: m.__name__)
def test_docstring_examples(module):
    results = doctest.testmod(module, verbose=False, report=True)
    assert results.failed == 0, f"{results.failed} of {results.attempted} examples failed"


@pytest.mark.parametrize("module", MODULES, ids=lambda m: m.__name__)
def test_the_module_actually_has_examples(module):
    """Guards against a module quietly losing its docstring examples."""
    finder = doctest.DocTestFinder()
    found = sum(len(t.examples) for t in finder.find(module))
    assert found > 0
