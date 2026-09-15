# swcomapi

Drive SOLIDWORKS from Python over its COM API — with the enumerations it never
gave you, the `[out]` parameters handled, and a pythonic layer over the calls
you actually make.

> **Status: 0.1.0, the first release.** Generated against SOLIDWORKS 2026 SP3
> and tested against it, 625 tests with it attached and 447 without.

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
│  ├─ sketch.py      sketching, as a context manager
│  ├─ modeling.py    extrude, cut, revolve
│  ├─ geometry.py    bodies, faces, edges, vertices
│  ├─ features.py    the tree, and suppression
│  ├─ dimensions.py  in mm and degrees, per configuration
│  ├─ properties.py  custom properties, as a mapping
│  ├─ configurations.py
│  ├─ equations.py   equations and global variables
│  ├─ materials.py   read and apply a material
│  ├─ sheetmetal.py  thickness, bend radius, K-factor
│  ├─ components.py  the components of an assembly
│  ├─ drawing.py     sheets and views
│  └─ export.py      pdf, step, dxf, stl, and the error codes decoded
└─ tools/            the generator: type libraries -> generated/
```

Nothing is ever out of reach: every wrapper object exposes the raw COM object
as `.com`.

```python
part.com.FeatureManager.InsertDeleteBody2(True)
```

## Documentation

- **[`DOCUMENTATION.md`](DOCUMENTATION.md)** — the reference, with every
  example run against a real SOLIDWORKS and its real output beside it.
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

## Regenerating

The generated files are committed, so the package installs and the
enumerations work on a machine with no SOLIDWORKS. To rebuild them against
another release:

```bash
python -m swcomapi.tools survey       # what is installed, and how big it is
python -m swcomapi.tools generate     # rebuild swcomapi/generated
python -m swcomapi.tools enumdoc      # rebuild docs/reference/enums.md
```

Generation is deterministic: running it twice leaves `git status` clean.

## Related

- [swdesigntables](https://github.com/ivanperezdesigner/swdesigntables) —
  builds SOLIDWORKS design tables without touching SOLIDWORKS. The two work
  together: generate the table there, insert it here.

## Licence

MIT.
