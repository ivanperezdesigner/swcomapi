"""The hand-written layer: the calls you actually make.

    import swcomapi as swc

    app = swc.connect()
    with app.open("bracket.SLDPRT") as part:
        part.configuration = "BRK-040"
        part.dimensions["Length@Boss-Extrude1"] = 55        # millimetres
        part.features["HolePattern"].suppress()
        part.rebuild()
        print(part.mass_properties["mass"])                 # grams
        part.export("BRK-040.step")

What each module covers:

`swcomapi.api.app`
    `SolidWorks`: connecting, opening, creating, listing, commands.
`swcomapi.api.document`
    `Document` and its three specialisations. `Part` adds mass properties and
    sheet metal, `Assembly` adds components, `Drawing` adds sheets and views.
`swcomapi.api.configurations`
    a sequence of configuration names, and switching between them.
`swcomapi.api.features`
    the feature tree, and suppression per configuration.
`swcomapi.api.dimensions`
    dimensions by full name, in millimetres and degrees.
`swcomapi.api.properties`
    custom properties as a dict, per file and per configuration.
`swcomapi.api.export`
    saving in any format, with the error bitmasks decoded.

Two rules hold everywhere here:

* **Millimetres and degrees**, in and out. The raw API is metres and radians.
* **``.com`` reaches the raw object** on every one of these classes, so
  nothing in the API is out of reach because a wrapper does not exist yet.
"""

from .app import SolidWorks
from .configurations import Configurations
from .dimensions import Dimensions
from .document import Assembly, Document, Drawing, Part, wrap
from .features import Feature, Features
from .properties import Properties

__all__ = [
    "SolidWorks",
    "Document",
    "Part",
    "Assembly",
    "Drawing",
    "wrap",
    "Configurations",
    "Features",
    "Feature",
    "Dimensions",
    "Properties",
]
