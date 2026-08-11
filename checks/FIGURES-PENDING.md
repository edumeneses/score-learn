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
| **media** | The figure needs audio, video, or a 3D model. **Mostly solved**: see the local material below |
| **hardware** | The figure needs a second machine, a Raspberry Pi, a webcam, or software that is not installed |

Pinned build for every capture: **ossia score 3.8.2**, fullscreen at
`QT_SCALE_FACTOR=2` on a 3840x2160 screen. Keep that format so the set stays
consistent.

---

## Done: 19 figures

Scripted, no interaction: `00-01` annotated score · `03-01` window regions ·
`04-01` first automation · `08-01` address and range · `09-01` cue list ·
`10-01` curve shapes · `15-01` trigger · `16-01` branching · `p1-01` cue structure ·
`p2-01` light wash.

Captured 2026-08-11 in an unlocked session, with menus composited in by
`capture.py --popups`: `00-02` nodal view · `02-01` one instant ·
`05-01` project folder panel · `06-01` device menu · `12-01` Record submenu ·
`14-01` library search · `18-01` transport and play-from-here ·
`24-01` interval metrics inspector.

## Pending: 28 figures

### Interaction only — what is left (5)

| Unit | Figure | What to capture | Note |
|---|---|---|---|
| 01 | `01-01` | The start screen with the bundled examples | Must be captured **at launch**: 3.8.2 has no menu entry that reopens it, which the lesson now says explicitly |
| 07 | `07-01` | The Add-device dialog with its protocol list, and the OSC settings | `Ctrl+B` and the `+` button both failed to open the dialog under synthetic input; it may need a real click on the menu item |
| 11 | `11-01` | An LFO patched to three destinations in the nodal view | Needs processes added to a score, then the view-mode button |
| 13 | `13-01` | A conditioning pipeline in the nodal view | Same |
| 34 | `34-01` | A folded, named score | `Ctrl+Alt+F` did not fold under synthetic input; use `View > Fold intervals` from the menu |

### Interaction plus transitions (3)

`mkscore.py` cannot emit transitions, the instantaneous intervals that make loops
and out-of-time material. These have to be drawn.

| Unit | Figure | What to capture |
|---|---|---|
| 17 | `17-01` | A loop built from a transition, and out-of-time material |
| P3 | `p3-01` | The mapping bench: one conditioned input, three branches, observation on each |
| P4 | `p4-01` | Idle loop, visitor trigger, two branches, return transitions |

## Material already on this machine

Installed through the package manager, under `~/Documents/ossia/score/packages/`, and
available in the user library. This removes the media blocker from most figures:

| Kind | Package | Amount |
|---|---|---|
| Audio excerpts, freely usable | `citizen-dj-free-music`, `citizen-dj-musicbox`, `citizen-dj-variety-stage`, `citizen-dj-joe-smith`, `citizen-dj-american-english`, `citizen-dj-tony-schwartz`, `citizen-dj-inventing-entertainment`, `citizen-dj-national-screening-room` | ~4,400 WAV each in the two largest |
| Percussive samples | `dirt-samples`, `drum-kits`, `the-libre-sample-pack`, `space-sounds` | ~1,800 WAV in dirt-samples alone |
| MIDI files | `free-midi-chords` | 18,456 `.mid` |
| Faust spatial library | `abclib` | ambisonics, decoders, geometry |
| Hosted plug-ins | `jsfx_pack` | JSFX effects, including MIDI ones |
| Faust amp models | `guitarix` | |
| AI / vision models | `librediffusion`, `yolov8-pose`, `blazepose-full-body`, `resnet50-v2-7`, `affectnet`, `rtmpose-body-2d` | |

Still missing locally: **video files** and **3D models**. A short video can be generated
with `ffmpeg`, which is installed; a simple glTF can be written by hand or exported from
any modelling tool.

### Interaction plus media (9)

The audio and MIDI ones can be done now with the material above.

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

### Interaction plus other software (11), and what this machine already has

Checked on this machine, 2026-08-11:

| Unit | Figure | Status here |
|---|---|---|
| 19 | `19-01` | **doable**: audio preferences plus an outlet inspector, both in-application |
| 21 | `21-01` | **doable**: `jsfx_pack` provides hosted plug-ins, no purchase needed |
| 23 | `23-01` | **doable**: ALSA `Midi Through Port-0` exists, so a MIDI device can be declared with no hardware; notes come from `free-midi-chords` |
| 29 | `29-01` | **doable**: script editor and console are in-application |
| 30 | `30-01` | **doable**: expression objects are in-application |
| 32 | `32-01` | **blocked**: Pure Data is not installed. `sudo apt install puredata` |
| 33 | `33-01` | **doable**: a browser on this machine can be the remote client over localhost |
| 35 | `35-01` | **partly**: headless on this machine is doable; the Raspberry Pi half needs a board |
| 36 | `36-01` | **doable**: two instances on one machine, which is the lesson's own first step |
| 37 | `37-01` | **doable**: OBS is installed at `/usr/bin/obs`, and its NDI plug-in (`distroav.so`) is present, so the score-to-OBS path can go over NDI. The Linux route in the lesson uses `shmdata` into GStreamer into `v4l2loopback`; neither the `libgstshmdata.so` GStreamer plug-in nor the `v4l2loopback` module is present, so NDI is the route to use here |
| 39 | `39-01` | **doable**: `cmake`, `ninja`, and `g++` are installed |

`40` (capstone) needs no figure: it is a brief and a rubric.

## What genuinely needs something we do not have

Three things, and only three:

1. **Pure Data**, for figure `32-01`. One command: `sudo apt install puredata`.
2. **A Raspberry Pi or spare machine**, for the deployment half of `35-01`. A Pi 4 is the
   board the reference documentation recommends. Without it, the headless part can still
   be shown on this machine.
3. **A camera and a real dome**, which are nice-to-have rather than blocking: `25-01` can
   use two video files instead of a webcam, and `p6-01` is specified as a fisheye image in
   a window precisely so that no dome is needed.

Everything else on this page can be produced on this machine in an unlocked session.

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
