---
layout: default
title: "Lesson 17: Loops, repetition, and out-of-time material"
description: "Transitions that go back in time, controlled repetition counts, sub-scenarios that stop cleanly, and material that lives outside the timeline."
parent: Lessons
nav_order: 20
unit: "17"
permalink: /learn/17-loops-and-out-of-time.html
score_version: "3.8.2"
reading_time: "13 min"
practice_time: "25 min"
score_file: 17-loops-and-out-of-time/lesson-17.score
---

# Lesson 17: Loops, repetition, and out-of-time material

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 16]({{ site.baseurl }}/learn/16-conditions-and-branching.html), because the structures here are drawn between the same instants that Lesson 16 branched from.
>
> **You will need** an empty document and the bench from P3 for firing things.
>
> **You will build** three structures, which are a loop that runs forever, a loop that runs a chosen number of times, and material that only exists when something fires it.

## Why this matters

An installation runs for eight hours, a performance repeats a phrase until the performer moves on, and a generative section produces material indefinitely; none of these is expressible as a longer timeline, although all three are ordinary requirements.

This lesson is therefore where the timeline stops being a line at all, and the mechanism is simple although slightly startling the first time, because an instantaneous interval can connect two states *regardless of their chronological order*, including backwards. Once you have that, loops, state machines, and out-of-time material are the same idea applied differently, which the final section makes explicit.

## Concepts

### Transitions

A transition is an instantaneous interval. It has zero duration and connects one state to another, and because it takes no time it can connect backwards without paradox, since reaching its start sends execution to its end wherever that is on the timeline; a loop is a transition pointing back to an earlier instant.

### Transitions target instants

Transitions connect to instants and not to intervals. Consequently, transitioning to an instant re-executes *every branch* connected to that instant, including parallel ones, because what the transition restarts is the point in time and not one path leaving it.

### Repetition counts

A repetition count is expressed through a maximum duration. The idiomatic way to say "about four times" is to leave the closing trigger unsatisfied on its own and give the preceding interval a maximum duration, so that the loop runs for the loop duration plus that maximum, and the count is tuned by adjusting it. The count is arithmetic instead of a counter, which feels indirect at first. However, it composes better with the rest of the score than a counter would.

### Out-of-time material

Out-of-time material is material not connected to the start of the score, which therefore does not run when the score plays. Give its first instant a trigger with **start on play** enabled, and it becomes available to fire at any moment, from a click or from a device value, without having been on the main timeline. In other words, it is how a cue that fires "whenever" is built, and some people use it as a sandbox as well.

### Process loops and structure loops

Process loops are a different mechanism from structure loops. An interval can loop a process internally, which is not the same as looping structure. In contrast to the structure loops this lesson is about, a sound file set to loop in its inspector is the other kind, and the two are often used together.

## Walkthrough: three structures

![A two-interval phrase with a dash-dot transition running back from its end to the instant before it, and below, an interval joined to nothing, carrying a trigger armed on play]({{ site.img }}/17/17-01-loop-and-out-of-time.png)

Both structures are in `lesson-17.score`, which ships with this lesson. The dash-dot line with the arrowhead is the transition, which leaves the instant at the end of `Phrase` and arrives at the instant before it, so that `Phrase` repeats and the score does not reach an end. Below it, `On demand` is joined to no instant the score starts from, which is the whole of what "out of time" means, while the yellow marker on its first instant is a trigger with start on play enabled, and that trigger is the only way the material will run.

Furthermore, the drawing itself describes the mechanism, because a transition looks different from an interval and *is* different; it has no duration, so there is no span to draw across, only a line from one instant to another.

1. **Build a two-interval phrase**, with an automation in each, so that you can hear or see where you are.
2. **Add a transition back** by dragging a connection from the last state to the first instant, then play, and the phrase repeats indefinitely.

   {: .warning }
   > **A loop with no exit runs forever**, which is either what you want, for an installation, or a bug. Steps 3 and 4 bound it in the two structural ways: a **maximum duration** on the loop's closing instant, so that the loop exits after a bounded time, or a **sub-scenario** whose containing interval ends on a trigger, which stops the loop and continues the score.

3. **Bound it with a maximum duration** by putting a trigger on the loop's closing instant, leaving its expression unsatisfied, and setting the preceding interval's maximum duration; on play, the loop repeats and then continues into whatever follows, and adjusting the maximum changes how many repetitions you get.
4. **Now bound it structurally** by undoing the above, selecting the phrase, and using `Object > Encapsulate`, `Ctrl+Alt+E`, to put it inside a sub-scenario so that the loop is contained in one interval, while `Decapsulate`, `Ctrl+Alt+D`, is the inverse when you change your mind. Put a trigger on the *end of that interval*, play, and fire the trigger, so that the loop and every process in it stops and the score continues, which is the cleaner idiom when you want a definite exit.
5. **Add a parallel layer** and see what a transition does to it, by putting a second interval on the loop's starting instant so that it runs alongside, then letting the loop restart; the layer restarts as well, because the transition targets the instant, and understanding this once prevents a class of confusing behaviour.
6. **Isolate the layer** with a second transition, so that the layer's own loop is separate, and note that because transitions are instantaneous they can isolate parallel loops without disturbing timing.
7. **Build a toggle** by putting a trigger at both ends of a looping interval, both firing on a value from your bench, so that pressing starts it and releasing returns it to the start and waits; a minimum duration on the interval prevents a double tap from skipping a cycle.
8. **Build out-of-time material** by making an interval that is *not* connected to the start of the score, and play to confirm that it does not run. Give its start a trigger with start on play enabled, then fire it while the score plays, and it runs on demand from outside the timeline.
9. **Try the re-trigger option** on that trigger, because with re-triggering enabled, firing it again restarts the material from the beginning, whereas without it, firing again stops the material, and it needs another event to start.
10. **Try the hover controls**, since while the score plays, hovering an interval shows play and stop buttons that start or stop that interval directly, ignoring the score's semantics; they are useful in rehearsal, and they respect the quantisation settings.

## Which bound to choose

The three ways to stop a loop suit different situations, and the choice follows from whether the exit is a time, an event, or a count.

**A maximum duration** suits the case where the count is approximate and the piece is timed, as in "this figure repeats for about twenty seconds"; it is the cheapest to write, and it makes the score's total duration predictable.

**A sub-scenario with a trigger on the containing interval** suits the case where the exit is an event, as in "this repeats until the performer arrives"; it is the cleanest structurally, because the loop is one object that can be stopped as a unit.

In contrast, **a condition counting a value** suits the case where the count must be exact and visible, so that you increment a parameter each cycle and branch when it reaches your number; it needs more machinery, and it is the only option when "exactly seven times" is a requirement instead of a feeling.

## The mental model that makes this click

The timeline is better understood as a graph whose edges happen to be drawn left to right than as a line, because that description accounts for every structure in this lesson: instants are nodes, intervals are edges with duration, and transitions are edges with none.

Seen that way, the structures of this lesson are one mechanism, since a loop is an edge pointing backwards, a state machine is a set of nodes with conditional edges, out-of-time material is a node with no path from the start, and parallel layers are two edges from one node. In other words, there is no separate looping feature, no separate state machine mode, and no special case for material outside the timeline, because there is a graph, and the left-to-right drawing is a convenience for the common case where time moves forward.

## Common mistakes

- **A loop with no exit in a piece that has to end**, which is acceptable in an installation that runs all day, whereas in a concert it means the score cannot reach its final cue.
- **Forgetting that a transition re-executes every branch on its target instant**, including parallel ones you did not intend to restart.
- **Several transitions to one instant** without realising that the smallest loop restarts first and cuts short whatever else was running.
- **No minimum duration on a toggle**, so that one press reads as two.
- **Expecting out-of-time material to run on play**, when by design it does not, and start on play exists to make it fireable.
- **Confusing a structure loop with a process loop**, when a looping sound file inside a non-looping interval is a different statement from a looping interval.

## Exercise

Build a document with three parts: a phrase that repeats about four times and then continues, implemented with a maximum duration; a phrase inside a sub-scenario that repeats until you fire a trigger and then continues; and an out-of-time cue that can be fired at any moment while the rest plays.

**Success criterion:** the first part always ends without intervention, the second ends only when fired, and the third does not run unless fired. Additionally, add a parallel layer to the first loop and say, before testing, whether it will restart with each repetition, and test to see whether you were right.

## Going further

- [Looping]({{ site.docs_baseurl }}/common-practices/1-looping.html), the reference for transitions, nested loops, and repetition counts.
- [Switches]({{ site.docs_baseurl }}/common-practices/2-switches.html) for toggles and parallel switching.
- [Out-of-time triggering]({{ site.docs_baseurl }}/common-practices/3-out-of-time.html) for material outside the timeline.
- [Live coding]({{ site.docs_baseurl }}/common-practices/8-live-coding.html), which uses never-ending intervals to make a score behave like a patch.
