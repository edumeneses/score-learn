---
layout: default
title: "Lesson 26: Shaders (ISF) and video mixing"
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

# Lesson 26: Shaders (ISF) and video mixing

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 25]({{ site.baseurl }}/learn/25-video-pipeline.html), and have a window device declared, since every image this lesson produces needs a destination.
>
> **You will need** no material beyond *score* itself, because shaders generate their own images.
>
> **You will build** a generated image from a shader you edited, combined with a second source, with parameters automated from the timeline.

## Why this matters

A shader is the most direct route from an idea to an image in this software, and ISF (Interactive Shader Format) makes it unusually approachable, because a shader declares its parameters in a small block of metadata and *score* turns those declarations into ports. The consequence to hold on to is that **a shader's parameters are automatable, mappable, and drivable from a sensor, in the same way as a device parameter**; you are not scripting graphics off to one side, but adding processes whose controls behave like every other control in the course.

Furthermore, this is the first lesson in which you write code, and it is the gentlest of them by design, because editing three lines of an existing shader and recompiling teaches the loop that Module J then applies to audio, MIDI (Musical Instrument Digital Interface), and logic.

## Concepts

### The ISF header

An ISF shader is a fragment shader plus a JSON (JavaScript Object Notation) header declaring its inputs. The header lists each input's name, type, range, and default, and *score* reads it to create the ports; because the format is an open specification with a large public library of shaders, a great deal of existing material works without modification.

### The compile loop

The editor and the compile loop are how code reaches the running engine. Code-based processes carry a window button on their header that opens a script editor, in which you edit and then press compile, or use `Ctrl+Enter`, so that the running engine takes the new code. Invalid code is refused instead of applied, which means a typo cannot produce a flash or a burst of noise mid-performance, and the errors appear in a pane at the bottom of the editor.

### Generators and filters

Generators and filters differ only in whether the header declares an image input. A shader with no image input generates noise, gradients, patterns, or geometry. In contrast, a shader with an image input filters what arrives, and that single difference determines where in the graph the process belongs.

### Blend modes

Blend modes do the compositing. The eight-channel video mixer from Lesson 25 gives each input an opacity and a blend mode, and the blend modes are where most of the visual character of a mix comes from, which is why trying each one once on real material teaches more than reading their definitions.

### Pixel utilities

Pixel utilities cross the boundary between images and data. A family of processes converts in both directions, and the most useful member is a lightness computer that turns a texture into a series of pixel values, which is how a shader ends up driving an LED strip. That conversion takes the image off the GPU (graphics processing unit), which Lesson 25 flagged as the expensive operation. Nevertheless, the result frequently justifies the cost.

## Walkthrough: edit a shader, then mix it

![The ISF shader editor open on a kaleidoscope filter, the inputs its header declares listed as ports in the inspector, and the rendered result playing in the inspector's preview]({{ site.img }}/26/26-01-shader-editor.png)

The figure is Lesson 25's document with one shader added after the H.264 source, and reading across it completes the lesson's argument. The editor in the middle shows the ISF header, a JSON block at the top of the fragment source declaring `inputImage`, `sides`, `angle`, `slidex`, `slidey`, and `center`, each with its type, its range, and its default; the inspector on the right lists precisely those names as ports, and the panel below them is the rendered result.

{: .note }
> **The inspector previews the texture of a process while the score plays.** A process with a texture output shows its current frame in the inspector, which is the quickest way to see what a shader is doing; the figure's result is that preview, and the output window is still where the work goes, although it is not where you have to look while you edit. The same panel carries the outlet's `Size`, `Format`, `Filter`, and `Address mode`. The editor has two tabs, `Fragment` and `Vertex`, and a shader is compiled with the `Compile` button at its foot.

1. **Add a shader process** from the library, under `Visuals > ISF Shader`, and set its output to your window device so that an image appears. The fastest route is the one from Lesson 21: select the process the shader should follow, then double-click the library entry, and *score* connects it and moves the window output onto the new process for you.
2. **Find its ports** in the inspector, which lists the parameters declared in the header on the process itself, and move one to watch the image change.
3. **Automate a parameter** by right-clicking a port, creating an automation, and drawing a curve, then play; the shader is now part of your timeline and no longer a static effect.
4. **Open the editor** with the window button on the process header and read the header block, identifying one declared input and finding where the code uses it.
5. **Change one number** in the code, something visibly obvious such as a scale or a colour, and then compile, so that you see the image update while the score is running.
6. **Break it on purpose** by introducing a syntax error and compiling; the running image is unchanged and the error appears in the pane below, which is the refusal described in Concepts protecting the performance.
7. **Add a declared input** by adding an entry to the header block, using it in the code, and compiling, so that a new port appears on the process and is automatable immediately.
8. **Add a second source**, a video file or a camera, and the video mixer.

   {: .warning }
   > **Devices cannot be added during playback.** Shaders can be edited while the score plays, along with almost every other element of a document. However, one documented exception applies to the whole application, so every window, camera, and output you will need must exist before you press play, and a camera has to be declared with the score stopped.

9. **Try every blend mode** on your shader's input against the video, and write down two you would use and one that surprised you.
10. **Automate the blend** by automating the mixer's opacity for one input so that the composition changes over thirty seconds.
11. **Cross the boundary** by adding a lightness computer on the shader's output and an LED view to see the resulting pixels, so that you can watch an image become data.

## Where to get shaders, and how to read one

Shaders come from three sources, and the order below is the order in which to try them: the user library, the public ISF collections, and your own edits.

**The user library ships with utility and fulldome shaders**, and the package manager provides more; these are already known to work. Moreover, several are useful to read as examples of the header format.

**The public ISF collections exist because ISF is an open specification**, which has produced a large body of shaders published for other tools. Most of them work unchanged, and the ones that do not usually fail on a feature named in their header, which the error pane identifies.

**Your own shaders usually begin as edits of an existing one**, since starting from working code and changing it is how nearly everyone begins, and it is a legitimate end point as well.

When reading an unfamiliar shader, read the header first, because the declared inputs tell you what the shader is *for* far faster than the code does. In other words, a shader with `speed`, `scale`, and `colour` inputs is a pattern generator, whereas one with an image input and a `threshold` is a filter; then find where each input is used in the code, and you know which port to reach for.

## Editing while it runs

The compile loop makes *score* a live-coding environment, which can be used in rehearsal as a fast iteration loop or in performance as material, and the two uses carry different risks.

**In rehearsal, the loop shortens iteration.** You change a number, compile, and hear or see the result immediately, without stopping and restarting, which is faster than the alternative and is how most shader work gets done.

**In performance, the loop becomes material.** Editing a running score is supported, since processes, sounds, and shaders can be added, removed, and altered while it plays, and some performers work this way by choice; the refusal of invalid code described in Concepts is what makes it survivable.

Performing this way requires that every output be declared in advance, as the warning at step 8 noted, and it requires accepting that the compile step is not instantaneous on a complex shader. A change made on a beat will therefore not land on that beat, so if timing matters, prepare the variant in advance and switch to it during the performance.

## Common mistakes

- **Editing code and not compiling**, whereas the engine runs what was compiled and ignores what sits in the editor.
- **Expecting invalid code to break something**, although it is refused; check the error pane before assuming that no change happened.
- **Adding a device mid-performance**, which is not possible, so declare every output before playing.
- **Cabling numbers into image inputs**, when numbers belong on declared parameters.
- **Building a chain of many shaders** where one edited shader would do, at a real frame-rate cost per pass.
- **Ignoring blend modes** and mixing every source with opacity alone, which produces flat results.
- **Forgetting that a lightness computer reads back from the GPU**, and failing to budget for that cost.

## Exercise

Take a shader from the library, add one new declared input to its header, use it in the code, and automate it from the timeline. Then mix that shader with a second source using at least two different blend modes over the course of thirty seconds, and finally send the shader's output through a lightness computer into an LED view, so that the same image ends as data.

**Success criterion:** the new port appears and is automatable, the mix changes character visibly, and the LED view shows pixels derived from your shader. If a shader from an external collection refused to compile, note the line the error pane pointed at.

## Going further

- [The shader process]({{ site.docs_baseurl }}/processes/shader.html) and the [ISF specification](https://isf.video).
- [Live coding]({{ site.docs_baseurl }}/common-practices/8-live-coding.html) for the editor, the compile shortcut, and the device caveat.
- [Video mixing]({{ site.docs_baseurl }}/common-practices/11-video-mixing.html) for the mixer and blend modes.
- [Pixel utilities]({{ site.docs_baseurl }}/processes/pixel-utilities.html) and [LED design]({{ site.docs_baseurl }}/common-practices/13-led-design.html) for the image-to-data path.
