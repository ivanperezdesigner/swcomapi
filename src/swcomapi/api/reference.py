"""Reference geometry: planes and axes.

Nothing is modelled on these, but almost everything needs them. A sketch on
anything other than the three default planes needs a plane made for it, and a
circular pattern round anything that is not already round needs an axis.

    >>> part.plane("Top Plane", distance=25).name           # doctest: +SKIP
    'Plane1'
    >>> part.axis("Front Plane", "Right Plane").name        # doctest: +SKIP
    'Axis1'

Distances in **mm**, angles in **degrees**.

How a plane is defined
----------------------

``InsertRefPlane`` takes three pairs - a constraint and a value - and reads
the geometry from the selection, in the order it was selected. This module
turns the everyday cases into arguments:

=====================================  ==================================
what you want                          what to pass
=====================================  ==================================
parallel, 25 mm away                   ``plane(doc, "Top Plane", 25)``
through a face, angled 30 degrees      ``plane(doc, face, angle=30,
                                       second=edge)``
halfway between two faces              ``plane(doc, a, second=b,
                                       midplane=True)``
through three points                   ``plane(doc, p1, second=p2,
                                       third=p3)``
=====================================  ==================================

An angled plane needs the edge or axis it turns about as well, which is the
part people miss: a plane and an angle alone is not enough to place one.
"""

from .. import com
from ..errors import SwCallError
from ..units import deg, mm
from .selection import select


def plane(
    document,
    reference,
    distance=None,
    angle=None,
    second=None,
    third=None,
    reverse=False,
    midplane=False,
):
    """Make a reference plane. Returns the new `Feature`.

    document
        the `swcomapi.api.document.Part` or `swcomapi.api.document.Assembly`
    reference
        what to build from: a plane by name, a `swcomapi.api.geometry.Face`,
        an `swcomapi.api.geometry.Edge`, or a vertex
    distance
        offset in mm, for a plane parallel to ``reference``
    angle
        angle in degrees. Needs ``second`` as the line to turn about
    second
        a second reference, for an angle, a midplane, or three points
    third
        a third reference, for three points
    reverse
        True offsets or angles the other way
    midplane
        True puts the plane halfway between ``reference`` and ``second``

    Example, a plane 25 mm above the top:

        >>> above = part.plane("Top Plane", distance=25)     # doctest: +SKIP
        >>> above.type                                       # doctest: +SKIP
        'RefPlane'

    Example, halfway between two faces:

        >>> faces = part.bodies[0].faces_of("plane")         # doctest: +SKIP
        >>> part.plane(faces[0], second=faces[1], midplane=True).name  # doctest: +SKIP
        'Plane2'

    Raises `SwCallError` when the references do not define a plane, which is
    what an angle with no line to turn about looks like.
    """
    from ..const import (
        swRefPlaneReferenceConstraint_Angle,
        swRefPlaneReferenceConstraint_Coincident,
        swRefPlaneReferenceConstraint_Distance,
        swRefPlaneReferenceConstraint_MidPlane,
        swRefPlaneReferenceConstraint_OptionFlip,
    )
    from .features import Feature

    if angle is not None and second is None:
        raise SwCallError(
            "an angled plane turns about a line, so it needs second= as well "
            "- the edge or axis it hinges on",
            member="InsertRefPlane",
        )
    if midplane and second is None:
        raise SwCallError(
            "a midplane sits between two things, so it needs second= as well",
            member="InsertRefPlane",
        )

    references = [thing for thing in (reference, second, third) if thing is not None]
    document.clear_selection()
    for position, thing in enumerate(references):
        select(document, thing, append=position > 0)

    flip = swRefPlaneReferenceConstraint_OptionFlip if reverse else 0
    coincident = swRefPlaneReferenceConstraint_Coincident

    if midplane:
        first_constraint, first_value = swRefPlaneReferenceConstraint_MidPlane, 0.0
        second_constraint, second_value = swRefPlaneReferenceConstraint_MidPlane, 0.0
    elif distance is not None:
        first_constraint = swRefPlaneReferenceConstraint_Distance | flip
        first_value = mm(distance)
        second_constraint, second_value = (coincident if second else 0), 0.0
    elif angle is not None:
        first_constraint = swRefPlaneReferenceConstraint_Angle | flip
        first_value = deg(angle)
        second_constraint, second_value = coincident, 0.0
    else:
        first_constraint, first_value = coincident, 0.0
        second_constraint, second_value = (coincident if second else 0), 0.0

    third_constraint = coincident if third else 0

    manager = com.call(document.com, "FeatureManager")
    made = com.call(
        manager,
        "InsertRefPlane",
        first_constraint,
        first_value,
        second_constraint,
        second_value,
        third_constraint,
        0.0,
    )
    if made is None:
        raise SwCallError(
            f"SOLIDWORKS would not make a plane in {document.name!r} from "
            f"{len(references)} reference(s). A plane needs enough to fix it: "
            f"one face and a distance, two for a midplane, or three points.",
            member="InsertRefPlane",
        )
    return Feature(made, document)


def axis(document, reference, second=None):
    """Make a reference axis. Returns the new `Feature`.

    document
        the `swcomapi.api.document.Part` or `swcomapi.api.document.Assembly`
    reference
        a cylindrical face, a straight edge, a plane, or a point
    second
        a second reference where one is not enough: a second plane for the
        line where they cross, or a second point

    Example, the line where two default planes cross:

        >>> part.axis("Front Plane", "Right Plane").type     # doctest: +SKIP
        'RefAxis'

    Example, the axis of a hole, which needs nothing else:

        >>> part.axis(bore).name                             # doctest: +SKIP
        'Axis2'

    A cylindrical face already has a temporary axis that a pattern can turn
    about, so make one of these only when the axis has to be selectable by
    name later.
    """
    from .features import Feature

    document.clear_selection()
    select(document, reference, append=False)
    if second is not None:
        select(document, second, append=True)

    if not com.call(document.com, "InsertAxis2", True):
        raise SwCallError(
            f"SOLIDWORKS would not make an axis in {document.name!r}. One "
            f"cylindrical face is enough; two planes, two points or a "
            f"straight edge also work, but a single flat face does not.",
            member="InsertAxis2",
        )
    return Feature(document.features[-1].com, document)
