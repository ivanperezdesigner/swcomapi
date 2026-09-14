"""Drive SOLIDWORKS from Python over its COM API.

    import swcomapi as swc

    app = swc.connect()                 # the open session, or a new one
    part = app.open("bracket.SLDPRT")   # a Part, an Assembly or a Drawing

    for name in part.configurations:
        part.configuration = name
        part.export(f"{name}.pdf")

    part.close()

``swc``, not ``sw``: ``swdesigntables`` already answers to that, and the two
packages are meant to be used together.

Three layers
------------

``swcomapi.api``
    written by hand, documented, with runnable examples: connecting, opening,
    configurations, features, dimensions, properties, drawings, export. This
    is where the names above come from.
``swcomapi.enums`` and ``swcomapi.const``
    all 1,434 enumerations and 14,889 constants, generated from the type
    libraries that ship with your SOLIDWORKS.
``swcomapi.com``
    the raw COM layer, for anything not wrapped. Every object this package
    hands you exposes its COM object as ``.com``, so nothing is out of reach::

        part.com.FeatureManager.InsertDeleteBody2(True)

Finding your way around
-----------------------

19,874 API members is more than anyone remembers, so the package can tell you
about itself::

    swc.find("flat pattern")            # search names and descriptions
    print(swc.describe("IPartDoc"))     # what an interface offers
    print(swc.describe("ISldWorks.OpenDoc6"))

Windows only, and talking to SOLIDWORKS needs it installed. The enumerations,
the signature table and the documentation links are plain data and import
anywhere.
"""

__version__ = "0.1.0"

# Everything below the errors is resolved lazily, through the module-level
# __getattr__, for one concrete reason: importing this package must stay cheap
# and must not drag pywin32 in on a machine that has no Windows. The enums and
# the API index are plain data and work everywhere; only a live connection
# needs COM.
#
# name -> the module it lives in.
_LAZY = {
    # connecting
    "attach": "swcomapi.session",
    "connect": "swcomapi.session",
    "launch": "swcomapi.session",
    "wait_until_ready": "swcomapi.session",
    # the objects the api layer hands back
    "SolidWorks": "swcomapi.api.app",
    "Document": "swcomapi.api.document",
    "Part": "swcomapi.api.document",
    "Assembly": "swcomapi.api.document",
    "Drawing": "swcomapi.api.document",
    # finding your way around the API
    "describe": "swcomapi.apidoc",
    "find": "swcomapi.apidoc",
    "find_interface": "swcomapi.apidoc",
    "doclink": "swcomapi.doclinks",
}

# Submodules worth having at the top level. These resolve to the module itself.
_LAZY_MODULES = {
    "api": "swcomapi.api",
    "apidoc": "swcomapi.apidoc",
    "com": "swcomapi.com",
    "const": "swcomapi.const",
    "doclinks": "swcomapi.doclinks",
    "enums": "swcomapi.enums",
    "generated": "swcomapi.generated",
    "interfaces": "swcomapi.interfaces",
    "session": "swcomapi.session",
    "signatures": "swcomapi.signatures",
    "units": "swcomapi.units",
}

# `doclink` is the friendlier spelling of `doclinks.link`, so the loader has to
# know it answers to a different name over there.
_RENAMED = {"doclink": "link"}

# Errors are plain classes with no COM dependency, so they are imported
# eagerly: catching them must never require a successful connection.
from .errors import (  # noqa: E402
    SwAmbiguousMemberError,
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
    # connecting
    "connect",
    "attach",
    "launch",
    "wait_until_ready",
    # documents
    "SolidWorks",
    "Document",
    "Part",
    "Assembly",
    "Drawing",
    # finding your way around
    "describe",
    "find",
    "find_interface",
    "doclink",
    # submodules
    "api",
    "apidoc",
    "com",
    "const",
    "doclinks",
    "enums",
    "generated",
    "interfaces",
    "session",
    "signatures",
    "units",
    # errors
    "SwError",
    "SwAmbiguousMemberError",
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
        module = importlib.import_module(_LAZY[name])
        value = getattr(module, _RENAMED.get(name, name))
    else:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    globals()[name] = value
    return value


def __dir__():
    return sorted(__all__)
