#!/usr/bin/env python3
"""Structural checks for the Learn score course.

Run from the repository root:  python3 scripts/check_lessons.py

Enforces the rules the course commits to, so that a drifting lesson fails the
build rather than reaching a reader:

  1. required front matter keys are present;
  2. the reading budget holds: body text between MIN_WORDS and MAX_WORDS, which
     corresponds to 10 to 15 minutes at 180 to 200 words per minute. Headings
     are not counted, as in check_voice.py, so that giving each concept its own
     linkable heading does not spend the budget;
  3. every declared score_file exists under library/learn/ (or is `none`);
  4. permalink matches the file name, since published permalinks are contractual;
  5. score_version matches the pinned site version;
  6. a checks/ note exists for every lesson, listing what to re-verify when the
     pinned score version changes;
  7. every page corresponds to a unit in _data/units.yml, is marked
     `written: true` there, declares that unit's number in `unit`, orders itself
     by the unit's position in that file, and carries its read and practice
     budgets. Position rather than number, because a milestone is `P1`, which
     has no place in a numeric sort;
  8. every internal /learn/<slug>.html link points at a slug that exists in
     _data/units.yml, so a forward reference to a lesson not yet written is
     allowed while a reference to a lesson that will never exist is not;
  9. _data/topics.yml, which drives the knowledge-base page, names only units
     that exist, every anchor it links to is a heading on that unit's page, and
     every written unit is reachable from at least one topic;
 10. every `{{ site.scores }}/...` link, which is how a figure downloads the
     document it shows, names a file that exists under library/learn/.

Exit code is non-zero if any check fails.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LESSONS = ROOT / "docs" / "learn"
LIBRARY = ROOT / "library" / "learn"
CHECKS = ROOT / "checks"
UNITS = ROOT / "_data" / "units.yml"
TOPICS = ROOT / "_data" / "topics.yml"

MIN_WORDS = 1400
MAX_WORDS = 1900
PINNED_VERSION = "3.8.2"

REQUIRED_KEYS = (
    "layout",
    "title",
    "description",
    "parent",
    "nav_order",
    "unit",
    "permalink",
    "score_version",
    "reading_time",
    "practice_time",
    "score_file",
)

FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
HTML_COMMENT = re.compile(r"<!--.*?-->", re.S)
LIQUID_TAG = re.compile(r"\{%.*?%\}", re.S)
LIQUID_VAR = re.compile(r"\{\{.*?\}\}")
MD_LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
LESSON_LINK = re.compile(r"/learn/([a-z0-9][a-z0-9-]*)\.html")
SCORES_LINK = re.compile(r"\{\{ site\.scores \}\}/([^)\s]+)")


def load_units() -> dict[str, dict[str, str]]:
    """Minimal reader for the deliberately flat _data/units.yml.

    Avoids a PyYAML dependency so the check runs on a bare Python 3 in CI. The
    file is machine-written and kept flat for exactly this reason.
    """
    units: dict[str, dict[str, str]] = {}
    current: dict[str, str] | None = None
    for raw in UNITS.read_text(encoding="utf8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("- "):
            current = {}
            line = line[2:]
        if current is None or ":" not in line:
            continue
        key, _, value = line.partition(":")
        current[key.strip()] = value.strip().strip('"').strip("'")
        if "slug" in current:
            current.setdefault("_index", len(units))
            units[current["slug"]] = current
    return units


def parse_front_matter(text: str) -> dict[str, str]:
    match = FRONT_MATTER.match(text)
    if not match:
        return {}
    out: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, _, value = line.partition(":")
        out[key.strip()] = value.strip().strip('"').strip("'")
    return out


def body_words(text: str) -> int:
    """Word count of prose a reader actually reads."""
    body = FRONT_MATTER.sub("", text)
    body = HTML_COMMENT.sub("", body)
    body = LIQUID_TAG.sub("", body)
    body = LIQUID_VAR.sub("", body)
    body = re.sub(r"\{:[^}]*\}", "", body)   # kramdown attribute lists, e.g. a link's title
    body = MD_LINK.sub(r"\1", body)          # keep link text, drop targets
    body = re.sub(r"```.*?```", "", body, flags=re.S)
    body = re.sub(r"^#{1,6}\s.*$", "", body, flags=re.M)
    body = re.sub(r"[|>#*`_{}-]", " ", body)
    return len([w for w in body.split() if any(c.isalnum() for c in w)])


HEADING = re.compile(r"^#{1,6}\s+(.*?)\s*#*\s*$", re.M)
EXPLICIT_ID = re.compile(r"^\{:\s*#([\w-]+)\s*\}", re.M)


def heading_ids(text: str) -> set[str]:
    """Anchor ids kramdown's GFM parser gives a page's headings.

    Mirrors generate_gfm_header_id: lowercase, drop every character that is not
    a word character, a hyphen, or a space, then turn spaces into hyphens, with
    -1, -2 appended to repeats. Markup is stripped first because the id is built
    from the heading's rendered text, not its source.
    """
    body = FRONT_MATTER.sub("", text)
    body = re.sub(r"```.*?```", "", body, flags=re.S)
    ids: set[str] = set(EXPLICIT_ID.findall(body))
    seen: dict[str, int] = {}
    for raw in HEADING.findall(body):
        plain = MD_LINK.sub(r"\1", raw)
        plain = re.sub(r"[*`_]", "", plain)
        base = re.sub(r"[^\w\- ]", "", plain.lower()).replace(" ", "-")
        n = seen.get(base, 0)
        ids.add(base if n == 0 else f"{base}-{n}")
        seen[base] = n + 1
    return ids


def load_topics() -> list[dict]:
    """Minimal reader for _data/topics.yml, kept flat for the same reason as units.yml.

    Topics are `- id:` entries with `title` and `intro`; each has a `questions:`
    list of `- q:` entries carrying `unit`, an optional `anchor`, and an optional
    inline list `see: ["07", "15"]`.
    """
    topics: list[dict] = []
    question: dict | None = None
    for raw in TOPICS.read_text(encoding="utf8").splitlines():
        line = raw.split(" #", 1)[0].rstrip() if not raw.lstrip().startswith("- q:") else raw.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^- id:\s*(\S+)$", line)
        if m:
            topics.append({"id": m.group(1), "questions": []})
            question = None
            continue
        m = re.match(r"^\s+- q:\s*(.+)$", line)
        if m:
            question = {"q": m.group(1).strip().strip('"'), "see": []}
            topics[-1]["questions"].append(question)
            continue
        m = re.match(r"^\s+(\w+):\s*(.*)$", line)
        if m and topics and m.group(1) != "questions":
            key, value = m.group(1), m.group(2).strip()
            target = question if question is not None and key in ("unit", "anchor", "see") else topics[-1]
            if key == "see":
                target["see"] = re.findall(r'"([^"]+)"', value)
            else:
                target[key] = value.strip('"').strip("'")
    return topics


def check_topics(units: dict[str, dict[str, str]], pages: list[Path]) -> list[str]:
    if not TOPICS.exists():
        return [f"{TOPICS.relative_to(ROOT)} is missing"]
    failures: list[str] = []
    by_num = {u["num"]: slug for slug, u in units.items()}
    ids_by_slug = {p.stem: heading_ids(p.read_text(encoding="utf8")) for p in pages}
    reached: set[str] = set()
    seen_topics: set[str] = set()
    for topic in load_topics():
        tid = topic["id"]
        if tid in seen_topics:
            failures.append(f"topics.yml: topic id {tid!r} is used twice")
        seen_topics.add(tid)
        for key in ("title", "intro"):
            if not topic.get(key):
                failures.append(f"topics.yml: topic {tid!r} has no {key}")
        if not topic["questions"]:
            failures.append(f"topics.yml: topic {tid!r} has no questions")
        for q in topic["questions"]:
            for num in [q.get("unit", "")] + q["see"]:
                slug = by_num.get(num)
                if slug is None:
                    failures.append(f"topics.yml: {tid}: {q['q']!r} names unit {num!r}, not in units.yml")
                else:
                    reached.add(slug)
            slug = by_num.get(q.get("unit", ""))
            anchor = q.get("anchor")
            if slug and anchor and anchor not in ids_by_slug.get(slug, set()):
                failures.append(
                    f"topics.yml: {tid}: {q['q']!r} links to #{anchor}, "
                    f"which is not a heading in {slug}.md"
                )
    for page in pages:
        if page.stem in units and page.stem not in reached:
            failures.append(f"topics.yml: {page.stem} is not reachable from any topic")
    return failures


def main() -> int:
    failures: list[str] = []
    units = load_units()
    if not units:
        print(f"could not read any unit from {UNITS}")
        return 1

    pages = sorted(p for p in LESSONS.glob("*.md") if p.name != "learn.md")
    if not pages:
        print("no lesson pages found under docs/learn/")
        return 1

    for page in pages:
        rel = page.relative_to(ROOT)
        text = page.read_text(encoding="utf8")
        fm = parse_front_matter(text)

        if not fm:
            failures.append(f"{rel}: no front matter")
            continue

        for key in REQUIRED_KEYS:
            if key not in fm:
                failures.append(f"{rel}: missing front matter key `{key}`")

        words = body_words(text)
        if not MIN_WORDS <= words <= MAX_WORDS:
            failures.append(
                f"{rel}: body is {words} words, outside the "
                f"{MIN_WORDS}-{MAX_WORDS} reading budget"
            )

        stem = page.stem
        expected_permalink = f"/learn/{stem}.html"
        if fm.get("permalink") != expected_permalink:
            failures.append(
                f"{rel}: permalink is {fm.get('permalink')!r}, "
                f"expected {expected_permalink!r}"
            )

        if fm.get("score_version") != PINNED_VERSION:
            failures.append(
                f"{rel}: score_version is {fm.get('score_version')!r}, "
                f"pinned version is {PINNED_VERSION!r}"
            )

        score_file = fm.get("score_file", "")
        if score_file and score_file != "none":
            if not (LIBRARY / score_file).exists():
                failures.append(f"{rel}: score_file {score_file!r} missing under library/learn/")

        if not (CHECKS / f"{stem}.md").exists():
            failures.append(f"{rel}: no re-verification note at checks/{stem}.md")

        unit = units.get(stem)
        if unit is None:
            failures.append(f"{rel}: no unit with slug {stem!r} in _data/units.yml")
        else:
            if unit.get("written") != "true":
                failures.append(
                    f"{rel}: page exists but _data/units.yml marks it `written: false`"
                )
            if fm.get("unit") != unit.get("num"):
                failures.append(
                    f"{rel}: front matter unit is {fm.get('unit')!r}, "
                    f"_data/units.yml says {unit.get('num')!r}"
                )
            expected_order = str(unit["_index"])
            if fm.get("nav_order") != expected_order:
                failures.append(
                    f"{rel}: nav_order is {fm.get('nav_order')!r}, "
                    f"expected {expected_order!r} (position in _data/units.yml)"
                )
            expected_read = f"{unit.get('read')} min"
            if fm.get("reading_time") != expected_read:
                failures.append(
                    f"{rel}: reading_time is {fm.get('reading_time')!r}, "
                    f"_data/units.yml says {expected_read!r}"
                )
            practice = unit.get("practice", "0")
            expected_practice = "none" if practice == "0" else f"{practice} min"
            if fm.get("practice_time") != expected_practice:
                failures.append(
                    f"{rel}: practice_time is {fm.get('practice_time')!r}, "
                    f"_data/units.yml says {expected_practice!r}"
                )

        for slug in set(LESSON_LINK.findall(text)):
            if slug not in units:
                failures.append(
                    f"{rel}: links to /learn/{slug}.html, which is not a unit "
                    f"in _data/units.yml"
                )

        for target in set(SCORES_LINK.findall(text)):
            if not (LIBRARY / target).exists():
                failures.append(f"{rel}: links to {target!r}, missing under library/learn/")

        print(f"{rel}: {words} words")

    failures.extend(check_topics(units, pages))

    if failures:
        print("\nFAILED")
        for line in failures:
            print(f"  {line}")
        return 1

    print(f"\nOK: {len(pages)} lesson page(s) pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
