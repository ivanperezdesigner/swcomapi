"""Making features: extrude, cut, revolve, and the dress-up on top of them.

What is here:

============  ================================================================
`extrude`     a sketch into a boss
`cut`         a sketch out of the body
`revolve`     a sketch round an axis
`sweep`       a profile along a path
`loft`        between two or more profiles
`fillet`      rounds edges and faces
`chamfer`     breaks them at an angle
`shell`       hollows the body out
`hole`        a plain round hole, straight through a face
============  ================================================================

Patterns and mirrors are next door in `swcomapi.api.patterns`, reference
planes and axes in `swcomapi.api.reference`.

The feature calls are the widest in the API. ``FeatureExtrusion3`` takes
twenty-four arguments, most of which are about draft and start conditions
nobody uses, and the two that matter - how deep, and which way - are in the
middle of them::

    FeatureExtrusion3(Sd, Flip, Dir, T1, T2, D1, D2, Dchk1, Dchk2, Ddir1,
                      Ddir2, Dang1, Dang2, OffsetReverse1, OffsetReverse2,
                      TranslateSurface1, TranslateSurface2, Merge,
                      UseFeatScope, UseAutoSelect, T0, StartOffset,
                      FlipStartOffset)

So this module gives them defaults that match the dialog's defaults, and
names the arguments a script actually varies::

    >>> part = app.new_part()                           # doctest: +SKIP
    >>> with part.sketch_on("Front Plane", add_to_db=True) as sketch:  # doctest: +SKIP
    ...     _ = sketch.rectangle((0, 0), (60, 40))
    >>> part.extrude(10).name               # 10 mm, blind, one direction  # doctest: +SKIP
    'Boss-Extrude1'
    >>> with part.sketch_on("Front Plane", add_to_db=True) as sketch:  # doctest: +SKIP
    ...     _ = sketch.circle((30, 20), 6)
    >>> part.cut(through_all=True, reverse=True).name   # doctest: +SKIP
    'Cut-Extrude1'

Depths and offsets in **mm**, angles in **degrees**. The sketch to work from
is the one that was just closed, which SOLIDWORKS leaves selected - which is
why `swcomapi.api.sketch.SketchSession` deliberately does *not* clear the
selection on the way out. Name a sketch and these re-select it instead.

Which way a cut goes
--------------------

``reverse=True`` above is not decoration. A cut leaves its sketch plane in
one direction, and from the Front Plane that is towards the viewer - away
from a boss the default extrude put behind it. Cutting through nothing
removes nothing, and SOLIDWORKS reports that as a bare ``None``.

The alternative is to sketch on the face, which always cuts into the
material; `cut` shows it. A face is selected as an object, not by the name
of the feature that made it - ``select("Boss-Extrude1", "FACE")`` finds
nothing and returns False.
"""

from .. import com
from ..errors import SwCallError
from ..units import deg, mm
from .selection import select, select_all


def extrude(
    document,
    depth,
    sketch=None,
    both_directions=False,
    second_depth=None,
    midplane=False,
    reverse=False,
    draft=None,
    draft_outward=False,
    merge=True,
    through_all=False,
):
    """Extrude a sketch into a boss. Returns the new `Feature`.

    document
        the `swcomapi.api.document.Part` to add it to
    depth
        how far, in mm. Ignored when ``through_all`` is True
    sketch
        the sketch to use, by name. The one just closed if omitted
    both_directions
        True extrudes the other way as well, by ``second_depth`` or by
        ``depth`` again
    second_depth
        the second direction's depth in mm, when it differs
    midplane
        True splits the depth either side of the sketch plane
    reverse
        True extrudes the other way
    draft
        a draft angle in degrees, or None for none
    draft_outward
        True drafts outward rather than inward
    merge
        True merges the result into the existing body, which is the default in
        the dialog too. False leaves a separate body
    through_all
        True ignores ``depth`` and goes all the way through

    Example, a 60 by 40 plate 10 mm thick:

        >>> blank = app.new_part()                          # doctest: +SKIP
        >>> with blank.sketch_on("Front Plane", add_to_db=True) as sk:  # doctest: +SKIP
        ...     _ = sk.rectangle((0, 0), (60, 40))
        >>> blank.extrude(10).name                          # doctest: +SKIP
        'Boss-Extrude1'

    Raises `SwCallError` when SOLIDWORKS declines, which for an extrusion
    almost always means the profile is not closed, or nothing was selected.
    """
    return _extrude(
        document,
        depth,
        sketch=sketch,
        cut=False,
        both_directions=both_directions,
        second_depth=second_depth,
        midplane=midplane,
        reverse=reverse,
        draft=draft,
        draft_outward=draft_outward,
        merge=merge,
        through_all=through_all,
    )


def cut(
    document,
    depth=None,
    sketch=None,
    both_directions=False,
    second_depth=None,
    midplane=False,
    reverse=False,
    draft=None,
    draft_outward=False,
    through_all=False,
):
    """Cut a sketch out of the body. Returns the new `Feature`.

    The same arguments as `extrude`, except that ``depth`` may be left out
    when ``through_all`` is True, and there is no ``merge``.

    Example, a 12 mm hole through a plate. Sketched on the face, because a
    cut leaves its sketch plane in the direction the plane faces: from the
    Front Plane it would go towards you, away from the material, and remove
    nothing. From a plane behind the solid, pass ``reverse=True``.

        >>> front = [f for f in part.bodies[0].faces
        ...          if f.normal == (0.0, 0.0, 1.0)][0]   # doctest: +SKIP
        >>> front.select()                                # doctest: +SKIP
        True
        >>> with part.sketch_on(add_to_db=True) as sketch:   # doctest: +SKIP
        ...     _ = sketch.circle((10, 10), 3)
        >>> part.cut(through_all=True).name.startswith("Cut-Extrude")  # doctest: +SKIP
        True

    A face is an object, not a name: ``select("Boss-Extrude1", "FACE")``
    returns False, because no face is called after the feature that made it.
    """
    if depth is None and not through_all:
        raise SwCallError(
            "a cut needs either depth= in mm or through_all=True",
            member="FeatureCut4",
        )
    return _extrude(
        document,
        depth or 0.0,
        sketch=sketch,
        cut=True,
        both_directions=both_directions,
        second_depth=second_depth,
        midplane=midplane,
        reverse=reverse,
        draft=draft,
        draft_outward=draft_outward,
        merge=True,
        through_all=through_all,
    )


def _extrude(
    document,
    depth,
    sketch,
    cut,
    both_directions,
    second_depth,
    midplane,
    reverse,
    draft,
    draft_outward,
    merge,
    through_all,
):
    """``FeatureExtrusion3`` or ``FeatureCut4``, which take the same arguments.

    Kept as one function because the two calls differ in the name and in one
    trailing pair of arguments, and nothing else. Splitting them would mean
    writing the twenty-four twice.
    """
    from ..const import (
        swEndCondBlind,
        swEndCondMidPlane,
        swEndCondThroughAll,
        swStartSketchPlane,
    )
    from .features import Feature

    if sketch is not None:
        _select_sketch(document, sketch)

    if through_all:
        end_condition = swEndCondThroughAll
    elif midplane:
        end_condition = swEndCondMidPlane
    else:
        end_condition = swEndCondBlind

    angle = deg(draft) if draft else 0.0
    first = mm(depth)
    second = mm(second_depth if second_depth is not None else depth)

    # The first seventeen are the same in both calls, and then they diverge:
    # FeatureExtrusion3 goes on with Merge, and FeatureCut4 with NormalCut and
    # four more arguments about assembly scope. Getting that join wrong is
    # silent - every argument is a bool or a number, so nothing complains and
    # the feature comes out wrong.
    common = (
        not both_directions,        # Sd: single direction
        False,                      # Flip: flip the side to cut
        reverse,                    # Dir: reverse the direction
        end_condition,              # T1
        swEndCondBlind if both_directions else 0,  # T2
        first,                      # D1
        second,                     # D2
        bool(draft),                # Dchk1
        bool(draft) and both_directions,  # Dchk2
        draft_outward,              # Ddir1
        draft_outward,              # Ddir2
        angle,                      # Dang1
        angle,                      # Dang2
        False,                      # OffsetReverse1
        False,                      # OffsetReverse2
        False,                      # TranslateSurface1
        False,                      # TranslateSurface2
    )
    tail = (
        swStartSketchPlane,         # T0
        0.0,                        # StartOffset
        False,                      # FlipStartOffset
    )

    manager = com.call(document.com, "FeatureManager")
    if cut:
        arguments = common + (
            False,                  # NormalCut
            True,                   # UseFeatScope
            True,                   # UseAutoSelect
            False,                  # AssemblyFeatureScope
            False,                  # AutoSelectComponents
            False,                  # PropagateFeatureToParts
        ) + tail + (False,)         # OptimizeGeometry
        feature = com.call(manager, "FeatureCut4", *arguments)
        member = "FeatureCut4"
    else:
        arguments = common + (
            merge,                  # Merge
            True,                   # UseFeatScope
            True,                   # UseAutoSelect
        ) + tail
        feature = com.call(manager, "FeatureExtrusion3", *arguments)
        member = "FeatureExtrusion3"

    if feature is None:
        raise SwCallError(
            f"SOLIDWORKS would not {'cut' if cut else 'extrude'} in "
            f"{document.name!r}. The usual causes are a profile that is not "
            f"closed and a sketch that is not selected"
            + (
                ", and for a cut, a direction that points away from the "
                "material - a sketch on the Front Plane cuts towards you "
                "unless you pass reverse=True"
                if cut
                else ""
            )
            + ".",
            member=member,
        )
    return Feature(feature, document)


def revolve(document, angle=360.0, sketch=None, axis=None, reverse=False, merge=True):
    """Revolve a sketch into a boss. Returns the new `Feature`.

    document
        the `swcomapi.api.document.Part`
    angle
        how far round, in degrees. 360 for a full revolve
    sketch
        the sketch to use, by name; the one just closed if omitted
    axis
        the axis to turn about, by name - a centreline in the sketch, or
        ``"Front Plane"``-style geometry. The sketch's own centreline if
        omitted, which is what SOLIDWORKS picks by itself
    reverse
        True turns the other way
    merge
        True merges into the existing body

    Example, a cylinder 40 mm across and 30 tall::

        with part.sketch_on("Front Plane") as sketch:
            sketch.centreline((0, 0), (0, 30))
            sketch.rectangle((0, 0), (20, 30))
        part.revolve()
    """
    from ..const import swEndCondBlind
    from .features import Feature

    if sketch is not None:
        _select_sketch(document, sketch)
    if axis is not None:
        document.select(axis, "SKETCHSEGMENT", append=True)

    manager = com.call(document.com, "FeatureManager")
    feature = com.call(
        manager,
        "FeatureRevolve2",
        True,               # SingleDir
        True,               # IsSolid
        False,              # IsThin
        False,              # IsCut
        reverse,            # ReverseDir
        False,              # BothDirectionUpToSameEntity
        swEndCondBlind,     # Dir1Type
        swEndCondBlind,     # Dir2Type
        deg(angle),         # Dir1Angle
        0.0,                # Dir2Angle
        False,              # OffsetReverse1
        False,              # OffsetReverse2
        0.0,                # OffsetDistance1
        0.0,                # OffsetDistance2
        0,                  # ThinType
        0.0,                # ThinThickness1
        0.0,                # ThinThickness2
        merge,              # Merge
        True,               # UseFeatScope
        True,               # UseAutoSelect
    )
    if feature is None:
        raise SwCallError(
            f"SOLIDWORKS would not revolve in {document.name!r}. A revolve "
            f"needs a closed profile and an axis that does not cross it.",
            member="FeatureRevolve2",
        )
    return Feature(feature, document)


def _select_sketch(document, name):
    """Select a sketch by name, so the feature call has something to work on."""
    document.clear_selection()
    if not document.select(str(name), "SKETCH"):
        raise SwCallError(
            f"no sketch named {name!r} in {document.name!r}; "
            f"see part.sketches.names()",
            member="SelectByID2",
        )


# --------------------------------------------------------------------- dress-up
# Fillet, chamfer and shell take no geometry of their own: they work from what
# is selected. So every one of them takes the geometry as an argument and
# selects it here, and leaves the selection alone when nothing is passed, for
# the caller who has already selected by hand.


def fillet(
    document,
    radius,
    edges=None,
    propagate=True,
    keep_features=True,
    constant_width=False,
    round_corners=False,
):
    """Round edges or faces. Returns the new `Feature`.

    document
        the `swcomapi.api.document.Part`
    radius
        the fillet radius in mm
    edges
        what to round: a list of `swcomapi.api.geometry.Edge`, of
        `swcomapi.api.geometry.Face`, of names, or a single one of those.
        None uses whatever is selected already
    propagate
        True carries the fillet round tangent edges, as the dialog does
    keep_features
        True keeps features that the fillet would otherwise swallow
    constant_width
        True holds the width constant rather than the radius
    round_corners
        True rounds where three fillets meet instead of mitring them

    Example, breaking every edge of a plate at 2 mm:

        >>> block.fillet(2, edges=block.bodies[0].edges).name   # doctest: +SKIP
        'Fillet1'

    Example, one edge only. On a different part, because the fillet above
    already rounded every edge of that one - which is the everyday version of
    the same mistake: a fillet needs an edge that is still there.

        >>> longest = max(part.bodies[0].edges, key=lambda e: e.length)  # doctest: +SKIP
        >>> part.fillet(3, edges=[longest]).type            # doctest: +SKIP
        'Fillet'

    Raises `SwCallError` when SOLIDWORKS declines, which nearly always means
    nothing suitable was selected.

    **A radius that is far too big does not raise.** SOLIDWORKS makes the
    feature anyway and lets it eat the model: a 200 mm fillet on one edge of
    a 60 by 40 by 10 plate leaves a 2,156 mm3 sliver with five faces, and
    reports success. Check the volume afterwards if the radius is coming from
    somewhere you do not control.
    """
    from ..const import (
        swFeatureFilletAttachEdges,
        swFeatureFilletConstantWidth,
        swFeatureFilletCornerType,
        swFeatureFilletKeepFeatures,
        swFeatureFilletPropagate,
        swFeatureFilletType_Simple,
        swFeatureFilletUniformRadius,
        swFilletOverFlowType_Default,
    )
    from .features import Feature

    if edges is not None:
        select_all(document, _as_list(edges))

    options = swFeatureFilletUniformRadius | swFeatureFilletAttachEdges
    if propagate:
        options |= swFeatureFilletPropagate
    if keep_features:
        options |= swFeatureFilletKeepFeatures
    if constant_width:
        options |= swFeatureFilletConstantWidth
    if round_corners:
        options |= swFeatureFilletCornerType

    manager = com.call(document.com, "FeatureManager")
    feature = com.call(
        manager,
        "FeatureFillet3",
        options,
        mm(radius),                     # R1
        0.0,                            # R2, the second radius of an asymmetric
        0.0,                            # Rho, for a conic fillet
        swFeatureFilletType_Simple,     # Ftyp
        swFilletOverFlowType_Default,   # OverflowType
        0,                              # ConicRhoType
        None,                           # Radii, for a variable radius
        None,                           # Dist2Arr
        None,                           # RhoArr
        None,                           # SetBackDistances
        None,                           # PointRadiusArray
        None,                           # PointDist2Array
        None,                           # PointRhoArray
    )
    if feature is None:
        raise SwCallError(
            f"SOLIDWORKS would not fillet in {document.name!r} at "
            f"{radius} mm. Either nothing suitable was selected, or the "
            f"radius does not fit - a fillet cannot be larger than the "
            f"material beside the edge it rounds.",
            member="FeatureFillet3",
        )
    return Feature(feature, document)


def chamfer(
    document,
    distance,
    edges=None,
    angle=45.0,
    other_distance=None,
    propagate=True,
    flip=False,
):
    """Break edges or faces at an angle. Returns the new `Feature`.

    document
        the `swcomapi.api.document.Part`
    distance
        the chamfer distance in mm
    edges
        what to break, the same as `fillet` takes. None uses the selection
    angle
        the angle in degrees, used only when ``other_distance`` is None.
        45 with a single distance is the everyday chamfer
    other_distance
        the second distance in mm, for a distance-distance chamfer. Given
        this, ``angle`` is ignored
    propagate
        True carries the chamfer round tangent edges
    flip
        True swaps which face the distance is measured on, which matters
        only when the two distances differ

    Example, a 2 mm break on every edge:

        >>> block.chamfer(2, edges=block.bodies[0].edges).name  # doctest: +SKIP
        'Chamfer1'

    Example, 3 by 1 rather than 45 degrees, on one face. On a different part,
    because the chamfer above already broke every edge of that one.

        >>> top = [f for f in part.bodies[0].faces
        ...        if f.normal == (0.0, 0.0, 1.0)][0]       # doctest: +SKIP
        >>> part.chamfer(3, edges=[top], other_distance=1).type  # doctest: +SKIP
        'Chamfer'

    `Part.chamfer` is the same call. Raises `SwCallError` when SOLIDWORKS
    declines, which means the chamfer does not fit or nothing was selected.
    """
    from ..const import (
        swChamferAngleDistance,
        swChamferDistanceDistance,
        swFeatureChamferFlipDirection,
        swFeatureChamferTangentPropagation,
    )
    from .features import Feature

    if edges is not None:
        select_all(document, _as_list(edges))

    options = 0
    if propagate:
        options |= swFeatureChamferTangentPropagation
    if flip:
        options |= swFeatureChamferFlipDirection

    if other_distance is None:
        kind = swChamferAngleDistance
        second = 0.0
    else:
        kind = swChamferDistanceDistance
        second = mm(other_distance)

    manager = com.call(document.com, "FeatureManager")
    feature = com.call(
        manager,
        "InsertFeatureChamfer",
        options,
        kind,
        mm(distance),       # Width
        deg(angle),         # Angle
        second,             # OtherDist
        0.0,                # VertexChamDist1, for a vertex chamfer only
        0.0,                # VertexChamDist2
        0.0,                # VertexChamDist3
    )
    if feature is None:
        raise SwCallError(
            f"SOLIDWORKS would not chamfer in {document.name!r} at "
            f"{distance} mm. Either nothing suitable was selected, or the "
            f"chamfer is bigger than the material beside the edge.",
            member="InsertFeatureChamfer",
        )
    return Feature(feature, document)


def shell(document, thickness, faces=None, outward=False):
    """Hollow the body out, opening the given faces. Returns the new `Feature`.

    document
        the `swcomapi.api.document.Part`
    thickness
        the wall thickness in mm
    faces
        the faces to remove, as `swcomapi.api.geometry.Face` objects or
        names. None shells to a closed hollow, with no opening
    outward
        True adds the wall outside the existing surface instead of inside

    Example, a 2 mm box open at the top:

        >>> top = [f for f in block.bodies[0].faces
        ...        if f.normal == (0.0, 0.0, 1.0)][0]       # doctest: +SKIP
        >>> block.shell(2, faces=[top]).name                # doctest: +SKIP
        'Shell1'

    ``InsertFeatureShell`` answers nothing at all - not the feature, not even
    a bool - so the feature comes back from the end of the tree, and a shell
    that failed shows up as a tree that did not grow.
    """
    from .features import Feature

    if faces is not None:
        select_all(document, _as_list(faces))

    before = len(document.features)
    com.call(document.com, "InsertFeatureShell", mm(thickness), bool(outward))
    if len(document.features) == before:
        raise SwCallError(
            f"SOLIDWORKS would not shell {document.name!r} at {thickness} mm. "
            f"A shell needs a solid body, and a wall thinner than the "
            f"smallest radius in it.",
            member="InsertFeatureShell",
        )
    return Feature(document.features[-1].com, document)


def hole(
    document,
    diameter,
    at,
    depth=None,
    face=None,
    through_all=False,
    reverse=False,
):
    """Put a plain round hole through a face. Returns the new `Feature`.

    document
        the `swcomapi.api.document.Part`
    diameter
        across, in mm
    at
        where the hole goes, as an ``(x, y, z)`` point in mm **on the face**.
        Model coordinates, not sketch coordinates: this is the point the
        mouse would be over
    depth
        how deep, in mm. Ignored when ``through_all`` is True
    face
        the face to start from, as a `swcomapi.api.geometry.Face`. None picks
        whatever face lies under ``at``, which is what you want nearly always
    through_all
        True goes all the way through instead of ``depth``
    reverse
        True drills the other way

    Example, a 6 mm hole through a 10 mm plate at (15, 10):

        >>> block.hole(6, at=(15, 10, 10), through_all=True).name  # doctest: +SKIP
        'Hole1'

    This is the plain hole, not the Hole Wizard: no counterbore, no thread,
    no standard. For those, drive the Hole Wizard through ``part.com`` - the
    call takes thirty-one arguments and is not worth wrapping until somebody
    needs it.
    """
    from ..const import swEndCondBlind, swEndCondThroughAll
    from .features import Feature

    if depth is None and not through_all:
        raise SwCallError(
            "a hole needs either depth= in mm or through_all=True",
            member="SimpleHole2",
        )

    document.clear_selection()
    if face is not None:
        select(document, face)
    elif not document.select("", "FACE", at=at):
        raise SwCallError(
            f"no face of {document.name!r} lies at {tuple(at)} mm, so there "
            f"is nowhere to start the hole. The point is in model "
            f"coordinates and has to be on the face, not above it.",
            member="SelectByID2",
        )

    end = swEndCondThroughAll if through_all else swEndCondBlind
    manager = com.call(document.com, "FeatureManager")
    feature = com.call(
        manager,
        "SimpleHole2",
        mm(diameter),           # Dia
        True,                   # Sd: single direction
        False,                  # Flip
        reverse,                # Dir
        end,                    # T1
        0,                      # T2
        mm(depth or 0.0),       # D1
        0.0,                    # D2
        False, False,           # Dchk1, Dchk2
        False, False,           # Ddir1, Ddir2
        0.0, 0.0,               # Dang1, Dang2
        False, False,           # OffsetReverse1, OffsetReverse2
        False, False,           # TranslateSurface1, TranslateSurface2
        True,                   # UseFeatScope
        True,                   # UseAutoSelect
        False,                  # AssemblyFeatureScope
        False,                  # AutoSelectComponents
        False,                  # PropagateFeatureToParts
    )
    if feature is None:
        raise SwCallError(
            f"SOLIDWORKS would not drill a {diameter} mm hole in "
            f"{document.name!r}. A blind hole needs depth=; a hole wider "
            f"than the face it starts on is refused.",
            member="SimpleHole2",
        )
    return Feature(feature, document)


def sweep(document, profile=None, path=None, merge=True, keep_tangency=True):
    """Sweep a profile along a path. Returns the new `Feature`.

    document
        the `swcomapi.api.document.Part`
    profile
        the profile sketch, by name or as a `swcomapi.api.sketch.Sketch`
    path
        the path sketch, the same way
    merge
        True merges into the existing body
    keep_tangency
        True keeps the result tangent where the path is

    The profile goes in under mark 1 and the path under mark 4; pass both, or
    select them yourself with those marks and pass neither.

    Example, a 20 mm square swept along an L:

        >>> blank = app.new_part()                          # doctest: +SKIP
        >>> with blank.sketch_on("Front Plane", add_to_db=True) as sk:  # doctest: +SKIP
        ...     _ = sk.line((0, 0), (0, 60))
        ...     _ = sk.line((0, 60), (40, 60))
        >>> with blank.sketch_on("Top Plane", add_to_db=True) as sk:  # doctest: +SKIP
        ...     _ = sk.centre_rectangle((0, 0), (10, 10))
        >>> blank.sweep(profile="Sketch2", path="Sketch1").type     # doctest: +SKIP
        'Sweep'

    The profile has to be closed and the path has to start on it, which is
    the one thing SOLIDWORKS will not do for you.
    """
    from .features import Feature

    if profile is not None or path is not None:
        document.clear_selection()
    if profile is not None:
        select(document, _sketch_name(profile), mark=1)
    if path is not None:
        select(document, _sketch_name(path), mark=4)

    manager = com.call(document.com, "FeatureManager")
    feature = com.call(
        manager,
        "InsertProtrusionSwept4",
        False,              # Propagate
        False,              # Alignment
        0,                  # TwistCtrlOption
        keep_tangency,      # KeepTangency
        False,              # BAdvancedSmoothing
        0,                  # StartMatchingType
        0,                  # EndMatchingType
        False,              # IsThinBody
        0.0, 0.0,           # Thickness1, Thickness2
        0,                  # ThinType
        0,                  # PathAlign
        merge,              # Merge
        True,               # UseFeatScope
        True,               # UseAutoSelect
        0.0,                # TwistAngle
        False,              # BMergeSmoothFaces
        False,              # CircularProfile
        0.0,                # CircularProfileDiameter
        0,                  # Direction
    )
    if feature is None:
        raise SwCallError(
            f"SOLIDWORKS would not sweep in {document.name!r}. The profile "
            f"must be a closed sketch, the path a separate one, and the path "
            f"has to touch the profile.",
            member="InsertProtrusionSwept4",
        )
    return Feature(feature, document)


def loft(document, profiles=None, closed=False, merge=True, keep_tangency=True):
    """Loft between two or more profiles. Returns the new `Feature`.

    document
        the `swcomapi.api.document.Part`
    profiles
        the sketches to run through, in order, by name or as
        `swcomapi.api.sketch.Sketch`. None uses the selection
    closed
        True closes the loft back round to the first profile
    merge
        True merges into the existing body
    keep_tangency
        True keeps tangency where the profiles allow it

    Order matters: the loft runs through the profiles in the order given, and
    a list in the wrong order comes out twisted rather than failing.

        >>> blank = app.new_part()                          # doctest: +SKIP
        >>> with blank.sketch_on("Front Plane", add_to_db=True) as sk:  # doctest: +SKIP
        ...     _ = sk.centre_rectangle((0, 0), (30, 20))
        >>> above = blank.plane("Front Plane", distance=40)  # doctest: +SKIP
        >>> with blank.sketch_on(above.name, add_to_db=True) as sk:  # doctest: +SKIP
        ...     _ = sk.centre_rectangle((0, 0), (10, 8))
        >>> blank.loft(profiles=["Sketch1", "Sketch2"]).type  # doctest: +SKIP
        'Blend'

    ``'Blend'``, not ``'Loft'``: the tree calls the feature ``Loft1`` and
    ``GetTypeName2`` calls its type ``Blend``, which is what the call was
    named before the interface renamed it. ``features.of_type("Loft")``
    therefore finds nothing.
    """
    from .features import Feature

    if profiles is not None:
        names = [_sketch_name(profile) for profile in _as_list(profiles)]
        if len(names) < 2:
            raise SwCallError(
                f"a loft needs at least two profiles, not {len(names)}",
                member="InsertProtrusionBlend2",
            )
        select_all(document, names, mark=1)

    manager = com.call(document.com, "FeatureManager")
    feature = com.call(
        manager,
        "InsertProtrusionBlend2",
        closed,             # Closed
        keep_tangency,      # KeepTangency
        False,              # ForceNonRational
        1.0,                # TessToleranceFactor
        0,                  # StartMatchingType
        0,                  # EndMatchingType
        1.0, 1.0,           # StartTangentLength, EndTangentLength
        False, False,       # StartTangentDir, EndTangentDir
        False,              # IsThinBody
        0.0, 0.0,           # Thickness1, Thickness2
        0,                  # ThinType
        merge,              # Merge
        True,               # UseFeatScope
        True,               # UseAutoSelect
        0,                  # GuideCurveInfluence
    )
    if feature is None:
        raise SwCallError(
            f"SOLIDWORKS would not loft in {document.name!r}. Every profile "
            f"has to be a separate sketch, and they have to be selected in "
            f"the order the loft runs through them.",
            member="InsertProtrusionBlend2",
        )
    return Feature(feature, document)


def _as_list(value):
    """One thing or many, always as a list.

    Examples::

        >>> _as_list("Front Plane")
        ['Front Plane']
        >>> _as_list(["a", "b"])
        ['a', 'b']
        >>> _as_list(("a", "EDGE"))
        [('a', 'EDGE')]
    """
    if isinstance(value, str):
        return [value]
    if isinstance(value, tuple) and len(value) == 2 and isinstance(value[1], str):
        return [value]
    if isinstance(value, (list, tuple)):
        return list(value)
    return [value]


def _sketch_name(value):
    """A sketch given as a name, a `Sketch` or a `Feature`, as a name.

    Sweep and loft select their sketches by name, because a ``Sketch``
    absorbed into a feature has no entity to select.
    """
    name = getattr(value, "name", value)
    if not name:
        raise SwCallError(
            "a sketch being edited has no name yet; close it first",
            member="SelectByID2",
        )
    return (str(name), "SKETCH")
