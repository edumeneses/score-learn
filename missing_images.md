# Missing figures

10 units still have no figure. Every other blocker (menus, dialogs, patches) is solved by
the scripted pipeline; what's left needs a human at the machine, a second device, or
software this course doesn't ship. For each: what the figure has to show, exactly what to
build, where to save the `.score`, and the capture format to match.

Capture format for all of them: pinned build **ossia score 3.8.2**, fullscreen,
`QT_SCALE_FACTOR=2`, 3840x2160. See `CLAUDE.md` for the capture/annotate pipeline and the
"hard-won facts" list before driving the interface.

---

## 22-01 — Spatial audio (Lesson 22)

**Shows:** a spatial scene in the nodal view: layout, path generator, DBAP, matrix, all
cabled.

**Build**, nodal view:
- Sound (mono file, loop on)
- Multi-cursor, 4 points in a square, plus a Point view to see them
- Path generator, set to circle
- DBAP: layout inlet ← multi-cursor/point view; source inlet ← path generator
- Spatialisation matrix, 4 outputs: data inlet ← DBAP output; audio inlet ← Sound

**Save:** `library/learn/22-spatial-audio-1/lesson-22.score`

**Note:** chaining connects by first port, which is wrong here — DBAP's layout and source
inlets need separate cables dragged by hand.

---

## 27-01 — 3D scenes (Lesson 27)

**Shows:** a scene with a primitive and a computed geometry, both rendering.

**Build**, nodal view:
- Window device
- Primitive mesh → model display → Window
- Array generator → array-to-mesh → model display (second geometry alongside the primitive)

**Save:** `library/learn/27-3d-scenes/lesson-27.score`

**Note:** no glTF model on this machine, so skip the model-loader half; the recommendation
already on record is primitive + computed geometry, which needs no file. Screenshot from
the process inspector's texture preview, same as `26-01` — the Window device's own output
surface can't be captured.

---

## 33-01 — Custom interfaces (Lesson 33)

**Shows:** a control surface populated with controls.

**Build:**
- Any document with 2–3 controllable ports (a gain, an LFO rate, a trigger)
- Add a Control surface process
- Drag those 2–3 addresses from the device explorer onto its central area

**Save:** `library/learn/33-custom-interfaces/lesson-33.score`

**Note:** the lesson also wants "a remote client connected," but every figure in this course
is a score window, and a browser WebSocket console is not one. Recommend the figure be the
populated surface only, with the remote-client step covered in prose as it is now. Flag if
you want it shown a different way.

---

## p5-01 — Audio looper set (Milestone P5)

**Shows:** four toggled layers and their key mapping.

**Build**, per the milestone brief:
- 4 independent layers, each a looping sound file, out-of-time with start-on-play
- Each toggled by its own key: two triggers per layer (start/stop), minimum duration so one
  press isn't read as two
- 2 gain sub-ports addressed from keys or controller
- One ending cue that brings every layer to zero

**Save:** `library/learn/p5-audio-looper-set/p5-solution.score`

---

## p6-01 — Fulldome scene (Milestone P6)

**Shows:** a fisheye output in a window, with the scene structure folded.

**Build**, per the milestone brief:
- Window device, fisheye projection, at a resolution you can run
- 4 scenes as sub-scenarios, chained by triggers with maximum durations
- 2 audio-reactive relationships, one continuous and one percussive, in at least two scenes
- Fold the top-level structure before capture (View > Fold intervals)

**Save:** `library/learn/p6-fulldome-scene/p6-solution.score`

**Note:** capture from the process inspector's texture preview, same reason as 27-01.

---

## 38-01 — Reading the documentation (Lesson 38)

**Shows:** contextual help open beside a selected object.

**Build:** select any process in a score (an existing one works fine — `p1-solution.score`
or similar), press `F1`. The reference page opens as a separate panel/window beside the
main one.

**Save:** no new `.score` needed; reuse an existing document.

**Note:** this one is pure interaction, no media or hardware. It was left off
`checks/FIGURES-PENDING.md`'s pending table by mistake — that table says "every figure that
needs only clicks is now done," which is stale. Worth doing whenever you're at the machine;
doesn't need to wait for anything else on this list.

---

## 36-01 — Distributed scores (Lesson 36)

**Shows:** two instances of score and their device trees — one controlling the other.

**Open question, yours per HANDOVER.md:** this breaks the one-window format every other
figure uses. Two instances side by side means a **root-window capture**, not the
window-drawable capture everything else uses (root capture only works when score isn't
fullscreen). The subject genuinely is two windows, so that may be the right call, but it's
a decision, not a default.

**Also unresolved:** "enable the local device" (lesson step 2) has no `Local` entry in the
add-device dialog's protocol list. Probably a `Settings` page — find it before building.

**Build**, once decided:
- Two instances, different ports, positioned deliberately (Xlib or `launch --geometry`,
  since `capture.py` sends screen coordinates and each window needs its origin added)
- Enable the local device on the controlled instance
- On the controller, declare a device pointing at it

**Save:** `library/learn/36-distributed-scores/lesson-36.score` (×2, or one shared)

---

## 37-01 — Recording and streaming (Lesson 37)

**Shows:** a capture application alongside a running score.

**Same format problem as 36-01**, not previously flagged: the natural figure is score's
video-chain output plus OBS receiving it over NDI, which is two windows, not one. Worth
deciding at the same time as 36-01's format question.

**Build**, once decided:
- A document producing video and audio
- NDI output configured in score's video chain (`libgstshmdata.so` and `v4l2loopback` are
  absent here, so NDI is the working route, not shmdata)
- OBS with its NDI plug-in receiving it

---

## 39-01 — Writing a process (Lesson 39) — explicitly on hold

**Shows:** to be decided — either the template's build output (terminal) or the new
process appearing in score's library (score window). Not a figure genre this course has
used yet; see HANDOVER.md for the open questions. **Left out of this round per your
instruction.**

---

## 35-01 — Headless and embedded (Lesson 35)

**Shows:** console output and full-screen playback on a deployed machine.

**Needs a Raspberry Pi 5 over the network** — hardware not on this machine. Console
output and recovery timing need only `ssh`; the full-screen screenshot half needs the Pi
running a desktop so `capture.py` can run there, or it's a photograph instead. Full detail
in `checks/FIGURES-PENDING.md`. **Blocked until the Pi is reachable.**

---

## Summary

| Unit | Blocker | Ready to build now? |
|---|---|---|
| 22-01 | interaction (nodal patch) | yes |
| 27-01 | interaction (nodal patch) | yes, no model file needed |
| 33-01 | interaction; figure-genre question flagged | yes, pending your call on the remote-client half |
| p5-01 | interaction + media (have material) | yes |
| p6-01 | interaction + live GPU | yes |
| 38-01 | interaction only | yes — quickest one here |
| 36-01 | interaction + hardware; format decision open | after you decide the format |
| 37-01 | interaction + other software; format decision open | after you decide the format |
| 39-01 | on hold by request | not this round |
| 35-01 | needs a Pi 5 over the network | blocked until reachable |
