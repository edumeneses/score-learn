# Re-verification note: 17-loops-and-out-of-time

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 17-01 | A loop built from a transition, and out-of-time material | **done**, docs/learn/assets/17/17-01-loop-and-out-of-time.png |

## Re-verify when the pinned version changes

- That transitions are instantaneous intervals and can connect backwards.
- That transitioning to an instant re-executes everything attached to it, and that the smallest loop restarts first.
- The maximum-duration idiom for repetition counts.
- Start-on-play for out-of-time material, and the hover play/stop buttons during playback.

## Claims that depend on external sources

- Grounded in the reference documentation for this topic; see the 'Going further'
  links on the lesson page, which are the pages this lesson was written against.

## Corrected 2026-08-11 against the running build

Encapsulate (Ctrl+Alt+E) and Decapsulate (Ctrl+Alt+D), in the Object menu, are the
commands that put a selection into a sub-scenario and take it back out.

## The two shapes, learned 2026-08-17

Edu drew both structures by hand, in `/media/Storage/temp/`, and `mkscore.py` was taught
them from the saved JSON. It now emits `lesson-17.score` with no interaction at all, so
this figure is re-shootable at the next version pin like the early ones.

**A transition is an interval with `"Graphal": true`** and every duration zero. It carries
none of an ordinary interval's machinery, no `Inlet`, `Outlet`, `Processes`, racks,
`Signatures`, `Zoom` or `ViewMode`, because it has no duration in which anything could
run. Its `StartState` is at the **later** instant and its `EndState` at the **earlier** one,
which is what makes it point backwards:

```json
{"ObjectName": "Scenario::IntervalModel", "id": 3, "Graphal": true,
 "DefaultDuration": 0, "MinDuration": 0, "MaxDuration": 0, "GuiDuration": 0,
 "Speed": 1.0, "Rigidity": true, "MinNull": false, "MaxInf": false,
 "StartState": 3, "EndState": 4, "StartDate": 7585200000,
 "HeightPercentage": 0.366}
```

The two instants it joins each carry **two** states: the ordinary chain state, and one end
of the transition. The departure state has `PreviousConstraint: null` and
`NextConstraint: <transition id>`; the arrival state has them the other way round. Both
appear in their instant's event `States` list.

**Out-of-time material has no special marker at all.** It is simply a chain that nothing
connects to the instant the score starts from: its first state has no incoming interval.
The trigger that makes it fireable is a timesync with `Active: true`, `AutoTrigger: true`
and `Start: true` together; `AutoTrigger` is the interface's **start on play**, confirmed
against `examples/basics/osc.score`, which is the only shipped example using it.

## Why the first generated version played once and stopped

Worth recording, because the document looked correct and was not.

A generated document ended at its root's duration however its contents looped. Two things
were missing, and **both** are needed:

1. `"MaxInf": true` on the root interval, so its maximum is not a bound;
2. `"Active": true` on the **base scenario's `EndTimeNode`**, which makes the document's
   closing instant a trigger that waits on the never-true expression every sync carries.

The second is the one that mattered. This is **not** something a reader does: both of Edu's
hand-built files carry it, including the one with no transition in it, so it is simply what
score writes into a new document. `mkscore.py` had been writing a more tightly bounded root
than score's own default, which no previous lesson noticed because every other example
document is meant to end. `document(..., endless=True)` is the opt-in.

The lesson's claim that "a loop with no exit runs forever" is therefore correct as written
for anyone working in the interface, and needed no correction.

## 2026-09-30: the walkthrough's bounded loop was wrong, and two other corrections

- **A trigger with a maximum on the loop's own closing instant does not bound the loop.**
  Built as step 3 described (one-shot looped by a transition, `T` on its end, max 3 s),
  every pass stretched to the maximum and looped again; it was still looping at 16.9 s.
  Upstream's "Repetition amount" animation (`repetition-ammount.gif`) shows the idiom it
  means: the loop sits inside a sub-scenario, and the trigger and maximum are on the end
  of the **interval that contains it**. Built that way on `lesson-17.score`'s `Phrase`
  (container max 10 s from 3 s), the phrase restarted at 9 s and the container released at
  13 s, after which the phrase stopped. Concepts ("Repetition counts"), walkthrough steps
  2 to 4, and "Which bound to choose" were rewritten to match.
- **Encapsulate needs the circle between two chained intervals in the selection.** With
  `Intro` and `Phrase` selected by `Ctrl+click`, `Object > Encapsulate` did nothing and the
  log printed `Too much entry states`; with the middle circle added, it made one container
  from the first circle. A rubber band that also takes the outer circles makes a box joined
  to nothing (`EncapsulateElements` falls back to `createBox`).
- **Draw the loop inside the container from its full view.** In the timeline the nested
  interval's circles sit under the container's edges and show no pluses on hover;
  double-clicking the container's name opens it full size, where the red plus drew the
  transition at once, and the document's name in the breadcrumb returns.
- **A transition is drawn with the red plus** below a hovered or selected state (help
  `Create a graph link`), next to the yellow `Create an interval` and the teal
  `Create a sequence` (`StateMenuOverlay.hpp`). Dragged onto an earlier state it saved as a
  `Graphal` interval between the two instants. Pressing where the plus is drawn but before
  it has appeared dragged the state instead and shrank the one-shot to zero, which
  `Ctrl+Z` undid.
- **`Start on play` is the right-hand button of the sync inspector and saves as `Start`;
  the left-hand one is `Auto-trigger` and saves as `AutoTrigger`.** Its help text: an
  auto-trigger sync "will directly restart their following floating scenario upon
  triggering. Else, triggering the timesync will stop the following subgraph". The note
  above, and `CLAUDE.md` and `mkscore.py`, had called `AutoTrigger` start on play; that was
  inferred from `examples/basics/osc.score`, which sets both. With `Active` alone, a click
  on the floating one-shot's marker did nothing; with `Start` added, it played on each
  click and never by itself. `lesson-17.score` sets all three, which is still correct.

## Exercise, 2026-09-30

- A one-shot from `one_shots` (0.2 to 4 s long, 4,096 files) looped by a transition
  repeated as a pulse. `C` on its closing circle put `{ %Window:/cursor/scaled@[1]% < 0.5 }`
  on the event that holds both the one-shot's end and the transition's departure; with the
  pointer high the bracket drew green and the pulse repeated, and after lowering it the
  bracket drew red and the one-shot stopped restarting.
- A second one-shot's lead-in selected and deleted left it joined to nothing; `T` plus
  `Start on play` armed it (its edge drew yellow at 1.8 s), and a click at 2.8 s played it.
