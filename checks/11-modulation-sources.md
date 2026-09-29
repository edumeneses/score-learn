# Re-verification note: 11-modulation-sources

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 11-01 | An automation into an LFO, then two conditioning objects | **done**, docs/learn/assets/11/11-01-lfo-patch.png |

See `checks/FIGURES-PENDING.md` for the consolidated list of figures that need
an interactive session, and why each one cannot be produced by the scripted
pipeline.

## Re-verify when the pinned version changes

- The three nodal insertion interactions (cable selected, port selected, process selected) and that a new process stays selected.
- Alt+Shift+G to hide cables.
- That LFOs follow an interval's musical metrics automatically.
- That a patch only runs while its interval runs.

## Claims that depend on external sources

- Grounded in the reference documentation for this topic; see the 'Going further'
  links on the lesson page, which are the pages this lesson was written against.

## Exercise, 2026-09-29, performed in 3.8.2 on the capture server

- A second excerpt's `Gain` sub-port, selected, then `LFO` double-clicked in the library:
  score adds the LFO in a new nodal slot under the waveform and cables it to `Gain`
  (`Inlet 10000` in the file). RMS after the sound swung between 0.00 and 0.18 at 1 Hz.
- The same gesture on `Pan` cables to `Inlet 10001`, but `Pan` is stored as a per-channel
  pair (`[1.0, 1.0]`) and a float LFO into it changed neither channel's level, so the
  exercise does not use it.
- Right-click on the LFO's `Freq.` port, `Create automation`: header
  `Min: 0.01 Max: 100`, flat at the bottom. `Min 1`, `Max 8` typed in the inspector and the
  last point dragged up gives a ramp from 1 to 8.
- **The inspector misreports some controls.** `Freq.` shows 14.919 while the stored value
  and the node read 1.0; a click on the inspector slider showed 43.044 and the saved value
  stayed 1.0. Smooth's `Freq (1e/LP)` and `Cutoff` show 252.095 and 2.889 against 120 and 1
  on the node. Linear 0 to 1 controls (`Amount`, `Ampl.`) read correctly.
