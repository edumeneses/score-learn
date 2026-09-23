---
layout: default
title: "Lesson 37: Recording and streaming: Spout, Syphon, shmdata, and OBS"
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

# Lesson 37: Recording and streaming: Spout, Syphon, shmdata, and OBS

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 36]({{ site.baseurl }}/learn/36-distributed-scores.html), since this lesson assumes a piece that already runs as you intend.
>
> **You will need** a document that produces video and audio, together with streaming software such as OBS Studio.
>
> **You will build** a capture of your own work, consisting of a local recording and a livestream, using the route that suits your platform.

## Why this matters

Documentation is how this work survives, because a piece runs for three nights and then exists only as a recording, which is what a funder, a curator, a programmer, and your future self will see. A poor capture of good work is therefore a real loss, and it is an avoidable one.

Streaming has become part of the practice for the same reason, and the mechanism is the same in both cases, since *score* is not a recorder but a producer of audio and video that other tools can capture. In other words, the lesson is mostly about the boundary between *score* and those tools, and that boundary is platform-specific in a way that little else in this course has been.

## Concepts

### Share protocols

Video leaves *score* through a share protocol. Instead of pointing a screen recorder at a window, you send the video output directly to the capture application, through **Spout** on Windows, **Syphon** on macOS, or **shmdata** on Linux. This is a clean handoff at full resolution and frame rate, and it is the route the reference documentation recommends for each platform.

### Direct network streams

The same output can go straight to a network stream. On Linux the shmdata output can be piped through GStreamer into a network stream, which skips the capture application entirely. This is the lightest route for an unattended stream and the least convenient for one where you want to add titles and switch sources.

### Recording values versus recording the piece

Recording control values is a different job from recording the piece. The CSV recorder from Lesson 12 logs numbers, which is what you want for analysis, for a paper, or for handing data to a collaborator. However, it produces data about the piece, whereas documentation records the piece itself.

## Walkthrough: a local recording, then a stream

{: .note }
> A figure for this lesson is pending: it needs a capture application alongside a running score, which requires interaction and platform-specific software. See `checks/37-recording-and-streaming.md`.

1. **Get the piece running as it should be seen**, because capture is the last step, and capturing a piece you are still editing wastes the take.
2. **Add the share output for your platform** and set it as the output of your video chain, alongside your monitoring window so that you keep a local view of the piece.

   {: .note }
   > **On Windows, Spout carries the video.** Add a Spout output in *score*, set it as the output of your video chain, and then add a Spout input source in OBS through the community plug-in.
   >
   > **On macOS, Syphon plays the same role.** Add a Syphon output and consume it in OBS; a Syphon virtual webcam makes the stream visible to applications that do not speak Syphon directly.
   >
   > **On Linux, shmdata feeds a virtual camera.** The recommended route sends shmdata into GStreamer and out to a virtual camera device. Consequently, that device behaves like a webcam for OBS, browsers, or any other application.

3. **Consume it in OBS** and confirm that you see the image at full size, without scaling artefacts.
4. **Route the audio by your platform's method** and confirm that the levels arrive. Check for the double-capture mistake, in which audio arrives twice, once through the intended path and once through a desktop capture, and sounds subtly wrong instead of obviously wrong.

   {: .warning }
   > **On Windows, the audio needs an output path that supports loopback**, since a driver without loopback delivers no audio at all, whereas with loopback OBS captures the output as an audio output source. In contrast, audio on Linux is simpler, because with JACK or PipeWire, OBS takes *score*'s output directly as a client input.

5. **Record two minutes and watch it back**, looking for dropped frames, listening for glitches, and checking the synchronisation between what you hear and what you see.
6. **Measure the cost** by comparing the frame rate with and without capture running. If it fell, decide between lowering the capture resolution, lowering the piece's resolution, or moving the capture to a second machine.

   {: .warning }
   > **Capture costs performance**, because encoding video is real work on the same machine that is rendering it. A piece that runs comfortably will not necessarily run comfortably while being captured, and the dependable solution is often a second machine, as a later section argues.

7. **Do a full take** with no editing and no adjustment during the run, because a capture is performed in the same sense that the piece is, and an interrupted take documents a different piece.
8. **Stream it** by configuring a destination in OBS and going live to a private or unlisted target as a test, and confirm that the stream is watchable instead of assuming it.
9. **Try the direct route** if you are on Linux and the stream is unattended, sending shmdata into GStreamer and on to a network stream with no capture application at all, and compare the processor cost with the OBS route.
10. **Record the settings that worked**, including resolutions, codecs, audio routing, and the frame rate you achieved. This record belongs with the rider from Lesson 34, because the next capture will be made under time pressure.

## Making a capture that represents the work

The properties below matter more than the encoder settings, and most people learn them only after a first disappointing document.

**Capture what the audience saw rather than what the projector received.** A fisheye dome image recorded as a fisheye circle is unwatchable as documentation, while a flat crop of it misrepresents what happened. For immersive work, a camera in the room, or an audience-perspective render, communicates far more than the raw output.

**Record the room's sound as well as the machine's**, because a spatial piece captured from the master output loses the very thing it was about. A stereo pair in the room, mixed with the direct output, is a compromise that documents the piece better than either source alone.

**Do not edit the timing**, since a recording that cuts the waiting is a recording of a different piece, and for interactive work the waiting is the content.

**Keep one unedited take.** Whatever you cut for a portfolio, keep the whole take somewhere, because it is the only record of what the piece did, and in two years it is the version you will want.

## Two machines, when you can

Capturing on a second machine is the single most useful piece of advice about capture, and it is the one most often ignored because of its cost.

Rendering a piece and encoding a stream are both demanding, and they compete for the same processor and the same graphics unit. However, on one machine capture degrades the thing it is capturing, so that the recording is worse *and* the performance is worse.

Sending the video to a second machine over NDI (Network Device Interface), as in Lesson 25, and encoding there costs bandwidth and buys back the whole performance budget. For a piece that will be documented once and performed many times, this arrangement is worth the trouble even if the second machine is borrowed.

Nevertheless, one machine is often all there is, and then the order of sacrifice runs as follows: reduce the capture resolution first, since a 1080p document of a 4K piece is perfectly usable; then reduce the capture frame rate; and only then reduce the piece itself. The audience should not see a degraded performance so that a recording can be sharper, and you should write down which compromise you made so that the next capture starts from a known position.

## Common mistakes

- **Screen-recording a window** instead of using the share protocol, which brings scaling and frame-rate loss with it.
- **Capturing audio twice** through two paths, which is hard to hear in the moment and obvious to a listener later.
- **Capturing on a machine that is already at its limit**, when the frame rate should be measured first and a second machine used if it falls.
- **Using a driver without loopback on Windows**, so that no audio arrives at all.
- **Streaming without a test**, because discovering that the stream was broken after the performance is a complete loss.
- **Documenting a spatial or immersive piece from the master output**, which records the mechanism instead of the experience.
- **Not writing down the settings**, although the next capture is always in a hurry.

## Exercise

Capture one of your milestone pieces twice, once locally at the highest quality your machine sustains and once as a live stream to a private destination. Measure the frame rate in all three conditions, playing alone, recording, and streaming, and then write the four-line capture note: share protocol, audio route, resolution, and achieved frame rate.

**Success criterion:** the local recording plays back with no dropped frames and correct synchronisation, you watched the stream on another device before you called it working, and your note is specific enough to repeat the setup without rediscovering it.

## Going further

- [Livestreaming]({{ site.docs_baseurl }}/common-practices/10-livestreaming.html) is the reference for every platform route above, with the exact pipelines.
- [Spout]({{ site.docs_baseurl }}/devices/spout-device.html), [Syphon]({{ site.docs_baseurl }}/devices/syphon-device.html), and [shmdata]({{ site.docs_baseurl }}/devices/shmdata-device.html) have their own device reference pages.
- [The CSV recorder]({{ site.docs_baseurl }}/processes/csv-recorder.html) covers logging values, whereas this lesson covered capturing media.
- [NDI]({{ site.docs_baseurl }}/devices/ndi-device.html) describes sending video to another machine so that it can be captured there.

{% include lesson_files.html %}
