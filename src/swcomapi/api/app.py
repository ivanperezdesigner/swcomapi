"""The application object: ``ISldWorks``.

This is the root of everything. You get one from `swcomapi.connect`, and every
document, every setting and every command hangs off it.

Phase 1 covers identity and window state - what you need to prove a connection
works. Opening, creating and closing documents arrive with `document.py`.

The raw ``ISldWorks`` is always on ``.com``, so anything not wrapped yet is
still one attribute away::

    app.com.SendMsgToUser2("hello", 0, 0)
"""

import re

from .. import com


class SolidWorks:
    """A connected SOLIDWORKS application.

    Do not build this directly; use `swcomapi.connect`, `swcomapi.attach` or
    `swcomapi.launch`, which handle the wait for the application to become
    responsive.

    Attributes:
        com  the raw ``ISldWorks`` COM object
    """

    def __init__(self, raw):
        self.com = raw

    # ------------------------------------------------------------- identity

    @property
    def revision_number(self):
        """The internal version string, as a str, e.g. ``'34.3.0'``.

        The cheapest version fact there is: a plain property read. The leading
        number is the internal major version, and it is what `year` is derived
        from.
        """
        return com.call(self.com, "RevisionNumber")

    @property
    def year(self):
        """The release year, as an int, e.g. ``2026``.

        Derived, not reported. SOLIDWORKS numbers its releases internally from
        28 for 2020 onwards - 28, 29, 30... - so the year is the major version
        plus 1992. Returns None if the build string cannot be read that way,
        rather than guessing.

        Examples::

            >>> _year_from_revision('34.3.0')
            2026
            >>> _year_from_revision('28.0.0')
            2020
            >>> _year_from_revision('') is None
            True
        """
        return _year_from_revision(self.revision_number)

    @property
    def build_numbers(self):
        """The three build strings, as a list of str.

        ``ISldWorks.GetBuildNumbers2`` takes no arguments in the useful sense:
        all three of its parameters are ``[out]`` BSTRs, and the method itself
        returns nothing. Calling it the way it reads in the documentation
        raises "Type mismatch" - which is exactly the trap `swcomapi.com.out`
        exists to remove.

        The order is base version, current version, hot fixes::

            ['sw2026_SP03',
             'd260519.003',
             ' - Hotfix: #HF-1530816 #HF-1531787 ...']
        """
        _, outs = com.call_out(
            self.com,
            "GetBuildNumbers2",
            com.out(com.VT_BSTR),
            com.out(com.VT_BSTR),
            com.out(com.VT_BSTR),
        )
        return outs

    @property
    def service_pack(self):
        """The service pack number, as an int, or None.

        Parsed out of the base version string, which is the only place
        SOLIDWORKS states it: ``'sw2026_SP03'`` means SP3.

        Examples::

            >>> _service_pack_from_build('sw2026_SP03')
            3
            >>> _service_pack_from_build('sw2025_SP0')
            0
            >>> _service_pack_from_build('something else') is None
            True
        """
        return _service_pack_from_build(self.build_numbers[0])

    @property
    def version(self):
        """A readable one-liner, as a str.

        Costs one extra COM call over `revision_number`, because the service
        pack only exists inside the build strings.

        Examples::

            >>> _version_string(2026, 3, '34.3.0')
            'SOLIDWORKS 2026 SP3 (34.3.0)'
            >>> _version_string(2026, None, '34.3.0')
            'SOLIDWORKS 2026 (34.3.0)'
            >>> _version_string(None, None, 'weird')
            'SOLIDWORKS (weird)'
        """
        revision = self.revision_number
        try:
            service_pack = self.service_pack
        except Exception:
            # An old build, or a hidden application that will not answer.
            # The year alone is still worth reporting.
            service_pack = None
        return _version_string(_year_from_revision(revision), service_pack, revision)

    @property
    def process_id(self):
        """The Windows process id of this SOLIDWORKS, as an int.

        Useful when you launched it yourself and may need to kill it, and to
        prove that `launch()` really did start a second process.
        """
        return com.call(self.com, "GetProcessID")

    # --------------------------------------------------------- window state

    @property
    def visible(self):
        """Whether the SOLIDWORKS window is shown, as a bool."""
        return bool(com.call(self.com, "Visible"))

    @visible.setter
    def visible(self, value):
        self.com.Visible = bool(value)

    # ------------------------------------------------------------- plumbing

    def __repr__(self):
        try:
            return f"<SolidWorks {self.version}>"
        except Exception:
            # A dead or busy connection must not make repr() explode; that
            # would break every debugger and traceback that touches it.
            return "<SolidWorks (not responding)>"


def _year_from_revision(revision):
    """The release year from a build string, or None.

    Kept as a module-level function so it can be tested and doctested without
    a live SOLIDWORKS.
    """
    if not revision:
        return None
    head = str(revision).split(".", 1)[0]
    try:
        major = int(head)
    except ValueError:
        return None
    if major < 28:
        # Before 2020 the numbering does not follow this rule; say nothing
        # rather than report a wrong year.
        return None
    return major + 1992


def _service_pack_from_build(base_version):
    """The service pack number out of a base version string, or None.

    The string looks like ``'sw2026_SP03'``. Anything else gives None rather
    than a guess.
    """
    if not base_version:
        return None
    match = re.search(r"_SP(\d+)", str(base_version))
    return int(match.group(1)) if match else None


def _version_string(year, service_pack, revision):
    """Assemble the readable version line."""
    name = f"SOLIDWORKS {year}" if year else "SOLIDWORKS"
    if service_pack is not None:
        name = f"{name} SP{service_pack}"
    return f"{name} ({revision})" if revision else name
