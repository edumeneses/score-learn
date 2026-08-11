#!/usr/bin/env python3
"""Build the downloads page and the archive of every example document.

Run from the repository root:  python3 scripts/make_downloads.py

The lesson documents are the most reusable thing the course produces, so they are
published as files rather than only described in prose. This script does two
things and is safe to re-run:

  1. writes `library/learn/all-scores.zip`, every document and its media;
  2. writes `docs/downloads.md`, a page listing each unit's files with sizes and
     a link back to the lesson that uses them.

Both outputs are committed, so the published site needs no plugin to produce
them and the archive is reproducible from the repository.
"""

from __future__ import annotations

import pathlib
import re
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
LIBRARY = ROOT / "library" / "learn"
UNITS = ROOT / "_data" / "units.yml"
ARCHIVE = LIBRARY / "all-scores.zip"
PAGE = ROOT / "docs" / "downloads.md"

KIND = {
    ".score": "score document",
    ".pd": "Pure Data patch",
    ".wav": "audio",
    ".mp4": "video",
    ".avi": "video",
    ".mid": "MIDI",
}


def human(size: int) -> str:
    for unit in ("B", "kB", "MB"):
        if size < 1024 or unit == "MB":
            return f"{size:.0f} {unit}" if unit == "B" else f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} MB"


def units() -> dict[str, tuple[str, str]]:
    """slug -> (unit number, title), read from the single source of truth."""
    out, num, title = {}, None, None
    for line in UNITS.read_text(encoding="utf8").splitlines():
        line = line.strip()
        if m := re.match(r'-?\s*num:\s*"?([^"\s]+)"?', line):
            num = m.group(1)
        elif m := re.match(r'title:\s*"?(.+?)"?$', line):
            title = m.group(1)
        elif m := re.match(r"slug:\s*(\S+)", line):
            out[m.group(1)] = (num or "?", title or m.group(1))
    return out


def main() -> int:
    meta = units()
    dirs = sorted(d for d in LIBRARY.iterdir() if d.is_dir())

    if ARCHIVE.exists():
        ARCHIVE.unlink()
    with zipfile.ZipFile(ARCHIVE, "w", zipfile.ZIP_DEFLATED) as zf:
        for d in dirs:
            for f in sorted(d.rglob("*")):
                if f.is_file():
                    zf.write(f, f.relative_to(LIBRARY))
    total = ARCHIVE.stat().st_size

    rows = []
    for d in dirs:
        num, title = meta.get(d.name, ("?", d.name))
        files = [f for f in sorted(d.rglob("*")) if f.is_file()]
        items = " · ".join(
            f"[{f.name}]({{{{ site.baseurl }}}}/library/learn/{d.name}/{f.name})"
            f" <small>({KIND.get(f.suffix, 'file')}, {human(f.stat().st_size)})</small>"
            for f in files
        )
        lesson = f"[{num}]({{{{ site.baseurl }}}}/learn/{d.name}.html)"
        rows.append(f"| {lesson} | {title} | {items} |")

    PAGE.write_text(
        "---\n"
        "layout: default\n"
        "title: Downloads\n"
        "description: \"Every example document the course ships, individually or as one archive.\"\n"
        "nav_order: 2\n"
        "permalink: /downloads\n"
        "---\n\n"
        "# Downloads\n\n"
        "*ossia score* {{ site.score_version }}\n"
        "{: .label .label-green}\n\n"
        "Every document the course ships, with the media it references. They open in "
        "*score* {{ site.score_version }}; older builds may refuse them, as "
        "[Lesson 05]({{ site.baseurl }}/learn/05-saving-and-reopening.html) explains.\n\n"
        f"[Download all of it]({{{{ site.baseurl }}}}/library/learn/all-scores.zip)"
        f" <small>({human(total)})</small>\n"
        "{: .btn .btn-primary }\n\n"
        "Keep each unit's folder together: the documents reference their media by a "
        "project-relative path, so a `.score` moved away from its folder opens with the "
        "media missing.\n\n"
        "| Unit | Title | Files |\n|---|---|---|\n" + "\n".join(rows) + "\n\n"
        "## How these were made\n\n"
        "Most are generated rather than hand-built: `scripts/mkscore.py` writes them as "
        "JSON, which is what a `.score` file is. That is what makes them reproducible "
        "when the pinned version changes, and it is why the figures in this course can be "
        "re-shot by script. The audio excerpts come from the Citizen DJ packages, "
        "installable through *score*'s package manager and free to use; the video clips "
        "are generated with `ffmpeg`, with the commands printed in "
        "[Lesson 25]({{ site.baseurl }}/learn/25-video-pipeline.html).\n",
        encoding="utf8",
    )
    print(f"wrote {ARCHIVE.relative_to(ROOT)} ({human(total)})")
    print(f"wrote {PAGE.relative_to(ROOT)} ({len(rows)} units)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
