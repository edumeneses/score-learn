# Re-verification note: 18-cues-and-transport

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 18-01 | Play-from-here in the context menu, above the transport bar | **done**, docs/learn/assets/18/18-01-transport.png |

See `checks/FIGURES-PENDING.md` for the consolidated list of figures that need
an interactive session, and why each one cannot be produced by the scripted
pipeline.

## Re-verify when the pinned version changes

- The transport button order: local play, global play, stop, reinitialise.
- That a cue on the first state fires on start and on reinitialise, and a cue on the last state fires on stop.
- Value compilation on seek, and the two preferences controlling it.
- The start marker in the musical metrics area.
- That JACK is still the only external transport.

## Claims that depend on external sources

- Grounded in the reference documentation for this topic; see the 'Going further'
  links on the lesson page, which are the pages this lesson was written against.

## Corrected 2026-08-11 against the running build

The Play menu names all four transport actions and their shortcuts: Play (space),
Play (global) (Shift+Space), Stop (Return), Reinitialize (Ctrl+Return), plus
Play (Network) and Stop (Network). The Object menu carries Synchronize (Shift+M)
and Merge events, which is the clearest way to find the synchronisation function.

## Exercise, 2026-09-30, performed in 3.8.2 on the capture server

- `phone:/level` dragged from the explorer onto the circle at the right-hand end of the
  root's top line saved in `BaseScenario.EndState` as `phone:/level 0.0`. A listener on
  port 9202 received `/level 0.0` when playback was stopped, and nothing when stop was
  pressed with the score already stopped.
- **The start marker lives in the time-signature strip**, 45 logical pixels above the root
  interval, between the ruler and the document's name. Its context menu offers
  `Add signature change`, `Set start marker`, and `Remove start marker`; the marker draws as
  a grey half disc, and play then starts from it. `setStartMarker` asserts on the interval
  that carries the time signature, which every document made by `File > New` has
  (`ScenarioDocumentModel` gives the root 4/4 and `HasTimeSignature`); a generated document
  without `HasSignature` would have none, so `gen.py` in the session scratchpad gained it.
- Played from a marker at 6.5 s, just after the Lesson 15 trigger, the seek released the
  trigger and **both branches ran**, because both events were at the default offset
  behaviour `True`. With the fourth excerpt's event set to `False`, only the tremolo ran,
  with the pointer on the side that would have chosen the other. Walkthrough step 6 and the
  common mistake about offset behaviour now say so.
- "Unsynchronize, plainly" now names the control: `Desynchronize`, the second button at the
  top of a state's inspector (`splitFromNode`).
