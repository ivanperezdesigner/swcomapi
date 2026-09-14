"""Find the installed SOLIDWORKS and its type libraries.

The generator needs the ``.tlb`` files, and their location is not fixed. It
moved with the 3DEXPERIENCE releases: 2025 and earlier install under
``C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS``, while 2026 lands in
``C:\\Program Files\\Dassault Systemes\\SOLIDWORKS 3DEXPERIENCE R2026x\\SOLIDWORKS``.
Guessing from a list of known paths would break on the next release.

So the directory is taken from the place that is always right: the COM
registration. ``SldWorks.Application`` resolves to a CLSID, the CLSID names the
``LocalServer32`` that implements it, and that is the real ``SLDWORKS.exe``
wherever it lives.

Set ``SWCOMAPI_SOLIDWORKS_DIR`` to override, which is what you want when
generating against a second install.
"""

import os
import winreg

PROGID = "SldWorks.Application"
DIR_ENV = "SWCOMAPI_SOLIDWORKS_DIR"

# The libraries the generator reads, in the order they are emitted. Names only:
# they are resolved against the install directory.
#
# `sldworks` and `swconst` are the API. The rest are add-in surfaces that ship
# in the box, and are included because "everything" was the brief.
CORE_LIBRARIES = ("sldworks.tlb", "swconst.tlb")

ADDIN_LIBRARIES = (
    "swcommands.tlb",
    "swpublished.tlb",
    "swdimxpert.tlb",
    "swmotionstudy.tlb",
    "swdocumentmgr.tlb",
    "SWRoutingLib.tlb",
    "sldcostingapi.tlb",
    "sustainability.tlb",
)

# Libraries that live in a subdirectory rather than beside SLDWORKS.exe.
NESTED_LIBRARIES = {
    "cosworks.tlb": "Simulation",
}

ALL_LIBRARIES = CORE_LIBRARIES + ADDIN_LIBRARIES + tuple(NESTED_LIBRARIES)


class InstallNotFoundError(RuntimeError):
    """SOLIDWORKS is not registered on this machine."""


def solidworks_dir():
    """The directory holding ``SLDWORKS.exe``, as a str.

    Raises `InstallNotFoundError` when SOLIDWORKS is not registered and no
    override is set.
    """
    override = os.environ.get(DIR_ENV)
    if override:
        if not os.path.isdir(override):
            raise InstallNotFoundError(
                f"{DIR_ENV} points at {override!r}, which is not a directory"
            )
        return override

    executable = _registered_executable()
    if executable is None:
        raise InstallNotFoundError(
            f"{PROGID} is not registered on this machine, so SOLIDWORKS "
            f"cannot be located. Install it, or set {DIR_ENV} to the "
            f"directory holding SLDWORKS.exe."
        )
    return os.path.dirname(executable)


def _registered_executable():
    """The path ``SldWorks.Application`` resolves to, or None.

    The registry stores it in 8.3 short form - ``C:\\PROGRA~1\\DASSAU~1\\...``
    - so it is expanded back to the long form before being handed out.
    """
    try:
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, rf"{PROGID}\CLSID") as key:
            clsid = winreg.QueryValue(key, None)
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, rf"CLSID\{clsid}\LocalServer32") as key:
            server = winreg.QueryValue(key, None)
    except OSError:
        return None

    server = server.strip().strip('"')
    return _expand_short_path(server)


def _expand_short_path(path):
    """A path with 8.3 components expanded to its long form.

    Falls back to the input when the file does not exist or the Windows call is
    unavailable, since a short path still works for opening files.
    """
    try:
        import win32api

        return win32api.GetLongPathName(path)
    except Exception:
        return path


def library_paths(directory=None, include_addins=True):
    """The type libraries present, as a list of absolute paths.

    directory
        where to look; defaults to `solidworks_dir()`
    include_addins
        False restricts the result to ``sldworks.tlb`` and ``swconst.tlb``

    Only files that exist are returned: which add-ins are installed varies by
    licence, and a missing one is normal rather than an error.
    """
    directory = directory or solidworks_dir()
    wanted = CORE_LIBRARIES if not include_addins else ALL_LIBRARIES

    found = []
    for name in wanted:
        nested = NESTED_LIBRARIES.get(name)
        parts = (directory, nested, name) if nested else (directory, name)
        candidate = os.path.join(*parts)
        if os.path.isfile(candidate):
            found.append(candidate)
    return found


def describe():
    """A summary of what was found, as a dict. For the survey output."""
    executable = _registered_executable()
    directory = solidworks_dir()
    return {
        "executable": executable,
        "directory": directory,
        "libraries": library_paths(directory),
        "override": os.environ.get(DIR_ENV),
    }
