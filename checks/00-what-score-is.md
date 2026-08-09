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
| 00-02 | The same document as a node graph | **pending**, see below |

## Why 00-02 is pending

`scripts/mkscore.py` can flip the racks to nodal (`lesson-00-nodal.score` is generated), but a document authored as JSON carries no node positions, so score draws the graph collapsed and the figure teaches nothing. Two ways out, in order of preference:

1. open `lesson-00.score` in score, switch the intervals to nodal view, lay the nodes out by hand, save as `lesson-00-nodal.score`, then capture with the same commands. This requires an unlocked session, since it needs real interaction.
2. give the builder explicit `Pos` values per process and find the coordinate space score expects for nodal layout.

Until then Lesson 00 states plainly that the figure is pending rather than shipping a misleading one.

## Re-verify when the pinned version changes

- Figure 00-01, if the timeline drawing, the trigger marker, the slot headers, or the colours changed. The badge coordinates in `figures/00.json` are pixels in the raw capture, so a layout change means re-picking them.
- That `lesson-00.score` still loads: score's document `Version` is 4 for 3.8.x, and `mkscore.py` writes that value.
- The trigger label `waits for /lesson/go` and the branch conditions on `lesson:/level`, which the walkthrough quotes verbatim.
- The claim that a web version is in development.
- The platform list, in particular embedded Linux support.

## Claims that depend on external sources

- The usability finding on the learning curve and on the device separation comes from the SAT *Ossia score UI/UX study report*. If that study is superseded, re-check both mentions.
- The *score* 3 feature list (GPU video pipeline, C++ live coding, tempo and musical metrics, hierarchical polyrhythms, generalised looping) comes from Celerier and Baltazar, *Networked Performances with Ossia Score*.
