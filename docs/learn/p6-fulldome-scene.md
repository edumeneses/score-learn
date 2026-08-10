---
layout: default
title: "Milestone P6: a fulldome scene reacting to live audio"
description: "A ten-minute dome-format set: fisheye output, audio-reactive visuals, a cue list, and a document that transfers to a real dome."
parent: Lessons
nav_order: 34
unit: "P6"
permalink: /learn/p6-fulldome-scene.html
score_version: "3.8.2"
reading_time: "15 min"
practice_time: "60 min"
score_file: none
---

# Milestone P6: a fulldome scene reacting to live audio

{% include lesson_meta.html %}

> **Before this milestone** finish Lessons 25 to 28. This unit introduces nothing new, and it closes Phase 2.
>
> **You will need** a sound source, a window device, and an hour. No dome is required.
>
> **You will build** a ten-minute dome-format set, monitored in a window, with a cue list you can perform and a document that would transfer to a real dome.

## Why this matters

A dome is the most demanding output surface in common use and the one where authoring on a laptop is least like the result. Everything you know about framing stops applying: there are no corners, the audience is not facing one direction, and content designed for a rectangle looks wrong in a way that is hard to predict from a monitor.

This milestone therefore has two goals, and the second is the harder one. Build something that works, and build it so that the transfer to a real dome is a configuration change rather than a rewrite. That discipline, parameterising what the venue decides, is the same one Lesson 22 asked for with speaker layouts, and it is what makes immersive work practical rather than heroic.

## The brief

Build a document that:

1. outputs in **fisheye projection**, so the same content could be sent to a dome;
2. runs for **ten minutes** as a sequence of **at least four scenes**, each in its own sub-scenario;
3. has **at least two audio-reactive relationships** with different characters, per Lesson 28;
4. is **performable**: scenes advance by cue, not only by clock, so a live sound source can breathe;
5. keeps every **venue-dependent value in one place**: resolution, projection, output routing, brightness ceiling;
6. never **strobes or flashes** unintentionally, which in a dome is a safety matter, not an aesthetic one;
7. ships with a **technical page**: what it outputs, what it needs, and how to reduce it if the venue has less.

## Concepts you are assembling

**Fisheye as the output format.** Dome projection systems expect a circular fisheye image. Producing one in a window on your desk is what makes the work portable: you author into the same projection the dome will consume, so nothing is reinterpreted later.

**Scenes as sub-scenarios.** Per Lesson 17 and the scene pattern, each section is a sub-scenario in its own interval, which makes it rehearsable with local play and legible when folded.

**Cued advance.** Triggers between scenes, per Lesson 15, with maximum durations so the set cannot stall. This is the structure that lets a ten-minute piece follow a live player rather than a stopwatch.

**Two reactive characters.** One continuous relationship and one percussive, per Lesson 28, each with its own curve and smoothing.

**A venue block.** One place in the document, or one small group of parameters, holding everything the room decides. When you arrive at the dome, you change those and nothing else.

## Walkthrough

{: .note }
> A figure for this lesson is pending: it needs a live GPU session, a fisheye output, and audio content. See `checks/p6-fulldome-scene.md`.

1. **Set up the output first.** A window device showing a fisheye projection, at a resolution you can actually run. Confirm the frame rate before building content, per Lesson 25.
2. **Build one scene completely.** One generated image, one reactive relationship, one exit trigger. Rehearse it alone.
3. **Judge it as a dome image, not a picture.** Content near the edge of a fisheye circle lands overhead or behind the audience. Whatever you place there will be missed by most of the room, and whatever you place at the centre is directly overhead, which is the most physically affecting position and the easiest to overuse.
4. **Duplicate to four scenes**, each with a different visual idea, saving the working scene as a fragment first.
5. **Add the second reactive relationship**, percussive, in at least two of the scenes.
6. **Chain the scenes with triggers**, each with a maximum duration so the set always advances.
7. **Add the venue block.** Collect resolution, projection parameters, output channel, and a brightness ceiling into one group of parameters, and make everything else read from them.
8. **Impose the brightness ceiling.** A dome fills the audience's whole field of view; what reads as bright on a monitor is overwhelming overhead. Put a ceiling on output brightness and respect it everywhere.
9. **Check for unintentional strobing.** Play the set and watch for any rapid full-field luminance change, particularly ones your audio-reactive chains could produce on a transient. Fix by smoothing or by capping the rate of change, not by hoping the material stays calm.
10. **Rehearse with live sound.** Play into it rather than playing a file, and note where the reactive tuning fails, which will be at the quiet end.
11. **Write the technical page**: output format and resolution, what it expects to receive, the venue block's values, the brightness ceiling, and a reduced version for a smaller system.

## Authoring for a room you have never been in

Four things that are cheap now and expensive at the venue.

**Test at the target resolution, not at a comfortable one.** A dome system may want considerably more pixels than your monitor. Discovering the frame-rate limit at the venue is the classic failure of immersive work.

**Keep a reduced version.** Half resolution, fewer layers, one reactive chain instead of two. A dome that cannot run your full version is not a disaster if the reduced one is ready and tested.

**Do not rely on precise geometry.** Dome calibration varies; content whose meaning depends on an exact edge or a precise alignment will not survive. Content whose meaning is in movement and mass will.

**Write down what you cannot test.** Honesty here is worth more than optimism: "brightness has only been judged on a monitor" is useful information for whoever helps you install it.

## What a dome does to material

Four perceptual facts that are cheap to state and expensive to learn at the venue.

**Peripheral motion is physical.** Movement at the edge of the field of view produces bodily responses, including nausea, that the same movement on a screen does not. Slow it down, and treat fast wide movement as a deliberate, sparing effect.

**There is no frame to compose against.** Rules about thirds, edges, and centring do not apply. What organises a dome image is mass, movement, and contrast, which is closer to how sound is organised than to how a picture is.

**The audience is not facing one direction.** Anything meaningful in one place will be missed by part of the room. Either repeat it around the dome or accept that it is an accent rather than a focus.

**Overhead is the strongest position** and the easiest to exhaust. Content directly above is unavoidable and affecting; using it constantly flattens the effect within minutes.

None of this is specific to *score*, and all of it changes what you should build with it, which is why this milestone asks you to judge the image as a dome image from the first scene rather than at the end.

## Common mistakes

- **Authoring rectangular and converting later.** The framing decisions do not survive the conversion.
- **Detail at the edge of the circle.** Most of the audience will not be looking there.
- **Brightness judged on a monitor.** A dome is far more affecting; assume you are too bright.
- **Unintentional strobing from a reactive chain.** This is a safety matter. Cap rates of change.
- **Venue values scattered through the document.** Then the load-in becomes an edit session.
- **No reduced version.** The venue's machine is not your machine.
- **A set that only follows the clock.** With live sound, the cue-based advance is what makes it a performance.

## Exercise

Extend the set in one direction, and one only.

Either **make it spatial in both media**: send one audio layer through the four-speaker scene from Lesson 22, so that a moving sound corresponds to a moving element in the image, and document how both would scale to a real rig.

Or **make it operable by someone else**: reduce the performance interface to at most four controls, write the page, and have another person run the set from it while you watch without intervening.

**Success criterion:** the set runs for ten minutes in fisheye at your target resolution, advances by cue with guaranteed maximum durations, has no unintentional full-field flashes, and its venue-dependent values live in one place. Keep it: it is the strongest single artefact for demonstrating what you can do with this software.

## Going further

- [Fulldome shaders]({{ site.docs_baseurl }}/processes/shaders/) in the shipped library, several of which are dome-specific.
- [Video techniques]({{ site.docs_baseurl }}/common-practices/5-video.html) and [video mixing]({{ site.docs_baseurl }}/common-practices/11-video-mixing.html).
- [Scenes]({{ site.docs_baseurl }}/common-practices/6-scenes.html) for the structural pattern.
- [Spatial audio]({{ site.docs_baseurl }}/common-practices/14-spatial-audio.html) if you take the spatial extension.
