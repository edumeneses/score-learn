---
layout: default
title: "Lesson 12: Recording live input into automations"
description: "Turn a performed gesture into an automation, clean it up, and know when a recording should stay a recording."
parent: Lessons
nav_order: 14
unit: "12"
permalink: /learn/12-recording-live-input.html
score_version: "3.8.2"
reading_time: "12 min"
practice_time: "15 min"
score_file: none
---

# Lesson 12: Recording live input into automations

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 11]({{ site.baseurl }}/learn/11-modulation-sources.html), because the exercises here assume the editing skills of the preceding lessons.
>
> **You will need** a device that sends values to *score*, which can be a MIDI (Musical Instrument Digital Interface) controller, a joystick, a sensor, or a script that emits OSC (Open Sound Control); the exercise uses the phone of Lesson 07, or its `fader.py` script.
>
> **You will build** an automation recorded from a performed gesture and cleaned to a curve you can edit, together with a recorded data file you can reuse.

## Why this matters

Some movements are easier to perform than to describe. The irregularity of a hand on a fader, the acceleration of a gesture, and the timing of a phrase felt without counting can all be approximated by drawing, although the approximation usually sounds like one. Recording closes that gap, because you perform the movement once and the software writes the curve, so that the irregularities which made the gesture convincing survive as breakpoints you can edit.

Furthermore, recording has a second use, which is less obvious and which the section on reading a recorded curve develops: it measures an input. When a sensor behaves oddly, recording its output into a curve you can look at tends to be faster than reasoning about the fault, because the shape of the noise tells you what kind of noise it is, and therefore which process will remove it.

## Concepts

### Recorded automations

Recording writes ordinary automations. The result is not a special object; it is an automation with breakpoints, which you edit in the same way as a drawn one, and that equivalence is what makes the technique a starting point for composition instead of a dead end.

### Recording density

A recording is dense by nature. A performed gesture arrives as hundreds of values, and the resulting curve carries a breakpoint for a great many of them, which makes it faithful. However, the same density makes it unwieldy, since it is hard to edit and, at the extreme, expensive to execute, so reducing it is a normal stage of the workflow, and the walkthrough below treats it as one.

### Recording and logging

Recording and logging answer different questions. An automation is for reuse inside the score, whereas the numbers themselves, for analysis or for another tool, come from the **CSV recorder** (comma-separated values), which writes values to a file instead of into the timeline. Deciding which of the two you need before you start avoids recording a curve when you wanted a table, or the reverse.

## Walkthrough: perform, record, clean

![The scenario's context menu with the Record submenu open, offering to record automations or messages]({{ site.img }}/12/12-01-record-menu.png)

1. **Confirm that input is arriving before you record.** Look in the device explorer for the values you expect to move, because recording an address that does not receive produces an empty automation.
2. **Select the addresses to record** in the device explorer, where one address is enough for a first attempt although the mechanism handles several at once.

   {: .warning }
   > **Selection decides what is recorded.** As with the snapshots of Lesson 09, the addresses selected in the device explorer are the addresses that get recorded, so the stale-selection trap described there applies here unchanged, and a parent node left selected records its whole subtree.

3. **Right-click in the score** at the point where the recording should begin and choose *record automations from here*, which sits in the Record submenu the figure shows.
4. **Press play, then perform the gesture** at the speed you want it in the piece.

   {: .warning }
   > **Recording starts when the first message arrives.** By default *score* waits for a value before it begins writing, so that an idle controller does not produce a leading flat line. However, this behaviour is a preference and can be changed, which means you should know which setting yours uses before you record a gesture that you cannot perform twice.

5. **Stop and inspect the result**, which is one automation per recorded address, sitting in a new interval, with a breakpoint for nearly every value that was received.
6. **Attach it, play it back, and compare it with what you performed**, since the new interval stays out of time until its start is synchronised with an instant on the timeline, as the exercise shows. The gesture should then reproduce, and this is the moment at which recording either convinces you or reveals that your input was noisier than you thought.
7. **Reduce it by deleting breakpoints that carry no information**, since a long straight run needs two points where the recording placed sixty; what remains should look like your gesture in ten to twenty points instead of several hundred.
8. **Shape what remains** with the tools of Lesson 10, because the reduced curve is now editable: bend a segment, move a breakpoint, or tighten the timing, and the recording becomes a composed object.
9. **Record the same gesture three times and keep the best**, because recording is cheap and the third attempt is usually the one with the right timing.
10. **Try the CSV recorder** on the same input and open the file, which holds the same data for a different purpose; this is what you send to a collaborator who needs the numbers without the score around them.

## When a recording should stay live

Recording captures a gesture *as performed once*, which is the wrong tool in three situations where the score should read the input live instead.

**When the performer is present, the score should respond to them.** If someone will be moving the fader at the show, a recording of them substitutes for the person, whereas mapping, the subject of [Lesson 13]({{ site.baseurl }}/learn/13-mapping-and-scaling.html), lets the score follow the hand that is there.

**When the input is the interaction, a recording defeats the purpose.** An installation that responds to a visitor cannot use a recording of a previous visitor, because the visitor in front of it would then have no effect on the piece.

**When the shape matters more than the timing, record for material.** If the curve of the gesture is what you liked, while its moment in time is incidental, record it once, extract the shape, and reuse that shape as a drawn automation wherever you need it, so that recording becomes a source of material instead of the material itself.

In other words, recording serves authoring, whereas mapping serves response; a piece usually needs both, and a project that confuses the two ends up either rigid, with a recorded gesture that cannot follow the room, or unrehearsable, with a live response that has no fixed timing to practise against.

## What a recorded curve tells you about your input

The measuring use of recording, introduced at the start of this lesson, rests on reading the shape of a curve, and each common shape corresponds to a different fault in the input and therefore to a different remedy.

**A staircase means quantisation.** The input arrives in discrete steps, either because the sensor has low resolution or because something upstream is rounding, and smoothing will hide the steps without adding resolution that the sensor did not have.

**A dense fuzz around a clean shape is jitter**, which is the normal condition of physical sensors and the condition that smoothing exists for. Moreover, the recording tells you how much smoothing you need, because the fuzz shows the noise before any filtering has touched it.

**Flat sections with sudden jumps mean rate limiting or dropped messages.** Check the sender before adding filtering here, because a dropped message is not noise, and treating it as noise produces a laggy response to a fast gesture.

**A drift over minutes means the sensor's baseline moves**, with temperature, with light, or with the room filling up. In contrast to jitter, no amount of filtering corrects it, which is the reason a calibrator, or a periodic re-zero, belongs in the design of an installation instead of in its repair.

**Values pinned at a bound mean the input saturates**, so that the interesting part of the gesture lies outside what the sensor can report; the fault is one of placement or range, which no mapping can correct.

Recording each of these once, with an input you have provoked into the fault, teaches more about sensors than a description can, and the conditioning pipeline of Lesson 13 assumes that you can tell them apart.

## Common mistakes

- **Not knowing your start-on-first-message setting**, so that recording begins at play and your curve gains a flat lead-in that shifts every breakpoint later.
- **Keeping the raw density**, although hundreds of breakpoints are unreadable and unmaintainable; reduce as a matter of course.
- **Recording a noisy sensor and then fighting the curve**, when filtering the input first with a smoothing or rate-limiting process, and recording the filtered value, cleans at the source, which is cheaper than cleaning the result.
- **A stale explorer selection**, so that the recording captures a parent node's whole subtree instead of the address you meant.
- **Treating a recording as unalterable**, when it is an ordinary automation and accepts every edit from Lesson 10.

## Exercise

Record a fader gesture and let a third excerpt replay it, because hearing your own hand come back while you touch nothing is the quickest way to judge whether a recording was worth keeping.

1. **Drag a third excerpt** onto the timeline after the second, as in [Lesson 11]({{ site.baseurl }}/learn/11-modulation-sources.html).
2. **Give its gain an address** by clicking the dot at the bottom left of its waveform, then `Gain`, and typing `phone:/fader` into the `Address` field of the inspector, which is the fader of [Lesson 07]({{ site.baseurl }}/learn/07-osc-devices.html). Play and move the fader, and the volume follows your hand.

   {: .warning }
   > **The excerpt starts at whatever level the fader was left at**, silent if it sits at zero, because the gain reads the parameter's current value from the start of playback.

3. **Select `phone:/fader` in the device explorer**, right-click the empty timeline below the excerpts, and choose `Record > Record automations from here`.
4. **Press play and perform** a gesture of about ten seconds on the phone, then stop, and a new interval appears holding an automation of `phone:/fader` with a breakpoint for nearly every value received.
5. **Attach the recording to the excerpt** by clicking the circle at the left end of the recording, holding `Ctrl` while clicking the circle at the left end of the third excerpt, and pressing `Shift+M`, which synchronises the two instants so that they happen together.

   {: .warning }
   > **A recording starts unattached.** No interval links its start to the rest of the timeline, which leaves it out of time, so it does not play until you synchronise it with an instant that does; [Lesson 17]({{ site.baseurl }}/learn/17-loops-and-out-of-time.html) covers material of that kind.

6. **Play with your hands off the phone**, and the excerpt repeats your gesture, because the recorded automation writes the same address that the gain reads.

With no phone, run `fader.py` from Lesson 07 during step 4, whose five-second ramp records and replays in the same way.

**You are done when** the third excerpt rises and falls as you moved the fader, while nobody touches it.

## Going further

- [Recording]({{ site.docs_baseurl }}/in-depth/recording.html), the reference procedure, and the [preferences]({{ site.docs_baseurl }}/reference/preferences.html) that control it.
- [The CSV recorder]({{ site.docs_baseurl }}/processes/csv-recorder.html) for logging values to a file that another tool can read.
- [Smooth]({{ site.docs_baseurl }}/processes/smooth.html) and [rate limiter]({{ site.docs_baseurl }}/processes/rate-limiter.html), the two processes to reach for when an input is noisy.
- [Data processing]({{ site.docs_baseurl }}/common-practices/12-data-processing.html), the reference recipe which [Lesson 13]({{ site.baseurl }}/learn/13-mapping-and-scaling.html) takes up and extends.

{% include lesson_files.html %}
