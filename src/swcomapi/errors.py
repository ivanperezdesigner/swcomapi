"""Exceptions raised by swcomapi.

Everything derives from `SwError`, so a caller that only wants to know whether
the automation failed can catch that one name.

The COM layer raises `pywintypes.com_error`, which prints as an unreadable
tuple of HRESULTs. `swcomapi.com` translates those into the classes below and
keeps the original exception in `__cause__`, so nothing is lost.
"""


class SwError(Exception):
    """Base class for every error this package raises."""


class SwUnavailableError(SwError):
    """pywin32 is missing, or this is not Windows, so COM is unreachable."""


class SwConnectionError(SwError):
    """Could not attach to or start SOLIDWORKS."""


class SwNotRunningError(SwConnectionError):
    """No SOLIDWORKS session is running, and attaching was requested."""


class SwBusyError(SwConnectionError):
    """SOLIDWORKS answered 'call rejected by callee' until the timeout ran out.

    Normal while the application is still loading, or while a modal dialog is
    open on screen. Waiting longer usually fixes the first case; the second
    needs a human to close the dialog.
    """


class SwCallError(SwError):
    """A COM call failed.

    Attributes:
        member   name of the method or property, as a str
        hresult  the COM HRESULT, as a signed int, or None
        detail   the description COM gave, as a str
    """

    def __init__(self, message, member=None, hresult=None, detail=""):
        super().__init__(message)
        self.member = member
        self.hresult = hresult
        self.detail = detail


class SwMemberNotFoundError(SwCallError, AttributeError):
    """The method or property does not exist on this object.

    Almost always one of two things: a typo, or a member that a newer
    SOLIDWORKS added and the installed version does not have. swcomapi does
    not pin a version, so the second case is expected and this is how it
    surfaces.

    It also derives from AttributeError so that `hasattr` and `getattr` with a
    default keep behaving the way Python code expects.
    """


class SwDocumentError(SwError):
    """Opening, saving or closing a document failed.

    SOLIDWORKS reports these through bitmask codes rather than exceptions.

    Attributes:
        path      the file involved, as a str
        errors    the error bitmask, as an int
        warnings  the warning bitmask, as an int
        names     the flag names decoded from the bitmasks, as a list of str
    """

    def __init__(self, message, path="", errors=0, warnings=0, names=None):
        super().__init__(message)
        self.path = path
        self.errors = errors
        self.warnings = warnings
        self.names = names if names is not None else []


class SwWarning(UserWarning):
    """Something worked but not the way you probably meant."""
