# Re-verification note: 30-expressions-and-jit

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 30-01 | An expression object's editor beside its result | **done**, docs/learn/assets/30/30-01-expression-object.png |

See `checks/FIGURES-PENDING.md` for the consolidated list.

## Re-verify when the pinned version changes

- The expression family names, including the micromap and the array generator and mapper.
- Bytebeat and C++ JIT availability.
- That the shared editor still refuses invalid code.

## Claims that depend on external sources

- Grounded in the reference pages linked under 'Going further' on the lesson page.

## Grounded by the figure, 2026-08-11

- **The expression family, by library path.** Filtering for `expression` returns exactly
  four: `Control > Mappings > Expression Value Filter`,
  `Control > Generators > Expression Value Generator`,
  `Audio > Utilities > Expression Audio Filter`, and
  `Audio > Utilities > Expression Audio Generator`. `Micromap` is a separate entry under
  `Control > Mappings`, so the lesson's name for it is right.
- **The formula is edited on the process**, in a text field on the node, not in a separate
  editor window. The lesson previously implied the shared script editor was used for these
  too; only the JavaScript and C++ routes open a window.
- **The variables**, from the library's own description of `Expression Value Filter`:
  `a`, `b`, `c` (the three parameters on the object), `t` in samples, `dt` the delta, `pos`
  the position in the parent, and `x` the value. The description also names the engine,
  ExprTK by Arash Partow, and gives its documentation at
  `http://www.partow.net/programming/exprtk`. The object is billed as 5 inputs, 1 output.
- **Chaining rewires the destination.** With Lesson 04's automation selected,
  double-clicking `Expression Value Filter` cabled the automation into the filter's `in`
  *and* moved the automation's `lesson:/level` address onto the filter's `out`. The
  automation slot header then reads
  `Automation (float).2 -> in (Expression Value Filter)`. This is what makes step 1's
  "insert between a source and a destination" a single interaction.

## How 30-01 was captured, 2026-08-11

On `lesson-04.score`. Select the automation, filter the library to `expression`,
double-click `Expression Value Filter`, then click into the formula field on the node and
type `sqrt(x) * 0.8 + 0.1`, which is the lesson's own example. `Ctrl+Shift+D` for the
device explorer, expand `lesson`, and play: `level` then reads `0.893403` at the end of the
fade, which is `sqrt(0.99) * 0.8 + 0.1` to three figures.

The document was **not** saved. `lesson-04.score` on disk is unchanged, and the figure is
reproducible from it in four interactions.

Playback runs with the `Dummy (No audio)` driver, so no audio device is needed to capture
a figure that requires the engine to be running.
