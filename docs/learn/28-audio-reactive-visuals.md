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

> **Before this lesson** finish [Lesson 27]({{ site.baseurl }}/learn/27-3d-scenes.html), since it joins Module G's audio to Module I's images.
>
> **You will need** a sound file with clear dynamics, and a shader with at least one interesting parameter.
>
> **You will build** an image that responds to sound in a way you can tune, and that keeps responding when the material changes.

## Why this matters

Audio-reactive visuals are the most requested and the most often disappointing technique in this field, because the mechanism is trivial, three objects in a line, while the result is usually either imperceptible or a strobing mess. The difference lies entirely in the conditioning between the sound and the image, which is why this lesson comes after Module E and not before it. In other words, you already have the tools, and this lesson is an application of them.

Furthermore, the lesson collects a specific trap that has appeared twice already: routing audio into an analysis process removes it from the mix, because connecting a cable removes propagation. In audio-reactive work you always want both the sound and the analysis, so you will always need to switch propagation back on, and knowing that in advance saves ten minutes of confusion.

## Concepts

### The three-object chain

The chain is three objects, and the middle one carries the difficulty. An **envelope** turns audio into a number, a **conditioning** stage scales and smooths it, and a **destination** parameter on an image process consumes it; the conditioning stage is where the tuning described below takes place.

### RMS and peak measures

The two measures have different characters. An RMS (root mean square) measure follows perceived loudness and moves smoothly. In contrast, a peak measure follows transients and moves abruptly, so the first suits continuous properties, such as brightness, scale, or drift, and the second suits events that should hit, such as a flash, a jump, or a trigger. In *score* these are two separate processes and not two outputs of one, so the choice is which of them you add.

### Scaling the range

Range is the first problem, because envelope output is small. Image parameters usually expect a different range entirely, so without scaling the image does not move and the technique appears not to work; a small multiplying and offsetting object, or a mapping curve per Lesson 13, is the fix.

### Smoothing the jitter

Smoothing is the second problem, because raw envelope output jitters. Applied directly to a visual parameter, the raw value produces movement that reads as noise instead of response, and smoothing calms it at the cost of latency. However, for visuals a surprising amount of latency is acceptable, since the eye forgives twenty milliseconds where the ear does not.

### The response curve

A curve is the third problem and the most important one. A linear relationship between loudness and a visual parameter rarely feels right, because both hearing and seeing are non-linear, so a mapping curve that is flat at the bottom, where quiet passages should produce no movement, and steep in the middle, where the interesting range should be expressive, is what separates a good result from a mechanical one.

## Walkthrough: from sound to image, tuned

![A sound file feeding an RMS envelope, its reading drawn by a signal display over the waveform, a micromap scaling it, and the result driving a shader's zoom parameter, with the rendered image in the inspector]({{ site.img }}/28/28-01-audio-reactive-chain.png)

The chain in the figure is the whole lesson in one frame. The sound file's output reaches `RMS`; the signal display draws the reading as a white line over the waveform; `Micromap` multiplies it by twenty; and the result is cabled into the `zoom` parameter of a shader, whose rendered image sits in the inspector on the right. The capture is paused part-way through, which is why the white line stops where it does; the line to its left is what the analysis produced from this material.

{: .note }
> **The two measures are two processes, and the follower is a third thing.** `Analysis > Envelope` holds three entries in 3.8.2: `RMS` and `Peak` each take an audio input and give a single value out, alongside `Gain` and `Gate` controls, so you choose between them by adding the one you want. `Envelope Follower (audio)`, however, is a sample-level follower whose output is **audio** and not a number, so it is not the object this lesson wants.

1. **Start with both halves working separately**, a sound file playing per Lesson 20 and a shader on screen through a window device per Lesson 25, and confirm each independently before connecting them.
2. **Add an envelope** and cable the sound file's audio output into it, choosing `RMS` for continuous work and `Peak` for transients.

   {: .warning }
   > **Propagation has to be switched back on.** Cabling audio into the envelope removes the dry path, as Lesson 19 established, so switch propagate back on in the source outlet's inspector, which is the next step, or you will have a responsive image and silence.

3. **Turn propagate back on** in the sound file's outlet inspector, so that you can still hear the material.
4. **Observe the envelope** by adding a signal display on its first output and playing; you should see a reading that follows the loudness, and if it looks flat, the cause is scale and not failure.
5. **Scale it** by inserting a small multiplying object and raising the value until the display uses its full height.
6. **Cable it to a shader parameter** and play, so that something moves; this is the whole technique, and it probably looks bad.
7. **Tune it** by inserting a mapping curve and drawing a relationship that is flat at the bottom, so that silence produces no movement, and steep through the range your material occupies.
8. **Add smoothing** and increase it until the movement stops twitching, then reduce it until the response stops feeling late, and note both values.
9. **Compare the two measures** by swapping the `RMS` process for a `Peak` process and watching the difference, continuous against percussive, then keep whichever suits the parameter.
10. **Drive a second parameter differently** by taking a second branch from the same envelope with its own curve and smoothing, so that one sound moves two visual properties with different characters; this is where the result starts to look composed instead of automatic.
11. **Change the material** by playing a different sound file through the same chain; if the visual stops responding, your curve is tuned to one recording and not to a range, which is the most common fragility in this technique.
12. **Analyse a group instead of the whole mix** by moving the analysis from the master to one sub-scenario, and note what the image now follows.

## Making it survive different material

The failure that matters is a chain tuned to one file, since a broken chain announces itself whereas a fragile one fails on the next piece of material; tuning against extremes, bounding the curve, and calibrating prevent it.

**Tune against your quietest and loudest material, and not against your favourite recording.** Play the extremes through the chain and set the curve so that both produce something acceptable.

**Prefer a curve with a floor and a ceiling to a linear relationship with a high multiplier.** A floor means that quiet material produces no movement in place of something faint and ugly, whereas a ceiling means that loud material saturates instead of breaking the image.

**Consider a calibrator when the material is out of your control.** The same object from Lesson 13 that learns a sensor's range can learn a signal's range, which makes the chain adapt without retuning. Moreover, this is the right answer for an installation that will play material chosen by someone else.

The general principle reaches beyond this lesson, because a mapping tuned to a single input demonstrates the technique, whereas a mapping tuned to a range can be played as an instrument.

## Beyond loudness

Loudness is the easiest feature to extract and the least interesting one, because it makes every visual respond to every sound at once, and three routes lead past it, in increasing order of effort: choosing the source, combining two measures, and analysing frequency content.

**Choosing the source is the cheapest improvement**, and analysing the right source matters as much as the conditioning, which step 12 put into practice. Analysing the master output means that every visual responds to every sound at once. Conversely, analysing one source, or one group, gives you a visual that responds to a specific element, which is usually the more musical choice.

**Using two features with different characters gives an image both a mood and a pulse.** A continuous measure for slow properties and a peak measure for hits, per this lesson, produce an image whose mood and whose accents come from different aspects of the same sound.

**Analysing frequency content is the most expensive route.** *score* has more analysis than the envelope, and driving separate visual properties from separate bands is what makes a visual look like it is listening instead of merely reacting. Nevertheless, this costs more tuning, and it is the difference people notice.

A single rule holds across all three routes: the relationship should be legible to an audience who cannot see your patch. If a viewer cannot tell what the image is following, the mapping is decoration and not reaction, which may be a legitimate choice if you know you made it.

## Common mistakes

- **Losing the sound**, because the cable removed propagation; this is the first thing to check when the image responds and the room is quiet.
- **Applying no scaling**, so that the envelope's small output leaves the image apparently unresponsive.
- **Using a linear mapping**, which is technically correct and rarely expressive.
- **Leaving a continuous parameter unsmoothed**, which gives jitter that reads as noise.
- **Over-smoothing a percussive parameter**, so that hits arrive after the sound.
- **Analysing the master** when you meant to follow one element.
- **Tuning to one file**, so that the next piece of material breaks the chain.
- **Using the peak measure for every parameter** because it looks more responsive on the display.

## Exercise

Build a chain from one sound source to two visual parameters, with different measures, curves, and smoothing for each, so that one follows loudness continuously while the other hits on transients. Then play three different sound files through it, including your quietest and loudest, and adjust until all three produce something you would show.

**Success criterion:** the sound remains audible, both parameters respond in visibly different characters, and all three files work without retuning. State the smoothing values you chose and why they differ between the two branches.

## Going further

- [Making audio-reactive visuals]({{ site.docs_baseurl }}/common-practices/5-video.html), the reference recipe, including the small mapping object.
- [Audio utilities]({{ site.docs_baseurl }}/processes/audio-utilities.html) for the envelope, and [signal display]({{ site.docs_baseurl }}/processes/signal-display.html) for observing it.
- [Audio-reactive example]({{ site.docs_baseurl }}/examples/video/audioreactive.html), which is worth opening and taking apart.
- [Mapping]({{ site.docs_baseurl }}/processes/mapping.html) and [calibrator]({{ site.docs_baseurl }}/processes/calibrator.html) for the conditioning stage.
