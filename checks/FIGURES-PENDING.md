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

## Done: 25 figures

Scripted, no interaction: `00-01` annotated score · `03-01` window regions ·
`04-01` first automation · `08-01` address and range · `09-01` cue list ·
`10-01` curve shapes · `15-01` trigger · `16-01` branching · `p1-01` cue structure ·
`p2-01` light wash.

Captured 2026-08-11 in an unlocked session, with menus composited in by
`capture.py --popups`: `00-02` nodal view · `02-01` one instant ·
`05-01` project folder panel · `06-01` device menu · `12-01` Record submenu ·
`14-01` library search · `18-01` transport and play-from-here ·
`24-01` interval metrics inspector · `01-01` the start screen ·
`11-01` an LFO patch · `13-01` the conditioning pipeline · `34-01` a folded score ·
`07-01` the Add device dialog, captured with one human click ·
`20-01` two sound files, from the installed Citizen DJ material.

The nodal-patch figures were built by selecting an interval, filtering the process
library, and double-clicking the result, which adds the process **and connects it**;
`capture.py menu X Y --pick N` handled the menu-driven ones.

## Pending: 22 figures

**Every figure that needs only clicks is now done.** What remains needs media, other
software, or hardware.

Three lessons for whoever continues this:

- Input goes to whatever window is **topmost at the click point**, not to the window you
  mean. `capture.py` refuses to send input when something covers the target, after a run
  where a fullscreen browser silently ate every click.
- Use `capture.py menu X Y --pick N`, which measures a menu's rows and clicks by index.
  Guessed menu coordinates failed every time.
- Some things cannot be automated at all. `Ctrl+B` never fires, and clicking the
  `Add device` row lands correctly without opening the dialog. For those, use
  `capture.py waitshot`, which polls until a dialog appears and then captures it, so a
  human only has to open the thing and walk away.

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

**Video**: solved. Two mockup clips are generated with `ffmpeg` and committed under
`library/learn/25-video-pipeline/`, one H.264 and one MJPEG, with the generating commands
printed in Lesson 25 so they can be remade at any resolution. No camera is needed.

Still missing locally: **3D models**. A simple glTF can be written by hand or exported
from any modelling tool; Lesson 27's figure can also be built from a primitive plus
computed geometry, which needs no file at all.

### Interaction plus media (9)

The audio and MIDI ones can be done now with the material above.

| Unit | Figure | What to capture |
|---|---|---|
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
| 32 | `32-01` | **doable, one unknown**: Pure Data 0.54.1 is installed and `lesson-32.pd` ships with the lesson, but the process library entry is not called `pure` (that search returns Airwindows plug-ins). Find it under `Script`, or try `pd` |
| 33 | `33-01` | **doable**: a browser on this machine can be the remote client over localhost |
| 35 | `35-01` | **partly**: headless on this machine is doable; the Raspberry Pi half needs a board |
| 36 | `36-01` | **doable**: two instances on one machine, which is the lesson's own first step |
| 37 | `37-01` | **doable**: OBS is installed at `/usr/bin/obs`, and its NDI plug-in (`distroav.so`) is present, so the score-to-OBS path can go over NDI. The Linux route in the lesson uses `shmdata` into GStreamer into `v4l2loopback`; neither the `libgstshmdata.so` GStreamer plug-in nor the `v4l2loopback` module is present, so NDI is the route to use here |
| 39 | `39-01` | **doable**: `cmake`, `ninja`, and `g++` are installed |

`40` (capstone) needs no figure: it is a brief and a rubric.

## What genuinely needs something we do not have

Three things, and only three:

1. **A Raspberry Pi or spare machine**, for the deployment half of `35-01`. See the note
   below on exactly what the figure needs from it: a networked Pi 5 is sufficient.
2. **A 3D model**, optional, for part of `27-01`. The figure can be built without one.

Pure Data is installed. Video is generated. A camera and a dome are not needed: `25-01`
uses the mockup clips and `p6-01` is specified as a fisheye image in a window.

## What figure 35-01 actually needs from a Pi

The figure has to show two things: score **playing a document with no editing interface**,
and the **console output** that proves it started that way. The lesson's claims that need a
real board are the ARM build, the graphics-driver configuration, the two launcher scripts,
and the automatic start after a power cut.

A **Raspberry Pi 5 reachable over the network is sufficient**, with three conditions:

1. **64-bit OS.** The 64-bit build is the one to use on a Pi 5. Note that the reference
   documentation was written for the Pi 3 and 4 on Debian Buster and Bullseye, so part of
   what Lesson 35 says about configuration has to be re-verified on a current OS. That
   re-verification is itself worth having.
2. **`ssh` access**, to install score, run it, and read the console output. The console half
   of the figure is text, so it needs nothing else.
3. **For the screenshot half, one of**: the Pi running a desktop session, in which case
   `capture.py` can be installed there and run over `ssh` with `DISPLAY` set, and the PNG
   copied back; or the Pi rendering full screen through the direct path, which bypasses the
   window system entirely and therefore **cannot be captured by any X11 tool**. In that
   case the figure becomes console output plus a photograph of the screen.

The honest recommendation: use the Pi 5 for the console output, the automatic start, and
the power-cut recovery time, all of which are the parts a reader actually needs, and treat
the full-screen photograph as optional.

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
