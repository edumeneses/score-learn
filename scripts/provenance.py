#!/usr/bin/env python3
"""Which document each raw capture shows, and whether it has changed since.

A figure is a picture of a document, so it goes stale the moment the document
changes, and nothing about the PNG says so. On 2026-09-24 the corrected
`lesson-00.score` silently invalidated five figures that crop its capture; they
were found by eye. This file makes that a checked fact instead.

`figures/provenance.json` maps each raw capture, relative to `figures/`, to:

  document   repository-relative path of the document open when it was shot,
             or null for a figure with no document (the start screen)
  sha256     the document's hash at capture time
  role       how the figure uses the document:
               shown       the document as saved; the figure links it
               base        the document plus unsaved additions; no link
               background  only visible behind a menu or a dialog; no link
  captured   the date
  note       optional; why a changed document was accepted, for instance

`capture.py shot` writes the entry whenever it saves under `figures/raw/`, and
`check_lessons.py` compares every entry with the document on disk: a changed
document fails the check when its role is `shown` and warns otherwise.

    python3 scripts/provenance.py status
    python3 scripts/provenance.py accept raw/raw-09-01.png --note "only the device gained haze, not shown"
    python3 scripts/provenance.py set raw/raw-06-01.png library/learn/.../lesson-00.score --role background
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIGURES = ROOT / "figures"
PROVENANCE = FIGURES / "provenance.json"
ROLES = ("shown", "base", "background")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load() -> dict:
    if not PROVENANCE.exists():
        return {}
    return json.loads(PROVENANCE.read_text())


def save(data: dict) -> None:
    ordered = {k: data[k] for k in sorted(data)}
    PROVENANCE.write_text(json.dumps(ordered, indent=2) + "\n")


def raw_key(path: str | Path) -> str:
    """`figures/raw/x.png`, an absolute path, or `raw/x.png`, as `raw/x.png`."""
    p = Path(path)
    if p.is_absolute():
        p = p.resolve().relative_to(FIGURES)
    elif p.parts[:1] == ("figures",):
        p = Path(*p.parts[1:])
    return p.as_posix()


def doc_key(path: str | Path | None) -> str | None:
    """A document path relative to the repository, or absolute if outside it."""
    if path is None:
        return None
    p = Path(path)
    p = p.resolve() if p.is_absolute() else (ROOT / p).resolve()
    try:
        return p.relative_to(ROOT).as_posix()
    except ValueError:
        return p.as_posix()


def record(raw: str | Path, document: str | Path | None, role: str,
           note: str | None = None) -> dict:
    """Write or replace one entry; returns it."""
    if role not in ROLES:
        raise SystemExit(f"role must be one of {ROLES}, not {role!r}")
    data = load()
    doc = doc_key(document)
    entry = {
        "document": doc,
        "sha256": sha256(ROOT / doc) if doc and (ROOT / doc).exists() else None,
        "role": role,
        "captured": datetime.date.today().isoformat(),
    }
    if note:
        entry["note"] = note
    data[raw_key(raw)] = entry
    save(data)
    return entry


def state(entry: dict) -> str:
    """fresh, changed, missing, or none."""
    doc = entry.get("document")
    if not doc:
        return "none"
    path = ROOT / doc
    if not path.exists():
        return "missing"
    return "fresh" if sha256(path) == entry.get("sha256") else "changed"


def cmd_status(args: argparse.Namespace) -> int:
    data = load()
    bad = 0
    for raw, entry in data.items():
        s = state(entry)
        bad += s in ("changed", "missing")
        if args.all or s in ("changed", "missing"):
            print(f"{s:8} {entry['role']:10} {raw:24} {entry.get('document')}")
    print(f"{len(data)} captures, {bad} whose document changed or is missing")
    return 0


def cmd_accept(args: argparse.Namespace) -> int:
    """Re-hash the document for a capture a person has checked still matches."""
    data = load()
    key = raw_key(args.raw)
    if key not in data:
        raise SystemExit(f"{key} has no provenance entry; use `set`")
    entry = data[key]
    if not entry.get("document"):
        raise SystemExit(f"{key} records no document")
    entry["sha256"] = sha256(ROOT / entry["document"])
    entry["note"] = f"{datetime.date.today().isoformat()}: accepted, {args.note}"
    save(data)
    print(f"accepted {key}: {entry['note']}")
    return 0


def cmd_set(args: argparse.Namespace) -> int:
    doc = None if args.document in ("none", "null") else args.document
    entry = record(args.raw, doc, args.role, args.note)
    print(f"{raw_key(args.raw)}: {entry}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("status", help="list captures whose document changed")
    p.add_argument("--all", action="store_true", help="list every capture")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("accept", help="mark a changed document as still matching")
    p.add_argument("raw")
    p.add_argument("--note", required=True, help="what changed, and why it is not visible")
    p.set_defaults(func=cmd_accept)

    p = sub.add_parser("set", help="write an entry by hand")
    p.add_argument("raw")
    p.add_argument("document", help="path, or none")
    p.add_argument("--role", default="shown", choices=ROLES)
    p.add_argument("--note", default=None)
    p.set_defaults(func=cmd_set)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
