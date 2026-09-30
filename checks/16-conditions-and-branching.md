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

## Exercise, 2026-09-30, performed in 3.8.2 on the capture server

- **Dropping a sound on a state that already has a next interval** creates a new state on
  the same event, 0.1 lower, and an interval holding the sound from it
  (`DropProcessOnState`), with no lead-in. The drop has to land on the circle itself: on the
  circle's centre it went into the tremolo's interval as a second slot; on its lower left
  edge it made the branch. The new interval overlaps the tremolo and can be dragged down
  by its top line.
- Played with both on one event, both ran (both top lines progressed).
- **The split is the scissors button at the top of the state inspector**, help text
  `Split condition` (`splitFromEvent`). The six buttons there are split, `Desynchronize`,
  snapshot (`Ctrl+L`), refresh (`Ctrl+U`), trigger (`T`), and condition (`C`). A click on a
  state circle sometimes selects the sync instead; the object tree then lists the states.
  Walkthrough step 6 now names the button.
- `C` sets a condition of `Always`; the event inspector's relation list is `=`, `≠`, `>`,
  `<`, `≥`, `≤`, `Contains`, `Pulse`, `Always`, `Never`, after which address and value fields
  appear. `Window:/cursor/scaled@[0]` with `≥ 0.5` and `< 0.5` saved as
  `{ %Window:/cursor/scaled@[0]% >= 0.5 }` and `< 0.5`. Clicking a condition bracket selects
  its event.
- With the pointer parked on the left quarter of the output window (`winpt.py`) and the
  trigger released by its maximum, only the tremolo progressed and the other branch drew
  red; on the right quarter, the reverse.
- **Offset behaviour is `True`, `False`, or `Expression`, and every event starts at
  `True`** (`EventModel` initialises `m_offset{OffsetBehavior::True}`). A seek past the
  branch instant therefore ran both branches (checked in Lesson 18's exercise). The
  Concepts paragraph now says so.
