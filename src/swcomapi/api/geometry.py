"""The solid itself: bodies, faces, edges and vertices.

Underneath the feature tree there is geometry, and it answers different
questions. The tree says how the part was made; the geometry says what it
came out as, on a 60 by 40 by 10 plate with one 12 mm hole in it:

    >>> body = part.bodies[0]                   # doctest: +SKIP
    >>> len(body.faces)                         # doctest: +SKIP
    7
    >>> body.box                                # in mm  # doctest: +SKIP
    (0.0, 0.0, 0.0, 60.0, 40.0, 10.0)
    >>> len(body.edges)                         # 12 for a plain block  # doctest: +SKIP
    14
    >>> [round(f.area) for f in body.faces_of("cylinder")]   # mm2  # doctest: +SKIP
    [377]

Everything in **mm** and **mm2**, as everywhere in ``swcomapi.api``.

What this is for
----------------

Counting holes, measuring faces, finding the flat one to sketch on, checking a
bounding box before a machine ever sees the part. It is read-only: nothing
here changes the model, because changing geometry is the feature tree's job.

The empty tuple
---------------

``GetBodies2`` returns ``None`` rather than an empty array for a part with no
solid in it, and so do ``GetFaces`` and ``GetEdges`` further down. Every list
here comes back as a real list, empty when there is nothing, so a loop over a
blank part is a loop over nothing rather than a ``TypeError``.
"""

from .. import com
from ..units import to_mm, to_mm2, to_mm3, to_mm_all

# swSurfaceTypes_e, as readable names. The numbers start at 4001 because they
# are Parasolid's, not SOLIDWORKS'.
SURFACE_TYPES = {
    4001: "plane",
    4002: "cylinder",
    4003: "cone",
    4004: "sphere",
    4005: "torus",
    4006: "spline",
    4007: "blend",
    4008: "offset",
    4009: "extruded",
    4010: "revolved",
}

# What SOLIDWORKS uses when a document has no material assigned, in kg/m3.
# The same number the mass properties dialog falls back to.
DEFAULT_DENSITY = 1000.0

# swBodyType_e.
BODY_TYPES = {
    0: "solid",
    1: "sheet",
    2: "wire",
    3: "minimum",
    4: "general",
    5: "empty",
    6: "mesh",
    7: "graphics",
}


class Body:
    """One body: a solid, a surface or a wire.

    Attributes:
        com  the raw ``IBody2``
    """

    def __init__(self, body, document=None):
        self.com = body
        self.document = document

    @property
    def name(self):
        """The body's name, as a str.

        Usually the feature that made it - ``'Boss-Extrude1'`` - which is what
        the Solid Bodies folder shows.
        """
        return com.call(self.com, "Name")

    @property
    def kind(self):
        """What sort of body it is, as a str: ``'solid'``, ``'sheet'``...

        One of the values in `BODY_TYPES`.
        """
        code = int(com.call(self.com, "GetType"))
        return BODY_TYPES.get(code, f"unknown ({code})")

    @property
    def faces(self):
        """Every face, as a list of `Face`."""
        return [
            Face(face, self) for face in com.to_list(com.call(self.com, "GetFaces"))
        ]

    @property
    def edges(self):
        """Every edge, as a list of `Edge`."""
        return [
            Edge(edge, self) for edge in com.to_list(com.call(self.com, "GetEdges"))
        ]

    @property
    def vertices(self):
        """Every vertex, as a list of ``(x, y, z)`` tuples in mm."""
        return [
            _point_of(vertex)
            for vertex in com.to_list(com.call(self.com, "GetVertices"))
        ]

    @property
    def box(self):
        """The bounding box in mm, as ``(x1, y1, z1, x2, y2, z2)``.

        Two opposite corners, in the part's own coordinates. Returns None for
        a body with no extent - an empty one, or a wire body.

        Example, the stock a part needs:

            >>> x1, y1, z1, x2, y2, z2 = part.bodies[0].box     # doctest: +SKIP
            >>> (x2 - x1, y2 - y1, z2 - z1)                     # doctest: +SKIP
            (60.0, 40.0, 10.0)
        """
        values = com.to_list(com.call(self.com, "GetBodyBox"))
        if len(values) < 6:
            return None
        return tuple(to_mm_all(values[:6]))

    @property
    def size(self):
        """How big the bounding box is, as ``(x, y, z)`` in mm, or None.

        The box measured rather than located, which is the form a stock size
        or a shipping carton is written in.
        """
        box = self.box
        if box is None:
            return None
        return (box[3] - box[0], box[4] - box[1], box[5] - box[2])

    @property
    def volume(self):
        """The body's volume in mm3, as a float."""
        return to_mm3(self._mass_properties()[3])

    @property
    def area(self):
        """The body's surface area in mm2, as a float."""
        return to_mm2(self._mass_properties()[4])

    @property
    def density(self):
        """The density the mass is computed at, in kg/m3, as a float.

        The document's, which is the material's when one is assigned and
        1000 when none is - the same number the mass properties dialog uses.
        """
        from ..const import swMaterialPropertyDensity

        if self.document is None:
            return DEFAULT_DENSITY
        value = com.call(
            self.document.com, "GetUserPreferenceDoubleValue", swMaterialPropertyDensity
        )
        return float(value) or DEFAULT_DENSITY

    @property
    def mass(self):
        """The body's mass in grams, as a float.

        Computed at the document's `density`.
        """
        return self.mass_at(self.density)

    def mass_at(self, density):
        """What the body would weigh in a material of ``density``, in grams.

        density
            in kg/m3: 7800 for steel, 2700 for aluminium, 1000 for water

        Example, the same plate in steel and in aluminium:

            >>> round(body.mass_at(7800), 1)        # doctest: +SKIP
            178.4
            >>> round(body.mass_at(2700), 1)        # doctest: +SKIP
            61.7
        """
        return self._mass_properties(density)[5] * 1000.0

    @property
    def centre_of_mass(self):
        """Where the centre of mass is, as ``(x, y, z)`` in mm.

        Spelled ``center_of_mass`` too.
        """
        return tuple(to_mm_all(self._mass_properties()[0:3]))

    center_of_mass = centre_of_mass

    @property
    def material(self):
        """The material's internal id name, as a str.

        Empty when none is assigned. This is the id, not the display name -
        ``swcomapi.api.document.Part.material`` gives what the tree shows.
        """
        return com.call(self.com, "GetMaterialIdName")

    def _mass_properties(self, density=None):
        """``GetMassProperties``, as a list of floats in SI units.

        The layout, measured on a 60 by 40 by 10 plate::

            [0:3]  centre of mass, m
            [3]    volume, m3
            [4]    surface area, m2
            [5]    mass, kg
            [6:]   moments of inertia

        ``Density`` is not optional and it is not "use the material": passing
        0.0 gets a density of 1, so the mass comes back numerically equal to
        the volume. That is why `density` is looked up and passed.
        """
        if density is None:
            density = self.density
        return com.to_list(
            com.call(self.com, "GetMassProperties", float(density))
        )

    def faces_of(self, kind):
        """Every face of one sort, as a list of `Face`.

        kind
            one of the values in `SURFACE_TYPES`: ``'plane'``,
            ``'cylinder'``, ``'cone'``...

        Example, counting drilled holes by their cylindrical walls:

            >>> len(part.bodies[0].faces_of("cylinder"))    # doctest: +SKIP
            1
        """
        return [face for face in self.faces if face.kind == kind]

    def __repr__(self):
        return f"<Body {self.name!r} {self.kind}, {len(self.faces)} faces>"


class Face:
    """One face of a body.

    Attributes:
        com  the raw ``IFace2``
    """

    def __init__(self, face, body=None):
        self.com = face
        self.body = body

    @property
    def kind(self):
        """What surface it lies on, as a str: ``'plane'``, ``'cylinder'``...

        One of the values in `SURFACE_TYPES`. This is the shape of the
        surface, not of the face: a face cut out of a plane is still a plane.
        """
        surface = com.call(self.com, "GetSurface")
        if surface is None:
            return "unknown"
        code = int(com.call(surface, "Identity"))
        return SURFACE_TYPES.get(code, f"unknown ({code})")

    @property
    def area(self):
        """The face's area in mm2, as a float."""
        return to_mm2(com.call(self.com, "GetArea"))

    @property
    def normal(self):
        """The outward normal, as an ``(x, y, z)`` unit vector, or None.

        Dimensionless, so no conversion: ``(0.0, 0.0, 1.0)`` is the front face
        of a plate sketched on the Front Plane.

        None for a face that has no single normal - a cylinder, a sphere, a
        spline. SOLIDWORKS answers those with ``(0, 0, 0)``, which would read
        as a direction and is not one.
        """
        values = com.to_list(com.call(self.com, "Normal"))
        if len(values) < 3 or not any(values[:3]):
            return None
        return tuple(values[:3])

    @property
    def box(self):
        """The face's bounding box in mm, as ``(x1, y1, z1, x2, y2, z2)``."""
        values = com.to_list(com.call(self.com, "GetBox"))
        if len(values) < 6:
            return None
        return tuple(to_mm_all(values[:6]))

    @property
    def edges(self):
        """The edges around the face, as a list of `Edge`."""
        return [
            Edge(edge, self.body)
            for edge in com.to_list(com.call(self.com, "GetEdges"))
        ]

    def select(self, append=False):
        """Select the face. Returns True.

        ``Select4`` is declared on ``IEntity``, not on ``IFace2``, and a face
        is an entity at run time - which is exactly the sort of thing late
        binding gets right and a generated wrapper would not.
        """
        return bool(com.call(self.com, "Select4", append, None))

    def __repr__(self):
        return f"<Face {self.kind} {self.area:.3f} mm2>"


class Edge:
    """One edge of a body.

    Attributes:
        com  the raw ``IEdge``
    """

    def __init__(self, edge, body=None):
        self.com = edge
        self.body = body

    @property
    def length(self):
        """The edge's length in mm, as a float.

        Measured between the edge's own parameters rather than the whole
        curve's: a circular edge belongs to a full circle, and asking the
        curve for its length would give the circumference every time.
        """
        params = com.call(self.com, "GetCurveParams3")
        curve = com.call(self.com, "GetCurve")
        if params is None or curve is None:
            return 0.0
        start = com.call(params, "UMinValue")
        end = com.call(params, "UMaxValue")
        return to_mm(com.call(curve, "GetLength3", start, end))

    @property
    def kind(self):
        """What the edge is, as a str: ``'line'``, ``'circle'`` or ``'curve'``.

        The two that can be told apart cheaply are the two worth knowing: a
        straight edge and a circular one.
        """
        curve = com.call(self.com, "GetCurve")
        if curve is None:
            return "unknown"
        if com.call(curve, "IsLine"):
            return "line"
        if com.call(curve, "IsCircle"):
            return "circle"
        return "curve"

    @property
    def start(self):
        """Where the edge starts, as ``(x, y, z)`` in mm, or None.

        None for a closed edge - a full circle has no ends.
        """
        return _point_of(com.call(self.com, "GetStartVertex"))

    @property
    def end(self):
        """Where the edge ends, as ``(x, y, z)`` in mm, or None."""
        return _point_of(com.call(self.com, "GetEndVertex"))

    @property
    def faces(self):
        """The two faces that meet at this edge, as a list of `Face`."""
        return [
            Face(face, self.body)
            for face in com.to_list(com.call(self.com, "GetTwoAdjacentFaces2"))
        ]

    def select(self, append=False):
        """Select the edge. Returns True."""
        return bool(com.call(self.com, "Select4", append, None))

    def __repr__(self):
        return f"<Edge {self.kind} {self.length:.3f} mm>"


def bodies_of(document, kind="solid", visible_only=False):
    """Every body in a part, as a list of `Body`.

    document
        the `swcomapi.api.document.Part`
    kind
        ``'solid'``, ``'sheet'``, ``'wire'`` or ``'all'``
    visible_only
        True leaves out the hidden ones

    Example:

        >>> len(bodies_of(part))                    # the solids  # doctest: +SKIP
        1
        >>> len(bodies_of(part, kind="all"))    # surfaces too  # doctest: +SKIP
        1
    """
    from ..const import (
        swAllBodies,
        swSheetBody,
        swSolidBody,
        swWireBody,
    )

    wanted = {
        "solid": swSolidBody,
        "sheet": swSheetBody,
        "wire": swWireBody,
        "all": swAllBodies,
    }
    if kind not in wanted:
        raise ValueError(
            f"kind is one of {sorted(wanted)}, not {kind!r}"
        )

    found = com.call(document.com, "GetBodies2", wanted[kind], visible_only)
    return [Body(body, document) for body in com.to_list(found)]


def _point_of(vertex):
    """A vertex's position as ``(x, y, z)`` in mm, or None.

    ``GetPoint`` answers with three doubles in metres, and with None for a
    vertex that is not there - which is what a closed edge's ends are.
    """
    if vertex is None:
        return None
    values = com.to_list(com.call(vertex, "GetPoint"))
    if len(values) < 3:
        return None
    return tuple(to_mm_all(values[:3]))
