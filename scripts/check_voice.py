#!/usr/bin/env python3
"""Measure how far a lesson's prose is from Edu's voice.

The avoid-list in CLAUDE.md is easy to satisfy while missing the voice entirely; the
2026-09 audit found every lesson doing exactly that. This tool measures the positive
habits instead, per page, against the targets the rewrite pass used. It is advisory:
it prints a table and exits 0 unless --strict is given, because a quoted complaint or a
technical phrase ("a trigger that is never satisfied") can legitimately trip a counter.

Usage:
    python3 scripts/check_voice.py            # every lesson page
    python3 scripts/check_voice.py 07 p3      # by unit number
    python3 scripts/check_voice.py --strict   # exit 1 if any page misses a target
    python3 scripts/check_voice.py 20 --show  # print the offending sentences
"""
from __future__ import annotations

import argparse
import collections
import re
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LESSONS = ROOT / "docs" / "learn"

TARGETS = {
    "mean_len": (">=", 20.0, "mean words per sentence"),
    "lt10_pct": ("<=", 15.0, "% of sentences under 10 words"),
    "ge25_pct": (">=", 35.0, "% of sentences of 25 words or more"),
    "connectors": (">=", 6, "sentence-initial logical connectors"),
    "rather_than": ("<=", 3, "'rather than'"),
    "comma_not": ("<=", 2, "', not X' contrasts"),
    "absolutist": ("<=", 4, "nothing/everything/anything/nobody/never"),
    "exactly": ("<=", 1, "'exactly'"),
    "deliberately": ("<=", 1, "'deliberately'"),
    "worth": ("<=", 2, "'worth'"),
    "moral": ("<=", 0, "discipline/habit/craft/honest(ly)/temptation/hygiene/taste"),
    "colon_lead": ("<=", 3, "colon after a lead of five words or fewer"),
    "num_open": ("<=", 2, "sentences opening One/Two/Three..."),
    "dashes": ("<=", 0, "em or en dashes"),
    "banned": ("<=", 0, "sentence-initial Also/Plus/Besides/On top of"),
}

CONNECTORS = re.compile(
    r"^(However|In contrast|Furthermore|Moreover|In other words|Conversely|"
    r"Nevertheless|Additionally|Simultaneously|Therefore|Consequently)\b"
)
BANNED = re.compile(r"^(Also|Plus|Besides|On top of (that|this))\b")
ABSOLUTIST = re.compile(r"\b(nothing|everything|anything|nobody|never)\b", re.I)
MORAL = re.compile(r"\b(discipline|habit|craft|honest|honestly|temptation|hygiene|taste)\b", re.I)
DASH = re.compile(r"[—–]")
NUM_OPEN = re.compile(r"^(One|Two|Three|Four|Five|Six)\b")


def body(text: str) -> str:
    """Prose a reader actually reads: no front matter, code, tables, headings, or markup."""
    text = re.sub(r"\A---.*?---\s*", "", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"\{%.*?%\}", "", text, flags=re.S)
    text = re.sub(r"\{\{.*?\}\}", "", text, flags=re.S)
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    lines = []
    for line in text.splitlines():
        s = line.strip()
        if not s or s[0] in "#|<" or s.startswith("---"):
            continue
        s = re.sub(r"^>\s?", "", s)
        s = re.sub(r"^(\d+\.|[-*])\s+", "", s)
        s = re.sub(r"`[^`]*`", "CODE", s)
        lines.append(s.replace("**", "").replace("*", ""))
    return "\n".join(lines)


def sentences(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\b(e\.g|i\.e|etc|vs|cf|Fig|fig|No)\.", lambda m: m.group(0).replace(".", "\x00"), text)
    text = re.sub(r"(\d)\.(\d)", lambda m: m.group(1) + "\x00" + m.group(2), text)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"'(])", text)
    return [p.replace("\x00", ".").strip() for p in parts if len(p.split()) >= 2]


def measure(path: Path, show: bool = False) -> dict:
    sents = sentences(body(path.read_text(encoding="utf8")))
    lens = [len(s.split()) for s in sents]
    c: dict = collections.Counter()
    offenders: dict[str, list[str]] = collections.defaultdict(list)
    for s, n in zip(sents, lens):
        if n < 10:
            c["lt10"] += 1
            offenders["lt10_pct"].append(s)
        if n >= 25:
            c["ge25"] += 1
        if CONNECTORS.match(s):
            c["connectors"] += 1
        if BANNED.match(s):
            c["banned"] += 1
            offenders["banned"].append(s)
        for key, rx in (
            ("rather_than", r"\brather than\b"),
            ("comma_not", r", not\b"),
            ("exactly", r"\bexactly\b"),
            ("deliberately", r"\bdeliberately\b"),
            ("worth", r"\bworth\b"),
        ):
            hits = len(re.findall(rx, s, flags=re.I))
            if hits:
                c[key] += hits
                offenders[key].append(s)
        for key, rx in (("absolutist", ABSOLUTIST), ("moral", MORAL), ("dashes", DASH)):
            hits = len(rx.findall(s))
            if hits:
                c[key] += hits
                offenders[key].append(s)
        if ":" in s and len(s.split(":")[0].split()) <= 5 and not s.startswith("Success criterion"):
            c["colon_lead"] += 1
            offenders["colon_lead"].append(s)
        if NUM_OPEN.match(s):
            c["num_open"] += 1
            offenders["num_open"].append(s)
    n = max(len(sents), 1)
    result = {
        "file": path.name,
        "words": sum(lens),
        "sentences": len(sents),
        "mean_len": round(statistics.mean(lens), 1) if lens else 0.0,
        "lt10_pct": round(100 * c["lt10"] / n, 1),
        "ge25_pct": round(100 * c["ge25"] / n, 1),
    }
    for key in TARGETS:
        result.setdefault(key, c[key])
    misses = []
    for key, (op, limit, _) in TARGETS.items():
        v = result[key]
        ok = v >= limit if op == ">=" else v <= limit
        if not ok:
            misses.append(key)
    result["misses"] = misses
    result["offenders"] = offenders if show else {}
    return result


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("units", nargs="*", help="unit numbers or slugs; default all")
    ap.add_argument("--strict", action="store_true", help="exit 1 if any page misses a target")
    ap.add_argument("--show", action="store_true", help="print the sentences behind each miss")
    args = ap.parse_args()

    pages = sorted(p for p in LESSONS.glob("*.md") if p.name != "learn.md")
    if args.units:
        pages = [p for p in pages if any(p.name.startswith(u + "-") or u in p.name for u in args.units)]
    if not pages:
        print("no lesson pages matched")
        return 1

    header = "file                             words mean  <10%  >=25% conn  rt ,not  abs exct delb wrth morl coln  num dash"
    print(header)
    failed = 0
    all_lens = []
    for p in pages:
        r = measure(p, show=args.show)
        flag = " " if not r["misses"] else "!"
        print(
            f"{flag}{r['file'][:32]:32} {r['words']:5} {r['mean_len']:4} {r['lt10_pct']:5} {r['ge25_pct']:6} "
            f"{r['connectors']:4} {r['rather_than']:3} {r['comma_not']:4} {r['absolutist']:4} {r['exactly']:4} "
            f"{r['deliberately']:4} {r['worth']:4} {r['moral']:4} {r['colon_lead']:4} {r['num_open']:4} {r['dashes']:4}"
        )
        if r["misses"]:
            failed += 1
            for key in r["misses"]:
                op, limit, label = TARGETS[key]
                print(f"      miss: {label} is {r[key]} (target {op} {limit})")
                for s in r["offenders"].get(key, [])[:6]:
                    print(f"        - {s[:140]}")
    print()
    print("targets:", ", ".join(f"{k} {op} {v}" for k, (op, v, _) in TARGETS.items()))
    print(f"{len(pages)} page(s), {failed} missing at least one target")
    return 1 if (args.strict and failed) else 0


if __name__ == "__main__":
    sys.exit(main())
