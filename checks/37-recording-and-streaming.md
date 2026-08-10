# Re-verification note: 37-recording-and-streaming

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 37-01 | A capture application alongside a running score | needs interaction + platform software |

See `checks/FIGURES-PENDING.md` for the consolidated list.

## Re-verify when the pinned version changes

- Every platform route: Spout plus the OBS plug-in on Windows, Syphon plus the virtual webcam on macOS, shmdata into GStreamer into v4l2loopback on Linux.
- The Windows audio advice about loopback-capable outputs.
- The direct RTP pipeline through GStreamer.

## Claims that depend on external sources

- Grounded in the reference pages linked under 'Going further' on the lesson page.
