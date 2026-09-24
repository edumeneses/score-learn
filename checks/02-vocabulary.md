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
