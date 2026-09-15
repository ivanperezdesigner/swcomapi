"""Sketches: reading them, and drawing new ones.

Drawing is a session, not a call. You open a sketch on a plane, add geometry
to it, and close it, and everything in between has to happen while that sketch
is the one being edited. That is what the context manager is for:

    >>> part = app.new_part()                               # doctest: +SKIP
    >>> with part.sketch_on("Front Plane", add_to_db=True) as sketch:  # doctest: +SKIP
    ...     _ = sketch.rectangle((0, 0), (60, 40))
    >>> part.extrude(10).name                               # doctest: +SKIP
    'Boss-Extrude1'

Everything in **mm**, as everywhere in ``swcomapi.api``. The API itself works
in metres; the conversion happens here.

The two traps
-------------

**A sketch left open.** If an exception escapes while a sketch is being
edited, SOLIDWORKS stays in sketch mode and every call after that behaves
oddly. The context manager closes the sketch on the way out whether the block
succeeded or not, which is the whole reason to use it rather than the two
calls by hand.

**Inference.** ``CreateLine`` and friends normally run through the same
inferencing a person's mouse does, so a line that nearly touches another gets
a coincident relation invented for it, and a rectangle comes out with the
relations a person would have got. For a script that wants exactly what it
said, ``add_to_db=True`` on `sketch_on` puts the sketch manager into
database mode: geometry goes straight in, with no relations and no snapping.
The cost is that nothing holds the sketch together afterwards.
"""

from collections.abc import Sequence

from .. import com
from ..errors import SwCallError
from ..units import mm, to_mm
from .selection import select

# swSketchSegments_e, as readable names.
SEGMENT_TYPES = {
    0: "line",
    1: "arc",
    2: "ellipse",
    3: "spline",
    4: "text",
    5: "parabola",
}


# What ``SketchAddConstraints`` calls each relation. The identifiers are the
# names of ``swConstraintType_e`` with an ``sg`` in front, which is a
# convention nothing states and everything relies on.
RELATIONS = {
    "horizontal": "sgHORIZONTAL2D",
    "vertical": "sgVERTICAL2D",
    "coincident": "sgCOINCIDENT",
    "collinear": "sgCOLINEAR",
    "concentric": "sgCONCENTRIC",
    "parallel": "sgPARALLEL",
    "perpendicular": "sgPERPENDICULAR",
    "tangent": "sgTANGENT",
    "equal": "sgSAMELENGTH",
    "fixed": "sgFIXED",
    "symmetric": "sgSYMMETRIC",
    "midpoint": "sgATMIDDLE",
    "merge": "sgMERGEPOINTS",
    "pierce": "sgPIERCE",
    "intersection": "sgATINTERSECT",
}


class Sketch:
    """One sketch, whether or not it is being edited.

    Attributes:
        com  the raw ``ISketch``
    """

    def __init__(self, sketch, document=None, feature=None):
        self.com = sketch
        self.document = document
        self._feature = feature

    @property
    def name(self):
        """The sketch's name, as a str: ``'Sketch1'``.

        Sitting on the feature, not on the sketch: ``ISketch`` has no name of
        its own. Empty when the sketch was reached without its feature, which
        happens for the one currently being edited.
        """
        if self._feature is None:
            return ""
        return com.call(self._feature, "Name")

    @property
    def is_3d(self):
        """True for a 3D sketch, as a bool."""
        return bool(com.call(self.com, "Is3D"))

    @property
    def segments(self):
        """The lines, arcs and the rest, as a list of `Segment`."""
        return [
            Segment(segment)
            for segment in com.to_list(com.call(self.com, "GetSketchSegments"))
        ]

    @property
    def points(self):
        """Every sketch point, as a list of ``(x, y, z)`` tuples in mm.

        Includes the endpoints of the segments, which is what makes this
        useful for checking what was drawn.
        """
        points = com.to_list(com.call(self.com, "GetSketchPoints2"))
        return [
            (
                to_mm(com.call(point, "X")),
                to_mm(com.call(point, "Y")),
                to_mm(com.call(point, "Z")),
            )
            for point in points
        ]

    def __len__(self):
        return len(com.to_list(com.call(self.com, "GetSketchSegments")))

    def __repr__(self):
        name = self.name or "being edited"
        return f"<Sketch {name!r}: {len(self)} segments>"


class Segment:
    """One line, arc, spline or ellipse in a sketch.

    Attributes:
        com  the raw ``ISketchSegment``
    """

    def __init__(self, segment):
        self.com = segment

    @property
    def kind(self):
        """What it is, as a str: ``'line'``, ``'arc'``, ``'spline'``...

        One of the values in `SEGMENT_TYPES`.
        """
        code = int(com.call(self.com, "GetType"))
        return SEGMENT_TYPES.get(code, f"unknown ({code})")

    @property
    def length(self):
        """Its length in mm, as a float.

        For an arc this is the arc length, not the chord.
        """
        return to_mm(com.call(self.com, "GetLength"))

    @property
    def is_construction(self):
        """True for construction geometry, as a bool.

        A centreline, or anything switched to construction. It does not
        contribute to a profile, which is why a failing extrusion is often
        this.
        """
        return bool(com.call(self.com, "ConstructionGeometry"))

    def __repr__(self):
        construction = ", construction" if self.is_construction else ""
        return f"<Segment {self.kind} {self.length:.3f} mm{construction}>"


class Sketches(Sequence):
    """The sketches in a document.

    A sequence, and a lookup by name:

        >>> part.sketches.names()               # doctest: +SKIP
        ['Sketch1', 'Sketch2']
        >>> part.sketches["Sketch1"]            # doctest: +SKIP
        <Sketch 'Sketch1': 4 segments>
        >>> len(part.sketches)                  # doctest: +SKIP
        2

    Reached through the feature tree, so the order is the tree's order and a
    sketch absorbed into a feature is still here.
    """

    def __init__(self, document):
        self.document = document

    def _entries(self):
        """``(feature, ISketch)`` for every sketch in the tree.

        ``IFeature.GetSpecificFeature2`` is what turns the tree entry into the
        sketch; a feature that is not a sketch answers None to it, which is
        also how a 3D sketch and a profile sketch end up in the same list.
        """
        found = []
        for feature in self.document.features:
            if feature.type not in ("ProfileFeature", "3DProfileFeature"):
                continue
            sketch = com.call(feature.com, "GetSpecificFeature2")
            if sketch is not None:
                found.append((feature.com, sketch))
        return found

    def __len__(self):
        return len(self._entries())

    def __iter__(self):
        for feature, sketch in self._entries():
            yield Sketch(sketch, self.document, feature)

    def __getitem__(self, key):
        if isinstance(key, str):
            for sketch in self:
                if sketch.name == key:
                    return sketch
            raise KeyError(
                f"no sketch named {key!r} in {self.document.name!r}; "
                f"see .names()"
            )
        entries = self._entries()
        if isinstance(key, slice):
            return [Sketch(s, self.document, f) for f, s in entries[key]]
        feature, sketch = entries[key]
        return Sketch(sketch, self.document, feature)

    def names(self):
        """Every sketch name, as a list of str."""
        return [sketch.name for sketch in self]

    @property
    def active(self):
        """The sketch being edited, as a `Sketch`, or None."""
        sketch = com.call(self.manager, "ActiveSketch")
        if sketch is None:
            return None
        return Sketch(sketch, self.document)

    @property
    def manager(self):
        """The raw ``ISketchManager``."""
        return com.call(self.document.com, "SketchManager")

    def __repr__(self):
        return f"<Sketches: {len(self)} in {self.document.name!r}>"


class SketchSession:
    """A sketch open for editing, with the drawing methods on it.

    Built by `swcomapi.api.document.Part.sketch_on`; not meant to be created
    directly. Use it as a context manager so the sketch is closed even when
    something goes wrong:

        >>> with part.sketch_on("Top Plane", add_to_db=True) as sketch:  # doctest: +SKIP
        ...     _ = sketch.rectangle((-30, -20), (30, 20))
        >>> part.sketches.names()[-1]                   # doctest: +SKIP
        'Sketch3'

    Coordinates are in mm, in the sketch's own plane: x and y across it, z out
    of it. For a sketch on the Front Plane that means x right, y up and z
    towards you, whatever the model's orientation happens to be on screen.
    """

    def __init__(self, document, plane=None, add_to_db=False, three_d=False):
        self.document = document
        self.plane = plane
        self.add_to_db = add_to_db
        self.three_d = three_d
        self._previous_db = None
        self.com = None

    # ------------------------------------------------------------- the session

    @property
    def manager(self):
        """The raw ``ISketchManager``."""
        return com.call(self.document.com, "SketchManager")

    def open(self):
        """Start the sketch. Returns self.

        Selects the plane if one was named, then ``InsertSketch``. Raises
        `SwCallError` if the plane cannot be selected, because otherwise the
        sketch lands on whatever happened to be selected already, and finding
        that out later is expensive.
        """
        manager = self.manager

        if self.plane is not None:
            self.document.clear_selection()
            if not self.document.select(self.plane, "PLANE"):
                if not self.document.select(self.plane, "FACE"):
                    raise SwCallError(
                        f"cannot sketch on {self.plane!r}: nothing of that "
                        f"name is a plane or a face in "
                        f"{self.document.name!r}. The default planes are "
                        f"'Front Plane', 'Top Plane' and 'Right Plane'.",
                        member="SelectByID2",
                    )

        if self.add_to_db:
            self._previous_db = bool(com.call(manager, "AddToDB"))
            com.set_property(manager, "AddToDB", True)

        if self.three_d:
            com.call(manager, "Insert3DSketch", True)
        else:
            com.call(manager, "InsertSketch", True)

        self.com = com.call(manager, "ActiveSketch")
        return self

    def close(self, rebuild=True):
        """Finish the sketch. Returns the `Sketch` that was drawn.

        rebuild
            True lets SOLIDWORKS rebuild as it closes, which is what you want
            unless you are about to make more changes
        """
        manager = self.manager
        drawn = com.call(manager, "ActiveSketch")

        if self.three_d:
            com.call(manager, "Insert3DSketch", rebuild)
        else:
            com.call(manager, "InsertSketch", rebuild)

        if self._previous_db is not None:
            com.set_property(manager, "AddToDB", self._previous_db)
            self._previous_db = None

        # The selection is deliberately left alone. SOLIDWORKS leaves the
        # sketch it has just closed selected, and that is what the feature
        # calls work from: clearing here would mean every extrude had to name
        # its sketch again.
        return Sketch(drawn, self.document)

    def __enter__(self):
        return self.open()

    def __exit__(self, exc_type, exc, traceback):
        # Closed even when the block raised: a session left in sketch mode
        # makes every later call behave strangely, and the original error is
        # much easier to read than what that turns into.
        self.close()
        return False

    # ------------------------------------------------------------- drawing

    def line(self, start, end):
        """A line from ``start`` to ``end``. Returns a `Segment`.

        Both are ``(x, y)`` or ``(x, y, z)`` tuples in mm.

        Example, a 60 by 40 box drawn the long way:

            >>> with part.sketch_on("Top Plane", add_to_db=True) as sk:  # doctest: +SKIP
            ...     first = sk.line((0, 0), (60, 0))
            ...     second = sk.line((60, 0), (60, 40))
            >>> first.length, second.length                 # doctest: +SKIP
            (60.0, 40.0)
        """
        x1, y1, z1 = _point(start)
        x2, y2, z2 = _point(end)
        return Segment(com.call(self.manager, "CreateLine", x1, y1, z1, x2, y2, z2))

    def centreline(self, start, end):
        """A construction line from ``start`` to ``end``. Returns a `Segment`.

        The axis a revolve or a mirror needs. Spelled ``centerline`` too, for
        whichever way you type it.
        """
        x1, y1, z1 = _point(start)
        x2, y2, z2 = _point(end)
        return Segment(
            com.call(self.manager, "CreateCenterLine", x1, y1, z1, x2, y2, z2)
        )

    centerline = centreline

    def circle(self, centre, radius):
        """A circle. Returns a `Segment`.

        centre
            ``(x, y)`` or ``(x, y, z)`` in mm
        radius
            in mm

        Example:

            >>> with part.sketch_on("Top Plane", add_to_db=True) as sk:  # doctest: +SKIP
            ...     drawn = sk.circle((30, 20), 6)
            >>> drawn.kind                                  # doctest: +SKIP
            'arc'
        """
        x, y, z = _point(centre)
        return Segment(
            com.call(self.manager, "CreateCircleByRadius", x, y, z, mm(radius))
        )

    def arc(self, centre, start, end, clockwise=False):
        """An arc around ``centre`` from ``start`` to ``end``, a `Segment`.

        All three are points in mm. ``clockwise=False`` sweeps the way
        SOLIDWORKS calls +1.
        """
        xc, yc, zc = _point(centre)
        x1, y1, z1 = _point(start)
        x2, y2, z2 = _point(end)
        direction = -1 if clockwise else 1
        return Segment(
            com.call(
                self.manager,
                "CreateArc",
                xc, yc, zc, x1, y1, z1, x2, y2, z2, direction,
            )
        )

    def rectangle(self, corner, opposite):
        """A rectangle between two opposite corners. Returns four `Segment`.

        Both corners are ``(x, y)`` or ``(x, y, z)`` in mm.

        Example, 60 by 40 from the origin:

            >>> with part.sketch_on("Top Plane", add_to_db=True) as sk:  # doctest: +SKIP
            ...     drawn = sk.rectangle((0, 0), (60, 40))
            >>> sorted(round(s.length) for s in drawn)      # doctest: +SKIP
            [40, 40, 60, 60]
        """
        x1, y1, z1 = _point(corner)
        x2, y2, z2 = _point(opposite)
        drawn = com.call(
            self.manager, "CreateCornerRectangle", x1, y1, z1, x2, y2, z2
        )
        return [Segment(segment) for segment in com.to_list(drawn)]

    def centre_rectangle(self, centre, corner):
        """A rectangle centred on ``centre``. Returns four `Segment`.

        Spelled ``center_rectangle`` too. A 60 by 40 box about the origin is
        ``sketch.centre_rectangle((0, 0), (30, 20))``.
        """
        x1, y1, z1 = _point(centre)
        x2, y2, z2 = _point(corner)
        drawn = com.call(
            self.manager, "CreateCenterRectangle", x1, y1, z1, x2, y2, z2
        )
        return [Segment(segment) for segment in com.to_list(drawn)]

    center_rectangle = centre_rectangle

    def point(self, at):
        """A sketch point. Returns the raw ``ISketchPoint``."""
        x, y, z = _point(at)
        return com.call(self.manager, "CreatePoint", x, y, z)

    def use_edges(self, chain=True, inner_loops=False):
        """Convert the selected edges into sketch geometry. Returns True.

        Select the edges first with ``document.select(...)``; this is
        "Convert Entities" in the interface.
        """
        return bool(com.call(self.manager, "SketchUseEdge3", chain, inner_loops))

    # --------------------------------------------------------- constraining

    def dimension(self, entities, at, value=None, name=None):
        """Add a driving dimension. Returns its full name, as a str.

        entities
            what to measure: one `Segment` for its own length or diameter,
            two for the distance or angle between them. Sketch points work
            too, as `point` returns them
        at
            where the dimension sits, as ``(x, y)`` or ``(x, y, z)`` in mm.
            Away from the geometry, or SOLIDWORKS puts the text on top of it
        value
            what to drive it to, in mm - or degrees for an angle. None
            leaves it at whatever was drawn
        name
            rename it, so later code can say ``part.dimensions["width@..."]``
            instead of ``D1``

        Returns the name to use with `swcomapi.api.dimensions.Dimensions`:
        ``'width@Sketch1@plate.SLDPRT'``.

        Example, a rectangle driven to 60 by 30:

            >>> blank = app.new_part()                       # doctest: +SKIP
            >>> with blank.sketch_on("Front Plane") as sk:   # doctest: +SKIP
            ...     sides = sk.rectangle((0, 0), (50, 25))
            ...     wide = sk.dimension(sides[0], (25, -12), 60, name="width")
            >>> blank.dimensions["width@Sketch1"]            # doctest: +SKIP
            60.0

        **Do not pass ``add_to_db=True`` when you mean to dimension.** That
        mode exists to keep SOLIDWORKS from inventing relations, and a
        dimension is a relation: in database mode the geometry goes in
        unattached and the dimension has nothing to hold.
        """
        for position, entity in enumerate(_as_list(entities)):
            select(self.document, entity, append=position > 0)

        x, y, z = _point(at)
        display = com.call(self.document.com, "AddDimension2", x, y, z)
        if display is None:
            raise SwCallError(
                "SOLIDWORKS would not dimension that. One entity gives a "
                "length or a diameter, two give a distance or an angle; "
                "anything else it declines. In a sketch opened with "
                "add_to_db=True there is nothing to attach a dimension to.",
                member="AddDimension2",
            )

        measured = com.call(display, "GetDimension")
        if name is not None:
            com.set_property(measured, "Name", str(name))
        full = com.call(measured, "FullName")

        if value is not None:
            self.document.dimensions[full] = value
        return full

    def relate(self, entities, kind):
        """Add a geometric relation. Returns True.

        entities
            the segments or points to relate, as a list
        kind
            what to make it: one of the keys of `RELATIONS`
            - ``'horizontal'``, ``'vertical'``, ``'coincident'``,
            ``'collinear'``, ``'concentric'``, ``'parallel'``,
            ``'perpendicular'``, ``'tangent'``, ``'equal'``, ``'fixed'``,
            ``'symmetric'``, ``'midpoint'``, ``'merge'``, ``'pierce'`` -
            or the raw id SOLIDWORKS uses, such as ``'sgHORIZONTAL2D'``

        Example, two lines made equal:

            >>> blank = app.new_part()                       # doctest: +SKIP
            >>> with blank.sketch_on("Front Plane") as sk:   # doctest: +SKIP
            ...     a = sk.line((0, 0), (40, 0))
            ...     b = sk.line((40, 0), (40, 25))
            ...     _ = sk.relate([a, b], "equal")
            >>> len(blank.sketches["Sketch1"].segments)      # doctest: +SKIP
            2

        A relation that cannot hold - two lines already perpendicular made
        parallel - is refused by the solver, not by this call, and shows up
        as an over-defined sketch rather than an exception.
        """
        identifier = RELATIONS.get(str(kind).lower(), str(kind))
        for position, entity in enumerate(_as_list(entities)):
            select(self.document, entity, append=position > 0)
        com.call(self.document.com, "SketchAddConstraints", identifier)
        return True

    def offset(
        self,
        distance,
        entities=None,
        both_directions=False,
        chain=True,
        construction=False,
        dimension=False,
    ):
        """Offset the selected geometry. Returns True.

        distance
            how far, in mm. Negative goes the other way
        entities
            what to offset. None offsets whatever is selected already
        both_directions
            True offsets to each side
        chain
            True follows the chain of connected segments
        construction
            True makes the result construction geometry
        dimension
            True adds a driving dimension for the offset

        Example, a 3 mm inset round a rectangle:

            >>> blank = app.new_part()                       # doctest: +SKIP
            >>> with blank.sketch_on("Front Plane") as sk:   # doctest: +SKIP
            ...     sides = sk.rectangle((0, 0), (60, 30))
            ...     _ = sk.offset(-3, entities=sides)
            >>> len(blank.sketches["Sketch1"].segments) > 4  # doctest: +SKIP
            True
        """
        if entities is not None:
            for position, entity in enumerate(_as_list(entities)):
                select(self.document, entity, append=position > 0)
        return bool(
            com.call(
                self.manager,
                "SketchOffset2",
                mm(distance),
                bool(both_directions),
                bool(chain),
                0,                      # CapEnds: none
                1 if construction else 0,
                bool(dimension),
            )
        )

    def mirror(self, entities, about):
        """Mirror sketch geometry about a centreline. Returns True.

        entities
            the segments to mirror
        about
            the centreline to mirror across, as the `Segment` that
            `centreline` returned

        Example, half a profile made whole:

            >>> blank = app.new_part()                       # doctest: +SKIP
            >>> with blank.sketch_on("Front Plane") as sk:   # doctest: +SKIP
            ...     spine = sk.centreline((0, -20), (0, 20))
            ...     side = sk.line((10, -20), (10, 20))
            ...     _ = sk.mirror([side], about=spine)
            >>> len(blank.sketches["Sketch1"].segments)      # doctest: +SKIP
            3

        The centreline goes in last, which is what ``SketchMirror`` reads it
        from, and it has to be construction geometry - a plain line is not a
        mirror line however it is drawn.
        """
        for position, entity in enumerate(_as_list(entities)):
            select(self.document, entity, append=position > 0)
        select(self.document, about, append=True)
        com.call(self.document.com, "SketchMirror")
        return True

    def __repr__(self):
        where = f" on {self.plane!r}" if self.plane else ""
        return f"<SketchSession{where}>"


def _point(value):
    """A 2- or 3-tuple in mm, as three floats in metres.

    Examples::

        >>> _point((60, 40))
        (0.06, 0.04, 0.0)
        >>> _point((0, 0, 10))
        (0.0, 0.0, 0.01)
        >>> _point((1.5, 0))
        (0.0015, 0.0, 0.0)
    """
    values = tuple(value)
    if len(values) == 2:
        x, y = values
        z = 0.0
    elif len(values) == 3:
        x, y, z = values
    else:
        raise ValueError(
            f"a point is (x, y) or (x, y, z) in mm, not {values!r}"
        )
    return mm(x), mm(y), mm(z)


def _as_list(value):
    """One thing or many, always as a list.

    Examples::

        >>> _as_list(1)
        [1]
        >>> _as_list([1, 2])
        [1, 2]
    """
    if isinstance(value, (list, tuple)):
        return list(value)
    return [value]
