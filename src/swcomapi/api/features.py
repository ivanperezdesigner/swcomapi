"""The feature tree, walkable and suppressible.

    for feature in part.features:
        print(feature.name, feature.type)

    part.features["HolePattern"].suppress()
    part.features["HolePattern"].unsuppress()
    part.features["Fillet1"].suppressed          # False

Suppressing per configuration is the useful case, and the one the raw API
makes awkward::

    part.features["HolePattern"].suppress(in_configurations=["BRK-020"])
    part.features["HolePattern"].suppress(everywhere=True)

What the tree actually contains
-------------------------------

``FirstFeature`` and ``GetNextFeature`` walk the top level only, and the top
level includes things that are not features in the everyday sense: the origin,
the three default planes, the annotations folder, the comments folder. They are
all here because hiding them would mean guessing, and a guess that drops a real
feature is worse than a list with ``Front Plane`` in it. `solid_features`
filters to what a person means.
"""

from .. import com
from ..errors import SwCallError

# Tree entries that are furniture rather than modelling. Type names as
# GetTypeName2 reports them.
FURNITURE = frozenset(
    {
        "OriginProfileFeature",
        "RefPlane",
        "CoordSys",
        "DetailCabinet",
        "CommentsFolder",
        "FavoriteFolder",
        "HistoryFolder",
        "SelectionSetFolder",
        "SensorFolder",
        "DocsFolder",
        "MaterialFolder",
        "SolidBodyFolder",
        "SurfaceBodyFolder",
        "EnvFolder",
        "LiveSectionFolder",
        "GridSystemFolder",
        "ProfileFeature",
    }
)


class Feature:
    """One entry in the feature tree.

    Attributes:
        com  the raw ``IFeature``
    """

    def __init__(self, feature, document=None):
        self.com = feature
        self._document = document

    # ------------------------------------------------------------- identity

    @property
    def name(self):
        """The name as it appears in the tree, as a str."""
        return com.call(self.com, "Name")

    @name.setter
    def name(self, value):
        self.com.Name = str(value)

    @property
    def type(self):
        """The feature type, as a str, e.g. ``'Extrusion'``, ``'Fillet'``.

        This is ``GetTypeName2``, the name the API uses. It is not what the
        tree shows next to the icon, and not localised, which makes it the one
        worth testing against.
        """
        return com.call(self.com, "GetTypeName2")

    @property
    def is_furniture(self):
        """True for a tree entry that is not a modelling feature.

        The origin, the default planes, the annotations and comments folders.
        """
        return self.type in FURNITURE

    # ---------------------------------------------------------- suppression

    @property
    def suppressed(self):
        """Whether the feature is suppressed in the active configuration.

        As a bool. Setting it is the same as calling `suppress` or
        `unsuppress` with no arguments.
        """
        from ..const import swThisConfiguration

        result = com.call(self.com, "IsSuppressed2", swThisConfiguration, None)
        states = com.to_list(result)
        return bool(states[0]) if states else False

    @suppressed.setter
    def suppressed(self, value):
        if value:
            self.suppress()
        else:
            self.unsuppress()

    def suppress(self, in_configurations=None, everywhere=False):
        """Suppress the feature.

        in_configurations
            a list of configuration names; the active one if omitted
        everywhere
            True suppresses it in every configuration, which is not the same
            as listing them all: a configuration added later inherits it

        Returns True. Raises `SwCallError` if SOLIDWORKS refuses, which it
        does when suppressing would break a feature that depends on this one.

        Example::

            part.features["HolePattern"].suppress(in_configurations=["BRK-020"])
        """
        from ..const import swSuppressFeature

        return self._set_suppression(swSuppressFeature, in_configurations, everywhere)

    def unsuppress(self, in_configurations=None, everywhere=False, with_dependents=False):
        """Unsuppress the feature.

        with_dependents
            True also unsuppresses the features that depend on this one, which
            is usually what you want: unsuppressing a sketch alone leaves the
            extrusion built on it still suppressed.

        Other arguments as `suppress`.
        """
        from ..const import swUnSuppressDependent, swUnSuppressFeature

        action = swUnSuppressDependent if with_dependents else swUnSuppressFeature
        return self._set_suppression(action, in_configurations, everywhere)

    def _set_suppression(self, action, in_configurations, everywhere):
        from ..const import (
            swAllConfiguration,
            swSpecifyConfiguration,
            swThisConfiguration,
        )

        if everywhere and in_configurations:
            raise SwCallError(
                "pass either everywhere=True or in_configurations=[...], not both",
                member="SetSuppression2",
            )
        if everywhere:
            scope, names = swAllConfiguration, None
        elif in_configurations:
            scope = swSpecifyConfiguration
            names = [str(name) for name in in_configurations]
        else:
            scope, names = swThisConfiguration, None

        ok = com.call(self.com, "SetSuppression2", action, scope, names)
        if not ok:
            raise SwCallError(
                f"SOLIDWORKS refused to change the suppression of "
                f"{self.name!r}. A feature that others depend on cannot be "
                f"suppressed on its own; try unsuppress(with_dependents=True) "
                f"for the reverse case.",
                member="SetSuppression2",
            )
        return True

    # ---------------------------------------------------------------- tree

    @property
    def children(self):
        """The features nested under this one, as a list of `Feature`.

        Sketches under an extrusion, that sort of thing.
        """
        found = []
        child = com.call(self.com, "GetFirstSubFeature")
        while child is not None:
            found.append(Feature(child, self._document))
            child = com.call(child, "GetNextSubFeature")
        return found

    @property
    def dimensions(self):
        """The full names of this feature's dimensions, as a list of str.

        Feed one to ``document.dimensions[...]`` to read or set it.
        """
        from .dimensions import _dimension_names

        return _dimension_names(self.com)

    # ------------------------------------------------------------ niceties

    def __repr__(self):
        try:
            state = " suppressed" if self.suppressed else ""
            return f"<Feature {self.name!r} ({self.type}){state}>"
        except Exception:
            return "<Feature (not responding)>"

    def __eq__(self, other):
        if not isinstance(other, Feature):
            return NotImplemented
        try:
            return self.name == other.name and self.type == other.type
        except Exception:
            return self is other

    def __hash__(self):
        try:
            return hash((self.name, self.type))
        except Exception:
            return id(self)


class Features:
    """The feature tree of a document.

    Iterate it, index it by name or position, ``len()`` it, ``in`` it.

    Do not build this directly; use ``document.features``.

    Attributes:
        com  the raw ``IModelDoc2``
    """

    def __init__(self, model, document=None):
        self.com = model
        self._document = document

    def __iter__(self):
        """Every top-level tree entry, in tree order."""
        feature = com.call(self.com, "FirstFeature")
        while feature is not None:
            yield Feature(feature, self._document)
            feature = com.call(feature, "GetNextFeature")

    def __len__(self):
        return sum(1 for _ in self)

    def __getitem__(self, key):
        """By name, or by position in tree order.

        Raises KeyError for a name that is not there, IndexError for a
        position that is out of range.
        """
        if isinstance(key, int):
            for position, feature in enumerate(self):
                if position == key:
                    return feature
            raise IndexError(f"the feature tree has fewer than {key + 1} entries")

        for feature in self:
            if feature.name == key:
                return feature
        raise KeyError(
            f"no feature named {key!r}. "
            f"document.features.names() lists what is there."
        )

    def __contains__(self, key):
        name = key.name if isinstance(key, Feature) else key
        return any(feature.name == name for feature in self)

    def names(self):
        """Every tree entry's name, in tree order. As a list of str."""
        return [feature.name for feature in self]

    def solid_features(self):
        """The modelling features only, as a list of `Feature`.

        Drops the origin, the default planes and the folders - see
        `FURNITURE`. Use plain iteration when you want everything.
        """
        return [feature for feature in self if not feature.is_furniture]

    def of_type(self, type_name):
        """Every feature whose `Feature.type` is ``type_name``.

        As a list of `Feature`.

        Example::

            part.features.of_type("Extrusion")
        """
        return [feature for feature in self if feature.type == type_name]

    def types(self):
        """The distinct feature types present, sorted. As a list of str.

        The quickest way to find out what a model is made of.
        """
        return sorted({feature.type for feature in self})

    def __repr__(self):
        try:
            return f"<Features: {len(self)} tree entries>"
        except Exception:
            return "<Features (not responding)>"
