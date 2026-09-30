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
practice_time: "45 min"
score_file: p4-interactive-installation/p4-solution.score
---

# Milestone P4: an interactive installation with two branches

{% include lesson_meta.html %}

> **Before this milestone** finish Lessons 15 to 18, because this unit introduces no new technique, and it closes Phase 1.
>
> **You will need** your P3 bench as the input, and about forty-five minutes.
>
> **You will build** an installation that idles, is triggered, plays one of two outcomes, and returns to idle, indefinitely and safely.

## Why this matters

This milestone proves Phase 1, because an installation is the hardest easy thing in this field: no part of it is technically advanced, and yet it must run for hours with no one watching, recover from every state it can reach, and not require anyone to restart it. Every technique in Module F exists for this shape of work, and this milestone is where they are used together for the first time.

Furthermore, it is the point where the course's emphasis on defined states pays off, because a cue that is wrong for one second in a performance is a mistake, whereas a cue that is wrong in an installation is wrong for eight hours.

## The brief

Build a document that:

1. sits in an **idle state**, visibly and audibly defined, until something happens;
2. is **triggered by a visitor**, through your P3 bench's conditioned input;
3. chooses between **two outcomes** by condition, covering the whole input range with no gap and no overlap;
4. **returns to idle** afterwards, automatically, whatever happened;
5. **repeats indefinitely**, with no drift and no accumulation;
6. **cannot be left in a broken state**, because stop sends every parameter to a safe condition and start puts the world into the idle look;
7. is documented well enough that a gallery invigilator with no technical training can turn it on and off.

## Concepts you are assembling

### The idle loop

The idle loop is a short phrase that repeats while it waits. It is built with a transition, per Lesson 17, or with a single interval whose end waits for the visitor trigger.

### One trigger and two conditions

A single trigger releases the instant, and two conditions choose the branch. The visitor's arrival releases the trigger, whereas the branch taken is decided by a condition on the same or another value; these are two separate mechanisms doing two separate jobs, which is the distinction Lesson 16 drew.

### The return path

The return path leads both outcomes back to the idle instant. It is either a transition from each branch's end or a shared instant that both branches reach and which transitions back, and without it the piece plays once and stops.

### Start and stop cues

Start and stop cues from Lesson 18 make the whole piece operable by someone who has not seen it before. The start cue puts the room into the idle look, whereas the stop cue sends every parameter to a safe condition.

## Walkthrough

[![An idle phrase, a trigger labelled "a visitor arrives", two branches of different lengths leaving the same instant, and a dash-dot return transition from each branch back to the beginning]({{ site.img }}/p4/p4-01-installation-structure.png)]({{ site.scores }}/p4-interactive-installation/p4-solution.score){: download="" title="Download p4-solution.score, the document in this figure" }

The reference solution, `p4-solution.score`, makes the whole brief legible in its shape, since `Idle` runs, the instant at its end waits for the visitor, and two branches leave that instant under conditions partitioned over the input range. Both ends carry a dash-dot transition back to the score's first instant, which is what makes the return automatic and the repetition indefinite.

Moreover, the branches are **different lengths on purpose**, because a return path that only works when both outcomes take the same time is not a return path. The drawing shows the trigger and the conditions as visibly separate things: the yellow marker releases the instant, while the conditions choose what leaves it.

1. **Build the idle loop first**, and let it run for five minutes while you watch; if it drifts, accumulates, or gets slower, fix that now, since every later part of the piece sits on top of it.
2. **Add the visitor trigger** at the end of the idle phrase, fired from your bench, with a minimum duration so that a single approach does not read as several arrivals.
3. **Split the instant** after the trigger and give each branch its condition, partitioned over the input range.
4. **Write the two outcomes** with different durations, so that the return path has to handle both.
5. **Add the return transitions** from both outcomes back to the idle instant, then play and force each branch several times to confirm that both return.
6. **Add maximum durations** to every waiting instant, including the idle loop's own, so that no state can be occupied forever.
7. **Add the start cue** to the first state, so that the idle look is fully specified before the piece plays.
8. **Add the stop cue** to the last state, so that stopping the score turns every output off.
9. **Leave it running for an hour** while you do something else, and then interact with it, because this is the only test that finds the failures in the next section, and it is the one people skip.
10. **Write the invigilator's card**, which covers how to start, how to stop, what "working" looks like, and who to call, on one side of one page and in language with no jargon.

## The eight-hour test

Some failure modes only appear over time, so a test that lasts two minutes cannot find them; each of the five below comes with the check that exposes it.

**Accumulation means that a quantity grows each cycle**, such as a value that ratchets or a list that lengthens, and the check is to watch one parameter across twenty cycles instead of two.

**Drift means that the idle loop's period changes slightly**, or that the visual and audio layers separate, and the check is to compare the first and the twentieth cycle.

**Stuck waiting happens when a visitor half-triggers and leaves**, and the check is to trigger and then withdraw at every point in the interaction, including during the outcome.

**Death by simultaneity occurs when two visitors, or one visitor moving quickly, produce input the score did not expect**, and the check is to fire the trigger repeatedly and rapidly.

**Silent resource growth is memory or file handles rising over hours**, and the check is to look at the machine's own monitoring after an hour.

An installation that passes these five checks is one you can leave. In contrast, one that has not been tested against them is a piece you will be called back for.

## Designing the idle state

The idle state is the part of an installation the public sees most and the part that receives the least attention, so the decisions that define it should be made explicitly.

**What does the idle state look like at the moment a visitor arrives?** It is a defined condition, specified as a cue, because an installation whose resting state depends on which outcome ran last has no idle state but an aftermath.

**Does the idle state invite a passing visitor to interact?** A completely static room does not read as interactive, and visitors walk past it. Conversely, slow movement in the idle loop is often the difference between a piece that is used and one that is admired from a distance; that is why the idle state is a loop and not a single cue.

**How long should the recovery to idle take after an interaction ends?** The return can be immediate, which is legible and slightly brutal, or gradual, which is more elegant and risks a second visitor arriving mid-recovery and seeing something incoherent. Decide which, and test a second visitor arriving early, which happens constantly.

In other words, the idle state is the work at rest and not its absence, so it deserves the same attention as the interaction it frames.

What to leave out matters as much as what to build. However, a first installation often grows a third input, a fourth outcome, or a generative layer, and becomes impressive for ten minutes and unmaintainable for eight hours. Complexity belongs in the material the piece presents, whereas its structure should stay small, since every added branch multiplies the states the eight-hour test has to cover.

## Common mistakes

- **Leaving out maximum durations** is the single most common reason an installation is found frozen, because one departed visitor leaves an instant waiting forever, whereas a maximum on every waiting instant lets the piece recover on its own.
- **An idle state that is not defined as a cue** makes the piece look different depending on which outcome ran last.
- **Branches with different durations and one shared return timing** cut one outcome off, so test the return from both.
- **Testing only for two minutes** finds none of the failures in the eight-hour test, since each of them needs time to appear.
- **A stop that leaves the room lit** is the case the stop cue exists to prevent.
- **Documentation written for yourself instead of for the invigilator** fails its reader, and if it contains the word "scenario" it needs rewriting.

## Exercise

Give the installation a third outcome that only some visitors see, because a piece that occasionally shows something new rewards a second visit, and "rare" has to be built as carefully as "always".

1. **Draw a random number while the piece idles** by selecting the idle phrase and double-clicking `LFO` in the process library, then setting its `Waveform` to `Noise1` in the inspector and typing a parameter nothing else writes into its `Out` field, such as `lesson:/shutter` in `p4-solution.score` or a new float on an OSC device of your own. With `Ampl.` and `Offset` at 0.5, the value is spread evenly between 0 and 1 and changes on every tick.
2. **Add the third outcome** by dropping an excerpt from the user library onto the circle at the end of the idle phrase, the visitor's instant, as in [Lesson 16]({{ site.baseurl }}/learn/16-conditions-and-branching.html), and give it a return transition to the first instant, as in [Lesson 17]({{ site.baseurl }}/learn/17-loops-and-out-of-time.html).

   {: .warning }
   > **Aim for the right-hand edge of that circle**, since an excerpt dropped on the idle phrase itself lands inside it as a second slot.

3. **Make it rare** by selecting that circle, through the object tree if a click catches the idle phrase instead, pressing `C`, and giving the condition `lesson:/shutter`, `>`, and `0.9`.
4. **Keep the partition** by clicking `+` beside each of the other two conditions and adding `lesson:/shutter`, `≤`, and `0.9` in the row that appears, whose `&` joins the two tests. Without it, a rare arrival would also satisfy one of the others, and two outcomes would run at once.
5. **Count** by releasing the visitor trigger twenty times and noting which outcome ran each time, which in `p4-solution.score` is `Quiet` or the new one, since nothing drives `lesson:/level` there. On paper a threshold of 0.9 gives one release in ten, whereas a test on {{ page.score_version }} gave fifteen in eighty-nine, closer to one in six, which is why counting is what makes "rare" reliable instead of accidental.

**You are done when** twenty releases in a row return to idle, the third outcome turns up among them without ever running beside another, and your count tells you how often it comes. Then run the eight-hour test again, since any change reopens it.

## Going further

- [Out-of-time triggering]({{ site.docs_baseurl }}/common-practices/3-out-of-time.html) and [looping]({{ site.docs_baseurl }}/common-practices/1-looping.html) for the two structures this milestone combines.
- [Start and stop cues]({{ site.docs_baseurl }}/common-practices/7-start-stop-cues.html) for the safety behaviour.
- [Headless and embedded]({{ site.baseurl }}/learn/35-headless-and-embedded.html), later in the course, for running this on a machine with no screen.
- [Rehearsal to show]({{ site.baseurl }}/learn/34-rehearsal-to-show.html) for the documentation this milestone starts.

{% include lesson_files.html %}
