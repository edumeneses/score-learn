# Re-verification note: 12-recording-live-input

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 12-01 | The Record submenu in the scenario's context menu | **done**, docs/learn/assets/12/12-01-record-menu.png |

See `checks/FIGURES-PENDING.md` for the consolidated list of figures that need
an interactive session, and why each one cannot be produced by the scripted
pipeline.

## Re-verify when the pinned version changes

- The menu entry 'Record automations from here'.
- That recording starts on the first received message by default, and the preference that changes it.
- That the CSV recorder still writes to a file.

## Claims that depend on external sources

- Grounded in the reference documentation for this topic; see the 'Going further'
  links on the lesson page, which are the pages this lesson was written against.

## Exercise, 2026-09-29, performed in 3.8.2 on the capture server

- A sound's `Gain` sub-port has an `Address` field (an earlier module B note said it did
  not; that was wrong). With it set to `phone:/fader`, RMS read 0.00 until `fader.py` ran and
  then rose with the ramp to about 0.17.
- `Record automations from here` with `phone:/fader` selected records an automation in a
  new interval whose start state has no previous interval, so it is **out of time and never
  plays**: nothing reached `display.py` on playback. Selecting its start state, `Ctrl+click`
  on the excerpt's start state, and `Shift+M` (Synchronize) moved it onto the excerpt's
  instant; playback then sent the ramp to port 9202 and RMS followed it (0.03, 0.07, 0.10,
  0.16), so an inlet address follows values that an automation inside score writes.
- Walkthrough step 6 now says to attach the recording before playing it back. The
  paragraph on recordings' file size went to make room, since the density concept already
  covers their cost.
