"""The components of an assembly.

An assembly is a tree of instances, not a list of parts. The same part can be
in it eleven times, each instance with its own name, its own position and its
own suppression state, and a sub-assembly brings its own children along. Here
with the same plate inserted twice:

    >>> names = sorted(assembly.components.names())      # doctest: +SKIP
    >>> [n.split("-")[-1] for n in names]                # doctest: +SKIP
    ['1', '2']
    >>> assembly.components[names[1]].path.endswith(".SLDPRT")  # doctest: +SKIP
    True
    >>> assembly.components[names[1]].position           # doctest: +SKIP
    (70.0, -20.0, -5.0)

That second instance was inserted at ``(100, 0, 0)``, and reads back at
``(70, -20, -5)``. Both numbers are right: `Components.add` lands the
bounding-box centre on the point it is given, and `Component.position`
reports the origin, which for a 60 by 40 by 10 plate is half a plate away in
each direction.

The order is SOLIDWORKS', not the order they went in: ``GetComponents`` does
not promise insertion order, which is why that first line sorts.

`Components` is the top level; `Component.children` goes down, and
`Components.all` flattens the whole tree.

The name to use
---------------

A component has three names and they are not interchangeable:

================  ======================  ==============================
what              example                 use it for
================  ======================  ==============================
``name``          ``'rail-2'``            telling instances apart
``path``          ``'C:\\work\\rail.SLDPRT'``  which file it comes from
``select_id``     ``'rail-2@frame'``      passing to a selection call
================  ======================  ==============================

``name`` is ``IComponent2.Name2``, which for a component inside a
sub-assembly carries the whole trail: ``'sub-1/rail-2'``. That is what
SOLIDWORKS uses as the key, so it is what `Components` indexes by.
"""

from collections.abc import Sequence

from .. import com
from ..errors import SwCallError

# The suppression states a component can be in, as readable strings.
# swComponentSuppressionState_e, which has two names for the same idea:
# swComponentResolved (3) is what SetSuppression2 takes, swComponentFullyResolved
# (2) is what a resolved component with resolved children reads back as.
STATES = {
    0: "suppressed",
    1: "lightweight",
    2: "resolved",
    3: "resolved",
    4: "lightweight",
    5: "id-mismatch",
}


class Component:
    """One instance in an assembly tree.

    Attributes:
        com  the raw ``IComponent2``
    """

    def __init__(self, component, assembly=None):
        self.com = component
        self._assembly = assembly

    # ---------------------------------------------------------------- naming

    @property
    def name(self):
        """The instance name, as a str: ``'rail-2'``.

        ``IComponent2.Name2``. Inside a sub-assembly it carries the trail:
        ``'sub-1/rail-2'``.
        """
        return com.call(self.com, "Name2")

    @name.setter
    def name(self, value):
        """Rename the instance, if SOLIDWORKS is willing.

        It often is not. Renaming a component from the tree is off by default
        - Tools > Options > External References > "Allow component files to be
        renamed from FeatureManager tree" - and with it off the write is
        accepted, ignored, and reported as success. So the name is read back.
        """
        wanted = str(value)
        com.set_property(self.com, "Name2", wanted)
        if self.name != wanted:
            raise SwCallError(
                f"SOLIDWORKS kept the name {self.name!r} instead of "
                f"{wanted!r}. Renaming components from the tree is off by "
                f"default: Tools > Options > External References > 'Allow "
                f"component files to be renamed from FeatureManager tree'.",
                member="Name2",
            )

    @property
    def path(self):
        """The file this instance comes from, as a str.

        Empty for a virtual component, which lives inside the assembly file.
        """
        return com.call(self.com, "GetPathName")

    @property
    def select_id(self):
        """The name a selection call wants, as a str: ``'rail-2@frame'``."""
        return com.call(self.com, "GetSelectByIDString")

    @property
    def is_virtual(self):
        """True for a component saved inside the assembly, as a bool."""
        return bool(com.call(self.com, "IsVirtual"))

    # ------------------------------------------------------------- the model

    @property
    def document(self):
        """The part or assembly behind this instance, or None.

        A `swcomapi.api.document.Part` or `Assembly`, wrapped. None for a
        suppressed or lightweight component: there is no model loaded to
        return, which is the point of those states.

        Example, the mass of one instance:

            >>> round(assembly.components[0].document.mass, 1)   # doctest: +SKIP
            61.7
        """
        from .document import wrap

        model = com.call(self.com, "GetModelDoc2")
        if model is None:
            return None
        return wrap(model, self._assembly.app if self._assembly else None)

    @property
    def configuration(self):
        """Which configuration of the part this instance shows, as a str."""
        return com.call(self.com, "ReferencedConfiguration")

    @configuration.setter
    def configuration(self, name):
        com.set_property(self.com, "ReferencedConfiguration", str(name))

    # ---------------------------------------------------------- suppression

    @property
    def state(self):
        """The suppression state, as one of the strings in `STATES`.

        ``'resolved'``, ``'lightweight'``, ``'suppressed'`` or
        ``'id-mismatch'``. Reading `suppressed` is shorter when that is all
        you need.
        """
        code = com.call(self.com, "GetSuppression2")
        return STATES.get(int(code), f"unknown ({code})")

    @property
    def suppressed(self):
        """Whether the instance is suppressed, as a bool.

        Setting it calls `suppress` or `resolve`.
        """
        return bool(com.call(self.com, "IsSuppressed"))

    @suppressed.setter
    def suppressed(self, value):
        if value:
            self.suppress()
        else:
            self.resolve()

    def suppress(self):
        """Suppress the instance. Returns True.

        A suppressed component is not loaded, not mated and not in the mass
        properties. Raises `SwCallError` if SOLIDWORKS refuses.
        """
        from ..const import swComponentSuppressed

        return self._set_state(swComponentSuppressed, "suppress")

    def resolve(self):
        """Resolve the instance, loading its model fully. Returns True."""
        from ..const import swComponentResolved

        return self._set_state(swComponentResolved, "resolve")

    def make_lightweight(self):
        """Load the instance lightweight. Returns True.

        Graphics only, no feature tree. It is what an assembly of a thousand
        parts opens as, and plenty of API calls return nothing useful for one
        - `document` gives None.
        """
        from ..const import swComponentLightweight

        return self._set_state(swComponentLightweight, "make lightweight")

    def _set_state(self, state, what):
        """``SetSuppression2``, with its return code read as an outcome."""
        from ..const import swSuppressionChangeOk

        code = int(com.call(self.com, "SetSuppression2", state))
        if code != swSuppressionChangeOk:
            raise SwCallError(
                f"could not {what} {self.name!r}: {_suppression_error(code)}",
                member="SetSuppression2",
            )
        return True

    # ------------------------------------------------------------ appearance

    @property
    def visible(self):
        """Whether the instance is shown, as a bool.

        Hiding is not suppressing: a hidden component is still loaded, still
        mated and still in the mass properties. This is the eye in the tree.
        """
        from ..const import swComponentVisible

        return int(com.call(self.com, "Visible")) == swComponentVisible

    @visible.setter
    def visible(self, value):
        from ..const import swComponentHidden, swComponentVisible

        com.set_property(
            self.com, "Visible", swComponentVisible if value else swComponentHidden
        )

    @property
    def excluded_from_bom(self):
        """Whether the instance is left out of the bill of materials, a bool."""
        return bool(com.call(self.com, "ExcludeFromBOM"))

    @excluded_from_bom.setter
    def excluded_from_bom(self, value):
        com.set_property(self.com, "ExcludeFromBOM", bool(value))

    # -------------------------------------------------------------- position

    @property
    def fixed(self):
        """True if the instance is fixed rather than floating, as a bool."""
        return bool(com.call(self.com, "IsFixed"))

    @property
    def flexible(self):
        """True if a sub-assembly is solved flexible rather than rigid."""
        from ..const import swComponentFlexibleSolving

        return int(com.call(self.com, "Solving")) == swComponentFlexibleSolving

    @property
    def position(self):
        """Where the instance sits, as an ``(x, y, z)`` tuple in mm.

        The origin of the component in assembly coordinates, taken from
        ``GetTotalTransform``. Returns None for a component with no transform,
        which happens for one that is not loaded.

        Example, the instance inserted at ``(100, 0, 0)``. By name, not by
        index: ``GetComponents`` does not answer in insertion order.

            >>> names = sorted(assembly.components.names())  # doctest: +SKIP
            >>> assembly.components[names[1]].position       # doctest: +SKIP
            (70.0, -20.0, -5.0)

        The numbers differ from the ones given to `Components.add` because
        that lands the bounding-box centre on the point, and this is the
        origin.
        """
        from ..units import to_mm

        transform = com.call(self.com, "GetTotalTransform", True)
        if transform is None:
            return None
        data = com.to_list(com.call(transform, "ArrayData"))
        if len(data) < 12:
            return None
        # ArrayData is 16 doubles: a 3x3 rotation, then the translation at
        # 9, 10, 11, then the scale and three spare.
        return tuple(to_mm(value) for value in data[9:12])

    @property
    def box(self):
        """The bounding box in mm, as ``(x1, y1, z1, x2, y2, z2)``.

        Two opposite corners in assembly coordinates, reference planes and
        sketches left out. Returns None for a component that is not loaded.
        """
        from ..units import to_mm_all

        values = com.to_list(com.call(self.com, "GetBox", False, False))
        if len(values) < 6:
            return None
        return tuple(to_mm_all(values[:6]))

    # ------------------------------------------------------------------ tree

    @property
    def children(self):
        """The instances directly inside this one, as a list of `Component`.

        Empty for a part. A sub-assembly gives its own top level, and going
        down means recursing - or use `Components.all`.
        """
        children = com.to_list(com.call(self.com, "GetChildren"))
        return [Component(child, self._assembly) for child in children]

    def select(self, append=False):
        """Select the instance in the assembly. Returns True."""
        return bool(com.call_out(self.com, "Select4", append, None, False)[0])

    def __repr__(self):
        return f"<Component {self.name!r} {self.state}>"


class Components(Sequence):
    """The top-level components of an assembly.

    A sequence, and a mapping by name:

        >>> len(assembly.components)                # doctest: +SKIP
        2
        >>> assembly.components[0].path.endswith(".SLDPRT")   # doctest: +SKIP
        True
        >>> sorted(c.name[-1] for c in assembly.components)   # doctest: +SKIP
        ['1', '2']

    Top level only, which is what the tree shows. `all` goes all the way
    down.

    The order is ``GetComponents``' own and it is not the order the components
    were inserted in, so index into it only when you do not care which one you
    get. Look components up by name when you do.
    """

    def __init__(self, assembly):
        self.assembly = assembly

    def _raw(self, top_level_only=True):
        """``GetComponents``, which returns None for an empty assembly."""
        return com.to_list(
            com.call(self.assembly.com, "GetComponents", top_level_only)
        )

    def __len__(self):
        return len(self._raw())

    def __iter__(self):
        for component in self._raw():
            yield Component(component, self.assembly)

    def __getitem__(self, key):
        if isinstance(key, str):
            for component in self:
                if component.name == key:
                    return component
            raise KeyError(
                f"no component named {key!r} at the top level of "
                f"{self.assembly.name!r}. Names are instance names such as "
                f"'rail-2'; see .names(), and .all() for the whole tree."
            )
        components = self._raw()
        if isinstance(key, slice):
            return [Component(c, self.assembly) for c in components[key]]
        return Component(components[key], self.assembly)

    def __contains__(self, key):
        if isinstance(key, str):
            return key in self.names()
        return super().__contains__(key)

    def names(self):
        """Every top-level instance name, as a list of str."""
        return [component.name for component in self]

    def paths(self):
        """The file behind every top-level instance, as a list of str.

        Duplicates are kept: two instances of the same part are two entries,
        which is what counting parts needs. Use ``set(asm.components.paths())``
        for the distinct files.
        """
        return [component.path for component in self]

    def all(self):
        """Every component at every level, as a list of `Component`.

        ``GetComponents(False)``, so SOLIDWORKS does the walking and the order
        is its own. A sub-assembly appears before its children.
        """
        return [Component(c, self.assembly) for c in self._raw(False)]

    def of_path(self, path):
        """Every instance that comes from ``path``, as a list of `Component`.

        The match is on the file name, case-insensitively, so a full path and
        a bare ``'rail.SLDPRT'`` both work.

        Example, hiding every instance of one part:

            >>> found = assembly.components.of_path(path)   # doctest: +SKIP
            >>> len(found)                                  # doctest: +SKIP
            2
            >>> for component in found:                     # doctest: +SKIP
            ...     component.visible = False
        """
        import os

        wanted = os.path.basename(str(path)).lower()
        return [
            component
            for component in self.all()
            if os.path.basename(component.path).lower() == wanted
        ]

    def suppressed(self):
        """The instances that are suppressed, as a list of `Component`."""
        return [component for component in self.all() if component.suppressed]

    def add(self, path, at=(0.0, 0.0, 0.0), configuration=None):
        """Insert a part or sub-assembly. Returns the new `Component`.

        path
            the file to insert, as a str
        at
            where to drop it, as ``(x, y, z)`` in **mm**. SOLIDWORKS lands the
            component's bounding-box centre on that point, not its origin, so
            `Component.position` reads back a different number
        configuration
            which configuration of it to show, by name; its last-used one if
            omitted

        Example:

            >>> added = assembly.components.add(path, at=(0, 80, 0))  # doctest: +SKIP
            >>> added.path == path                          # doctest: +SKIP
            True
            >>> len(assembly.components)                    # doctest: +SKIP
            3

        The trap this removes
        ---------------------

        ``AddComponent5`` needs the file already loaded in the session. Given
        a path to something not open it does not complain, does not open it
        and does not insert it: it returns None and the assembly is unchanged,
        which is a long afternoon if you trust it. So the file is opened first
        if it is not open already, and left open, as SOLIDWORKS needs it for
        as long as the assembly refers to it.

        The assembly also has to be the active document, which it is not right
        after opening the part, so it is activated first.

        Raises FileNotFoundError if the file is not there, and `SwCallError`
        if SOLIDWORKS still declines.
        """
        import os

        from ..const import swAddComponentConfigOptions_CurrentSelectedConfig
        from ..units import mm

        target = os.path.abspath(str(path))
        if not os.path.isfile(target):
            raise FileNotFoundError(target)

        self._ensure_loaded(target)
        self._activate()

        x, y, z = at
        component = com.call(
            self.assembly.com,
            "AddComponent5",
            target,
            swAddComponentConfigOptions_CurrentSelectedConfig,
            "",
            False,
            str(configuration) if configuration else "",
            mm(x),
            mm(y),
            mm(z),
        )
        if component is None:
            raise SwCallError(
                f"SOLIDWORKS would not insert {target} into "
                f"{self.assembly.name!r}. Check that the file is a part or an "
                f"assembly and that inserting it would not be circular.",
                member="AddComponent5",
            )
        return Component(component, self.assembly)

    def _ensure_loaded(self, target):
        """Open ``target`` if the session does not already have it."""
        app = self.assembly.app
        if app is None:
            return
        import os

        open_paths = {os.path.normcase(document.path) for document in app.documents}
        if os.path.normcase(target) not in open_paths:
            app.open(target)

    def _activate(self):
        """Make the assembly the active document again.

        ``AddComponent5`` inserts into whatever document is active, not into
        the one it was called on, so getting this wrong puts the component in
        somebody else's assembly and reports success. The activation is
        checked rather than assumed.
        """
        from ..const import swDontRebuildActiveDoc

        app = self.assembly.app
        if app is None:
            return
        active = app.active
        if active is not None and active.name == self.assembly.name:
            return

        _, out = com.call_out(
            app.com,
            "ActivateDoc3",
            self.assembly.name,
            True,
            swDontRebuildActiveDoc,
            interface="ISldWorks",
        )
        active = app.active
        if active is None or active.name != self.assembly.name:
            raise SwCallError(
                f"could not bring {self.assembly.name!r} to the front, so "
                f"inserting would land in "
                f"{active.name if active else 'no document'} instead. "
                f"ActivateDoc3 reported {out.get('Errors', 0)}.",
                member="ActivateDoc3",
            )

    def __repr__(self):
        return f"<Components: {len(self)} at the top level>"


def _suppression_error(code):
    """What ``SetSuppression2``'s return code means, as a str."""
    from ..const import (
        swSuppressionBadComponent,
        swSuppressionBadState,
        swSuppressionChangeFailed,
    )

    if code == swSuppressionBadComponent:
        return "SOLIDWORKS does not recognise the component"
    if code == swSuppressionBadState:
        return "that state is not one a component can be put into"
    if code == swSuppressionChangeFailed:
        return (
            "SOLIDWORKS refused the change. Suppressing a component that "
            "others are mated to is the usual reason"
        )
    return f"SetSuppression2 returned {code}"
