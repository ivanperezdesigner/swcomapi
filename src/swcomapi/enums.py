"""Every SOLIDWORKS enumeration, as a real ``IntEnum``.

    >>> from swcomapi.enums import swDocumentTypes_e
    >>> swDocumentTypes_e.swDocPART
    <swDocumentTypes_e.swDocPART: 1>
    >>> int(swDocumentTypes_e.swDocPART)
    1
    >>> swDocumentTypes_e(3).name
    'swDocDRAWING'

Names are kept exactly as the API spells them - ``swDocumentTypes_e``,
``swDocPART`` - so a VBA macro translates line by line and the official
documentation still reads as documentation.

Built on demand
---------------

The classes are created the first time you name one, out of the plain data in
``swcomapi.generated._enum_data``, and cached from then on. Building all 1,434
of them up front was measured at about 158 ms; this way costs about 8 ms, and
you would not know the difference: ``enums.pyi`` declares every class, so the
editor and mypy see the lot.

Flags
-----

Everything is an ``IntEnum``, including the enumerations that hold bit flags.
Combining them works and gives you the plain int the API wants::

    options = swOpenDocOptions_e.swOpenDocOptions_Silent | \\
              swOpenDocOptions_e.swOpenDocOptions_ReadOnly

There is no ``IntFlag`` anywhere because nothing in the type libraries says
which enumerations are flags, and guessing from the values would get it wrong:
``swDocumentTypes_e`` runs 0, 1, 2, 3, 4 and is not a flag set, yet three of
those are powers of two.
"""

from enum import IntEnum

from .generated._enum_data import ENUM_LIBRARY, ENUMS

__all__ = sorted(ENUMS)


def __getattr__(name):
    """Build an enumeration the first time it is asked for (PEP 562)."""
    members = ENUMS.get(name)
    if members is None:
        raise AttributeError(
            f"module {__name__!r} has no enumeration {name!r}. "
            f"It may belong to a SOLIDWORKS add-in that was not installed when "
            f"swcomapi was generated."
        )
    # `module` and `qualname` are set so that repr, pickling and the editor all
    # report swcomapi.enums rather than the enum module.
    built = IntEnum(name, members, module=__name__, qualname=name)
    built.__doc__ = f"{name} ({len(members)} constants, from {ENUM_LIBRARY[name]})."
    globals()[name] = built
    return built


def __dir__():
    return __all__


def names():
    """Every enumeration name, sorted. As a list of str."""
    return list(__all__)


def find(text):
    """Enumeration names containing ``text``, case-insensitively.

    For when you know roughly what you want and not what it is called. There
    are 1,434 of them.

    Example::

        >>> find("SaveAsVersion")
        ['swSaveAsVersion_e']
        >>> find("documenttypes")
        ['swDocumentTypes_e']
    """
    lowered = text.lower()
    return [name for name in __all__ if lowered in name.lower()]


def library_of(name):
    """Which type library an enumeration came from, as a str.

    Raises KeyError if there is no such enumeration.
    """
    return ENUM_LIBRARY[name]
