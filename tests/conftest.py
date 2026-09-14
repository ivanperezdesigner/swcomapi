"""Shared fixtures.

The suite is split in two:

* everything in `tests/` runs anywhere, with no SOLIDWORKS involved
* everything in `tests/live/` is marked `live` and talks to a real one

The live tests are skipped unless SWCOMAPI_LIVE=1 is set, so a plain
`pytest` never launches a CAD application by surprise.
"""

import os

import pytest

LIVE_ENV = "SWCOMAPI_LIVE"


def pytest_collection_modifyitems(config, items):
    if os.environ.get(LIVE_ENV) == "1":
        return
    skip = pytest.mark.skip(reason=f"needs a real SOLIDWORKS; set {LIVE_ENV}=1 to run")
    for item in items:
        if "live" in item.keywords:
            item.add_marker(skip)
