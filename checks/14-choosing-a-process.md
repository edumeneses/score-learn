# Re-verification note: 14-choosing-a-process

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 14-01 | The process library filtered, showing Control > Mappings | **done**, docs/learn/assets/14/14-01-library-search.png |

See `checks/FIGURES-PENDING.md` for the consolidated list of figures that need
an interactive session, and why each one cannot be produced by the scripted
pipeline.

## Re-verify when the pinned version changes

- Every object named in the decision table still exists and is in the stated family.
- That F1 opens the reference page for a selected library process.
- The library's top-level sections, since the study recommended reorganising them.

## Claims that depend on external sources

- Grounded in the reference documentation for this topic; see the 'Going further'
  links on the lesson page, which are the pages this lesson was written against.

## Exercise, 2026-09-29, performed in 3.8.2 on the capture server

- RMS chained after a sound, then Value display: `vec2f: [0.12, 0.11]`, one level per
  channel. The decision table's loudness row now names RMS or peak under
  `Analysis > Envelope`, because `Envelope Follower (audio)` beside them returns audio.
- Signal display chained after an LFO draws the wave over the sound's waveform, five
  cycles in about 4.6 s at 1 Hz.
- `Timing > Audio > Metronome` dropped on empty timeline gets its own interval; its outlet
  is `Audio Out` with `Propagate` on, plus `Pulse Out`, and its description reads
  "Generates sound according to the current beat". Not heard, since the capture server
  runs the Dummy driver.
