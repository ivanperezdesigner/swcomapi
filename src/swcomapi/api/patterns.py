"""Repeating features: linear, circular and mirrored.

A pattern is three things at once - what to repeat, which way to go, and how
many - and the API takes only the third as arguments. The first two are
selections, filed under marks that nothing in the documentation lists
together:

* mark 1: the direction, or the axis
* mark 2: the second direction, or the mirror plane
* mark 4: the features to repeat

Get a mark wrong and the call still succeeds, with a pattern that went the
wrong way. So these functions take the features and the direction as
arguments and do the marking themselves:

    >>> part.patterns.linear("Cut-Extrude1", edge, count=3, spacing=15)
    ... # doctest: +SKIP
    <Feature 'LPattern1' (LPattern)>

Spacings in **mm**, angles in **degrees**, as everywhere in ``swcomapi.api``.

What counts as a direction
--------------------------

Anything straight: an edge of the model, a reference axis, a temporary axis,
a linear sketch segment, or a flat face - a face gives its normal. A cylinder
gives its own axis, which is the quickest way to point a pattern along a hole
without making an axis for it.
"""

from .. import com
from ..errors import SwCallError
from ..units import deg, mm
from .selection import select, select_all

# The marks these three calls read their selections from.
DIRECTION_1 = 1
DIRECTION_2 = 2
MIRROR_ABOUT = 2
FEATURES = 4


def linear(
    document,
    features,
    direction,
    count,
    spacing,
    second_direction=None,
    second_count=1,
    second_spacing=0.0,
    reverse=False,
    reverse_second=False,
    geometry_pattern=False,
):
    """Repeat features along one or two directions. Returns the new `Feature`.

    document
        the `swcomapi.api.document.Part` or `swcomapi.api.document.Assembly`
    features
        what to repeat: a `swcomapi.api.features.Feature`, a name, or a list
        of either
    direction
        what to go along: an edge, an axis, a face, or a name
    count
        how many instances **including the original**, as an int. 4 gives the
        original and three copies, which is what the dialog means too
    spacing
        the gap between instances, in mm
    second_direction
        a second direction, for a grid. None for a single row
    second_count
        how many in the second direction, including the first row
    second_spacing
        the gap in the second direction, in mm
    reverse
        True goes the other way along ``direction``
    reverse_second
        True goes the other way along ``second_direction``
    geometry_pattern
        True copies the geometry rather than re-solving the feature at every
        instance. Faster, and the only way a pattern of a feature that ends
        on a curved face will solve

    Example, three holes 15 mm apart along the longest edge:

        >>> along = max(part.bodies[0].edges, key=lambda e: e.length)  # doctest: +SKIP
        >>> part.patterns.linear("Cut-Extrude1", along, count=3, spacing=15).name
        ... # doctest: +SKIP
        'LPattern1'

    Raises `SwCallError` when SOLIDWORKS declines. The usual cause is an
    instance that lands off the body, which SOLIDWORKS refuses rather than
    dropping - suppress the instances in the dialog, or move the pattern.
    """
    from .features import Feature

    if count < 1:
        raise SwCallError(
            f"count is how many instances there are in total, including the "
            f"original, so it is at least 1, not {count}",
            member="FeatureLinearPattern5",
        )

    document.clear_selection()
    select(document, direction, mark=DIRECTION_1)
    if second_direction is not None:
        select(document, second_direction, mark=DIRECTION_2)
    select_all(document, _as_list(features), mark=FEATURES, append=True)

    manager = com.call(document.com, "FeatureManager")
    feature = com.call(
        manager,
        "FeatureLinearPattern5",
        int(count),                 # Num1
        mm(spacing),                # Spacing1
        int(second_count),          # Num2
        mm(second_spacing),         # Spacing2
        bool(reverse),              # FlipDir1
        bool(reverse_second),       # FlipDir2
        "",                         # DName1, a dimension to drive instead
        "",                         # DName2
        bool(geometry_pattern),     # GeometryPattern
        False,                      # VaryInstance
        False, False,               # HasOffset1, HasOffset2
        False, False,               # CtrlByNum1, CtrlByNum2
        False, False,               # FromCentroid1, FromCentroid2
        False, False,               # RevOffset1, RevOffset2
        0.0, 0.0,                   # Offset1, Offset2
        False,                      # D2PatternSeedOnly
        False,                      # SyncSubAssemblies
    )
    if feature is None:
        raise SwCallError(
            f"SOLIDWORKS would not pattern in {document.name!r}. Either the "
            f"direction is not a straight thing it can follow, or an "
            f"instance lands off the body.",
            member="FeatureLinearPattern5",
        )
    return Feature(feature, document)


def circular(
    document,
    features,
    axis,
    count,
    angle=360.0,
    equal_spacing=True,
    reverse=False,
    geometry_pattern=False,
    symmetric=False,
):
    """Repeat features round an axis. Returns the new `Feature`.

    document
        the `swcomapi.api.document.Part` or `swcomapi.api.document.Assembly`
    features
        what to repeat, the same as `linear` takes
    axis
        what to turn about: a reference axis, a temporary axis, a cylindrical
        face, a circular edge, or a name
    count
        how many instances **including the original**, as an int
    angle
        how far round, in degrees. 360 with ``equal_spacing`` spreads them
        evenly all the way round; anything less fills that sector
    equal_spacing
        True treats ``angle`` as the total to divide up. False treats it as
        the gap between one instance and the next
    reverse
        True turns the other way
    geometry_pattern
        True copies the geometry rather than re-solving the feature
    symmetric
        True mirrors the pattern about the axis as well

    Example, four more holes round the one in the middle:

        >>> part.patterns.circular("Cut-Extrude1", bore, count=4).name
        ... # doctest: +SKIP
        'CirPattern1'

    A cylindrical face is its own axis, which saves making one. The
    temporary axis of a revolve works too, and is called ``"Axis1"`` only if
    somebody made a real one.
    """
    from .features import Feature

    if count < 1:
        raise SwCallError(
            f"count is how many instances there are in total, including the "
            f"original, so it is at least 1, not {count}",
            member="FeatureCircularPattern5",
        )

    document.clear_selection()
    select(document, axis, mark=DIRECTION_1)
    select_all(document, _as_list(features), mark=FEATURES, append=True)

    manager = com.call(document.com, "FeatureManager")
    feature = com.call(
        manager,
        "FeatureCircularPattern5",
        int(count),                 # Number
        deg(angle),                 # Spacing
        bool(reverse),              # FlipDirection
        "",                         # DName
        bool(geometry_pattern),     # GeometryPattern
        bool(equal_spacing),        # EqualSpacing
        False,                      # VaryInstance
        False,                      # SyncSubAssemblies
        False,                      # BDir2
        bool(symmetric),            # BSymmetric
        1,                          # Number2
        0.0,                        # Spacing2
        "",                         # DName2
        False,                      # EqualSpacing2
    )
    if feature is None:
        raise SwCallError(
            f"SOLIDWORKS would not pattern in {document.name!r} round "
            f"{axis!r}. A circular pattern needs something round to turn "
            f"about: an axis, a cylindrical face or a circular edge.",
            member="FeatureCircularPattern5",
        )
    return Feature(feature, document)


def mirror(document, features, about, merge=True, geometry_pattern=False):
    """Mirror features about a plane or a face. Returns the new `Feature`.

    document
        the `swcomapi.api.document.Part`
    features
        what to mirror, the same as `linear` takes
    about
        the plane or flat face to mirror across: ``"Right Plane"``, a
        `swcomapi.api.geometry.Face`, or a name
    merge
        True merges the mirrored result into the body it came from
    geometry_pattern
        True copies the geometry rather than re-solving the feature

    Example, a plate mirrored to the other side of the Right Plane:

        >>> block.mirror("Boss-Extrude1", about="Right Plane").name  # doctest: +SKIP
        'Mirror1'

    To mirror the whole body rather than a feature, pass the body instead of
    its name: ``block.mirror(block.bodies[0], about="Right Plane")``.
    """
    from .features import Feature
    from .geometry import Body

    to_mirror = _as_list(features)
    mirror_body = any(isinstance(thing, Body) for thing in to_mirror)

    document.clear_selection()
    select_all(document, to_mirror, mark=FEATURES if not mirror_body else 1)
    select(document, about, mark=MIRROR_ABOUT)

    manager = com.call(document.com, "FeatureManager")
    feature = com.call(
        manager,
        "InsertMirrorFeature2",
        mirror_body,                # BMirrorBody
        bool(geometry_pattern),     # BGeometryPattern
        bool(merge),                # BMerge
        False,                      # BKnit
        0,                          # ScopeOptions
    )
    if feature is None:
        raise SwCallError(
            f"SOLIDWORKS would not mirror in {document.name!r} about "
            f"{about!r}. The thing mirrored about has to be a plane or a "
            f"flat face, and the mirrored feature has to have somewhere to "
            f"land.",
            member="InsertMirrorFeature2",
        )
    return Feature(feature, document)


class Patterns:
    """The pattern calls, hanging off a document.

    Reached as ``part.patterns``; not meant to be built directly.

        >>> part.patterns.linear("Cut-Extrude1", edge, 3, 15)   # doctest: +SKIP
        <Feature 'LPattern1' (LPattern)>
        >>> part.patterns.circular("Cut-Extrude1", bore, 4)     # doctest: +SKIP
        <Feature 'CirPattern1' (CirPattern)>
    """

    def __init__(self, document):
        self.document = document

    def linear(self, features, direction, count, spacing, **options):
        """Repeat along a direction. See `swcomapi.api.patterns.linear`."""
        return linear(self.document, features, direction, count, spacing, **options)

    def circular(self, features, axis, count, angle=360.0, **options):
        """Repeat round an axis. See `swcomapi.api.patterns.circular`."""
        return circular(self.document, features, axis, count, angle, **options)

    def mirror(self, features, about, **options):
        """Mirror across a plane. See `swcomapi.api.patterns.mirror`."""
        return mirror(self.document, features, about, **options)

    def __repr__(self):
        return f"<Patterns of {self.document.name!r}>"


def _as_list(value):
    """One thing or many, always as a list.

    Examples::

        >>> _as_list("Cut-Extrude1")
        ['Cut-Extrude1']
        >>> _as_list(["a", "b"])
        ['a', 'b']
    """
    if isinstance(value, str):
        return [value]
    if isinstance(value, tuple) and len(value) == 2 and isinstance(value[1], str):
        return [value]
    if isinstance(value, (list, tuple)):
        return list(value)
    return [value]
