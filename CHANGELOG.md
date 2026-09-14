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

[Unreleased]: https://github.com/ivanperezdesigner/swcomapi/compare/main...HEAD
