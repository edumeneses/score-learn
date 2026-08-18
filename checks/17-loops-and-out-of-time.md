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
