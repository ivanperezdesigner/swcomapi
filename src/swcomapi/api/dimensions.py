"""Dimensions, in millimetres and degrees.

    part.dimensions["Length@Boss-Extrude1"]           # 40.0, in mm
    part.dimensions["Length@Boss-Extrude1"] = 55      # in mm
    part.dimensions["Angle@Sketch1"]                  # in degrees

The full name is the one SOLIDWORKS shows: the dimension, then ``@``, then the
feature or sketch that owns it. Hover a dimension in the model and that is what
the tooltip says.

The units, again
----------------

The API stores lengths in metres and angles in radians, whatever the document
is set to. A 40 mm extrusion is ``0.04``. This module converts both ways and
works out which conversion applies from the dimension's own type, so you never
have to remember.

Per configuration
-----------------

A dimension driven by a design table has a different value in every
configuration. ``[]`` reads the active one; `value_in` and `set_in` reach a
named one without switching::

    part.dimensions.value_in("Length@Boss-Extrude1", "BRK-040")
    part.dimensions.set_in("Length@Boss-Extrude1", "BRK-040", 40)
"""

from collections.abc import MutableMapping

from .. import com, units
from ..errors import SwCallError


def _angular_types():
    """The swDimensionType_e values that mean "this is an angle".

    Derived from the generated enumeration by name rather than written down.
    Writing them down invites exactly the mistake that was made here first
    time: 2 and 11 look like plausible angle codes and are in fact
    swLinearDimension and swHorLinearDimension, so every length would have
    been converted through radians.

    Examples::

        >>> sorted(_angular_types())
        [3, 16]
    """
    from ..generated._enum_data import ENUMS

    return frozenset(
        value
        for name, value in ENUMS["swDimensionType_e"].items()
        if "Angular" in name
    )


ANGULAR_TYPES = _angular_types()


class Dimensions(MutableMapping):
    """The dimensions of a document, keyed by full name.

    A mapping, but a lazy one: it does not walk the feature tree until you ask
    it to. ``len()`` and iteration do walk it, and on a large part that costs
    real time, so reach for ``[]`` when you know the name.

    Do not build this directly; use ``document.dimensions``.

    Attributes:
        com  the raw ``IModelDoc2``
    """

    def __init__(self, model, owner=None):
        self.com = model
        self._owner = owner

    # ------------------------------------------------------------- mapping

    def __getitem__(self, name):
        """The value in millimetres, or degrees for an angle. As a float.

        Raises KeyError if there is no such dimension.
        """
        dimension = self.raw(name)
        return _from_system(dimension, com.call(dimension, "SystemValue"))

    def __setitem__(self, name, value):
        """Set the value, in millimetres or degrees.

        The model is not rebuilt: call ``document.rebuild()`` when you have
        finished changing things, so a run of edits costs one rebuild instead
        of one each.
        """
        dimension = self.raw(name)
        dimension.SystemValue = _to_system(dimension, value)

    def __delitem__(self, name):
        raise TypeError(
            "a dimension cannot be deleted through this mapping; delete the "
            "feature or the sketch relation that owns it"
        )

    def __iter__(self):
        return iter(self.names())

    def __len__(self):
        return len(self.names())

    def __contains__(self, name):
        try:
            self.raw(name)
        except KeyError:
            return False
        return True

    # -------------------------------------------------------------- lookup

    def raw(self, name):
        """The raw ``IDimension``. Raises KeyError if there is no such name.

        ``IModelDoc2.Parameter`` returns Nothing rather than failing for a name
        that is not there, which in Python is a bare None and a confusing
        ``AttributeError`` three lines later. This turns it into a KeyError.
        """
        dimension = com.call(self.com, "Parameter", str(name))
        if dimension is None:
            raise KeyError(
                f"{name!r} is not a dimension in this document. The name is "
                f"'Dimension@Feature', as the tooltip shows it, for example "
                f"'Length@Boss-Extrude1'."
            )
        return dimension

    def names(self):
        """Every dimension's full name, sorted. As a list of str.

        Walks the feature tree, so it is the slow way in. Worth it when you do
        not know what a model is called inside.
        """
        found = []
        feature = com.call(self.com, "FirstFeature")
        while feature is not None:
            found.extend(_dimension_names(feature))
            feature = com.call(feature, "GetNextFeature")
        return sorted(found)

    # --------------------------------------------------------- per config

    def value_in(self, name, configuration):
        """The value in one configuration, without switching to it.

        In millimetres or degrees, as a float.

        ``swSpecifyConfiguration`` is the option that makes the name list
        count; ``swThisConfiguration`` reads the active one and ignores the
        names entirely, which looks like it works and does not.

        Example::

            part.dimensions.value_in("Length@Boss-Extrude1", "BRK-040")
        """
        from ..const import swSpecifyConfiguration

        dimension = self.raw(name)
        result = com.call(
            dimension,
            "GetSystemValue3",
            swSpecifyConfiguration,
            [str(configuration)],
        )
        values = com.to_list(result)
        if not values:
            raise SwCallError(
                f"{name!r} has no value in configuration {configuration!r}",
                member="GetSystemValue3",
            )
        return _from_system(dimension, values[0])

    def set_in(self, name, configuration, value):
        """Set the value in one configuration, without switching to it.

        In millimetres or degrees.
        """
        from ..const import swSpecifyConfiguration

        dimension = self.raw(name)
        com.call(
            dimension,
            "SetSystemValue3",
            _to_system(dimension, value),
            swSpecifyConfiguration,
            [str(configuration)],
        )

    # ------------------------------------------------------------ niceties

    def is_angular(self, name):
        """True if ``name`` is an angle, so its unit is degrees.

        Example::

            part.dimensions.is_angular("Angle@Sketch1")       # True
        """
        return com.call(self.raw(name), "GetType") in ANGULAR_TYPES

    def __repr__(self):
        return "<Dimensions of a document; index it by 'Dim@Feature'>"


def _dimension_names(feature):
    """Every dimension name on one feature, as a list of str."""
    names = []
    parameter = com.call(feature, "GetFirstDisplayDimension")
    while parameter is not None:
        dimension = com.call(parameter, "GetDimension2", 0)
        if dimension is not None:
            names.append(com.call(dimension, "FullName"))
        parameter = com.call(feature, "GetNextDisplayDimension", parameter)
    return names


def _is_angular(dimension):
    """True if this raw ``IDimension`` measures an angle."""
    try:
        return com.call(dimension, "GetType") in ANGULAR_TYPES
    except Exception:
        # A dimension type this release does not report is far more likely to
        # be a length than an angle, and treating an angle as a length is a
        # visible error while the reverse is a silent one.
        return False


def _from_system(dimension, value):
    """A system value to millimetres, or degrees for an angle."""
    if value is None:
        return None
    return units.to_deg(value) if _is_angular(dimension) else units.to_mm(value)


def _to_system(dimension, value):
    """Millimetres or degrees to the system value the API wants."""
    return units.deg(value) if _is_angular(dimension) else units.mm(value)
