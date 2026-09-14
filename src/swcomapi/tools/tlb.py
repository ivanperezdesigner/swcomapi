"""Read a COM type library into plain Python data.

This is the module the whole generated layer rests on. It turns a ``.tlb`` file
into nested dicts and lists - no COM objects escape it - so everything
downstream is ordinary data that can be diffed, tested and written to a file.

Why bother, when the online help exists? Because the type library is the only
machine-readable, exact, version-correct account of the API. And because it
carries more than signatures:

* a one-line description for nearly every interface and most methods, written
  by the vendor. The official help pages are behind an Akamai rule that
  refuses every non-browser client, so this is the documentation.
* which parameters are ``[out]`` and ``[in,out]``, and what VARTYPE each one
  needs. Nothing else tells you this, and 3,700-odd methods need it.

Run it directly for a census of what is installed::

    python -m swcomapi.tools.tlb --survey

What gets filtered out
----------------------

Every COM interface inherits ``QueryInterface``, ``AddRef``, ``Release`` and
the four ``IDispatch`` members. They appear in the type library on all 516
interfaces and are pure plumbing, so they are dropped: they would add some
3,600 entries that no Python caller ever wants. They are recognised by their
reserved member ids rather than by name, which is the spelling-proof test.

SOLIDWORKS also ships two flavours of many methods: ``GetMassProperties``
returns a VARIANT that Python can read, while ``IGetMassProperties`` takes raw
pointers and exists for C++. The second kind is marked ``com_only`` so the
generated stubs can steer callers away from it.
"""

import pythoncom

# ------------------------------------------------------------------ TYPEKIND

TKIND_ENUM = 0
TKIND_RECORD = 1
TKIND_MODULE = 2
TKIND_INTERFACE = 3
TKIND_DISPATCH = 4
TKIND_COCLASS = 5
TKIND_ALIAS = 6
TKIND_UNION = 7

TKIND_NAMES = {
    TKIND_ENUM: "enum",
    TKIND_RECORD: "record",
    TKIND_MODULE: "module",
    TKIND_INTERFACE: "interface",
    TKIND_DISPATCH: "dispatch",
    TKIND_COCLASS: "coclass",
    TKIND_ALIAS: "alias",
    TKIND_UNION: "union",
}

# ------------------------------------------------------------------- INVKIND

INVOKE_FUNC = 1
INVOKE_PROPERTYGET = 2
INVOKE_PROPERTYPUT = 4
INVOKE_PROPERTYPUTREF = 8

INVKIND_NAMES = {
    INVOKE_FUNC: "method",
    INVOKE_PROPERTYGET: "get",
    INVOKE_PROPERTYPUT: "put",
    INVOKE_PROPERTYPUTREF: "putref",
}

# ---------------------------------------------------------------- PARAMFLAGS

PARAMFLAG_FIN = 1
PARAMFLAG_FOUT = 2
PARAMFLAG_FLCID = 4
PARAMFLAG_FRETVAL = 8
PARAMFLAG_FOPT = 16
PARAMFLAG_FHASDEFAULT = 32

# ---------------------------------------------------------------- FUNCFLAGS

FUNCFLAG_FRESTRICTED = 1
FUNCFLAG_FHIDDEN = 64

# ------------------------------------------------------------------ VARTYPES

VT_EMPTY = 0
VT_NULL = 1
VT_I2 = 2
VT_I4 = 3
VT_R4 = 4
VT_R8 = 5
VT_CY = 6
VT_DATE = 7
VT_BSTR = 8
VT_DISPATCH = 9
VT_ERROR = 10
VT_BOOL = 11
VT_VARIANT = 12
VT_UNKNOWN = 13
VT_DECIMAL = 14
VT_I1 = 16
VT_UI1 = 17
VT_UI2 = 18
VT_UI4 = 19
VT_I8 = 20
VT_UI8 = 21
VT_INT = 22
VT_UINT = 23
VT_VOID = 24
VT_HRESULT = 25
VT_PTR = 26
VT_SAFEARRAY = 27
VT_CARRAY = 28
VT_USERDEFINED = 29

# The COM spelling, for the documentation.
VT_COM_NAMES = {
    VT_EMPTY: "void",
    VT_NULL: "null",
    VT_I2: "short",
    VT_I4: "long",
    VT_R4: "float",
    VT_R8: "double",
    VT_CY: "CURRENCY",
    VT_DATE: "DATE",
    VT_BSTR: "BSTR",
    VT_DISPATCH: "IDispatch*",
    VT_ERROR: "SCODE",
    VT_BOOL: "VARIANT_BOOL",
    VT_VARIANT: "VARIANT",
    VT_UNKNOWN: "IUnknown*",
    VT_DECIMAL: "DECIMAL",
    VT_I1: "char",
    VT_UI1: "unsigned char",
    VT_UI2: "unsigned short",
    VT_UI4: "unsigned long",
    VT_I8: "__int64",
    VT_UI8: "unsigned __int64",
    VT_INT: "int",
    VT_UINT: "unsigned int",
    VT_VOID: "void",
    VT_HRESULT: "HRESULT",
}

# What Python actually sees, for the stubs. VT_VARIANT is deliberately `Any`:
# SOLIDWORKS uses it for everything from a SafeArray of doubles to a single
# object, so any narrower promise would be a lie.
VT_PY_NAMES = {
    VT_EMPTY: "None",
    VT_NULL: "None",
    VT_I2: "int",
    VT_I4: "int",
    VT_R4: "float",
    VT_R8: "float",
    VT_CY: "float",
    VT_DATE: "float",
    VT_BSTR: "str",
    VT_DISPATCH: "Any",
    VT_ERROR: "int",
    VT_BOOL: "bool",
    VT_VARIANT: "Any",
    VT_UNKNOWN: "Any",
    VT_DECIMAL: "float",
    VT_I1: "int",
    VT_UI1: "int",
    VT_UI2: "int",
    VT_UI4: "int",
    VT_I8: "int",
    VT_UI8: "int",
    VT_INT: "int",
    VT_UINT: "int",
    VT_VOID: "None",
    VT_HRESULT: "int",
}

# The VARTYPE to hand `swcomapi.com.out()` for an [out] parameter of each
# pointed-to type. VT_INT and VT_UINT have no VARIANT representation, so they
# travel as VT_I4; an [out] object arrives as VT_DISPATCH.
OUT_VT_SUBSTITUTIONS = {
    VT_INT: VT_I4,
    VT_UINT: VT_I4,
    VT_UI4: VT_I4,
    VT_UI2: VT_I2,
    VT_I1: VT_I2,
    VT_UI1: VT_I2,
    VT_VOID: VT_VARIANT,
    VT_UNKNOWN: VT_DISPATCH,
    VT_USERDEFINED: VT_DISPATCH,
}

# IUnknown's and IDispatch's own members live in this reserved member id range.
# Recognising them by id rather than by name means a renamed or re-cased entry
# cannot slip through.
RESERVED_MEMID_LOW = 0x60000000
RESERVED_MEMID_HIGH = 0x6001FFFF


# ------------------------------------------------------------------- loading


def load(path):
    """Load a type library. Returns the ``ITypeLib``.

    Raises ``pythoncom.com_error`` if the file is not a readable type library.
    Some libraries that ship with SOLIDWORKS - ``cosworks.tlb`` for one - fail
    here because they depend on a DLL that is not on the path; that is a fact
    about the install, not something to work around.
    """
    return pythoncom.LoadTypeLib(path)


def read_library(path):
    """Read a whole type library into plain data.

    Returns a dict::

        {
          "path": "C:\\\\...\\\\sldworks.tlb",
          "name": "SldWorks",                      # the library's own name
          "doc": "SldWorks 2026 Type Library",
          "guid": "{83A33D31-27C5-11CE-BFD4-00400513BB57}",
          "major": 3, "minor": 34,
          "enums": [ ...see read_enum... ],
          "interfaces": [ ...see read_interface... ],
          "skipped": {"coclass": 507, ...},        # kinds not read
        }

    Enums and interfaces come out sorted by name, so regenerating against the
    same library twice produces byte-identical output.
    """
    tlb = load(path)
    name, doc, _, _ = tlb.GetDocumentation(-1)
    attr = tlb.GetLibAttr()

    enums = []
    interfaces = []
    skipped = {}

    for index in range(tlb.GetTypeInfoCount()):
        kind = tlb.GetTypeInfoType(index)
        if kind == TKIND_ENUM:
            enums.append(read_enum(tlb, index))
        elif kind in (TKIND_DISPATCH, TKIND_INTERFACE):
            interfaces.append(read_interface(tlb, index))
        else:
            label = TKIND_NAMES.get(kind, str(kind))
            skipped[label] = skipped.get(label, 0) + 1

    return {
        "path": path,
        "name": name,
        "doc": doc or "",
        "guid": str(attr[0]),
        "major": attr[3],
        "minor": attr[4],
        "enums": sorted(enums, key=lambda e: e["name"]),
        "interfaces": sorted(interfaces, key=lambda i: i["name"]),
        "skipped": skipped,
    }


# --------------------------------------------------------------------- enums


def read_enum(tlb, index):
    """Read one enumeration.

    Returns a dict::

        {
          "name": "swDocumentTypes_e",
          "doc": "",
          "guid": "{55A9AAAE-97D1-4621-A5A9-21A67CDCE87A}",
          "members": [("swDocNONE", 0), ("swDocPART", 1), ...],
        }

    Members keep the order the library declares them in, which is the order the
    documentation lists and usually the order the values run in. They are not
    sorted: a reader comparing against the docs wants to see them as declared.

    The libraries carry no per-member descriptions - all 12,503 of them are
    blank - so there is nothing to read beyond name and value.
    """
    info = tlb.GetTypeInfo(index)
    attr = info.GetTypeAttr()
    name, doc, _, _ = tlb.GetDocumentation(index)

    members = []
    for position in range(attr.cVars):
        var = info.GetVarDesc(position)
        members.append((info.GetNames(var.memid)[0], var.value))

    return {
        "name": name,
        "doc": doc or "",
        "guid": str(attr[0]),
        "members": members,
    }


# ---------------------------------------------------------------- interfaces


def read_interface(tlb, index):
    """Read one interface, with its members.

    Returns a dict::

        {
          "name": "ISldWorks",
          "doc": "Interface for SOLIDWORKS",
          "guid": "{...}",
          "kind": "dispatch",
          "members": [ ...see read_member... ],
        }

    Members are sorted by name, then by kind, so a property's getter and setter
    sit together and the output is stable across runs.
    """
    info = tlb.GetTypeInfo(index)
    attr = info.GetTypeAttr()
    name, doc, _, _ = tlb.GetDocumentation(index)

    members = []
    for position in range(attr.cFuncs):
        func = info.GetFuncDesc(position)
        if is_reserved(func.memid):
            continue
        members.append(read_member(info, func))

    _mark_com_only(members)

    return {
        "name": name,
        "doc": doc or "",
        "guid": str(attr[0]),
        "kind": TKIND_NAMES.get(attr.typekind, str(attr.typekind)),
        "members": sorted(members, key=lambda m: (m["name"], m["kind"])),
    }


def is_reserved(memid):
    """True for ``IUnknown``'s and ``IDispatch``'s own members.

    ``QueryInterface``, ``AddRef``, ``Release``, ``GetTypeInfoCount``,
    ``GetTypeInfo``, ``GetIDsOfNames`` and ``Invoke`` appear on every one of
    the 516 interfaces. Dropping them removes some 3,600 entries of pure
    plumbing.
    """
    return RESERVED_MEMID_LOW <= memid <= RESERVED_MEMID_HIGH


def read_member(info, func):
    """Read one method or property.

    Returns a dict::

        {
          "name": "OpenDoc6",
          "kind": "method",             # method | get | put | putref
          "memid": 167,
          "doc": "Opens an existing document",
          "returns": {...a type dict...},
          "params": [ {...a type dict, plus name/direction/out_vt...} ],
          "has_out": True,
          "hidden": False,
          "com_only": False,            # filled in by _mark_com_only
        }
    """
    names = info.GetNames(func.memid)
    name = names[0]
    param_names = list(names[1:])
    _, doc, _, _ = info.GetDocumentation(func.memid)

    params = []
    for position, arg in enumerate(func.args):
        tdesc, flags = arg[0], arg[1]
        param = type_info(tdesc, info)
        param["name"] = (
            param_names[position] if position < len(param_names) else f"arg{position}"
        )
        param["direction"] = direction_of(flags)
        param["optional"] = bool(flags & PARAMFLAG_FOPT)
        param["flags"] = flags
        if param["direction"] in ("out", "inout"):
            param["out_vt"] = out_vartype(tdesc)
        params.append(param)

    kind = INVKIND_NAMES.get(func.invkind, str(func.invkind))
    return {
        "name": name,
        "kind": kind,
        "memid": func.memid,
        "doc": (doc or "").strip(),
        "returns": type_info(func.rettype[0], info),
        "params": params,
        "has_out": any(p["direction"] in ("out", "inout") for p in params),
        "hidden": bool(func.wFuncFlags & (FUNCFLAG_FHIDDEN | FUNCFLAG_FRESTRICTED)),
        "com_only": False,
    }


def direction_of(flags):
    """``"in"``, ``"out"`` or ``"inout"`` from a parameter's flags.

    Examples::

        >>> direction_of(PARAMFLAG_FIN)
        'in'
        >>> direction_of(PARAMFLAG_FOUT)
        'out'
        >>> direction_of(PARAMFLAG_FIN | PARAMFLAG_FOUT)
        'inout'
        >>> direction_of(0)
        'in'
    """
    if flags & PARAMFLAG_FOUT:
        return "inout" if flags & PARAMFLAG_FIN else "out"
    return "in"


def _mark_com_only(members):
    """Flag the C++-only twin of each method that has one.

    SOLIDWORKS publishes many methods twice: ``GetMassProperties`` hands back a
    VARIANT that Python can read, and ``IGetMassProperties`` takes raw pointers
    for C++. Both are in the library, only one is usable from Python.

    The test is exact rather than a guess about the leading I: a member counts
    as C++-only when stripping its leading ``I`` yields the name of another
    member of the same kind on the same interface.
    """
    by_kind = {}
    for member in members:
        by_kind.setdefault(member["kind"], set()).add(member["name"])
    for member in members:
        name = member["name"]
        if len(name) > 1 and name[0] == "I" and name[1].isupper():
            if name[1:] in by_kind.get(member["kind"], ()):
                member["com_only"] = True


# --------------------------------------------------------------------- types


def type_info(tdesc, info):
    """Describe a TYPEDESC as plain data.

    Returns a dict::

        {
          "vt": 26,                 # the outermost VARTYPE
          "com": "IModelDoc2*",     # how the documentation spells it
          "py": "IModelDoc2",       # what Python actually gets
          "interface": "IModelDoc2" # set only when it resolves to one
        }

    A TYPEDESC is either a bare VARTYPE, or a tuple whose head says what it
    wraps: ``(26, target)`` is a pointer, ``(29, href)`` a reference to another
    type in the library, resolved here into its name.

    Arrays never appear: SOLIDWORKS passes them inside a ``VARIANT``, which is
    why the Python type for those is ``Any`` and why
    ``swcomapi.com.to_list`` exists.
    """
    # A bare VARTYPE.
    if isinstance(tdesc, int):
        return {
            "vt": tdesc,
            "com": VT_COM_NAMES.get(tdesc, f"VT({tdesc})"),
            "py": VT_PY_NAMES.get(tdesc, "Any"),
        }

    head = tdesc[0]

    if head == VT_USERDEFINED:
        name = _resolve_reference(tdesc[1], info)
        return {
            "vt": VT_USERDEFINED,
            "com": name,
            "py": name if name.startswith("I") else "Any",
            "interface": name,
        }

    if head == VT_PTR:
        inner = type_info(tdesc[1], info)
        result = {
            "vt": VT_PTR,
            "com": inner["com"] + "*",
            # A pointer is how COM spells "by reference". What arrives in
            # Python is whatever it points at.
            "py": inner["py"],
        }
        if "interface" in inner:
            result["interface"] = inner["interface"]
        return result

    if head in (VT_SAFEARRAY, VT_CARRAY):
        inner = type_info(tdesc[1], info)
        return {
            "vt": head,
            "com": f"SAFEARRAY({inner['com']})",
            "py": f"list[{inner['py']}]",
        }

    return {"vt": head, "com": f"VT({head})", "py": "Any"}


def _resolve_reference(href, info):
    """The name behind a VT_USERDEFINED reference handle.

    Returns the interface or enum name, or ``"Any"`` when the reference points
    outside this library and cannot be followed.
    """
    try:
        return info.GetRefTypeInfo(href).GetDocumentation(-1)[0]
    except pythoncom.com_error:
        return "Any"


def out_vartype(tdesc):
    """The VARTYPE to hand ``swcomapi.com.out()`` for this ``[out]`` parameter.

    An ``[out]`` parameter is declared as a pointer, so what matters is the
    type it points at. A few of those have no VARIANT form and travel as a
    wider one: ``int`` and ``unsigned long`` go as ``VT_I4``, an object comes
    back as ``VT_DISPATCH``.

    Examples, straight from ``ISldWorks``::

        >>> out_vartype((VT_PTR, VT_I4))            # OpenDoc6's Errors
        3
        >>> out_vartype((VT_PTR, VT_BSTR))          # GetBuildNumbers2's args
        8
        >>> out_vartype((VT_PTR, VT_R8))            # a coordinate
        5
        >>> out_vartype((VT_PTR, (VT_USERDEFINED, 0)))
        9
        >>> out_vartype((VT_PTR, VT_UINT))
        3
        >>> out_vartype(VT_I4)                      # not a pointer at all
        3
    """
    target = tdesc[1] if isinstance(tdesc, tuple) and tdesc[0] == VT_PTR else tdesc
    if isinstance(target, tuple):
        # A pointer to a pointer, or to a named type. Either way an object
        # comes back, except for a nested array which arrives as a VARIANT.
        if target[0] in (VT_USERDEFINED, VT_PTR):
            return VT_DISPATCH
        return VT_VARIANT
    return OUT_VT_SUBSTITUTIONS.get(target, target)


# -------------------------------------------------------------------- survey


def survey(libraries):
    """Count what a set of libraries contains. Returns a list of dicts.

    Each entry is either a count row or, when the library will not load, a row
    with an ``error`` key. A library that fails is reported, never hidden: it
    means the install lacks a DLL that library needs.
    """
    rows = []
    for path in libraries:
        try:
            lib = read_library(path)
        except pythoncom.com_error as exc:
            rows.append({"path": path, "error": str(exc)})
            continue
        members = [m for i in lib["interfaces"] for m in i["members"]]
        rows.append(
            {
                "path": path,
                "name": lib["name"],
                "enums": len(lib["enums"]),
                "enum_members": sum(len(e["members"]) for e in lib["enums"]),
                "interfaces": len(lib["interfaces"]),
                "members": len(members),
                "documented": sum(1 for m in members if m["doc"]),
                "with_out": sum(1 for m in members if m["has_out"]),
                "com_only": sum(1 for m in members if m["com_only"]),
                "properties": sum(1 for m in members if m["kind"] in ("get", "put")),
            }
        )
    return rows
