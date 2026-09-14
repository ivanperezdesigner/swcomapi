"""Find out what the API has, without a browser and without SOLIDWORKS.

Run it with the venv's Python::

    .venv\\Scripts\\python examples\\06_explore_the_api.py

Nothing here connects to anything: the index, the enumerations and the
documentation links are plain data that ship with the package, so this runs on
a machine with no SOLIDWORKS on it at all.

Output on the machine this was written on::

    SOLIDWORKS 2026 API index
      10 type libraries
      729 interfaces, 19874 members
      17097 members with a description
      1662 C++-only twins
      1434 enumerations, 14889 constants

    Interfaces with "MassProp" in the name:
      ICWMassPropertiesManager, IMassProperty, IMassProperty2, IMassPropertyOverrideOptions

    20 members match GetMassProperties. The first four:
      IBody.GetMassProperties, IBody2.GetMassProperties,
      IModelDoc.GetMassProperties, IModelDoc2.GetMassProperties

    IModelDocExtension.SaveAs3(Name, Version, Options, ExportData, ...
      ...

    swDocumentTypes_e has 8 constants; swDocPART is 1

    Enumerations with "SaveAs" in the name:
      swEdrawingSaveAsOption_e, swSaveAsOptions_e, swSaveAsVersion_e, ...

    982 members write into their parameters. OpenDoc6's are:
      Errors at 4 (inout), Warnings at 5 (inout)
"""

import swcomapi as swc


def main():
    print(swc.summary())

    print()
    print('Interfaces with "MassProp" in the name:')
    print(f"  {', '.join(swc.find_interface('MassProp'))}")

    found = swc.find("GetMassProperties")
    print()
    print(f"{len(found)} members match GetMassProperties. The first four:")
    print(f"  {', '.join(found[:4])}")

    print()
    print(swc.describe("IModelDocExtension.SaveAs3"))

    from swcomapi import enums

    print()
    print(
        f"swDocumentTypes_e has {len(enums.swDocumentTypes_e)} constants; "
        f"swDocPART is {int(enums.swDocumentTypes_e.swDocPART)}"
    )

    print()
    print('Enumerations with "SaveAs" in the name:')
    print(f"  {', '.join(enums.find('SaveAs'))}")

    from swcomapi import signatures

    outputs = signatures.outputs_of("OpenDoc6")
    print()
    print(
        f"{len(signatures.members_with_outputs())} members write into their "
        f"parameters. OpenDoc6's are:"
    )
    print(
        "  "
        + ", ".join(
            f"{name} at {index} ({direction})"
            for index, name, _, direction in outputs
        )
    )

    print()
    print("The official page for any of it:")
    print(f"  {swc.doclink('IModelDocExtension', 'SaveAs3')}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
