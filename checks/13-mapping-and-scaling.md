# Re-verification note: 13-mapping-and-scaling

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 13-01 | The conditioning pipeline as a patch | **done**, docs/learn/assets/13/13-01-pipeline.png |

See `checks/FIGURES-PENDING.md` for the consolidated list of figures that need
an interactive session, and why each one cannot be produced by the scripted
pipeline.

## Re-verify when the pinned version changes

- The library sections 'Control > Mappings' and 'Control > Data Processing'.
- That a mapping needs a running interval, and the never-satisfied-trigger idiom.
- Calibrator, range filter, smooth, rate limiter, Micromap behaviour.

## Claims that depend on external sources

- Grounded in the reference documentation for this topic; see the 'Going further'
  links on the lesson page, which are the pages this lesson was written against.

## Confirmed 2026-08-11 against the running build

The library path Control > Mappings is correct, and contains: ADSR, Accumulator,
Angle mapper, Array Flattener, Array Recombiner, Array Value Combiner, Array tool,
Arraymap, Calibrator, Combine inlets, Counter, Easetanbul, Empty audio/midi/value
mapper, Exp Smoothing, Expression Value Filter, Mapping curve, Mapping tool,
Micromap, Multi-choice, Range Filter, Rate Limiter, Repetition Filter, Smooth.
The smoothing object is named Exp Smoothing.

- 2026-09-16 crop audit: Figure `13-01`: node titles are clipped at the nodal slot top edge in the raw itself, so no crop recovers them; re-shoot queued in `checks/FIGURES-PENDING.md` (rebuild the patch, fit the graph, then shoot).

- 2026-09-17: `13-01` re-shot. Patch rebuilt on `lesson-04.score`: click the automation's slot header to select it, type each name into the process library search with `typeinto.py`, double-click the single result (Calibrator, Range Filter, Mapping curve, Exp Smoothing; each new process is selected, so the next chains after it), then the nodal slot's fourth small icon fits the graph and the titles clear the slot's top edge.

## Exercise, 2026-09-29, performed in 3.8.2 on the capture server

- With the `Gain` port selected (address `phone:/fader`), double-clicking
  `Control > Mappings > Mapping curve` inserted the curve, moved the address to its `In`,
  and cabled its output to `Gain`: the refactoring Lesson 11 describes.
- `Window:/cursor/scaled@[1]` typed into `In`, and `Target` set to `Min 1`, `Max 0`: with
  the pointer at the top of the output window RMS read 0.15, at the middle 0.07, a quarter
  down 0.13. The stored document keeps `TargetMin 1`, `TargetMax 0`.
- Clicking the cable and double-clicking `Smooth` inserted it (`ValueFilter`, OneEuro,
  `Amount` 0.1, `Continuous` off). What `Continuous` and `Amount` do is taken from
  upstream's `processes/smooth.md`; the glide itself was too fast to time with screenshots.
- The mouse replaces the microphone that the plan first proposed, since audio input cannot
  be exercised under the capture server's Dummy driver and RMS of a stereo input is a
  `vec2f`, whose conversion by a mapping curve is untested.
