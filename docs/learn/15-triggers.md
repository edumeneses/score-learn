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

> **Before this lesson** finish [Milestone P3]({{ site.baseurl }}/learn/p3-mapping-bench.html); its conditioned input is what you will fire triggers from.
>
> **You will need** `lesson-15.score` and one input you can control.
>
> **You will build** a score that waits, and that you can release by hand and by a value from a device.

## Why this matters

This is the lesson the software exists for. Everything up to now could have been done, with more or less friction, in other tools. A timeline whose instants can *wait*, and whose durations are therefore ranges rather than numbers, is what *score* offers that a workstation does not.

It is also, according to the usability study, the concept newcomers most often report as unfamiliar, in their own words. That unfamiliarity is not a failure of intelligence; it is that no other tool in most people's history has this. So this lesson goes slowly, and it insists you watch what waiting *looks like*, because the visual signature is what makes an interactive score readable.

## Concepts

**A trigger is a property of an instant.** Not an object of its own: it is a flag on a time synchronisation point, which is why Lesson 02 found it in the file as `Active` on a `TimeSyncModel`. Select a state and press `T`, or use the inspector, and the instant now waits.

**Waiting has a visual signature.** Two things change. A T-shaped marker appears above the state. The preceding interval's duration is drawn as a **dashed line**, because that duration is no longer determined: the interval will run until the trigger fires. Learning to read the dash is how you tell an interactive score from a linear one at a glance.

**The trigger expression decides what fires it.** By default a trigger is set never to be true on its own, which means it waits for you: a click on the marker, or an external command. Give it an expression over a device parameter and it fires when that expression becomes true. The default operator for a value arriving is a *pulse*: any value at that address satisfies it, which is what you want for a button.

**Minimum, nominal, and maximum duration.** An interval's nominal duration is what it is drawn as. Its minimum is the earliest a trigger may release it, and its maximum is the point at which it gives up waiting and proceeds anyway. These three numbers are the whole vocabulary of flexible time: a minimum protects against a double tap, a maximum guarantees the show goes on.

**Start on play, and re-triggering.** Two options in the trigger inspector. **Start on play** makes a trigger available from the moment the score starts, which is what lets a part of the score sit outside the main flow and still be fireable. The re-trigger option decides what a second firing does: restart the following material from the beginning, or, if unchecked, stop it and require another event to begin again.

## Walkthrough: build a score that waits

![An interval whose duration is drawn dashed, ending at an instant carrying a trigger marker]({{ site.img }}/15/15-01-trigger.png)

1. **Open `lesson-15.score`.** One interval with an automation, ending at an instant that waits, followed by a second interval. Note the dashed duration before the trigger.
2. **Play it.** The first automation runs. The playhead reaches the trigger and stops there. The progress bar on the first interval stops advancing. Nothing is broken: this is waiting, and this is what it looks like.
3. **Release it by hand.** Click the T marker. The second interval begins. Stop, and do it again, releasing at a different moment: the piece is the same, its timing is not.
4. **Now build your own.** In a new document, make two chained intervals with an automation in each. Select the state between them and press `T`.
5. **Set a minimum duration** on the first interval, in the inspector, of two seconds. Play, and try to release the trigger immediately: it will not fire before the minimum. This is the protection against accidental double firing.
6. **Set a maximum duration** of eight seconds. Play and wait without touching anything: at eight seconds the score proceeds by itself. You have just written a passage that is interactive *and* guaranteed to end, which is the combination a show needs.
7. **Fire it from a device.** Drag a parameter from the device explorer onto the trigger marker, or onto the address field in the trigger inspector. Now a value at that address releases the trigger. Use a button on a controller, or the third branch of your P3 bench.
8. **Watch the automation's behaviour while waiting.** The preceding automation's duration is now elastic. Decide whether that is what you want: it may be right, or it may be that the automation should finish and then wait, which means putting the wait in its own short interval afterwards.
9. **Try start on play** on a trigger belonging to material not connected to the start of the score, and note that it becomes fireable as soon as the score runs. This is the mechanism [Lesson 17]({{ site.baseurl }}/learn/17-loops-and-out-of-time.html) builds on.

## What happens to a stretched automation

The subtle part of this lesson, and the thing to test rather than assume.

When an interval's end waits, the interval becomes elastic, and the processes inside it are stretched to fit however long the wait lasts. For an automation that means a fade which takes as long as the performer takes. Sometimes that is exactly the intention: a light that reaches full brightness precisely when the performer arrives at their mark. Often it is not: a two-second fade should be two seconds regardless of when the next cue comes.

The idiom for the second case is to separate the two concerns. Put the fade in a rigid interval of its own, then chain a second interval whose only job is to wait. The fade is then always two seconds and the waiting absorbs the variability. Deciding, per passage, which of the two you want is most of the craft of writing flexible time.

## Three shapes of interactive passage

Nearly every interactive passage you will write is one of three shapes, and naming them makes the structural choice quick.

**Wait, then run.** The instant waits; when it fires, a rigid section plays out at its written duration. Use it when the material has a shape that must be preserved: a phrase, a fade, a sequence. This is the shape that needs the wait in its own interval, so the material stays rigid.

**Run, then wait.** Material plays and then the score holds at the following instant until released. Use it for a section that must be complete before the next cue can be taken.

**Run while waiting.** The material is inside the elastic interval, so it stretches to fill however long the wait lasts. Use it when the material's job is to fill time: a drone, a loop, an idle animation. Note that a fade used this way becomes slower the longer the wait, which is either expressive or a bug depending on what you meant.

Deciding which of the three you are writing, before you place the trigger, is what keeps flexible time from producing surprises.

## Common mistakes

- **Reading a wait as a hang.** The progress bar stopping at the trigger, with the playhead not advancing, is the signature. Learn it now and you will never restart the application unnecessarily.
- **No maximum duration in a show.** An interactive cue with no upper bound depends on someone being there. A maximum is your insurance.
- **No minimum duration on a hand-fired trigger.** Double taps happen, especially under pressure.
- **Stretching an automation without meaning to.** Test whether you want the elasticity in the fade or in a separate waiting interval.
- **Expecting a trigger to fire from a value it never receives.** Confirm the address is arriving in the device explorer first; this is Lesson 07's diagnosis applied to triggers.
- **Forgetting that a trigger defaults to never firing by itself.** That is deliberate: it waits for you until you tell it what to wait for.

## Exercise

Write a forty-second passage with three sections and two triggers, in which: the first trigger is fired by a value from your bench and has a two-second minimum; the second is fired by hand and has a twelve-second maximum so the passage always ends; and one of the three automations must keep its exact duration regardless of when its trigger fires.

**Success criterion:** the passage can be performed with different timings twice in a row, always terminates without intervention, and you can point to the interval you made rigid and say why. If your fade stretched when you did not want it to, restructure rather than adjusting the curve.

## Going further

- [Breaking the timeline]({{ site.docs_baseurl }}/quick-start/breaking-the-timeline.html), the reference introduction to triggers.
- [The scenario reference]({{ site.docs_baseurl }}/processes/scenario.html) for triggers, durations, and their inspector options.
- [Out-of-time triggering]({{ site.docs_baseurl }}/common-practices/3-out-of-time.html), which [Lesson 17]({{ site.baseurl }}/learn/17-loops-and-out-of-time.html) covers.
- [Switches]({{ site.docs_baseurl }}/common-practices/2-switches.html) for trigger expressions used as toggles.
