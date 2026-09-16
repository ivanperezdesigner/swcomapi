"""Mates: what holds an assembly together.

Inserting a component puts it somewhere; a mate is what stops it moving. The
API takes both halves as a selection and everything else as arguments, and
answers with a status code that is easy to ignore:

    >>> first, second = assembly.components.in_order()       # doctest: +SKIP
    >>> assembly.mates.coincident(first.plane("Front Plane"),
    ...                           second.plane("Front Plane"))  # doctest: +SKIP
    <Mate 'Coincident1' coincident>
    >>> assembly.mates.names()                               # doctest: +SKIP
    ['Coincident1']

Distances in **mm**, angles in **degrees**.

What can be mated
-----------------

Faces, edges, vertices, planes and axes - of components, not of the assembly.
A face reached through ``component.document.bodies`` belongs to the part file
and cannot be mated; the one to use comes from the component, which is what
`swcomapi.api.components.Component.faces` is for.

Alignment
---------

``'closest'`` is the default and is what a person clicking gets: SOLIDWORKS
picks whichever of aligned and anti-aligned needs the component to move
least. Say ``'aligned'`` or ``'anti'`` when the result has to be repeatable
whatever position the component starts in - a script that inserts and mates
in one go is exactly that case.

Why a mate fails
----------------

``AddMate5`` answers a status from ``swAddMateError_e`` and returns an
``IMate2`` anyway in some of the failure cases, so a caller that only checks
for None sees success. This module reads the status and raises.

And the status reads backwards. ``swAddMateError_NoError`` is **1**;
``swAddMateError_ErrorUknown`` - Dassault's spelling - is **0**. Every other
status in the API is zero for success, so the obvious ``if status:`` rejects
every mate that worked. `NO_MATE_ERROR` is here so that is written down once.
"""

from collections.abc import Sequence

from .. import com
from ..errors import SwCallError
from ..units import deg, mm, to_deg, to_mm
from .selection import select

# swMateType_e, as readable names. The ones a script uses; the rest come back
# as their number, which is enough to see what is there.
MATE_TYPES = {
    0: "coincident",
    1: "concentric",
    2: "perpendicular",
    3: "parallel",
    4: "tangent",
    5: "distance",
    6: "angle",
    8: "symmetric",
    9: "cam follower",
    10: "gear",
    11: "width",
    12: "lock to sketch",
    13: "rack and pinion",
    15: "path",
    16: "lock",
    17: "screw",
    21: "slot",
    22: "hinge",
    24: "profile centre",
}

# swMateAlign_e.
ALIGNMENTS = {"aligned": 0, "anti": 1, "closest": 2}

# swAddMateError_e, in the words the dialog uses.
#
# Read the numbers twice. This enumeration does not follow the convention
# every other status in the API follows: **1 is success** and **0 is an
# unknown failure**. Treating 0 as "no error" - which is what anyone who has
# used the rest of the API will do - means every mate that worked is reported
# as broken, and every mate that failed for a reason SOLIDWORKS could not name
# is reported as fine.
NO_MATE_ERROR = 1

MATE_ERRORS = {
    0: "SOLIDWORKS did not say why",
    1: "no error",
    2: "the mate type does not match what was selected",
    3: "the alignment is wrong for that mate",
    4: "one of the selections is not something that can be mated",
    5: "the mate would over-define the assembly",
    6: "the gear ratio is not usable",
}


class Mate:
    """One mate in an assembly.

    Attributes:
        com  the raw ``IMate2``
    """

    def __init__(self, mate, feature=None, document=None):
        self.com = mate
        self._feature = feature
        self.document = document

    @property
    def name(self):
        """The mate's name as the tree shows it, as a str: ``'Coincident1'``."""
        if self._feature is None:
            return ""
        return com.call(self._feature, "Name")

    @property
    def kind(self):
        """What sort of mate it is, as a str: ``'coincident'``, ``'distance'``.

        One of the values of `MATE_TYPES`.
        """
        code = int(com.call(self.com, "Type"))
        return MATE_TYPES.get(code, f"unknown ({code})")

    @property
    def alignment(self):
        """How the two halves face each other, as a str.

        ``'aligned'``, ``'anti'`` or ``'closest'``.
        """
        code = int(com.call(self.com, "Alignment"))
        for name, value in ALIGNMENTS.items():
            if value == code:
                return name
        return f"unknown ({code})"

    @property
    def distance(self):
        """The mate's distance in mm, as a float, or None if it has none."""
        if self.kind != "distance":
            return None
        return _dimension_of(self.com, angular=False)

    @property
    def angle(self):
        """The mate's angle in degrees, as a float, or None if it has none."""
        if self.kind != "angle":
            return None
        return _dimension_of(self.com, angular=True)

    def delete(self):
        """Remove the mate. Returns True.

        The component it held stays where it was, floating, which is what
        deleting a mate in the interface does too.
        """
        if self._feature is None:
            raise SwCallError(
                "this mate was not reached through the tree, so there is no "
                "feature to delete; find it again in assembly.mates",
                member="EditDelete",
            )
        self.document.clear_selection()
        com.call(self._feature, "Select2", False, 0)
        com.call(self.document.com, "EditDelete")
        return True

    def __repr__(self):
        detail = ""
        if self.kind == "distance":
            value = self.distance
            detail = f" {value:.1f} mm" if value is not None else ""
        elif self.kind == "angle":
            value = self.angle
            detail = f" {value:.1f} deg" if value is not None else ""
        return f"<Mate {self.name!r} {self.kind}{detail}>"


class Mates(Sequence):
    """The mates of an assembly, and the calls that add more.

    A sequence, and a lookup by name:

        >>> first, second = assembly.components.in_order()   # doctest: +SKIP
        >>> _ = assembly.mates.coincident(first.plane("Top Plane"),
        ...                               second.plane("Top Plane"))  # doctest: +SKIP
        >>> assembly.mates.names()                          # doctest: +SKIP
        ['Coincident1']
        >>> assembly.mates["Coincident1"].kind              # doctest: +SKIP
        'coincident'
        >>> len(assembly.mates)                             # doctest: +SKIP
        1

    Reached as ``assembly.mates``; not meant to be built directly.
    """

    def __init__(self, document):
        self.document = document

    # ------------------------------------------------------------- reading

    def _entries(self):
        """``(feature, IMate2)`` for every mate in the tree.

        Mates live under the MateGroup folder, and each one is a feature whose
        specific feature is the ``IMate2``. A mate added to a sub-assembly is
        in that sub-assembly's tree, not this one.
        """
        found = []
        for feature in self.document.features:
            if not feature.type.startswith("MateGroup"):
                continue
            for child in feature.children:
                mate = com.call(child.com, "GetSpecificFeature2")
                if mate is not None:
                    found.append((child.com, mate))
        return found

    def __len__(self):
        return len(self._entries())

    def __iter__(self):
        for feature, mate in self._entries():
            yield Mate(mate, feature, self.document)

    def __getitem__(self, key):
        if isinstance(key, str):
            for mate in self:
                if mate.name == key:
                    return mate
            raise KeyError(
                f"no mate named {key!r} in {self.document.name!r}; see .names()"
            )
        entries = self._entries()
        if isinstance(key, slice):
            return [Mate(m, f, self.document) for f, m in entries[key]]
        feature, mate = entries[key]
        return Mate(mate, feature, self.document)

    def names(self):
        """Every mate name, in tree order. As a list of str."""
        return [mate.name for mate in self]

    def of_kind(self, kind):
        """Every mate of one sort, as a list of `Mate`.

        ``kind`` is one of the values of `MATE_TYPES`: ``'concentric'``.
        """
        return [mate for mate in self if mate.kind == kind]

    # ------------------------------------------------------------- writing

    def add(
        self,
        first,
        second,
        kind,
        distance=None,
        angle=None,
        align="closest",
        flip=False,
        lock_rotation=False,
    ):
        """Add a mate between two things. Returns the new `Mate`.

        first, second
            what to mate: faces, edges, vertices, planes or axes belonging to
            components of this assembly
        kind
            one of the values of `MATE_TYPES`, or a ``swMateType_e`` number
        distance
            the gap in mm, for a distance mate
        angle
            the angle in degrees, for an angle mate
        align
            ``'closest'``, ``'aligned'`` or ``'anti'``
        flip
            True flips the mate over, which for a distance mate is which side
            of the gap the component sits on
        lock_rotation
            True stops a concentric mate from spinning

        The named methods below - `coincident`, `concentric`, `distance`
        and the rest - are this call with ``kind`` filled in, and read better.

        Raises `SwCallError` with the reason SOLIDWORKS gave, decoded through
        `MATE_ERRORS`, because ``AddMate5`` reports failure in a status
        parameter and still hands back an object.
        """
        kind_value = _mate_type(kind)
        align_value = _alignment(align)

        self.document.clear_selection()
        select(self.document, first, append=False)
        select(self.document, second, append=True)

        made, out = com.call_out(
            self.document.com,
            "AddMate5",
            kind_value,                     # MateTypeFromEnum
            align_value,                    # AlignFromEnum
            bool(flip),                     # Flip
            mm(distance or 0.0),            # Distance
            mm(distance or 0.0),            # DistanceAbsUpperLimit
            mm(distance or 0.0),            # DistanceAbsLowerLimit
            0.0, 0.0,                       # GearRatioNumerator, Denominator
            deg(angle or 0.0),              # Angle
            deg(angle or 0.0),              # AngleAbsUpperLimit
            deg(angle or 0.0),              # AngleAbsLowerLimit
            False,                          # ForPositioningOnly
            bool(lock_rotation),            # LockRotation
            0,                              # WidthMateOption
        )
        status = int(out.get("ErrorStatus", NO_MATE_ERROR))
        if made is None or status != NO_MATE_ERROR:
            raise SwCallError(
                f"SOLIDWORKS would not add a {kind} mate in "
                f"{self.document.name!r}: "
                f"{MATE_ERRORS.get(status, f'status {status}')}. Both halves "
                f"have to belong to components of this assembly, and a face "
                f"read from component.document belongs to the part file "
                f"instead.",
                member="AddMate5",
            )
        return self[-1] if len(self) else Mate(made, None, self.document)

    def coincident(self, first, second, **options):
        """Make two faces, edges or points touch. Returns the new `Mate`."""
        return self.add(first, second, "coincident", **options)

    def concentric(self, first, second, **options):
        """Line two round things up on the same axis. Returns the new `Mate`."""
        return self.add(first, second, "concentric", **options)

    def distance(self, first, second, value, **options):
        """Hold two things a fixed distance apart, in mm. Returns a `Mate`."""
        return self.add(first, second, "distance", distance=value, **options)

    def parallel(self, first, second, **options):
        """Keep two things parallel. Returns the new `Mate`."""
        return self.add(first, second, "parallel", **options)

    def perpendicular(self, first, second, **options):
        """Keep two things square to each other. Returns the new `Mate`."""
        return self.add(first, second, "perpendicular", **options)

    def tangent(self, first, second, **options):
        """Keep a round thing touching a flat or round one. Returns a `Mate`."""
        return self.add(first, second, "tangent", **options)

    def angle(self, first, second, value, **options):
        """Hold two things at a fixed angle, in degrees. Returns a `Mate`."""
        return self.add(first, second, "angle", angle=value, **options)

    def lock(self, first, second, **options):
        """Freeze one component relative to another. Returns the new `Mate`."""
        return self.add(first, second, "lock", **options)

    def __repr__(self):
        return f"<Mates: {len(self)} in {self.document.name!r}>"


def _mate_type(kind):
    """A mate kind as a ``swMateType_e`` number, from a name or a number.

    Examples::

        >>> _mate_type("concentric")
        1
        >>> _mate_type(5)
        5
    """
    if isinstance(kind, int):
        return kind
    wanted = str(kind).lower()
    for code, name in MATE_TYPES.items():
        if name == wanted:
            return code
    raise SwCallError(
        f"no mate called {kind!r}; the kinds are "
        + ", ".join(sorted(MATE_TYPES.values())),
        member="AddMate5",
    )


def _alignment(align):
    """An alignment as a ``swMateAlign_e`` number, from a name or a number.

    Examples::

        >>> _alignment("aligned")
        0
        >>> _alignment("closest")
        2
    """
    if isinstance(align, int):
        return align
    try:
        return ALIGNMENTS[str(align).lower()]
    except KeyError:
        raise SwCallError(
            f"alignment is 'aligned', 'anti' or 'closest', not {align!r}",
            member="AddMate5",
        ) from None


def _dimension_of(mate, angular):
    """The value a distance or angle mate is driven by, in mm or degrees.

    None when the mate has no dimension, which is every mate but those two.
    """
    dimension = com.call(mate, "DisplayDimension2", 0)
    if dimension is None:
        return None
    measured = com.call(dimension, "GetDimension")
    if measured is None:
        return None
    value = com.call(measured, "SystemValue")
    return to_deg(value) if angular else to_mm(value)
