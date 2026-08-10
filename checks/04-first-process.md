# Re-verification note: 04-first-process

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 04-01 | lesson-04.score: one interval, one automation, slot header showing address and range | done, docs/learn/assets/04/04-01-first-automation.png |

Figures are produced by the pipeline described in the README: `scripts/mkscore.py`,
`scripts/capture.py`, then `scripts/annotate.py` against a spec in `figures/`.
Anything marked pending needs synthetic input, which requires an unlocked session.

## Re-verify when the pinned version changes

- That `automation (float)` is still the library name of the process.
- The address-assignment gesture: dragging a parameter from the device explorer onto the inspector's address field.
- Curve editing: double-click adds a breakpoint, Shift+Drag bends a segment.
- The blue dot at the slot's top right: plain drag extends the slot preserving automation length, Cmd+Drag scales the automation.
- Full-size edit by double-clicking the process name, and Ctrl+Alt+Up / Cmd+Up to leave it.

## Claims that depend on external sources

- The gestures and modifiers come from the reference page on writing automations. The Cmd+Drag and Cmd+Up bindings are stated there in macOS form; verify the Linux and Windows equivalents before the video is recorded.
