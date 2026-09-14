"""Connect to SOLIDWORKS and report what you are talking to.

Run it with the venv's Python::

    .venv\\Scripts\\python examples\\01_connect.py

Output on the machine this was written on, with SOLIDWORKS 2026 SP3 open::

    Connected.
      version      : SOLIDWORKS 2026 SP3 (34.3.0)
      year         : 2026
      service pack : 3
      revision     : 34.3.0
      process id   : 24628        (different on every launch)
      visible      : True

      base version : sw2026_SP03
      current      : d260519.003
      hot fixes    : - Hotfix: #HF-1530816 #HF-1531787 ...

    Reaching past the wrapper, straight at ISldWorks:
      app.com.RevisionNumber = 34.3.0

Nothing here opens or changes a document, so it is safe to run against a
session you are working in.
"""

import swcomapi as swc


def main():
    # attach() uses the session already on screen and raises if there is none.
    # connect() would start one instead. visible=None leaves the window state
    # exactly as it was found, which is what you want when a human is using it.
    try:
        app = swc.attach(visible=None)
    except swc.SwNotRunningError as exc:
        print(exc)
        print("\nStart SOLIDWORKS, or swap attach() for connect() to have one started.")
        return 1

    print("Connected.")
    print(f"  version      : {app.version}")
    print(f"  year         : {app.year}")
    print(f"  service pack : {app.service_pack}")
    print(f"  revision     : {app.revision_number}")
    print(f"  process id   : {app.process_id}")
    print(f"  visible      : {app.visible}")

    # GetBuildNumbers2 is the first real [out] parameter trap in the API: all
    # three of its arguments are written into, and the method returns nothing.
    base, current, hotfixes = app.build_numbers
    print()
    print(f"  base version : {base}")
    print(f"  current      : {current}")
    print(f"  hot fixes    : {hotfixes.strip() or '(none)'}")

    # The escape hatch: anything the wrapper does not cover yet is one
    # attribute away on .com.
    print()
    print("Reaching past the wrapper, straight at ISldWorks:")
    print(f"  app.com.RevisionNumber = {app.com.RevisionNumber}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
