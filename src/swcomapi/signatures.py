"""Which parameters a SOLIDWORKS method writes its results into.

This is the table that lets `swcomapi.com.call_out` work without you knowing
anything about VARIANTs. Ask it about a method and it tells you where the
outputs are::

    >>> outputs_of("GetBuildNumbers2")
    ((0, 'BaseVersion', 8, 'out'), (1, 'CurrentVersion', 8, 'out'), (2, 'HotFixes', 8, 'out'))
    >>> outputs_of("RevisionNumber")
    ()

Each entry is ``(parameter index, parameter name, VARTYPE, direction)``.

The direction is the part that is easy to get wrong. A pure ``[out]``
parameter is not something the caller passes at all - it has to be *inserted*
into the argument list at its own position, which can be in the middle::

    IModelDocExtension.GetMassProperties2(Accuracy, Status, UseSelected)
                                             in      out       in

An ``[in,out]`` one does take a value from the caller, and carries it in as its
starting point::

    ISldWorks.OpenDoc6(FileName, Type, Options, Configuration, Errors, Warnings)
                          in      in     in          in         inout   inout

Keyed by name, not by interface
-------------------------------

There is no way to ask a live SOLIDWORKS object what interface it implements:
``IDispatch.GetTypeInfo`` raises ``TYPE_E_ELEMENTNOTFOUND`` on every one of
them. So the table is keyed by member name, which was measured to be safe
enough: of the 982 member names that take an ``[out]`` parameter, 109 appear on
more than one interface and only 26 disagree about the shape.

Those 26 are told apart by how many arguments the caller passes, which
`shape_for_args` works out exactly rather than approximately. ``ISldWorks``
and ``IModelDocExtension`` both have a ``GetMassProperties2``, and they are
different methods::

    >>> shape_for_args("GetMassProperties2", 0)[1]
    ((0, 'Status', 3, 'inout'),)
    >>> shape_for_args("GetMassProperties2", 2)[1]
    ((1, 'Status', 3, 'out'),)
"""

from .errors import SwAmbiguousMemberError
from .generated._out_data import OUT_PARAMS


def shape_for_args(member, argument_count, interface=None, kind="method"):
    """The shape of ``member`` when called with ``argument_count`` arguments.

    member
        the method name, as a str
    argument_count
        how many arguments the caller is supplying, counting the ``[in,out]``
        ones and not the pure ``[out]`` ones
    interface
        the interface name, when even the argument count does not settle it
    kind
        ``"method"``, ``"get"`` or ``"put"``

    Returns ``(arity, outputs, supplies_inout)``. ``arity`` is the method's
    real parameter count, ``outputs`` is the tuple described in this module's
    docstring, and ``supplies_inout`` says whether the caller passed values
    for the ``[in,out]`` parameters or left them to be filled in.

    Returns ``(argument_count, (), False)`` for a member with no ``[out]``
    parameters, including one the table has never heard of.

    An ``[in,out]`` parameter may be left out. SOLIDWORKS uses that direction
    for error codes whose incoming value it ignores, so making you pass two
    zeroes to ``OpenDoc6`` would be pointless ceremony. Both spellings work:

        >>> shape_for_args("OpenDoc6", 4)[0]
        6
        >>> shape_for_args("OpenDoc6", 4)[2]
        False
        >>> shape_for_args("OpenDoc6", 6)[2]
        True

    A pure ``[out]`` parameter can never be passed, because it has no
    incoming value at all::

        >>> shape_for_args("GetBuildNumbers2", 0)[0]
        3
        >>> shape_for_args("RevisionNumber", 0)
        (0, (), False)

    Raises `SwAmbiguousMemberError` when two shapes fit equally well, or when
    no shape takes that many arguments.
    """
    shapes = OUT_PARAMS.get((member, kind))
    if not shapes:
        return argument_count, (), False

    if interface is not None:
        narrowed = tuple(shape for shape in shapes if interface in shape[2])
        if narrowed:
            shapes = narrowed

    fitting = [
        (shape, argument_count == _with_inout(shape))
        for shape in shapes
        if argument_count in (_without_inout(shape), _with_inout(shape))
    ]
    if len(fitting) == 1:
        (arity, outputs, _), supplies_inout = fitting[0]
        return arity, outputs, supplies_inout

    if not fitting:
        raise SwAmbiguousMemberError(
            f"{member!r} does not take {argument_count} argument(s). "
            + _shape_summary(shapes)
            + " Its [out] parameters are supplied for you, so leave them out.",
            member=member,
        )

    raise SwAmbiguousMemberError(
        f"{member!r} with {argument_count} argument(s) matches "
        f"{len(fitting)} different methods. "
        + _shape_summary(shape for shape, _ in fitting)
        + " Pass interface= to say which one you mean.",
        member=member,
    )


def outputs_of(member, arity=None, interface=None, kind="method"):
    """Where ``member`` writes its results. Returns a tuple of quadruples.

    Introspection, for reading the table rather than calling through it. Use
    `shape_for_args` when you are about to make a call.

    Returns ``()`` for a member with no ``[out]`` parameters, including one
    that does not exist: as far as calling it goes those are the same thing.

    Raises `SwAmbiguousMemberError` when the name matches several shapes and
    neither ``arity`` nor ``interface`` picks one.

    Examples::

        >>> outputs_of("GetMassProperties2", arity=1)
        ((0, 'Status', 3, 'inout'),)
        >>> outputs_of("GetMassProperties2", interface="IModelDocExtension")
        ((1, 'Status', 3, 'out'),)
    """
    shapes = OUT_PARAMS.get((member, kind))
    if not shapes:
        return ()

    if interface is not None:
        narrowed = tuple(shape for shape in shapes if interface in shape[2])
        if narrowed:
            shapes = narrowed
    if arity is not None:
        narrowed = tuple(shape for shape in shapes if shape[0] == arity)
        if narrowed:
            shapes = narrowed

    if len(shapes) == 1:
        return shapes[0][1]

    raise SwAmbiguousMemberError(
        f"{member!r} takes [out] parameters in {len(shapes)} different shapes. "
        + _shape_summary(shapes)
        + " Pass arity= or interface= to say which one you mean.",
        member=member,
    )


def _without_inout(shape):
    """The fewest arguments a caller can pass: every output left to us."""
    arity, outputs, _ = shape
    return arity - len(outputs)


def _with_inout(shape):
    """The most a caller can pass: the ``[in,out]`` ones supplied as well.

    Pure ``[out]`` parameters are never among them; they have no incoming
    value to supply.
    """
    arity, outputs, _ = shape
    return arity - sum(1 for _, _, _, direction in outputs if direction == "out")


def _shape_summary(shapes):
    """A readable list of the options, for an error message."""
    parts = []
    for shape in shapes:
        low, high = _without_inout(shape), _with_inout(shape)
        counts = f"{low}" if low == high else f"{low} or {high}"
        parts.append(f"{counts} argument(s) on {', '.join(shape[2][:2])}")
    return "; ".join(parts)


def has_outputs(member, kind="method"):
    """True if ``member`` writes into any of its parameters.

    Examples::

        >>> has_outputs("OpenDoc6")
        True
        >>> has_outputs("RevisionNumber")
        False
    """
    return bool(OUT_PARAMS.get((member, kind)))


def shapes_of(member, kind="method"):
    """Every known shape for ``member``, as a tuple of ``(arity, outs, ifaces)``.

    Use this when a lookup reports an ambiguity and you want to see why.

    Example::

        >>> for arity, outs, interfaces in shapes_of("GetMassProperties2"):
        ...     print(arity, [name for _, name, _, _ in outs], interfaces[0])
        1 ['Status'] IModelDoc
        3 ['Status'] IModelDocExtension
    """
    return OUT_PARAMS.get((member, kind), ())


def members_with_outputs():
    """Every ``(name, kind)`` that takes an ``[out]`` parameter, sorted.

    982 of them, which is why this table is generated rather than written.
    """
    return sorted(OUT_PARAMS)


def ambiguous_members():
    """The ``(name, kind)`` pairs with more than one shape, sorted.

    26 of them. Worth knowing they exist; you will almost certainly never meet
    one, because the argument count settles them.
    """
    return sorted(key for key, shapes in OUT_PARAMS.items() if len(shapes) > 1)
