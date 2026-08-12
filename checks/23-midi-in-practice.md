# Re-verification note: 23-midi-in-practice

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 23-01 | A piano roll with notes, beside a MIDI device tree | **done**, docs/learn/assets/23/23-01-piano-roll.png |

See `checks/FIGURES-PENDING.md` for the consolidated list of figures that need an
interactive session or media, and why each cannot be produced by the scripted
pipeline.

## Re-verify when the pinned version changes

- MIDI input and output device settings.
- That dropping a MIDI file gives an editable piano roll.
- The MIDI utilities family, including the arpeggiator, and patternist.
- The RTP MIDI recommendations per platform.

## Claims that depend on external sources

- Grounded in the reference pages linked under 'Going further' on the lesson page.

## Grounded by the figure, 2026-08-12

- **Three MIDI protocols, not two.** The add-device dialog lists `MIDI Controller`,
  `MIDI Input`, and `MIDI Output` under `Hardware`. The lesson's "two devices, two
  directions" is still the right mental model, and the note now records the third.
- **No hardware is needed.** Under `MIDI Input` the devices column offers `Default MIDI In`,
  hardware inputs, and software inputs including `Midi Through Port-0` and
  `libremidi-observe`, plus `Computer keyboard` under `Other`. The output side offers
  `Default MIDI Out` and the same software ports. The figure uses `Midi Through Port-0` for
  input and `Default MIDI Out`, which score names `MIDI Out`, for output.
- **Notes are placed by double-clicking the grid.** A drag across an empty lane does
  nothing. This is worth stating in the lesson because dragging is what everyone tries.
- **The piano roll's inspector carries `Channel`, `Min`, and `Max`**, defaulting to 1, 60,
  and 71, so the grid shows one octave from middle C. Its `Outputs` section has a `MIDI Out`
  combo listing the declared MIDI output devices, which is how the roll is connected; no
  cable is drawn.
- The full protocol list in the dialog, for the record: **Network** OSCQuery, Bitfocus,
  CoAP, LSL, MQTT, OSC, Minuit; **Lights** Artnet, NeoPixel LEDs; **Audio** Audio;
  **Hardware** BLE, Evdev, Joystick, MIDI Controller, MIDI Input, MIDI Output, Raw I/O,
  Serial, Wiimote; **Video** Camera input, NDI Input, NDI Output, Sh4lt Input, Sh4lt Output,
  Shmdata Input, Shmdata Output, Window; **Web** HTTP and below.

## What is missing from the figure, and why

The figure shows the two devices as rows, **not as an expanded address tree**. Building the
tree needs the `Create whole tree` checkbox in the add-device dialog, and that checkbox does
not respond to synthetic clicks: tried on the indicator, on the label, and with the dialog
activated first, in all three cases with no effect, while clicks in the same dialog's
protocol and device lists work normally. One human click on that checkbox would complete
the figure; nothing else is missing.

## Correction to a previous session's conclusion

`CLAUDE.md` recorded that the add-device dialog "needed a human click even then". That is
wrong, and the cause was the `find_window` frame bug fixed earlier today: the dialog was
opening all along and the capture was looking at the window manager's frame, which does not
contain it. Driven from the device explorer's context menu, `Add device` opens under
synthetic input every time.

## How 23-01 was captured, 2026-08-12

On `lesson-09.score`, whose intervals are empty, so the piano roll is the only process.

1. `Ctrl+Shift+D`, right-click the `lesson` device, and `capture.py menu 103 295 --button 3
   --pick 4` for `Add device`.
2. Click `MIDI Input`, then `Midi Through Port-0`, then `Add`. Repeat with `MIDI Output`
   and `Default MIDI Out`.
3. Select the interval, filter the process library to `piano`, double-click
   `Midi > Piano roll`.
4. Double-click the grid once per note. The lanes in the capture format are 33 px apart:
   C at y=1004, D 938, E 871, F 838, G 771, A 704, B 638.
5. Select the process by its slot header and set `MIDI Out` in the inspector.
