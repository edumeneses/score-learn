# Re-verification note: 21-effects-and-plugins

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 21-01 | An effect chain in the nodal view with a hosted plug-in | **done**, docs/learn/assets/21/21-01-effect-chain.png |

See `checks/FIGURES-PENDING.md` for the consolidated list of figures that need an
interactive session or media, and why each cannot be produced by the scripted
pipeline.

## Grounded by the figure, 2026-08-11

- **The hosted formats are, exactly:** `Airwindows`, `CLAP`, `Faust`, `JSFX`, `LV2`,
  `PureData`, `VST`, and `VST 3`, listed under `Plugins` in the process library. The
  lesson previously said only "several external formats, VST among them"; it now names
  them.
- **The plug-in blocker is gone.** `jsfx_pack`, from score's own package manager, supplies
  free JSFX effects, so the lesson no longer depends on the reader owning one. The figure
  uses `Plugins > JSFX > loser > MGA_JSLimiterST`.
- **Fast chaining works exactly as the lesson claims.** With a process selected,
  double-clicking a library entry adds the new process *and* cables it after the selected
  one, and leaves the new one selected so the next double-click continues the chain. The
  figure's chain was built with two double-clicks and no cable drawn by hand.
- **A hosted plug-in's parameters are ports.** The inspector lists `Threshold (dB)`,
  `Release (ms)`, `Link Stereo (%)`, and `Ceiling` under `Inputs`, beside `Audio In` and
  `MIDI In`, with `Audio Out`, `MIDI Out`, and a `Propagate` toggle under `Outputs`.

## Re-verify when the pinned version changes

- The hosted plug-in formats.
- Fast chaining by double-clicking a library process with another process selected.
- Polyphony: mono processors replicated per channel, and list-valued controls. Documented for Faust and selected processes only.

## Claims that depend on external sources

- Grounded in the reference pages linked under 'Going further' on the lesson page.

## How 21-01 was captured, 2026-08-11

No document was authored for this figure; it is built on `lesson-20.score`, which already
ships a sound file.

1. Select the sound process in the timeline.
2. Filter the process library, `Ctrl+Shift+P`, to `flanger`, and double-click the built-in
   `Audio > Effects > Flanger`. It is added *and* cabled after the sound file, in a second
   slot that score creates in the nodal view.
3. Filter to `JSLimiter` and double-click `Plugins > JSFX > loser > MGA_JSLimiterST`, which
   chains after the flanger.
4. Drag the slot's bottom edge down to give the graph room, then drag the two node titles
   apart: score places a chained node on top of its predecessor, so they overlap until
   moved.

Two things to know before repeating this:

- **A node dragged past the interval's right edge disappears.** The nodal graph is clipped
  to the interval's width in the timeline, which for `Plays once` is about 1,226 px in the
  capture format. Dragging the second node 756 px right put it out of view; `Ctrl+Z` undoes
  the move.
- **The zoom buttons at the slot's left edge did not change the node size** when clicked,
  so laying the graph out means moving nodes, not zooming.
