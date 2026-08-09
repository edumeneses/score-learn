# Learn *score*

A graded course for [*ossia score*](https://ossia.io), the interactive sequencer for the intermedia arts. Forty-seven units, each between ten and fifteen minutes, take a reader from a first installation to a complete interactive work.

Authored by Eduardo Meneses (Société des Arts Technologiques, Montréal). Content is licensed [CC BY-SA 4.0](LICENSE); the vendored Jekyll theme keeps its MIT terms ([LICENSE-theme.txt](LICENSE-theme.txt)).

## Status

Draft, Phase 1 in progress. **Where the course will eventually be published is deliberately undecided.** It is authored here so that the pedagogy can be written and revised without negotiating an upstream merge first; placement is settled with Jean-Michaël Celerier once Phase 1 exists and can be judged on its content.

The full plan, including the audit of the material this course is built on, is at `Documents/ossia_score_tutorial_syllabus.md` in the Assistant repository.

## Decisions this repository implements

| Decision | Value |
|---|---|
| Target build | *ossia score* **3.8.2**, pinned. Every page declares `score_version`, and `scripts/check_lessons.py` fails on a mismatch |
| Hardware | **None required.** Milestones use emulated sensors, a software Art-Net receiver, keyboard-mapped controls, and a binaural fold-down of the spatial material. SAT-specific paths appear as optional sidebars |
| Language | English first; French for Phase 1 once the English pages are stable. No parallel drafting |
| Licence | CC BY-SA 4.0 for prose, figures, and score files |
| Backend | Mirrors `ossia/score-docs` exactly, so folding the course upstream is a file move |

## Why the backend is a mirror

Every element below is taken from `ossia/score-docs`, at the same version, so that the two sites render identically and a merge does not become a porting exercise:

- Jekyll >= 4.2 with just-the-docs **0.3.2 vendored in-tree**, not `remote_theme`, and the same custom `color_scheme`;
- the same plugin set, including `jcelerier/jekyll-wikirefs`, `jekyll-seo-tag`, and the in-tree `_plugins/`;
- the same `preview.sh` and `_local_config.yml` pattern, serving on `http://127.0.0.1:4000` with an empty `baseurl`;
- `html-proofer` for link checking, already a `score-docs` dependency.

Paths are chosen to be the upstream paths already: lessons live under `docs/learn/`, score files under `library/learn/`. The one mechanical difference between the two hosting outcomes is isolated to a single site variable, `docs_baseurl`, used for every cross-link into the reference documentation. It is absolute while this repository is standalone and becomes empty if the course merges.

Published permalinks are contractual, since future videos will point at them.

## Layout

```
docs/learn/                  lesson pages, docs/learn/NN-<slug>.md
docs/learn/assets/NN/        figures for lesson NN, PNG at 2x, plus short GIFs
library/learn/NN-<slug>/     runnable .score files and their media
checks/NN-<slug>.md          what to re-verify when the pinned version changes
figures/NN.json              crop and badge spec for lesson NN's figures
figures/raw/                 raw captures, kept so badges can be moved cheaply
scripts/check_lessons.py     front matter, reading budget, permalink, and asset checks
scripts/mkscore.py           builds the example .score documents
scripts/capture.py           launches score, sizes it, captures its window
scripts/annotate.py          crops a raw capture and draws the numbered badges
_config.yml                  site config; _local_config.yml overrides it for preview
```

## Working on the course

```bash
./preview.sh                      # bundle install on first run, then serve on :4000
python3 scripts/check_lessons.py  # front matter, word budget, permalinks, assets
```

## The figure pipeline

Figures are produced by script, not by hand, so that a lesson can be re-shot when the pinned score version changes. Nothing in the chain needs interaction with the interface, which also means it runs on a machine whose session is locked.

```bash
python3 scripts/mkscore.py 00                     # build the lesson's .score files
python3 scripts/capture.py --match score launch \
    --qt-scale 2 --fullscreen \
    --open "$PWD/library/learn/00-what-score-is/lesson-00.score"
python3 scripts/capture.py --match score shot figures/raw/raw-00-01.png
python3 scripts/annotate.py figures/00.json       # crop + numbered badges
```

- `mkscore.py` writes the example scores as JSON, which is what a `.score` file is. Authoring them here rather than in the interface is what makes a figure reproducible.
- `capture.py` drives X11 directly through python-xlib: no screenshot utility, no root privileges. It captures from the window's own drawable, because a compositing window manager returns black for the root window. It can also send synthetic input through XTEST, which requires an unlocked session.
- `annotate.py` crops a raw capture and draws numbered badges whose numbers match the lesson's walkthrough steps. The wording stays in the page, where it can be corrected, translated, and read aloud for the video.

Capture format: fullscreen on a 3840x2160 screen with `QT_SCALE_FACTOR=2`, giving a 1920x1080 logical layout at 2x device pixels. Raw captures live in `figures/raw/` and are kept, so a badge can be moved without re-running score.

Requirements: `python-xlib` and `Pillow`, plus a display. `checks/NN-<slug>.md` records, per lesson, which figures exist and what has to be re-verified at the next version pin.

`check_lessons.py` enforces the reading budget of 1,400 to 1,900 words per lesson, which is the 10 to 15 minute cap the course commits to. A lesson that outgrows the band is split into Part I and Part II rather than allowed to overrun.

## Conventions

1. **Numbers are permanent.** New material takes a new number or a Part II. Never renumber a published unit.
2. **One concept per lesson**, and nothing is used before it is introduced.
3. **Every lesson ends in an artefact**, not a definition, and ships a runnable score file.
4. **A *Make it work* milestone introduces nothing new.** It assembles the preceding cluster.
5. **The course links outward.** Reference material is linked through `docs_baseurl`, never restated.
6. **Each page is a shooting script.** "Why this matters", "Concepts", and "Exercise" are written to be read aloud nearly verbatim when the videos are recorded.

## Commits

One commit per module, one tag per phase, so that whichever review path is chosen later, a reviewer receives coherent blocks rather than 47 unrelated pages.
