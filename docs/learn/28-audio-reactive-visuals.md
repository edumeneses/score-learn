---
layout: default
title: "Lesson 28: Audio-reactive visuals"
description: "Extract a value from sound and drive an image with it, with the scaling, smoothing, and propagation details that make it usable."
parent: Lessons
nav_order: 33
unit: "28"
permalink: /learn/28-audio-reactive-visuals.html
score_version: "3.8.2"
reading_time: "14 min"
practice_time: "30 min"
score_file: none
---

# Lesson 28: Audio-reactive visuals

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 27]({{ site.baseurl }}/learn/27-3d-scenes.html). You need Module G's audio and Module I's images.
>
> **You will need** a sound file with clear dynamics, and a shader with at least one interesting parameter.
>
> **You will build** an image that responds to sound in a way you can tune, and that keeps responding when the material changes.

## Why this matters

Audio-reactive visuals are the most requested and most often disappointing technique in this field. The mechanism is trivial, three objects in a line, and the result is usually either imperceptible or a strobing mess. The difference is entirely in the conditioning between the sound and the image, which is why this lesson comes after Module E rather than before it: you already have the tools, and this is an application of them.

The lesson also collects a specific trap that has appeared twice already. Routing audio into an analysis process removes it from the mix, because connecting a cable removes propagation. In audio-reactive work you always want both the sound and the analysis, so you will always need to switch propagation back on, and knowing that in advance saves the ten minutes everybody loses to it.

## Concepts

**The chain is three objects.** An **envelope** turns audio into a number. A **conditioning** stage scales and smooths it. A **destination** parameter on an image process consumes it. Everything difficult is in the middle object.

**Two measures, different characters.** The envelope's first output is a root-mean-square measure, which follows perceived loudness and moves smoothly. Its second is a peak measure, which follows transients and moves abruptly. Use the first for anything continuous, brightness, scale, drift; use the second for anything that should hit, a flash, a jump, a trigger.

**Range is the first problem.** Envelope output is small, and image parameters usually expect something else entirely. Without scaling, the image does not move and the technique appears not to work. A small multiplying and offsetting object, or a mapping curve per Lesson 13, is the fix.

**Smoothing is the second problem.** Raw envelope output applied to a visual parameter produces jitter, which reads as noise rather than as response. Smoothing calms it at the cost of latency, and for visuals a surprising amount of latency is acceptable: the eye forgives twenty milliseconds where the ear does not.

**A curve is the third and most important.** A linear relationship between loudness and a visual parameter almost never feels right, because both hearing and seeing are non-linear. A mapping curve that is flat at the bottom, so quiet passages do nothing, and steep in the middle, so the interesting range is expressive, is what separates a good result from a mechanical one.

**Propagation.** Cabling audio into the envelope removes the dry path. Switch propagate back on in the source outlet's inspector, or you will have a responsive image and silence.

**Analyse the right thing.** Analysing the master output means everything drives everything. Analysing one source, or one group, gives you a visual that responds to a specific element, which is usually the more musical choice.

## Walkthrough: from sound to image, tuned

{: .note }
> A figure for this lesson is pending: it needs audio content and a live GPU session, so it requires media this course does not ship. See `checks/28-audio-reactive-visuals.md`.

1. **Start with both halves working separately.** A sound file playing, per Lesson 20, and a shader on screen through a window device, per Lesson 25. Confirm each independently before connecting them.
2. **Add an envelope** and cable the sound file's audio output into it.
3. **Turn propagate back on** in the sound file's outlet inspector, so you can still hear the material. Do this now rather than wondering later.
4. **Observe the envelope.** Add a signal display on its first output and play. You should see a reading that follows the loudness. If it looks flat, it is scale, not failure.
5. **Scale it.** Insert a small multiplying object and raise the value until the display uses its full height. You are now looking at a usable control signal.
6. **Cable it to a shader parameter** and play. Something should move. This is the whole technique, and it probably looks bad.
7. **Now tune it.** Insert a mapping curve and draw a relationship: flat at the bottom so silence does nothing, steep through the range your material actually occupies.
8. **Add smoothing** and increase it until the movement stops twitching, then reduce it until the response stops feeling late. Note both values.
9. **Compare the two measures.** Swap the root-mean-square output for the peak output and watch the difference: continuous against percussive. Keep whichever suits the parameter.
10. **Drive a second parameter differently.** From the same envelope, take a second branch with its own curve and smoothing, so one sound moves two visual properties with different characters. This is where the result starts to look composed rather than automatic.
11. **Change the material.** Play a different sound file through the same chain. If the visual stops responding, your curve is tuned to one recording rather than to a range, which is the most common fragility in this technique.
12. **Analyse a group instead of everything.** Move the analysis from the master to one sub-scenario and hear the difference in what the image is following.

## Making it survive different material

The failure that matters is not a broken chain, it is a chain tuned to one file. Three habits.

**Tune against your quietest and loudest material, not your favourite.** Play the extremes through the chain and set the curve so both produce something acceptable.

**Prefer a curve with a floor and a ceiling** to a linear relationship with a high multiplier. A floor means quiet material does nothing rather than something faint and ugly; a ceiling means loud material saturates instead of breaking the image.

**Consider a calibrator.** The same object from Lesson 13 that learns a sensor's range can learn a signal's range, which makes the chain adapt instead of needing retuning. This is the right answer for an installation that will play material chosen by someone else.

The general principle, worth stating because it applies far beyond this lesson: a mapping tuned to a single input is a demonstration; a mapping tuned to a range is an instrument.

## Beyond loudness

Loudness is the easiest feature to extract and the least interesting one, because it makes every visual respond to everything at once. Three ways to get further, in order of effort.

**Analyse a group rather than the master.** The cheapest improvement available: a visual following one instrument reads as related to that instrument, while a visual following the mix reads as a level meter.

**Use two features with different characters.** A continuous measure for slow properties and a peak measure for hits, per this lesson, gives an image that has both a mood and a pulse.

**Analyse frequency content.** *score* has more analysis than the envelope, and driving separate visual properties from separate bands is what makes a visual look like it is listening rather than reacting. This costs more tuning and it is the difference people notice.

One rule holds across all three: the relationship should be legible to an audience who cannot see your patch. If a viewer cannot tell what the image is following, the mapping is decoration rather than reaction, which may be fine, and is worth knowing you chose.

## Common mistakes

- **Losing the sound.** Propagation was removed by the cable. This is the first thing to check when the image responds and the room is quiet.
- **No scaling.** The envelope's output is small; the image appears not to react.
- **A linear mapping.** Technically correct and rarely expressive.
- **No smoothing on a continuous parameter**, giving jitter that reads as noise.
- **Too much smoothing on a percussive parameter**, so hits arrive after the sound.
- **Analysing the master** when you meant to follow one element.
- **Tuning to one file.** The next piece of material will break it.
- **Using the peak measure for everything** because it looks more responsive on the display.

## Exercise

Build a chain from one sound source to two visual parameters, with different measures, curves, and smoothing for each: one following loudness continuously, one hitting on transients. Then play three different sound files through it, including your quietest and loudest, and adjust until all three produce something you would show.

**Success criterion:** the sound remains audible, both parameters respond in visibly different characters, and all three files work without retuning. State the smoothing values you chose and why they differ between the two branches.

## Going further

- [Making audio-reactive visuals]({{ site.docs_baseurl }}/common-practices/5-video.html), the reference recipe, including the small mapping object.
- [Audio utilities]({{ site.docs_baseurl }}/processes/audio-utilities.html) for the envelope, and [signal display]({{ site.docs_baseurl }}/processes/signal-display.html) for observing it.
- [Audio-reactive example]({{ site.docs_baseurl }}/examples/video/audioreactive.html), which is worth opening and taking apart.
- [Mapping]({{ site.docs_baseurl }}/processes/mapping.html) and [calibrator]({{ site.docs_baseurl }}/processes/calibrator.html) for the conditioning stage.
