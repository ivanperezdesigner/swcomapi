"""Drive SOLIDWORKS from Python over its COM API.

Two layers, one package:

* ``swcomapi.generated`` -- the whole API surface, produced by reading the type
  libraries that ship with SOLIDWORKS. Every enumeration, every interface,
  every method signature, with a link to the official page for each one.
* ``swcomapi.api`` -- a hand-written, documented layer over the calls you make
  every day: connect, open, configurations, features, dimensions, drawings,
  export.

Every wrapper object exposes the raw COM object as ``.com``, so nothing in the
API is ever out of reach.

Quickstart::

    import swcomapi as sw

    app = sw.connect()          # attach to the open session, or start one
    print(app.version)          # 'SOLIDWORKS 2026 (34.3.0.150)'

Windows only. Connecting needs SOLIDWORKS installed; the enums, the signature
table and the documentation links are plain data and import anywhere.
"""

__version__ = "0.0.1"

# The COM entry points are resolved lazily, through the module-level
# __getattr__ below, for one concrete reason: `swcomapi.generated.enums` and
# the documentation links are pure data that work on any platform, and
# importing the package must not drag pywin32 in and fail on a machine that
# has no Windows. `import swcomapi` stays cheap; `sw.connect` is what pulls in
# the COM layer.
#
# name -> the module it lives in.
_LAZY = {
    "attach": "swcomapi.session",
    "connect": "swcomapi.session",
    "launch": "swcomapi.session",
    "wait_until_ready": "swcomapi.session",
    "SolidWorks": "swcomapi.api.app",
}

# Submodules worth having at the top level. These resolve to the module
# itself, not to something inside it.
_LAZY_MODULES = {
    "const": "swcomapi.const",
    "enums": "swcomapi.enums",
    "generated": "swcomapi.generated",
    "com": "swcomapi.com",
    "units": "swcomapi.units",
    "session": "swcomapi.session",
}

# Errors are plain classes with no COM dependency, so they are imported
# eagerly: catching them must never require a successful connection.
from .errors import (  # noqa: E402
    SwBusyError,
    SwCallError,
    SwConnectionError,
    SwDocumentError,
    SwError,
    SwMemberNotFoundError,
    SwNotRunningError,
    SwUnavailableError,
    SwWarning,
)

__all__ = [
    "__version__",
    # entry points
    "connect",
    "attach",
    "launch",
    "wait_until_ready",
    "SolidWorks",
    # submodules worth having at the top level
    "enums",
    "const",
    "generated",
    "com",
    "units",
    "session",
    # errors
    "SwError",
    "SwUnavailableError",
    "SwConnectionError",
    "SwNotRunningError",
    "SwBusyError",
    "SwCallError",
    "SwMemberNotFoundError",
    "SwDocumentError",
    "SwWarning",
]


def __getattr__(name):
    """Resolve the lazy names on first use (PEP 562)."""
    import importlib

    if name in _LAZY_MODULES:
        value = importlib.import_module(_LAZY_MODULES[name])
    elif name in _LAZY:
        value = getattr(importlib.import_module(_LAZY[name]), name)
    else:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    globals()[name] = value
    return value


def __dir__():
    return sorted(__all__)
