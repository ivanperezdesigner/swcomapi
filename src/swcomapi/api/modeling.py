"""Making features: extrude, cut, revolve.

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

    >>> with part.sketch_on("Front Plane", add_to_db=True) as sketch:
    ...     _ = sketch.rectangle((0, 0), (60, 40))
    >>> part.extrude(10).name                   # 10 mm, blind, one direction
    'Boss-Extrude1'

    >>> _ = part.select("Boss-Extrude1", "FACE")
    >>> with part.sketch_on(add_to_db=True) as sketch:
    ...     _ = sketch.circle((30, 20), 6)
    >>> part.cut(through_all=True).name         # a hole all the way through
    'Cut-Extrude1'

Depths and offsets in **mm**, angles in **degrees**. The sketch to work from
is the one that was just closed, which SOLIDWORKS leaves selected - which is
why `swcomapi.api.sketch.SketchSession` deliberately does *not* clear the
selection on the way out. Name a sketch and these re-select it instead.

Which way a cut goes
--------------------

A cut leaves the sketch plane in the direction the plane faces, so a sketch
on the Front Plane cuts towards you - away from a boss extruded the default
way, which removes nothing at all. Sketching on the **face** instead, as
above, always cuts into the material. On a plane behind the solid, pass
``reverse=True``.
"""

from .. import com
from ..errors import SwCallError
from ..units import deg, mm


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

    Example, a 60 by 40 plate 10 mm thick::

        with part.sketch_on("Front Plane") as sketch:
            sketch.rectangle((0, 0), (60, 40))
        feature = part.extrude(10)
        feature.name                # 'Boss-Extrude1'

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

        >>> _ = part.select("Boss-Extrude1", "FACE")
        >>> with part.sketch_on(add_to_db=True) as sketch:
        ...     _ = sketch.circle((30, 20), 6)
        >>> part.cut(through_all=True).name
        'Cut-Extrude1'
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
