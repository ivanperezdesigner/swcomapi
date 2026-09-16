"""Selecting the things a feature call works from.

Almost every feature in SOLIDWORKS is made out of what is selected when the
call is made. ``FeatureFillet3`` takes a radius and nothing else: which edges
it rounds is whatever was selected beforehand. Worse, the bigger calls want
their inputs sorted into **marks** - a linear pattern reads the direction from
the selection marked 1 and the features to repeat from the selection marked 4
- and a mark that lands on the wrong item fails silently, with a feature that
comes out wrong rather than an error.

So this module is the one place that knows how to select something:

    >>> select(part, part.bodies[0].edges[0])                  # doctest: +SKIP
    True
    >>> select_all(part, part.bodies[0].edges)                 # doctest: +SKIP
    14
    >>> select_all(part, [part.features["Cut-Extrude1"]], mark=4)  # doctest: +SKIP
    1

What can be selected
--------------------

* a wrapper from this package - `swcomapi.api.geometry.Face`,
  `swcomapi.api.geometry.Edge`, `swcomapi.api.geometry.Body`,
  `swcomapi.api.features.Feature`, `swcomapi.api.sketch.Sketch`,
  `swcomapi.api.components.Component`
* a raw COM object, which is asked to select itself the same way
* a ``(name, kind)`` tuple, for ``SelectByID2``: ``("Front Plane", "PLANE")``
* a plain string, which is looked up as a feature, a plane and then a sketch,
  in that order

The marks, in one place
-----------------------

They are not documented together anywhere, and guessing costs an afternoon:

===========================  ====  ==========================================
call                         mark  what goes in it
===========================  ====  ==========================================
``FeatureLinearPattern5``     1    the edge or axis giving direction 1
``FeatureLinearPattern5``     2    the edge or axis giving direction 2
``FeatureLinearPattern5``     4    the features to repeat
``FeatureCircularPattern5``   1    the axis to turn about
``FeatureCircularPattern5``   4    the features to repeat
``InsertMirrorFeature2``      1    the features to mirror
``InsertMirrorFeature2``      2    the face or plane to mirror about
``InsertProtrusionSwept4``    1    the profile sketch
``InsertProtrusionSwept4``    4    the path sketch
``InsertRefPlane``          0,1,2  the references, one mark each, in order
===========================  ====  ==========================================

Two of those are worth saying out loud, because both were wrong in this
package until a live run caught them:

* ``InsertMirrorFeature2`` takes the features on **mark 1**, not mark 4. It
  is the only call here that does.
* ``InsertRefPlane`` gives every reference **its own mark** - 0, then 1, then
  2. Put two references on mark 0, which is what selecting two things
  normally gives you, and no constraint pair in
  ``swRefPlaneReferenceConstraints_e`` makes a plane at all.
"""

from .. import com
from ..errors import SwCallError

# What a bare string is looked up as, in order. A feature name is by far the
# most common thing to name, and "Front Plane" is a feature too - but only
# BODYFEATURE matches a modelling feature, so both have to be tried.
STRING_KINDS = ("BODYFEATURE", "PLANE", "SKETCH", "FACE", "EDGE", "AXIS")


def select(document, thing, mark=0, append=True):
    """Select one thing, with a mark. Returns True.

    document
        the `swcomapi.api.document.Document` the thing belongs to
    thing
        a wrapper, a raw COM object, a ``(name, kind)`` tuple or a name
    mark
        the mark to file it under, as an int. 0 for calls that do not sort
        their inputs
    append
        False clears the selection first. True is the default here, unlike
        the raw API, because these calls are nearly always building up a
        selection of several things

    Raises `SwCallError` when SOLIDWORKS will not select it, which for a name
    means the name is not there and for an object means the object belongs to
    a document that has been closed.
    """
    if not append:
        document.clear_selection()

    if isinstance(thing, str):
        return _select_named(document, thing, None, mark, append)
    if isinstance(thing, tuple) and len(thing) == 2:
        return _select_named(document, thing[0], thing[1], mark, append)

    target = getattr(thing, "com", thing)
    if not _select_object(document, target, mark, append):
        raise SwCallError(
            f"SOLIDWORKS would not select {thing!r} in {document.name!r}. "
            f"An object selects only in the document it came from, and only "
            f"while that document is still open.",
            member="Select4",
        )
    return True


def select_all(document, things, mark=0, append=False):
    """Select several things under one mark. Returns how many, as an int.

    ``append=False`` here, because a list is normally the whole of what the
    call should work from. Pass True to add to a selection already built.

    Example, every edge of a block, ready for a fillet:

        >>> select_all(part, part.bodies[0].edges)          # doctest: +SKIP
        14
    """
    count = 0
    for position, thing in enumerate(things):
        select(document, thing, mark=mark, append=append or position > 0)
        count += 1
    return count


def selection_data(document, mark):
    """An ``ISelectData`` carrying ``mark``, or None for mark 0.

    ``Select4`` accepts a null ``ISelectData``, and building one for every
    unmarked selection is a COM round trip for nothing.
    """
    if not mark:
        return None
    manager = com.call(document.com, "SelectionManager")
    data = com.call(manager, "CreateSelectData")
    com.set_property(data, "Mark", int(mark))
    return data


def selected(document, mark=-1):
    """How many things are selected under ``mark``, as an int.

    ``mark=-1`` counts everything, whatever its mark, which is what
    ``GetSelectedObjectCount2`` means by -1.
    """
    manager = com.call(document.com, "SelectionManager")
    return int(com.call(manager, "GetSelectedObjectCount2", int(mark)))


def _select_object(document, target, mark, append):
    """``Select2`` for a feature, ``Select4`` for anything else.

    ``IFeature`` takes the mark as a plain int and has no ``Select4``;
    everything else takes an ``ISelectData``. Telling them apart by asking
    for ``GetTypeName2`` is cheaper than catching the failure of the wrong
    call, which leaves the selection half built.
    """
    if _is_feature(target):
        return bool(com.call(target, "Select2", append, int(mark)))

    data = selection_data(document, mark)
    if _is_component(target):
        return bool(com.call(target, "Select4", append, data, False))
    return bool(com.call(target, "Select4", append, data))


def _is_feature(target):
    """True if ``target`` is an ``IFeature``, as a bool."""
    return _answers(target, "GetTypeName2")


def _is_component(target):
    """True if ``target`` is an ``IComponent2``, as a bool.

    ``Select4`` on a component takes a third argument, and passing two to it
    is a type mismatch rather than a missing member.
    """
    return _answers(target, "GetPathName") and _answers(
        target, "ReferencedConfiguration"
    )


def _answers(target, member):
    """True if ``target`` has ``member``, as a bool.

    Late binding has no interface to ask, so the question is answered by
    asking for the member and seeing whether it is there.
    """
    try:
        com.call(target, member)
    except Exception:
        return False
    return True


def _select_named(document, name, kind, mark, append):
    """``SelectByID2`` by name, trying `STRING_KINDS` when no kind is given."""
    kinds = (kind,) if kind else STRING_KINDS
    for candidate in kinds:
        if document.select(name, candidate, mark=mark, append=append):
            return True
    raise SwCallError(
        f"nothing called {name!r} could be selected in {document.name!r}"
        + (
            f" as a {kind}."
            if kind
            else "; tried " + ", ".join(STRING_KINDS) + ". Name a kind with "
            "(name, kind) if it is something else."
        ),
        member="SelectByID2",
    )
