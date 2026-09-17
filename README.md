# swcomapi

Drive SOLIDWORKS from Python over its COM API — with the enumerations it never
gave you, the `[out]` parameters handled, and a pythonic layer over the calls
you actually make.

> **Status: 0.2.0.** Generated against SOLIDWORKS 2026 SP3 and tested against
> it: 511 tests that need no SOLIDWORKS, plus 170 that do - 37 feature tests
> and 129 docstrings executed against a live session. Every worked example in
> the documentation is one of those tests.

```bash
pip install swcomapi
```

Windows only, and it needs SOLIDWORKS installed to *connect*. The
enumerations, the signature table and the documentation links are plain data
and import anywhere.

```python
import swcomapi as swc

app = swc.connect()

with app.open("bracket.SLDPRT") as part:
    part.configuration = "BRK-040"
    part.dimensions["Length@Boss-Extrude1"] = 55        # mm
    part.properties["Revision"] = "B"
    part.rebuild()
    print(f"{part.mass:.1f} g of {part.material}")      # 187.2 g of 6061 Alloy
    part.export("BRK-040.step")
```

`swc`, not `sw`:
[`swdesigntables`](https://github.com/ivanperezdesigner/swdesigntables) already
answers to that, and the two are meant to be used together.

## Why

Talking to SOLIDWORKS from Python with bare `win32com` hurts in four specific
places.

**1. The enumerations do not exist.** The API has 1,434 of them and 14,889
constants. In VBA they are global names; in Python you end up writing the bare
integer — `OpenDoc6(path, 1, 0, "", 0, 0)` — and a wrong one fails silently.

```python
from swcomapi import const
const.swDocPART                     # 1
const.swSaveAsCurrentVersion        # 0
```

**2. The `[out]` parameters.** 982 members return data by writing into their
arguments, and with late binding you have to build a `VARIANT(VT_BYREF | vt)`
for each one and know its exact type. This package generates that table from
the type libraries of your own install and fills them in:

```python
doc, out = swc.com.call_out(app.com, "OpenDoc6", path, 1, 0, "")
out["Errors"], out["Warnings"]      # 0, 0
```

**3. Nothing tells you what exists.** No autocompletion, no signatures, and
`help.solidworks.com` returns `403` to anything that is not a browser.

```python
swc.find("GetMassProperties")                   # 20 members match
print(swc.describe("IModelDocExtension.SaveAs3"))
swc.doclink("IModelDoc2")                       # the official page
```

**4. The traps.** Things that fail silently, and that this package has each
been bitten by and fixed:

| what | what happens without it |
|---|---|
| `None` for an unused `IDispatch*` | "Type mismatch", naming no parameter |
| a plain `"Front"` view name | no view, no error |
| a tuple where a SafeArray is wanted | the call succeeds and does the wrong thing |
| `IDimension.SystemValue` | writes every configuration at once |
| `GetMassProperties2` on a part | status -1 and no values, some of the time |
| a global variable called `thickness` | refused; it is reserved for sheet metal |
| `run_command` with a command that opens a dialog | every later call blocks, with no error |
| `AddDimension2` with "Input dimension value" on | opens the Modify box and waits for a person |
| `swAddMateError_NoError` | it is **1**, not 0, so `if status:` rejects every mate that worked |
| `InsertMirrorFeature2` with the features on mark 4 | a bare `None`; it wants them on mark 1 |
| `InsertRefPlane` with both references on mark 0 | no plane, for any constraint pair there is |
| a fillet radius that cannot possibly fit | no error: it makes the feature and eats the body |
| `CreateDetailViewAt4` with no scale | refused outright; there is no falling back to the parent |
| `InsertModelAnnotations3` asked for `swInsertDimensions` | no dimensions on the sheet, and the same `None` it answers when it works |
| `InsertBomTable6` on a view of a part | a bare `None`; the view has to be of an assembly |
| `SetSuppression2` | returns True for a change it did not make |
| `GetMassProperties(0.0)` | a density of 1, so mass equals volume |
| `swThisConfiguration` with a name list | reads the active one and ignores the names |

## What is in it

```
swcomapi/
├─ com.py            the raw layer: calls, [out] parameters, SafeArrays
├─ units.py          m/rad <-> mm/deg
├─ session.py        connect / attach / launch
├─ enums.py          1,434 enumerations, lazily built
├─ const.py          the same, flat, the way VBA sees them
├─ signatures.py     which parameters each member writes into
├─ apidoc.py         describe / find / find_interface / summary
├─ doclinks.py       deep links into the official help
├─ api/              the pythonic layer
│  ├─ app.py         SolidWorks
│  ├─ document.py    Document, Part, Assembly, Drawing
│  ├─ sketch.py      sketching, dimensioning, relating
│  ├─ modeling.py    extrude, cut, revolve, sweep, loft, fillet, chamfer,
│  │                 shell, hole
│  ├─ patterns.py    linear, circular, mirror
│  ├─ reference.py   reference planes and axes
│  ├─ selection.py   what a feature call works from, marks and all
│  ├─ geometry.py    bodies, faces, edges, vertices
│  ├─ features.py    the tree, and suppression
│  ├─ dimensions.py  in mm and degrees, per configuration
│  ├─ properties.py  custom properties, as a mapping
│  ├─ configurations.py
│  ├─ equations.py   equations and global variables
│  ├─ materials.py   read and apply a material
│  ├─ sheetmetal.py  thickness, bend radius, K-factor
│  ├─ components.py  the components of an assembly, and moving them
│  ├─ mates.py       what holds an assembly together
│  ├─ drawing.py     sheets, views, sections, details, notes, parts list
│  └─ export.py      pdf, step, dxf, stl, and the error codes decoded
└─ tools/            the generator: type libraries -> generated/
```

Nothing is ever out of reach: every wrapper object exposes the raw COM object
as `.com`.

```python
part.com.FeatureManager.InsertDeleteBody2(True)
```

## Modelling

The pythonic layer builds geometry as well as reading it. Everything in
millimetres and degrees; the API's metres and radians never reach you.

```python
import swcomapi as swc

app = swc.connect()
part = app.new_part()

with part.sketch_on("Front Plane") as sketch:
    sides = sketch.rectangle((0, 0), (50, 25))
    sketch.dimension(sides[0], at=(25, -12), value=60, name="width")
    sketch.dimension(sides[1], at=(-12, 12), value=30, name="height")

part.extrude(10)
part.chamfer(2, edges=part.bodies[0].edges)
part.hole(6, at=(15, 10, 10), through_all=True)

along = max(part.bodies[0].edges, key=lambda edge: edge.length)
part.patterns.linear("Hole1", along, count=3, spacing=15)
```

An assembly is components and mates:

```python
assembly = app.new_assembly()
assembly.components.add("rail.SLDPRT", at=(0, 0, 0))
assembly.components.add("gusset.SLDPRT", at=(150, 0, 0))

rail, gusset = assembly.components.in_order()
assembly.mates.coincident(rail.plane("Top Plane"), gusset.plane("Top Plane"))
assembly.mates.distance(rail.plane("Right Plane"),
                        gusset.plane("Right Plane"), 80)

assembly.interferences()            # []
```

And a drawing is sheets, views and annotations:

```python
drawing = app.new_drawing()
front = drawing.views.add("rail.SLDPRT", "Front", at=(100, 100))
front.insert_dimensions()

drawing.views.add_section(front, through=((100, 60), (100, 140)), at=(220, 100))
drawing.views.add_detail(front, centre=(100, 100), radius=12, at=(260, 160))
front.add_note("BREAK ALL EDGES 0.5", at=(20, 20))

drawing.export("rail.pdf")
```

What is not wrapped - the Hole Wizard, weldments, surfacing, configurations of
a mate - is still reachable through `.com`, and
[`docs/reference/cheatsheet.md`](docs/reference/cheatsheet.md) lists
everything that is.

## Documentation

- **[`DOCUMENTATION.md`](DOCUMENTATION.md)** — the reference, with every
  example run against a real SOLIDWORKS and its real output beside it.
- **[`docs/reference/cheatsheet.md`](docs/reference/cheatsheet.md)** — every
  call in the pythonic layer on one page, generated from the package itself.
- **[`docs/reference/enums.md`](docs/reference/enums.md)** — all 1,434
  enumerations with links to the official pages.
- **[`examples/`](examples/)** — six runnable scripts, from connecting to
  building an assembly and a drawing.
- **[`CHANGELOG.md`](CHANGELOG.md)** — what changed.

## Running the tests

```bash
.venv\Scripts\python -m pytest tests -m "not live"   # no SOLIDWORKS needed
.venv\Scripts\python -m ruff check src tests
.venv\Scripts\python -m mypy
```

With SOLIDWORKS on the machine, the live suite builds its own geometry and
cleans up after itself:

```bash
set SWCOMAPI_LIVE=1
.venv\Scripts\python -m pytest tests -q
```

Expect it to take a while, and expect to restart SOLIDWORKS partway through a
long run. It does not give memory back when a document closes: a fresh session
starts around 190 MB and is several GB after a hundred test parts, at which
point every COM call slows to a crawl. Run the live suite in batches, with a
restart between them, rather than waiting on one invocation.

That includes the documentation. Every worked example in a docstring is run
against a real SOLIDWORKS, on a document built for it, by
`tests/live/test_doctests_live.py` — because an example nothing executes is a
claim nobody checked, and several of them turned out to be wrong.

## Regenerating

The generated files are committed, so the package installs and the
enumerations work on a machine with no SOLIDWORKS. To rebuild them against
another release:

```bash
python -m swcomapi.tools survey       # what is installed, and how big it is
python -m swcomapi.tools generate     # rebuild swcomapi/generated
python -m swcomapi.tools enumdoc      # rebuild docs/reference/enums.md
python -m swcomapi.tools cheatsheet   # rebuild docs/reference/cheatsheet.md
```

Generation is deterministic: running it twice leaves `git status` clean.

## Related

- [swdesigntables](https://github.com/ivanperezdesigner/swdesigntables) —
  builds SOLIDWORKS design tables without touching SOLIDWORKS. The two work
  together: generate the table there, insert it here.

## Licence

MIT.
