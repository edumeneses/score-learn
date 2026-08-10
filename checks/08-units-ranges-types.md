# Re-verification note: 08-units-ranges-types

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 08-01 | Crop of a slot header from lesson-00.score showing a destination address next to Min and Max | done, docs/learn/assets/08/08-01-address-and-range.png |

Figures are produced by the pipeline described in the README: `scripts/mkscore.py`,
`scripts/capture.py`, then `scripts/annotate.py` against a spec in `figures/`.
Anything marked pending needs synthetic input, which requires an unlocked session.

## Re-verify when the pinned version changes

- Every suffix in the syntax table: @[1], @[1][0], @[color.rgb.r], @[angle.radian], and that a bare address still writes to all members of an array.
- That zero-based indexing still holds.
- That the slot header still prints Min and Max, which figure 08-01 crops.
- Clip-mode behaviour at a boundary, which step 4 asks the reader to observe.

## Claims that depend on external sources

- The suffix syntax and the unit-conversion mechanism come from the reference unit-system page. The list of supported units lives in the libossia documentation and is versioned separately.
