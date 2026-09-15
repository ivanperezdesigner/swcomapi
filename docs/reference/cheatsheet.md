# Cheat sheet

Every call in the pythonic layer, with the signature read from
the installed package and the description taken from its own docstring. Run
`python -m swcomapi.tools cheatsheet` to rebuild it; do not edit it by hand.

For what a call does in detail, and for the traps, see
[`DOCUMENTATION.md`](../../DOCUMENTATION.md). For the 19,874 members of the
COM API underneath, use `swcomapi.find` and `swcomapi.describe`.

## What holds everywhere

- **Millimetres and degrees**, everywhere. SOLIDWORKS works in metres and
  radians and this package converts. The one exception is equations, which
  are in the document's own units, because an equation is a string
  SOLIDWORKS parses rather than a number it stores.
- **Points are tuples**: `(x, y)` in a sketch, `(x, y, z)` in space.
- **The raw COM object is always there**, on `.com`, on every wrapper.
- **Names SOLIDWORKS reserves cannot be used for a global variable.**
  `thickness` is one: it drives sheet metal, and the equation manager
  refuses it.
- A dimension's name is `Dimension@Feature`, or `Dimension@Feature@Document`.

## Connecting

| call | what it does |
|---|---|
| `swc.connect(visible=True, timeout=180.0)` | Attach to a running SOLIDWORKS, or start one if none is running. |
| `swc.attach(visible=None, timeout=180.0)` | Use the SOLIDWORKS session that is already open. |
| `swc.launch(visible=True, timeout=180.0)` | Start a new SOLIDWORKS process and use that. |

## `app`

Getting hold of SOLIDWORKS, and the documents it has open.

### `SolidWorks`

A connected SOLIDWORKS application.

| call | what it does |
|---|---|
| `.revision_number` | [get] The internal version string, as a str, e.g. `'34.3.0'`. |
| `.year` | [get] The release year, as an int, e.g. `2026`. |
| `.build_numbers` | [get] The three build strings, as a list of str. |
| `.service_pack` | [get] The service pack number, as an int, or None. |
| `.version` | [get] A readable one-liner, as a str. |
| `.process_id` | [get] The Windows process id of this SOLIDWORKS, as an int. |
| `.visible` | [get/set] Whether the SOLIDWORKS window is shown, as a bool. |
| `.open(path, configuration=None, read_only=False, silent=True, view_only=False)` | Open a file. Returns a `Part`, `Assembly` or `Drawing`. |
| `.new_part(template=None)` | Create a new part. Returns a `Part`. |
| `.new_assembly(template=None)` | Create a new assembly. Returns an `Assembly`. |
| `.new_drawing(template=None)` | Create a new drawing. Returns a `Drawing`. |
| `.documents` | [get] Every open document, as a list of `Document` subclasses. |
| `.active` | [get] The document with focus, as a `Document` subclass, or None. |
| `.close(name)` | Close a document by name, discarding unsaved changes. |
| `.close_all()` | Close every open document, discarding unsaved changes. Returns None. |
| `.run_command(command, note='')` | Run a SOLIDWORKS UI command by its `swCommands_e` value. |
| `.quit()` | Close SOLIDWORKS, discarding unsaved changes. Returns None. |

### `year_from_major(major)`

The release year from an internal major version, or None.

### `document_type_of(path)`

The `swDocumentTypes_e` value for a file, from its extension.

## `document`

Anything open: a part, an assembly or a drawing.

### `wrap(model, app=None)`

Wrap a raw `IModelDoc2` in the right class.

### `Document`

An open SOLIDWORKS document.

| call | what it does |
|---|---|
| `.name` | [get] The document's title, as a str. Usually the file name. |
| `.path` | [get] The full file path, as a str. Empty for a document never saved. |
| `.folder` | [get] The folder the document lives in, as a str. Empty if never saved. |
| `.kind` | [get] `'part'`, `'assembly'`, `'drawing'` or `'other'`, as a str. |
| `.modified` | [get] True if there are unsaved changes. |
| `.extension` | [get] The raw `IModelDocExtension`. |
| `.configurations` | [get] The document's configurations, as a `Configurations`. |
| `.configuration` | [get/set] The active configuration's name, as a str. Assign to switch. |
| `.features` | [get] The feature tree, as a `Features`. |
| `.dimensions` | [get] The dimensions, as a `Dimensions`. In millimetres and degrees. |
| `.equations` | [get] The equations and global variables, as an `Equations`. |
| `.sketches` | [get] The sketches, as a `swcomapi.api.sketch.Sketches`. |
| `.sketch_on(plane=None, add_to_db=False, three_d=False)` | Open a sketch for drawing. Returns a context manager. |
| `.properties` | [get] The file-level custom properties, as a `Properties`. |
| `.properties_of(configuration)` | The custom properties of one configuration, as a `Properties`. |
| `.rebuild(all_configurations=False)` | Rebuild the model. Returns True if it rebuilt without error. |
| `.save(silent=True)` | Save in place. Returns the path written, as a str. |
| `.save_as(path, **options)` | Save to `path`. The extension picks the format. |
| `.export(path, **options)` | Save a copy to `path`, leaving this document where it is. |
| `.close(save=False)` | Close the document. |
| `.select(name, kind, mark=0, append=False)` | Select something by name. Returns True if it got selected. |
| `.clear_selection()` | Deselect everything. Returns None. |
| `.selection_count` | [get] How many things are selected, as an int. |

### `Part`

A part document. Adds modelling, mass properties and sheet metal.

| call | what it does |
|---|---|
| `.bodies` | [get] The solid bodies, as a list of `swcomapi.api.geometry.Body`. |
| `.bodies_of(kind='solid', visible_only=False)` | The bodies of one sort, as a list of `swcomapi.api.geometry.Body`. |
| `.extrude(depth, **options)` | Extrude a sketch into a boss. Returns the new `Feature`. |
| `.cut(depth=None, **options)` | Cut a sketch out of the body. Returns the new `Feature`. |
| `.revolve(angle=360.0, **options)` | Revolve a sketch into a boss. Returns the new `Feature`. |
| `.mass_properties` | [get] Mass, volume, area and centre of mass, as a dict. |
| `.mass` | [get] Mass in grams, as a float. |
| `.volume` | [get] Volume in cubic millimetres, as a float. |
| `.area` | [get] Surface area in square millimetres, as a float. |
| `.centre_of_mass` | [get] `(x, y, z)` in millimetres, as a tuple of float. |
| `.material` | [get/set] The active configuration's material, as a str. Empty if none. |
| `.material_database` | [get] Which library the applied material comes from, as a str. |
| `.material_of(configuration)` | The material of one configuration, as a str. |
| `.set_material(name, configuration=None, database=None)` | Apply a material. Returns the name applied, as a str. |
| `.is_sheet_metal` | [get] True if the part has a sheet metal feature. |
| `.sheet_metal` | [get] The sheet metal parameters, as a `SheetMetal`, or None. |
| `.export_flat_pattern(path, include_bend_lines=True)` | Write the flat pattern to a DXF or DWG. Returns the path, as a str. |

### `Assembly`

An assembly document. Adds components.

| call | what it does |
|---|---|
| `.components` | [get] The top-level components, as a `swcomapi.api.components.Components`. |
| `.component_count` | [get] How many components the assembly has, counting sub-assemblies. |
| `.component_paths()` | The file path of every top-level component, as a list of str. |

### `Drawing`

A drawing document. Adds sheets and views.

| call | what it does |
|---|---|
| `.sheets` | [get] The sheets, as a `swcomapi.api.drawing.Sheets`. |
| `.views` | [get] The views on the active sheet, as a `swcomapi.api.drawing.Views`. |
| `.sheet` | [get/set] The active sheet's name, as a str. Assign to switch. |
| `.scale` | [get/set] The active sheet's scale, as a `(numerator, denominator)` tuple. |
| `.view_names()` | The name of every view on the active sheet, as a list of str. |

## `sketch`

Drawing, and reading a sketch back.

### `Sketch`

One sketch, whether or not it is being edited.

| call | what it does |
|---|---|
| `.name` | [get] The sketch's name, as a str: `'Sketch1'`. |
| `.is_3d` | [get] True for a 3D sketch, as a bool. |
| `.segments` | [get] The lines, arcs and the rest, as a list of `Segment`. |
| `.points` | [get] Every sketch point, as a list of `(x, y, z)` tuples in mm. |

### `Segment`

One line, arc, spline or ellipse in a sketch.

| call | what it does |
|---|---|
| `.kind` | [get] What it is, as a str: `'line'`, `'arc'`, `'spline'`... |
| `.length` | [get] Its length in mm, as a float. |
| `.is_construction` | [get] True for construction geometry, as a bool. |

### `Sketches`

The sketches in a document.

| call | what it does |
|---|---|
| `.names()` | Every sketch name, as a list of str. |
| `.active` | [get] The sketch being edited, as a `Sketch`, or None. |
| `.manager` | [get] The raw `ISketchManager`. |

### `SketchSession`

A sketch open for editing, with the drawing methods on it.

| call | what it does |
|---|---|
| `.manager` | [get] The raw `ISketchManager`. |
| `.open()` | Start the sketch. Returns self. |
| `.close(rebuild=True)` | Finish the sketch. Returns the `Sketch` that was drawn. |
| `.line(start, end)` | A line from `start` to `end`. Returns a `Segment`. |
| `.centreline(start, end)` | A construction line from `start` to `end`. Returns a `Segment`. |
| `.centerline(start, end)` | A construction line from `start` to `end`. Returns a `Segment`. |
| `.circle(centre, radius)` | A circle. Returns a `Segment`. |
| `.arc(centre, start, end, clockwise=False)` | An arc around `centre` from `start` to `end`, a `Segment`. |
| `.rectangle(corner, opposite)` | A rectangle between two opposite corners. Returns four `Segment`. |
| `.centre_rectangle(centre, corner)` | A rectangle centred on `centre`. Returns four `Segment`. |
| `.center_rectangle(centre, corner)` | A rectangle centred on `centre`. Returns four `Segment`. |
| `.point(at)` | A sketch point. Returns the raw `ISketchPoint`. |
| `.use_edges(chain=True, inner_loops=False)` | Convert the selected edges into sketch geometry. Returns True. |

## `modeling`

Turning a sketch into geometry.

### `extrude(document, depth, sketch=None, both_directions=False, second_depth=None, midplane=False, reverse=False, draft=None, draft_outward=False, merge=True, through_all=False)`

Extrude a sketch into a boss. Returns the new `Feature`.

### `cut(document, depth=None, sketch=None, both_directions=False, second_depth=None, midplane=False, reverse=False, draft=None, draft_outward=False, through_all=False)`

Cut a sketch out of the body. Returns the new `Feature`.

### `revolve(document, angle=360.0, sketch=None, axis=None, reverse=False, merge=True)`

Revolve a sketch into a boss. Returns the new `Feature`.

## `features`

The tree, and suppression.

### `Feature`

One entry in the feature tree.

| call | what it does |
|---|---|
| `.name` | [get/set] The name as it appears in the tree, as a str. |
| `.type` | [get] The feature type, as a str, e.g. `'Extrusion'`, `'Fillet'`. |
| `.is_furniture` | [get] True for a tree entry that is not a modelling feature. |
| `.suppressed` | [get/set] Whether the feature is suppressed in the active configuration. |
| `.suppress(in_configurations=None, everywhere=False)` | Suppress the feature. |
| `.unsuppress(in_configurations=None, everywhere=False, with_dependents=False)` | Unsuppress the feature. |
| `.children` | [get] The features nested under this one, as a list of `Feature`. |
| `.dimensions` | [get] The full names of this feature's dimensions, as a list of str. |

### `Features`

The feature tree of a document.

| call | what it does |
|---|---|
| `.names()` | Every tree entry's name, in tree order. As a list of str. |
| `.solid_features()` | The modelling features only, as a list of `Feature`. |
| `.of_type(type_name)` | Every feature whose `Feature.type` is `type_name`. |
| `.types()` | The distinct feature types present, sorted. As a list of str. |

## `dimensions`

Named dimensions, in millimetres and degrees.

### `Dimensions`

The dimensions of a document, keyed by full name.

| call | what it does |
|---|---|
| `.raw(name)` | The raw `IDimension`. Raises KeyError if there is no such name. |
| `.names()` | Every dimension's full name, sorted. As a list of str. |
| `.value_in(name, configuration)` | The value in one configuration, without switching to it. |
| `.set_in(name, configuration, value)` | Set the value in one configuration, without switching to it. |
| `.set_everywhere(name, value)` | Set the value in every configuration, in millimetres or degrees. |
| `.is_angular(name)` | True if `name` is an angle, so its unit is degrees. |

## `configurations`

The configurations of a document.

### `Configurations`

The configurations of a document.

| call | what it does |
|---|---|
| `.names()` | Every configuration name, in the order SOLIDWORKS lists them. |
| `.active` | [get] The active configuration's name, as a str. |
| `.activate(name)` | Make `name` the active configuration. |
| `.raw(name)` | The raw `IConfiguration` for `name`. |
| `.description_of(name)` | A configuration's description, as a str. May be empty. |
| `.comment_of(name)` | A configuration's comment, as a str. May be empty. |
| `.parent_of(name)` | The name of `name`'s parent configuration, or None. |
| `.children_of(name)` | The names of `name`'s derived configurations, sorted. |
| `.add(name, description='', comment='', parent=None, activate=False)` | Add a configuration. Returns its name, as a str. |

## `equations`

Equations and global variables.

### `Equations`

The equations of a document, in the order the dialog shows them.

| call | what it does |
|---|---|
| `.names()` | The names on the left of each equation, as a list of str. |
| `.globals()` | The global variables only, as a dict of name to value. |
| `.is_global(index)` | True if the equation at `index` is a global variable, as a bool. |
| `.value_of(name)` | What `name` evaluates to, as a float. |
| `.index_of(name)` | Where `name`'s equation is in the list, as an int, or None. |
| `.add(equation, at=None, solve=True)` | Add an equation. Returns its index, as an int. |
| `.evaluate()` | Re-evaluate every equation. Returns SOLIDWORKS' own code, an int. |

## `properties`

Custom properties, as a mapping.

### `Properties`

The custom properties of a document or one of its configurations.

| call | what it does |
|---|---|
| `.names()` | Every property name, in the order SOLIDWORKS stores them. |
| `.expression_of(name)` | The stored text, before evaluation, as a str. |
| `.of(configuration)` | The properties of one configuration, as another `Properties`. |

## `materials`

Reading and applying a material.

### `material_of(part, configuration=None)`

The material applied to one configuration, as a str.

### `database_of(part, configuration=None)`

Which database the applied material comes from, as a str.

### `set_material(part, name, configuration=None, database=None)`

Apply a material. Returns the name applied, as a str.

### `databases(app)`

The material database files SOLIDWORKS is searching, as a list of str.

### `database_names(app)`

The database names without their paths or extensions, as a list of str.

## `geometry`

Bodies, faces, edges and vertices.

### `Body`

One body: a solid, a surface or a wire.

| call | what it does |
|---|---|
| `.name` | [get] The body's name, as a str. |
| `.kind` | [get] What sort of body it is, as a str: `'solid'`, `'sheet'`... |
| `.faces` | [get] Every face, as a list of `Face`. |
| `.edges` | [get] Every edge, as a list of `Edge`. |
| `.vertices` | [get] Every vertex, as a list of `(x, y, z)` tuples in mm. |
| `.box` | [get] The bounding box in mm, as `(x1, y1, z1, x2, y2, z2)`. |
| `.size` | [get] How big the bounding box is, as `(x, y, z)` in mm, or None. |
| `.volume` | [get] The body's volume in mm3, as a float. |
| `.area` | [get] The body's surface area in mm2, as a float. |
| `.density` | [get] The density the mass is computed at, in kg/m3, as a float. |
| `.mass` | [get] The body's mass in grams, as a float. |
| `.mass_at(density)` | What the body would weigh in a material of `density`, in grams. |
| `.centre_of_mass` | [get] Where the centre of mass is, as `(x, y, z)` in mm. |
| `.center_of_mass` | [get] Where the centre of mass is, as `(x, y, z)` in mm. |
| `.material` | [get] The material's internal id name, as a str. |
| `.faces_of(kind)` | Every face of one sort, as a list of `Face`. |

### `Face`

One face of a body.

| call | what it does |
|---|---|
| `.kind` | [get] What surface it lies on, as a str: `'plane'`, `'cylinder'`... |
| `.area` | [get] The face's area in mm2, as a float. |
| `.normal` | [get] The outward normal, as an `(x, y, z)` unit vector, or None. |
| `.box` | [get] The face's bounding box in mm, as `(x1, y1, z1, x2, y2, z2)`. |
| `.edges` | [get] The edges around the face, as a list of `Edge`. |
| `.select(append=False)` | Select the face. Returns True. |

### `Edge`

One edge of a body.

| call | what it does |
|---|---|
| `.length` | [get] The edge's length in mm, as a float. |
| `.kind` | [get] What the edge is, as a str: `'line'`, `'circle'` or `'curve'`. |
| `.start` | [get] Where the edge starts, as `(x, y, z)` in mm, or None. |
| `.end` | [get] Where the edge ends, as `(x, y, z)` in mm, or None. |
| `.faces` | [get] The two faces that meet at this edge, as a list of `Face`. |
| `.select(append=False)` | Select the edge. Returns True. |

### `bodies_of(document, kind='solid', visible_only=False)`

Every body in a part, as a list of `Body`.

## `sheetmetal`

Thickness, bend radius and K-factor.

### `SheetMetal`

The sheet metal parameters of one feature.

| call | what it does |
|---|---|
| `.thickness` | [get] The material thickness in mm, as a float. |
| `.bend_radius` | [get] The default inside bend radius in mm, as a float. |
| `.k_factor` | [get] The K-factor, as a float. |
| `.bend_allowance` | [get] How the bend allowance is worked out, as a str. |
| `.relief_ratio` | [get] The auto relief ratio, as a float. |
| `.uses_gauge_table` | [get] True if a gauge table drives the thickness, as a bool. |
| `.definition` | [get] The raw `ISheetMetalFeatureData`. |
| `.as_dict()` | Every parameter at once, as a dict. |

### `features_of(part)`

The sheet metal features of a part, as a list of `SheetMetal`.

### `of(part)`

The part's sheet metal parameters, as a `SheetMetal`, or None.

### `is_sheet_metal(part)`

True if the part has a sheet metal feature, as a bool.

## `components`

The components of an assembly.

### `Component`

One instance in an assembly tree.

| call | what it does |
|---|---|
| `.name` | [get/set] The instance name, as a str: `'rail-2'`. |
| `.path` | [get] The file this instance comes from, as a str. |
| `.select_id` | [get] The name a selection call wants, as a str: `'rail-2@frame'`. |
| `.is_virtual` | [get] True for a component saved inside the assembly, as a bool. |
| `.document` | [get] The part or assembly behind this instance, or None. |
| `.configuration` | [get/set] Which configuration of the part this instance shows, as a str. |
| `.state` | [get] The suppression state, as one of the strings in `STATES`. |
| `.suppressed` | [get/set] Whether the instance is suppressed, as a bool. |
| `.suppress()` | Suppress the instance. Returns True. |
| `.resolve()` | Resolve the instance, loading its model fully. Returns True. |
| `.make_lightweight()` | Load the instance lightweight. Returns True. |
| `.visible` | [get/set] Whether the instance is shown, as a bool. |
| `.excluded_from_bom` | [get/set] Whether the instance is left out of the bill of materials, a bool. |
| `.fixed` | [get] True if the instance is fixed rather than floating, as a bool. |
| `.flexible` | [get] True if a sub-assembly is solved flexible rather than rigid. |
| `.position` | [get] Where the instance sits, as an `(x, y, z)` tuple in mm. |
| `.box` | [get] The bounding box in mm, as `(x1, y1, z1, x2, y2, z2)`. |
| `.children` | [get] The instances directly inside this one, as a list of `Component`. |
| `.select(append=False)` | Select the instance in the assembly. Returns True. |

### `Components`

The top-level components of an assembly.

| call | what it does |
|---|---|
| `.names()` | Every top-level instance name, as a list of str. |
| `.paths()` | The file behind every top-level instance, as a list of str. |
| `.all()` | Every component at every level, as a list of `Component`. |
| `.of_path(path)` | Every instance that comes from `path`, as a list of `Component`. |
| `.suppressed()` | The instances that are suppressed, as a list of `Component`. |
| `.add(path, at=(0.0, 0.0, 0.0), configuration=None)` | Insert a part or sub-assembly. Returns the new `Component`. |

## `drawing`

Sheets and views.

### `View`

One view on a sheet.

| call | what it does |
|---|---|
| `.name` | [get] The view's name, as a str: `'Drawing View1'`. |
| `.kind` | [get] What sort of view it is, as a str: `'standard'`, `'section'`... |
| `.model` | [get] The file the view is of, as a str. |
| `.position` | [get/set] Where the view sits on the sheet, as `(x, y)` in mm. |
| `.scale` | [get/set] The view's scale, as a float: 0.5 for 1:2. |
| `.uses_sheet_scale` | [get] True while the view follows the sheet's scale, as a bool. |
| `.dimension_count` | [get] How many dimensions are shown in the view, as an int. |
| `.dimensions` | [get] The dimensions shown in the view, as a list of raw objects. |
| `.activate()` | Make this the active view. Returns True. |

### `Views`

The views on the active sheet.

| call | what it does |
|---|---|
| `.names()` | Every view name on the active sheet, as a list of str. |
| `.add(model, view='Front', at=(100.0, 100.0), scale=None)` | Put a model view on the sheet. Returns the new `View`. |
| `.add_standard(model)` | Put front, top and right views on the sheet. Returns True. |
| `.of_kind(kind)` | Every view of one sort, as a list of `View`. |

### `Sheet`

One sheet of a drawing.

| call | what it does |
|---|---|
| `.name` | [get] The sheet's name, as a str: `'Sheet1'`. |
| `.scale` | [get/set] The sheet's scale, as a `(numerator, denominator)` tuple. |
| `.size` | [get] The paper size, as `(width, height)` in mm. |
| `.first_angle` | [get] True for first-angle projection, False for third-angle. |
| `.activate()` | Make this the active sheet. Returns True. |

### `Sheets`

The sheets of a drawing.

| call | what it does |
|---|---|
| `.names()` | Every sheet name, in order. As a list of str. |
| `.active` | [get] The sheet being shown, as a `Sheet`. |
| `.add(name=None, paper='A3', scale=(1, 1), first_angle=True)` | Add a sheet. Returns the new `Sheet`, which becomes the active one. |

## `export`

Writing a file out, and decoding what went wrong.

### `save_as(document, path, silent=True, copy=False, save_references=False)`

Save `document` to `path`. The extension picks the format.

### `save_error_names(code)`

The `swFileSaveError_e` flags set in `code`, as a list of str.

### `save_warning_names(code)`

The `swFileSaveWarning_e` flags set in `code`, as a list of str.

### `load_error_names(code)`

The `swFileLoadError_e` flags set in `code`, as a list of str.

### `load_warning_names(code)`

The `swFileLoadWarning_e` flags set in `code`, as a list of str.

### `format_of(path)`

A readable name for the format `path`'s extension implies, or None.

---

207 members across 15 modules.
