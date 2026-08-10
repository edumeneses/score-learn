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
score_file: none
---

# Milestone P3: a sensor to sound and light mapping bench

{% include lesson_meta.html %}

> **Before this milestone** finish Lessons 10 to 14. This unit introduces nothing new.
>
> **You will need** one input, emulated if you have no hardware, and about an hour.
>
> **You will build** a reusable bench: one gesture driving three destinations through a documented, calibrated, tunable pipeline.

## Why this matters

Everything in Module F depends on having an input you trust. Triggers fired by a value, conditions evaluated against a value, branches chosen by a value: all of them assume you know what your input does and that it does it reliably. Most interactive pieces that behave unpredictably do so not because the interaction logic is wrong but because the input feeding it was never conditioned.

A bench is also a habit worth acquiring. Instead of building the mapping again inside each new piece, you build it once, save it as a fragment, and start from a known-good instrument. The best practitioners in this field almost all have some version of this file.

## The brief

Build a document that:

1. takes **one input**, and works with an emulated one, so that it runs on any machine;
2. **calibrates** that input and records the learned range in writing;
3. drives **three destinations** with clearly different characters: one immediate, one smoothed, one stepped or quantised;
4. keeps the pipeline **running for the whole score**, not only inside one interval;
5. **observes** every stage, so that a wrong value can be located rather than guessed at;
6. ships with a **written map**: input, each stage in order, each output with its range;
7. is saved to the **user library** as a reusable fragment.

## Emulating an input

If you have no sensor, you have three good options, and the first is the one to use.

**A second application sending OSC.** Six lines in any language, or a small Pure Data or Max patch with a slider. Gives you full control over range, rate, and noise, which is better for a bench than a real sensor because you can *choose* how badly it behaves.

**A joystick or gamepad.** *score* has a joystick device, and any cheap controller gives you real axes with real jitter.

**A generator inside *score*.** An LFO plus a noise source, fed into your pipeline as though it were external. Least realistic, since it never drops out or saturates, but it needs nothing installed.

Whichever you choose, deliberately give the input two defects to work against: a range that is not 0 to 1, and visible jitter. A bench tested on a clean input teaches nothing.

## Concepts you are assembling

**The four-stage pipeline** from Lesson 13: condition, relate, send, observe.

**Three characters from one gesture.** The exercise is not three copies of a mapping; it is three *intentions*. Immediate means minimal smoothing and a curve that responds at once. Smoothed means generous filtering and a curve that ignores small movements. Stepped means the continuous input becomes discrete, which is what a step or quantising object is for, and which feels categorically different to whoever is moving the sensor.

**A pipeline that outlives its interval**, using the never-satisfied trigger from Lesson 11, so the bench responds whenever the score is playing.

**Observation at every stage**, using signal displays, so that "the light is not moving" becomes a question with a location.

## Walkthrough

{: .note }
> A figure for this lesson is pending: the bench is assembled in the nodal view, which requires interaction. See `checks/p3-mapping-bench.md`.

1. **Set up the input** and confirm values arrive in the device explorer.
2. **Make the pipeline interval** and give its end a trigger that is never satisfied, so it runs indefinitely.
3. **Calibrate.** Move the input through its full range and record what the calibrator learned, in your written map.
4. **Condition once, centrally.** Range filter and, if the input is noisy at the source, one modest smooth. Everything downstream consumes this conditioned value, which is what keeps the three branches comparable.
5. **Branch one: immediate.** A mapping curve, steep in the middle, straight to the destination. No smoothing.
6. **Branch two: smoothed.** The same conditioned value, a gentler curve, and a generous smooth just before the output. Tune it until it feels calm and not late.
7. **Branch three: stepped.** Quantise the conditioned value into a small number of levels and drive the third destination from those. Four or five levels is plenty to feel the difference.
8. **Observe each branch.** A signal display on each output. Play, move the input, and watch three shapes that come from one movement.
9. **Rate-limit anything on a network** and confirm in the message log that traffic dropped.
10. **Write the map** and **save the fragment** with `Alt+Drag` into the user library, named for what it is.

## How to know it is finished

- Moving the input produces three visibly different behaviours, and you can describe each in one sentence without referring to numbers.
- The bench responds at any point while the score plays, not only during one interval.
- Every stage has an observation you can look at, and you can name which stage you would check first if the third branch stopped moving.
- Re-calibrating after moving the sensor takes under a minute and needs no edits elsewhere.
- The written map lets someone else rebuild the bench, and the fragment lets you rebuild it in one drag.

## What a bench is worth

Two arguments for spending an hour on something that is not a piece.

**It separates instrument from composition.** When a piece behaves badly, the question is always whether the input, the mapping, or the structure is at fault. With a bench you trust, that question collapses: the bench is known good, so the fault is in what you built on top. Without one, every debugging session re-examines everything.

**It is where you develop taste.** Deciding how an input should feel, how much smoothing, how steep a curve, where the dead zone is, is a judgement that improves with deliberate practice and does not improve at all when it is buried inside a project deadline. A bench is the practice room for that judgement.

There is a third, practical reason. Interactive work is usually demonstrated before it is finished, to a curator, a collaborator, a funder. A bench that reliably shows one gesture producing three different behaviours is a five-minute demonstration of the idea of your piece, available at any stage, including before the piece exists.

One more reason to build it now rather than later: the bench is what makes Module F testable. A trigger fired by a value, a condition evaluated against a value, a branch chosen by a value, all need an input you can move deliberately and repeatably. Without the bench you will be debugging the interaction logic and the input at the same time, which is twice the work and half the certainty.

## Common mistakes

- **Three parallel pipelines instead of one conditioned value with three branches.** They drift apart, and re-calibrating means doing it three times.
- **Smoothing the immediate branch "a little".** Then it is not the immediate branch, and the comparison the bench exists for is gone.
- **Testing on a clean input.** The defects are the point.
- **No observation.** The first time a branch goes quiet you will wish you had spent the two minutes.
- **Forgetting the never-satisfied trigger**, so the bench stops responding after a few seconds and appears broken.
- **Leaving the map in your head.** In three months it will not be there.

## Exercise

Extend the bench in one direction, and one only.

Either **make it a two-input instrument**: add a second input and make one destination depend on both, for instance a position where one input is distance and the other is angle. Note what you had to decide that a single input never asked of you.

Or **make it fail gracefully**: define what each destination should do when the input stops arriving entirely, and implement it. An installation whose sensor is unplugged should not hold its last value forever, and deciding what it does instead is a real design question that [Lesson 34]({{ site.baseurl }}/learn/34-rehearsal-to-show.html) returns to.

**Success criterion:** the bench passes the five-point finish list plus your extension, and exists as a named fragment in your user library. You will use it in [Milestone P4]({{ site.baseurl }}/learn/p4-interactive-installation.html), where its output starts firing triggers instead of moving values.

## Going further

- [Data processing]({{ site.docs_baseurl }}/common-practices/12-data-processing.html), which this milestone implements end to end.
- [The joystick device]({{ site.docs_baseurl }}/devices/joystick-device.html), the cheapest real input.
- [Signal display]({{ site.docs_baseurl }}/processes/signal-display.html), the observation process used throughout.
- [Presets]({{ site.docs_baseurl }}/presets.html) for saving the bench as a fragment.
