# swcomapi — reference

Every example here was run against SOLIDWORKS 2026 SP3 with the version of the
package in this repository, and every output is what it actually printed.
Nothing is illustrative.

```python
import swcomapi as swc
```

`swc`, not `sw`: [`swdesigntables`](https://github.com/ivanperezdesigner/swdesigntables)
already answers to that, and the two are meant to be used together.

- [1. Connecting](#1-connecting)
- [2. Documents](#2-documents)
- [3. Sketching](#3-sketching)
- [4. Dress-up: fillet, chamfer, shell, hole](#4-dress-up-fillet-chamfer-shell-hole)
- [5. Patterns and mirrors](#5-patterns-and-mirrors)
- [6. Reference geometry](#6-reference-geometry)
- [7. Features](#7-features)
- [8. Dimensions](#8-dimensions)
- [9. Custom properties](#9-custom-properties)
- [10. Configurations](#10-configurations)
- [11. Mass, material and geometry](#11-mass-material-and-geometry)
- [12. Equations](#12-equations)
- [13. Sheet metal](#13-sheet-metal)
- [14. Assemblies](#14-assemblies)
- [15. Drawings](#15-drawings)
- [16. Exporting](#16-exporting)
- [17. Enumerations and constants](#17-enumerations-and-constants)
- [18. Finding out what exists](#18-finding-out-what-exists)
- [19. Units](#19-units)
- [20. The escape hatch](#20-the-escape-hatch)
- [21. Errors](#21-errors)
- [22. What this package does not do](#22-what-this-package-does-not-do)

---

## 1. Connecting

Three ways in, and you almost always want the first.

```python
app = swc.connect()        # attach to a running SOLIDWORKS, or start one
app = swc.attach()         # attach only; raises if none is running
app = swc.launch()         # start a new one, always
```

`visible=None` leaves the window exactly as it was found, which is what you
want when a person is using that session:

```python
app = swc.attach(visible=None)
```

What the application knows about itself:

```python
app.version            # 'SOLIDWORKS 2026 SP3 (34.3.0)'
app.year               # 2026
app.revision_number    # '34.3.0'
app.service_pack       # 3
app.build_numbers      # ['sw2026_SP03', 'd260519.003', ' - Hotfix: #HF-1530816 ...']
app.visible            # True
app.documents          # []
app.active             # None
```

`year` is derived, not reported: SOLIDWORKS numbers its releases internally
from 28 for 2020, so the year is the major version plus 1992.

`build_numbers` is the first trap this package removes. `GetBuildNumbers2`
looks like it takes an argument and does not: all three of its parameters are
`[out]` strings and the method itself returns nothing. Called the way it reads
in the documentation it raises "Type mismatch".

---

## 2. Documents

```python
part = app.open("bracket.SLDPRT")       # a Part, Assembly or Drawing
part = app.new_part()
asm = app.new_assembly()
drawing = app.new_drawing()
```

`open` takes `configuration=`, `read_only=`, `silent=` and `view_only=`. A
relative path is resolved against the current directory, because SOLIDWORKS
resolves it against its own and that is never what you meant.

```python
part.kind          # 'part'
part.name          # 'plate.SLDPRT'
part.path          # 'C:\\work\\plate.SLDPRT'
part.folder        # 'C:\\work'
part.modified      # False
```

Use it as a context manager so nothing is left open when a script crashes:

```python
with app.open("bracket.SLDPRT") as part:
    part.export("bracket.step")
# closed, even if export raised
```

Leaving a document open is not harmless: the next run gets
`swFileLoadWarning_AlreadyOpen` and a document in a state the script did not
expect.

---

## 3. Sketching

A sketch is a session, not a call. The context manager closes it whether the
block succeeded or not — a session left in sketch mode makes every later call
behave strangely, and the original error then arrives buried.

```python
with part.sketch_on("Front Plane", add_to_db=True) as sketch:
    sketch.rectangle((0, 0), (60, 40))

part.extrude(10)

with part.sketch_on("Front Plane", add_to_db=True) as hole:
    hole.circle((30, 20), radius=6)

part.cut(through_all=True, reverse=True)
```

Everything in **mm**. What can be drawn:

| method | what it makes |
|---|---|
| `line(start, end)` | a line |
| `centreline(start, end)` | construction line, for a revolve axis |
| `circle(centre, radius)` | a circle |
| `arc(centre, start, end, clockwise=False)` | an arc |
| `rectangle(corner, opposite)` | four lines |
| `centre_rectangle(centre, corner)` | four lines, centred |
| `point(at)` | a sketch point |
| `use_edges(chain=True)` | Convert Entities, on the selection |

`add_to_db=True` puts the sketch manager into database mode: geometry goes in
exactly as given, with no inferred relations and no snapping. That is what a
script usually wants. The cost is that nothing holds the sketch together
afterwards.

Reading sketches back:

```python
part.sketches                   # <Sketches: 2 in 'Part185'>
part.sketches.names()           # ['Sketch1', 'Sketch2']
part.sketches["Sketch1"]        # <Sketch 'Sketch1': 4 segments>

part.sketches["Sketch1"].segments
# [<Segment line 60.000 mm>, <Segment line 40.000 mm>,
#  <Segment line 60.000 mm>, <Segment line 40.000 mm>]

[s.length for s in part.sketches["Sketch1"].segments]   # [60.0, 40.0, 60.0, 40.0]
[s.kind for s in part.sketches["Sketch2"].segments]     # ['arc']

part.sketches["Sketch1"].points
# [(0.0, 0.0, 0.0), (60.0, 40.0, 0.0), (0.0, 40.0, 0.0), (60.0, 0.0, 0.0)]

part.sketches["Sketch1"].is_3d      # False
```

### Making features

```python
part.extrude(10)                            # blind, one direction
part.extrude(10, midplane=True)             # split either side of the sketch
part.extrude(10, draft=3)                   # 3 degrees of draft
part.extrude(10, sketch="Sketch1")          # name the sketch explicitly
part.cut(through_all=True, reverse=True)
part.cut(5)
part.revolve()                              # 360 degrees about the centreline
part.revolve(90)
```

Depths in mm, angles in degrees. A cut that points away from the material
removes nothing and SOLIDWORKS reports that as a bare `None`:

```python
part.cut(through_all=True)
# SwCallError: SOLIDWORKS would not cut in 'Part1'. The usual causes are a
# profile that is not closed and a sketch that is not selected, and for a cut,
# a direction that points away from the material - a sketch on the Front Plane
# cuts towards you unless you pass reverse=True.
```

### Dimensions and relations

A sketch drawn with `add_to_db=True` has no relations and no dimensions: the
geometry goes straight into the database, unattached. That is what you want
when a script is placing everything itself. When the sketch has to stay
parametric, leave `add_to_db` off and drive it:

```python
part = app.new_part()
with part.sketch_on("Front Plane") as sketch:
    sides = sketch.rectangle((0, 0), (50, 25))
    sketch.dimension(sides[0], at=(25, -12), value=60, name="width")
    sketch.dimension(sides[1], at=(-12, 12), value=30, name="height")

part.dimensions["width@Sketch1"]
# 60.0
```

`dimension` returns the full name `part.dimensions` wants, so the dimension it
just made is drivable from then on — including from a design table.

Relations by their English names:

```python
with part.sketch_on("Front Plane") as sketch:
    first = sketch.line((0, 0), (40, 0))
    second = sketch.line((40, 0), (40, 25))
    sketch.relate([first, second], "equal")
    sketch.relate([first], "horizontal")
```

`horizontal`, `vertical`, `coincident`, `collinear`, `concentric`, `parallel`,
`perpendicular`, `tangent`, `equal`, `fixed`, `symmetric`, `midpoint`,
`merge`, `pierce`, `intersection` — and the raw `sg` identifier for anything
else. There is also `sketch.offset(...)` and `sketch.mirror(...)`.

Trim and extend are not wrapped: both are pick-point operations whose
enumeration is not in every install, and a script that knows where its
geometry is has no reason to trim.


---

## 4. Dress-up: fillet, chamfer, shell, hole

None of these takes geometry as an argument in the raw API: they work from
what is selected. Here the geometry is the argument, and the selecting happens
for you.

```python
part = app.new_part()
with part.sketch_on("Front Plane", add_to_db=True) as sketch:
    sketch.rectangle((0, 0), (60, 40))
part.extrude(10)

part.fillet(2, edges=part.bodies[0].edges)
# <Feature 'Fillet1' (Fillet)>

part.chamfer(2, edges=part.bodies[0].edges)
# <Feature 'Chamfer1' (Chamfer)>
```

A chamfer takes an angle, or a second distance. `angle=` is ignored the moment
`other_distance=` is given, because SOLIDWORKS switches to a different chamfer
type:

```python
top = [f for f in part.bodies[0].faces if f.normal == (0.0, 0.0, 1.0)][0]
part.chamfer(3, edges=[top], other_distance=1)
```

Shell opens the faces you name and leaves a wall behind:

```python
part.shell(2, faces=[top])
```

`InsertFeatureShell` answers nothing at all — not the feature, not a bool — so
the feature comes back from the end of the tree, and a shell that failed is a
tree that did not grow. That is what `shell` checks.

A plain hole goes at a point **on the face**, in model coordinates:

```python
part.hole(6, at=(15, 10, 10), through_all=True)
```

That is the point the mouse would be over. There is no sketch: `SimpleHole2`
places the hole from the selection, and the selection is the face under that
point. A point that is not on a face raises rather than drilling somewhere
else.

The Hole Wizard is not wrapped. It takes thirty-one arguments and a standard
you have to name exactly; drive it through `part.com.FeatureManager` when you
need it.

---

## 5. Patterns and mirrors

A pattern is what to repeat, which way, and how many. The API takes only the
last as arguments; the first two are selections, filed under *marks*:

| mark | what goes in it |
| --- | --- |
| 1 | the direction, or the axis |
| 2 | the second direction, or the mirror plane |
| 4 | the features to repeat |

A mark in the wrong place does not fail. It makes a feature that is quietly
wrong — which is why the marking is not left to the caller.

```python
along = max(part.bodies[0].edges, key=lambda edge: edge.length)
part.patterns.linear("Cut-Extrude1", along, count=3, spacing=15)
# <Feature 'LPattern1' (LPattern)>
```

`count` is the total, including the original, the way the dialog means it:
`count=3` gives the original and two copies.

Round an axis, where a cylindrical face is its own axis:

```python
bore = part.bodies[0].faces_of("cylinder")[0]
part.patterns.circular("Cut-Extrude1", bore, count=4)
# <Feature 'CirPattern1' (CirPattern)>
```

And a mirror, about a plane or a flat face:

```python
part.mirror("Boss-Extrude1", about="Right Plane")
```

Pass a body instead of a feature name and the whole body is mirrored:

```python
part.mirror(part.bodies[0], about="Right Plane")
```

---

## 6. Reference geometry

Nothing is modelled on a reference plane, and almost everything needs one.

```python
above = part.plane("Top Plane", distance=25)
# <Feature 'Plane1' (RefPlane)>

with part.sketch_on(above.name, add_to_db=True) as sketch:
    sketch.rectangle((0, 0), (20, 20))
```

Halfway between two faces, which is the one people reach for most:

```python
faces = part.bodies[0].faces_of("plane")
part.plane(faces[0], second=faces[1], midplane=True)
```

An angled plane needs the line it hinges on as well — a plane and an angle
alone do not place one, and `plane` says so rather than letting SOLIDWORKS
refuse:

```python
part.plane(face, angle=30, second=edge)
```

Axes the same way: one cylindrical face is enough, two planes give the line
where they cross.

```python
part.axis("Front Plane", "Right Plane")
# <Feature 'Axis1' (RefAxis)>
part.axis(bore)
```

A cylindrical face already has a temporary axis a pattern can turn about, so
make a real one only when it has to be selectable by name later.

---

## 7. Features

```python
part.features.names()
# ['Comments', 'Favorites', 'History', 'Selection Sets', 'Sensors',
#  'Design Binder', 'Annotations', 'Surface Bodies', 'Solid Bodies',
#  'Lights and Cameras', 'Markups', 'Equations', 'Material <not specified>',
#  'Front Plane', 'Top Plane', 'Right Plane', 'Origin', 'Sketch1',
#  'Boss-Extrude1', 'Sketch2', 'Cut-Extrude1']

part.features.solid_features()
# [<Feature 'Boss-Extrude1' (Extrusion)>, <Feature 'Cut-Extrude1' (ICE)>]

part.features.types()
# ['CommentsFolder', 'DetailCabinet', 'DocsFolder', 'EnvFolder', 'EqnFolder',
#  'Extrusion', 'FavoriteFolder', 'HistoryFolder', 'ICE', 'InkMarkupFolder',
#  'MaterialFolder', 'OriginProfileFeature', 'ProfileFeature', 'RefPlane',
#  'SelectionSetFolder', 'SensorFolder', 'SolidBodyFolder', 'SurfaceBodyFolder']

part.features.of_type("Extrusion")          # [<Feature 'Boss-Extrude1' (Extrusion)>]
part.features["Boss-Extrude1"]              # <Feature 'Boss-Extrude1' (Extrusion)>
part.features[-1]                           # the last one in the tree
len(part.features)                          # 21
```

`solid_features()` drops the origin, the planes and every folder.
`part.features["Front Plane"].is_furniture` is `True`.

A cut extrusion's type name is `ICE`, not `Cut-Extrude`. That is SOLIDWORKS'
own name for it, and it is what `of_type` matches on.

### Suppression

```python
feature = part.features["Fillet1"]
feature.suppressed                                  # False
feature.suppress()
feature.unsuppress(with_dependents=True)
feature.suppress(in_configurations=["BRK-020"])
feature.suppress(everywhere=True)
```

`SetSuppression2` returns `True` for a change it did not make. A feature whose
state is driven by a configuration table keeps its state, the call reports
success, and the tree does not move. This package reads the state back:

```python
# SwCallError: SOLIDWORKS reported success but 'Fillet1' is still
# unsuppressed. The usual cause is a configuration table driving
# $STATE@Fillet1: the table owns the state and a direct call cannot override
# it. Change the table, or the sketch or feature it is built on.
```

---

## 8. Dimensions

In **millimetres and degrees**, both ways. The API works in metres and
radians; the conversion happens here.

```python
part.dimensions.names()             # ['D1@Boss-Extrude1@Part185.Part']
part.dimensions["D1@Boss-Extrude1@Part185.Part"]        # 10.0
part.dimensions["D1@Boss-Extrude1@Part185.Part"] = 80
part.rebuild()
part.dimensions["D1@Boss-Extrude1@Part185.Part"]        # 80.0

dict(part.dimensions)               # {'D1@Boss-Extrude1@Part185.Part': 80.0}
part.dimensions.is_angular("D1@Boss-Extrude1@Part185.Part")     # False
```

An angular dimension comes back in degrees, and is written in degrees. Which
dimensions are angular is worked out from the enumeration by name, not from a
list written by hand — an earlier version of this package had the two linear
types in that list and would have converted every length through radians.

---

## 9. Custom properties

A `MutableMapping`, so it behaves like a dict.

```python
part.properties["Revision"] = "B"
part.properties["Designer"] = "I. Perez"

dict(part.properties)               # {'Revision': 'B', 'Designer': 'I. Perez'}
len(part.properties)                # 2
"Revision" in part.properties       # True
part.properties.get("Nothing", "-") # '-'
del part.properties["Designer"]
dict(part.properties)               # {'Revision': 'B'}
```

Per configuration:

```python
part.properties_of("BRK-040")["part number"]        # 'ABC000-0003A'
dict(part.properties_of("BRK-060-ANOD"))
# {'part number': 'ABC000-0003A', 'finish': 'ANODIZED'}
```

A property that is **there and empty** is not the same as one that is not
there. `Get6` reports both with an empty value and `WasResolved` True; its
return code is the only thing that distinguishes them, and that is what this
package reads.

To see the formula rather than the result:

```python
part.properties["Mass"] = '"SW-Mass@@Default@Part189"'
part.properties.expression_of("Mass")       # '"SW-Mass@@Default@Part189"'
part.properties["Mass"]                     # '65'
```

---

## 10. Configurations

```python
part.configurations                 # <Configurations: 1 - active 'Default'>
part.configurations.names()         # ['Default']
part.configuration                  # 'Default'

part.configurations.add("Heavy", description="thicker")
part.configurations.names()         # ['Default', 'Heavy']
part.configuration                  # 'Heavy'   - adding activates it

part.configuration = "Default"
```

`add` also makes derived configurations, with `parent=`. Reading per
configuration goes through `swSpecifyConfiguration`, not
`swThisConfiguration`: the latter reads the active one and ignores the name
list, silently.

---

## 11. Mass, material and geometry

```python
part.mass               # 137.21415986824604      grams
part.volume             # 137214.15986824603      mm3
part.area               # 18835.752039526185      mm2
part.centre_of_mass     # (30.0, 20.0, 30.0)      mm

part.mass_properties
# {'centre': (30.0, 20.0, 30.0), 'volume': 137214.16, 'area': 18835.75,
#  'mass': 137.21, 'density': 0.001}
```

### Material

```python
part.material                   # ''
part.material = "6061 Alloy"
part.material                   # '6061 Alloy'
part.material_database          # 'SOLIDWORKS Materials'
part.mass                       # 370.4782316442643

part.material_of("BRK-040")     # per configuration
part.set_material("AISI 304", configuration="BRK-040")
```

A name the library does not have applies nothing and reports nothing through
the raw call, so this package reads it back:

```python
part.material = "Unobtainium"
# SwCallError: 'Unobtainium' was not applied; the part now has 6061 Alloy.
# The name has to be spelled as the material tree shows it...
```

What libraries are available:

```python
from swcomapi.api.materials import database_names
database_names(app)
# ['custom materials', 'solidworks din materials', 'solidworks materials',
#  'sustainability extras']
```

### The solid itself

```python
part.bodies                     # [<Body 'Cut-Extrude1' solid, 7 faces>]
body = part.bodies[0]

body.name                       # 'Cut-Extrude1'
body.kind                       # 'solid'
body.size                       # (60.0, 40.0, 60.0)     mm
body.box                        # (0.0, 0.0, 0.0, 60.0, 40.0, 60.0)
body.mass_at(7800)              # 1070.270446972319      grams, as steel

len(body.faces)                 # 7
sorted({f.kind for f in body.faces})    # ['cylinder', 'plane']
len(body.faces_of("plane"))             # 6

hole = body.faces_of("cylinder")[0]
hole                            # <Face cylinder 2261.947 mm2>
hole.area                       # 2261.9467105846506
hole.normal                     # None

len(body.edges)                 # 14
sorted({e.kind for e in body.edges})    # ['circle', 'line']
circle = next(e for e in body.edges if e.kind == "circle")
circle                          # <Edge circle 37.699 mm>
circle.length                   # 37.6991118430775
len(body.vertices)              # 8
```

Three things measured rather than assumed, and all three are easy to get
wrong:

- `IBody2.GetMassProperties` takes a density, and `0.0` does not mean "use the
  material" — it means a density of 1, so the mass comes back numerically
  equal to the volume. `body.mass` looks up the document's density and passes
  it.
- A curved face has no single normal. SOLIDWORKS answers `(0, 0, 0)`, which
  reads as a direction and is not one, so `Face.normal` is `None` there.
- An edge's length is measured between its own curve parameters. Asking the
  curve would give the full circumference for every circular edge.

---

## 12. Equations

```python
part.equations.add('"width" = 60')
part.equations.add('"height" = "width" * 0.5')

list(part.equations)            # ['"width" = 60', '"height" = "width" * 0.5']
part.equations.names()          # ['width', 'height']
part.equations.globals()        # {'width': 60.0, 'height': 30.0}
part.equations["height"]        # 30.0

part.equations["width"] = 80
part.equations.globals()        # {'width': 80.0, 'height': 40.0}
part.equations                  # <Equations: 2, 2 of them global variables>

part.equations[0] = '"width" = 90'      # rewrite the whole line
del part.equations[1]
```

**Equations are in the document's own units**, not in metres — the one place
in this package where that is true, because an equation is a string SOLIDWORKS
parses rather than a number it stores.

Two things worth knowing:

- `IEquationMgr.Equation` is an indexed property, and Python cannot spell a
  write to one: an attribute assignment has nowhere to put the index. It goes
  through `swcomapi.com.set_property_at`.
- `Add3` is the current call and it returns -1 for every combination tried on
  2026 SP3. `Add2` adds the same equation and works, so that is what is used —
  which is why there is no per-configuration argument.

---

## 13. Sheet metal

```python
part.is_sheet_metal             # True
part.sheet_metal.thickness      # 2.0        mm
part.sheet_metal.bend_radius    # 3.0        mm
part.sheet_metal.k_factor       # 0.5
part.sheet_metal.bend_allowance # 'k-factor'

part.sheet_metal.as_dict()
# {'thickness': 2.0, 'bend_radius': 3.0, 'k_factor': 0.5,
#  'bend_allowance': 'k-factor', 'relief_ratio': 0.5}

part.export_flat_pattern("blank.dxf")
```

`IFeature.GetDefinition` hands back an `ISheetMetalFeatureData` and SOLIDWORKS
holds the feature while you have it. Not releasing it leaves the feature
locked for the rest of the session: the tree still shows it, editing it does
nothing, and nothing says why. Every read here releases.

---

## 14. Assemblies

```python
asm = app.new_assembly()
asm.components.add(plate)
asm.components.add(plate, at=(0, 60, 0))
asm.components.add(plate, at=(0, 120, 0))
```

`at` is in mm, and SOLIDWORKS lands the component's **bounding-box centre** on
that point, not its origin.

```python
asm.components                  # <Components: 3 at the top level>
sorted(asm.components.names())  # ['plate-1', 'plate-2', 'plate-3']
asm.component_count             # 3
asm.components.paths()          # duplicates kept: three entries

one = asm.components[0]
one                             # <Component 'plate-2' resolved>
one.name                        # 'plate-2'
one.select_id                   # 'plate-2@Assem23'
one.configuration               # 'Default'
one.state                       # 'resolved'
one.suppressed                  # False
one.visible                     # True
one.fixed                       # False
one.position                    # (-30.0, 40.0, -5.0)       mm
one.box                         # (-30.0, 40.0, -5.0, 30.0, 80.0, 5.0)
one.document                    # <Part 'plate.SLDPRT'>
one.document.mass               # 64.8
one.children                    # []

asm.components.of_path("plate.SLDPRT")      # every instance of that file
asm.components.all()                        # every level, not just the top
asm.components["plate-2"]                   # by name
```

Suppressing and hiding are different things:

```python
one.suppress()
one.state                       # 'suppressed'
one.document                    # None       - nothing is loaded
one.resolve()

one.visible = False             # still loaded, still mated, still in the mass
```

`GetComponents` does **not** answer in insertion order, so index into it only
when you do not care which one you get; look components up by name when you
do.

`AddComponent5` needs the file already open in the session. Given a path to
something closed it inserts nothing, complains about nothing and returns
`None`. `components.add` opens it first, then brings the assembly to the
front — because `AddComponent5` inserts into whatever document is *active*,
not into the one it was called on.

### Mates

Inserting a component puts it somewhere. A mate is what stops it moving.

```python
rail, gusset = assembly.components.in_order()

assembly.mates.coincident(rail.plane("Top Plane"), gusset.plane("Top Plane"))
assembly.mates.distance(rail.plane("Right Plane"),
                        gusset.plane("Right Plane"), 80)
assembly.mates.names()
# ['Coincident1', 'Distance1']
```

`in_order()` is not decoration: `GetComponents` does not answer in insertion
order, and does not answer in the same order twice. Two examples in 0.1.1
passed one run and failed the next for exactly that reason.

What can be mated is geometry **of the instance**, not of the part file:

```python
rail.plane("Right Plane")
# ('Right Plane@rail-1@frame', 'PLANE')

rail.faces          # the faces of this instance
rail.document.bodies[0].faces   # the faces of the part file - not mateable
```

That distinction is the one that wastes an afternoon. A face read through
`component.document` belongs to the part, and `AddMate5` refuses it with a
status code rather than an error.

The named calls are `coincident`, `concentric`, `distance`, `parallel`,
`perpendicular`, `tangent`, `angle` and `lock`; `mates.add(first, second,
kind)` reaches the rest by name or by `swMateType_e` number. Distances are in
mm and angles in degrees, and a mate that fails says why:

```python
assembly.mates.concentric(rail.plane("Top Plane"), gusset.plane("Top Plane"))
# SwCallError: SOLIDWORKS would not add a concentric mate in 'frame.SLDASM':
# the two things cannot be mated that way.
```

Components move, and can be fixed where they are:

```python
gusset.move(by=(30, 0, 0))
gusset.fixed = True
```

A component held by mates moves and springs back, because the mates are
solved afterwards. That is deliberate — it is how you check that a mate
really holds.

And the interference check, run headless:

```python
assembly.interferences()
# [{'volume': 24000.0, 'components': ['rail-1', 'rail-2']}]
```

It loads every component fully, so it is slow on a big assembly and worth
doing once at the end rather than after every mate.


---

## 15. Drawings

```python
drawing = app.new_drawing()
front = drawing.views.add(plate, "Front", at=(80, 150))
top = drawing.views.add(plate, "Top", at=(80, 90))
iso = drawing.views.add(plate, "Isometric", at=(200, 150), scale=(1, 2))
drawing.export("plate.pdf")
```

Positions are in **mm from the bottom-left corner of the sheet**.

```python
drawing.sheets                  # <Sheets: 1 in 'Draw12 - Sheet1'>
drawing.sheets.names()          # ['Sheet1']
drawing.sheets.active           # <Sheet 'Sheet1' at 1:5>
drawing.sheets.active.size      # (279.4, 215.9)        mm
drawing.scale                   # (1.0, 5.0)
drawing.sheets.active.first_angle       # False - third angle

drawing.views                   # <Views: 3 on 'Sheet1'>
drawing.views.names()           # ['Drawing View1', 'Drawing View2', 'Drawing View3']
front                           # <View 'Drawing View1' named at 2:1>
front.position                  # (80.0, 150.0)
front.model                     # 'C:\\...\\plate.SLDPRT'
front.kind                      # 'named'
front.scale                     # 2.0
front.uses_sheet_scale          # True
iso.scale                       # 0.5
iso.uses_sheet_scale            # False - setting a scale is what detaches it

front.position = (100, 150)
front.activate()
```

Adding sheets:

```python
sheet = drawing.sheets.add("Detail", paper="A4", scale=(1, 2))
sheet                           # <Sheet 'Detail' at 1:2>
sheet.size                      # (297.0, 210.0)
drawing.sheets.names()          # ['Sheet1', 'Detail']
drawing.sheet = "Sheet1"
```

Three traps, all of them silent through the raw API:

- `CreateDrawViewFromModelView3` wants the standard views spelled with a
  leading asterisk — `"*Front"` — because that is how SOLIDWORKS names the
  views it supplies itself. Plain `"Front"` returns `None` and says nothing.
  `views.add` adds the asterisk for the nine standard names.
- `SetViewPosition` needs a SafeArray. Handed a Python tuple it returns `True`
  and moves the view somewhere else: `(150, 200)` mm came out at `(0, 150)`.
- `NewSheet4` takes the paper size twice, as `PaperSize` and as `TemplateIn`.

A view made from a model view reports its kind as `'named'`, not
`'standard'`; `'standard'` is what `Create3rdAngleViews2` lays out.

### Sections, details and annotations

A section view is cut along a line, and a detail view is blown up out of a
circle. Neither can be handed to the API as an argument, so both are drawn on
the sheet first — which is what these two do for you:

```python
front = drawing.views.add(path, "Front", at=(100, 100))

drawing.views.add_section(front, through=((100, 60), (100, 140)), at=(220, 100))
drawing.views.add_detail(front, centre=(100, 100), radius=12, at=(260, 160))
```

Everything is in mm on the sheet, measured from the bottom-left corner, for
the line and the circle as much as for the view. The line has to cross the
view; if SOLIDWORKS puts up a dialog asking about the section, it missed.

Then the annotations:

```python
front.insert_dimensions()           # the model's own dimensions
front.add_note("BREAK ALL EDGES 0.5", at=(20, 20))
front.add_balloons()                # assemblies only
front.add_bom(at=(280, 240), kind="top level")
```

`insert_dimensions` brings across the dimensions the model already has — the
same ones `part.dimensions` drives. A dimension changed on the sheet changes
the model.


---

## 16. Exporting

One call, and the extension decides the format:

```python
part.export("plate.step")
part.export("plate.pdf")
part.export("plate.stl")
part.export("plate.dxf")
part.export("plate.3mf")

part.save()
part.save_as("plate.SLDPRT")
part.export_flat_pattern("blank.dxf")       # sheet metal only
```

`SaveAs3` does not raise. It returns `False` and writes two bitmasks into its
last two parameters, and a script that ignores them reports success while
writing nothing. `export` decodes both:

```python
part.export("plate.nonsense")
# SwDocumentError: saving C:\work\plate.nonsense failed:
# swFileSaveAsInvalidFileExtension
```

Decoding a code by hand:

```python
from swcomapi.api.export import save_error_names, load_error_names, format_of

save_error_names(3)         # ['swGenericSaveError', 'swReadOnlySaveError']
save_error_names(256)       # ['swFileSaveAsInvalidFileExtension']
load_error_names(2)         # ['swFileNotFoundError']
format_of("plate.dxf")      # 'DXF'
```

---

## 17. Enumerations and constants

Every enumeration in the API, generated from the type libraries of the
SOLIDWORKS on this machine — 1,434 of them, 14,889 constants.

```python
from swcomapi import enums

enums.swDocumentTypes_e                     # <enum 'swDocumentTypes_e'>
enums.swDocumentTypes_e.swDocPART           # <swDocumentTypes_e.swDocPART: 1>
int(enums.swDocumentTypes_e.swDocPART)      # 1
enums.swDocumentTypes_e.__doc__             # 'swDocumentTypes_e (8 constants, from SwConst).'

len(enums.names())                          # 1434
enums.find("SaveAs")
# ['swEdrawingSaveAsOption_e', 'swSaveAsOptions_e', 'swSaveAsVersion_e',
#  'swSaveAsmAsPartOptions_e', 'swSustainabilitySaveAsFileType_e']
enums.library_of("swDocumentTypes_e")       # 'SwConst'
```

Or flat, the way VBA sees them:

```python
from swcomapi import const

const.swDocPART                 # 1
const.swSaveAsCurrentVersion    # 0
len(const.names())              # 14889
const.enum_of("swDocPART")      # 'swDocumentTypes_e'

const.find("swFileSave")[:3]
# [('swFileSave', 1, 'swFileSaveTypes_e'),
#  ('swFileSaveAs', 2, 'swFileSaveTypes_e'),
#  ('swFileSaveAsBadEDrawingsVersion', 1024, 'swFileSaveError_e')]
```

Both are lazy: importing `swcomapi` builds none of them. The names are in
`.pyi` stubs, so the editor and mypy see all 14,889 without any of them being
constructed at run time. Building them all eagerly costs about 158 ms per
import; this costs about 8 ms.

Everything is an `IntEnum` and nothing is an `IntFlag`, even the bitmasks:
SOLIDWORKS mixes flags and plain values inside the same enumeration, and an
`IntFlag` would refuse the values that are not powers of two.

---

## 18. Finding out what exists

The package ships an index of the whole API: 729 interfaces, 19,874 members,
17,097 of them with the vendor's own one-line description.

```python
swc.summary()
# SOLIDWORKS 2026 API index
#   10 type libraries
#   729 interfaces, 19874 members
#   17097 members with a description
#   1662 C++-only twins
#   1434 enumerations, 14889 constants

swc.find("GetMassProperties")
# ['IBody.GetMassProperties', 'IBody2.GetMassProperties',
#  'IModelDoc.GetMassProperties', 'IModelDocExtension.GetMassProperties']

swc.find_interface("MassProp")
# ['ICWMassPropertiesManager', 'IMassProperty', 'IMassProperty2',
#  'IMassPropertyOverrideOptions']
```

`describe` is the one to remember:

```python
print(swc.describe("IModelDocExtension.SaveAs3"))
```

```
IModelDocExtension.SaveAs3(Name, Version, Options, ExportData, AdvancedSaveAsOptions, Errors, Warnings) -> bool
  Saves the active document to the specified name in the specified format with advances SaveAsOptions.
  parameters:
    Name                   str    in
    Version                int    in
    Options                int    in
    ExportData             Any    in
    AdvancedSaveAsOptions  Any    in
    Errors                 int    inout   <- optional, comes back in the result
    Warnings               int    inout   <- optional, comes back in the result
  call it with: swcomapi.com.call_out(obj, 'SaveAs3', ...)
  docs: https://help.solidworks.com/2026/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs3.html
```

It works on enumerations and interfaces too:

```python
print(swc.describe("swDocumentTypes_e"))
```

```
swDocumentTypes_e  (enumeration, 8 constants, from SwConst)
  swDocNONE              = 0
  swDocPART              = 1
  swDocASSEMBLY          = 2
  swDocDRAWING           = 3
  swDocSDM               = 4
  swDocLAYOUT            = 5
  swDocIMPORTED_PART     = 6
  swDocIMPORTED_ASSEMBLY = 7
  docs: https://help.solidworks.com/2026/english/api/swconst/...
```

And a link to the official page for anything, built rather than fetched, so it
costs nothing and works offline:

```python
swc.doclink("IModelDoc2")
# 'https://help.solidworks.com/2026/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html'

swc.doclink("IModelDocExtension", "SaveAs3")
swc.doclink("swDocumentTypes_e")
swc.doclink("IModelDoc2", year=2027)
```

### What SOLIDWORKS writes into its parameters

```python
from swcomapi import signatures

signatures.outputs_of("OpenDoc6")
# ((4, 'Errors', 3, 'inout'), (5, 'Warnings', 3, 'inout'))

signatures.has_outputs("RevisionNumber")            # False
len(signatures.members_with_outputs())              # 982
sorted(signatures.dispatch_ins_for_args("SaveAs3", 5))      # [3, 4]
```

You never need this to make a call — `com.call_out` reads it for you — but it
is there when you want to know why a call behaves as it does.

---

## 19. Units

The API works in **metres and radians, always**, whatever the document's own
units are set to. Everything in `swcomapi.api` converts; `swcomapi.com` does
not.

```python
from swcomapi import units

units.mm(60)            # 0.06
units.to_mm(0.06)       # 60.0
units.deg(45)           # 0.7853981633974483
units.to_deg(0.785...)  # 45.0
units.inch(1)           # 0.0254
units.to_inch(0.0254)   # 1.0

units.to_mm_all([0.06, 0.04])   # [60.0, 40.0]
units.to_mm2(0.0024)            # 2400.0
units.to_mm3(2.4e-05)           # 24000.0
units.to_g(0.0648)              # 64.8
```

The one exception is [equations](#9-equations), which are strings SOLIDWORKS
parses in the document's own units.

---

## 20. The escape hatch

Every wrapper exposes the raw COM object as `.com`, so nothing in the API is
out of reach for want of a wrapper:

```python
type(part.com).__name__         # 'CDispatch'
part.com.FeatureManager.InsertDeleteBody2(True)
```

The raw layer takes the sharp edges off without getting in the way:

```python
swc.com.call(part.com, "GetTitle")          # 'plate.SLDPRT'

result, out = swc.com.call_out(app.com, "GetBuildNumbers2")
# (None, {'BaseVersion': 'sw2026_SP03', 'CurrentVersion': 'd260519.003',
#         'HotFixes': ' - Hotfix: #HF-1530816 ...'})
```

| function | what it does |
|---|---|
| `com.call(obj, name, *args)` | call or read, with the errors translated |
| `com.call_out(obj, name, *args)` | the same, plus the `[out]` parameters |
| `com.set_property(obj, name, value)` | write a property |
| `com.set_property_at(obj, name, value, *index)` | write an indexed property |
| `com.nothing()` | VBA's `Nothing`, for an unused `IDispatch*` |
| `com.byref(vt)` | one `[out]` holder, by hand |
| `com.to_list(value)` | a SafeArray as a list; `None` becomes `[]` |
| `com.to_tuples(value, 3)` | the same, grouped |
| `com.from_list(values)` | a SafeArray to pass in |

Four things `com.call` gets right that a straight `getattr` does not:

1. **`[out]` parameters** are built, slotted into their real positions and read
   back — including the ones in the middle of the argument list.
2. **`None` becomes a null `VT_DISPATCH`** wherever the generated table says a
   parameter wants an object. A bare `None` arrives as `VT_EMPTY` and
   SOLIDWORKS answers "Type mismatch" without naming the parameter.
3. **Zero-argument members** are handled either way. Late binding sometimes
   hands back the answer and sometimes hands back a method still waiting to be
   called, and the difference is not something you can predict. Deciding with
   `callable()` looks right and is wrong — a `CDispatch` is callable, so
   `doc.Extension()` gets attempted and fails with "Member not found".
4. **Errors** come out as the classes in `swcomapi.errors`, with the original
   `com_error` kept in `__cause__`.

---

## 21. Errors

```
SwError
├── SwUnavailableError        pywin32 is not installed
├── SwConnectionError         could not reach SOLIDWORKS
│   └── SwNotRunningError     nothing is running to attach to
├── SwBusyError               it is busy, and rejected the call
├── SwCallError               a call failed
│   ├── SwMemberNotFoundError also an AttributeError
│   └── SwAmbiguousMemberError
└── SwDocumentError           open, save or export failed
```

In practice:

```python
app.open("nothing.SLDPRT")
# FileNotFoundError: C:\work\nothing.SLDPRT

part.export("plate.nonsense")
# SwDocumentError: saving C:\work\plate.nonsense failed:
# swFileSaveAsInvalidFileExtension

swc.com.call(part.com, "NoSuchMember")
# SwMemberNotFoundError: the COM object has no member 'NoSuchMember'

part.material = "Unobtainium"
# SwCallError: 'Unobtainium' was not applied; the part now has 6061 Alloy...
```

`SwMemberNotFoundError` is also an `AttributeError`, so code that expects one
from `getattr` keeps working. `SwDocumentError` carries `.path`, `.errors`,
`.warnings` and `.names`, so a script can act on the code as well as print it.

---

## 22. What this package does not do

- **Design tables.** That is
  [`swdesigntables`](https://github.com/ivanperezdesigner/swdesigntables),
  which builds them without SOLIDWORKS running. The two work together:
  generate the table there, insert it here.
- **Anything on macOS or Linux.** SOLIDWORKS is Windows-only and so is COM.
  The enumerations, the signature table and the documentation links are plain
  data and import anywhere; everything that connects does not.
- **Pin a SOLIDWORKS version.** Late binding all the way through, never
  `gencache.EnsureDispatch`. A method your release does not have fails with a
  clear error rather than at import time.
- **Hide the API.** Every wrapper is a thin layer over calls you could make
  yourself, and `.com` is always there. The wrapper exists to remove the
  traps, not to replace the API.

### Not wrapped yet

Reachable through `.com`, with `swc.find` and `swc.describe` for the
signature, but without the unit conversion and the selection marks done for
you:

- the Hole Wizard, threads, and every hole that is not a plain round one
- draft, rib, dome, wrap, combine, split, move/copy body, scale
- surfacing and weldments
- sketch trim and extend, sketch patterns, slots, polygons, text
- mates beyond the eight named ones — width, cam, gear, slot, path, screw —
  which `mates.add(first, second, kind)` still reaches by name or number
- exploded views, configurations of a mate
- geometric tolerances, datums, surface finish and weld symbols on a drawing
- appearances, colours, layers and camera views
- PDM

The pattern for all of them is the same as the code here: find the member,
read what it wants, pass metres and radians. If one of them turns into
everyday work, it belongs in the package instead.
