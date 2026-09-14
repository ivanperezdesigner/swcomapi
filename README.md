# swcomapi

Drive SOLIDWORKS from Python over its COM API — with the enums it never gave
you, and a pythonic layer over the calls you actually make.

> **Status: alpha, under construction.** Nothing is published to PyPI yet.
> Done so far: the COM core, and the generated enumerations.

```bash
pip install swcomapi     # not yet available
```

Windows only, and it needs SOLIDWORKS installed to *connect*. The enums, the
signature table and the documentation links are plain data and import anywhere.

## Why

Talking to SOLIDWORKS from Python with bare `win32com` hurts in three specific
places:

1. **The enums do not exist.** The API has around a thousand enumerations. In
   VBA they are global names; in Python you end up writing the bare integer —
   `OpenDoc6(path, 1, 0, "", 0, 0)` — and a wrong one fails silently.
2. **The `[out]` parameters.** Many methods return data by reference. With late
   binding you have to build `VARIANT(pythoncom.VT_BYREF | VT_I4, 0)` by hand
   and know the exact type of each one.
3. **Nothing tells you what exists.** No autocompletion, no signatures.

`swcomapi` reads the type libraries shipped with your SOLIDWORKS install and
generates the whole surface — every interface, every method signature, every
enum — then puts a hand-written, documented layer on top of the parts you use
every day.

Nothing is ever out of reach: every wrapper object exposes the raw COM object
as `.com`.

## Documentation

- Reference and runnable examples: `DOCUMENTATION.md`
- Changes: `CHANGELOG.md`

## Related

- [swdesigntables](https://github.com/ivanperezdesigner/swdesigntables) — builds
  SOLIDWORKS design tables without touching SOLIDWORKS. The two work together:
  generate the table with `swdesigntables`, insert it with `swcomapi`.

## Licence

MIT.
