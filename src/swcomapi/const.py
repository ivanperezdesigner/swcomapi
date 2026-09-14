"""Every SOLIDWORKS constant as a plain name, the way VBA sees them.

    >>> from swcomapi.const import swDocPART, swOpenDocOptions_Silent
    >>> swDocPART
    1
    >>> swOpenDocOptions_Silent
    1

In VBA the constants are global, so the documentation and every macro you will
ever read use them bare: ``swDocPART``, not
``swDocumentTypes_e.swDocPART``. This module gives you that spelling, which
makes translating a macro a matter of changing the syntax and nothing else.

Use `swcomapi.enums` instead when you want the type: an ``IntEnum`` member
prints as ``<swDocumentTypes_e.swDocPART: 1>`` and tells you where it came
from, where this module just gives you ``1``.

Why a flat namespace is safe here
---------------------------------

All 14,889 constants across all 1,434 enumerations have distinct names -
Dassault prefixes everything - so nothing shadows anything. That is not
assumed: the generator checks it and refuses to emit if it ever stops being
true.
"""

from .generated._enum_data import ENUMS

# Built on first use rather than at import, so that `import swcomapi.const`
# does not walk 14,889 entries for a script that wants one of them.
_FLAT = {}
_OWNER = {}


def _build():
    if _FLAT:
        return
    for enum_name, members in ENUMS.items():
        for member, value in members.items():
            _FLAT[member] = value
            _OWNER[member] = enum_name


def __getattr__(name):
    _build()
    try:
        value = _FLAT[name]
    except KeyError:
        raise AttributeError(
            f"module {__name__!r} has no constant {name!r}. "
            f"Try swcomapi.const.find({name.lower()!r}) to search."
        ) from None
    globals()[name] = value
    return value


def __dir__():
    _build()
    return sorted(_FLAT)


def names():
    """Every constant name, sorted. As a list of str."""
    _build()
    return sorted(_FLAT)


def find(text):
    """Constant names containing ``text``, case-insensitively.

    Returns a list of ``(name, value, enumeration)`` tuples, sorted by name.

    Example::

        >>> find("swDocPART")
        [('swDocPART', 1, 'swDocumentTypes_e')]
    """
    _build()
    lowered = text.lower()
    return [
        (name, _FLAT[name], _OWNER[name])
        for name in sorted(_FLAT)
        if lowered in name.lower()
    ]


def enum_of(name):
    """Which enumeration a constant belongs to, as a str.

    Raises KeyError if there is no such constant.
    """
    _build()
    return _OWNER[name]
