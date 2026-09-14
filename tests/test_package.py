"""The package's public surface.

Small, but it guards two real promises: that the names in `__all__` resolve to
the right kind of object, and that importing the package does not need a COM
stack to be present.
"""

import importlib
import sys

import pytest

import swcomapi as sw


class TestEntryPoints:
    @pytest.mark.parametrize("name", ["connect", "attach", "launch", "wait_until_ready"])
    def test_they_are_functions_not_modules(self, name):
        """Regression: `swcomapi.connect` used to resolve to the submodule.

        A submodule named `connect.py` shadows a `connect` function on the
        package, so `sw.connect()` raised "'module' object is not callable".
        The module is called `session` for exactly this reason.
        """
        attr = getattr(sw, name)
        assert callable(attr), f"sw.{name} is {type(attr).__name__}, not callable"

    def test_solidworks_is_the_class(self):
        from swcomapi.api.app import SolidWorks

        assert sw.SolidWorks is SolidWorks

    def test_there_is_no_connect_submodule_to_shadow_anything(self):
        with pytest.raises(ModuleNotFoundError):
            importlib.import_module("swcomapi.connect")


class TestSubmodules:
    @pytest.mark.parametrize("name", ["com", "units", "session"])
    def test_they_resolve_to_modules(self, name):
        import types

        assert isinstance(getattr(sw, name), types.ModuleType)


class TestErrors:
    @pytest.mark.parametrize(
        "name",
        [
            "SwError",
            "SwUnavailableError",
            "SwConnectionError",
            "SwNotRunningError",
            "SwBusyError",
            "SwCallError",
            "SwMemberNotFoundError",
            "SwDocumentError",
            "SwWarning",
        ],
    )
    def test_every_error_is_exported_and_is_a_class(self, name):
        assert isinstance(getattr(sw, name), type)

    def test_everything_derives_from_sw_error(self):
        """One name to catch, so `except sw.SwError` really is enough."""
        for name in sw.__all__:
            attr = getattr(sw, name)
            if isinstance(attr, type) and name.startswith("Sw") and name != "SwWarning":
                assert issubclass(attr, sw.SwError), name

    def test_the_warning_is_a_warning_not_an_error(self):
        assert issubclass(sw.SwWarning, Warning)


class TestDunders:
    def test_all_the_names_in_all_resolve(self):
        for name in sw.__all__:
            getattr(sw, name)

    def test_dir_matches_all(self):
        assert dir(sw) == sorted(sw.__all__)

    def test_an_unknown_name_raises_attribute_error(self):
        # Through a variable, so that neither B018 (useless expression) nor
        # B009 (getattr with a constant) fires. Ruff dislikes both spellings.
        missing = "nonsense"
        with pytest.raises(AttributeError, match="has no attribute 'nonsense'"):
            getattr(sw, missing)

    def test_version_is_a_string(self):
        assert isinstance(sw.__version__, str)
        assert sw.__version__.count(".") == 2


class TestLazyImport:
    def test_importing_the_package_does_not_pull_in_pywin32(self):
        """`import swcomapi` must stay cheap, and must work where COM cannot.

        The enums and the documentation links are plain data. Only an actual
        connection needs pywin32, so the COM layer is imported on first use.
        """
        for name in list(sys.modules):
            if name == "swcomapi" or name.startswith("swcomapi."):
                del sys.modules[name]
        for name in ("pythoncom", "win32com", "win32com.client"):
            sys.modules.pop(name, None)

        importlib.import_module("swcomapi")
        assert "pythoncom" not in sys.modules
        assert "swcomapi.com" not in sys.modules
