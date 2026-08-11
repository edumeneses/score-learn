# Re-verification note: 25-video-pipeline

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 25-01 | Two video sources addressed to the Window device | **done**, docs/learn/assets/25/25-01-video-sources.png |

See `checks/FIGURES-PENDING.md` for the consolidated list of figures that need an
interactive session or media, and why each cannot be produced by the scripted
pipeline.

## Re-verify when the pinned version changes

- That a window device is required for anything to appear.
- The Qt RHI backends listed, and the ISF shader format.
- The video mixer's library location: Visuals > ISF Shader > Utility > Video Mixer.
- The alpha-setting filter used for fades.

## Claims that depend on external sources

- Grounded in the reference pages linked under 'Going further' on the lesson page.

## Media shipped with this lesson, 2026-08-11

No camera is available on the authoring machine and none is needed. Two mockup clips are
generated with `ffmpeg` and committed under `library/learn/25-video-pipeline/`:

- `mock-bars.mp4`, H.264, 1280x720, 8 s, small file and comparatively expensive to decode;
- `mock-second.avi`, MJPEG, same size and length, larger file and cheap to decode.

The generating commands are in the lesson itself, so the clips can be regenerated at any
resolution. Using two different codecs is deliberate: it makes the decoding-cost section
demonstrable rather than assertable.

## How lesson-25.score was built, 2026-08-11

`scripts/mkscore.py 25`. Two shapes were read out of score's own
`examples/video/video.score` rather than guessed:

- **VideoProcess**, uuid `32dc5341-7748-4c31-a226-82e6bd685744`, whose `FilePath` takes the
  `<PROJECT>:` prefix, so the clips resolve from the project folder.
- **The Window device**, protocol `5a181207-7d40-4ad8-814e-879fcdf8cc31`, copied with its
  address tree.

The important finding: an image reaches the window by giving the video outlet an
**`Address` of `Window:/`**, not by drawing a cable. That is why this document needed no
cable definitions, which are path-based and awkward to generate.

Not shown in the figure: the rendered output. The window opened at x=3765, off the right
edge of the screen, so the capture contains the document only. To show the output too,
move that window on-screen before capturing.
