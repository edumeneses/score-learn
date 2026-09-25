# Handover — 2026-08-19

State of the *Learn score* course, and what to do next. Read `CLAUDE.md` first for the
toolchain and the rules; this file is status and queue.

## 2026-09-25: the capture pipeline was rebuilt; read this first

Figures are now shot on a **capture server** (`capture.py server start`, Xvfb on `:7`)
with pinned settings, every raw records the document it shows, and `drive.py` can run
score from inside through its scripting API. `CLAUDE.md` has the details; the reasons
are in the commits of 2026-09-24 and 25. Open items from that work:

1. **P4's reference solution does not wait for the visitor.** `Idle` is rigid at 4 s, so
   the trigger fires by itself; `checks/p4-interactive-installation.md` has the evidence.
   The fix is `lesson_00`'s, but how long `Idle` may wait is Edu's choice, since step 6
   asks for a maximum on every waiting instant. Then re-shoot `p4-01`.
2. **Six background figures** (`05-01`, `06-01`, `12-01`/`18-01`, `14-01`, `24-01`) show the
   pre-fix `lesson-00.score` behind a menu or dialog. `check_lessons.py` warns; re-shoot on
   the capture server or `provenance.py accept` each with a note.
3. **Lesson 02's "dashed line" claim** is unsettled; `checks/02-vocabulary.md` says how to
   settle it on `lesson-15.score`.
4. **Try `drive.py` on the multi-object scenes** (22, 27, 33, P5, P6) before asking Edu to
   assemble them by hand: `createProcess` and `createCable` exist in 3.8.2, though no
   whole patch has been built that way yet.
5. `sudo apt install xvfb` would replace the copy unpacked in `~/.local/opt/xvfb`.
6. Other Claude sessions build and debug score on this machine. Stop score only with
   `capture.py stop`; the old name-based kill hit their runs.

## Start here: the next two figures, both waiting on a decision

Everything else in the queue is ordinary work. These two are scoped, and each raises a
question that is Edu's to answer rather than the next session's to guess.

### `39-01`, the plug-in build. Two questions before starting.

The toolchain is all present: `cmake`, `ninja`, `g++`, `git`, `/media/Storage/avendish`,
and `/media/Storage/score-addon-puara`, which is a real addon rather than the template.

1. **The SDK on this machine is 3.8.0 and the course is pinned to 3.8.2.**
   `~/Documents/ossia/score/sdk/3.8.0` is the only one there. Building an addon against a
   mismatched SDK is the exact failure Lesson 39 step 5 warns about, so the SDK wants
   downloading for 3.8.2, through the application's settings, before any build output is
   treated as authoritative.
2. **What genre should this figure be?** "The template's build output" implies a terminal
   screenshot, and **no figure in this course is one**: every other figure is a score
   window at the pinned 3840x2160, `QT_SCALE_FACTOR=2` format. The recommendation on the
   table is to make the figure **the new process appearing in score's library**, which is
   a score window and consistent with its neighbours, and to quote the build log as a
   fenced code block in the lesson text, where it can be corrected, translated, and read
   aloud like everything else. Not yet agreed.

Note also that the walkthrough says to build the **untouched template**, so
`score-addon-puara` is not a substitute: it is Edu's own project, and step 6 exists
precisely so that a first build fails with no code of your own in it.

### `36-01`, two instances and their device trees. One question, one unknown.

1. **It breaks the capture format.** Two instances side by side means two non-fullscreen
   windows and a **root-window capture** rather than the window-drawable capture every
   other figure uses. Root capture works only when score is not fullscreen, which is
   recorded in `CLAUDE.md`. The figure will therefore look unlike its neighbours. That may
   be fine, since the subject genuinely is two windows, but it should be a decision.
2. **"Enable the local device" was not located.** Lesson 36 step 2 says to enable the
   local device on the instance being controlled. There is no `Local` entry in the
   add-device dialog's protocol list, which is recorded in full in
   `checks/23-midi-in-practice.md`; it is presumably a page in `Settings`. Find it before
   building the figure, and record where it was.

Practical note for whoever builds it: `capture.py` sends **screen** coordinates, so with
two windows every click needs the window's own origin added to the in-window coordinate.
Position both windows deliberately first, with Xlib or `launch --geometry`, and compute
from those origins.

### One loose end from `p3-01`

The third branch's observation in `p3-bench.score` is blank while the other two are live,
and stays blank however long the score plays. The cause was **not** established, and the
lesson deliberately asserts none: it points at the blank display as an illustration of why
the milestone asks for observation on every stage. If a later session works out why
`Multi-choice` reports nothing there, fix the lesson and `checks/p3-mapping-bench.md`
together.

## Where things stand

### 2026-09-16: voice pass over every lesson, and a crop audit of every figure

All 47 lesson pages were rewritten into Edu's voice against `WRITING_STYLE.md`. Before
the pass the prose obeyed the avoid-list and nothing else: mean sentence 14.5 words, 37%
of sentences under ten words, zero sentence-initial connectors, contrast carried by
"rather than" 229 times. After it: mean 24.5 words, 8% under ten, 306 connectors, no
verbless fragments, no aphoristic colon leads, acronyms glossed on first use, and every
page inside the word budget. The metrics tool is now `scripts/check_voice.py` (advisory,
`--strict` to fail); `scripts/check_lessons.py` still passes on all pages. The pass also fixed the
contradictions the audit found (start-screen routes in 01, the view-switch references in
00, counts in 14, 22, P2 and P3, the scripting-route tally across 29, 30 and 39, the
capstone rubric weights, the ffmpeg continuation bug in 25, a fisheye mapping error in
P6, a stale patch description in 32, and the `Cmd` shortcuts in 03 and 04).

Every figure was viewed against its lesson and its raw. Four specs were corrected and
re-rendered on the 16th; the four that needed a new capture (00-01, 00-02, 13-01, 31-01)
were re-shot on the 17th once the session was unlocked, and every figure now shows what
its lesson says it shows. The capture facts learned on the way (Wayland display and auth,
the first view-mode button being nodal, the musical-metrics setting that blanks the ruler,
moving editor windows by configure) are in `CLAUDE.md`.


**The course text is finished.** All **47 units** are written and pass
`scripts/check_lessons.py`: front matter, the 1,400 to 1,900 word budget, permalink
stability, the pinned version, score files, `checks/` notes, and every internal link.
635 minutes of reading, 1,340 minutes of practice.

**37 figures exist**, covering 36 of the 46 units that need one; unit 00 has two, and the
capstone needs none. **10 units still have no figure.**

**15 example documents** ship, with their media, all downloadable.

Live at <https://www.edumeneses.com/score-learn/>, not indexed, CI green, html-proofer
clean.

| Phase | Units | Text | Figures |
|---|---|---|---|
| 1 — authoring interactive scores | 00-18, P1-P4 (23) | done | 19 of 22 |
| 2 — media | 19-28, P5-P6 (12) | done | 8 of 12 |
| 3 — scripting, deployment, contributing | 29-40 (12) | done | 4 of 11 |

### Figures done

`00-01` annotated score · `00-02` nodal view · `01-01` start screen · `02-01` one instant ·
`03-01` window regions · `04-01` first automation · `05-01` project folder · `06-01` device
menu · `07-01` add-device dialog · `08-01` address and range · `09-01` cue list ·
`10-01` curve shapes · `11-01` LFO patch · `12-01` Record submenu · `13-01` conditioning
pipeline · `14-01` library search · `15-01` trigger · `16-01` branching ·
`17-01` loop and out-of-time · `18-01` transport ·
`19-01` audio preferences · `20-01` sound files · `21-01` effect chain with a plug-in ·
`23-01` piano roll and MIDI tree · `24-01` metrics inspector · `25-01` video sources ·
`26-01` shader editor · `28-01` audio-reactive chain · `29-01` script editor and console ·
`30-01` expression object · `31-01` Faust editor · `32-01` hosted Pd patch ·
`34-01` folded score · `p1-01` cue structure · `p2-01` light wash ·
`p3-01` mapping bench · `p4-01` installation structure

### Documents that ship

`lesson-00` (+ nodal variant) · `lesson-04` · `lesson-09` · `lesson-10` · `lesson-15` ·
`lesson-16` · `lesson-17` · `lesson-20` (two Citizen DJ excerpts) · `lesson-25` (two generated clips) ·
`lesson-32` (+ `lesson-32.pd`) · `p1-solution` · `p2-solution` · `p3-bench` · `p4-solution`

Generated by `scripts/mkscore.py`, which knows: automations (single and multi-segment),
scenarios, intervals, states with messages, events with conditions, triggers, chains,
`Sound`, `VideoProcess`, an OSC device, the `Window` device, **transitions**, and
out-of-time material with a start-on-play trigger.

## The queue, in the order I would take it

### 1. Multi-object scenes

`22-01` spatial (layout, path generator, DBAP, matrix) · `27-01` a 3D scene ·
`33-01` a control surface with a remote client · `p5-01` the looper set ·
`p6-01` a fisheye output. Each is an afternoon rather than an hour.

The p3 bench showed the cheap way to do these: **Edu assembles the patch in ten minutes,
saves it, and the rest is scripted.** Laying out a nodal patch through screenshots is where
the time goes, and it is the one part a person at the machine is simply faster at.
`checks/p3-mapping-bench.md` records the process uuids and the cable format, which are
generatable and were previously thought not to be.

### 2. Scoped, and waiting on a decision

`36-01` and `39-01`. Both are described at the top of this file; do not start either
without answering the question attached to it.

### 3. Needs something not on this machine

| Unit | Figure | Needs |
|---|---|---|
| 35 | console output and full-screen playback on a deployed machine | **A Raspberry Pi 5 over the network is sufficient.** See the detailed note in `checks/FIGURES-PENDING.md`: ssh gets the console output, the autostart, and the power-cut recovery time, which are the parts a reader needs. A screenshot needs the Pi running a desktop so `capture.py` can run there over ssh; the direct full-screen path bypasses the window system and cannot be captured by any X11 tool. **Edu has said a networked Pi 5 is available; it needs ssh access handing to the session** |
| 37 | a capture application alongside a running score | OBS is installed with its NDI plug-in; **use NDI**, since `libgstshmdata.so` and `v4l2loopback` are absent |
| 27 | part of the 3D scene | A glTF model would help; the figure can be built from a primitive plus computed geometry instead |

## Material available locally

Installed through score's package manager, under `~/Documents/ossia/score/packages/`:
Citizen DJ (eight packages, ~4,400 WAV each in the two largest), `dirt-samples`,
`drum-kits`, `space-sounds`, `the-libre-sample-pack`, `free-midi-chords` (18,456 `.mid`),
`abclib`, `jsfx_pack`, `guitarix`, and several AI and vision models.

Pure Data 0.54.1 is installed. `ffmpeg` is installed, and the two video clips in
`library/learn/25-video-pipeline/` were generated with it; the commands are printed in
Lesson 25. There is **no webcam** and **no 3D model** on this machine.

## Open decisions, all Edu's

1. **Where the course is published.** Upstream in `ossia/score-docs`, or standalone. The
   backend mirrors score-docs exactly so either is a file move. To be settled with
   Jean-Michaël Celerier now that the whole course exists.
2. **Whether to keep the repository public.** Pages needs it public on the free plan, so
   it is public repo *plus* live preview, or private repo *and* no preview. The site is
   noindexed either way, but the Markdown is readable on GitHub.
3. **French translation of Phase 1**, planned for after the English text settles.
4. **The video channel**, when recording starts, and whether the four existing *score* 3
   videos are embedded as supplements or superseded.
5. **Google Fonts.** The vendored theme still loads Catamaran from
   `fonts.googleapis.com` on every page view. Removing it changes the typography.

## Things worth knowing before you touch anything

- Figures have corrected the prose **ten times** so far: the start screen cannot be
  reopened from a menu; the transport shortcuts; how Pure Data ports are declared; the
  protocol list; the buffer size is not settable at all under PipeWire, which prints an
  environment variable to set instead; a texture reaches a window device through an
  **output address** and not a cable, which Lessons 25 and 26 both got wrong; an expression
  object's formula is typed on the process rather than in the shared script editor; piano
  roll notes are placed by **double-clicking**, since dragging does nothing; there is **no
  blank Faust process** in the library, only presets to start from; and the envelope's "two
  outputs" are in fact **two separate processes**, `RMS` and `Peak`, with a third,
  `Envelope Follower (audio)`, whose output is audio and which is the wrong object
  entirely. **Treat a figure as a test of the lesson**, and when they disagree, fix the
  lesson and record it in `checks/`.
- **Check whether a widget is disabled before blaming synthetic input.** An hour went into
  concluding that a checkbox refused XTEST clicks; it was greyed out, and only a human
  looking at the screen saw it. The neighbouring checkbox took a click first time and would
  have settled it.
- The `Window` device's output window **cannot be captured** by any tool here: it is a GPU
  surface, it opens almost entirely off the right edge, and interfering with its geometry
  stops it opening at all. Use the **process inspector's texture preview**, which shows the
  live output frame inside the main window. That is what figure 26-01 is, and it is the
  same class of problem as the Raspberry Pi's direct rendering path in unit 35.
- **The toolchain gained four things recently**, all documented in `CLAUDE.md`, and worth
  knowing before you reinvent any of them. `scripts/typeinto.py` types into a focused
  sub-widget without stealing focus, and reads the server's keymap, because this keyboard
  is a multilingual layout on which `capture.py type` silently drops quotes.
  `capture.py find_window` now prefers the application's window over the identically named
  window-manager frame, which had been making dialogs invisible to captures at random.
  `launch --open` parses with `shlex`, so a path with a space in it works. And `mkscore.py`
  emits **transitions** and out-of-time material, which is how `17-01`, `p4-01` were built
  with no interaction at all.
- **Cables are generatable**, contrary to an earlier note. Each end is a list of
  `{ObjectName, ObjectId}` from the document root down to the port;
  `checks/p3-mapping-bench.md` has a worked example and the six process uuids the bench
  uses. Nobody has taught `mkscore.py` process shapes beyond the ones listed above, because
  no figure has needed it yet.
- **An endless document needs two settings, not one**: `MaxInf` on the root interval *and*
  `Active` on the base scenario's `EndTimeNode`. Miss the second and an inner loop still
  stops when the root's duration runs out. Score writes both into every new document;
  `mkscore.py` did not, which is why generated loops ended and hand-drawn ones did not.
- `checks/<slug>.md` is the memory of each unit: figure status, what to re-verify at the
  next version pin, corrections made, and which reference page the lesson was written
  against. Keep writing them.
- The plan and the audit of prior art live at
  `/media/Storage/Assistant/Documents/ossia_score_tutorial_syllabus.md`.
