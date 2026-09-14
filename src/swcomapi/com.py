"""The raw COM layer: dispatch, ``[out]`` parameters and SafeArrays.

Nothing here knows anything about SOLIDWORKS. It exists because three details
of the COM bridge get in the way of every single script, and they are worth
solving once:

1. **``[out]`` parameters.** A COM method can return data by writing into its
   arguments. ``ISldWorks.OpenDoc6`` is the canonical example: the document
   comes back as the return value, but the errors and the warnings come back
   through the last two parameters. With late binding you have to hand pywin32
   a ``VARIANT`` flagged ``VT_BYREF`` for each one, and know its exact type.

   ``call_out()`` does all of that for you, from the generated table in
   ``swcomapi.signatures``::

       >>> doc, out = call_out(app, "OpenDoc6", path, 1, 0, "")  # doctest: +SKIP
       >>> out                                                   # doctest: +SKIP
       {'Errors': 0, 'Warnings': 0}

   ``byref()`` is there for the rare case the table cannot help with.

2. **SafeArrays.** SOLIDWORKS returns arrays as flat tuples: ``GetBox`` gives
   six numbers that are really two corners, ``GetCoordinateSystem`` nine that
   are really three vectors. ``to_list()`` and ``to_tuples()`` unpack them, and
   ``to_list()`` also turns the ``None`` that means "empty" into ``[]``.

3. **The object you do not have.** SOLIDWORKS declares plenty of parameters as
   ``IDispatch*`` and then documents them as unused. ``SaveAs3`` has two.
   VBA passes ``Nothing``; Python's ``None`` reaches SOLIDWORKS as
   ``VT_EMPTY`` and the call fails with "Type mismatch" naming no parameter.
   ``call()`` converts a ``None`` in one of those positions into the null
   ``VT_DISPATCH`` that works, from the same generated table, so this::

       call_out(ext, "SaveAs3", path, 0, options, None, None)

   is all you write. ``nothing()`` is there for a call made by hand.

4. **Unreadable errors.** A failing call raises ``pywintypes.com_error``, which
   prints as a nest of HRESULTs. ``call()`` translates it into the classes in
   ``swcomapi.errors`` and keeps the original in ``__cause__``.

Everything in metres and radians, exactly as the API wants it. Conversion is
``swcomapi.units``' job.

Examples::

    >>> to_list(None)
    []
    >>> to_list((1.0, 2.0, 3.0))
    [1.0, 2.0, 3.0]
    >>> to_tuples((0.0, 0.0, 0.0, 0.025, 0.04, 0.01), 3)
    [(0.0, 0.0, 0.0), (0.025, 0.04, 0.01)]
"""

import types

from .errors import SwCallError, SwMemberNotFoundError, SwUnavailableError

# What "this still needs calling" means. Everything else - a str, an int, a
# tuple, a COM object - is a value the bridge has already produced.
_INVOCABLE = (
    types.MethodType,
    types.FunctionType,
    types.BuiltinFunctionType,
    types.BuiltinMethodType,
    types.MethodDescriptorType,
)

try:
    import pythoncom
    import win32com.client
    from win32com.client import VARIANT
except ImportError:  # pragma: no cover - only reachable off Windows
    # The ignores are for mypy only: it sees the names as a module and a type
    # from the successful branch. `_require_pywin32` turns the None into a
    # readable error at the point of use.
    pythoncom = None  # type: ignore[assignment]
    win32com = None  # type: ignore[assignment]
    VARIANT = None  # type: ignore[assignment,misc]


# The VARTYPEs SOLIDWORKS actually uses, re-exported so callers never have to
# import pythoncom themselves.
if pythoncom is not None:  # pragma: no branch
    VT_I2 = pythoncom.VT_I2
    VT_I4 = pythoncom.VT_I4
    VT_R4 = pythoncom.VT_R4
    VT_R8 = pythoncom.VT_R8
    VT_BSTR = pythoncom.VT_BSTR
    VT_BOOL = pythoncom.VT_BOOL
    VT_VARIANT = pythoncom.VT_VARIANT
    VT_DISPATCH = pythoncom.VT_DISPATCH
    VT_ARRAY = pythoncom.VT_ARRAY
    VT_BYREF = pythoncom.VT_BYREF
else:  # pragma: no cover
    VT_I2 = VT_I4 = VT_R4 = VT_R8 = VT_BSTR = 0
    VT_BOOL = VT_VARIANT = VT_DISPATCH = VT_ARRAY = VT_BYREF = 0

# HRESULTs worth naming. COM hands them over as signed 32-bit ints.
DISP_E_UNKNOWNNAME = -2147352570  # 0x80020006, "Unknown name."
DISP_E_MEMBERNOTFOUND = -2147352573  # 0x80020003, "Member not found."
RPC_E_CALL_REJECTED = -2147418111  # 0x80010001, "Call was rejected by callee."
RPC_E_SERVERCALL_RETRYLATER = -2147417851  # 0x8001010A, the server is busy.
RPC_E_DISCONNECTED = -2147417848  # 0x8001010D, the object is gone.

# The HRESULTs that mean "ask again in a moment" rather than "this failed".
BUSY_HRESULTS = (RPC_E_CALL_REJECTED, RPC_E_SERVERCALL_RETRYLATER)


def _require_pywin32():
    if pythoncom is None:
        raise SwUnavailableError(
            "pywin32 is not importable, so COM is unreachable. swcomapi can "
            "only talk to SOLIDWORKS on Windows, with `pip install pywin32`."
        )


# ------------------------------------------------------------------- dispatch


def dispatch(progid, new_instance=False):
    """Get a COM object for ``progid``.

    progid
        the registered name, as a str, e.g. ``"SldWorks.Application"``
    new_instance
        True forces a brand new process (``DispatchEx``); False lets COM hand
        back the running one if the server is a singleton, which SOLIDWORKS is

    Deliberately ``Dispatch``, never ``gencache.EnsureDispatch``: the generated
    cache is pinned to one type library version, writes into the user's
    profile, and breaks the moment SOLIDWORKS is upgraded. swcomapi gets its
    enums and signatures from ``swcomapi.generated`` instead, which is exactly
    why it does not care which version is installed.
    """
    _require_pywin32()
    try:
        if new_instance:
            return win32com.client.DispatchEx(progid)
        return win32com.client.Dispatch(progid)
    except pythoncom.com_error as exc:
        raise _translate(exc, progid) from exc


def active_object(progid):
    """Get the already-running COM object for ``progid``, or raise.

    Unlike ``dispatch``, this never starts anything: it looks the object up in
    the Running Object Table. Raises ``pywintypes.com_error`` when nothing is
    registered there, which is how ``swcomapi.connect`` tells "SOLIDWORKS is
    open" from "SOLIDWORKS is not open".
    """
    _require_pywin32()
    return win32com.client.GetActiveObject(progid)


# ------------------------------------------------------------ [out] arguments


def byref(vartype=None, initial=None):
    """Build an argument a COM method can write its result into.

    You rarely need this: `call_out` builds them for you. Reach for it when a
    method is missing from the generated table, or when you want to see the
    raw machinery.

    vartype
        one of the ``VT_*`` constants re-exported by this module; defaults to
        ``VT_VARIANT``, which SOLIDWORKS accepts for most ``[out]`` parameters
    initial
        the starting value; None becomes ``""`` for ``VT_BSTR`` and ``0``
        otherwise

    Returns a ``win32com.client.VARIANT`` flagged ``VT_BYREF``. After the call
    the result sits in its ``.value``.

    Example, the two ``[out]`` parameters of ``ISldWorks.OpenDoc6`` done the
    hard way::

        errors = byref(VT_I4)
        warnings = byref(VT_I4)
        doc = call(app, "OpenDoc6", path, 1, 0, "", errors, warnings)
        print(errors.value, warnings.value)   # 0 0
    """
    _require_pywin32()
    if vartype is None:
        vartype = VT_VARIANT
    if initial is None:
        initial = "" if vartype == VT_BSTR else 0
    return VARIANT(VT_BYREF | vartype, initial)


def is_byref(value):
    """True if ``value`` was built by `byref`."""
    return VARIANT is not None and isinstance(value, VARIANT)


# ------------------------------------------------------------------ the call


def call(obj, member, *args, interface=None, kind="method"):
    """Call a method, or read a property, and translate any COM failure.

    obj
        the COM object
    member
        the member name, as a str, spelled exactly as the API spells it
    args
        the arguments in declaration order; use `byref` for ``[out]`` ones, or
        let `call_out` build them
    interface
        the interface name, for the few member names whose shape is ambiguous
    kind
        ``"method"``, ``"get"`` or ``"put"``

    A ``None`` in a position the generated table says wants a COM object
    becomes `nothing`; everywhere else it is passed through untouched.

    Returns whatever the member returns.

    Raises `SwMemberNotFoundError` when the member does not exist in the
    installed SOLIDWORKS, and `SwCallError` for anything else.

    The thing this gets right
    ------------------------

    Late binding is inconsistent about zero-argument members, in a way that
    bites every script written against SOLIDWORKS. Reading the attribute
    sometimes hands back the answer and sometimes hands back a method still
    waiting to be called, and the difference is not something you can predict
    from the documentation. All four of these are real, from one part
    document::

        doc.EditRebuild3   ->  True           a bool: already invoked
        doc.GetTitle       ->  'Part1.SLDPRT' a str: already invoked
        doc.ForceRebuild3  ->  <bound method> not invoked yet
        doc.Extension      ->  <COMObject>    already invoked

    Deciding with ``callable()`` looks right and is wrong: a ``CDispatch`` is
    callable, so ``doc.Extension()`` gets attempted and fails with "Member not
    found". The test that works is whether the attribute is a Python function
    or method object; a COM object is not, and neither is a string.
    """
    _require_pywin32()
    try:
        attr = getattr(obj, member)
    except AttributeError as exc:
        raise SwMemberNotFoundError(
            f"{_name_of(obj)} has no member {member!r}", member=member
        ) from exc
    except pythoncom.com_error as exc:
        raise _translate(exc, member) from exc

    if not needs_calling(attr):
        if args:
            raise SwCallError(
                f"{member!r} was already evaluated by the COM bridge, which "
                f"means it takes no arguments, but {len(args)} were given",
                member=member,
            )
        return attr

    if any(value is None for value in args):
        args = _objects(args, member, interface, kind)

    try:
        return attr(*args)
    except pythoncom.com_error as exc:
        raise _translate(exc, member) from exc


def nothing():
    """A null COM object, for an ``[in]`` parameter you have nothing to put in.

    This is VBA's ``Nothing``. It comes up constantly, because SOLIDWORKS
    declares plenty of parameters as ``IDispatch*`` and then documents them as
    "not used"::

        ext.SaveAs3(path, 0, options, nothing(), nothing(), errors, warnings)

    Python's ``None`` is not the same thing. pywin32 marshals it as
    ``VT_EMPTY``, and SOLIDWORKS rejects that with "Type mismatch" without
    saying which parameter it meant.

    `call_out` inserts this for you wherever the generated table says a
    parameter wants an object, so a plain ``None`` works there::

        _, out = call_out(ext, "SaveAs3", path, 0, options, None, None)

    Use it directly only when calling the COM object by hand.
    """
    _require_pywin32()
    return VARIANT(VT_DISPATCH, None)


def needs_calling(attr):
    """True if ``attr`` is a method still waiting to be invoked.

    See `call` for why this cannot be ``callable()``.

    Examples::

        >>> needs_calling(True)
        False
        >>> needs_calling("Part1.SLDPRT")
        False
        >>> needs_calling((1.0, 2.0))
        False
        >>> needs_calling(len)
        True
    """
    return isinstance(attr, _INVOCABLE)


def call_out(obj, member, *args, interface=None, kind="method"):
    """Call a method and collect what it wrote into its parameters.

    Pass only the real arguments. The ``[out]`` ones are looked up in
    ``swcomapi.signatures``, built, slotted into the right positions and read
    back afterwards.

    obj
        the COM object
    member
        the method name, as a str
    args
        the ``[in]`` arguments, in order, with the ``[out]`` ones left out
    interface
        the interface name, for the 26 method names whose shape is ambiguous
        and that the argument count does not settle
    kind
        ``"method"``, ``"get"`` or ``"put"``

    Returns ``(return_value, outputs)``, where ``outputs`` is a dict keyed by
    the parameter names the API uses.

    An ``[in,out]`` parameter is both: pass its input value in ``args`` as
    normal and it comes back in ``outputs`` too.

    Examples, both of them real traps::

        # GetBuildNumbers2 is three [out] strings and returns nothing.
        _, out = call_out(app, "GetBuildNumbers2")
        out["BaseVersion"]      # 'sw2026_SP03'

        # OpenDoc6's last two parameters are [in,out] error codes.
        doc, out = call_out(app, "OpenDoc6", path, 1, 0, "")
        out["Errors"], out["Warnings"]      # 0, 0
    """
    from . import signatures

    arity, outputs, supplies_inout = signatures.shape_for_args(
        member, len(args), interface=interface, kind=kind
    )
    if not outputs:
        return call(obj, member, *args, interface=interface, kind=kind), {}

    # Walk the real parameter list and fill each position from the right
    # place: a pure [out] gets a fresh holder inserted, an [in,out] gets one
    # seeded with the caller's value, and everything else takes the next
    # argument as given. Inserting rather than overwriting is what makes a
    # mid-list [out] work, and SOLIDWORKS has plenty - see
    # IModelDocExtension.GetMassProperties2(Accuracy, Status, UseSelected).
    by_index = {index: (name, vartype, direction) for index, name, vartype, direction in outputs}
    supplied = iter(args)
    full = []
    holders = {}
    for position in range(arity):
        if position not in by_index:
            full.append(next(supplied))
            continue
        name, vartype, direction = by_index[position]
        holder = byref(vartype)
        if direction == "inout" and supplies_inout:
            holder.value = next(supplied)
        holders[name] = holder
        full.append(holder)

    result = call(obj, member, *full, interface=interface, kind=kind)
    return result, {name: holder.value for name, holder in holders.items()}


def _objects(args, member, interface, kind):
    """``args`` with a ``None`` in a COM-object position replaced by `nothing`.

    The table is consulted only when there is a ``None`` to translate, so a
    normal call pays nothing for this.
    """
    from . import signatures

    wants_object = signatures.dispatch_ins_for_args(
        member, len(args), interface=interface, kind=kind
    )
    if not wants_object:
        return args
    return tuple(
        nothing() if value is None and index in wants_object else value
        for index, value in enumerate(args)
    )


def _name_of(obj):
    """A readable label for ``obj``, for error messages."""
    name = type(obj).__name__
    return "the COM object" if name in ("CDispatch", "PyIDispatch") else name


def _translate(exc, member):
    """Turn a ``com_error`` into the right class from ``swcomapi.errors``."""
    hresult, detail = _unpack(exc)
    if _signed(hresult) in (DISP_E_UNKNOWNNAME, DISP_E_MEMBERNOTFOUND):
        return SwMemberNotFoundError(
            f"{member!r} does not exist in this SOLIDWORKS version",
            member=member,
            hresult=hresult,
            detail=detail,
        )
    suffix = f": {detail}" if detail else ""
    if hresult is None:
        message = f"{member!r} failed{suffix}"
    else:
        message = f"{member!r} failed with HRESULT {hresult:#010x}{suffix}"
    return SwCallError(message, member=member, hresult=hresult, detail=detail)


def _unpack(exc):
    """Pull the HRESULT and the human description out of a ``com_error``.

    A com_error's args are ``(hresult, source_description, excepinfo,
    arg_index)``, and the message worth reading sits in the second slot, or in
    the third slot of ``excepinfo`` when the server filled one in.

    Returns ``(hresult_or_None, detail_str)`` with the HRESULT normalised to
    unsigned, so that ``{:#010x}`` prints the form the documentation uses.
    """
    hresult = None
    detail = ""
    args = getattr(exc, "args", ())

    if args:
        try:
            hresult = int(args[0]) & 0xFFFFFFFF
        except (TypeError, ValueError):
            hresult = None
    if len(args) > 1 and isinstance(args[1], str):
        detail = args[1]

    excepinfo = args[2] if len(args) > 2 else None
    if isinstance(excepinfo, tuple) and len(excepinfo) > 2:
        described = excepinfo[2]
        if isinstance(described, str) and described.strip():
            detail = described.strip()

    return hresult, detail


def _signed(hresult):
    """An unsigned HRESULT back as the signed int the constants use."""
    if hresult is None:
        return None
    return hresult - 0x100000000 if hresult >= 0x80000000 else hresult


def is_busy(exc):
    """True if ``exc`` is a com_error that means "retry in a moment".

    SOLIDWORKS answers with these while it is still loading, and while a modal
    dialog is open on screen.
    """
    hresult, _ = _unpack(exc)
    return _signed(hresult) in BUSY_HRESULTS


# ----------------------------------------------------------------- SafeArrays


def to_list(value):
    """A SafeArray coming out of the API, as a list.

    SOLIDWORKS uses an empty array and a null VARIANT interchangeably for "no
    results", and pywin32 surfaces the second as ``None``. Both become ``[]``.
    A lone scalar becomes a one-item list, because several methods return one
    object directly when there is only one.

    Examples::

        >>> to_list(None)
        []
        >>> to_list((1.0, 2.0))
        [1.0, 2.0]
        >>> to_list(3.0)
        [3.0]
    """
    if value is None:
        return []
    if isinstance(value, (tuple, list)):
        return list(value)
    return [value]


def to_tuples(value, size):
    """A flat SafeArray regrouped into tuples of ``size``.

    For the methods that return points or vectors as one long array: ``GetBox``
    gives two corners as six numbers, ``GetCoordinateSystem`` three vectors as
    nine.

    Raises ValueError when the length is not a multiple of ``size``, which is
    the honest answer when the array is not the shape you assumed.

    Examples::

        >>> to_tuples((0.0, 0.0, 0.0, 0.025, 0.04, 0.01), 3)
        [(0.0, 0.0, 0.0), (0.025, 0.04, 0.01)]
        >>> to_tuples(None, 3)
        []
    """
    flat = to_list(value)
    if len(flat) % size:
        raise ValueError(f"cannot regroup {len(flat)} values into tuples of {size}")
    return [tuple(flat[i : i + size]) for i in range(0, len(flat), size)]


def from_list(values, vartype=None):
    """Build a SafeArray to hand to a method that takes an array ``[in]``.

    values
        an iterable of plain Python values
    vartype
        the element type; defaults to ``VT_R8``, which is what the coordinate
        lists want. Use ``VT_DISPATCH`` for a list of COM objects.

    Example, the point list ``ISketchManager.CreateSpline`` wants::

        pts = from_list([0.0, 0.0, 0.0, 0.025, 0.0, 0.0])
    """
    _require_pywin32()
    if vartype is None:
        vartype = VT_R8
    return VARIANT(VT_ARRAY | vartype, list(values))
