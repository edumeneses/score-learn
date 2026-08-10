---
layout: default
title: "Milestone P4: an interactive installation with two branches"
description: "A visitor-triggered work with an idle state, two outcomes, a guaranteed return to idle, and a document that survives eight hours unattended."
parent: Lessons
nav_order: 22
unit: "P4"
permalink: /learn/p4-interactive-installation.html
score_version: "3.8.2"
reading_time: "15 min"
practice_time: "60 min"
score_file: none
---

# Milestone P4: an interactive installation with two branches

{% include lesson_meta.html %}

> **Before this milestone** finish Lessons 15 to 18. This unit introduces nothing new, and it is the end of Phase 1.
>
> **You will need** your P3 bench as the input, and an hour.
>
> **You will build** an installation: idle, triggered, one of two outcomes, back to idle, indefinitely, safely.

## Why this matters

This is the milestone that proves Phase 1. An installation is the hardest easy thing in this field: nothing in it is technically advanced, and it must run for hours with nobody watching, recover from every state it can reach, and never require someone to restart it. Every technique in Module F exists for this shape of work.

It is also the point where the course's insistence on defined states pays. A cue that is wrong for one second in a performance is a mistake; a cue that is wrong in an installation is wrong for eight hours.

## The brief

Build a document that:

1. sits in an **idle state**, visibly and audibly defined, until something happens;
2. is **triggered by a visitor**, through your P3 bench's conditioned input;
3. chooses between **two outcomes** by condition, covering the whole input range with no gap and no overlap;
4. **returns to idle** afterwards, automatically, whatever happened;
5. **repeats indefinitely**, with no drift and no accumulation;
6. **cannot be left in a broken state**: stop sends everything to a safe condition, and start puts the world into the idle look;
7. is documented well enough that a gallery invigilator with no technical training can turn it on and off.

## Concepts you are assembling

**The idle loop.** A short phrase that repeats, waiting. Built with a transition, per Lesson 17, or with a single interval whose end waits for the visitor trigger.

**One trigger, two conditions.** The visitor's arrival releases a trigger; the branch taken is decided by a condition on the same or another value. Note that these are two separate mechanisms doing two separate jobs, which Lesson 16 insisted on.

**The return path.** Both outcomes must lead back to the idle instant. This is a transition from each branch's end, or a shared instant that both branches reach and which transitions back.

**A maximum duration as insurance.** If the visitor walks away mid-interaction, the piece must recover on its own. Every waiting instant in an installation should have a maximum duration; without one, a departure leaves the piece stuck.

**Start and stop cues** from Lesson 18, which are what make the whole thing operable by someone who has never seen it.

## Walkthrough

{: .note }
> A figure for this lesson is pending: the structure includes transitions, which need to be drawn interactively. See `checks/p4-interactive-installation.md`.

1. **Build the idle loop first**, and let it run for five minutes while you watch. If it drifts, accumulates, or gets slower, fix that now: everything else sits on top of it.
2. **Add the visitor trigger** at the end of the idle phrase, fired from your bench, with a minimum duration so a single approach does not read as several.
3. **Split the instant** after the trigger and give each branch its condition, partitioned over the input range.
4. **Write the two outcomes**, deliberately different in duration, so that the return path has to handle both.
5. **Add the return transitions** from both outcomes back to the idle instant. Play, and force each branch several times.
6. **Add maximum durations** to every waiting instant, including the idle loop's own, so that no state can be occupied forever.
7. **Add the start cue** to the first state: the idle look, fully specified.
8. **Add the stop cue** to the last state: everything off.
9. **Leave it running for an hour** while you do something else, and then interact with it. This is the only test that matters, and it is the one people skip.
10. **Write the invigilator's card**: how to start, how to stop, what "working" looks like, and who to call. One side of one page, in language with no jargon.

## The eight-hour test

Five failure modes that only appear over time, all of which have caught people, and each with its check.

**Accumulation.** Something grows each cycle: a value that ratchets, a list that lengthens. Check by watching one parameter across twenty cycles rather than two.

**Drift.** The idle loop's period changes slightly, or the visual and audio layers separate. Check by comparing the first and twentieth cycle.

**Stuck waiting.** A visitor half-triggers and leaves. Check by triggering and then withdrawing at every point in the interaction, including during the outcome.

**Death by simultaneity.** Two visitors, or one visitor moving quickly, produce input the score never expected. Check by firing the trigger repeatedly and rapidly.

**Silent resource growth.** Memory or file handles rising over hours. Check by looking at the machine's own monitoring after an hour, not by hoping.

An installation that passes these five is one you can leave. One that has not been tested against them is a piece you will be called back for.

## Designing the idle state

The idle state is the part of an installation the public sees most and the part that receives the least attention. Three decisions worth making explicitly.

**What does idle look like, exactly?** Not "nothing": a defined condition, specified as a cue, that a visitor arriving at any moment encounters. An installation whose resting state depends on which outcome ran last has no idle state, it has an aftermath.

**Does idle invite interaction?** A completely static room does not read as interactive, and visitors walk past. Slow movement in the idle loop is often the difference between a piece that is used and one that is admired from a distance. This is why the idle state is a loop rather than a single cue.

**How long is the recovery?** After an interaction, the return to idle can be immediate or gradual. Immediate is legible and slightly brutal; gradual is more elegant and risks a second visitor arriving mid-recovery and seeing something incoherent. Decide which, and then test the case of the second visitor arriving early, because it will happen constantly.

The general principle: the idle state is not the absence of the work, it is the work at rest, and it deserves the same attention as the interaction it frames.

A note on what to leave out. The temptation in a first installation is to add a third input, a fourth outcome, or a generative layer, and the result is usually a piece that is impressive for ten minutes and unmaintainable for eight hours. Two branches done reliably is a finished work; five branches half-tested is a piece you will be called back to restart. Ambition belongs in the material, not in the structure.

## Common mistakes

- **No maximum duration anywhere.** The single most common reason an installation is found frozen.
- **An idle state that is not actually defined**, so the piece looks different depending on which outcome ran last.
- **Branches with different durations and one shared return timing**, so one outcome is cut off. Test both.
- **Testing only for two minutes.** Everything works for two minutes.
- **A stop that leaves the room lit.** The stop cue exists for this.
- **Documentation written for you rather than for the invigilator.** If it contains the word "scenario", rewrite it.

## Exercise

Extend the installation in one direction, and only one.

Either **add a third outcome that is rare**: chosen by a condition that is only occasionally satisfied, so most visitors see two outcomes and a few see something else. Note what you had to do to make "rare" reliable rather than accidental.

Or **make it degrade gracefully**: define and implement what the piece does when the sensor stops reporting entirely, so that a failed input produces a defined idle rather than a frozen interaction. Then unplug the input mid-cycle and confirm.

**Success criterion:** the piece passes the eight-hour test's five checks, an untrained person can start and stop it from your card, and you can state what happens if the visitor leaves at any of the four points in the interaction. Keep this document: it is the reference shape for Phase 2's media milestones.

## Going further

- [Out-of-time triggering]({{ site.docs_baseurl }}/common-practices/3-out-of-time.html) and [looping]({{ site.docs_baseurl }}/common-practices/1-looping.html) for the structures used here.
- [Start and stop cues]({{ site.docs_baseurl }}/common-practices/7-start-stop-cues.html) for the safety behaviour.
- [Headless and embedded]({{ site.baseurl }}/learn/35-headless-and-embedded.html), later in the course, for running this on a machine with no screen.
- [Rehearsal to show]({{ site.baseurl }}/learn/34-rehearsal-to-show.html) for the documentation this milestone starts.
