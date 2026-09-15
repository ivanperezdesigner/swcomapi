"""Getting hold of SOLIDWORKS: the session entry points.

Three ways in, because they answer three different questions:

``attach()``
    Use the session that is already open. Raises if there is none. This is what
    you want while developing: the model is on screen, you run the script, you
    watch what it does.
``launch()``
    Start a fresh process and use that. For batch work, where there must be no
    doubt about which documents are open.
``connect()``
    Attach if a session is open, start one otherwise. The convenient default.

The module is ``session`` rather than ``connect`` on purpose: a submodule named
``connect`` would shadow the ``connect`` function on the package, so
``swcomapi.connect`` would hand you a module instead of something callable.

The wait that matters
---------------------

A freshly started SOLIDWORKS registers itself with COM long before it can
answer. Calls made in that window fail with ``RPC_E_CALL_REJECTED``
(0x80010001), "Call was rejected by callee" - which reads like a bug and is
not. The same thing happens any time a modal dialog is open on screen.

So every entry point here polls a harmless property until the application
answers, and reports a clear ``SwBusyError`` if it never does. Starting
SOLIDWORKS 2026 cold takes well over a minute on a normal machine, which is
why ``timeout`` defaults to 180 seconds.
"""

import time

from . import com
from .errors import SwBusyError, SwConnectionError, SwNotRunningError

PROGID = "SldWorks.Application"

# Long enough for a cold start of SOLIDWORKS 2026 on a normal machine.
DEFAULT_TIMEOUT = 180.0

# How often to re-ask while the application is still refusing calls.
POLL_INTERVAL = 0.5


def attach(visible=None, timeout=DEFAULT_TIMEOUT):
    """Use the SOLIDWORKS session that is already open.

    visible
        True or False forces the window state; None leaves it alone, which is
        what you want when attaching to a session a human is working in
    timeout
        seconds to keep retrying while the application refuses calls

    Returns a `swcomapi.api.app.SolidWorks`.
    Raises `SwNotRunningError` if no session is open.

    Example::

        >>> app = attach()                      # doctest: +SKIP
        >>> app.version                         # doctest: +SKIP
        'SOLIDWORKS 2026 SP3 (34.3.0)'
    """
    try:
        raw = com.active_object(PROGID)
    except Exception as exc:  # pywintypes.com_error, but keep the import local
        if com.pythoncom is not None and isinstance(exc, com.pythoncom.com_error):
            raise SwNotRunningError(
                "No SOLIDWORKS session is running. Open SOLIDWORKS, or use "
                "connect() to have one started."
            ) from exc
        raise
    return _finish(raw, visible, timeout)


def launch(visible=True, timeout=DEFAULT_TIMEOUT):
    """Start a new SOLIDWORKS process and use that.

    visible
        False starts it hidden, which is what batch jobs want. Note that a
        hidden SOLIDWORKS still shows modal dialogs, and a modal dialog with
        no visible window is a hung script: suppress them with the document
        options rather than by hiding the application.
    timeout
        seconds to keep retrying while the application is still loading

    Returns a `swcomapi.api.app.SolidWorks`.
    """
    raw = com.dispatch(PROGID, new_instance=True)
    return _finish(raw, visible, timeout)


def connect(visible=True, timeout=DEFAULT_TIMEOUT):
    """Attach to a running SOLIDWORKS, or start one if none is running.

    visible
        applied either way; True is the sane default for interactive work
    timeout
        seconds to keep retrying while the application refuses calls

    Returns a `swcomapi.api.app.SolidWorks`.

    Example::

        >>> import swcomapi as swc                      # doctest: +SKIP
        >>> app = swc.connect()                         # doctest: +SKIP
        >>> app.year                                    # doctest: +SKIP
        2026
    """
    try:
        return attach(visible=visible, timeout=timeout)
    except SwNotRunningError:
        pass

    # Plain Dispatch, not DispatchEx: SOLIDWORKS is a singleton server, so if
    # one appeared between the attach and now, COM hands that one back rather
    # than starting a second.
    raw = com.dispatch(PROGID)
    return _finish(raw, visible, timeout)


def _finish(raw, visible, timeout):
    """Wait until `raw` answers, set its window state, and wrap it."""
    from .api.app import SolidWorks

    wait_until_ready(raw, timeout=timeout)
    app = SolidWorks(raw)
    if visible is not None:
        app.visible = visible
    return app


def wait_until_ready(raw, timeout=DEFAULT_TIMEOUT, probe="RevisionNumber"):
    """Poll a harmless property until SOLIDWORKS answers.

    raw
        the COM object
    timeout
        seconds to keep trying, as a float
    probe
        the property to read; ``RevisionNumber`` is a plain string read with no
        side effects whatsoever, which is exactly what a probe should be

    Returns the probe's value. Raises `SwBusyError` on timeout.

    Only "busy" HRESULTs are retried. Anything else is a real failure and is
    raised straight away, so a genuine problem does not hide behind a long
    wait.
    """
    if com.pythoncom is None:  # pragma: no cover - only reachable off Windows
        com._require_pywin32()

    deadline = time.monotonic() + timeout
    attempts = 0
    while True:
        attempts += 1
        try:
            return getattr(raw, probe)
        except com.pythoncom.com_error as exc:
            if not com.is_busy(exc):
                raise SwConnectionError(
                    f"SOLIDWORKS refused to answer {probe!r}: {exc}"
                ) from exc
            if time.monotonic() >= deadline:
                raise SwBusyError(
                    f"SOLIDWORKS kept rejecting calls for {timeout:g} s "
                    f"({attempts} attempts). It is either still loading, or a "
                    f"modal dialog is open on screen and needs closing."
                ) from exc
            time.sleep(POLL_INTERVAL)
