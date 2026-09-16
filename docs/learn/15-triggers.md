---
layout: default
title: "Lesson 15: Interactive triggers"
description: "Make an instant wait: flexible durations, trigger expressions, remote control from a device parameter, and how waiting looks during playback."
parent: Lessons
nav_order: 18
unit: "15"
permalink: /learn/15-triggers.html
score_version: "3.8.2"
reading_time: "14 min"
practice_time: "30 min"
score_file: 15-triggers/lesson-15.score
---

# Lesson 15: Interactive triggers

{% include lesson_meta.html %}

> **Before this lesson** finish [Milestone P3]({{ site.baseurl }}/learn/p3-mapping-bench.html), because its conditioned input is what you will fire triggers from.
>
> **You will need** `lesson-15.score` and one input you can control by hand.
>
> **You will build** a score that waits, and that you can release by hand and by a value from a device.

## Why this matters

A timeline whose instants can *wait*, and whose durations are therefore ranges instead of fixed numbers, is what *score* offers that a workstation does not, since every technique up to this point could have been reproduced, with more or less friction, in other tools. This lesson introduces that capability, and the lessons on branching and loops that follow build on it.

Moreover, the usability study found that this is the concept newcomers most often report as unfamiliar, in their own words, and that unfamiliarity reflects the tools they used before, none of which offered a timeline that waits, more than any difficulty in the idea itself. Therefore this lesson goes slowly and insists that you watch what waiting *looks like*, because the visual signature is what makes an interactive score readable.

## Concepts

**A trigger is a property of an instant.** It is a flag on a time synchronisation point and not an object of its own, which is why Lesson 02 found it in the file as `Active` on a `TimeSyncModel`; select a state and press `T`, or use the inspector, and the instant now waits.

**Waiting has a visual signature made of two changes.** A T-shaped marker appears above the state, and the preceding interval's duration is drawn as a **dashed line**, because that duration is no longer determined and the interval will run until the trigger fires; learning to read the dash is how you tell an interactive score from a linear one at a glance.

**The trigger expression decides what fires it.** By default a trigger is set so that it does not become true on its own, which means it waits for you, either as a click on the marker or as an external command. However, given an expression over a device parameter, it fires when that expression becomes true; the default operator for a value arriving is a *pulse*, which any value at that address satisfies, and which is what you want for a button.

**An interval has a minimum, a nominal, and a maximum duration.** The nominal duration is what the interval is drawn as, its minimum is the earliest a trigger may release it, and its maximum is the point at which it gives up waiting and proceeds anyway. These three numbers are the whole vocabulary of flexible time, because a minimum protects against a double tap while a maximum guarantees that the show goes on.

**The trigger inspector offers two further options, start on play and re-triggering.** Start on play makes a trigger available from the moment the score starts, which is what lets a part of the score sit outside the main flow and still be fireable, whereas the re-trigger option decides what a second firing does: restart the following material from the beginning, or, if unchecked, stop it and require another event to begin again.

## Walkthrough: build a score that waits

![An interval whose duration is drawn dashed, ending at an instant carrying a trigger marker]({{ site.img }}/15/15-01-trigger.png)

1. **Open `lesson-15.score`** and read its structure, which is one interval with an automation, ending at an instant that waits, followed by a second interval; the dashed duration before the trigger is the signature from the Concepts section.
2. **Play it and watch the transport.** The first automation runs, the playhead reaches the trigger and stops there, and the progress bar on the first interval stops advancing, which is what waiting looks like when the score is behaving correctly.
3. **Release it by hand** by clicking the T marker, at which point the second interval begins; stop, and do it again while releasing at a different moment, so that you see the same piece play with a different timing.
4. **Now build your own** in a new document, with two chained intervals carrying an automation each, and select the state between them and press `T`.
5. **Set a minimum duration** of two seconds on the first interval, in the inspector, then play and try to release the trigger immediately; it will not fire before the minimum, which is the protection against accidental double firing.
6. **Set a maximum duration** of eight seconds, then play and wait without touching the score, because at eight seconds it proceeds by itself; you have written a passage that is interactive *and* guaranteed to end, which is the combination a show needs.
7. **Fire it from a device** by dragging a parameter from the device explorer onto the trigger marker, or onto the address field in the trigger inspector, so that a value at that address releases the trigger; a button on a controller works, and so does the third branch of your P3 bench.
8. **Watch the automation's behaviour while waiting**, because the preceding automation's duration is now elastic, and decide whether that is what you want; the next section gives the alternative when it is not.
9. **Try start on play** on a trigger belonging to material that is not connected to the start of the score, and note that it becomes fireable as soon as the score runs, which is the mechanism [Lesson 17]({{ site.baseurl }}/learn/17-loops-and-out-of-time.html) builds on.

## What happens to a stretched automation

The interaction between a waiting instant and the processes before it is the subtle part of this lesson, and it should be tested instead of assumed.

When an interval's end waits, the interval becomes elastic, and the processes inside it are stretched to fit however long the wait lasts, so that for an automation a fade takes as long as the performer takes. Sometimes that is the intention, as with a light that reaches full brightness at the moment the performer arrives at their mark. However, a two-second fade is often meant to be two seconds regardless of when the next cue comes, and the stretch is then a fault.

The idiom for the second case is to separate the two concerns, by putting the fade in a rigid interval of its own and then chaining a second interval whose only job is to wait. In other words, the fade is then always two seconds, and the waiting interval absorbs the variability; deciding, passage by passage, which of the two behaviours you want is most of the work of writing flexible time, and the three shapes below name the choices.

## Three shapes of interactive passage

Nearly every interactive passage you will write is one of three shapes, and naming them makes the structural choice quick.

**Wait, then run** has the instant wait and, when it fires, a rigid section plays out at its written duration. Use it when the material has a shape that must be preserved, such as a phrase, a fade, or a sequence; this is the shape that uses the separate waiting interval from the previous section.

In contrast, **run, then wait** plays the material and then holds the score at the following instant until released, which suits a section that must be complete before the next cue can be taken.

**Run while waiting** places the material inside the elastic interval, so that it stretches to fill however long the wait lasts. Use it when the material's job is to fill time, as a drone, a loop, or an idle animation does; a fade used this way becomes slower the longer the wait, which is either expressive or a bug depending on what you meant.

Deciding which of the three you are writing, before you place the trigger, is what keeps flexible time from producing surprises.

## Common mistakes

- **Reading a wait as a hang**, when the progress bar stopping at the trigger with the playhead not advancing is the signature of waiting; learn it now and you will not restart the application unnecessarily.
- **No maximum duration in a show**, although an interactive cue with no upper bound depends on someone being there, and a maximum is your insurance against their absence.
- **No minimum duration on a hand-fired trigger**, when double taps happen, especially under pressure.
- **Stretching an automation without meaning to**, which the separate waiting interval prevents; test whether you want the elasticity in the fade or in that interval.
- **Expecting a trigger to fire from a value that does not arrive**, when confirming the address in the device explorer first is Lesson 07's diagnosis applied to triggers.
- **Forgetting that a trigger does not fire by itself by default**, since it waits for you until you tell it what to wait for.

## Exercise

Write a forty-second passage with three sections and two triggers, in which the first trigger is fired by a value from your bench and has a two-second minimum, while the second is fired by hand and has a twelve-second maximum so that the passage always ends. Additionally, one of the three automations must keep its exact duration regardless of when its trigger fires.

**Success criterion:** the passage can be performed with different timings twice in a row, always terminates without intervention, and you can point to the interval you made rigid and say why. If your fade stretched when you did not want it to, restructure the passage instead of adjusting the curve, because the elasticity comes from the structure and not from the curve.

## Going further

- [Breaking the timeline]({{ site.docs_baseurl }}/quick-start/breaking-the-timeline.html), the reference introduction to triggers.
- [The scenario reference]({{ site.docs_baseurl }}/processes/scenario.html) for triggers, durations, and their inspector options.
- [Out-of-time triggering]({{ site.docs_baseurl }}/common-practices/3-out-of-time.html), which [Lesson 17]({{ site.baseurl }}/learn/17-loops-and-out-of-time.html) covers.
- [Switches]({{ site.docs_baseurl }}/common-practices/2-switches.html) for trigger expressions used as toggles.
