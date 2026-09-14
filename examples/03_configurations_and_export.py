"""Drive a part with configurations and export one file per size.

Run it with the venv's Python::

    .venv\\Scripts\\python examples\\03_configurations_and_export.py

It builds a plate, gives it three configurations at different thicknesses,
writes a part number into each, and exports a STEP from every one. This is the
shape of most real work: one model, a family of outputs.

Output on the machine this was written on::

    Built the plate: 60 x 40 x 10 mm

    configurations: ['Default', 'PLT-06', 'PLT-10', 'PLT-16']

    PLT-06   thickness  6.0 mm   mass  38.9 g   part number PLT-000-06
      -> PLT-06.step     15 KB
    PLT-10   thickness 10.0 mm   mass  64.8 g   part number PLT-000-10
      -> PLT-10.step     15 KB
    PLT-16   thickness 16.0 mm   mass 103.7 g   part number PLT-000-16
      -> PLT-16.step     15 KB

    Written to C:\\Users\\...\\Temp\\swcomapi-example-xxxxxxxx

The part is closed without saving. Only the STEP files are left behind.
"""

import os
import tempfile

import swcomapi as swc

THICKNESSES = {"PLT-06": 6.0, "PLT-10": 10.0, "PLT-16": 16.0}


def main():
    app = swc.connect()
    folder = tempfile.mkdtemp(prefix="swcomapi-example-")

    part = app.new_part()
    with part.sketch_on("Front Plane", add_to_db=True) as sketch:
        sketch.rectangle((0, 0), (60, 40))
    part.extrude(10)
    part.material = "6061 Alloy"
    print("Built the plate: 60 x 40 x 10 mm")

    # The extrusion's depth. Its name carries the document's name, so it is
    # read rather than written down.
    depth = part.dimensions.names()[0]

    for name, thickness in THICKNESSES.items():
        part.configurations.add(name)       # adding activates it
        part.dimensions[depth] = thickness
        part.properties_of(name)["part number"] = f"PLT-000-{int(thickness):02d}"
        part.rebuild()

    print()
    print(f"configurations: {part.configurations.names()}")
    print()

    for name in THICKNESSES:
        part.configuration = name
        number = part.properties_of(name)["part number"]
        print(
            f"{name}   thickness {part.dimensions[depth]:4.1f} mm   "
            f"mass {part.mass:5.1f} g   part number {number}"
        )
        target = part.export(os.path.join(folder, f"{name}.step"))
        print(f"  -> {os.path.basename(target):15s} {os.path.getsize(target) // 1024} KB")

    print()
    print(f"Written to {folder}")

    part.close()        # without saving: the configurations were the point
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
