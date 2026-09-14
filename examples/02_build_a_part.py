"""Build a part from nothing: sketch, extrude, cut, measure.

Run it with the venv's Python::

    .venv\\Scripts\\python examples\\02_build_a_part.py

It makes a 60 by 40 plate 10 mm thick with a 12 mm hole through it, which is
small enough that every number can be checked by hand::

    volume = 60 * 40 * 10 - pi * 6**2 * 10 = 22869.0 mm3

Output on the machine this was written on::

    Drew Sketch1: 4 segments, lengths [60.0, 40.0, 60.0, 40.0] mm
    Extruded Boss-Extrude1
    Drew Sketch2: 1 segments, lengths [37.7] mm
    Cut Cut-Extrude1

    volume    : 22869.0 mm3   (arithmetic says 22869.0)
    area      : 6950.8 mm2
    mass      : 61.7 g        as 6061 Alloy
    bounding  : 60.0 x 40.0 x 10.0 mm

    faces     : 7   (6 plane, 1 cylinder)
    edges     : 14  (12 line, 2 circle)
    vertices  : 8

The part is left open, unsaved, so you can look at it.
"""

import math

import swcomapi as swc


def main():
    app = swc.connect()
    part = app.new_part()

    # add_to_db=True means the geometry goes in exactly as given: no inferred
    # relations, no snapping. It is what a script wants and not what a person
    # drawing with a mouse wants.
    with part.sketch_on("Front Plane", add_to_db=True) as sketch:
        sketch.rectangle((0, 0), (60, 40))
    drawn = part.sketches[-1]
    print(
        f"Drew {drawn.name}: {len(drawn)} segments, "
        f"lengths {[round(s.length, 1) for s in drawn.segments]} mm"
    )

    boss = part.extrude(10)
    print(f"Extruded {boss.name}")

    with part.sketch_on("Front Plane", add_to_db=True) as hole:
        hole.circle((30, 20), radius=6)
    drawn = part.sketches[-1]
    print(
        f"Drew {drawn.name}: {len(drawn)} segments, "
        f"lengths {[round(s.length, 1) for s in drawn.segments]} mm"
    )

    # reverse=True because the sketch is on the Front Plane and the material
    # is behind it. Without it the cut removes nothing, and SOLIDWORKS reports
    # that by returning None.
    cut = part.cut(through_all=True, reverse=True)
    print(f"Cut {cut.name}")

    part.material = "6061 Alloy"

    expected = 60 * 40 * 10 - math.pi * 6**2 * 10
    print()
    print(f"volume    : {part.volume:.1f} mm3   (arithmetic says {expected:.1f})")
    print(f"area      : {part.area:.1f} mm2")
    print(f"mass      : {part.mass:.1f} g        as {part.material}")

    body = part.bodies[0]
    x, y, z = body.size
    print(f"bounding  : {x:.1f} x {y:.1f} x {z:.1f} mm")

    planes = len(body.faces_of("plane"))
    cylinders = len(body.faces_of("cylinder"))
    lines = sum(1 for edge in body.edges if edge.kind == "line")
    circles = sum(1 for edge in body.edges if edge.kind == "circle")
    print()
    print(f"faces     : {len(body.faces)}   ({planes} plane, {cylinders} cylinder)")
    print(f"edges     : {len(body.edges)}  ({lines} line, {circles} circle)")
    print(f"vertices  : {len(body.vertices)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
