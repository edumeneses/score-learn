# Re-verification note: 28-audio-reactive-visuals

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 28-01 | The three-object chain with a signal display, beside the image it drives | **done**, docs/learn/assets/28/28-01-audio-reactive-chain.png |

See `checks/FIGURES-PENDING.md` for the consolidated list of figures that need an
interactive session or media, and why each cannot be produced by the scripted
pipeline.

## Re-verify when the pinned version changes

- The envelope's two outputs and their characters.
- That propagation must be re-enabled to keep hearing an analysed source.
- The small mapping object recommended for scaling the envelope.

## Claims that depend on external sources

- Grounded in the reference pages linked under 'Going further' on the lesson page.

## Corrections made by the figure, 2026-08-12

The lesson said the envelope has two outputs, "the first a root-mean-square measure, the
second a peak measure". That is not how 3.8.2 presents it. `Analysis > Envelope` holds
**three separate processes**:

- **`RMS`**, "provided by ossia score, Gist library, 3 inputs, 1 output". One audio inlet
  named `in`, controls `Gain` and `Gate`, one value outlet named `out`. This is the object
  the lesson means.
- **`Peak`**, its sibling, the same shape.
- **`Envelope Follower (audio)`**, "provided by Kevin Ferguson", whose ports are `Audio In`,
  `Millis (up)` 50.0, `Millis (down)` 15.0, and **`Audio Out`**. It is a sample-level
  follower and its output is audio, so it is the wrong object for driving a control, and it
  is the one whose name most invites the mistake.

The lesson now says the two measures are two processes, step 2 names `RMS` and `Peak`, and
step 9 swaps the process rather than the output.

## Grounded by the figure

- **The rendered image needs no window device.** As with 26-01, the shader's own inspector
  previews its texture output, and the chain in this figure has no `Window` device at all.
- **The chain builds itself.** Selecting a process and double-clicking the next in the
  library connected sound to `RMS`, `RMS` to `Signal display`, `RMS` to `Micromap`, and
  `Micromap` to the shader, each time by first port.
- **The signal display draws over the source.** Added after `RMS`, it lands in the sound's
  slot and draws its reading as a white line on top of the waveform, which makes "the
  reading follows the loudness" visible without any extra work.
- **`Micromap` defaults to `x / 127`**, a MIDI-shaped scaling. For an RMS reading it wants
  raising; the figure uses `x * 20`.

## How 28-01 was captured, 2026-08-12

On `lesson-20.score`. Select the sound process, then double-click in turn: `Analysis >
Envelope > RMS`, `Monitoring > Signal display`, `Control > Mappings > Micromap`, and
`Visuals > ISF Shader > generator > Kaleidolines`, re-selecting `RMS` before the micromap.

Two interactions were needed that no earlier figure had used, both now in `CLAUDE.md`:

- **Cables can be drawn.** Chaining connects by first port, which here put the micromap's
  output on the shader's `invert`, a toggle. Dragging from the micromap's outlet dot to the
  `zoom` inlet dot made a second cable; clicking the unwanted one and pressing `Delete`
  removed it.
- **The nodal slot has a fit control**, the fourth small icon at its left edge, which
  scrolls the graph so every node is visible. Its bottom edge drags down to make room, which
  is what allows a two-row layout when a chain is wider than the interval.

Selecting a node by clicking its title **does** work; the earlier note that it does not came
from a case where a floating editor window covered the point being clicked.
