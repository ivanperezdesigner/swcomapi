# Changelog

All notable changes to this project are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the project follows [Semantic Versioning](https://semver.org/).

## [0.2.0] - 2026-09-15

The release that makes the package do the everyday work. Up to 0.1.1 the
pythonic layer could read and edit a document that already existed, and could
extrude, cut and revolve. Everything else - rounding an edge, patterning a
hole, mating a component, cutting a section on a drawing - meant dropping to
raw COM and remembering that the API is metres and radians. It does not any
more.

### Added

Solid features, in `swcomapi.api.modeling`:
- `fillet` and `chamfer`, on edges, faces or whatever is selected. Distances
  in mm, angles in degrees, and a chamfer takes either an angle or a second
  distance.
- `shell`, opening the faces you name.
- `hole`, the plain round one, at a point on a face.
- `sweep` and `loft`, which take their profiles by name and mark them for you.

Repeats, in the new `swcomapi.api.patterns`:
- `linear`, `circular` and `mirror`, reached as `part.patterns.linear(...)`
  and `part.mirror(...)`. `count` is the total number of instances, the way
  the dialog means it.

Reference geometry, in the new `swcomapi.api.reference`:
- `plane` - parallel at a distance, angled, midway between two things, or
  through three points - and `axis`. Both reached as `part.plane(...)` and
  `part.axis(...)`.

Sketches that hold their shape, on `SketchSession`:
- `dimension`, which adds a driving dimension, names it if you ask, and
  returns the name `part.dimensions` wants.
- `relate`, for the fifteen everyday relations by their English names.
- `offset` and `mirror`.

Assemblies, in the new `swcomapi.api.mates`:
- `assembly.mates` reads the mates and adds them: `coincident`, `concentric`,
  `distance`, `parallel`, `perpendicular`, `tangent`, `angle` and `lock`, plus
  `add` for the rest by name or number.
- `Component.body`, `.faces`, `.edges` and `.plane(name)` - the geometry of
  the *instance*, which is the half of mating that is easy to get wrong: a
  face read from `component.document` belongs to the part file and cannot be
  mated.
- `Component.move`, and `Component.fixed` is now settable.
- `Components.in_order()`, because `GetComponents` does not answer in
  insertion order, or twice in the same order.
- `Assembly.interferences()`, the interference check run headless.

Drawings, in `swcomapi.api.drawing`:
- `views.add_section` and `views.add_detail`, which draw the section line or
  the detail circle for you - there is no way to hand either to the API as an
  argument.
- `view.insert_dimensions`, `view.add_note`, `view.add_balloons` and
  `view.add_bom`.

And underneath all of it, the new `swcomapi.api.selection`:
- `select` and `select_all` take a wrapper, a raw COM object, a `(name, kind)`
  pair or a bare name, and file it under the mark the call expects. The marks
  are documented in one table there, which is more than they are anywhere
  else: a linear pattern reads its direction from mark 1 and its features from
  mark 4, and a mark in the wrong place does not fail - it makes a feature
  that is quietly wrong.

### Fixed, before anyone saw it

All six found by running the new code against SOLIDWORKS 2026 SP3 rather than
by reading the documentation, which says none of it.

- `AddDimension2` obeys Tools > Options > General > "Input dimension value",
  which is on by default. With it on, the call opens the Modify box and waits
  for a person — and a dialog blocks every COM call in the session, with no
  error and no timeout. `SketchSession.dimension` turns the option off for
  the length of the call and puts it back. It cost this release two hung runs
  before it was understood.
- `swAddMateError_NoError` is **1**, and `swAddMateError_ErrorUknown`
  (Dassault's spelling) is **0** — backwards from every other status in the
  API. The obvious `if status:` rejects every mate that worked.
- `InsertMirrorFeature2` reads the features to mirror from mark 1. Every
  other pattern call in the API reads what to repeat from mark 4, and with
  mark 4 this one answers a bare `None`.
- `InsertRefPlane` gives each reference its own mark — 0, then 1, then 2.
  With both references on mark 0, which is what selecting two things normally
  gives you, no constraint pair in `swRefPlaneReferenceConstraints_e` makes a
  plane at all.
- `CreateDetailViewAt4` refuses a zero scale outright instead of falling back
  to the parent view's; a detail view with no scale given now asks for 2:1.
- `GetTypeName2` on a loft answers `'Blend'`, the name the call had before
  the interface renamed it, so `features.of_type("Loft")` finds nothing. The
  docstring said `'Loft'`.
- A fillet whose radius cannot possibly fit does not fail. SOLIDWORKS makes
  the feature, reports success, and lets it eat the model — 200 mm on one
  edge of a 60 by 40 by 10 plate leaves a 2,156 mm3 sliver with five faces.
  The docstring promised the opposite; now it says what happens.

### Changed
- `Document.select` takes a pick point, so a face can be selected where the
  mouse would be rather than by name.
- The cheat sheet covers 257 calls across 19 modules, up from 207 across 15.

## [0.1.1] - 2026-09-15

The documentation started being executed, and it turned out to be making
claims. Every worked example in a docstring now runs against a real
SOLIDWORKS, which is how the fixes below were found.

### Added
- `docs/reference/cheatsheet.md` — every call in the pythonic layer on one
  page, with its signature and what it does. Generated from the installed
  package by `python -m swcomapi.tools cheatsheet`, so it cannot drift from
  the code, and checked against the committed copy by the test suite.
- `tests/live/test_doctests_live.py` — runs the docstring examples that need
  SOLIDWORKS, by stripping their `+SKIP` flag and building each docstring its
  own plate, assembly or drawing. 89 docstrings, and it closes what it opens.
- 170 executable examples, up from 57. The reStructuredText literal blocks
  that nothing could run are doctests now.

### Fixed
- `Part.mass` and the rest of `mass_properties` raised for a perfectly solid
  part. `IModelDocExtension.GetMassProperties2` answers status -1 and no
  values depending on the state of the session — Dassault describe it as
  getting "mass properties of selected assembly components", a call meant for
  assemblies. `IBody2` always answers, so the bodies are asked instead and
  added up when the document declines.
- `del part.equations["width"]` works. It took a name everywhere except
  `__delitem__`, where it reached `int()` and raised ValueError.
- `equations.add()` names the cause it was missing: a name SOLIDWORKS keeps
  for itself. `"thickness"` drives sheet metal and is refused, reported as
  -1 with no reason, which looks like a broken install.
- The `cut` examples in `modeling` and `document` sketched on the Front Plane
  and cut towards the viewer, removing nothing. They cut into the material
  now, and both modules say which way a cut goes.
- `run_command` warns that a command which opens a dialog blocks every COM
  call until somebody answers it. Its own example used to be `Save`.
- Examples that claimed a face can be selected by the name of the feature
  that made it, that `RevisionNumber` is a method, that a part exports to
  DXF, that a cut is an `Extrusion`, that `GetComponents` answers in
  insertion order, and that `components.add` puts a component's origin where
  you asked rather than centring its bounding box.
- The stale comment in `modeling` claiming `SketchSession` clears the
  selection on the way out, which it deliberately does not.

### Changed
- The GitHub Actions are on their current majors, off the deprecated Node 20.

## [0.1.0] - 2026-09-15

First release. Generated against SOLIDWORKS 2026 SP3; late binding, so it
is not tied to that release.

### Added
- Project scaffolding: packaging, CI, licence.
- `swcomapi.errors` — one exception tree under `SwError`. `SwMemberNotFoundError`
  also derives from `AttributeError`, so `hasattr` keeps working.
- `swcomapi.units` — metres and radians in, millimetres and degrees out. The API
  is always metric and always radians, whatever the document's own units say.
- `swcomapi.com` — the raw layer: `dispatch`, `out`/`call`/`call_out` for the
  `[out]` parameters, `to_list`/`to_tuples`/`from_list` for the SafeArrays, and
  translation of `pywintypes.com_error` into readable exceptions.
- `swcomapi.session` — `attach`, `launch`, `connect`, and the retry loop that
  waits out the `RPC_E_CALL_REJECTED` a loading SOLIDWORKS answers with.
- `swcomapi.api.app.SolidWorks` — identity and window state, with the raw
  `ISldWorks` on `.com`.
- `examples/01_connect.py`.
- `swcomapi.tools.install` - finds SOLIDWORKS through its COM registration,
  since the install directory moved between 2025 and 2026.
- `swcomapi.tools.tlb` - reads a type library into plain data: every interface,
  member, parameter direction and enumeration, plus the vendor's own one-line
  descriptions. 86% of members carry one, and the official pages are behind an
  Akamai rule that refuses non-browser clients, so this is the documentation.
- `swcomapi.tools.generate` and `python -m swcomapi.tools {survey,generate}`.
  Output is deterministic: no timestamps, no paths, everything sorted.
- `swcomapi.enums` - all 1,434 enumerations as real `IntEnum` classes, built on
  demand. Measured: 1,434 eager classes cost ~158 ms to import, the data plus
  on-demand building costs ~8 ms.
- `swcomapi.const` - all 14,889 constants as bare names, the way VBA sees them.
  Safe because every name is distinct across every enumeration; the generator
  refuses to emit if that ever stops being true.
- `swcomapi/enums.pyi` and `swcomapi/const.pyi` - generated stubs, so the
  editor and mypy see every name without paying for it at runtime.
- `swcomapi.signatures` and the generated `OUT_PARAMS` table - which parameters
  each of 982 members writes into, so `com.call_out` can fill them in. Keyed by
  name because there is no way to ask a live SOLIDWORKS object what interface
  it implements: `IDispatch.GetTypeInfo` raises on every one of them.
- The generated `DISPATCH_IN` table and `com.nothing()` - 977 members take an
  `[in]` parameter that wants a COM object. `None` for one of those reaches
  SOLIDWORKS as `VT_EMPTY` and the call fails with "Type mismatch" naming no
  parameter; `com.call` converts it to the null `VT_DISPATCH` that VBA spells
  `Nothing`.
- `swcomapi.apidoc` - `describe`, `find`, `find_interface` and `summary` over a
  gzipped index of 729 interfaces and 19,874 members, 17,097 of them carrying
  the vendor's own description.
- `swcomapi.doclinks` - deep links into the official help, built rather than
  fetched, so they cost nothing and work offline.
- `com.set_property` and `com.set_property_at` - a property put is not a
  property read, and an indexed property put is a third thing again, which
  Python has no syntax for.
- The pythonic layer: `api.app`, `api.document`, `api.sketch`, `api.modeling`,
  `api.geometry`, `api.features`, `api.dimensions`, `api.properties`,
  `api.configurations`, `api.equations`, `api.materials`, `api.sheetmetal`,
  `api.components`, `api.drawing` and `api.export`. Everything in millimetres
  and degrees, with the raw object on `.com`.
- `DOCUMENTATION.md`, `docs/reference/enums.md` and six runnable examples.
- `python -m swcomapi.tools enumdoc`.

### Fixed
- `Feature.suppress` and `.unsuppress` read the state back. `SetSuppression2`
  returns True for a change it did not make when a configuration table owns the
  feature's state.
- A dimension write goes to the active configuration only.
  `IDimension.SystemValue` writes the value into every configuration at once,
  so a loop over configurations left them all at the last value.
- `Dimensions.value_in` and `.set_in` pass the configuration names as a
  SafeArray. Handed a Python list, `GetSystemValue3` answers None and
  `SetSystemValue3` writes nothing, neither of them complaining.
- `Properties.get` distinguishes a property that is absent from one that is
  present and empty. `Get6` reports both the same way through its `[out]`
  parameters; only its return code tells them apart.
- `Part.material` reads the return value of `GetMaterialPropertyName2` rather
  than its `[out]` parameter, which is the database, not the material.
- `Feature.is_furniture` drops every `*Folder` type rather than a list that
  2026 had already outgrown.
- `Body.mass` passes the document's density. `GetMassProperties(0.0)` means a
  density of 1, not "use the material".
- `View.position` sends a SafeArray. A tuple moves the view somewhere else and
  reports success.
- `Views.add` asterisks the standard view names, which is what
  `CreateDrawViewFromModelView3` wants and what makes the difference between a
  view and a silent None.

[0.2.0]: https://github.com/ivanperezdesigner/swcomapi/releases/tag/v0.2.0
[0.1.1]: https://github.com/ivanperezdesigner/swcomapi/releases/tag/v0.1.1
[0.1.0]: https://github.com/ivanperezdesigner/swcomapi/releases/tag/v0.1.0
