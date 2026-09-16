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
> **You will need** two video files and a GPU (graphics processing unit) that met Lesson 01's requirements. No camera is required, because two mockup clips ship with this lesson, `mock-bars.mp4` and `mock-second.avi`, and the box below says how they were made so that you can generate your own at any resolution.
>
> **You will build** a document that puts video on screen, fades it, and mixes a second source into it.

## Why this matters

Video in *score* is a GPU render graph built from the processes you place, executed on its own thread, with each process writing into a render target; it is not a player bolted onto the side of an audio sequencer. That architecture is why video, control, and audio can share one timeline without the video work being a special case, and it is why the techniques you have used all course apply unchanged to a shader's parameters.

However, the mental model differs from audio in one respect that causes early confusion. Audio propagates up the hierarchy by default, as Lesson 19 established, whereas video does not: an image goes where you cable it, and it appears on screen only when something is cabled to an output, so every connection in the video graph has to be made explicitly.

## Concepts

**The render graph runs on its own thread and combines processes according to your cables.** Video processes form a graph that *score* builds and executes separately from the rest of the engine, with each process rendering into a target whose results are combined as the cables dictate. Furthermore, the abstraction underneath is Qt's rendering hardware interface, which lets the same graph run on OpenGL ES, Vulkan, Metal, or Direct3D 11 depending on the platform.

**Shaders are written in ISF (Interactive Shader Format).** Image processes use this open specification for shaders with declared parameters, which matters for two reasons: ISF shaders exist in quantity outside *score*, and a shader's declared parameters become ports, so they are automatable like any other parameter in the course, as Lesson 26 shows by writing one.

**An output is a device, declared like any other.** To get an image on screen you need a **window** device, declared in the device explorer, which is the destination you cable your final image into; other outputs exist for sharing images with other applications, namely Spout on Windows, Syphon on macOS, NDI (Network Device Interface) over a network, and shmdata on Linux.

**A camera is a device as well.** Declaring a camera device makes its image a source in the graph, identical in kind to a video file.

**Video ports carry textures and connect only to other video ports.** This sounds obvious and produces a specific confusion when a reader wants an image to react to a number. In contrast to the image input, which accepts only another image, the number belongs on a *parameter* of the image process.

**Fades are made with alpha, since video outlets have no gain.** Audio has a gain sub-port on every outlet, whereas video has no equivalent, so to fade an image you insert a filter that sets its opacity, the user library's alpha-setting shader being the standard one, and automate that filter's parameter.

**Mixing is itself a process.** The user library provides an eight-channel video mixer, found in the process library under visuals, ISF shader, utility, with an opacity and a blend mode per input; a four-point mapping object is available alongside it for simple projection alignment.

## Walkthrough: an image on screen, then two

![Two video sources in a score, their thumbnails visible, with the Window device declared in the explorer]({{ site.img }}/25/25-01-video-sources.png)

The figure is `lesson-25.score`, which ships with this lesson and holds the two generated clips, one H.264 and one MJPEG, each addressed to the `Window` device. What makes the image appear is an **address** of `Window:/` on each video outlet, which is the same mechanism a state uses to reach a device parameter, so no cable is involved. The output window itself opened off-screen when this was captured, so the figure shows the document and not the rendered result.

{: .note }
> **Making your own test clips is better than downloading them**, because you control the resolution, the length, and the codec, which are the three variables this lesson asks you to measure. Both clips shipped here came from `ffmpeg`, which most systems already have installed:
>
> ```bash
> ffmpeg -f lavfi -i "testsrc2=size=1280x720:rate=25:duration=8" \
>     -c:v libx264 -preset veryfast -crf 28 -pix_fmt yuv420p mock-bars.mp4
> ffmpeg -f lavfi -i "smptehdbars=size=1280x720:rate=25:duration=8" \
>     -vf "hue=s=0.6,noise=alls=8:allf=t" -c:v mjpeg -q:v 12 mock-second.avi
> ```
>
> The two differ in codec on purpose: one is H.264, which is small and comparatively expensive to decode, while the other is MJPEG, which is large and cheap. Playing both and watching the frame rate is the fastest demonstration of the decoding cost described below.

1. **Declare a window device** before you add a source, because without it there is nowhere for an image to go, and this is the step people skip.
2. **Drop a video file** into an interval, in the same way that you dropped a sound file in Lesson 20; the process appears, although no image reaches the screen yet.
3. **Send its output to the window device** by selecting the video process and setting the address on its outlet, which the inspector offers as a list of the declared windows, then play. The image appears; however, unlike audio, no output occurred until you named a destination.
4. **Switch to the nodal view**, because, as with audio effects, this is where video work belongs.
5. **Add the alpha filter** from the user library between the video and the window, and cable it in.
6. **Automate the opacity** by right-clicking the filter's opacity port, creating an automation, and drawing a fade in and out; when you play, you have a video fade built from the general mechanism.
7. **Add a second source**, either another file or a camera device.
8. **Add the video mixer**, cable both sources into it and the mixer into the window, then set an opacity and a blend mode per input and watch the combination change.
9. **Automate a blend** by automating one input's opacity so that the two sources cross over during the piece.
10. **Check the frame rate** while both sources and the mixer run, watching for stutter and noting what your machine does under that load, since this number is a real constraint on what you can plan.
11. **Try a share output** if you have another application that accepts NDI, Spout, or Syphon: send your image there in place of the window, and confirm that it arrives.

## Performance, and what actually costs

Video is the first part of this course where the machine's limits become a design constraint instead of a footnote, and the cost is dominated by resolution, the number of render targets, decoding, and readbacks, roughly in that order.

**Resolution sets the baseline, because cost scales with pixels.** A pipeline that stutters at 4K may be comfortable at 1080p, and for a projection surface that is smaller than 4K anyway, the extra pixels bought no visible improvement.

**The number of render targets multiplies that baseline.** Every process in the chain writes into a target, so a chain of eight filters costs eight passes. In other words, combining operations into one shader, when you can, is the single most effective optimisation available.

**Decoding costs processor time separately from rendering, and codec choice matters enormously.** A format designed for editing plays back cheaply and takes disk space, whereas a format designed for delivery is small and expensive to decode; for installation work, favour the cheap-to-decode option and accept the file size.

**Readbacks take a texture off the GPU so that it can be inspected**, for example when pixels are converted into values for lights, as Lesson 14 mentioned, and they are comparatively expensive. Nevertheless, the conversion is often justified by what it enables, although its cost has to be budgeted like any other pass.

The practical conclusion is to measure with your real content at your real resolution early, because authoring at a comfortable size and discovering the limit during installation leaves no time to change the design.

## Where the image goes

The image can reach four destinations, and the choice affects how the piece is installed.

**A window on a display or projector is the simplest destination**, and it is what you use while authoring. In a venue this becomes a full-screen output on a specific display, which is a venue-dependent value that should be isolated, as Milestone P6 insists.

**A share protocol reaches another application on the same machine**, Spout on Windows or Syphon on macOS, which is the right choice when another tool does the projection mapping or the media server work.

**NDI over a network sends video to another machine**, which is convenient. However, it costs bandwidth and adds latency, so test both with the real content before relying on them.

**Off the GPU into data is the route to LEDs**, per Lesson 26's pixel utilities, when the destination is a strip of lights and not a screen.

A piece often uses two destinations at once, a monitoring window plus the real output, and building that pairing from the start saves reconfiguring at the venue.

## Common mistakes

- **Declaring no window device**, so that the graph runs and no image reaches the screen; this is the most common first failure.
- **Expecting video to propagate like audio**, whereas no image appears until it is cabled to an output.
- **Cabling a number into an image input**, since numbers belong on parameters.
- **Looking for a gain on a video outlet**, when the fade has to be made with an alpha filter.
- **Authoring at 4K on a laptop**, and thereby planning a piece that the venue machine cannot run either.
- **Building a chain of many small filters** where one shader would do, and then wondering why the frame rate fell.
- **Using a delivery codec for playback**, which decodes slowly and produces a symptom that looks like a *score* problem.

## Exercise

Build a document with two video sources mixed through the video mixer into a window device, with one source's opacity automated across thirty seconds and the blend mode changed at least once. Then measure the result by running it at your intended resolution and noting the frame rate, and again at half that resolution.

**Success criterion:** both sources reach the screen, the crossover is smooth, and you can state the resolution at which your machine stops being comfortable. If no image appeared, check the window device before you check the rest of the graph.

## Going further

- [The graphics pipeline]({{ site.docs_baseurl }}/in-depth/graphics-pipeline.html), which is short and explains the architecture.
- [Working with video]({{ site.docs_baseurl }}/quick-start/working-with-video.html) and [video techniques]({{ site.docs_baseurl }}/common-practices/5-video.html).
- [Video mixing]({{ site.docs_baseurl }}/common-practices/11-video-mixing.html) for the mixer and the mapping object.
- [The window device]({{ site.docs_baseurl }}/devices/window-device.html) and [camera device]({{ site.docs_baseurl }}/devices/camera-device.html).
