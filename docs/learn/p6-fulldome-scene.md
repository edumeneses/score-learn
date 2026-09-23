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

> **Before this milestone** finish Lessons 25 to 28, because this unit introduces no new technique, and it closes Phase 2.
>
> **You will need** a sound source, a window device, and an hour, while no dome is required at any point.
>
> **You will build** a ten-minute dome-format set, monitored in a window, with a cue list that can be performed and a document that would transfer to a real dome.

## Why this matters

A dome is the most demanding output surface in common use and the one where authoring on a laptop is least like the result, because what you know about framing stops applying: there are no corners, the audience is not facing one direction, and content designed for a rectangle looks wrong in a way that is hard to predict from a monitor.

This milestone therefore has two goals, of which the second is the harder: build something that works, and build it so that the transfer to a real dome is a configuration change and not a rewrite. Moreover, parameterising what the venue decides is the same practice Lesson 22 asked for with speaker layouts, and it is what makes immersive work practical instead of heroic, since a piece that must be rebuilt at each venue is performed at few of them.

## The brief

Build a document that:

1. outputs in **fisheye projection**, so that the same content could be sent to a dome;
2. runs for **ten minutes** as a sequence of **at least four scenes**, each in its own sub-scenario;
3. has **at least two audio-reactive relationships** with different characters, per Lesson 28;
4. is **performable**, because scenes advance by cue and not only by clock, so that a live sound source can breathe;
5. keeps every **venue-dependent value in one place**, which means resolution, projection, output routing, and brightness ceiling;
6. does not **strobe or flash** unintentionally, which in a dome is a safety matter before it is an aesthetic one;
7. ships with a **technical page** stating what it outputs, what it needs, and how to reduce it if the venue has less.

## Concepts you are assembling

### Fisheye output

Dome projection systems expect a circular fisheye image, so fisheye is the output format from the first scene. Producing one in a window on your desk is what makes the work portable, because you author into the same projection the dome will consume and no framing decision is reinterpreted later.

### Scenes as sub-scenarios

Each scene is a sub-scenario in its own interval, per Lesson 17 and the scene pattern, which makes it rehearsable with local play and legible when the document is folded.

### Scenes that advance on triggers

Scenes advance on triggers, per Lesson 15, each with a maximum duration so that the set cannot stall. This is the structure that lets a ten-minute piece follow a live player instead of a stopwatch. Simultaneously, the maximum durations guarantee that it advances even when no cue arrives.

### Two reactive characters

The two reactive relationships have different characters, one continuous and one percussive, per Lesson 28, each with its own curve and its own smoothing.

### The venue block

A venue block is one place in the document, or one small group of parameters, holding every value the room decides. When you arrive at the dome, you change those values and no others, which is the whole of the transfer the second goal asked for.

## Walkthrough

{: .note }
> A figure for this lesson is pending: it needs a live GPU session, a fisheye output, and audio content. See `checks/p6-fulldome-scene.md`.

1. **Set up the output first**, as a window device showing a fisheye projection at a resolution your machine can run, and confirm the frame rate before building content, per Lesson 25.
2. **Build one scene completely**, with one generated image, one reactive relationship, and one exit trigger, and rehearse it alone before any other scene exists.
3. **Judge it as a dome image and not as a picture**, because content near the edge of a fisheye circle lands at the horizon, beside or behind the audience, where most of the room will miss it, whereas content at the centre is directly overhead, which is the most physically affecting position and the easiest to overuse.
4. **Duplicate to four scenes**, each with a different visual idea, after saving the working scene as a fragment so that each copy starts from a tested structure.
5. **Add the second reactive relationship**, the percussive one, in at least two of the scenes.
6. **Chain the scenes with triggers**, each with a maximum duration, so that the set advances whether or not a cue arrives.
7. **Add the venue block** by collecting resolution, projection parameters, output channel, and a brightness ceiling into one group of parameters, and make every other part of the document read from them.
8. **Impose the brightness ceiling**, because a dome fills the audience's whole field of view and what reads as bright on a monitor is overwhelming overhead; put a ceiling on output brightness and respect it in every scene.
9. **Check for unintentional strobing** by playing the set and watching for any rapid full-field luminance change, particularly the ones your audio-reactive chains could produce on a transient, and fix it by smoothing or by capping the rate of change, since hoping the material stays calm is not a fix.
10. **Rehearse with live sound**, playing into the set instead of playing a file, and note where the reactive tuning fails, which will be at the quiet end.
11. **Write the technical page**, which lists the output format and resolution, what the set expects to receive, the venue block's values, the brightness ceiling, and a reduced version for a smaller system.

## Authoring for a room you have never been in

Several precautions cost minutes at your desk and hours at the venue, and each of the four below can be taken before the technical page is written.

**Test at the target resolution instead of at a comfortable one**, because a dome system may want considerably more pixels than your monitor, and discovering the frame-rate limit at the venue is the classic failure of immersive work.

**Keep a reduced version at half resolution, with fewer layers and one reactive chain instead of two**, so that a dome which cannot run the full version is an inconvenience and not a disaster.

**Do not rely on precise geometry**, because dome calibration varies from one installation to the next; content whose meaning depends on an exact edge or a precise alignment will not survive. Conversely, content whose meaning is in movement and mass will.

**Write down what you could not test**, since a plain statement such as "brightness has only been judged on a monitor" is more useful to whoever helps you install the piece than an optimistic page that hides the gap.

## What a dome does to material

A dome changes how material is perceived in ways that a monitor cannot show, and each of the four effects below changes a decision you would otherwise make as if for a screen.

**Peripheral motion is physical**, because movement at the edge of the field of view produces bodily responses, including nausea, that the same movement on a screen does not; slow it down, and treat fast wide movement as a sparing effect used on purpose.

**There is no frame to compose against**, so rules about thirds, edges, and centring do not apply. In contrast, what organises a dome image is mass, movement, and contrast, which is closer to how sound is organised than to how a picture is.

**The audience is not facing one direction**, so an element that is meaningful in one place will be missed by part of the room, and you must either repeat it around the dome or accept that it is an accent and not a focus.

**Overhead is the strongest position and the easiest to exhaust**, because content directly above is unavoidable and affecting. However, using it constantly flattens the effect within minutes.

None of these effects is specific to *score*. Nevertheless, all of them change what you should build with it, which is why this milestone asks you to judge the image as a dome image from the first scene instead of at the end.

## Common mistakes

- **Authoring rectangular and converting later** loses the framing decisions, which do not survive the conversion.
- **Detail at the edge of the circle** is wasted, because most of the audience will not be looking there.
- **Brightness judged on a monitor** underestimates a dome, which is far more affecting, so assume that you are too bright.
- **Unintentional strobing from a reactive chain** is a safety matter before it is an aesthetic one, and capping rates of change is how it is prevented.
- **Venue values scattered through the document** turn the load-in into an edit session.
- **Arriving with no reduced version** assumes that the venue's machine is your machine, which it is not.
- **A set that only follows the clock** stops being a performance with live sound, because the cue-based advance is what lets the set follow the player.

## Exercise

Pick one extension and build it completely before considering the other, since each one changes what the technical page has to describe.

Either **make it spatial in both media** by sending one audio layer through the four-speaker scene from Lesson 22, so that a moving sound corresponds to a moving element in the image, and document how both would scale to a real rig.

Or **make it operable by someone else** by reducing the performance interface to at most four controls, writing the page, and having another person run the set from it while you watch without intervening.

**Success criterion:** the set runs for ten minutes in fisheye at your target resolution, advances by cue with guaranteed maximum durations, has no unintentional full-field flashes, and keeps its venue-dependent values in one place. Keep it, because it is the strongest single artefact for demonstrating what you can do with this software.

## Going further

- [Fulldome shaders]({{ site.docs_baseurl }}/processes/shaders/) in the shipped library, several of which are dome-specific.
- [Video techniques]({{ site.docs_baseurl }}/common-practices/5-video.html) and [video mixing]({{ site.docs_baseurl }}/common-practices/11-video-mixing.html).
- [Scenes]({{ site.docs_baseurl }}/common-practices/6-scenes.html) for the structural pattern.
- [Spatial audio]({{ site.docs_baseurl }}/common-practices/14-spatial-audio.html) if you take the spatial extension.
