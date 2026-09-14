"""Put a part on a drawing and write the PDF.

Run it with the venv's Python::

    .venv\\Scripts\\python examples\\05_drawing.py

It builds a plate, saves it, makes a drawing with three views of it, and
exports a PDF into a temporary folder.

Output on the machine this was written on::

    Saved the plate to C:\\Users\\...\\Temp\\swcomapi-example-xxxxxxxx

    Sheet1: 279.4 x 215.9 mm at 1:5, third angle

    Drawing View1  named       at 2:1     (80.0, 150.0) mm
    Drawing View2  named       at 2:1     (80.0, 90.0) mm
    Drawing View3  named       at 1:2     (200.0, 150.0) mm

    Exported plate.pdf, 22 KB

The drawing and the part are left open so you can look at them; only the PDF
is written to disk.
"""

import os
import tempfile

import swcomapi as swc


def main():
    app = swc.connect()
    folder = tempfile.mkdtemp(prefix="swcomapi-example-")

    part = app.new_part()
    with part.sketch_on("Front Plane", add_to_db=True) as sketch:
        sketch.rectangle((0, 0), (60, 40))
    part.extrude(10)
    plate = os.path.join(folder, "plate.SLDPRT")
    part.save_as(plate)
    print(f"Saved the plate to {folder}")

    drawing = app.new_drawing()
    sheet = drawing.sheets.active
    width, height = sheet.size
    angle = "first" if sheet.first_angle else "third"
    numerator, denominator = sheet.scale
    print()
    print(
        f"{sheet.name}: {width:.1f} x {height:.1f} mm "
        f"at {numerator:g}:{denominator:g}, {angle} angle"
    )

    # Positions are in mm from the bottom-left corner of the sheet. The view
    # names go in as "Front" and "Top"; the API wants them asterisked and
    # views.add does that - plain "Front" gets no view and no error.
    drawing.views.add(plate, "Front", at=(80, 150))
    drawing.views.add(plate, "Top", at=(80, 90))
    drawing.views.add(plate, "Isometric", at=(200, 150), scale=(1, 2))

    print()
    for view in drawing.views:
        x, y = view.position
        scale = f"{view.scale:g}:1" if view.scale >= 1 else f"1:{1 / view.scale:g}"
        print(f"{view.name:14s} {view.kind:11s} at {scale:7s} ({x:.1f}, {y:.1f}) mm")

    target = drawing.export(os.path.join(folder, "plate.pdf"))
    print()
    print(f"Exported {os.path.basename(target)}, {os.path.getsize(target) // 1024} KB")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
