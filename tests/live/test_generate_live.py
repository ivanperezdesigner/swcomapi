"""The generator against the real type libraries.

The important one is the determinism test: regenerating from the same install
must produce byte-identical files. If it does not, every regeneration becomes
a diff and nobody can tell a real API change from noise.
"""

import pytest

from swcomapi.tools import generate, install

pytestmark = pytest.mark.live


@pytest.fixture(scope="module")
def paths():
    try:
        found = install.library_paths()
    except install.InstallNotFoundError as exc:
        pytest.skip(str(exc))
    if not found:
        pytest.skip("no type libraries found")
    return found


@pytest.fixture(scope="module")
def api(paths):
    return generate.gather(paths)


class TestGather:
    def test_it_reads_the_whole_install(self, api):
        assert len(api["libraries"]) >= 2
        assert api["year"] >= 2020

    def test_the_real_data_passes_the_safety_checks(self, api):
        """Every constant name distinct, every name an identifier.

        True on 2026 with all ten libraries. If a future release breaks it,
        this is where it shows up rather than in someone's script.
        """
        generate.check(api)

    def test_enums_and_interfaces_come_out_sorted(self, api):
        assert list(api["enums"]) == sorted(api["enums"])
        assert list(api["interfaces"]) == sorted(api["interfaces"])

    def test_libraries_are_read_in_a_fixed_order(self, api):
        files = [lib["file"].lower() for lib in api["libraries"]]
        assert files == sorted(files)

    def test_the_headline_numbers_are_the_right_order_of_magnitude(self, api):
        numbers = generate.counts(api)
        assert numbers["enums"] > 1000
        assert numbers["constants"] > 10000
        assert numbers["interfaces"] > 500
        assert numbers["members"] > 15000
        assert numbers["with_out"] > 500

    def test_a_library_that_will_not_load_is_recorded(self, api):
        """Not an assertion that any fails - on a full install none do."""
        assert isinstance(api["failed"], list)


class TestDeterminism:
    def test_gathering_twice_gives_identical_data(self, paths):
        assert generate.gather(paths) == generate.gather(paths)

    def test_regenerating_produces_byte_identical_files(self, paths, tmp_path):
        first = tmp_path / "first"
        second = tmp_path / "second"
        api = generate.gather(paths)
        generate.write(api, str(first))
        generate.write(generate.gather(paths), str(second))

        for path, _ in generate.write(api, str(first)):
            import os

            relative = os.path.relpath(path, first)
            assert (first / relative).read_bytes() == (second / relative).read_bytes(), relative

    def test_the_committed_output_matches_what_the_generator_produces_now(self, paths, tmp_path):
        """The one that catches a hand-edited generated file.

        Regenerating into a scratch directory and comparing against what is
        committed is exactly the check the release process needs: it must leave
        `git status` clean.
        """
        import os

        api = generate.gather(paths)
        generate.write(api, str(tmp_path))

        committed = generate.package_root()
        differences = []
        for path, _ in generate.write(api, str(tmp_path)):
            relative = os.path.relpath(path, tmp_path)
            fresh = (tmp_path / relative).read_bytes()
            existing = os.path.join(committed, relative)
            if not os.path.isfile(existing):
                differences.append(f"{relative} is missing from the package")
                continue
            with open(existing, "rb") as handle:
                if handle.read() != fresh:
                    differences.append(f"{relative} differs from freshly generated output")

        assert not differences, (
            "run `python -m swcomapi.tools generate`:\n  " + "\n  ".join(differences)
        )


class TestTheRealSurface:
    def test_it_found_the_enumeration_everything_starts_with(self, api):
        members = dict(api["enums"]["swDocumentTypes_e"]["members"])
        assert members["swDocPART"] == 1

    def test_it_found_the_interfaces_that_matter(self, api):
        for name in ("ISldWorks", "IModelDoc2", "IModelDocExtension", "IFeatureManager"):
            assert name in api["interfaces"], name

    def test_interfaces_remember_which_library_they_came_from(self, api):
        assert api["interfaces"]["ISldWorks"]["library"] == "SldWorks"

    def test_enums_remember_theirs(self, api):
        assert api["enums"]["swDocumentTypes_e"]["library"] == "SwConst"

    def test_simulation_is_included(self, api):
        """cosworks.tlb only loads when Simulation is installed."""
        files = {lib["file"].lower() for lib in api["libraries"]}
        if "cosworks.tlb" not in files:
            pytest.skip("Simulation is not installed")
        assert any(e["library"] == "CosmosWorksLib" for e in api["enums"].values())
