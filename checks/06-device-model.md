# Re-verification note: 06-device-model

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 06-01 | The device explorer's menu, with Add device (Ctrl+B) | **done**, docs/learn/assets/06/06-01-device-menu.png |

Figures are produced by the pipeline described in the README: `scripts/mkscore.py`,
`scripts/capture.py`, then `scripts/annotate.py` against a spec in `figures/`.
Anything marked pending needs synthetic input, which requires an unlocked session.

## Re-verify when the pinned version changes

- The protocol list in the table, against the reference devices table. Protocols are added between releases.
- That right-click then Edit still opens device settings, and that the OSC device still shows a listening port plus a destination host and port.
- That selecting a parameter still opens an inspector at the bottom of the explorer panel, and that values can be written from there.
- The claim that a document opens with its device declarations intact and no equipment attached.

## Claims that depend on external sources

- The device list comes from the reference devices table include. The finding that devices are misconfigured through misunderstood parameters, and the recommendation to teach devices with examples, come from the SAT UI/UX study report.

## Protocol list re-read 2026-08-11 from the running build

The `Add device` dialog groups protocols as: Network (OSCQuery, OSC, Minuit, CoAP, MQTT,
LSL, Bitfocus); Lights (Artnet, NeoPixel LEDs); Audio (Audio); Hardware (BLE, Evdev,
Joystick, MIDI Controller, MIDI Input, MIDI Output, Raw I/O, Serial, Wiimote); Video
(Camera input, NDI Input, NDI Output, Sh4lt Input, Sh4lt Output, Shmdata Input, Shmdata
Output, Window); Web (HTTP, and more below the scroll). LSL, Bitfocus, NeoPixel LEDs,
Evdev, MIDI Controller, NDI and Sh4lt are in the build but absent from the reference
devices table, so the lesson's table now says it is read from the build.
