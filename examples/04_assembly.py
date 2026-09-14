"""Build an assembly and walk its components.

Run it with the venv's Python::

    .venv\\Scripts\\python examples\\04_assembly.py

It saves a plate into a temporary folder, inserts three instances of it into a
new assembly, and reads each one back.

Output on the machine this was written on::

    Saved the plate: 60 x 40 x 10 mm, 6061 Alloy, 64.8 g

    3 components, from 1 distinct file

    plate-1    resolved   fixed     at (-30.0, -20.0, -5.0) mm
    plate-2    resolved   floating  at (-30.0, 40.0, -5.0) mm
    plate-3    resolved   floating  at (-30.0, 100.0, -5.0) mm

    total mass: 194.4 g

    Suppressing plate-2:
      state     : suppressed
      document  : None            nothing is loaded
      mass now  : 129.6 g

    Resolved again: 194.4 g

Everything is closed and deleted at the end.
"""

import os
import shutil
import tempfile

import swcomapi as swc


def main():
    app = swc.connect()
    folder = tempfile.mkdtemp(prefix="swcomapi-example-")

    try:
        part = app.new_part()
        with part.sketch_on("Front Plane", add_to_db=True) as sketch:
            sketch.rectangle((0, 0), (60, 40))
        part.extrude(10)
        part.material = "6061 Alloy"
        plate = os.path.join(folder, "plate.SLDPRT")
        part.save_as(plate)
        print(
            f"Saved the plate: 60 x 40 x 10 mm, {part.material}, {part.mass:.1f} g"
        )

        asm = app.new_assembly()
        # add() opens the file first. AddComponent5 needs it loaded in the
        # session: given a path to something closed it inserts nothing,
        # complains about nothing and returns None.
        asm.components.add(plate)
        asm.components.add(plate, at=(0, 60, 0))
        asm.components.add(plate, at=(0, 120, 0))
        asm.rebuild()

        components = sorted(asm.components, key=lambda c: c.name)
        distinct = {os.path.basename(c.path).lower() for c in components}
        print()
        print(f"{len(components)} components, from {len(distinct)} distinct file")
        print()
        for component in components:
            x, y, z = component.position
            print(
                f"{component.name:10s} {component.state:11s}"
                f"{'fixed' if component.fixed else 'floating':10s}"
                f"at ({x:.1f}, {y:.1f}, {z:.1f}) mm"
            )

        def total_mass():
            return sum(
                c.document.mass for c in asm.components if c.document is not None
            )

        print()
        print(f"total mass: {total_mass():.1f} g")

        # Suppressing is not hiding: a suppressed component is not loaded, not
        # mated, and not in the mass.
        second = asm.components["plate-2"]
        second.suppress()
        print()
        print("Suppressing plate-2:")
        print(f"  state     : {second.state}")
        print(f"  document  : {second.document}            nothing is loaded")
        print(f"  mass now  : {total_mass():.1f} g")

        second.resolve()
        print()
        print(f"Resolved again: {total_mass():.1f} g")

        app.close_all()
    finally:
        shutil.rmtree(folder, ignore_errors=True)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
