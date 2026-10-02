#!/usr/bin/env python3
"""List the processes the published reference manual documents, for the topics page.

Run from the repository root:  python3 scripts/make_processes.py

The question filter on the Find by topic page (docs/topics.md) also searches the
processes of the *ossia score* reference manual, so that a reader who types "LFO"
or "arpeggiator" finds the upstream page even when no lesson question names it.
This script writes that list to `_data/processes.yml`, which is committed, so the
build needs no network access. Re-run it when upstream publishes new pages.

The source is the live site's search index (`assets/js/search-data.json` under
`docs_baseurl`), not a local score-docs checkout: a checkout can be ahead of what
ossia.io serves, and on 2026-10-02 the `edu/docs` branch had 163 process pages of
which 66 returned 404. Each page's description is read from its own `<meta
name="description">`, which is the published front matter.

Each entry records:

  title        the page title, or the section title for a sub-process
  path         relative to docs_baseurl, so the link follows the placement variable
  description  the page's description, when it has its own
  in           for a sub-process, the title of the page that documents it
  units        the course units that link to that page (or that exact section)

A few pages document several processes, one per section (Audio utilities holds Gain,
Metronome, and Stereo merger); those sections become entries of their own. They are
listed in GROUP_PAGES by hand, because the index does not say which sections are
processes and which are "Usage" or "Related processes".
"""

from __future__ import annotations

import concurrent.futures
import datetime
import html
import json
import pathlib
import re
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONFIG = ROOT / "_config.yml"
UNITS = ROOT / "_data" / "units.yml"
LESSONS = ROOT / "docs" / "learn"
DATA = ROOT / "_data" / "processes.yml"

# Pages whose sections are processes in their own right, with the sections to skip.
GROUP_PAGES = {
    "processes/analysis.html": {"Analysis processes"},
    "processes/array-utilities.html": set(),
    "processes/audio-effects.html": {"Related processes"},
    "processes/audio-utilities.html": set(),
    "processes/control-utilities.html": set(),
    "processes/midi-utilities.html": {"Example: using the step sequencer to drive MIDI inputs"},
}

# jekyll-seo-tag falls back to the site's description when a page has none.
SITE_DESCRIPTION = "Online documentation for score software"


def docs_baseurl() -> str:
    m = re.search(r'^docs_baseurl:\s*"?([^"\s]+)"?', CONFIG.read_text(encoding="utf8"), re.M)
    if not m:
        raise SystemExit("_config.yml has no docs_baseurl")
    return m.group(1).rstrip("/")


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "score-learn make_processes.py"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf8")


def description(base: str, path: str) -> str:
    m = re.search(r'<meta name="description" content="([^"]*)"', fetch(f"{base}/{path}"))
    text = html.unescape(m.group(1)).strip() if m else ""
    return "" if text == SITE_DESCRIPTION else text


def unit_numbers() -> dict[str, str]:
    """slug -> unit number, from the single source of truth."""
    out: dict[str, str] = {}
    num = None
    for line in UNITS.read_text(encoding="utf8").splitlines():
        line = line.strip()
        if m := re.match(r'-?\s*num:\s*"?([^"\s]+)"?', line):
            num = m.group(1)
        elif (m := re.match(r"slug:\s*(\S+)", line)) and num:
            out[m.group(1)] = num
    return out


def lesson_links() -> dict[str, set[str]]:
    """'processes/x.html' or 'processes/x.html#y' -> unit numbers linking to it."""
    nums = unit_numbers()
    links: dict[str, set[str]] = {}
    pattern = re.compile(r"\{\{ ?site\.docs_baseurl ?\}\}/(processes/[^)\"\s]+)")
    for page in sorted(LESSONS.glob("*.md")):
        if page.stem not in nums:
            continue
        for target in pattern.findall(page.read_text(encoding="utf8")):
            links.setdefault(target, set()).add(nums[page.stem])
    return links


def unit_key(num: str) -> tuple[int, str]:
    # Lessons in number order, then milestones in theirs, as units.yml orders them.
    return (0, num) if num.isdigit() else (1, num)


def main() -> int:
    base = docs_baseurl()
    index = json.loads(fetch(f"{base}/assets/js/search-data.json"))

    pages: dict[str, str] = {}
    sections: dict[str, list[tuple[str, str]]] = {}
    for item in index.values():
        url = item["url"]
        if not url.startswith(f"{base}/processes/"):
            continue
        path, _, anchor = url[len(base) + 1:].partition("#")
        pages.setdefault(path, html.unescape(item["doc"]).strip())
        if anchor:
            sections.setdefault(path, []).append((anchor, html.unescape(item["title"]).strip()))

    missing = sorted(set(GROUP_PAGES) - set(pages))
    if missing:
        print("warning: GROUP_PAGES names pages the index no longer has: " + ", ".join(missing))

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        descriptions = dict(zip(pages, pool.map(lambda p: description(base, p), pages)))

    links = lesson_links()
    entries = []
    for path, title in pages.items():
        # "Array utilities" is described as "Array utilities", which adds nothing.
        text = descriptions[path] if descriptions[path].casefold() != title.casefold() else ""
        entries.append({"title": title, "path": path, "description": text,
                        "units": links.get(path, set())})
        skip = GROUP_PAGES.get(path)
        if skip is None:
            continue
        for anchor, section in sections.get(path, []):
            if section in skip or section == title:
                continue
            target = f"{path}#{anchor}"
            entries.append({"title": section, "path": target, "in": title,
                            "units": links.get(target, set())})
    entries.sort(key=lambda e: (e["title"].casefold(), e.get("in", "")))

    lines = [
        "# Generated by scripts/make_processes.py from the reference manual's live search",
        f"# index on {datetime.date.today().isoformat()}. Do not edit; re-run the script.",
        "",
    ]
    for e in entries:
        lines.append(f"- title: {json.dumps(e['title'], ensure_ascii=False)}")
        lines.append(f"  path: {json.dumps(e['path'])}")
        if e.get("description"):
            lines.append(f"  description: {json.dumps(e['description'], ensure_ascii=False)}")
        if e.get("in"):
            lines.append(f"  in: {json.dumps(e['in'], ensure_ascii=False)}")
        if e["units"]:
            nums = ", ".join(json.dumps(n) for n in sorted(e["units"], key=unit_key))
            lines.append(f"  units: [{nums}]")
    DATA.write_text("\n".join(lines) + "\n", encoding="utf8")

    subs = sum(1 for e in entries if e.get("in"))
    print(f"wrote {DATA.relative_to(ROOT)}: {len(pages)} pages and {subs} sub-processes")

    # A lesson link to a process page the live site does not serve is a 404 for readers.
    published = set(pages) | {f"{p}#{a}" for p, secs in sections.items() for a, _ in secs}
    dead = sorted(t for t in links if t not in published and t.split("#")[0] not in pages)
    for target in dead:
        print(f"note: {base}/{target} is not published yet; linked from units "
              + ", ".join(sorted(links[target], key=unit_key)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
