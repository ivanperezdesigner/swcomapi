"""Materials: reading one, setting one, and finding out what is available.

    part.material                       # 'Stainless Steel (ferritic)'
    part.material = "6061 Alloy"        # from the SOLIDWORKS library
    part.material_database             # 'SOLIDWORKS Materials'
    part.material_of("BRK-040")        # per configuration

A material belongs to a configuration, not to a part, which is how one file
ships in steel and in aluminium. `material` reads and writes the active one;
`material_of` and `set_material` take a configuration name.

Where the names come from
-------------------------

A material is a name inside a database file, and both halves are needed to
set one. ``databases(app)`` lists the ``.sldmat`` files SOLIDWORKS is
searching, and the names inside them are the ones the material tree shows -
``"6061 Alloy"``, ``"AISI 304"``, ``"ABS"``. Setting a name that is not in
the database leaves the part with no material and reports nothing, so
`set_material` reads it back.

The trap
--------

``IPartDoc.GetMaterialPropertyName2`` returns the material name as its return
value and the database as an ``[out]`` parameter. Reading the ``[out]`` one
and calling it the material - which is the natural mistake, since the
parameter list is what you see first - gets you ``'SOLIDWORKS Materials'``
for every part in the world, or an empty string.
"""

import os

from .. import com
from ..errors import SwCallError

# What SOLIDWORKS calls its own library, and the default database when one is
# not named. Any .sldmat file can be used instead.
DEFAULT_DATABASE = "SOLIDWORKS Materials"


def material_of(part, configuration=None):
    """The material applied to one configuration, as a str.

    part
        a `swcomapi.api.document.Part`
    configuration
        which configuration, by name; the active one if omitted

    Returns ``''`` when the configuration has no material.

    Example:

        >>> material_of(part)                       # doctest: +SKIP
        '6061 Alloy'
        >>> material_of(part, part.configuration)   # doctest: +SKIP
        '6061 Alloy'
    """
    name, _ = com.call_out(
        part.com,
        "GetMaterialPropertyName2",
        configuration if configuration is not None else part.configuration,
        interface="IPartDoc",
    )
    return name or ""


def database_of(part, configuration=None):
    """Which database the applied material comes from, as a str.

    Returns ``''`` when there is no material. The name of the ``.sldmat``
    file without its extension - usually ``'SOLIDWORKS Materials'``.
    """
    _, out = com.call_out(
        part.com,
        "GetMaterialPropertyName2",
        configuration if configuration is not None else part.configuration,
        interface="IPartDoc",
    )
    return out.get("Database", "") or ""


def set_material(part, name, configuration=None, database=None):
    """Apply a material. Returns the name applied, as a str.

    part
        a `swcomapi.api.document.Part`
    name
        the material's name, as the tree shows it: ``"6061 Alloy"``. Pass
        ``""`` to remove the material
    configuration
        which configuration to apply it to; the active one if omitted.
        Pass ``"*"`` for every configuration
    database
        the ``.sldmat`` file, or its name without the extension.
        ``"SOLIDWORKS Materials"`` if omitted

    Examples:

        >>> set_material(part, "AISI 304")          # doctest: +SKIP
        'AISI 304'
        >>> set_material(part, "")                  # no material  # doctest: +SKIP
        ''
        >>> part.material                           # doctest: +SKIP
        ''

    Raises `SwCallError` when the material does not end up applied, which
    happens for a name the database does not contain: ``SetMaterialPropertyName2``
    returns nothing at all, and the part is left with no material.
    """
    which = configuration if configuration is not None else part.configuration

    com.call(
        part.com,
        "SetMaterialPropertyName2",
        which,
        str(database or DEFAULT_DATABASE),
        str(name),
    )

    applied = material_of(part, None if which == "*" else which)
    if str(name) and applied != str(name):
        raise SwCallError(
            f"{name!r} was not applied; the part now has "
            f"{applied or 'no material'}. The name has to be spelled as the "
            f"material tree shows it, and it has to be in "
            f"{database or DEFAULT_DATABASE!r} - see "
            f"swcomapi.api.materials.databases(app) for what is available.",
            member="SetMaterialPropertyName2",
        )
    return applied


def databases(app):
    """The material database files SOLIDWORKS is searching, as a list of str.

    Full paths to ``.sldmat`` files. The SOLIDWORKS library is the one named
    ``solidworks materials.sldmat``; anything else is a custom library
    somebody added.

    Example:

        >>> all(p.lower().endswith(".sldmat") for p in databases(app))  # doctest: +SKIP
        True
    """
    return com.to_list(com.call(app.com, "GetMaterialDatabases"))


def database_names(app):
    """The database names without their paths or extensions, as a list of str.

    The form `set_material` wants.

    Spelled as the files are on disk, which on some installs means lower case:
    this machine answers ``'solidworks materials'``. The lookup SOLIDWORKS does
    when a material is applied is not case sensitive, so either spelling works
    in `set_material`.

    Example:

        >>> "solidworks materials" in database_names(app)    # doctest: +SKIP
        True
    """
    return [
        os.path.splitext(os.path.basename(path))[0] for path in databases(app)
    ]
