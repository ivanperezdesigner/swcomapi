"""Look up any part of the SOLIDWORKS API without leaving Python.

19,874 members across 729 interfaces, with the description Dassault wrote for
each one, which parameters are outputs, and a link to the official page::

    >>> import swcomapi as swc
    >>> print(swc.describe("IModelDocExtension.GetMassProperties2"))
    IModelDocExtension.GetMassProperties2(Accuracy, UseSelected) -> Any
      Gets mass properties of selected assembly components
      parameters:
        Accuracy     int    in
        Status       int    out     <- supplied for you, comes back in the result
        UseSelected  bool   in
      call it with: swcomapi.com.call_out(obj, 'GetMassProperties2', ...)
      docs: https://help.solidworks.com/...

And when you do not know the name::

    >>> swc.find("GetMassProperties")[:2]
    ['IBody.GetMassProperties', 'IBody2.GetMassProperties']

which searches the descriptions too, so a plain English phrase works.

Why this exists
---------------

The official pages are the only place the full prose lives, and they are not
reachable from a script: ``help.solidworks.com`` answers ``403`` to anything
that is not a browser, and builds its pages with JavaScript even then. The type
libraries carry a one-line description for 86% of members, and that turns out
to be enough to find what you want - after which the link takes you to the
rest.

What it costs
-------------

Nothing until you ask. The index is a gzipped JSON file next to the generated
modules, 494 KB on disk, and it is read and cached the first time one of these
functions is called. Importing ``swcomapi`` does not touch it.
"""

import gzip
import json
import os

from . import doclinks

# The index, once read. Annotated because mypy cannot infer anything from an
# empty dict.
_INDEX: dict = {}

# The VARTYPEs the signature table uses, spelled for a human.
_VT_NAMES = {
    2: "short",
    3: "int",
    5: "float",
    8: "str",
    9: "object",
    11: "bool",
    12: "any",
}


def index():
    """The whole API index, as a dict. Read once and cached.

    Its shape::

        {
          "year": 2026,
          "libraries": [{"name": ..., "file": ...}],
          "interfaces": {name: {"doc", "library", "members": [...]}},
          "enums": {name: {"library", "members": [[name, value], ...]}},
        }

    Each member is ``{"name", "kind", "doc", "returns", "returns_com",
    "params": [{"name", "py", "com", "dir"}], "com_only"?}``.
    """
    if not _INDEX:
        path = os.path.join(os.path.dirname(__file__), "generated", "api_index.json.gz")
        with gzip.open(path, "rt", encoding="utf-8") as handle:
            _INDEX.update(json.load(handle))
    return _INDEX


# ------------------------------------------------------------------ searching


def find(text, limit=40):
    """Members whose name or description matches ``text``.

    Returns a list of ``"Interface.Member"`` strings, sorted, with exact and
    prefix name matches first. Searches the descriptions too, so a plain
    English phrase works.

    limit
        how many to return; None for all of them

    Examples::

        >>> "IModelDocExtension.GetMassProperties2" in find("GetMassProperties")
        True
        >>> find("nonexistent gibberish phrase")
        []
    """
    lowered = str(text).lower()
    exact, prefix, name_match, doc_match = [], [], [], []

    for interface_name, interface in index()["interfaces"].items():
        for member in interface["members"]:
            full = f"{interface_name}.{member['name']}"
            name = member["name"].lower()
            if name == lowered:
                exact.append(full)
            elif name.startswith(lowered):
                prefix.append(full)
            elif lowered in name:
                name_match.append(full)
            elif lowered in member["doc"].lower():
                doc_match.append(full)

    ordered = sorted(exact) + sorted(prefix) + sorted(name_match) + sorted(doc_match)
    return ordered if limit is None else ordered[:limit]


def find_interface(text, limit=40):
    """Interfaces whose name or description matches ``text``.

    Returns a list of names, sorted, name matches first.

    Example::

        >>> "IModelDocExtension" in find_interface("ModelDoc")
        True
    """
    lowered = str(text).lower()
    names, docs = [], []
    for name, interface in index()["interfaces"].items():
        if lowered in name.lower():
            names.append(name)
        elif lowered in interface["doc"].lower():
            docs.append(name)
    ordered = sorted(names) + sorted(docs)
    return ordered if limit is None else ordered[:limit]


def members_of(interface, kind=None):
    """Every member of ``interface``, as a list of names, sorted.

    kind
        ``"method"``, ``"get"`` or ``"put"`` to narrow it down

    Raises KeyError if there is no such interface.

    Example::

        >>> "OpenDoc6" in members_of("ISldWorks")
        True
    """
    entry = index()["interfaces"][interface]
    return sorted(
        member["name"]
        for member in entry["members"]
        if kind is None or member["kind"] == kind
    )


def interfaces():
    """Every interface name, sorted. As a list of str."""
    return sorted(index()["interfaces"])


# ------------------------------------------------------------------ describing


def describe(what, member=None):
    """A readable description of an interface or one of its members.

    what
        ``"IModelDoc2"``, or ``"IModelDoc2.SaveAs3"``, or an interface name
        with ``member`` given separately
    member
        the member name, when not already part of ``what``

    Returns a multi-line str. Never raises for an unknown name: it says what
    it could not find and suggests a search, because the whole point is to be
    usable from a prompt.

    Examples::

        >>> print(describe("swDocumentTypes_e"))     # doctest: +ELLIPSIS
        swDocumentTypes_e  (enumeration, 8 constants, from SwConst)
          swDocNONE                 = 0
        ...
        >>> print(describe("INoSuchThing"))          # doctest: +ELLIPSIS
        'INoSuchThing' is not in the API index...
    """
    if member is None and "." in str(what):
        what, member = str(what).split(".", 1)
    what = str(what)

    data = index()
    if what in data["enums"]:
        return _describe_enum(what, data["enums"][what])
    if what not in data["interfaces"]:
        return _not_found(what)
    if member is None:
        return _describe_interface(what, data["interfaces"][what])
    return _describe_member(what, data["interfaces"][what], member)


def _not_found(name):
    hits = find(name, limit=5) or find_interface(name, limit=5)
    lines = [f"{name!r} is not in the API index."]
    if hits:
        lines.append("Did you mean one of these?")
        lines.extend(f"  {hit}" for hit in hits)
    else:
        lines.append(f"  swcomapi.find({name.lower()!r}) to search by name or description")
        lines.append(f"  {doclinks.search_link(name)}")
    return "\n".join(lines)


def _describe_enum(name, entry):
    lines = [
        f"{name}  (enumeration, {len(entry['members'])} constants, "
        f"from {entry['library']})"
    ]
    width = max((len(member) for member, _ in entry["members"]), default=0)
    for member, value in entry["members"]:
        lines.append(f"  {member:<{width}} = {value}")
    url = doclinks.link(name, library=entry["library"])
    if url:
        lines.append(f"  docs: {url}")
    return "\n".join(lines)


def _describe_interface(name, entry):
    methods = [m for m in entry["members"] if m["kind"] == "method" and not m.get("com_only")]
    properties = sorted({m["name"] for m in entry["members"] if m["kind"] in ("get", "put")})
    twins = [m for m in entry["members"] if m.get("com_only")]

    lines = [f"{name}  (interface, from {entry['library']})"]
    if entry["doc"]:
        lines.append(f"  {entry['doc']}")
    lines.append(
        f"  {len(methods)} methods, {len(properties)} properties"
        + (f", {len(twins)} C++-only twins hidden" if twins else "")
    )
    if properties:
        lines.append("  properties: " + ", ".join(properties[:12]))
        if len(properties) > 12:
            lines.append(f"    ...and {len(properties) - 12} more")
    if methods:
        names = sorted(m["name"] for m in methods)
        lines.append("  methods: " + ", ".join(names[:12]))
        if len(names) > 12:
            lines.append(f"    ...and {len(names) - 12} more")
    lines.append(f"  swcomapi.apidoc.members_of({name!r}) for the full list")
    url = doclinks.link(name, library=entry["library"])
    if url:
        lines.append(f"  docs: {url}")
    return "\n".join(lines)


def _describe_member(interface, entry, member):
    matches = [m for m in entry["members"] if m["name"] == member]
    if not matches:
        hits = [m["name"] for m in entry["members"] if member.lower() in m["name"].lower()]
        lines = [f"{interface} has no member {member!r}."]
        if hits:
            lines.append("Did you mean: " + ", ".join(sorted(hits)[:8]))
        else:
            lines.append(f"  swcomapi.apidoc.members_of({interface!r}) to list them all")
        return "\n".join(lines)

    lines = []
    for found in matches:
        lines.extend(_describe_one(interface, entry, found))
    return "\n".join(lines)


def _describe_one(interface, entry, found):
    supplied = [p for p in found["params"] if p["dir"] != "out"]
    signature = ", ".join(p["name"] for p in supplied)
    label = {"get": " (property, read)", "put": " (property, write)"}.get(found["kind"], "")

    lines = [
        f"{interface}.{found['name']}({signature}) -> {found['returns']}{label}"
    ]
    if found["doc"]:
        lines.append(f"  {found['doc']}")
    if found.get("com_only"):
        lines.append(
            f"  NOT callable from Python: this is the C++ flavour, taking raw "
            f"pointers. Use {found['name'][1:]} instead."
        )

    if found["params"]:
        lines.append("  parameters:")
        width = max(len(p["name"]) for p in found["params"])
        for param in found["params"]:
            note = ""
            if param["dir"] == "out":
                note = "   <- supplied for you, comes back in the result"
            elif param["dir"] == "inout":
                note = "   <- optional, comes back in the result"
            lines.append(
                f"    {param['name']:<{width}}  {param['py']:<6} {param['dir']:<5}{note}"
            )

    if any(p["dir"] != "in" for p in found["params"]):
        lines.append(f"  call it with: swcomapi.com.call_out(obj, {found['name']!r}, ...)")

    url = doclinks.link(interface, found["name"], library=entry["library"])
    if url:
        lines.append(f"  docs: {url}")
    return lines


# -------------------------------------------------------------------- summary


def summary():
    """What the index contains, as a str. One line per count.

    Example::

        >>> print(summary())                         # doctest: +ELLIPSIS
        SOLIDWORKS ... API index
        ...
    """
    data = index()
    members = [m for i in data["interfaces"].values() for m in i["members"]]
    lines = [
        f"SOLIDWORKS {data['year']} API index",
        f"  {len(data['libraries'])} type libraries",
        f"  {len(data['interfaces'])} interfaces, {len(members)} members",
        f"  {sum(1 for m in members if m['doc'])} members with a description",
        f"  {sum(1 for m in members if m.get('com_only'))} C++-only twins",
        f"  {len(data['enums'])} enumerations, "
        f"{sum(len(e['members']) for e in data['enums'].values())} constants",
    ]
    return "\n".join(lines)
