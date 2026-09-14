"""Configurations, as a sequence of names.

    part.configurations                  # ['BRK-020', 'BRK-040', 'Default']
    part.configuration                   # 'Default', the active one
    part.configuration = "BRK-040"       # switch

    for name in part.configurations:
        part.configuration = name
        part.export(f"{name}.pdf")

Switching costs a rebuild, and SOLIDWORKS does it whether or not you asked, so
a loop over configurations is inherently slow. There is no way around that;
what there is a way around is doing it twice by accident, which is why
`Configurations.activate` returns early when the configuration is already
active.
"""

from collections.abc import Sequence

from .. import com
from ..errors import SwCallError


class Configurations(Sequence):
    """The configurations of a document.

    A sequence of names: iterate it, index it, ``len()`` it, ``in`` it. The
    objects behind the names are reachable with `raw`.

    Do not build this directly; use ``document.configurations``.

    Attributes:
        com  the raw ``IModelDoc2``
    """

    def __init__(self, model, document=None):
        self.com = model
        self._document = document

    # ------------------------------------------------------------ sequence

    def __getitem__(self, index):
        return self.names()[index]

    def __len__(self):
        return len(self.names())

    def __contains__(self, name):
        return str(name) in self.names()

    def __iter__(self):
        return iter(self.names())

    def names(self):
        """Every configuration name, in the order SOLIDWORKS lists them.

        As a list of str. Note that this is the creation order, not
        alphabetical and not the tree's display order.
        """
        return com.to_list(com.call(self.com, "GetConfigurationNames"))

    # -------------------------------------------------------------- active

    @property
    def active(self):
        """The active configuration's name, as a str."""
        manager = com.call(self.com, "ConfigurationManager")
        configuration = com.call(manager, "ActiveConfiguration")
        return com.call(configuration, "Name")

    def activate(self, name):
        """Make ``name`` the active configuration.

        Returns True if a switch happened, False if it was already active.
        Raises KeyError for a name that is not there, and `SwCallError` if
        SOLIDWORKS refuses.

        Switching rebuilds the model, so the early return is not just tidiness.
        """
        name = str(name)
        if name not in self.names():
            raise KeyError(
                f"no configuration named {name!r}. "
                f"This document has: {', '.join(self.names())}"
            )
        if self.active == name:
            return False
        if not com.call(self.com, "ShowConfiguration2", name):
            raise SwCallError(
                f"SOLIDWORKS refused to activate configuration {name!r}",
                member="ShowConfiguration2",
            )
        return True

    # ------------------------------------------------------------ the objects

    def raw(self, name):
        """The raw ``IConfiguration`` for ``name``.

        Raises KeyError if there is no such configuration.
        """
        configuration = com.call(self.com, "GetConfigurationByName", str(name))
        if configuration is None:
            raise KeyError(f"no configuration named {name!r}")
        return configuration

    def description_of(self, name):
        """A configuration's description, as a str. May be empty."""
        return com.call(self.raw(name), "Description") or ""

    def comment_of(self, name):
        """A configuration's comment, as a str. May be empty."""
        return com.call(self.raw(name), "Comment") or ""

    def parent_of(self, name):
        """The name of ``name``'s parent configuration, or None.

        A derived configuration has one; a top-level configuration does not.
        """
        parent = com.call(self.raw(name), "GetParent")
        return com.call(parent, "Name") if parent is not None else None

    def children_of(self, name):
        """The names of ``name``'s derived configurations, sorted.

        As a list of str.
        """
        children = com.to_list(com.call(self.raw(name), "GetChildren"))
        return sorted(com.call(child, "Name") for child in children)

    def add(self, name, description="", comment="", parent=None, activate=False):
        """Add a configuration. Returns its name, as a str.

        name
            the new configuration's name
        description
            the description, which is what a BOM shows when it is told to
        comment
            the comment, which nothing shows but a person reading the tree
        parent
            the configuration to derive from, by name; a top-level
            configuration if omitted
        activate
            True switches to it, which costs a rebuild. False by default,
            since adding a run of configurations should cost one rebuild at
            the end rather than one each.

        Raises `SwCallError` if SOLIDWORKS refuses, which it does for a name
        that is already in use, and KeyError for a parent that does not exist.

        ``IConfigurationManager.AddConfiguration`` is the one call that does
        both flavours. ``IModelDoc2.AddConfiguration3`` cannot derive, and
        there is no ``AddDerivedConfiguration`` anywhere despite the name
        appearing in older examples.

        Example::

            part.configurations.add("BRK-080", description="Long bracket")
            part.configurations.add("BRK-080-ANOD", parent="BRK-080")
        """
        from ..const import swConfigOption_DontActivate

        name = str(name)
        if parent is not None:
            self.raw(parent)  # raises KeyError if it is not there

        manager = com.call(self.com, "ConfigurationManager")
        created = com.call(
            manager,
            "AddConfiguration",
            name,
            str(comment),
            "",
            0 if activate else swConfigOption_DontActivate,
            "" if parent is None else str(parent),
            str(description),
        )
        if not created:
            raise SwCallError(
                f"SOLIDWORKS refused to add configuration {name!r}. "
                f"The usual reason is that the name is already in use.",
                member="AddConfiguration",
            )
        return name

    def __repr__(self):
        try:
            names = self.names()
            return f"<Configurations: {len(names)} - active {self.active!r}>"
        except Exception:
            return "<Configurations (not responding)>"
