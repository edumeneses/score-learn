---
layout: default
title: "Lesson 12: Recording live input"
description: "Turn a performed gesture into an automation, clean it up, and know when a recording should stay a recording."
parent: Lessons
nav_order: 14
unit: "12"
permalink: /learn/12-recording-live-input.html
score_version: "3.8.2"
reading_time: "12 min"
practice_time: "20 min"
score_file: none
---

# Lesson 12: Recording live input

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 11]({{ site.baseurl }}/learn/11-modulation-sources.html).
>
> **You will need** a device that sends values to *score*: a MIDI controller, a joystick, a sensor, or a script that emits OSC.
>
> **You will build** an automation recorded from a performed gesture, cleaned to something you can edit, plus a recorded data file you can reuse.

## Why this matters

Some movements are easier to perform than to describe. The slight irregularity of a hand on a fader, the acceleration of a real gesture, the timing of a phrase that a performer feels rather than counts: you can approximate these by drawing, and the approximation usually sounds like an approximation. Recording collapses that gap. You perform the movement once and the software writes the curve.

There is a second, less obvious use. Recording is a measurement tool. When a sensor is behaving oddly, recording its output into a curve you can look at is often faster than reasoning about it, because the shape of the noise tells you what kind of noise it is.

## Concepts

**Recording writes automations.** The result is not a special object: it is an ordinary automation, with breakpoints, that you can edit exactly like a drawn one. That is what makes the technique practical rather than a dead end.

**Selection decides what is recorded.** As with the snapshots of Lesson 09, the addresses selected in the device explorer are the addresses that get recorded. The stale-selection trap is the same one.

**Recording starts on the first message, not on play.** By default *score* waits for a value to arrive before it starts writing, so that an idle controller does not produce a leading flat line. This is a preference and can be changed; know which behaviour yours is set to before you record something you cannot perform twice.

**A recording is dense.** A performed gesture arrives as hundreds of values, and the resulting curve has a breakpoint for a great many of them. This is faithful and unwieldy: it is hard to edit and, at the extreme, expensive to execute. Reducing it is a normal part of the workflow, not a repair.

**Recording against logging.** An automation is for reuse inside the score. When you want the numbers themselves, for analysis or for another tool, the **CSV recorder** writes values to a file instead. The two answer different questions and it is worth being clear which one you are asking.

## Walkthrough: perform, record, clean

{: .note }
> A figure for this lesson is pending: it needs the right-click menu that starts a recording, plus a before-and-after of a dense curve, which requires interaction. See `checks/12-recording-live-input.md`.

1. **Get input arriving first.** Before recording anything, confirm in the device explorer that the values you expect are moving. Recording an address that never receives produces an empty automation and a confusing five minutes.
2. **Select the addresses to record** in the device explorer. One is enough for a first attempt; the mechanism handles several at once.
3. **Right-click in the score** where the recording should begin and choose *record automations from here*.
4. **Press play, then perform.** Writing begins when the first value arrives. Perform the gesture you want, at the speed you want it in the piece.
5. **Stop, and look at what you got.** One automation per recorded address, sitting in a new interval, with a breakpoint for essentially every value received.
6. **Play it back.** The gesture should reproduce. This is the moment where recording either convinces you or reveals that your input was noisier than you thought.
7. **Reduce it.** Delete breakpoints that carry no information: long straight runs need two points, not sixty. What remains should look like your gesture in ten to twenty points rather than several hundred.
8. **Shape what remains.** Now that it is editable, the curve is subject to everything from Lesson 10: bend a segment, move a breakpoint, tighten the timing. This is where a recording becomes a composed object.
9. **Record the same gesture three times** and keep the best. Recording is cheap; the third attempt is usually the one with the right timing.
10. **Try the CSV recorder** on the same input, and open the file. Same data, different purpose: this is what you send to a collaborator who needs numbers rather than a score.

## When a recording should stay live

Recording captures a gesture *as performed once*. Three situations where that is exactly wrong, and the score should read the input live instead.

**When the performer is present.** If someone will be moving the fader at the show, the score should respond to them, not to a recording of them. That is mapping, [Lesson 13]({{ site.baseurl }}/learn/13-mapping-and-scaling.html).

**When the input is the interaction.** An installation that responds to a visitor cannot use a recording of a previous visitor.

**When the shape matters more than the timing.** If what you liked about the gesture is its curve rather than its moment, record it once, extract the shape, and then reuse that shape as a drawn automation. This is the most common productive use: recording as a source of material, not as the material itself.

The general rule: record to *author*, map to *respond*. A piece usually needs both, and confusing them produces either a rigid piece or an unrehearsable one.

## What a recorded curve tells you about your input

Recording is a measuring instrument, and reading the result is a skill worth practising deliberately, because the shape of a recording diagnoses the input faster than reasoning does.

**A staircase** means quantisation: the input arrives in discrete steps, either because the sensor is low resolution or because something upstream is rounding. Smoothing will hide it; it will not add resolution that was never there.

**A dense fuzz around a clean shape** is jitter, and it is the normal condition of physical sensors. It is what smoothing is for, and the recording tells you how much you need.

**Flat sections with sudden jumps** mean the input is being rate limited or is dropping messages. Check the sender before adding filtering here: a dropped message is not noise, and treating it as noise produces a laggy response to a fast gesture.

**A drift over minutes** means the sensor's baseline moves, with temperature, with light, with the room filling up. No amount of filtering fixes it, and it is the reason a calibrator, or a periodic re-zero, belongs in the design of an installation rather than in its repair.

**Values pinned at a bound** mean the input saturates, and the interesting part of the gesture is outside what the sensor can report. That is a placement or a range problem, not a mapping problem.

Recording each of these once, deliberately, is a better education in sensors than reading about them.

One practical note on file sizes. A dense recording is not only awkward to edit, it also makes the document larger, since every breakpoint is stored as text in the `.score` file. A few long recordings left unreduced can turn a small document into a slow one to open. Reducing is therefore hygiene as much as craft.

## Common mistakes

- **Recording before checking that values arrive.** The failure is silent and looks like a broken feature.
- **Not knowing your start-on-first-message setting.** If recording begins at play instead, your curve has a flat lead-in that shifts everything.
- **Keeping the raw density.** Hundreds of breakpoints are unreadable and unmaintainable. Reduce as a matter of course.
- **Recording a noisy sensor and then fighting the curve.** Filter the input first, with a smoothing or rate-limiting process, and record the filtered value. Cleaning at the source beats cleaning the result.
- **A stale explorer selection**, so the recording captures a parent node's whole subtree.
- **Treating a recording as unalterable.** It is an ordinary automation.

## Exercise

Record the same twelve-second gesture three ways: raw, filtered through a smoothing process before recording, and raw then reduced by hand to fewer than twenty breakpoints. Play all three against each other on the same parameter.

**Success criterion:** you can say which of the three you would put in a piece, and you can state the breakpoint count of each. If the filtered version lost something you wanted, note what: that is the argument for cleaning afterwards rather than at the source, and both positions are defensible.

## Going further

- [Recording]({{ site.docs_baseurl }}/in-depth/recording.html), the reference procedure, and the [preferences]({{ site.docs_baseurl }}/reference-manual/references/preferences.html) that control it.
- [The CSV recorder]({{ site.docs_baseurl }}/processes/csv-recorder.html) for logging values to a file.
- [Smooth]({{ site.docs_baseurl }}/processes/smooth.html) and [rate limiter]({{ site.docs_baseurl }}/processes/rate-limiter.html), the two processes to reach for when an input is noisy.
- [Data processing]({{ site.docs_baseurl }}/common-practices/12-data-processing.html), which [Lesson 13]({{ site.baseurl }}/learn/13-mapping-and-scaling.html) takes up.
