"""Command line for the generator tools.

    python -m swcomapi.tools survey      # what is installed, and how big it is
    python -m swcomapi.tools survey -v   # plus the per-interface breakdown
    python -m swcomapi.tools generate    # rebuild swcomapi/generated
"""

import argparse
import sys

from . import generate as generate_module
from . import install, tlb


def main(argv=None):
    parser = argparse.ArgumentParser(prog="python -m swcomapi.tools")
    sub = parser.add_subparsers(dest="command", required=True)

    survey = sub.add_parser("survey", help="count what the installed type libraries contain")
    survey.add_argument(
        "-d",
        "--dir",
        dest="directory",
        help="the SOLIDWORKS directory; defaults to the registered install",
    )
    survey.add_argument(
        "--core-only",
        action="store_true",
        help="only sldworks.tlb and swconst.tlb, skipping the add-in libraries",
    )
    survey.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="also list the ten largest interfaces",
    )

    gen = sub.add_parser("generate", help="rebuild swcomapi/generated from the type libraries")
    gen.add_argument(
        "-d",
        "--dir",
        dest="directory",
        help="the SOLIDWORKS directory; defaults to the registered install",
    )
    gen.add_argument(
        "-o",
        "--out",
        dest="root",
        help="the swcomapi package directory to write into; defaults to this one",
    )
    gen.add_argument(
        "--core-only",
        action="store_true",
        help="only sldworks.tlb and swconst.tlb, skipping the add-in libraries",
    )

    args = parser.parse_args(argv)
    if args.command == "survey":
        return _survey(args)
    if args.command == "generate":
        return _generate(args)
    return 1


def _generate(args):
    try:
        directory = args.directory or install.solidworks_dir()
    except install.InstallNotFoundError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    paths = install.library_paths(directory, include_addins=not args.core_only)
    print(f"reading {len(paths)} type libraries from {directory}")

    try:
        api, written = generate_module.run(paths, args.root)
    except generate_module.GenerationError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    numbers = generate_module.counts(api)
    print(f"SOLIDWORKS {api['year']}")
    for key in ("libraries", "enums", "constants", "interfaces", "members",
                "documented", "properties", "with_out", "com_only"):
        print(f"  {key:<12} {numbers[key]:>7}")

    if api["failed"]:
        print()
        print("not loadable on this machine:")
        for filename, error in api["failed"]:
            print(f"  {filename}: {error}")

    print()
    print("written:")
    for path, size in written:
        print(f"  {size/1024:>8.0f} KB  {path}")
    return 0


def _survey(args):
    try:
        directory = args.directory or install.solidworks_dir()
    except install.InstallNotFoundError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    paths = install.library_paths(directory, include_addins=not args.core_only)
    if not paths:
        print(f"error: no type libraries found in {directory!r}", file=sys.stderr)
        return 2

    print(f"SOLIDWORKS directory: {directory}")
    print(f"type libraries found: {len(paths)}")
    print()

    header = (
        f"{'library':<22} {'enums':>6} {'members':>8} {'ifaces':>7} "
        f"{'API':>7} {'doc''d':>6} {'props':>6} {'[out]':>6} {'C++':>5}"
    )
    print(header)
    print("-" * len(header))

    rows = tlb.survey(paths)
    totals = {}
    failures = []
    for row in rows:
        name = row["path"].rsplit("\\", 1)[-1]
        if "error" in row:
            failures.append((name, row["error"]))
            continue
        print(
            f"{name:<22} {row['enums']:>6} {row['enum_members']:>8} "
            f"{row['interfaces']:>7} {row['members']:>7} {row['documented']:>6} "
            f"{row['properties']:>6} {row['with_out']:>6} {row['com_only']:>5}"
        )
        for key in ("enums", "enum_members", "interfaces", "members", "documented",
                    "properties", "with_out", "com_only"):
            totals[key] = totals.get(key, 0) + row[key]

    print("-" * len(header))
    print(
        f"{'TOTAL':<22} {totals.get('enums', 0):>6} {totals.get('enum_members', 0):>8} "
        f"{totals.get('interfaces', 0):>7} {totals.get('members', 0):>7} "
        f"{totals.get('documented', 0):>6} {totals.get('properties', 0):>6} "
        f"{totals.get('with_out', 0):>6} {totals.get('com_only', 0):>5}"
    )

    members = max(totals.get("members", 0), 1)
    print()
    print(f"prose coverage : {totals.get('documented', 0)}/{members} = "
          f"{100 * totals.get('documented', 0) / members:.1f}% of members carry a description")
    print(f"[out] burden   : {totals.get('with_out', 0)}/{members} = "
          f"{100 * totals.get('with_out', 0) / members:.1f}% of members have an [out] parameter")

    if failures:
        print()
        print("libraries that would not load:")
        for name, error in failures:
            print(f"  {name}: {error}")

    if args.verbose:
        _largest_interfaces(paths)

    return 0


def _largest_interfaces(paths):
    interfaces = []
    for path in paths:
        try:
            lib = tlb.read_library(path)
        except Exception:
            continue
        for iface in lib["interfaces"]:
            interfaces.append((len(iface["members"]), iface["name"], lib["name"]))
    interfaces.sort(reverse=True)

    print()
    print("largest interfaces:")
    for count, name, lib in interfaces[:10]:
        print(f"  {count:>5}  {name} ({lib})")


if __name__ == "__main__":
    raise SystemExit(main())
