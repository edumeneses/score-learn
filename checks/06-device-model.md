# Re-verification note: 06-device-model

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 06-01 | The protocol chooser and a device's edit dialog | pending: needs interaction (right-click menu and modal dialog) |

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
