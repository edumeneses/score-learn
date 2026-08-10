---
layout: default
title: "Lesson 37: Recording and streaming the output"
description: "Get audio and video out of score into a recording or a livestream, per platform, and know what each route costs."
parent: Lessons
nav_order: 43
unit: "37"
permalink: /learn/37-recording-and-streaming.html
score_version: "3.8.2"
reading_time: "12 min"
practice_time: "20 min"
score_file: none
---

# Lesson 37: Recording and streaming the output

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 36]({{ site.baseurl }}/learn/36-distributed-scores.html).
>
> **You will need** a document that produces video and audio, and streaming software such as OBS Studio.
>
> **You will build** a capture of your own work: a local recording and a livestream, using the route that suits your platform.

## Why this matters

Documentation is how this work survives. A piece runs for three nights and then exists only as a recording, which is what a funder, a curator, a programmer, and your future self will actually see. A bad capture of good work is a real loss, and it is avoidable.

Streaming has become part of the practice for the same reason, and the mechanism is the same: *score* is not a recorder, it is a producer of audio and video that other tools can capture. The lesson is therefore mostly about the boundary, and the boundary is platform-specific in a way little else in this course has been.

## Concepts

**Video leaves through a share protocol.** Rather than pointing a screen recorder at a window, send the video output directly to the capture application: **Spout** on Windows, **Syphon** on macOS, **shmdata** on Linux. This is a clean handoff at full resolution and frame rate, and it is what the reference documentation recommends for each platform.

**On Windows.** Add a Spout output in *score* and set it as the output of your video chain, then add a Spout input source in OBS through the community plug-in. For audio, use the loopback-capable output path rather than a driver without loopback, and capture it as an audio output source.

**On macOS.** Add a Syphon output and consume it in OBS; a Syphon virtual webcam makes the stream visible to applications that do not speak Syphon directly.

**On Linux.** The recommended route is shmdata into GStreamer and out to a virtual camera device, which then behaves like a webcam for OBS, browsers, or anything else. Audio is simpler: with JACK or PipeWire, OBS takes *score*'s output directly as a client input.

**Straight to a network stream.** On Linux the same shmdata output can be piped through GStreamer into a network stream, which skips the capture application entirely. This is the lightest route for an unattended stream and the least convenient for one where you want to add titles and switch sources.

**Recording control values is a different job.** The CSV recorder from Lesson 12 logs numbers, which is what you want for analysis, for a paper, or for handing data to a collaborator. It is not documentation of the piece; it is data about it.

**Capture costs performance.** Encoding video is real work on the same machine that is rendering it. A piece that runs comfortably will not necessarily run comfortably while being captured, and the honest solution is often a second machine.

## Walkthrough: a local recording, then a stream

{: .note }
> A figure for this lesson is pending: it needs a capture application alongside a running score, which requires interaction and platform-specific software. See `checks/37-recording-and-streaming.md`.

1. **Get the piece running as it should be seen.** Capture is the last step, and capturing a piece you are still editing wastes the take.
2. **Add the share output** for your platform and set it as the output of your video chain, alongside your monitoring window rather than instead of it.
3. **Consume it in OBS** and confirm you see the image at full size, without scaling artefacts.
4. **Route the audio** by your platform's method and confirm the levels arrive. Check for the double-capture mistake: audio arriving twice, once through the intended path and once through a desktop capture, which sounds subtly wrong rather than obviously wrong.
5. **Record two minutes** and watch it back. Look for dropped frames, listen for glitches, and check the synchronisation between what you hear and what you see.
6. **Measure the cost.** Compare the frame rate with and without capture running. If it fell, decide between lowering the capture resolution, lowering the piece's, or using a second machine.
7. **Do a proper take.** Full length, no editing during, no adjusting mid-run. Documentation is a performance.
8. **Now stream it.** Configure a destination in OBS and go live to a private or unlisted target as a test. Confirm the stream is watchable rather than assuming.
9. **Try the direct route** if you are on Linux and the stream is unattended: shmdata into GStreamer into a network stream, with no capture application at all. Compare the processor cost.
10. **Record the settings that worked**: resolutions, codecs, audio routing, and the frame rate you achieved. This belongs with the rider from Lesson 34, because the next capture will be under time pressure.

## Making a capture that represents the work

Four things that matter more than the encoder settings, and that people learn after their first disappointing document.

**Capture what the audience saw, not what the projector received.** A fisheye dome image recorded as a fisheye circle is unwatchable as documentation, and a flat crop of it is not what happened. For immersive work, a camera in the room, or an audience-perspective render, communicates far more than the raw output.

**Record the room's sound as well as the machine's.** A spatial piece captured from the master output loses precisely the thing it was about. A stereo pair in the room, mixed with the direct output, is a compromise that documents better than either alone.

**Do not edit the timing.** A recording that cuts the waiting is a recording of a different piece, and for interactive work the waiting is the content.

**Keep one unedited take.** Whatever you cut for a portfolio, keep the whole thing somewhere. It is the only record of what the piece actually did, and in two years it is the version you will want.

## Two machines, when you can

The single most useful piece of advice about capture, and the one most often ignored because of cost.

Rendering a piece and encoding a stream are both demanding, and they compete for the same processor and the same graphics unit. On one machine, capture degrades the thing it is capturing, which is exactly backwards: the recording is worse *and* the performance is worse.

Sending the video to a second machine over NDI, per Lesson 25, and encoding there costs bandwidth and buys back the whole performance budget. For a piece that will be documented once and performed many times, this is worth arranging even if the second machine is borrowed.

When one machine is all there is, the honest order of sacrifice is: reduce the capture resolution first, since a 1080p document of a 4K piece is perfectly usable; then reduce the capture frame rate; and only then reduce the piece itself. Never let the audience see a degraded performance so that a recording can be sharper, and write down which compromise you made so the next capture starts from a known position.

## Common mistakes

- **Screen-recording a window** instead of using the share protocol, and getting scaling and frame-rate loss for free.
- **Audio captured twice** through two paths, which is hard to hear and obvious to a listener later.
- **Capturing on the machine that is already at its limit.** Measure, and use a second machine if needed.
- **A driver without loopback on Windows**, so no audio arrives at all.
- **Streaming without a test.** Discovering the stream was broken after the performance is a complete loss.
- **Documenting a spatial or immersive piece from the master output**, which records the mechanism rather than the experience.
- **Not writing down the settings.** The next capture is always in a hurry.

## Exercise

Capture one of your milestone pieces twice: once locally at the highest quality your machine sustains, and once as a live stream to a private destination. Measure the frame rate in all three conditions, playing alone, recording, and streaming. Then write the four-line capture note: share protocol, audio route, resolution, and achieved frame rate.

**Success criterion:** the local recording plays back with no dropped frames and correct synchronisation, the stream was watched by you on another device before you called it working, and your note is specific enough to repeat the setup without rediscovering it.

## Going further

- [Livestreaming]({{ site.docs_baseurl }}/common-practices/10-livestreaming.html), the reference for every platform route above, with the exact pipelines.
- [Spout]({{ site.docs_baseurl }}/devices/spout-device.html), [Syphon]({{ site.docs_baseurl }}/devices/syphon-device.html), and [shmdata]({{ site.docs_baseurl }}/devices/shmdata-device.html) device references.
- [The CSV recorder]({{ site.docs_baseurl }}/processes/csv-recorder.html) for logging values rather than media.
- [NDI]({{ site.docs_baseurl }}/devices/ndi-device.html), for sending video to another machine to capture there.
