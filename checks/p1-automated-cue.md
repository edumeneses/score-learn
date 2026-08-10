# Re-verification note: p1-automated-cue

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| p1-01 | p1-solution.score: Rise, Hold, and Fall chained, four automations, states at both ends | done, docs/learn/assets/p1/p1-01-cue-structure.png |

Figures are produced by the pipeline described in the README: `scripts/mkscore.py`,
`scripts/capture.py`, then `scripts/annotate.py` against a spec in `figures/`.
Anything marked pending needs synthetic input, which requires an unlocked session.

## Re-verify when the pinned version changes

- That p1-solution.score still loads and still shows two stacked slots in Hold.
- The stacked-automation behaviour quoted in the brief: frontmost red, others greyed, slot address bar to choose, right-click to remove.
- That folding with Ctrl+Alt+F still produces a readable three-section structure, which the finish list depends on.

## Claims that depend on external sources

- The stacking behaviour comes from the reference page on states and automations in practice.
