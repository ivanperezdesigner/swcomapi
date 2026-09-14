"""Unit conversion, because the SOLIDWORKS API is metres and radians. Always.

The document's own unit system is irrelevant to the API: a part modelled in
inches still reports a 25 mm extrusion as 0.025. This is the single most common
source of silently wrong automation, so swcomapi never guesses.

The rule in this package:

* `swcomapi.com` and anything raw passes values straight through, in metres
  and radians.
* `swcomapi.api` takes and returns millimetres and degrees, and says so in
  every docstring.

Examples::

    >>> mm(25)
    0.025
    >>> to_mm(0.025)
    25.0
    >>> deg(90)
    1.5707963267948966
    >>> round(to_deg(1.5707963267948966), 10)
    90.0
    >>> inch(1)
    0.0254
    >>> to_mm_all([0.025, 0.04, 0.0])
    [25.0, 40.0, 0.0]
"""

import math

MM_PER_M = 1000.0
INCH_PER_M = 39.37007874015748
M_PER_INCH = 0.0254

# ---------------------------------------------------------------- to the API


def mm(value):
    """Millimetres to metres. Use when handing a length to a raw API call."""
    return value / MM_PER_M


def cm(value):
    """Centimetres to metres."""
    return value / 100.0


def inch(value):
    """Inches to metres."""
    return value * M_PER_INCH


def deg(value):
    """Degrees to radians. Use when handing an angle to a raw API call."""
    return math.radians(value)


# -------------------------------------------------------------- from the API


def to_mm(value):
    """Metres to millimetres."""
    return value * MM_PER_M


def to_cm(value):
    """Metres to centimetres."""
    return value * 100.0


def to_inch(value):
    """Metres to inches."""
    return value / M_PER_INCH


def to_deg(value):
    """Radians to degrees."""
    return math.degrees(value)


# ------------------------------------------------------------------ areas &
# volumes, for mass properties. The API reports m2, m3 and kilograms.


def to_mm2(value):
    """Square metres to square millimetres."""
    return value * MM_PER_M**2


def to_mm3(value):
    """Cubic metres to cubic millimetres."""
    return value * MM_PER_M**3


def to_cm3(value):
    """Cubic metres to cubic centimetres. What SOLIDWORKS shows by default."""
    return value * 100.0**3


def to_g(value):
    """Kilograms to grams."""
    return value * 1000.0


# ----------------------------------------------------------------- sequences
# GetBox, GetMassProperties and the point-returning methods hand back flat
# arrays of metres. Converting them one by one gets noisy.


def to_mm_all(values):
    """Every metre in an iterable to millimetres, as a list of float."""
    return [v * MM_PER_M for v in values]


def to_deg_all(values):
    """Every radian in an iterable to degrees, as a list of float."""
    return [math.degrees(v) for v in values]


def mm_all(values):
    """Every millimetre in an iterable to metres, as a list of float."""
    return [v / MM_PER_M for v in values]
