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

[Unreleased]: https://github.com/ivanperezdesigner/swcomapi/compare/main...HEAD
