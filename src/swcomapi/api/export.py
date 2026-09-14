"""Saving a document, in any format SOLIDWORKS can write.

One call, and the extension decides the format::

    part.export("bracket.pdf")
    part.export("bracket.step")
    part.export("bracket.stl")
    part.export("bracket.dxf")

That works because ``IModelDocExtension.SaveAs3`` dispatches on the extension
itself. This module's job is the part it does not do: telling you plainly when
it fails.

Why the errors need work
------------------------

``SaveAs3`` does not raise. It returns False and writes two bitmasks into its
last two parameters, and the only way to find out what went wrong is to decode
them against ``swFileSaveError_e`` and ``swFileSaveWarning_e``. A script that
ignores them reports success while writing nothing, which is the worst outcome
available. `save_as` decodes both and raises `SwDocumentError` with the flag
names in it.
"""

import os

from .. import com
from ..errors import SwDocumentError, SwWarning

# What SaveAs3 will write, for the error message when it will not. Not a
# gate: SOLIDWORKS decides, and a release that adds a format should not need a
# change here. Sheet metal DXF and DWG go through a different call, see
# `swcomapi.api.document.Part.export_flat_pattern`.
KNOWN_FORMATS = {
    ".sldprt": "SOLIDWORKS part",
    ".sldasm": "SOLIDWORKS assembly",
    ".slddrw": "SOLIDWORKS drawing",
    ".pdf": "PDF",
    ".step": "STEP",
    ".stp": "STEP",
    ".iges": "IGES",
    ".igs": "IGES",
    ".stl": "STL",
    ".x_t": "Parasolid text",
    ".x_b": "Parasolid binary",
    ".sat": "ACIS",
    ".3mf": "3MF",
    ".dxf": "DXF",
    ".dwg": "DWG",
    ".png": "PNG image",
    ".jpg": "JPEG image",
    ".tif": "TIFF image",
    ".edrw": "eDrawings",
    ".eprt": "eDrawings",
    ".easm": "eDrawings",
    ".wrl": "VRML",
    ".ply": "PLY",
    ".obj": "OBJ",
    ".glb": "glTF binary",
    ".gltf": "glTF",
    ".3dxml": "3D XML",
    ".xml": "3D XML",
    ".jt": "JT",
    ".ipt": "Inventor part",
}


def save_as(document, path, silent=True, copy=False, save_references=False):
    """Save ``document`` to ``path``. The extension picks the format.

    document
        a `swcomapi.api.document.Document`
    path
        where to write it, as a str. A relative path is resolved against the
        current directory, because SOLIDWORKS resolves it against its own and
        that is never what you meant.
    silent
        True suppresses the dialogs SOLIDWORKS would otherwise show. Leave it
        True in a script: a dialog with nobody to answer it hangs the call.
    copy
        True saves a copy and leaves the open document pointing at its old
        file, which is what you want when exporting.
    save_references
        True also saves the parts an assembly refers to.

    Returns the absolute path written, as a str.

    Raises `SwDocumentError` if SOLIDWORKS reports an error, with the decoded
    flag names. Warns `SwWarning` for a warning, since the file did get
    written.

    Examples::

        >>> save_as(part, "out/bracket.step")           # doctest: +SKIP
        'C:\\\\work\\\\out\\\\bracket.step'
    """
    from ..const import (
        swSaveAsCurrentVersion,
        swSaveAsOptions_Copy,
        swSaveAsOptions_SaveReferenced,
        swSaveAsOptions_Silent,
    )

    target = os.path.abspath(path)
    parent = os.path.dirname(target)
    if parent and not os.path.isdir(parent):
        raise SwDocumentError(
            f"cannot save to {target}: the folder {parent} does not exist",
            path=target,
        )

    options = 0
    if silent:
        options |= swSaveAsOptions_Silent
    if copy:
        options |= swSaveAsOptions_Copy
    if save_references:
        options |= swSaveAsOptions_SaveReferenced

    ok, out = com.call_out(
        document.extension,
        "SaveAs3",
        target,
        swSaveAsCurrentVersion,
        options,
        None,  # export data, only needed for sheet-specific drawing exports
        None,  # advanced save-as options
        interface="IModelDocExtension",
    )

    errors = out.get("Errors", 0) or 0
    warnings = out.get("Warnings", 0) or 0

    if errors:
        raise SwDocumentError(
            f"saving {target} failed: {', '.join(save_error_names(errors))}",
            path=target,
            errors=errors,
            warnings=warnings,
            names=save_error_names(errors),
        )
    if not ok and not errors:
        raise SwDocumentError(
            f"saving {target} failed, and SOLIDWORKS gave no reason. "
            f"The usual cause is an extension it cannot write"
            + (f" ({os.path.splitext(target)[1]})" if os.path.splitext(target)[1] else "")
            + ".",
            path=target,
        )
    if warnings:
        import warnings as warnings_module

        warnings_module.warn(
            f"saved {target} with warnings: {', '.join(save_warning_names(warnings))}",
            SwWarning,
            stacklevel=3,
        )
    return target


def save_error_names(code):
    """The ``swFileSaveError_e`` flags set in ``code``, as a list of str.

    Examples::

        >>> save_error_names(0)
        []
        >>> save_error_names(1)
        ['swGenericSaveError']
        >>> save_error_names(3)
        ['swGenericSaveError', 'swReadOnlySaveError']
        >>> save_error_names(256)
        ['swFileSaveAsInvalidFileExtension']
    """
    return _flag_names(code, "swFileSaveError_e")


def save_warning_names(code):
    """The ``swFileSaveWarning_e`` flags set in ``code``, as a list of str."""
    return _flag_names(code, "swFileSaveWarning_e")


def load_error_names(code):
    """The ``swFileLoadError_e`` flags set in ``code``, as a list of str.

    Examples::

        >>> load_error_names(0)
        []
        >>> load_error_names(2)
        ['swFileNotFoundError']
        >>> load_error_names(1026)
        ['swFileNotFoundError', 'swInvalidFileTypeError']
    """
    return _flag_names(code, "swFileLoadError_e")


def load_warning_names(code):
    """The ``swFileLoadWarning_e`` flags set in ``code``, as a list of str.

    Examples::

        >>> load_warning_names(0)
        []
        >>> load_warning_names(2)
        ['swFileLoadWarning_ReadOnly']
        >>> load_warning_names(130)
        ['swFileLoadWarning_ReadOnly', 'swFileLoadWarning_AlreadyOpen']
    """
    return _flag_names(code, "swFileLoadWarning_e")


def _flag_names(code, enum_name):
    """Decode a bitmask against one of the generated enumerations.

    Any bit with no name is reported as ``bit N``, so an unrecognised code
    still produces something a person can act on rather than being dropped.
    """
    from ..generated._enum_data import ENUMS

    code = int(code or 0)
    if not code:
        return []

    members = ENUMS.get(enum_name, {})
    names = []
    matched = 0
    for name, value in members.items():
        if value and code & value == value:
            names.append(name)
            matched |= value

    leftover = code & ~matched
    if leftover:
        names.extend(f"bit {bit}" for bit in _bits(leftover))
    return names


def _bits(code):
    """The set bit positions in ``code``, lowest first.

    Examples::

        >>> list(_bits(0))
        []
        >>> list(_bits(5))
        [0, 2]
    """
    position = 0
    while code:
        if code & 1:
            yield position
        code >>= 1
        position += 1


def format_of(path):
    """A readable name for the format ``path``'s extension implies, or None.

    Examples::

        >>> format_of("bracket.STEP")
        'STEP'
        >>> format_of("bracket.pdf")
        'PDF'
        >>> format_of("bracket.nonsense") is None
        True
    """
    return KNOWN_FORMATS.get(os.path.splitext(str(path))[1].lower())
