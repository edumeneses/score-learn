# Re-verification note: Lesson 00

Pinned build: **ossia score 3.8.2** (AppImage, `~/Applications/ossia.score-3.8.2-linux-x86_64.AppImage`)

## How the figure is produced

Fully scripted, no interface interaction:

```bash
python3 scripts/mkscore.py 00                    # writes library/learn/00-what-score-is/
python3 scripts/capture.py --match score launch \
    --qt-scale 2 --fullscreen \
    --open "$PWD/library/learn/00-what-score-is/lesson-00.score"
python3 scripts/capture.py --match score shot figures/raw/raw-00-01.png
python3 scripts/annotate.py figures/00.json      # crop + numbered badges
```

Capture format: fullscreen on a 3840x2160 screen with `QT_SCALE_FACTOR=2`, which is a 1920x1080 logical layout at 2x device pixels. Captured from the window's own drawable, not from the root window, because a compositing window manager returns black for the root.

| ID | Content | Status |
|---|---|---|
| 00-01 | Annotated `lesson-00.score`, badges 1 to 7 matching the walkthrough steps | **done**, `docs/learn/assets/00/00-01-annotated-score.png` |
| 00-02 | The same document as a node graph | **done**, docs/learn/assets/00/00-02-nodal-view.png |

## How 00-02 was produced

`mkscore.py` can flip the racks to nodal, but a JSON-authored document carries no node
positions, so score drew that graph collapsed. The figure was captured instead by
opening `lesson-00.score` and pressing the view-mode button at the bottom left of the
window, at roughly x=767, y=2098 in the capture format, which switches the editor to the
node graph and lays it out. That needed an unlocked session.

## Re-verify when the pinned version changes

- Figure 00-01, if the timeline drawing, the trigger marker, the slot headers, or the colours changed. The badge coordinates in `figures/00.json` are pixels in the raw capture, so a layout change means re-picking them.
- That `lesson-00.score` still loads: score's document `Version` is 4 for 3.8.x, and `mkscore.py` writes that value.
- The trigger label `waits for /lesson/go` and the branch conditions on `lesson:/level`, which the walkthrough quotes verbatim.
- The claim that a web version is in development.
- The platform list, in particular embedded Linux support.

## Claims that depend on external sources

- The usability finding on the learning curve and on the device separation comes from the SAT *Ossia score UI/UX study report*. If that study is superseded, re-check both mentions.
- The *score* 3 feature list (GPU video pipeline, C++ live coding, tempo and musical metrics, hierarchical polyrhythms, generalised looping) comes from Celerier and Baltazar, *Networked Performances with Ossia Score*.

- 2026-09-16 crop audit: Figure `00-02` recropped as a stopgap so the whole scenario node is in frame; the raw was captured unfitted, so a re-shoot with the nodal fit icon is queued (`scripts/reshoot_00_02.sh`). Figure `00-01`: `Bright` runs past the editor edge in the raw, so its end state is not visible; a re-shoot at a smaller zoom is queued.

- 2026-09-17: both figures re-shot. `00-01` now comes from `raw-00-01b.png`, the same document zoomed out with Ctrl+wheel (`scripts/wheel.py`) so `Bright` and the root's flexible end are on screen; `raw-00-01.png` stays because 02-01 and 08-01 crop it. `00-02` was re-shot from `lesson-00.score`: nodal mode is the FIRST view-mode button (raw 768,2112; click twice, the first click only focuses), then the nodal slot's + icon (768,73) six times, then the scenario node's bottom-right handle dragged out and the node dragged to the top by its title until every nested interval was legible. `lesson-00-nodal.score` is not usable for this: its root has no visible slot.

- 2026-09-24: `lesson-00.score` corrected, and `00-01` re-shot on it. Edu found in score that the trigger never waited: `Approach` was rigid (min = max = 6 s), and a trigger waits only between the preceding interval's minimum and maximum, so it fired by itself at 6 s. `Approach` is now elastic with an infinite maximum, the root is endless (`document(..., endless=True)`), `Bright` is 5 s so it ends on screen, and the nested slot is 321 px so `Shutter` is whole. `mkscore.py 00` had also been failing on a stale `extra_devices` reference, so the shipped file predated later builder fixes; `lesson_00()` now calls `document()`. The new raw is `raw-00-01c.png`, captured at score's own zoom (no Ctrl+wheel needed now 0 to 11 s fits). The running document could not be played to confirm the wait: synthetic clicks were being swallowed that session (see below). **`00-02` still shows the old layout** (Bright longer than Dark, Shutter clipped) and needs the 2026-09-17 procedure repeated; that same session swallowed every click, with byte-identical captures before and after, although logind reported the session unlocked.

- 2026-09-25: both leftovers closed on the capture server (`capture.py server start`). **The trigger now waits**: played with no input, at 8.35 s `Approach` has run to its end, the trigger instant is highlighted, and neither `Bright` nor `Dark` has started. **`00-02` re-shot** as `raw-00-02b.png` with the procedure in `figures/00-02.json`; the taller nested slot needs the node stretched to the editor's bottom, or `Shutter` is clipped. The figure's link now downloads `lesson-00.score`, the document it was shot on and the one the prose calls "the same file"; it used to download `lesson-00-nodal.score`, which shows no root slot. `check_lessons.py` now catches that mismatch.
- 2026-09-25, later: the conditions on `Bright` and `Dark` were being ignored (both branches ran), because they lacked score's `%address%` form; see `checks/16-conditions-and-branching.md`. Fixed in `mkscore.py`, and `00-01`, `02-01`, `03-01`, `08-01` (all from `raw-00-01d.png`) and `00-02` (`raw-00-02c.png`) re-shot, since score now draws a condition bracket on each branch; badge 6 points at `Bright`'s. Step 6's "so that only one of them runs" is now true of the document.
