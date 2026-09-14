"""Equations and global variables.

A part's equations are an ordered list of strings, and SOLIDWORKS keeps them
that way: index 0 is the first line of the Equations dialog::

    part.equations                      # ['"width" = 60', '"D1@Sketch1" = "width"']
    part.equations[0]                   # '"width" = 60'
    part.equations["width"]             # 60.0
    part.equations["width"] = 80        # rewrites that line

Global variables and driven dimensions live in the same list, told apart by
`Equations.is_global`. A global variable's line is ``"name" = value``; a
driven dimension's is ``"D1@Sketch1@part.SLDPRT" = expression``.

Units
-----

**Equations are not in metres.** They are in the document's own units, which
is the one place in this package where that is true, because an equation is a
string SOLIDWORKS parses rather than a number it stores. A part working in
millimetres has ``"width" = 60`` meaning 60 mm, and writing 80 there means
80 mm. `Equations.value_of` reads back whatever the document's units are, so
compare it against the dialog rather than against `swcomapi.units`.

Why it is worth wrapping
------------------------

``IEquationMgr.Equation(index)`` is a parameterised property: readable and
writable at the same index, with no method to find one by name. Python cannot
spell a write to one - an attribute assignment has nowhere to put the index -
so it goes through `swcomapi.com.set_property_at`. Everything here is that,
plus the lookup by name, plus not having to remember that the add takes the
index to insert *before* and ``-1`` to append.
"""

from collections.abc import Sequence

from .. import com
from ..errors import SwCallError


class Equations(Sequence):
    """The equations of a document, in the order the dialog shows them.

    A sequence of the raw lines, and a mapping by name for the values::

        part.equations.names()              # ['width', 'height']
        part.equations["width"]             # 60.0
        part.equations["width"] = 80
        part.equations.add('"depth" = 12')
        del part.equations[2]

    Attributes:
        com  the raw ``IEquationMgr``
    """

    def __init__(self, model, document=None):
        self.com = com.call(model, "GetEquationMgr")
        self.document = document

    def __len__(self):
        return int(com.call(self.com, "GetCount"))

    def __iter__(self):
        for index in range(len(self)):
            yield com.call(self.com, "Equation", index)

    def __getitem__(self, key):
        """A line by index, or a value by name.

        ``equations[0]`` is the line as written; ``equations["width"]`` is what
        that global variable evaluates to.
        """
        if isinstance(key, str):
            return self.value_of(key)
        if isinstance(key, slice):
            return list(self)[key]
        count = len(self)
        if key < 0:
            key += count
        if not 0 <= key < count:
            raise IndexError(f"the document has {count} equations, not {key + 1}")
        return com.call(self.com, "Equation", key)

    def __setitem__(self, key, value):
        """Rewrite a line by index, or a global variable's value by name.

        ``equations[0] = '"width" = 80'`` replaces the whole line.
        ``equations["width"] = 80`` keeps the name and changes the value.
        """
        if isinstance(key, str):
            index = self.index_of(key)
            if index is None:
                raise KeyError(
                    f"no equation or global variable named {key!r}; "
                    f"see .names(). Use .add() to make one."
                )
            com.set_property_at(self.com, "Equation", f'"{key}" = {value}', index)
            return
        com.set_property_at(self.com, "Equation", str(value), int(key))

    def __delitem__(self, index):
        """Delete a line by index."""
        if com.call(self.com, "Delete", int(index)) < 0:
            raise SwCallError(
                f"could not delete equation {index}; the document has "
                f"{len(self)}",
                member="Delete",
            )

    def __contains__(self, key):
        if isinstance(key, str):
            return key in self.names() or any(key == line for line in self)
        return super().__contains__(key)

    # ---------------------------------------------------------------- reading

    def names(self):
        """The names on the left of each equation, as a list of str.

        The quotes are stripped, so a global variable ``"width" = 60`` is
        listed as ``'width'`` and a driven dimension as
        ``'D1@Sketch1@plate.SLDPRT'``.
        """
        return [_name_of(line) for line in self]

    def globals(self):
        """The global variables only, as a dict of name to value.

        Example::

            part.equations.globals()        # {'width': 60.0, 'height': 40.0}
        """
        found = {}
        for index, line in enumerate(self):
            if com.call(self.com, "GlobalVariable", index):
                found[_name_of(line)] = com.call(self.com, "Value", index)
        return found

    def is_global(self, index):
        """True if the equation at ``index`` is a global variable, as a bool."""
        return bool(com.call(self.com, "GlobalVariable", int(index)))

    def value_of(self, name):
        """What ``name`` evaluates to, as a float.

        In the **document's units**, not in metres: an equation is a string
        SOLIDWORKS parses, so ``"width" = 60`` in a millimetre part reads
        back as 60.0.

        Raises KeyError when there is no equation of that name.
        """
        index = self.index_of(name)
        if index is None:
            raise KeyError(
                f"no equation or global variable named {name!r}; see .names()"
            )
        return com.call(self.com, "Value", index)

    def index_of(self, name):
        """Where ``name``'s equation is in the list, as an int, or None.

        The quotes do not have to be given: ``"width"`` and ``width`` both
        find ``"width" = 60``.
        """
        wanted = str(name).strip().strip('"')
        for index, line in enumerate(self):
            if _name_of(line) == wanted:
                return index
        return None

    # --------------------------------------------------------------- writing

    def add(self, equation, at=None, solve=True):
        """Add an equation. Returns its index, as an int.

        equation
            the whole line, as a str: ``'"width" = 60'``, or
            ``'"D1@Sketch1@plate.SLDPRT" = "width" * 2'``
        at
            insert before this index; appended at the end if omitted
        solve
            True rebuilds after adding, which is what the dialog does

        Examples::

            part.equations.add('"width" = 60')
            part.equations.add('"height" = "width" * 0.5')

        Raises `SwCallError` when SOLIDWORKS rejects it, which it does for a
        reference to a name that does not exist, an expression it cannot
        parse, and a line with no right-hand side. The raw call answers -1
        rather than complaining, which is easy to miss.

        It is forgiving about the quotes: ``width = 60`` is accepted and
        stored as written. Quoting is still the form to use, because a name
        with a space or an ``@`` in it needs it.

        Why ``Add2`` and not ``Add3``
        -----------------------------

        ``Add3`` is the current call and the one that takes a configuration
        scope, and on 2026 SP3 it returns -1 for every combination tried:
        index 0 and -1, all configurations and a named one, and the config
        names passed as None, as an empty tuple, as a list and as a SafeArray.
        ``Add2`` adds the same equation and works. So that is what is called,
        and there is no ``configurations`` argument to offer - an equation
        added here applies everywhere. Per-configuration equations have to be
        written in the dialog for now.
        """
        index = int(
            com.call(
                self.com,
                "Add2",
                -1 if at is None else int(at),
                str(equation),
                bool(solve),
            )
        )
        if index < 0:
            raise SwCallError(
                f"SOLIDWORKS would not add {equation!r}. The usual causes "
                f"are a reference to a name that is not in this document, an "
                f"expression it cannot parse, and a line with nothing on the "
                f"right of the equals sign.",
                member="Add2",
            )
        return index

    def evaluate(self):
        """Re-evaluate every equation. Returns SOLIDWORKS' own code, an int.

        The documentation calls it the number of equations that failed. It is
        not: a document whose equations all solve answers -1 on 2026 SP3. Read
        it as "it ran", and check the values you care about with `value_of`.
        """
        return int(com.call(self.com, "EvaluateAll"))

    def __repr__(self):
        count = len(self)
        globals_count = sum(1 for index in range(count) if self.is_global(index))
        return f"<Equations: {count}, {globals_count} of them global variables>"


def _name_of(line):
    """The name on the left of an equation line, as a str.

    Examples::

        >>> _name_of('"width" = 60')
        'width'
        >>> _name_of('"D1@Sketch1@plate.SLDPRT" = "width" * 2')
        'D1@Sketch1@plate.SLDPRT'
        >>> _name_of('"width"=60')
        'width'
        >>> _name_of('nonsense')
        'nonsense'
    """
    left = str(line).split("=", 1)[0]
    return left.strip().strip('"')
