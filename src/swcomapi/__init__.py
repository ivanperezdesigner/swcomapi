"""Drive SOLIDWORKS from Python over its COM API.

Two layers, one package:

* ``swcomapi.generated`` -- the whole API surface, produced by reading the type
  libraries that ship with SOLIDWORKS. Every enumeration, every interface,
  every method signature, with a link to the official page for each one.
* ``swcomapi.api`` -- a hand-written, documented layer over the calls you make
  every day: connect, open, configurations, features, dimensions, drawings,
  export.

Every wrapper object exposes the raw COM object as ``.com``, so nothing in the
API is ever out of reach.

Windows only. Connecting needs SOLIDWORKS installed; the enums and the
documentation links are plain data and import anywhere.
"""

__version__ = "0.0.1"
