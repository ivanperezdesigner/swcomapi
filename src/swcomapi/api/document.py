"""Documents: parts, assemblies and drawings.

    part = app.open("bracket.SLDPRT")

    part.name                       # 'bracket.SLDPRT'
    part.configurations             # ['BRK-020', 'BRK-040', 'Default']
    part.configuration = "BRK-040"
    part.dimensions["Length@Boss-Extrude1"] = 55      # mm
    part.features["HolePattern"].suppress()
    part.properties["Revision"] = "B"
    part.rebuild()
    part.export("BRK-040.pdf")
    part.close()

``app.open`` gives you a `Part`, an `Assembly` or a `Drawing` depending on what
the file is, and each adds what only it can do: mass properties and flat
patterns on a part, components on an assembly, sheets and views on a drawing.

Closing
-------

A document is a context manager, which is the reliable way to not leave files
open in SOLIDWORKS after a script has crashed::

    with app.open("bracket.SLDPRT") as part:
        part.export("bracket.step")
    # closed, even if export raised

Leaving a document open is not harmless: the next run gets
``swFileLoadWarning_AlreadyOpen`` and a document that may be in a state the
script did not expect.

Everything in millimetres
-------------------------

Every length here is millimetres and every angle degrees, in and out. The raw
API is metres and radians; see `swcomapi.units`.
"""

import os

from .. import com, units
from ..errors import SwDocumentError
from . import export as export_module
from .configurations import Configurations
from .dimensions import Dimensions
from .features import Features
from .properties import Properties


def wrap(model, app=None):
    """Wrap a raw ``IModelDoc2`` in the right class.

    Returns a `Part`, an `Assembly`, a `Drawing`, or a plain `Document` for a
    type this package does not specialise. Returns None for None, so it can be
    used on anything the API hands back.

    Examples::

        >>> wrap(None) is None
        True
    """
    if model is None:
        return None

    from ..const import swDocASSEMBLY, swDocDRAWING, swDocPART

    kinds = {swDocPART: Part, swDocASSEMBLY: Assembly, swDocDRAWING: Drawing}
    return kinds.get(com.call(model, "GetType"), Document)(model, app)


class Document:
    """An open SOLIDWORKS document.

    Do not build this directly; use ``app.open(...)`` or ``app.new_part()``,
    which return the right subclass.

    Attributes:
        com  the raw ``IModelDoc2``
        app  the `swcomapi.api.app.SolidWorks` it belongs to, or None
    """

    def __init__(self, model, app=None):
        self.com = model
        self.app = app

    # ------------------------------------------------------------- identity

    @property
    def name(self):
        """The document's title, as a str. Usually the file name."""
        return com.call(self.com, "GetTitle")

    @property
    def path(self):
        """The full file path, as a str. Empty for a document never saved."""
        return com.call(self.com, "GetPathName")

    @property
    def folder(self):
        """The folder the document lives in, as a str. Empty if never saved."""
        return os.path.dirname(self.path)

    @property
    def kind(self):
        """``'part'``, ``'assembly'``, ``'drawing'`` or ``'other'``, as a str."""
        from ..const import swDocASSEMBLY, swDocDRAWING, swDocPART

        return {
            swDocPART: "part",
            swDocASSEMBLY: "assembly",
            swDocDRAWING: "drawing",
        }.get(com.call(self.com, "GetType"), "other")

    @property
    def modified(self):
        """True if there are unsaved changes.

        ``GetSaveFlag`` is the API's name for it, which reads backwards: it is
        True when the document is *dirty*.
        """
        return bool(com.call(self.com, "GetSaveFlag"))

    @property
    def extension(self):
        """The raw ``IModelDocExtension``.

        Half the useful API lives here rather than on ``IModelDoc2``, so it is
        worth a short name.
        """
        return com.call(self.com, "Extension")

    # ------------------------------------------------------------ the parts

    @property
    def configurations(self):
        """The document's configurations, as a `Configurations`.

        A sequence of names.
        """
        return Configurations(self.com, self)

    @property
    def configuration(self):
        """The active configuration's name, as a str. Assign to switch."""
        return self.configurations.active

    @configuration.setter
    def configuration(self, name):
        self.configurations.activate(name)

    @property
    def features(self):
        """The feature tree, as a `Features`."""
        return Features(self.com, self)

    @property
    def dimensions(self):
        """The dimensions, as a `Dimensions`. In millimetres and degrees."""
        return Dimensions(self.com, self)

    @property
    def equations(self):
        """The equations and global variables, as an `Equations`.

        A sequence of the lines and a lookup by name::

            part.equations.names()          # ['width', 'height']
            part.equations["width"]         # 60.0   (document units)
            part.equations["width"] = 80
            part.equations.add('"depth" = 12')

        In the document's own units, not in millimetres: an equation is a
        string SOLIDWORKS parses. See `swcomapi.api.equations`.
        """
        from .equations import Equations

        return Equations(self.com, self)

    @property
    def sketches(self):
        """The sketches, as a `swcomapi.api.sketch.Sketches`.

        A sequence and a lookup by name::

            part.sketches.names()        # ['Sketch1', 'Sketch2']
            part.sketches["Sketch1"].segments
        """
        from .sketch import Sketches

        return Sketches(self)

    def sketch_on(self, plane=None, add_to_db=False, three_d=False):
        """Open a sketch for drawing. Returns a context manager.

        plane
            what to sketch on, by name: ``"Front Plane"``, ``"Top Plane"``,
            ``"Right Plane"``, or a face. Whatever is already selected if
            omitted
        add_to_db
            True puts the sketch manager into database mode, so geometry goes
            in exactly as given, with no inferred relations and no snapping.
            What a script usually wants; the cost is that nothing holds the
            sketch together afterwards
        three_d
            True opens a 3D sketch

        Use it in a ``with`` block, so the sketch is closed even if the block
        raises - a session left in sketch mode makes everything after it
        behave strangely::

            with part.sketch_on("Front Plane") as sketch:
                sketch.rectangle((0, 0), (60, 40))

        Everything in mm. See `swcomapi.api.sketch.SketchSession` for what can
        be drawn.
        """
        from .sketch import SketchSession

        return SketchSession(self, plane=plane, add_to_db=add_to_db, three_d=three_d)

    @property
    def properties(self):
        """The file-level custom properties, as a `Properties`.

        For a configuration's own properties, ``properties_of(name)``.
        """
        return self.properties_of("")

    def properties_of(self, configuration):
        """The custom properties of one configuration, as a `Properties`.

        Pass ``""`` for the file-level set, which is what `properties` does.
        """
        manager = com.call(self.extension, "CustomPropertyManager", str(configuration))
        return Properties(manager, str(configuration), self)

    # -------------------------------------------------------------- working

    def rebuild(self, all_configurations=False):
        """Rebuild the model. Returns True if it rebuilt without error.

        all_configurations
            True forces every configuration to rebuild, which is slow and is
            what you want before saving a file whose configurations a script
            has been changing.

        A False return means a feature failed to rebuild. It is not an
        exception because a partly-failed rebuild is a real state that a
        script may want to inspect rather than abort on.
        """
        member = "ForceRebuild3" if all_configurations else "EditRebuild3"
        return bool(
            com.call(self.com, member, False) if all_configurations
            else com.call(self.com, member)
        )

    def save(self, silent=True):
        """Save in place. Returns the path written, as a str.

        Raises `SwDocumentError` if SOLIDWORKS reports an error, with the
        decoded flag names. A document that was never saved has no path, and
        that is an error here rather than a dialog: use `save_as`.
        """
        from ..const import swSaveAsOptions_Silent

        if not self.path:
            raise SwDocumentError(
                f"{self.name!r} has never been saved, so there is nowhere to "
                f"save it to. Use save_as(path).",
                path="",
            )

        ok, out = com.call_out(
            self.com,
            "Save3",
            swSaveAsOptions_Silent if silent else 0,
            interface="IModelDoc2",
        )
        errors = out.get("Errors", 0) or 0
        if errors or not ok:
            names = export_module.save_error_names(errors)
            raise SwDocumentError(
                f"saving {self.path!r} failed"
                + (f": {', '.join(names)}" if names else ""),
                path=self.path,
                errors=errors,
                warnings=out.get("Warnings", 0) or 0,
                names=names,
            )
        return self.path

    def save_as(self, path, **options):
        """Save to ``path``. The extension picks the format.

        Returns the absolute path written, as a str. See
        `swcomapi.api.export.save_as` for the options.
        """
        return export_module.save_as(self, path, **options)

    def export(self, path, **options):
        """Save a copy to ``path``, leaving this document where it is.

        The same call as `save_as` with ``copy=True``, and the name to reach
        for when writing a PDF, a STEP or a DXF: an export should not make
        SOLIDWORKS think the open document now lives in the export folder.

        Returns the absolute path written, as a str.

        Example::

            part.export("out/BRK-040.step")
        """
        options.setdefault("copy", True)
        return export_module.save_as(self, path, **options)

    def close(self, save=False):
        """Close the document.

        save
            True saves first; False discards any unsaved changes, silently,
            which is what a script almost always wants

        Returns None. Closing an already-closed document does nothing.
        """
        if self.app is None:
            raise SwDocumentError(
                f"{self.name!r} was not opened through a SolidWorks object, "
                f"so this cannot close it. Use app.close(name).",
                path=self.path,
            )
        if save:
            self.save()
        self.app.close(self.name)

    # ------------------------------------------------------------ selecting

    def select(self, name, kind, mark=0, append=False):
        """Select something by name. Returns True if it got selected.

        name
            what SOLIDWORKS calls it, e.g. ``"Boss-Extrude1"``, ``"Front Plane"``
        kind
            the selection type, as the API's string: ``"BODYFEATURE"``,
            ``"PLANE"``, ``"FACE"``, ``"COMPONENT"``, ``"SKETCH"``...
        mark
            the selection mark, which some feature-creating calls require to
            tell one selection from another
        append
            True adds to the selection instead of replacing it

        Example::

            part.select("Front Plane", "PLANE")
        """
        return bool(
            com.call(
                self.extension,
                "SelectByID2",
                str(name),
                str(kind),
                0.0,
                0.0,
                0.0,
                bool(append),
                int(mark),
                None,
                0,
            )
        )

    def clear_selection(self):
        """Deselect everything. Returns None.

        Worth doing before any call that acts on the selection, because what
        is selected when a script starts is whatever the last person clicked.
        """
        com.call(self.com, "ClearSelection2", True)

    @property
    def selection_count(self):
        """How many things are selected, as an int."""
        manager = com.call(self.com, "SelectionManager")
        return com.call(manager, "GetSelectedObjectCount2", -1)

    # ------------------------------------------------------------- niceties

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        """Close without saving, whether or not the block succeeded.

        Deliberately does not save on the way out: a block that raised
        half-way through has left the document in a state nobody chose, and
        writing that to disk would be worse than losing it.
        """
        self.close(save=False)
        return False

    def __repr__(self):
        try:
            return f"<{type(self).__name__} {self.name!r}>"
        except Exception:
            return f"<{type(self).__name__} (not responding)>"


class Part(Document):
    """A part document. Adds modelling, mass properties and sheet metal."""

    # ------------------------------------------------------------- geometry

    @property
    def bodies(self):
        """The solid bodies, as a list of `swcomapi.api.geometry.Body`.

        The geometry rather than the tree: faces, edges, vertices and the
        bounding box::

            part.bodies[0].size             # (60.0, 40.0, 10.0) in mm
            part.bodies[0].faces_of("cylinder")

        Surfaces and wires are left out; `bodies_of` takes a ``kind``.
        """
        from .geometry import bodies_of

        return bodies_of(self)

    def bodies_of(self, kind="solid", visible_only=False):
        """The bodies of one sort, as a list of `swcomapi.api.geometry.Body`.

        kind
            ``'solid'``, ``'sheet'``, ``'wire'`` or ``'all'``
        visible_only
            True leaves out the hidden ones
        """
        from .geometry import bodies_of

        return bodies_of(self, kind=kind, visible_only=visible_only)

    # ------------------------------------------------------------ modelling

    def extrude(self, depth, **options):
        """Extrude a sketch into a boss. Returns the new `Feature`.

        Takes the sketch that was just closed, or one named with
        ``sketch="Sketch1"``. Depth in mm.

        Example, a 60 by 40 plate 10 mm thick::

            with part.sketch_on("Front Plane") as sketch:
                sketch.rectangle((0, 0), (60, 40))
            part.extrude(10)

        Every argument is described in `swcomapi.api.modeling.extrude`.
        """
        from .modeling import extrude

        return extrude(self, depth, **options)

    def cut(self, depth=None, **options):
        """Cut a sketch out of the body. Returns the new `Feature`.

        Example, a 12 mm hole all the way through::

            with part.sketch_on("Front Plane") as sketch:
                sketch.circle((30, 20), radius=6)
            part.cut(through_all=True)

        See `swcomapi.api.modeling.cut`.
        """
        from .modeling import cut

        return cut(self, depth, **options)

    def revolve(self, angle=360.0, **options):
        """Revolve a sketch into a boss. Returns the new `Feature`.

        Angle in degrees. See `swcomapi.api.modeling.revolve`.
        """
        from .modeling import revolve

        return revolve(self, angle, **options)

    # ------------------------------------------------------ mass properties

    @property
    def mass_properties(self):
        """Mass, volume, area and centre of mass, as a dict.

        Keys, all in millimetre units:

        ``mass``
            grams
        ``volume``
            cubic millimetres
        ``area``
            square millimetres
        ``centre``
            ``(x, y, z)`` in millimetres, in the part's own coordinate system
        ``density``
            grams per cubic millimetre, derived as mass over volume

        One COM call, so read this once and pick out what you need rather than
        reading `mass` and `volume` separately.

        Example::

            part.mass_properties["mass"]          # 496.033
        """
        from ..const import swMassPropertyAccuracyLevel_Medium

        # swMassPropertyAccuracyLevel_e runs Lower, Medium, Higher - there is
        # no member called Default, whatever the parameter table implies by
        # calling 1 "default".
        result, out = com.call_out(
            self.extension,
            "GetMassProperties2",
            swMassPropertyAccuracyLevel_Medium,
            False,
            interface="IModelDocExtension",
        )
        values = com.to_list(result)
        if len(values) < 6 or out.get("Status", 0):
            raise SwDocumentError(
                f"{self.name!r} has no mass properties. A part with no solid "
                f"body, or one whose material has no density, reports none.",
                path=self.path,
            )

        volume = units.to_mm3(values[3])
        mass = units.to_g(values[5])
        return {
            "centre": tuple(units.to_mm_all(values[0:3])),
            "volume": volume,
            "area": units.to_mm2(values[4]),
            "mass": mass,
            "density": (mass / volume) if volume else 0.0,
        }

    @property
    def mass(self):
        """Mass in grams, as a float."""
        return self.mass_properties["mass"]

    @property
    def volume(self):
        """Volume in cubic millimetres, as a float."""
        return self.mass_properties["volume"]

    @property
    def area(self):
        """Surface area in square millimetres, as a float."""
        return self.mass_properties["area"]

    @property
    def centre_of_mass(self):
        """``(x, y, z)`` in millimetres, as a tuple of float."""
        return self.mass_properties["centre"]

    # ---------------------------------------------------------- the material

    @property
    def material(self):
        """The active configuration's material, as a str. Empty if none.

        Assign a name to apply one::

            part.material                   # 'Stainless Steel (ferritic)'
            part.material = "6061 Alloy"
            part.material = ""              # no material

        A material belongs to a configuration, not to a part - see
        `material_of` and `set_material`, and `swcomapi.api.materials` for
        which names are available.
        """
        from .materials import material_of

        return material_of(self)

    @material.setter
    def material(self, name):
        from .materials import set_material

        set_material(self, name)

    @property
    def material_database(self):
        """Which library the applied material comes from, as a str.

        Usually ``'SOLIDWORKS Materials'``. Empty when no material is applied.
        """
        from .materials import database_of

        return database_of(self)

    def material_of(self, configuration):
        """The material of one configuration, as a str.

        Example, a part that ships in two metals::

            part.material_of("BRK-040")         # '6061 Alloy'
            part.material_of("BRK-040-SS")      # 'AISI 304'
        """
        from .materials import material_of

        return material_of(self, configuration)

    def set_material(self, name, configuration=None, database=None):
        """Apply a material. Returns the name applied, as a str.

        configuration
            which configuration; the active one if omitted, ``"*"`` for all
        database
            the ``.sldmat`` library; the SOLIDWORKS one if omitted

        Raises `SwCallError` if the material does not end up applied - which
        is what a misspelled name does, silently, through the raw call. See
        `swcomapi.api.materials.set_material`.
        """
        from .materials import set_material

        return set_material(self, name, configuration=configuration, database=database)

    # ----------------------------------------------------------- sheet metal

    @property
    def is_sheet_metal(self):
        """True if the part has a sheet metal feature.

        Example::

            if part.is_sheet_metal:
                part.export_flat_pattern("blank.dxf")
        """
        return bool(self.features.of_type("SheetMetal") or self.features.of_type("SMBaseFlange"))

    def export_flat_pattern(self, path, include_bend_lines=True):
        """Write the flat pattern to a DXF or DWG. Returns the path, as a str.

        path
            where to write it; the extension must be ``.dxf`` or ``.dwg``
        include_bend_lines
            True also writes the bend lines, which is what a press brake
            operator wants and what a laser programmer does not

        Raises `SwDocumentError` if the part is not sheet metal, or if
        SOLIDWORKS declines to write the file.

        ``IPartDoc.ExportToDWG2`` is the call, not ``SaveAs3``: saving a part
        as DXF gives you the model's edges, not the unfolded blank.
        """
        from ..const import swExportToDWG_ExportSheetMetal

        target = os.path.abspath(path)
        if os.path.splitext(target)[1].lower() not in (".dxf", ".dwg"):
            raise SwDocumentError(
                f"a flat pattern goes to .dxf or .dwg, not {target!r}",
                path=target,
            )
        if not self.is_sheet_metal:
            raise SwDocumentError(
                f"{self.name!r} is not a sheet metal part, so it has no flat "
                f"pattern.",
                path=self.path,
            )

        # The options are a bit field of swExportToDWG_e-adjacent flags packed
        # into an array; geometry 1 is "the flat pattern".
        ok = com.call(
            self.com,
            "ExportToDWG2",
            target,
            self.path,
            swExportToDWG_ExportSheetMetal,
            True,
            None,
            False,
            False,
            1 if include_bend_lines else 0,
            None,
        )
        if not ok:
            raise SwDocumentError(
                f"SOLIDWORKS declined to write the flat pattern to {target!r}",
                path=target,
            )
        return target


class Assembly(Document):
    """An assembly document. Adds components."""

    @property
    def components(self):
        """The top-level components, as a `swcomapi.api.components.Components`.

        A sequence and a mapping at once::

            asm.components.names()          # ['rail-1', 'rail-2', 'gusset-1']
            asm.components["rail-2"].path   # 'C:\\\\work\\\\rail.SLDPRT'
            asm.components.all()            # every level, not just the top
        """
        from .components import Components

        return Components(self)

    @property
    def component_count(self):
        """How many components the assembly has, counting sub-assemblies.

        As an int.
        """
        return com.call(self.com, "GetComponentCount", False)

    def component_paths(self):
        """The file path of every top-level component, as a list of str.

        Duplicates are kept: two instances of the same part are two entries,
        which is what a count of parts needs.
        """
        return self.components.paths()


class Drawing(Document):
    """A drawing document. Adds sheets and views.

    The everyday job::

        drawing = app.new_drawing()
        drawing.views.add(path, "Front", at=(120, 200))
        drawing.views.add(path, "Top", at=(120, 100))
        drawing.export("bracket.pdf")

    Positions in mm from the bottom-left corner of the sheet. See
    `swcomapi.api.drawing` for the rest.
    """

    @property
    def sheets(self):
        """The sheets, as a `swcomapi.api.drawing.Sheets`.

        A sequence and a lookup by name::

            drawing.sheets.names()          # ['Sheet1']
            drawing.sheets.active.size      # (420.0, 297.0) in mm
            drawing.sheets.add("Detail", paper="A3", scale=(1, 2))
        """
        from .drawing import Sheets

        return Sheets(self)

    @property
    def views(self):
        """The views on the active sheet, as a `swcomapi.api.drawing.Views`.

        A sequence and a lookup by name::

            drawing.views.names()
            drawing.views["Drawing View1"].scale = (1, 2)
            drawing.views.add(path, "Isometric", at=(300, 200))
        """
        from .drawing import Views

        return Views(self)

    @property
    def sheet(self):
        """The active sheet's name, as a str. Assign to switch."""
        return com.call(com.call(self.com, "GetCurrentSheet"), "GetName")

    @sheet.setter
    def sheet(self, name):
        if not com.call(self.com, "ActivateSheet", str(name)):
            raise SwDocumentError(
                f"no sheet named {name!r}. This drawing has: "
                f"{', '.join(self.sheets.names())}",
                path=self.path,
            )

    @property
    def scale(self):
        """The active sheet's scale, as a ``(numerator, denominator)`` tuple.

        A 1:2 sheet reads ``(1.0, 2.0)``.
        """
        return self.sheets.active.scale

    @scale.setter
    def scale(self, ratio):
        self.sheets.active.scale = ratio

    def view_names(self):
        """The name of every view on the active sheet, as a list of str."""
        return self.views.names()
