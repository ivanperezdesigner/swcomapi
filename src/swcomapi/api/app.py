"""The application object: ``ISldWorks``.

This is the root of everything. You get one from `swcomapi.connect`, and every
document, every setting and every command hangs off it:

    >>> import swcomapi as swc                          # doctest: +SKIP
    >>> app = swc.connect()                             # doctest: +SKIP
    >>> app.version                                     # doctest: +SKIP
    'SOLIDWORKS 2026 SP3 (34.3.0)'
    >>> opened = app.open(path)     # a Part, Assembly or Drawing  # doctest: +SKIP
    >>> opened.kind                                     # doctest: +SKIP
    'part'
    >>> app.active is None              # the one with focus  # doctest: +SKIP
    False

The raw ``ISldWorks`` is always on ``.com``, so anything not wrapped is still
one attribute away:

    >>> app.com.RevisionNumber      # a property, not a method  # doctest: +SKIP
    '34.3.0'

and ``swcomapi.describe("ISldWorks")`` lists all 366 of its members.
"""

import os
import re

from .. import com

# SOLIDWORKS numbers its releases internally from 28 for 2020 onwards, so the
# year is the major version plus 1992. The same number appears in the type
# libraries' version, which is why the generator uses this too.
RELEASE_YEAR_OFFSET = 1992
FIRST_KNOWN_MAJOR = 28


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
        raises "Type mismatch" - which is exactly the trap
        `swcomapi.com.call_out` exists to remove.

        The order is base version, current version, hot fixes:

            >>> app.build_numbers[0]                    # doctest: +SKIP
            'sw2026_SP03'
            >>> len(app.build_numbers)                  # doctest: +SKIP
            3
        """
        _, out = com.call_out(self.com, "GetBuildNumbers2")
        return [out["BaseVersion"], out["CurrentVersion"], out["HotFixes"]]

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

    # ----------------------------------------------------------- documents

    def open(self, path, configuration=None, read_only=False, silent=True, view_only=False):
        """Open a file. Returns a `Part`, `Assembly` or `Drawing`.

        path
            the file to open. A relative path is resolved against the current
            directory, because SOLIDWORKS resolves it against its own and that
            is never what you meant.
        configuration
            open with this configuration active, by name
        read_only
            True opens it without taking the write lock, which is what you
            want when several scripts read the same library part
        silent
            True suppresses the dialogs. Leave it True in a script: a dialog
            with nobody to answer it hangs the call.
        view_only
            True opens it in Large Design Review, which is fast and cannot be
            edited. For reading properties off a big assembly.

        Raises FileNotFoundError if the file is not there - checked here,
        because ``OpenDoc6`` reports a missing file as a generic error code.
        Raises `SwDocumentError` if SOLIDWORKS reports an error, with the
        decoded flag names. Warns `SwWarning` for a warning, since the
        document did open.

        Example:

            >>> opened = app.open(path)                 # doctest: +SKIP
            >>> opened.kind                             # doctest: +SKIP
            'part'
        """
        import os
        import warnings

        from ..const import (
            swOpenDocOptions_ReadOnly,
            swOpenDocOptions_Silent,
            swOpenDocOptions_ViewOnly,
        )
        from ..errors import SwDocumentError, SwWarning
        from .document import wrap
        from .export import load_error_names, load_warning_names

        target = os.path.abspath(path)
        if not os.path.isfile(target):
            raise FileNotFoundError(target)

        options = 0
        if silent:
            options |= swOpenDocOptions_Silent
        if read_only:
            options |= swOpenDocOptions_ReadOnly
        if view_only:
            options |= swOpenDocOptions_ViewOnly

        model, out = com.call_out(
            self.com,
            "OpenDoc6",
            target,
            document_type_of(target),
            options,
            "" if configuration is None else str(configuration),
            interface="ISldWorks",
        )

        errors = out.get("Errors", 0) or 0
        warning_code = out.get("Warnings", 0) or 0
        if errors or model is None:
            names = load_error_names(errors)
            raise SwDocumentError(
                f"could not open {target}"
                + (f": {', '.join(names)}" if names else ""),
                path=target,
                errors=errors,
                warnings=warning_code,
                names=names,
            )
        if warning_code:
            warnings.warn(
                f"opened {target} with warnings: "
                f"{', '.join(load_warning_names(warning_code))}",
                SwWarning,
                stacklevel=2,
            )
        return wrap(model, self)

    def new_part(self, template=None):
        """Create a new part. Returns a `Part`.

        template
            a ``.prtdot`` file; the user's default part template if omitted
        """
        return self._new(template, "part")

    def new_assembly(self, template=None):
        """Create a new assembly. Returns an `Assembly`."""
        return self._new(template, "assembly")

    def new_drawing(self, template=None):
        """Create a new drawing. Returns a `Drawing`."""
        return self._new(template, "drawing")

    def _new(self, template, kind):
        from ..const import (
            swDefaultTemplateAssembly,
            swDefaultTemplateDrawing,
            swDefaultTemplatePart,
        )
        from ..errors import SwDocumentError
        from .document import wrap

        defaults = {
            "part": swDefaultTemplatePart,
            "assembly": swDefaultTemplateAssembly,
            "drawing": swDefaultTemplateDrawing,
        }
        if template is None:
            template = com.call(
                self.com, "GetUserPreferenceStringValue", defaults[kind]
            )
        if not template:
            raise SwDocumentError(
                f"SOLIDWORKS has no default {kind} template configured, so "
                f"there is nothing to create one from. Pass template= with a "
                f"path, or set it in Tools > Options > Default Templates."
            )

        template = str(template)
        if not os.path.isfile(template):
            template = self._template_in_search_path(template, kind)

        model = com.call(self.com, "NewDocument", template, 0, 0.0, 0.0)
        if model is None:
            raise SwDocumentError(
                f"SOLIDWORKS declined to create a {kind} from template "
                f"{template}",
                path=template,
            )
        return wrap(model, self)

    def _template_in_search_path(self, missing, kind):
        """Find ``kind``'s template when the configured path is gone.

        Upgrading SOLIDWORKS leaves the default template settings pointing at
        the old release's folder, and only for the types the user never
        touched: this machine's 2026 install has a part template under
        ``SOLIDWORKS 2026`` and an assembly one still under
        ``SOLIDWORKS 2025``, which no longer exists. ``NewDocument`` answers
        that with a bare None.

        So the file name is looked for in the template folders SOLIDWORKS is
        actually searching. Returns the path found, as a str.

        Raises `SwDocumentError` naming the configured path when there is
        nothing to fall back to, since that is the setting to fix.
        """
        from ..const import swFileLocationsDocumentTemplates
        from ..errors import SwDocumentError

        wanted = os.path.basename(missing).lower()
        folders = com.call(
            self.com, "GetUserPreferenceStringValue", swFileLocationsDocumentTemplates
        )
        for folder in str(folders or "").split(";"):
            folder = folder.strip()
            if not folder or not os.path.isdir(folder):
                continue
            for entry in os.listdir(folder):
                if entry.lower() == wanted:
                    return os.path.join(folder, entry)

        raise SwDocumentError(
            f"the default {kind} template is set to {missing}, which does not "
            f"exist, and no file of that name is in the template folders "
            f"SOLIDWORKS is searching ({folders}). An upgrade leaves this "
            f"behind; fix it in Tools > Options > Default Templates, or pass "
            f"template= with a path.",
            path=missing,
        )

    @property
    def documents(self):
        """Every open document, as a list of `Document` subclasses.

        Example:

            >>> sorted(set(d.kind for d in app.documents))  # doctest: +SKIP
            ['part']
        """
        from .document import wrap

        return [wrap(model, self) for model in com.to_list(com.call(self.com, "GetDocuments"))]

    @property
    def active(self):
        """The document with focus, as a `Document` subclass, or None.

        None when SOLIDWORKS is open with nothing in it, which a script that
        expects to work on "whatever is on screen" has to handle.
        """
        from .document import wrap

        return wrap(com.call(self.com, "ActiveDoc"), self)

    def close(self, name):
        """Close a document by name, discarding unsaved changes.

        name
            the document's title, as ``document.name`` reports it - not its
            path. ``CloseDoc`` wants the title, and silently does nothing when
            given a path.

        Returns None. Closing something that is not open does nothing.
        """
        com.call(self.com, "CloseDoc", str(name))

    def close_all(self):
        """Close every open document, discarding unsaved changes. Returns None.

        Worth calling at the start of a batch run: what is open when a script
        starts is whatever the last person left there.
        """
        com.call(self.com, "CloseAllDocuments", True)

    # ------------------------------------------------------------- commands

    def run_command(self, command, note=""):
        """Run a SOLIDWORKS UI command by its ``swCommands_e`` value.

        command
            a member of ``swcomapi.enums.swCommands_e``
        note
            text for the undo stack, which is what the user sees if they undo

        The escape hatch for the several hundred things that have a menu item
        and no API call. It drives the interface, so SOLIDWORKS must be
        visible and nothing modal may be open.

        Example, a command that opens nothing:

            >>> from swcomapi.const import swCommands_ZoomToFit  # doctest: +SKIP
            >>> _ = app.run_command(swCommands_ZoomToFit)        # doctest: +SKIP

        Pick the command carefully in a script. Anything that would put a
        dialog on screen - Save on a document that has never been saved, for
        instance - blocks every COM call until somebody answers it, and a
        script has nobody to do that. There is no timeout and no error: the
        session simply stops responding.
        """
        return com.call(self.com, "RunCommand", int(command), str(note))

    def quit(self):
        """Close SOLIDWORKS, discarding unsaved changes. Returns None.

        Only for a session your script started with `swcomapi.launch`. Calling
        it on a session a person is using closes their work.
        """
        com.call(self.com, "ExitApp")

    # ------------------------------------------------------------- plumbing

    def __repr__(self):
        try:
            return f"<SolidWorks {self.version}>"
        except Exception:
            # A dead or busy connection must not make repr() explode; that
            # would break every debugger and traceback that touches it.
            return "<SolidWorks (not responding)>"


def year_from_major(major):
    """The release year from an internal major version, or None.

    Used both for a running application and for a type library, which carry
    the same number: SOLIDWORKS 2026 is major 34 in both.

    Examples::

        >>> year_from_major(34)
        2026
        >>> year_from_major(28)
        2020
        >>> year_from_major(27) is None
        True
    """
    if major is None or major < FIRST_KNOWN_MAJOR:
        # Before 2020 the numbering does not follow this rule; say nothing
        # rather than report a wrong year.
        return None
    return major + RELEASE_YEAR_OFFSET


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
    return year_from_major(major)


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


# Which swDocumentTypes_e a file extension means. OpenDoc6 needs telling, and
# gets it wrong on its own for a file whose extension does not match what is
# inside.
DOCUMENT_TYPES = {
    ".sldprt": "part",
    ".prtdot": "part",
    ".sldlfp": "part",
    ".sldasm": "assembly",
    ".asmdot": "assembly",
    ".slddrw": "drawing",
    ".drwdot": "drawing",
}


def document_type_of(path):
    """The ``swDocumentTypes_e`` value for a file, from its extension.

    Anything unrecognised gets ``swDocPART``, which is what SOLIDWORKS does
    with an imported STEP or IGES: those come in as a part.

    Examples::

        >>> from swcomapi.const import swDocPART, swDocASSEMBLY, swDocDRAWING
        >>> document_type_of("bracket.SLDPRT") == swDocPART
        True
        >>> document_type_of("frame.sldasm") == swDocASSEMBLY
        True
        >>> document_type_of("sheet1.SLDDRW") == swDocDRAWING
        True
        >>> document_type_of("imported.step") == swDocPART
        True
    """
    import os

    from ..const import swDocASSEMBLY, swDocDRAWING, swDocPART

    values = {"part": swDocPART, "assembly": swDocASSEMBLY, "drawing": swDocDRAWING}
    extension = os.path.splitext(str(path))[1].lower()
    return values[DOCUMENT_TYPES.get(extension, "part")]
