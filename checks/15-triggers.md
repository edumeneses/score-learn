# Re-verification note: 15-triggers

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 15-01 | An elastic interval ending at a trigger, with its label | **done**, docs/learn/assets/15/15-01-trigger.png |

See `checks/FIGURES-PENDING.md` for the consolidated list of figures that need
an interactive session, and why each one cannot be produced by the scripted
pipeline.

## Re-verify when the pinned version changes

- That T toggles a trigger on a selected state.
- The dashed-duration drawing before a trigger, which the walkthrough asks the reader to read.
- Minimum, nominal, and maximum duration semantics.
- Start-on-play and the re-trigger option in the trigger inspector.
- That dropping a device parameter on the trigger marker sets its address.

## Claims that depend on external sources

- Grounded in the reference documentation for this topic; see the 'Going further'
  links on the lesson page, which are the pages this lesson was written against.

- 2026-09-16 crop audit: Figure `15-01`: badge 7 pointed at empty space; it now points at the "waits for /lesson/go" label. Re-rendered from the same raw.

## Exercise, 2026-09-30, performed in 3.8.2 on the capture server

- **A dropped excerpt's lead-in usually hangs from the previous excerpt's start, not its
  end.** Dropping a second excerpt level with the first and after its end drew a lead-in
  that looks chained, but the saved file shows it leaving a new state on the *first
  excerpt's start event* (5.25 s long, from 1 s). The drop's magnetism
  (`magneticStates` in `ScenarioDropHandler.cpp`) picks the nearest state in height before
  the drop point, and both of the first excerpt's states share its height; the loop keeps
  the first one found, which is its start state. The part of the lead-in under the first
  excerpt's box is hidden, so the reader cannot see this until the lead-in is selected.
- `T` on the second excerpt's start (`Enable trigger` in the `Object` menu) makes every
  interval ending there non-rigid with `MinNull` and `MaxInf` (`AddTrigger` runs
  `SetRigidity(false)`). The sync inspector then reads `Trigger: Never`. Played, the
  lead-in turns green and dashed and the second excerpt waits; a click on the T marker
  starts it.
- With the minimum null, a click at about 4 s, during the first excerpt, started the
  second excerpt over it. Ticking `Min` in the interval inspector gives `00:00:00 000` and ticking
  `Max` gives 1.2 times the duration (`on_maxFiniteToggled`), drawn as `(` and `)` on the
  interval; **both brackets drag**. With `(` at the first excerpt's end (min 4.4 s) and `)`
  at max 10.1 s, a timed run (`seq.py`) showed a click at 2.6 s ignored, not deferred, and
  the maximum releasing the trigger at 11.1 s with no input.
- The warning's "usually" is deliberate: a reader who dropped the second excerpt at a
  different height may have a lead-in from another state, and the exercise's steps work
  either way.
