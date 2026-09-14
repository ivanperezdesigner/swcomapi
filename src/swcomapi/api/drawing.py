"""Drawings: sheets, views, and getting the model onto paper.

The everyday job is four lines::

    drawing = app.new_drawing()
    drawing.views.add("bracket.SLDPRT", "Front", at=(100, 150))
    drawing.views.add("bracket.SLDPRT", "Top", at=(100, 80))
    drawing.export("bracket.pdf")

Positions are in **mm from the bottom-left corner of the sheet**, which is
how SOLIDWORKS measures them and not how a person reads a drawing. An A3
sheet is 420 by 297, so ``(210, 148.5)`` is the middle of it.

View names
----------

``"Front"``, ``"Top"``, ``"Right"``, ``"Left"``, ``"Bottom"``, ``"Back"``,
``"Isometric"``, ``"Dimetric"``, ``"Trimetric"``, and the name of any custom
view saved in the model.

The API wants the standard ones spelled with a leading asterisk -
``"*Front"`` - because that is how SOLIDWORKS names the views it supplies
itself, as against the ones a person saved. Plain ``"Front"`` gets no view and
no error: ``CreateDrawViewFromModelView3`` returns None and says nothing. So
`Views.add` adds the asterisk for the nine standard names, passes anything
else through as given, and raises when nothing appears.

Scale
-----

A view starts at the sheet's scale. Setting `View.scale` detaches it, which is
what "Use custom scale" does in the dialog - there is no separate flag to set,
and reading `View.uses_sheet_scale` afterwards tells you it happened.
"""

from collections.abc import Sequence

from .. import com
from ..errors import SwCallError
from ..units import mm, to_mm

# swDrawingViewTypes_e, as readable names. A view made from a model view
# reports itself as "named" rather than "standard": "standard" is the kind
# Create3rdAngleViews2 lays out.
VIEW_TYPES = {
    1: "sheet",
    2: "section",
    3: "detail",
    4: "projected",
    5: "auxiliary",
    6: "standard",
    7: "named",
    8: "relative",
    9: "detached",
    10: "alternate position",
}

# The model views CreateDrawViewFromModelView3 knows by name. Not a gate -
# a custom view saved in the model works too - but the six orthographic ones
# and the three axonometric ones are what a script asks for, and a typo in
# one of them is otherwise silent.
STANDARD_VIEWS = (
    "Front",
    "Back",
    "Left",
    "Right",
    "Top",
    "Bottom",
    "Isometric",
    "Dimetric",
    "Trimetric",
)


class View:
    """One view on a sheet.

    Attributes:
        com  the raw ``IView``
    """

    def __init__(self, view, drawing=None):
        self.com = view
        self.drawing = drawing

    @property
    def name(self):
        """The view's name, as a str: ``'Drawing View1'``."""
        return com.call(self.com, "GetName2")

    @property
    def kind(self):
        """What sort of view it is, as a str: ``'standard'``, ``'section'``...

        One of the values in `VIEW_TYPES`.
        """
        code = int(com.call(self.com, "Type"))
        return VIEW_TYPES.get(code, f"unknown ({code})")

    @property
    def model(self):
        """The file the view is of, as a str.

        The full path, or empty for a view with no model behind it.
        """
        return com.call(self.com, "GetReferencedModelName")

    @property
    def position(self):
        """Where the view sits on the sheet, as ``(x, y)`` in mm.

        From the bottom-left corner of the sheet.
        """
        values = com.to_list(com.call(self.com, "Position"))
        if len(values) < 2:
            return None
        return (to_mm(values[0]), to_mm(values[1]))

    @position.setter
    def position(self, at):
        """Move the view. ``at`` is ``(x, y)`` in mm from the sheet corner.

        The position has to reach SOLIDWORKS as a SafeArray, which a Python
        tuple is not: passed as a tuple the call still returns True and the
        view lands somewhere else entirely. `swcomapi.com.from_list` builds
        the array.
        """
        x, y = at
        position = com.from_list([mm(x), mm(y), 0.0])
        if not com.call(self.com, "SetViewPosition", position, True):
            raise SwCallError(
                f"could not move {self.name!r} to {at!r}. A view that is "
                f"aligned to another can only move along that alignment; "
                f"break the alignment first.",
                member="SetViewPosition",
            )

    @property
    def scale(self):
        """The view's scale, as a float: 0.5 for 1:2.

        Assign a float, or a ``(numerator, denominator)`` tuple.
        """
        return float(com.call(self.com, "ScaleDecimal"))

    @scale.setter
    def scale(self, value):
        if isinstance(value, (tuple, list)):
            numerator, denominator = value
            value = float(numerator) / float(denominator)
        com.set_property(self.com, "ScaleDecimal", float(value))

    @property
    def uses_sheet_scale(self):
        """True while the view follows the sheet's scale, as a bool.

        Goes False by itself the moment `scale` is set: that is what "Use
        custom scale" means, and there is no separate flag to set.
        """
        return bool(com.call(self.com, "UseSheetScale"))

    @property
    def dimension_count(self):
        """How many dimensions are shown in the view, as an int."""
        return int(com.call(self.com, "GetDimensionCount"))

    @property
    def dimensions(self):
        """The dimensions shown in the view, as a list of raw objects.

        ``IDisplayDimension``, one per dimension. The value is on the model
        dimension inside it::

            display = view.dimensions[0]
            dimension = swcomapi.com.call(display, "GetDimension2", 0)

        `swcomapi.api.dimensions.Dimensions` is the wrapper for reading and
        writing values; these are the ones placed on this view.
        """
        return com.to_list(com.call(self.com, "GetDisplayDimensions"))

    def activate(self):
        """Make this the active view. Returns True.

        Needed before anything that works on "the current view" - inserting
        annotations, sketching on the view rather than on the sheet.
        """
        if self.drawing is None:
            return False
        return bool(com.call(self.drawing.com, "ActivateView", self.name))

    def __repr__(self):
        return f"<View {self.name!r} {self.kind} at {_as_ratio(self.scale)}>"


class Views(Sequence):
    """The views on the active sheet.

    A sequence, and a lookup by name::

        drawing.views.names()               # ['Drawing View1', 'Drawing View2']
        drawing.views["Drawing View1"].scale
        len(drawing.views)

    The first thing ``GetFirstView`` returns is the sheet itself rather than a
    view, and it is dropped here - which is why the count agrees with what the
    tree shows.
    """

    def __init__(self, drawing):
        self.drawing = drawing

    def _raw(self):
        sheet_view = com.call(self.drawing.com, "GetFirstView")
        if sheet_view is None:
            return []
        found = []
        view = com.call(sheet_view, "GetNextView")
        while view is not None:
            found.append(view)
            view = com.call(view, "GetNextView")
        return found

    def __len__(self):
        return len(self._raw())

    def __iter__(self):
        for view in self._raw():
            yield View(view, self.drawing)

    def __getitem__(self, key):
        if isinstance(key, str):
            for view in self:
                if view.name == key:
                    return view
            raise KeyError(
                f"no view named {key!r} on the active sheet; see .names()"
            )
        views = self._raw()
        if isinstance(key, slice):
            return [View(view, self.drawing) for view in views[key]]
        return View(views[key], self.drawing)

    def names(self):
        """Every view name on the active sheet, as a list of str."""
        return [view.name for view in self]

    def add(self, model, view="Front", at=(100.0, 100.0), scale=None):
        """Put a model view on the sheet. Returns the new `View`.

        model
            the part or assembly, by path. It has to be open in the session,
            like everything else that refers to a file by name
        view
            which view: ``"Front"``, ``"Top"``, ``"Isometric"``... see
            `STANDARD_VIEWS`, or the name of a view saved in the model
        at
            where to put it, as ``(x, y)`` in mm from the bottom-left corner
            of the sheet
        scale
            a float or a ``(numerator, denominator)`` tuple. The sheet's scale
            if omitted

        Example, three views on an A3 sheet::

            drawing.views.add(path, "Front", at=(120, 200))
            drawing.views.add(path, "Top", at=(120, 100))
            drawing.views.add(path, "Isometric", at=(300, 200), scale=(1, 2))

        Raises `SwCallError` when no view appears, which for this call means
        the model is not open, the view name is misspelled, or the position is
        off the sheet.
        """
        x, y = at
        created = com.call(
            self.drawing.com,
            "CreateDrawViewFromModelView3",
            str(model),
            _view_name(view),
            mm(x),
            mm(y),
            0.0,
        )
        if created is None:
            raise SwCallError(
                f"no view was created for {model!r}. The model has to be open "
                f"in the session, the view name has to be one SOLIDWORKS "
                f"knows ({', '.join(STANDARD_VIEWS)}, or one saved in the "
                f"model), and {at!r} has to be on the sheet.",
                member="CreateDrawViewFromModelView3",
            )

        made = View(created, self.drawing)
        if scale is not None:
            made.scale = scale
        return made

    def add_standard(self, model):
        """Put front, top and right views on the sheet. Returns True.

        ``Create3rdAngleViews2``, which places all three and aligns them, and
        which is what the Standard 3 View command does.
        """
        if not com.call(self.drawing.com, "Create3rdAngleViews2", str(model)):
            raise SwCallError(
                f"SOLIDWORKS would not lay out standard views of {model!r}. "
                f"The model has to be open in the session.",
                member="Create3rdAngleViews2",
            )
        return True

    def of_kind(self, kind):
        """Every view of one sort, as a list of `View`.

        kind
            one of the values in `VIEW_TYPES`: ``'standard'``, ``'section'``,
            ``'detail'``, ``'projected'``...
        """
        return [view for view in self if view.kind == kind]

    def __repr__(self):
        return f"<Views: {len(self)} on {self.drawing.sheet!r}>"


class Sheet:
    """One sheet of a drawing.

    Attributes:
        com  the raw ``ISheet``
    """

    def __init__(self, sheet, drawing=None):
        self.com = sheet
        self.drawing = drawing

    @property
    def name(self):
        """The sheet's name, as a str: ``'Sheet1'``."""
        return com.call(self.com, "GetName")

    @property
    def scale(self):
        """The sheet's scale, as a ``(numerator, denominator)`` tuple.

        A 1:2 sheet reads ``(1.0, 2.0)``.
        """
        properties = self._properties()
        return (properties[2], properties[3]) if len(properties) > 3 else (1.0, 1.0)

    @scale.setter
    def scale(self, ratio):
        numerator, denominator = ratio
        com.call(
            self.com, "SetScale", float(numerator), float(denominator), True, False
        )

    @property
    def size(self):
        """The paper size, as ``(width, height)`` in mm.

        Example, an A3 sheet::

            drawing.sheets["Sheet1"].size       # (420.0, 297.0)
        """
        properties = self._properties()
        if len(properties) < 7:
            return None
        return (to_mm(properties[5]), to_mm(properties[6]))

    @property
    def first_angle(self):
        """True for first-angle projection, False for third-angle.

        The European convention and the American one. It decides which side of
        the front view the top view belongs on, so it is worth checking before
        a drawing goes out.
        """
        properties = self._properties()
        return bool(properties[4]) if len(properties) > 4 else False

    def _properties(self):
        """``GetProperties2``: paper size, template, scale1, scale2, first
        angle, width, height, and a custom-size flag."""
        return com.to_list(com.call(self.com, "GetProperties2"))

    def activate(self):
        """Make this the active sheet. Returns True."""
        if self.drawing is None:
            return False
        return bool(com.call(self.drawing.com, "ActivateSheet", self.name))

    def __repr__(self):
        numerator, denominator = self.scale
        return f"<Sheet {self.name!r} at {numerator:g}:{denominator:g}>"


class Sheets(Sequence):
    """The sheets of a drawing.

    A sequence, and a lookup by name::

        drawing.sheets.names()          # ['Sheet1', 'Sheet2']
        drawing.sheets["Sheet2"].activate()
        drawing.sheets.active.size      # (420.0, 297.0)
    """

    def __init__(self, drawing):
        self.drawing = drawing

    def names(self):
        """Every sheet name, in order. As a list of str."""
        return com.to_list(com.call(self.drawing.com, "GetSheetNames"))

    def __len__(self):
        return len(self.names())

    def __iter__(self):
        for name in self.names():
            yield self[name]

    def __getitem__(self, key):
        names = self.names()
        if isinstance(key, slice):
            return [self[name] for name in names[key]]
        if isinstance(key, int):
            key = names[key]
        if key not in names:
            raise KeyError(
                f"no sheet named {key!r} in {self.drawing.name!r}; "
                f"it has {', '.join(names)}"
            )
        return Sheet(com.call(self.drawing.com, "Sheet", key), self.drawing)

    @property
    def active(self):
        """The sheet being shown, as a `Sheet`."""
        return Sheet(com.call(self.drawing.com, "GetCurrentSheet"), self.drawing)

    def add(self, name=None, paper="A3", scale=(1, 1), first_angle=True):
        """Add a sheet. Returns the new `Sheet`, which becomes the active one.

        name
            what to call it; SOLIDWORKS numbers it if omitted
        paper
            ``"A0"`` to ``"A4"``, or ``"A"`` to ``"E"`` for the American
            sizes. ``"A4"`` and ``"A4 portrait"`` are both spellable
        scale
            a ``(numerator, denominator)`` tuple
        first_angle
            True for first-angle projection, False for third

        Example::

            drawing.sheets.add("Detail", paper="A3", scale=(1, 2))
        """
        size = PAPER_SIZES.get(str(paper).strip().lower())
        if size is None:
            raise ValueError(
                f"paper is one of {sorted(set(PAPER_SIZES))}, not {paper!r}"
            )

        numerator, denominator = scale
        before = set(self.names())
        # PaperSize and TemplateIn are separate enumerations - swDwgPaperSizes_e
        # and swDwgTemplates_e - that happen to number the same sizes the same
        # way, so one value serves for both.
        made = com.call(
            self.drawing.com,
            "NewSheet4",
            str(name) if name else "",
            size,
            size,
            float(numerator),
            float(denominator),
            bool(first_angle),
            "",      # TemplateName: the default sheet format
            0.0,     # Width, only read for a user-defined size
            0.0,     # Height
            "",      # PropertyViewName
            0.0, 0.0, 0.0, 0.0,   # zone margins
            0, 0,    # zone rows and columns
        )
        if not made:
            raise SwCallError(
                f"SOLIDWORKS would not add a sheet named {name!r}. A name "
                f"already in use is the usual reason; this drawing has "
                f"{', '.join(sorted(before))}.",
                member="NewSheet4",
            )
        return self.active

    def __repr__(self):
        return f"<Sheets: {len(self)} in {self.drawing.name!r}>"


def _as_ratio(scale):
    """A scale written the way a drawing writes it, as a str.

    Examples::

        >>> _as_ratio(0.5)
        '1:2'
        >>> _as_ratio(2.0)
        '2:1'
        >>> _as_ratio(1.0)
        '1:1'
        >>> _as_ratio(0.0)
        '?'
    """
    if not scale:
        return "?"
    if scale >= 1:
        return f"{scale:g}:1"
    return f"1:{1 / scale:g}"


def _view_name(view):
    """The name ``CreateDrawViewFromModelView3`` wants, as a str.

    The standard views are asterisked; anything else is a view saved in the
    model and is passed through untouched.

    Examples::

        >>> _view_name("Front")
        '*Front'
        >>> _view_name("isometric")
        '*Isometric'
        >>> _view_name("*Top")
        '*Top'
        >>> _view_name("Detail A")
        'Detail A'
    """
    bare = str(view).lstrip("*")
    for standard in STANDARD_VIEWS:
        if bare.lower() == standard.lower():
            return f"*{standard}"
    return str(view)


# swDwgPaperSizes_e, by the names a person uses. Both spellings of the
# landscape sizes are here so that "a3" and "A3" both work.
PAPER_SIZES = {
    "a": 0,
    "a landscape": 0,
    "a portrait": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "a4": 6,
    "a4 portrait": 7,
    "a3": 8,
    "a2": 9,
    "a1": 10,
    "a0": 11,
}
