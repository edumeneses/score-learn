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
