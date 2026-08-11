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
