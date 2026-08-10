# Figures that need Edu

Every figure in this course is produced by the scripted pipeline in the README:
`mkscore.py` writes an example document, `capture.py` launches the pinned build and
captures its window, `annotate.py` crops and draws the numbered badges. That chain
needs **no interaction**, which is why eleven figures already exist.

The figures below cannot be produced that way. Each needs one of three things that
a script cannot supply, and the table says which:

| Blocker | Why |
|---|---|
| **interaction** | The figure shows a menu, a modal dialog, a typed search, a nodal patch, or a transition. Synthetic input through XTEST is swallowed whenever the session is locked, and `mkscore.py` does not emit transitions or node positions |
| **media** | The figure needs audio, video, or a 3D model that this course cannot ship for licensing reasons |
| **hardware** | The figure needs a second machine, a Raspberry Pi, a plug-in, a MIDI controller, or a capture application |

Pinned build for every capture: **ossia score 3.8.2**, fullscreen at
`QT_SCALE_FACTOR=2` on a 3840x2160 screen. Keep that format so the set stays
consistent.

---

## Done: 11 figures

`00-01` annotated score · `03-01` window regions · `04-01` first automation ·
`08-01` address and range · `09-01` cue list · `10-01` curve shapes ·
`15-01` trigger · `16-01` branching · `p1-01` cue structure · `p2-01` light wash ·
plus the raws in `figures/raw/` they were cropped from.

## Pending: 36 figures

### Interaction only — fastest to clear (13)

These need an **unlocked session** and nothing else. Most are one screenshot each.
If you clear only one group, clear this one.

| Unit | Figure | What to capture |
|---|---|---|
| 01 | `01-01` | Start screen with the bundled examples, and the `File` menu showing how to reopen it |
| 02 | `02-01` | Zoom on `lesson-00.score`'s trigger instant, badged for state, event, trigger |
| 05 | `05-01` | The project folder panel beside a project directory on disk |
| 06 | `06-01` | The protocol chooser, and a device's edit dialog |
| 07 | `07-01` | The OSC protocol dialog with both port settings, and the address editor |
| 11 | `11-01` | An LFO patched to three destinations in the nodal view |
| 12 | `12-01` | The record-automations context menu, plus a dense curve before and after reduction |
| 13 | `13-01` | A conditioning pipeline in the nodal view: calibrator, filter, curve, smooth |
| 14 | `14-01` | The process library with a search in progress |
| 18 | `18-01` | The transport bar with its four buttons identified, and the play-from-here menu |
| 24 | `24-01` | The musical metrics area, and an interval's metrics inspector |
| 34 | `34-01` | A folded, named score beside its documentation |
| 38 | `38-01` | Contextual help open beside a selected object |

Also in this group, and worth doing first because it is the one figure the course
promises and does not have:

| Unit | Figure | What to capture |
|---|---|---|
| 00 | `00-02` | `lesson-00.score` as a node graph. `mkscore.py` can flip the racks to nodal, but a JSON-authored document has no node positions, so score draws the graph collapsed. Open `lesson-00.score`, switch the intervals to nodal, lay the nodes out by hand, save as `lesson-00-nodal.score`, then capture |

### Interaction plus transitions (3)

`mkscore.py` cannot emit transitions, the instantaneous intervals that make loops
and out-of-time material. These have to be drawn.

| Unit | Figure | What to capture |
|---|---|---|
| 17 | `17-01` | A loop built from a transition, and out-of-time material |
| P3 | `p3-01` | The mapping bench: one conditioned input, three branches, observation on each |
| P4 | `p4-01` | Idle loop, visitor trigger, two branches, return transitions |

### Interaction plus media (9)

Need a sound file, a video file, or a model. Any material you already own works;
what matters is that the figure shows real content rather than an empty slot.

| Unit | Figure | What to capture |
|---|---|---|
| 20 | `20-01` | A sound file slot with a gain automation and a signal display |
| 22 | `22-01` | A spatial scene in the nodal view: layout, path generator, DBAP, matrix |
| P5 | `p5-01` | The looper set: four toggled layers and their key mapping |
| 25 | `25-01` | Two video sources through the mixer into a window device |
| 26 | `26-01` | The shader editor with code beside its rendered result |
| 27 | `27-01` | A scene with a primitive, a loaded model, and generated geometry |
| 28 | `28-01` | The three-object reactive chain with a signal display, beside the image it drives |
| P6 | `p6-01` | A fisheye output in a window, with the scene structure folded |
| 31 | `31-01` | The Faust editor with code and a running audio chain |

### Interaction plus hardware or extra software (11)

| Unit | Figure | Needs |
|---|---|---|
| 19 | `19-01` | Audio preferences dialog and an audio outlet's inspector |
| 21 | `21-01` | An effect chain with a hosted plug-in — needs a plug-in |
| 23 | `23-01` | A piano roll with notes, beside a MIDI device tree — needs a controller or virtual port |
| 29 | `29-01` | The script editor and the console panel |
| 30 | `30-01` | An expression object's editor beside its result |
| 32 | `32-01` | A hosted patch's ports in the nodal view — needs Pure Data and a patch |
| 33 | `33-01` | A populated control surface, and a remote client connected — needs a second device |
| 35 | `35-01` | Console output and full-screen playback on a deployed machine — needs a Pi or spare machine |
| 36 | `36-01` | Two instances and their device trees — needs two machines |
| 37 | `37-01` | A capture application alongside a running score — needs OBS |
| 39 | `39-01` | The plug-in template's build output, and the new process in the library — needs CMake, Ninja, a compiler |

`40` (capstone) needs no figure: it is a brief and a rubric.

---

## How to capture one

With the session unlocked:

```bash
cd /media/Storage/score-learn
source /media/Storage/Assistant/venv/bin/activate
export DISPLAY=:1

# launch the pinned build in the figure format, optionally on a document
python3 scripts/capture.py --match score launch --qt-scale 2 --fullscreen \
    --open "$PWD/library/learn/00-what-score-is/lesson-00.score"

# set up whatever the figure shows: open the menu, patch the nodes, type the search
# capture.py can also drive it: click / drag / key / type  (needs an unlocked session)

python3 scripts/capture.py --match score shot figures/raw/raw-NN-01.png
```

Then write `figures/NN.json` with a crop and the badge coordinates, in raw-capture
pixels, and render it:

```bash
python3 scripts/annotate.py figures/NN.json
```

Finally, replace the `{: .note }` pending block in the lesson with the image, mark
the figure done in that unit's `checks/` note, and remove its row above.

Two format notes learned the hard way, both in the per-unit checks files:

- The scenario editor reaches about **x = 3225** in this capture format, which is
  wider than the panels suggest. A crop stopping at 3020 silently loses a
  document's last state.
- Capture from the **window's own drawable**, not the root window, which returns
  black under a compositing window manager. `capture.py` already does this.
