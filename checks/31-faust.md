# Re-verification note: 31-faust

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 31-01 | The Faust editor with code and a running audio chain | **done**, docs/learn/assets/31/31-01-faust-editor.png |

See `checks/FIGURES-PENDING.md` for the consolidated list.

## Re-verify when the pinned version changes

- That controls declared in Faust become ports.
- The mono-process polyphony rule and list-valued controls.
- sp.spat and its editable speaker count; abclib in the package manager.

## Claims that depend on external sources

- Grounded in the reference pages linked under 'Going further' on the lesson page.

## Grounded by the figure, 2026-08-12

- **Declared controls become ports**, confirmed by replacement rather than by assertion.
  The process started as the `16_channel_volume` preset with sixteen `Volume-NN` ports;
  compiling six lines that declare `gain` and `cutoff` left exactly those two, plus
  `Audio In`, `Audio Out`, and `Propagate`. The node in the score shows them too.
- **The library has no empty Faust process.** `Plugins > Faust` lists presets only:
  `16_channel_volume` and the `abc_*` family from abclib. `Script` holds `Avendish`, `JIT`,
  `Javascript`, `Process launcher`, and `Shell command`, and no Faust. So step 1 of the
  walkthrough is "add a preset and replace its code", which the lesson now says.
- **The process keeps the preset's label after recompiling.** The inspector still reads
  `Process (Faust: 16_channel_volume)` while the ports are the new ones. The object tree
  meanwhile shows the process as `Faust`.
- **The editor is a separate top-level window** named `score`, 1600x1600 as it opens, with
  the same shape as the JavaScript editor: a log pane and `Clear log`, `Close`, `Compile`.
  It is toggled by the button in the inspector, so a second click closes it again.
- The code compiled and ran on the `Dummy (No audio)` driver, so no audio device is needed
  to capture this figure.

## The code in the figure

```faust
import("stdfaust.lib");

gain = hslider("gain", 0.5, 0, 1, 0.01);
cutoff = hslider("cutoff", 2000, 100, 8000, 1);

process = fi.lowpass(3, cutoff) : *(gain);
```

Deliberately the lesson's own shape: a filter from the standard library, a gain, and two
declared controls, which is steps 3 and 5 in one processor.

## How 31-01 was captured, 2026-08-12

On `lesson-20.score`. Select the sound process, filter the library to `16_channel`,
double-click the preset, open the editor from the inspector, replace the code with
`scripts/typeinto.py`, press `Compile`, move the editor window clear of the node, and play.

**Typing the code needed a new tool**, `scripts/typeinto.py`, for two reasons that are now
in `CLAUDE.md` and that cost most of the time on this figure:

1. `capture.py key` and `capture.py type` call `require_focus`, which activates the main
   window first. That is correct for shortcuts and wrong for a focused sub-widget: the
   activation resets focus, so the keystrokes went to the score. `ctrl+a` then `delete`,
   meant to clear the editor, is Select All and Delete in the main window.
2. The keyboard is a **multilingual layout with dead keys**. Keycode 48 carries
   `dead_acute`, `dead_diaeresis`, `apostrophe`, and `quotedbl` at levels 0 to 3, so a
   double quote needs AltGr and shift together. `capture.py type` assumes a US layout and
   guesses shift from a fixed character list, which here produced `import(stdfaust.lib);`
   with the quotes missing, and then a page of diaereses. A missing quote is a compile
   error, not a visible typo, so it is worth checking the code in the capture before
   pressing compile.
