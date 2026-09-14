# Changelog

All notable changes to this project are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the project follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

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

[Unreleased]: https://github.com/ivanperezdesigner/swcomapi/compare/main...HEAD
