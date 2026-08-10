# Re-verification note: 09-states-snapshots-presets

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 09-01 | lesson-09.score: three states, two empty intervals, a cue list with no processes | done, docs/learn/assets/09/09-01-cue-list.png |

Figures are produced by the pipeline described in the README: `scripts/mkscore.py`,
`scripts/capture.py`, then `scripts/annotate.py` against a spec in `figures/`.
Anything marked pending needs synthetic input, which requires an unlocked session.

## A finding about the capture format

score fits a document to the editor's width on load, and the editor extends to about
x=3225 in the capture format, which is wider than the panels suggest. Two figures were
first cropped at x=3020 and silently lost their last state. Crops for a full-width
document must reach 3260. `scripts/mkscore.py` writes a computed `Zoom` for correctness,
but the fit on load is what actually determines the layout.

## Re-verify when the pinned version changes

- Ctrl+L (snapshot, adds from the explorer selection) against Ctrl+R (refresh, updates stored values). The distinction is the core of the lesson.
- That auto-sequence is still off by default and still lives in Settings under the user interface tab.
- That the blue + beside a state still chains a new state, with and without auto-sequence.
- That dropping parameters onto an existing state adds them and replaces same-address values.
- The floating-cue setup named at the end: a trigger with auto-trigger and start-on-play.

## Claims that depend on external sources

- The two camera icons, their shortcuts, and the floating-cue configuration come from the reference cues page. Auto-sequence comes from the states-and-automations-in-practice page.
