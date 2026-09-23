---
layout: default
title: "Milestone P3: a sensor to sound and light mapping bench"
description: "One emulated sensor, three mapped destinations, a calibration routine, and a written map: the instrument you will reuse for the rest of the course."
parent: Lessons
nav_order: 17
unit: "P3"
permalink: /learn/p3-mapping-bench.html
score_version: "3.8.2"
reading_time: "15 min"
practice_time: "60 min"
score_file: p3-mapping-bench/p3-bench.score
---

# Milestone P3: a sensor to sound and light mapping bench

{% include lesson_meta.html %}

> **Before this milestone** finish Lessons 10 to 14, because this unit introduces no new technique and combines the ones those lessons cover.
>
> **You will need** one input, emulated if you have no hardware, and about an hour.
>
> **You will build** a reusable bench in which one gesture drives three destinations through a documented, calibrated, tunable pipeline.

## Why this matters

The whole of Module F depends on having an input you trust, because a trigger fired by a value, a condition evaluated against a value, and a branch chosen by a value all assume that you know what your input does and that it does it reliably. Most interactive pieces that behave unpredictably do so because the input feeding the logic was not conditioned, and that is why this bench comes before the module that needs it.

Moreover, a bench changes how each later piece begins, because you build the mapping once, save it as a fragment, and start every new project from a known-good instrument, whereas without one the mapping is rebuilt inside each piece. Most experienced practitioners in this field keep some version of this file, and the brief below describes one.

## The brief

Build a document that:

1. takes **one input**, and works with an emulated one, so that it runs on any machine;
2. **calibrates** that input and records the learned range in writing;
3. drives **three destinations** with distinct characters: one immediate, one smoothed, one stepped or quantised;
4. keeps the pipeline **running for the whole score**, and not only inside one interval;
5. **observes** every stage, so that a wrong value can be located instead of guessed at;
6. ships with a **written map** of the input, each stage in order, and each output with its range;
7. is saved to the **user library** as a reusable fragment.

## Emulating an input

If you have no sensor, three emulations serve well, and the first is the one to prefer because it gives you control over the input's faults.

**A second application sending OSC (Open Sound Control) takes six lines in any language**, or a small Pure Data or Max patch with a slider, and it gives you full control over range, rate, and noise, which is better for a bench than a real sensor because you can *choose* how badly it behaves.

**A joystick or gamepad reaches *score* through its joystick device**, and any cheap controller gives you real axes with real jitter.

**A generator inside *score*, an LFO (low-frequency oscillator) plus a noise source, can be fed into your pipeline as though it were external.** Nevertheless, it is the least realistic option, since it does not drop out or saturate, although it needs no software installed.

Whichever you choose, give the input two defects on purpose, a range that is not 0 to 1 and visible jitter, because a bench tested on a clean input teaches you little.

## Concepts you are assembling

### The four-stage pipeline

The four-stage pipeline from Lesson 13 runs condition, relate, send, and observe in that order, and the bench keeps the stages separate so that each can be checked alone.

### Three intentions for one gesture

The three branches are three intentions for one gesture, whereas three copies of a mapping would be one intention repeated. Immediate means minimal smoothing and a curve that responds at once; smoothed means generous filtering and a curve that ignores small movements; stepped means that the continuous input becomes discrete, which is what a step or quantising object is for, and which feels categorically different to whoever is moving the sensor.

### Observation at every stage

Observation at every stage, using signal displays, turns "the light is not moving" into a question with a location.

## Walkthrough

![An LFO standing in for a sensor, conditioned once by a range filter, then branching three ways: straight to a signal display, through a smoothing filter, and through a multi-choice step, each branch ending in its own observation]({{ site.img }}/p3/p3-01-mapping-bench.png)

`p3-bench.score` ships with this milestone as the skeleton of the answer, with one input conditioned once, three branches, and an observation on each, whereas the calibration, the rate limiting, and the written map are yours to add.

Read from left to right, the `LFO` stands in for a sensor, which is the third emulation option above, and the `Range Filter` conditions that value **once** so that all three branches consume the same output; that shared stage is what keeps the branches comparable and what makes re-calibrating a single edit instead of three. The three characters then leave that shared stage in turn: straight through to a signal display, through `Smooth` set to a One Euro filter, and through `Multi-choice`, which turns the continuous value into a small number of levels.

However, the third branch's display is blank in the figure while the other two are alive, and that is not a mistake in the capture but what the fifth requirement buys you. A branch has gone quiet, and because every stage is observed you can see *which* one, so that the fault becomes a question with a location instead of a guess.

{: .note }
> **The processes, by library path.** `Control > Generators > LFO`; `Control > Mappings > Range Filter`, `Smooth`, and `Multi-choice`; and, for observation, `Monitoring > Signal display` beside the plain value display. `Smooth` offers `OneEuro`, `LowPass`, `Average`, and `Median` as its `Type`, which is where the character of the smoothed branch is actually chosen.

1. **Set up the input** and confirm that values arrive in the device explorer.
2. **Make the pipeline interval** and give its end a trigger that is never satisfied, so that the interval runs for as long as the score plays.
3. **Calibrate by moving the input through its full range**, and record what the calibrator learned in your written map.
4. **Condition once, centrally**, with a range filter and, if the input is noisy at the source, one modest smooth, so that every downstream stage consumes this conditioned value.
5. **Build the immediate branch** as a mapping curve, steep in the middle, running straight to the destination with no smoothing at all, because any filtering here erases the contrast with the other two branches.
6. **Build the smoothed branch** from the same conditioned value, through a gentler curve and a generous smooth placed immediately before the output, and tune it until it feels calm without feeling late.
7. **Build the stepped branch** by quantising the conditioned value into a small number of levels and driving the third destination from those, since four or five levels is plenty to feel the difference.
8. **Observe each branch** with a signal display on each output, then play, move the input, and watch three shapes that come from one movement.
9. **Rate-limit every destination that crosses a network** and confirm in the message log that the traffic dropped.
10. **Write the map** and **save the fragment** with `Alt+Drag` into the user library, named for what it is.

## How to know it is finished

- Moving the input produces three visibly different behaviours, and you can describe each in one sentence without referring to numbers.
- The bench responds at any point while the score plays, and not only during one interval.
- Every stage has an observation you can look at, and you can name which stage you would check first if the third branch stopped moving.
- Re-calibrating after moving the sensor takes under a minute and needs no edits elsewhere.
- The written map lets someone else rebuild the bench, and the fragment lets you rebuild it in one drag.

## What a bench is worth

An hour spent on something that is not a piece is justified because a bench separates the instrument from the composition. When a piece behaves badly, the question is always whether the input, the mapping, or the structure is at fault, and with a bench you trust, that question collapses, because the bench is known good and the fault must lie in what you built on top of it. In contrast, without one, every debugging session re-examines the whole chain from sensor to output.

Furthermore, the bench is where the judgement about how an input should feel gets practised, because deciding how much smoothing, how steep a curve, and where the dead zone sits improves with repeated practice and does not improve at all when it is buried inside a project deadline.

Additionally, interactive work is usually demonstrated before it is finished, to a curator, a collaborator, or a funder, and a bench that reliably shows one gesture producing three behaviours is a five-minute demonstration of the idea of your piece, available before the piece exists.

The timing matters as well, because the bench is what makes Module F testable. Each structure in that module needs an input you can move on purpose and repeatably, and without the bench you will be debugging the interaction logic and the input at the same time, which doubles the work and halves the certainty of any conclusion.

## Common mistakes

- **Building three parallel pipelines instead of one conditioned value with three branches** means that they drift apart and that re-calibrating has to be done three times.
- **Smoothing the immediate branch "a little"** turns it into a second smoothed branch, so the comparison the bench exists for is gone.
- **Testing on a clean input** tells you how the pipeline behaves on data it will not meet, whereas the defects are what the bench exists for.
- **Leaving out the observations** saves two minutes now and costs far more the first time a branch goes quiet.
- **Forgetting the trigger that keeps the pipeline alive** lets the bench stop responding after a few seconds, so that it appears broken; a pipeline that outlives its interval needs the trigger that is never satisfied, from Lesson 11, so that the bench responds whenever the score is playing.
- **Leaving the map in your head** works until the sensor moves or three months pass, and by then the reasons behind each range are gone.

## Exercise

Extend the bench in one direction only, since doing both at once hides which one failed.

Either **make it a two-input instrument** by adding a second input and making one destination depend on both, for instance a position where one input is distance and the other is angle, and note what you had to decide that a single input did not ask of you.

Or **make it fail gracefully** by defining what each destination should do when the input stops arriving entirely, and then implementing it. An installation whose sensor is unplugged should not hold its last value forever, and deciding what it does instead is a design question that [Lesson 34]({{ site.baseurl }}/learn/34-rehearsal-to-show.html) returns to.

**Success criterion:** the bench passes the five-point finish list plus your extension, and it exists as a named fragment in your user library. You will use it in [Milestone P4]({{ site.baseurl }}/learn/p4-interactive-installation.html), where its output starts firing triggers instead of moving values.

## Going further

- [Data processing]({{ site.docs_baseurl }}/common-practices/12-data-processing.html), which this milestone implements end to end.
- [The joystick device]({{ site.docs_baseurl }}/devices/joystick-device.html), the cheapest real input.
- [Signal display]({{ site.docs_baseurl }}/processes/signal-display.html), the observation process used throughout.
- [Presets]({{ site.docs_baseurl }}/presets.html) for saving the bench as a fragment.
