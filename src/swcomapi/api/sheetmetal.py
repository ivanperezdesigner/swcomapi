"""Sheet metal: thickness, bend radius, K-factor, and the flat pattern.

    part.is_sheet_metal                 # True
    part.sheet_metal.thickness          # 2.0   mm
    part.sheet_metal.bend_radius        # 2.0   mm
    part.sheet_metal.k_factor           # 0.5
    part.sheet_metal.bend_allowance     # 'k-factor'
    part.export_flat_pattern("blank.dxf")

The numbers are on the sheet metal feature, not on the part: a part with two
sheet metal bodies has two of them, each with its own thickness. `of` gives
the first, which is what a single-body part has and what a script means.

Reading them costs a lock
-------------------------

``IFeature.GetDefinition`` on a sheet metal feature hands back an
``ISheetMetalFeatureData``, and SOLIDWORKS holds the feature while you have
it. Releasing it is ``ReleaseSelectionAccess`` and forgetting to leaves the
feature locked for the rest of the session - the tree still shows it, editing
it does nothing, and nothing says why.

`SheetMetal` reads what it needs and releases immediately, so there is nothing
to remember. `SheetMetal.definition` hands you the raw object if you want the
rest of it; that one is yours to release.
"""

from .. import com
from ..units import to_mm

# swBendAllowanceTypes_e, as readable names. Numbered from 1, not from 0:
# swBendAllowanceBendTable is 1 and there is no zero.
BEND_ALLOWANCE = {
    1: "bend table",
    2: "k-factor",
    3: "bend allowance",
    4: "bend deduction",
    5: "bend calculation table",
    6: "gauge table",
}

# The feature types that carry sheet metal parameters, as GetTypeName2
# reports them. "SheetMetal" is the folder a converted solid gets;
# "SMBaseFlange" is what a base flange makes.
SHEET_METAL_TYPES = ("SheetMetal", "SMBaseFlange")


class SheetMetal:
    """The sheet metal parameters of one feature.

    Attributes:
        feature  the `swcomapi.api.features.Feature` they come from
    """

    def __init__(self, feature):
        self.feature = feature

    @property
    def thickness(self):
        """The material thickness in mm, as a float."""
        return to_mm(self._read("Thickness"))

    @property
    def bend_radius(self):
        """The default inside bend radius in mm, as a float."""
        return to_mm(self._read("BendRadius"))

    @property
    def k_factor(self):
        """The K-factor, as a float.

        Dimensionless: the position of the neutral axis through the
        thickness, so 0.5 is the middle. Only meaningful when
        `bend_allowance` is ``'k-factor'``.
        """
        return float(self._read("KFactor"))

    @property
    def bend_allowance(self):
        """How the bend allowance is worked out, as a str.

        One of the values in `BEND_ALLOWANCE`: ``'k-factor'``,
        ``'bend table'``, ``'gauge table'``, ``'bend deduction'``...
        """
        code = int(self._read("BendAllowanceType"))
        return BEND_ALLOWANCE.get(code, f"unknown ({code})")

    @property
    def relief_ratio(self):
        """The auto relief ratio, as a float."""
        return float(self._read("ReliefRatio"))

    @property
    def uses_gauge_table(self):
        """True if a gauge table drives the thickness, as a bool."""
        return bool(self._read("GetUseGaugeTable"))

    @property
    def definition(self):
        """The raw ``ISheetMetalFeatureData``.

        SOLIDWORKS holds the feature while you have this. Call
        ``ReleaseSelectionAccess`` on it when you are done, or the feature
        stays locked for the rest of the session.
        """
        return com.call(self.feature.com, "GetDefinition")

    def _read(self, member):
        """Read one value and let go of the feature again.

        The release is the point: a definition that is not released leaves
        the feature locked, and nothing reports that it happened.
        """
        definition = com.call(self.feature.com, "GetDefinition")
        if definition is None:
            return 0
        try:
            return com.call(definition, member)
        finally:
            com.call(definition, "ReleaseSelectionAccess")

    def as_dict(self):
        """Every parameter at once, as a dict.

        One pass over the feature rather than one per value, which matters
        when reading a folder of parts.

        Example, on a sheet metal part - `swcomapi.api.document.Part.sheet_metal`
        is None on one that is not:

            >>> metal = part.sheet_metal                    # doctest: +SKIP
            >>> sorted(metal.as_dict()) if metal else "not sheet metal"  # doctest: +SKIP
            'not sheet metal'
        """
        definition = com.call(self.feature.com, "GetDefinition")
        if definition is None:
            return {}
        try:
            code = int(com.call(definition, "BendAllowanceType"))
            return {
                "thickness": to_mm(com.call(definition, "Thickness")),
                "bend_radius": to_mm(com.call(definition, "BendRadius")),
                "k_factor": float(com.call(definition, "KFactor")),
                "bend_allowance": BEND_ALLOWANCE.get(code, f"unknown ({code})"),
                "relief_ratio": float(com.call(definition, "ReliefRatio")),
            }
        finally:
            com.call(definition, "ReleaseSelectionAccess")

    def __repr__(self):
        return (
            f"<SheetMetal {self.feature.name!r}: {self.thickness:g} mm thick, "
            f"r{self.bend_radius:g}>"
        )


def features_of(part):
    """The sheet metal features of a part, as a list of `SheetMetal`.

    One per sheet metal body. Empty for a part that is not sheet metal.
    """
    found = []
    for kind in SHEET_METAL_TYPES:
        found.extend(SheetMetal(feature) for feature in part.features.of_type(kind))
    return found


def of(part):
    """The part's sheet metal parameters, as a `SheetMetal`, or None.

    The first sheet metal feature, which is the only one in a part with a
    single body. `features_of` gives them all.

    Example, on a part with no sheet metal in it:

        >>> of(part) is None                            # doctest: +SKIP
        True
    """
    found = features_of(part)
    return found[0] if found else None


def is_sheet_metal(part):
    """True if the part has a sheet metal feature, as a bool."""
    return bool(features_of(part))
