# Re-verification note: 03-interface-and-transport

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 03-01 | The whole window with lesson-00.score open: explorer panel, panel switch, scenario editor, time ruler, breadcrumb, inspector, transport | done, docs/learn/assets/03/03-01-window-regions.png |

Figures are produced by the pipeline described in the README: `scripts/mkscore.py`,
`scripts/capture.py`, then `scripts/annotate.py` against a spec in `figures/`.
Anything marked pending needs synthetic input, which requires an unlocked session.

## Re-verify when the pinned version changes

- Every shortcut quoted: Ctrl+Shift+D/P/B/L/C/G, space, Enter, Ctrl+Alt+Up, Ctrl+Alt+U, Ctrl+Alt+F, Esc, and the two zoom gestures.
- The four explorer faces and their order along the bottom of the panel.
- That the breadcrumb under the time ruler is still clickable and still reads `<document> /`.
- The transport bar contents: position, play, stop, speed, volume.
- Figure 03-01 badge coordinates, which are pixels in the raw capture.

## Claims that depend on external sources

- The controls-and-shortcuts 2/5 rating, the lost-panels report, and the accidental-view-entry report all come from the SAT UI/UX study report.
