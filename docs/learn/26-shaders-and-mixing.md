---
layout: default
title: "Lesson 26: Shaders and mixing"
description: "Use, edit, and write ISF shaders whose parameters become ports, and combine images with blend modes and pixel utilities."
parent: Lessons
nav_order: 31
unit: "26"
permalink: /learn/26-shaders-and-mixing.html
score_version: "3.8.2"
reading_time: "14 min"
practice_time: "30 min"
score_file: none
---

# Lesson 26: Shaders and mixing

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 25]({{ site.baseurl }}/learn/25-video-pipeline.html), and have a window device declared.
>
> **You will need** nothing beyond *score*; shaders generate their own images.
>
> **You will build** a generated image from a shader you edited, combined with a second source, with parameters automated from the timeline.

## Why this matters

A shader is the most direct route from an idea to an image in this software, and the Interactive Shader Format makes it unusually approachable: a shader declares its parameters in a small block of metadata, and *score* turns those declarations into ports. The consequence is the thing to hold on to: **a shader's parameters are automatable, mappable, and drivable from a sensor, exactly like a device parameter**. You are not scripting graphics off to one side; you are adding processes whose knobs behave like every other knob in the course.

This is also the first lesson where you write code, and deliberately the gentlest one. Editing three lines of an existing shader and recompiling teaches the loop that Module J then applies to audio, MIDI, and logic.

## Concepts

**ISF in one paragraph.** An ISF shader is a fragment shader plus a JSON header declaring its inputs: their names, types, ranges, and defaults. *score* reads that header and creates ports. Because the format is an open specification with a large public library of shaders, a great deal of material works without modification.

**The editor and the compile loop.** Code-based processes carry a window button on their header that opens a script editor. Edit, then press compile, or use `Ctrl+Enter`, and the running engine takes the new code. Invalid code is refused rather than applied, deliberately, so a typo cannot produce a flash or a burst of noise mid-performance. Errors appear in a pane at the bottom of the editor.

**Generators against filters.** A shader with no image input generates: noise, gradients, patterns, geometry. A shader with an image input filters what arrives. The distinction is only in whether the header declares an image input, and it determines where in the graph the process belongs.

**Blend modes do the compositing.** The eight-channel video mixer from Lesson 25 gives each input an opacity and a blend mode. Blend modes are where most of the visual character of a mix comes from, and they are worth trying exhaustively once rather than reading about.

**Pixel utilities cross the boundary.** A family of processes converts between images and data: most usefully, a lightness computer turns a texture into a series of pixel values, which is how a shader ends up driving an LED strip. That conversion takes the image off the GPU, which Lesson 25 flagged as the expensive operation, and it is often worth it anyway.

**Live coding is supported and normal.** Shaders can be edited while the score plays, along with almost everything else in a document. One documented exception applies to the whole application: **devices cannot be added during playback**, so every window, camera, and output you will need must exist before you press play.

## Walkthrough: edit a shader, then mix it

![The ISF shader editor open on a kaleidoscope filter, the inputs its header declares listed as ports in the inspector, and the rendered result playing in the inspector's preview]({{ site.img }}/26/26-01-shader-editor.png)

The figure is Lesson 25's document with one shader added after the H.264 source. Read across it and the lesson's argument is complete. The editor in the middle shows the ISF header, a JSON block at the top of the fragment source declaring `inputImage`, `sides`, `angle`, `slidex`, `slidey`, and `center`, each with its type, its range, and its default. The inspector on the right lists exactly those names, as ports. The panel below them is the rendered result.

{: .note }
> **The inspector previews the texture.** A process with a texture output shows its current frame in the inspector while the score plays, which is the quickest way to see what a shader is doing; the figure's result is that preview, not the output window. The output window is still where the work goes, but it is not where you have to look while you edit. The same panel carries the outlet's `Size`, `Format`, `Filter`, and `Address mode`. Note also that the editor has two tabs, `Fragment` and `Vertex`, and that a shader is compiled with the `Compile` button at its foot.

1. **Add a shader process** from the library, under `Visuals > ISF Shader`, and set its output to your window device. An image appears. The fastest route is the one from Lesson 21: select the process the shader should follow, then double-click the library entry, and *score* connects it and moves the window output onto the new process for you.
2. **Find its ports.** The parameters declared in its header are on the process, and the inspector lists them. Move one and watch the image change.
3. **Automate a parameter.** Right-click a port, create an automation, draw a curve, play. The shader is now part of your timeline rather than a static effect.
4. **Open the editor** with the window button on the process header and read the header block. Identify one declared input and find where the code uses it.
5. **Change one number** in the code, something obviously visual such as a scale or a colour, then compile. The image updates while the score is running.
6. **Break it on purpose.** Introduce a syntax error and compile. Note that the running image is unchanged and the error appears in the pane below. That refusal is a feature.
7. **Add a declared input.** Add an entry to the header block, use it in the code, and compile. A new port appears on the process, and it is automatable immediately.
8. **Add a second source**, a video file or a camera, and the video mixer.
9. **Try every blend mode** on your shader's input against the video, and write down two you would use and one that surprised you.
10. **Automate the blend.** Automate the mixer's opacity for one input so the composition changes over thirty seconds.
11. **Cross the boundary.** Add a lightness computer on the shader's output and an LED view to see the resulting pixels, so you can watch an image become data.

## Where to get shaders, and how to read one

Three sources, in the order worth trying.

**The user library.** *score* ships with utility and fulldome shaders, and the package manager provides more. These are already known to work, and several are worth reading as examples of the header format.

**The public ISF collections.** Because ISF is an open specification, there is a large body of shaders published for other tools. Most work unchanged, and the ones that do not usually fail on a feature named in their header, which the error pane will tell you.

**Your own.** Starting from an existing shader and changing it is how nearly everyone begins, and it is a legitimate end point too.

When reading an unfamiliar shader, read the header first: the declared inputs tell you what it is *for* far faster than the code does. A shader with `speed`, `scale`, and `colour` inputs is a pattern generator; one with an image input and a `threshold` is a filter. Then find where each input is used in the code, and you know which port to reach for.

## Editing while it runs

The compile loop makes *score* a live-coding environment, and there are two ways to use that.

**In rehearsal, as a fast iteration loop.** Change a number, compile, hear or see the result immediately, without stopping and restarting. This is simply faster than the alternative and it is how most shader work gets done.

**In performance, as material.** Editing a running score is supported: processes, sounds, and shaders can be added, removed, and altered while it plays. Some performers work this way deliberately, and the refusal of invalid code is what makes it survivable, since a typo cannot produce a flash or a burst of noise.

Two cautions if you perform this way. Devices must exist before you press play, without exception, so every output is declared in advance. And the compile step is not instantaneous on a complex shader, so a change made on a beat will not land on that beat; if timing matters, prepare the variant and switch to it rather than typing it live.

## Common mistakes

- **Editing code and not compiling.** The engine runs what was compiled, not what is in the editor.
- **Expecting invalid code to break something.** It is refused; check the error pane rather than assuming nothing happened.
- **Adding a device mid-performance.** Not possible. Declare every output before playing.
- **Cabling numbers into image inputs.** Numbers go to declared parameters.
- **A chain of many shaders** where one edited shader would do, at a real frame-rate cost per pass.
- **Ignoring blend modes** and mixing everything with opacity alone, which produces flat results.
- **Forgetting that a lightness computer reads back from the GPU.** Budget for it.

## Exercise

Take a shader from the library, add one new declared input to its header, use it in the code, and automate it from the timeline. Then mix that shader with a second source using at least two different blend modes over the course of thirty seconds, and finally send the shader's output through a lightness computer into an LED view.

**Success criterion:** the new port appears and is automatable, the mix changes character audibly, and the LED view shows pixels derived from your shader. If a shader from an external collection refused to compile, note the line the error pane pointed at.

## Going further

- [The shader process]({{ site.docs_baseurl }}/processes/shader.html) and the [ISF specification](https://isf.video).
- [Live coding]({{ site.docs_baseurl }}/common-practices/8-live-coding.html) for the editor, the compile shortcut, and the device caveat.
- [Video mixing]({{ site.docs_baseurl }}/common-practices/11-video-mixing.html) for the mixer and blend modes.
- [Pixel utilities]({{ site.docs_baseurl }}/processes/pixel-utilities.html) and [LED design]({{ site.docs_baseurl }}/common-practices/13-led-design.html) for the image-to-data path.
