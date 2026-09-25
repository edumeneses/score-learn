# Re-verification note: 16-conditions-and-branching

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 16-01 | Two conditional branches from one instant plus a parallel layer | **done**, docs/learn/assets/16/16-01-branching.png |

See `checks/FIGURES-PENDING.md` for the consolidated list of figures that need
an interactive session, and why each one cannot be produced by the scripted
pipeline.

## Re-verify when the pinned version changes

- The split-condition function, without which both branches run.
- That Delete/Backspace removes a selected condition.
- Offset behaviour (true / false / live) on conditions.
- That conditions live on events and messages on states.

## Claims that depend on external sources

- Grounded in the reference documentation for this topic; see the 'Going further'
  links on the lesson page, which are the pages this lesson was written against.

## Corrected 2026-08-11 against the running build

The Object menu offers Add Condition (C), Remove Condition (Shift+C), Merge events,
and Synchronize (Shift+M). An earlier draft named a 'split condition' function; the
mechanism is real but those are the names the interface uses.

- 2026-09-16 crop audit: Figure `16-01`: crop now starts above the `Approach` header instead of cutting through its curve. Re-rendered from the same raw.

- 2026-09-25: **`lesson-16.score`'s conditions were ignored until today**, so both `High` and `Low` ran whatever the input, contradicting step 1. They were written `{ lesson:/level >= 0.5 }`; score reads an address in a condition only between percent signs, `{ %lesson:/level% >= 0.5 }`, which is the form in upstream's shipped examples and the one `mkscore.py`'s `cond()` now writes. Verified in lesson 00, whose branches have the same shape: with the old form both ran and no condition bracket was drawn; with the new one only the true branch ran, its bracket drawn green and the other's red. The inspector shows a condition as three fields (address, relation, value) with no percent signs, so the lesson's `sensors:/level > 0.5` matches what a reader sees. `16-01` re-shot: the brackets now appear, badge 7 points at one, badge 4 moved to the shared instant.
