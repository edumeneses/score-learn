# Re-verification note: 26-shaders-and-mixing

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 26-01 | The shader editor with code beside its rendered result | **done**, docs/learn/assets/26/26-01-shader-editor.png |

See `checks/FIGURES-PENDING.md` for the consolidated list of figures that need an
interactive session or media, and why each cannot be produced by the scripted
pipeline.

## Re-verify when the pinned version changes

- The script editor button, the Compile action, Ctrl+Enter, and that invalid code is refused.
- That declared ISF inputs become ports.
- That devices cannot be added during playback.
- The lightness computer and LED view.

## Claims that depend on external sources

- Grounded in the reference pages linked under 'Going further' on the lesson page.

## Grounded by the figure, 2026-08-11

- **Declared ISF inputs become ports**, confirmed on `Visuals > ISF Shader > filter >
  Kaleidoscope`. Its header declares `inputImage` (type `image`), `sides` (float, min 1,
  max 32, default 6), `angle`, `slidex`, `slidey`, and `center`; the inspector lists every
  one of them, and the node carries them as controls.
- **The editor has `Fragment` and `Vertex` tabs**, a log pane under the code, and
  `Clear log`, `Close`, and `Compile` along the bottom, the same shape as the JavaScript
  editor of Lesson 29. It is opened from the process header or from the inspector.
- **The inspector previews the texture.** While the score plays, the process inspector
  shows the current output frame under `Outputs`. This is the figure's rendered result: no
  output window is in the capture at all. The same panel carries the outlet's `Size`
  (1280x720 here), `Format` (`RGBA8`), `Filter` (`Linear`), and `Address mode`
  (`Clamp to edge`).
- **Chaining moves the window output onto the new process**, exactly as chaining an
  expression object moved the destination address in Lesson 30. Selecting the video and
  double-clicking the shader cabled video into `inputImage` and left the shader's output
  addressed to `Window`.

## Correction made by the figure, 2026-08-11

Step 1 said to **cable** the shader to the window device. That is not the mechanism. The
outlet carries an **output address**, offered in the inspector as a list of the declared
windows, and it is what puts an image on screen; `checks/25-video-pipeline.md` had already
recorded this for video and the lesson text had not caught up. Lesson 26 step 1 and
Lesson 25 step 3 are both corrected.

## The output window, and why it is not in the figure

The `Window` device's window is a **GPU surface**: `XGetImage` on its own drawable returns
black while it is on screen, and a root-window capture of the same region returns a flat
grey. It is therefore not capturable by the harness the way every other figure is.

Three further findings, for whoever needs the window itself:

- **It opens off-screen.** The device exposes `screen`, `position`, `cursor`, `size`,
  `key`, and `fullscreen` as ordinary parameters. `position` came up as `[1883, 19]` in
  logical pixels, which at `QT_SCALE_FACTOR=2` is x=3766 on a 3840 px screen, so about 74
  px of a 2560 px window is visible. The document stores `[0, 0]`; the value in the
  explorer is what the window manager actually did.
- **`position` is a readback while stopped.** Typing a new value into the device explorer
  is overwritten immediately unless the score is playing. Setting it during playback holds.
- **Moving or resizing that window from outside stops it opening again.** After an Xlib
  `configure` on it, and after editing `size` in the explorer, later runs created no window
  at all until score was restarted. Do not fight it; use the inspector preview.
