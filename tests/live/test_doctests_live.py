"""Every docstring example that needs SOLIDWORKS, executed against it.

Skipped unless ``SWCOMAPI_LIVE=1``.

`tests/test_doctests.py` runs the examples that need nothing but Python. The
rest could not run there, so they were written as reStructuredText literal
blocks, which nothing executes, or marked ``# doctest: +SKIP``, which is
doctest's way of not executing them either. Around a hundred worked examples
that no suite had ever run. Several were wrong, in the way unexecuted
examples always eventually are: the cut in `swcomapi.api.modeling` removed
nothing, because it pointed away from the material.

So every example is now an ordinary doctest marked ``+SKIP``, and this module
strips the flag back off and runs it for real against a document built for
it. An example is either executed somewhere or it is not an example.

Each docstring gets its own fresh document, because a docstring is a
self-contained example and must not depend on what the one before it did.
That is deliberately slow.
"""

import doctest
import importlib
import os
import pkgutil

import pytest

import swcomapi as swc
from swcomapi import api

pytestmark = pytest.mark.live

# Everything with examples that touch SOLIDWORKS: the whole pythonic layer,
# plus the two lower modules whose examples open a session.
MODULES = sorted(
    [f"swcomapi.api.{module.name}" for module in pkgutil.iter_modules(api.__path__)]
    + ["swcomapi.session", "swcomapi.com"]
)

# Masses, document names and build numbers differ from machine to machine, so
# the examples say so with an ellipsis rather than pretending otherwise.
FLAGS = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE

# What a docstring may ask for by name. Anything an example does not mention
# is not built, so a docstring about dimensions does not pay for an assembly.
FIXTURES = ("part", "document", "assembly", "drawing", "body", "face", "sketch")


class Scratch:
    """The documents one docstring's examples run against.

    Built on demand and closed together afterwards, so a failure leaves no
    windows open on the machine running the suite.
    """

    def __init__(self, app, folder):
        self.app = app
        self.folder = folder
        self.opened = []

    def part(self):
        """The plate every example is written against.

        60 by 40 by 10 in 6061, with one 12 mm hole through the middle. The
        hole is there so that an example about a cylindrical face has one to
        find. Built rather than opened from a file, so the suite carries no
        fixture geometry and cannot be broken by someone editing it.
        """
        part = self.app.new_part()
        self.opened.append(part)
        with part.sketch_on("Front Plane", add_to_db=True) as sketch:
            sketch.rectangle((0, 0), (60, 40))
        part.extrude(10)
        part.select("Boss-Extrude1", "FACE")
        with part.sketch_on(add_to_db=True) as sketch:
            sketch.circle((30, 20), 6)
        part.cut(through_all=True)
        part.set_material("6061 Alloy")
        return part

    def saved_part(self):
        """The same plate, written to disk so an assembly can reference it."""
        part = self.part()
        path = os.path.join(self.folder, "plate.SLDPRT")
        part.save_as(path)
        return part, path

    def assembly(self):
        """An assembly with two instances of the plate in it."""
        _, path = self.saved_part()
        assembly = self.app.new_assembly()
        self.opened.append(assembly)
        assembly.components.add(path, at=(0, 0, 0))
        assembly.components.add(path, at=(100, 0, 0))
        assembly.rebuild()
        return assembly

    def drawing(self):
        """A drawing with one front view of the plate on it."""
        _, path = self.saved_part()
        drawing = self.app.new_drawing()
        self.opened.append(drawing)
        drawing.views.add(path, "Front", at=(100, 100))
        return drawing

    def close(self):
        for document in reversed(self.opened):
            try:
                document.close()
            except Exception:
                pass
        self.opened = []


def examples_in(module):
    """Every DocTest in ``module`` that has at least one example."""
    return [test for test in doctest.DocTestFinder().find(module) if test.examples]


def unskip(test):
    """Clear ``+SKIP`` from every example. Returns how many were cleared.

    The flag is what keeps these out of the offline suite; here it is the one
    thing between the example and being checked.
    """
    cleared = 0
    for example in test.examples:
        if example.options.pop(doctest.SKIP, None) is not None:
            cleared += 1
    return cleared


def wanted_by(test):
    """Which fixtures a docstring's examples mention, as a set of str."""
    source = "".join(example.source for example in test.examples)
    return {name for name in FIXTURES if name in source}


def globs_for(test, scratch):
    """The names a docstring's examples can use, as a dict."""
    wanted = wanted_by(test)
    globs = dict(test.globs)
    globs.update({"swc": swc, "app": scratch.app})

    if {"part", "document", "body", "face", "sketch"} & wanted:
        part = scratch.part()
        globs["part"] = part
        globs["document"] = part
        if "body" in wanted:
            globs["body"] = part.bodies[0]
        if "face" in wanted:
            globs["face"] = part.bodies[0].faces[0]
        if "sketch" in wanted:
            globs["sketch"] = part.sketches["Sketch1"]
    if "assembly" in wanted:
        globs["assembly"] = scratch.assembly()
    if "drawing" in wanted:
        globs["drawing"] = scratch.drawing()
    return globs


@pytest.fixture(scope="module")
def app():
    try:
        return swc.attach(visible=None)
    except Exception as exc:
        pytest.skip(f"no SOLIDWORKS to talk to: {exc}")


def pytest_generate_tests(metafunc):
    """One test per docstring, named after the thing it documents."""
    if "doctest_name" not in metafunc.fixturenames:
        return
    names = []
    for module_name in MODULES:
        module = importlib.import_module(module_name)
        names.extend(test.name for test in examples_in(module))
    metafunc.parametrize("doctest_name", sorted(names))


def module_of(doctest_name):
    """Which listed module a DocTest name belongs to, as a str."""
    candidates = [name for name in MODULES if doctest_name.startswith(name)]
    return max(candidates, key=len)


def test_the_examples_run(app, tmp_path, doctest_name):
    """Run one docstring's examples against documents built for it."""
    module = importlib.import_module(module_of(doctest_name))
    found = [test for test in examples_in(module) if test.name == doctest_name]
    assert found, f"{doctest_name} went missing"

    test = found[0]
    unskip(test)

    scratch = Scratch(app, str(tmp_path))
    try:
        test.globs = globs_for(test, scratch)
        runner = doctest.DocTestRunner(optionflags=FLAGS, verbose=False)
        runner.run(test, clear_globs=False)
    finally:
        scratch.close()

    assert runner.failures == 0, (
        f"{runner.failures} of {runner.tries} examples failed in {doctest_name}"
    )


class TestTheRunnerItself:
    def test_unskip_clears_the_flag(self):
        parsed = doctest.DocTestParser().get_doctest(
            ">>> 1 + 1  # doctest: +SKIP\n2\n", {}, "sample", None, 0
        )
        assert doctest.SKIP in parsed.examples[0].options
        assert unskip(parsed) == 1
        assert doctest.SKIP not in parsed.examples[0].options

    def test_a_docstring_asks_only_for_what_it_mentions(self):
        parsed = doctest.DocTestParser().get_doctest(
            ">>> part.mass\n187.2\n", {}, "sample", None, 0
        )
        assert wanted_by(parsed) == {"part"}

    def test_every_module_in_the_pythonic_layer_is_covered(self):
        every = {f"swcomapi.api.{m.name}" for m in pkgutil.iter_modules(api.__path__)}
        assert not every - set(MODULES)

    def test_module_of_picks_the_longest_match(self):
        assert module_of("swcomapi.api.document.Part.mass") == "swcomapi.api.document"
