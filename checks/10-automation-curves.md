# Re-verification note: 10-automation-curves

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 10-01 | Four curve shapes: linear, accelerating, decelerating, two-segment hold | **done**, docs/learn/assets/10/10-01-curve-shapes.png |

See `checks/FIGURES-PENDING.md` for the consolidated list of figures that need
an interactive session, and why each one cannot be produced by the scripted
pipeline.

## A finding about generated curves

A curve's **last segment must extend slightly past x = 1** or score draws the curve
flat, or not at all. score's own example documents use `End: [1.0119, ...]`, and
reproducing that is what made the four shapes in this figure render.
`scripts/mkscore.py` now emits `1.0119` for the implicit single segment. Several
earlier lesson documents were generated with `1.0` and have been regenerated.

## Re-verify when the pinned version changes

- The four creation routes, especially interpolate-states and right-click on a value port.
- That tween mode is still an inspector toggle on the automation.
- That changing min/max does not redraw the curve.
- The 2D spline and gradient variants.

## Claims that depend on external sources

- Grounded in the reference documentation for this topic; see the 'Going further'
  links on the lesson page, which are the pages this lesson was written against.
