# Re-verification note: 25-video-pipeline

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 25-01 | Two video sources through the mixer into a window device | needs interaction + video media |

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
