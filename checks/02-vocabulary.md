# Re-verification note: 02-vocabulary

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 02-01 | One instant zoomed: state, event, trigger | **done**, docs/learn/assets/02/02-01-instant.png |

Figures are produced by the pipeline described in the README: `scripts/mkscore.py`,
`scripts/capture.py`, then `scripts/annotate.py` against a spec in `figures/`.
Anything marked pending needs synthetic input, which requires an unlocked session.

## Re-verify when the pinned version changes

- Every definition against the interface: that clicking each object shows what the walkthrough says it shows.
- That `T` still toggles a trigger on a selected state, and `Ctrl+Alt+F` / `Ctrl+Alt+U` still fold and unfold.
- That the inspector still separates structural context from parameters, since step 3 depends on it.
- The claim that a scenario is itself a process, which the whole nesting explanation rests on.

## Claims that depend on external sources

- Definitions are reconciled with the project glossary; that page is incomplete (several headings have no body), so divergence is possible.
- The 'elements I do not touch' and trigger-unfamiliarity findings come from the SAT UI/UX study report.

- 2026-09-24: `02-01` re-cropped from `raw-00-01c.png`, the capture of the corrected `lesson-00.score` (elastic `Approach`, so the trigger now waits). **To verify:** the Trigger definition says the interface "draws the preceding interval's duration as a dashed line". In the corrected document `Approach` (min 6 s, max infinite) ends in a `(` bracket at the trigger and shows no dashes, whereas the root in the old capture (14 s, max 15 s) drew `( - - - )`. Dashes may only appear between a finite minimum and maximum, or only while playing. Check against the interface with playback running before changing the prose.
- 2026-09-25: played on the capture server, the waiting trigger draws `Approach` solid to
  its end and highlights the instant's vertical line; no dashes appear. That does not yet
  settle the claim, because `Bright`'s slot covers the region where a dashed continuation
  of `Approach` would be drawn. Settle it on a document where nothing covers the waiting
  interval's continuation, for instance `lesson-15.score`, whose `Approach` waits between
  5 and 8 s.
- 2026-09-25, later: **settled, and the claim holds.** `p4-solution.score`'s `Idle` now waits between 4 s and 60 s, and score draws that range as a dashed continuation of the interval, both at rest and while the trigger waits; nothing covers it there. In `lesson-00.score` the same continuation runs behind `Bright`'s slot, which is why it could not be seen.
