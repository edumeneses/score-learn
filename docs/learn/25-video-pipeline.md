---
layout: default
title: "Lesson 25: The video pipeline"
description: "How score's render graph works, getting a video file and a camera on screen, and why video ports are not control ports."
parent: Lessons
nav_order: 30
unit: "25"
permalink: /learn/25-video-pipeline.html
score_version: "3.8.2"
reading_time: "14 min"
practice_time: "25 min"
score_file: none
---

# Lesson 25: The video pipeline

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 24]({{ site.baseurl }}/learn/24-tempo-and-sync.html).
>
> **You will need** two video files and a GPU that met Lesson 01's requirements. No camera is required: two mockup clips ship with this lesson, `mock-bars.mp4` and `mock-second.avi`, and the box below says how they were made so you can generate your own at any resolution.
>
> **You will build** a document that puts video on screen, fades it, and mixes a second source into it.

## Why this matters

Video in *score* is not a bolted-on player. It is a GPU render graph, built from the processes you place, executed on its own thread, with each process writing into a render target. That architecture is why video and control and audio can share one timeline without the video work being a special case, and it is why the same techniques you have used all course apply to a shader's parameters.

It also means the mental model differs from audio in one respect that causes early confusion. Audio propagates up the hierarchy by default, as Lesson 19 established. Video does not: an image goes where you cable it, and it appears on screen only when something is cabled to an output. Nothing is implicit.

## Concepts

**The render graph.** Video processes form a graph that *score* builds and runs on a separate thread. Each process renders into a target, and the results are combined according to your cables. The abstraction underneath is Qt's rendering hardware interface, which lets the same graph run on OpenGL ES, Vulkan, Metal, or Direct3D 11 depending on the platform.

**Shaders are ISF.** Image processes are written in the Interactive Shader Format, an open specification for shaders with declared parameters. This matters because ISF shaders exist in quantity outside *score*, and because a shader's declared parameters become ports, which makes them automatable like anything else. Lesson 26 writes one.

**An output is a device.** To get an image on screen you need a **window** device, declared in the device explorer like any other. That is the destination you cable your final image into. Other outputs exist for sharing images with other applications: Spout on Windows, Syphon on macOS, NDI over a network, shmdata on Linux.

**A camera is a device too.** Declare a camera device and its image becomes a source in the graph, identical in kind to a video file.

**Video ports are not control ports.** They carry textures, and they connect only to other video ports. This sounds obvious and produces a specific confusion: to make an image react to a number, you connect the number to a *parameter* of an image process, not to its image input.

**Fades are alpha, not gain.** Audio has a gain sub-port on every outlet; video does not have the equivalent. To fade an image you insert a filter that sets its opacity, the user library's alpha-setting shader being the standard one, and automate that filter's parameter.

**Mixing is a process.** The user library provides an eight-channel video mixer, found in the process library under visuals, ISF shader, utility, with an opacity and a blend mode per input. There is also a four-point mapping object for simple projection alignment.

## Walkthrough: an image on screen, then two

![Two video sources in a score, their thumbnails visible, with the Window device declared in the explorer]({{ site.img }}/25/25-01-video-sources.png)

The figure is `lesson-25.score`, which ships with this lesson: the two generated clips, one H.264 and one MJPEG, each addressed to the `Window` device. Note what makes the image appear: not a cable, but an **address** of `Window:/` on each video outlet, which is the same mechanism a state uses to reach a device parameter. The output window itself opened off-screen when this was captured, so what you see here is the document rather than the rendered result.

{: .note }
> **Making your own test clips.** Test material is better generated than downloaded: you control the resolution, the length, and the codec, which are exactly the variables this lesson asks you to measure. Both clips shipped here came from `ffmpeg`, which is on most systems already:
>
> ```bash
> ffmpeg -f lavfi -i "testsrc2=size=1280x720:rate=25:duration=8" >        -c:v libx264 -preset veryfast -crf 28 -pix_fmt yuv420p mock-bars.mp4
> ffmpeg -f lavfi -i "smptehdbars=size=1280x720:rate=25:duration=8" >        -vf "hue=s=0.6,noise=alls=8:allf=t" -c:v mjpeg -q:v 12 mock-second.avi
> ```
>
> The two deliberately differ in codec: one H.264, which is small and comparatively expensive to decode, and one MJPEG, which is large and cheap. Playing both and watching the frame rate is the fastest demonstration of the decoding cost described below.

1. **Declare a window device.** Without it there is nowhere for an image to go. Do this first; it is the step people skip.
2. **Drop a video file** into an interval, exactly as you did with a sound file in Lesson 20.
3. **Cable its output to the window device.** Play. The image appears. Note that unlike audio, nothing happened until you drew that cable.
4. **Switch to the nodal view.** As with audio effects, this is where video work belongs.
5. **Add the alpha filter** from the user library between the video and the window, and cable it in.
6. **Automate the opacity.** Right-click the filter's opacity port, create an automation, and draw a fade in and out. Play: you now have a video fade, built from the general mechanism rather than a special feature.
7. **Add a second source**, either another file or a camera device.
8. **Add the video mixer** and cable both sources into it, then the mixer into the window. Set an opacity and a blend mode per input and watch the combination change.
9. **Automate a blend.** Automate one input's opacity so the two sources cross over during the piece.
10. **Check the frame rate honestly.** Watch for stutter, and note what your machine does with two sources plus a mixer. This number is a real constraint on what you can plan.
11. **Try a share output.** If you have another application that accepts NDI, Spout, or Syphon, send your image there instead of to a window, and confirm it arrives.

## Performance, and what actually costs

Video is the first part of this course where the machine's limits are a design constraint rather than a footnote. Four things dominate, roughly in order.

**Resolution.** Cost scales with pixels. A pipeline that stutters at 4K may be comfortable at 1080p, and for a projection surface that is smaller than 4K anyway, the extra pixels bought nothing.

**The number of render targets.** Every process in the chain writes into a target, so a chain of eight filters costs eight passes. Combining operations into one shader, when you can, is the single most effective optimisation available.

**Decoding.** Video file playback costs processor time separately from rendering, and codec choice matters enormously. A format designed for editing plays back cheaply and takes disk space; a format designed for delivery is small and expensive to decode. For installation work, favour the cheap-to-decode option and accept the file size.

**Readbacks.** Anything that takes a texture off the GPU to look at it, converting pixels into values for lights per Lesson 14's mention, is comparatively expensive. It is often worth it; it is never free.

The practical habit: measure with your real content at your real resolution early, rather than authoring at a comfortable size and discovering the limit during installation.

## Where the image goes

Four destinations, and the choice affects how the piece is installed.

**A window** on a display or projector: the simplest, and it is what you use while authoring. In a venue this becomes a full-screen output on a specific display, which is a venue-dependent value worth isolating, as Milestone P6 insists.

**A share protocol to another application on the same machine**, Spout on Windows or Syphon on macOS. Right when another tool does the projection mapping or the media server work.

**NDI over a network**, which sends video to another machine. Convenient, and it costs bandwidth and adds latency; test both with the real content rather than assuming.

**Off the GPU into data**, per Lesson 26's pixel utilities, when the destination is LEDs rather than a screen.

A piece often uses two at once, a monitoring window plus the real output, and it is worth building that from the start rather than reconfiguring at the venue.

## Common mistakes

- **No window device.** The graph runs, and nothing is on screen. This is the most common first failure.
- **Expecting video to propagate like audio.** Nothing appears until it is cabled to an output.
- **Cabling a number into an image input.** Numbers go to parameters.
- **Looking for a gain on a video outlet.** Fade with an alpha filter instead.
- **Authoring at 4K on a laptop** and planning a piece the venue machine cannot run either.
- **A chain of many small filters** where one shader would do, then wondering why the frame rate fell.
- **A delivery codec for playback.** It decodes slowly, and the symptom looks like a *score* problem.

## Exercise

Build a document with two video sources mixed through the video mixer into a window device, with one source's opacity automated across thirty seconds and the blend mode changed at least once. Then measure: run it at your intended resolution and note the frame rate, then at half that resolution and note it again.

**Success criterion:** both sources reach the screen, the crossover is smooth, and you can state the resolution at which your machine stops being comfortable. If nothing appeared, check the window device before anything else.

## Going further

- [The graphics pipeline]({{ site.docs_baseurl }}/in-depth/graphics-pipeline.html), which is short and explains the architecture.
- [Working with video]({{ site.docs_baseurl }}/quick-start/working-with-video.html) and [video techniques]({{ site.docs_baseurl }}/common-practices/5-video.html).
- [Video mixing]({{ site.docs_baseurl }}/common-practices/11-video-mixing.html) for the mixer and the mapping object.
- [The window device]({{ site.docs_baseurl }}/devices/window-device.html) and [camera device]({{ site.docs_baseurl }}/devices/camera-device.html).
