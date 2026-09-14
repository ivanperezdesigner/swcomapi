"""Links into the official SOLIDWORKS API documentation.

Every URL is built from the name, never fetched, so this costs nothing and
works offline::

    >>> link("IModelDoc2")
    'https://help.solidworks.com/2026/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html'
    >>> link("IModelDocExtension", "GetMassProperties2")
    'https://help.solidworks.com/2026/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMassProperties2.html'
    >>> link("swDocumentTypes_e")
    'https://help.solidworks.com/2026/english/api/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDocumentTypes_e.html'

The release defaults to whatever the generated layer was built from, and any
other year works::

    >>> link("IModelDoc2", year=2027).startswith("https://help.solidworks.com/2027/")
    True

Why build rather than fetch
---------------------------

``help.solidworks.com`` returns ``403 Access Denied`` to every client that is
not a browser, and the pages are assembled by JavaScript even then. So the
content cannot be mirrored into this package, and the documentation that ships
with it comes from the type libraries instead. The link is how you get to the
rest: the parameter tables, the remarks and the VBA examples.

The three patterns above were each opened in a real browser and checked
against the generated data before being written down here.
"""

from .generated import SOLIDWORKS_YEAR

BASE = "https://help.solidworks.com"

# Type library name -> (.NET namespace, help path segment).
#
# Verified by opening a page from each: the sldworks, swconst and swcommands
# patterns were all confirmed against the live site.
#
# swmotionstudy, swdimxpert and swpublished sit under "SOLIDWORKS API Help"
# beside sldworks in the site's own table of contents, and share its path.
LIBRARY_DOCS = {
    "SldWorks": ("SolidWorks.Interop.sldworks", "sldworksapi"),
    "SwConst": ("SolidWorks.Interop.swconst", "swconst"),
    "SwCommands": ("SolidWorks.Interop.swcommands", "swcommands"),
    "SwMotionStudy": ("SolidWorks.Interop.swmotionstudy", "sldworksapi"),
    "SwDimXpert": ("SolidWorks.Interop.swdimxpert", "sldworksapi"),
    "SWPublished": ("SolidWorks.Interop.swpublished", "sldworksapi"),
}

# The add-ins each have their own help set, published at paths this package has
# not verified. Rather than emit a link that might 404, `link` returns None for
# them and `search_link` gives you a way in that definitely works.
UNMAPPED_LIBRARIES = {
    "CosmosWorksLib": "SOLIDWORKS Simulation API Help",
    "SldCostingAPI": "SOLIDWORKS Costing API Help",
    "SWRoutingLib": "SOLIDWORKS Routing API Help",
    "sustainabilityLib": "SOLIDWORKS Sustainability API Help",
}

# Where a name lives, when the caller has not said. Built on first use.
# Annotated because mypy cannot infer anything from an empty dict.
_HOMES: dict[str, str] = {}


def link(name, member=None, year=None, library=None):
    """The documentation URL for an interface, an enumeration or a member.

    name
        an interface name like ``"IModelDoc2"``, or an enumeration name like
        ``"swDocumentTypes_e"``
    member
        a method or property on that interface, as a str
    year
        the release to link to; defaults to the one this package was generated
        from
    library
        the type library, when you already know it. Looked up otherwise.

    Returns the URL as a str, or None when the name belongs to an add-in whose
    help path is not known - see `UNMAPPED_LIBRARIES` - or is not in the
    generated data at all.

    Examples::

        >>> link("ISldWorks", "OpenDoc6")
        'https://...sldworks.ISldWorks~OpenDoc6.html'
        >>> link("swNotARealName_e") is None
        True
    """
    library = library or library_of(name)
    mapping = LIBRARY_DOCS.get(library)
    if mapping is None:
        return None

    namespace, path = mapping
    year = year or SOLIDWORKS_YEAR
    page = f"{namespace}~{namespace}.{name}"
    if member:
        page += f"~{member}"
    return f"{BASE}/{year}/english/api/{path}/{page}.html"


def search_link(text, year=None):
    """A search URL for the API help, as a str.

    The way in for anything `link` cannot build, and a useful fallback in
    general: the site's search covers every help set, including the add-ins.

    Example::

        >>> search_link("GetMassProperties")        # doctest: +ELLIPSIS
        'https://help.solidworks.com/search.aspx?q=GetMassProperties&ver=...'
    """
    from urllib.parse import quote_plus

    year = year or SOLIDWORKS_YEAR
    return f"{BASE}/search.aspx?q={quote_plus(str(text))}&ver={year}&lang=english"


def library_of(name):
    """Which type library declares ``name``, as a str, or None.

    Looks in the generated enumeration data first, since that is already
    loaded, and falls back to the interface index.

    Examples::

        >>> library_of("swDocumentTypes_e")
        'SwConst'
        >>> library_of("IModelDoc2")
        'SldWorks'
        >>> library_of("nonsense") is None
        True
    """
    _build_homes()
    return _HOMES.get(name)


def _build_homes():
    """Index every interface and enumeration name to its library, once."""
    if _HOMES:
        return

    from .generated._enum_data import ENUM_LIBRARY

    _HOMES.update(ENUM_LIBRARY)

    # The interface index is the gzipped one, so it is only touched when an
    # interface name is actually asked about - which this does lazily too,
    # after the enums have already answered most questions.
    from . import apidoc

    for name, interface in apidoc.index()["interfaces"].items():
        _HOMES.setdefault(name, interface["library"])


def is_documented(name):
    """True if `link` can build a URL for ``name``.

    Examples::

        >>> is_documented("IModelDoc2")
        True
        >>> is_documented("nonsense")
        False
    """
    return link(name) is not None
