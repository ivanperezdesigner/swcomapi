"""Custom properties, as a dict.

    part.properties["Material"] = "6061-T6"
    part.properties["Material"]              # '6061-T6'
    dict(part.properties)                    # every property
    "Revision" in part.properties            # True
    del part.properties["Scrap"]

Configuration-specific properties are the same object, asked a different
question::

    part.properties.of("BRK-040")["PartNo"] = "BRK-040-A"

Two things this gets right
-------------------------

**Where a property lives.** SOLIDWORKS keeps two sets: one on the file and one
per configuration, and the API reaches them through the same manager with the
configuration name passed as a string - empty for the file-level set. Reading
the wrong one is the commonest way to conclude a property "is not there".
``part.properties`` is the file-level set; ``part.properties.of(name)`` is a
configuration's own.

**Resolved against evaluated.** A property can hold an expression such as
``"D1@Sketch1"``. ``Get6`` hands back both the expression and what it
currently evaluates to. ``[]`` gives you the evaluated value, since that is
what you almost always want, and `expression_of` gives the other.
"""

from collections.abc import MutableMapping

from .. import com
from ..errors import SwCallError


class Properties(MutableMapping):
    """The custom properties of a document or one of its configurations.

    A real mapping: iterate it, ``len()`` it, ``in`` it, ``dict()`` it.

    Do not build this directly; use ``document.properties``.

    Attributes:
        com            the raw ``ICustomPropertyManager``
        configuration  the configuration name, or ``""`` for the file-level set
    """

    def __init__(self, manager, configuration="", owner=None):
        self.com = manager
        self.configuration = configuration
        self._owner = owner

    # ------------------------------------------------------------- mapping

    def __getitem__(self, name):
        """The evaluated value, as a str. Raises KeyError if absent."""
        resolved, _ = self._get(name)
        if resolved is None:
            raise KeyError(name)
        return resolved

    def __setitem__(self, name, value):
        """Add the property, or replace it if it is already there.

        Everything is written as text. SOLIDWORKS does keep a type per
        property, but a number written as text still drives a dimension and
        still shows in a BOM, while guessing the type wrongly does not.
        """
        from ..const import swCustomInfoText, swCustomPropertyReplaceValue

        result = com.call(
            self.com,
            "Add3",
            str(name),
            swCustomInfoText,
            "" if value is None else str(value),
            swCustomPropertyReplaceValue,
        )
        # Add3 returns a swCustomInfoAddResult_e; 0 and 1 both mean it worked
        # (added, and replaced).
        if result not in (0, 1):
            raise SwCallError(
                f"could not set property {name!r}: Add3 returned {result}",
                member="Add3",
            )

    def __delitem__(self, name):
        """Remove the property. Raises KeyError if it was not there."""
        if name not in self:
            raise KeyError(name)
        com.call(self.com, "Delete2", str(name))

    def __iter__(self):
        return iter(self.names())

    def __len__(self):
        return com.call(self.com, "Count")

    def __contains__(self, name):
        return str(name) in self.names()

    # -------------------------------------------------------------- reading

    def names(self):
        """Every property name, in the order SOLIDWORKS stores them.

        As a list of str.
        """
        return com.to_list(com.call(self.com, "GetNames"))

    def expression_of(self, name):
        """The stored text, before evaluation, as a str.

        For a property holding ``"D1@Sketch1"`` this gives you that, where
        ``[]`` gives you the number it currently works out to.

        Raises KeyError if the property is absent.
        """
        _, expression = self._get(name)
        if expression is None:
            raise KeyError(name)
        return expression

    def _get(self, name):
        """``(evaluated, expression)``, or ``(None, None)`` if absent.

        ``Get6``'s **return value** is what says whether the property exists:
        ``swCustomInfoGetResult_NotPresent`` (1) or
        ``swCustomInfoGetResult_ResolvedValue`` (2). Its ``[out]`` parameters
        do not - ``WasResolved`` comes back True for a property that is not
        there at all, with an empty value beside it, which is
        indistinguishable from a property that is present and empty.

        Measured on 2026 SP3: asking for a name that does not exist returns 1
        with ``{'ValOut': '', 'ResolvedValOut': '', 'WasResolved': True}``.
        """
        from ..const import swCustomInfoGetResult_NotPresent

        result, out = com.call_out(
            self.com,
            "Get6",
            str(name),
            False,
            interface="ICustomPropertyManager",
        )
        if result == swCustomInfoGetResult_NotPresent:
            return None, None
        return out.get("ResolvedValOut", ""), out.get("ValOut", "")

    # ----------------------------------------------------------- navigation

    def of(self, configuration):
        """The properties of one configuration, as another `Properties`.

        Example::

            part.properties.of("BRK-040")["PartNo"] = "BRK-040-A"
        """
        if self._owner is None:
            raise SwCallError(
                "this Properties was built without its document, so it cannot "
                "reach another configuration's properties",
                member="of",
            )
        return self._owner.properties_of(configuration)

    # -------------------------------------------------------------- niceties

    def __repr__(self):
        where = f" of {self.configuration!r}" if self.configuration else ""
        try:
            return f"<Properties{where}: {len(self)} propertie(s)>"
        except Exception:
            return f"<Properties{where} (not responding)>"
