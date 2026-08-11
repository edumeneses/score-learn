# Re-verification note: 19-audio-setup

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 19-01 | The audio preferences dialog and an audio outlet's inspector | **done**, docs/learn/assets/19/19-01-audio-preferences.png |

See `checks/FIGURES-PENDING.md` for the consolidated list of figures that need an
interactive session or media, and why each cannot be produced by the scripted
pipeline.

## Correction made by the figure, 2026-08-11

The lesson told the reader to set the buffer size, without qualification. That is false
for one of the six backends, and the figure is what caught it.

The `Audio` page is reached from the menu bar's `Settings` menu, whose single row is also
called `Settings`; the dialog it opens is titled `Settings` and its pages are listed down
the left side. The `Driver` list in 3.8.2 holds exactly six entries: `Dummy (No audio)`,
`JACK`, `ALSA (raw)`, `ALSA (PortAudio)`, `ALSA (MiniAudio)`, and `PipeWire`.

What each shows differs, and this is the correction:

- **`ALSA (PortAudio)`**, used for the figure, shows `Buffer size`, `Rate`, `Device`, a
  `Rescan` button, and a readout of the inputs, outputs, and rate the device reports.
- **`PipeWire`** shows no buffer size and no rate at all. In their place it prints
  `To configure buffer size and sample rate with pipewire, set the PIPEWIRE_QUANTUM
  environment variable before starting ossia`, with `export PIPEWIRE_QUANTUM=256/48000`
  as the example. It offers `Auto-connect ports`, and `Inputs` and `Outputs` counts with
  the port names listed, `in_0`, `in_1`, `out_0`, `out_1`.
- **`Dummy (No audio)`** shows `Buffer size` and `Rate` and nothing else.
- **`JACK`** on this machine reported `JACK does not seem to be running. Check that jackd
  is running and that .///lib/libjack.so exists.` The doubled separator in that path is
  score's message, quoted verbatim.

The lesson now carries this as a note, and steps 1 to 3 name the dialog, the six backends,
and the `Rescan` readout.

## Re-verify when the pinned version changes

- The audio preference layout: backend list, buffer size, output device.
- Whether PipeWire still defers the buffer size to `PIPEWIRE_QUANTUM`.
- The routing rule: child to parent interval to parent scenario, and the top interval to the main output.
- That connecting an audio cable removes propagation, and that the toggle is on the port in the inspector.
- That every audio outlet still carries a gain sub-port.

## Claims that depend on external sources

- Grounded in the reference pages linked under 'Going further' on the lesson page.

## How 19-01 was captured, 2026-08-11

Both halves are in one window capture, which works because the settings dialog is
centred and the inspector is in the right dock, so they do not overlap.

```bash
python3 scripts/capture.py --match "score 3.8.2" launch --qt-scale 2 --fullscreen \
    --open "$PWD/library/learn/20-sound-files/lesson-20.score"
# select the sound process first: the dialog takes focus once it is open
python3 scripts/capture.py --match "score 3.8.2" click 1300 760
python3 scripts/capture.py --match "score 3.8.2" click 599 21     # Settings menu
python3 scripts/capture.py --match "score 3.8.2" click 615 82     # its single row
# Audio page, then Driver, then Device
python3 scripts/capture.py --match "score 3.8.2" click 962 852
python3 scripts/capture.py --match "score 3.8.2" shot figures/raw/raw-19-01.png --popups
```

Three things learned here, all now recorded in `CLAUDE.md`:

- **The `Settings` menu holds one row**, 288x36 px, which is below the 40 px floor that
  `capture.py menu` uses to recognise a menu. It reports `no menu appeared` and yet the
  menu is open, so click the row directly rather than using `--pick`.
- **A reparenting window manager gives the frame the same name and size as the window it
  wraps.** `find_window` matched both and picked whichever the tree walk returned first,
  so the same capture command sometimes contained the dialog and sometimes did not. It now
  prefers the application's own window, which made captures deterministic.
- **`ALSA (PortAudio)` reports 0 in, 0 out on the `pipewire` device** and 64 in, 64 out on
  `default`. The figure uses `default` for that reason.
