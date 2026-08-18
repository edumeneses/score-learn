---
layout: default
title: "Lesson 17: Loops and out of time"
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

# Lesson 17: Loops and out of time

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 16]({{ site.baseurl }}/learn/16-conditions-and-branching.html).
>
> **You will need** an empty document and the bench from P3 for firing things.
>
> **You will build** three structures: a loop that runs forever, a loop that runs a chosen number of times, and material that only exists when something fires it.

## Why this matters

An installation runs for eight hours. A performance repeats a phrase until the performer moves on. A generative section produces material indefinitely. None of these is expressible as a longer timeline, and all three are ordinary requirements.

This lesson is also where the timeline stops being a line at all. The mechanism is simple and slightly startling the first time: an instantaneous interval can connect two states *regardless of their chronological order*, including backwards. Once you have that, loops, state machines, and out-of-time material are all the same idea applied differently.

## Concepts

**Transitions.** An instantaneous interval, with zero duration, connecting one state to another. Because it takes no time, it can connect backwards without paradox: reaching its start sends execution to its end, wherever that is on the timeline. A loop is a transition pointing back to an earlier instant.

**Transitions connect to instants, not to intervals.** This has a consequence worth knowing before you are surprised by it: transitioning to an instant re-executes *everything* connected to that instant, including parallel branches. When several transitions target the same instant, the smallest loop restarts first and cuts short whatever else was running.

**A loop with no exit runs forever.** Which is either what you want, for an installation, or a bug. Two ways to bound it: put the loop inside a **sub-scenario** and trigger the end of the interval containing that sub-scenario, which stops the loop and continues the score; or use a **maximum duration** on the loop's closing instant, so the loop exits after a bounded time.

**Repetition count by maximum duration.** The idiomatic way to say "about four times": leave the closing trigger never satisfied on its own, and give the preceding interval a maximum duration. The loop then runs for loop duration plus that maximum, and the count is tuned by adjusting it. It is arithmetic rather than a counter, which feels indirect at first and composes better with everything else.

**Out-of-time material.** Material not connected to the start of the score does not run when the score plays. Give its first instant a trigger with **start on play** enabled, and it becomes available to fire at any moment, from a click or from a device value, without ever having been on the main timeline. Some people use this as a sandbox; it is also how a cue that fires "whenever" is built.

**Process loops are a different thing.** An interval can also loop a process internally, which is not the same as looping structure. Structure loops are what this lesson is about; a sound file set to loop in its inspector is the other kind, and the two are often used together.

## Walkthrough: three structures

![A two-interval phrase with a dash-dot transition running back from its end to the instant before it, and below, an interval joined to nothing, carrying a trigger armed on play]({{ site.img }}/17/17-01-loop-and-out-of-time.png)

Both structures are in `lesson-17.score`, which ships with this lesson. The dash-dot line with the arrowhead is the transition: it leaves the instant at the end of `Phrase` and arrives at the instant before it, so `Phrase` repeats and the score never reaches an end. Below it, `On demand` is joined to nothing the score starts from, which is the whole of what "out of time" means; the yellow marker on its first instant is a trigger with start on play enabled, and it is the only way that material will ever run.

Note what the drawing tells you about the mechanism. A transition looks different from an interval because it *is* different: it has no duration, so there is nothing to draw across, only a line from one instant to another.

1. **Build a two-interval phrase**, each with an automation, so you can hear or see where you are.
2. **Add a transition back.** From the last state, drag a connection back to the first instant. Play: the phrase repeats indefinitely.
3. **Bound it with a maximum duration.** Put a trigger on the loop's closing instant, leave its expression never satisfied, and set the preceding interval's maximum duration. Play: the loop repeats and then continues into whatever follows. Adjust the maximum to change how many repetitions you get.
4. **Now bound it structurally.** Undo the above, select the phrase, and use `Object > Encapsulate`, `Ctrl+Alt+E`, to put it inside a sub-scenario, so the loop is contained in one interval. `Decapsulate`, `Ctrl+Alt+D`, is the inverse when you change your mind. Put a trigger on the *end of that interval*. Play, and fire the trigger: the loop and everything in it stops, and the score continues. This is the cleaner idiom when you want a definite exit.
5. **Add a parallel layer** and see what a transition does to it. Put a second interval on the loop's starting instant, so it runs alongside, then let the loop restart: the layer restarts too, because the transition targets the instant. Understanding this once prevents a class of confusing behaviour.
6. **Isolate the layer.** Use a second transition so the layer's own loop is separate, and note that because transitions are instantaneous, they can be used to isolate parallel loops without disturbing timing.
7. **Build a toggle.** Put a trigger at both ends of a looping interval, both firing on a value from your bench: pressing starts it, releasing returns it to the start and waits. A minimum duration on the interval prevents a double tap from skipping a cycle.
8. **Build out-of-time material.** Make an interval that is *not* connected to the start of the score. Play: it does not run. Give its start a trigger with start on play enabled, then fire it while the score plays. It runs, on demand, from outside the timeline.
9. **Try the re-trigger option** on that trigger. With re-triggering enabled, firing it again restarts the material from the beginning; without, firing again stops it, and it needs another event to start.
10. **Try the hover controls.** While the score plays, hovering an interval shows play and stop buttons, which start or stop that interval directly, ignoring the score's semantics. Useful in rehearsal; note that they respect the quantisation settings.

## Which bound to choose

Three ways to stop a loop, and they suit different situations.

**Maximum duration** when the count is approximate and the piece is timed: "this figure repeats for about twenty seconds". Cheapest to write, and it makes the score's total duration predictable.

**Sub-scenario with a trigger on the containing interval** when the exit is an event: "this repeats until the performer arrives". The cleanest structurally, because the loop is one object that can be stopped as a unit.

**A condition counting a value** when the count must be exact and visible: increment a parameter each cycle and branch when it reaches your number. More machinery, and the only option when "exactly seven times" is a requirement rather than a feeling.

## The mental model that makes this click

Stop thinking of the timeline as a line and think of it as a graph whose edges happen to be drawn left to right. Instants are nodes; intervals are edges with duration; transitions are edges with none.

Once that lands, everything in this lesson is one mechanism. A loop is an edge pointing backwards. A state machine is a set of nodes with conditional edges. Out-of-time material is a node with no path from the start. Parallel layers are two edges from one node. There is no separate looping feature, no separate state machine mode, and no special case for material outside the timeline: there is a graph, and the left-to-right drawing is a convenience for the common case where time moves forward.

## Common mistakes

- **A loop with no exit in a piece that has to end.** Fine in an installation, fatal in a concert.
- **Forgetting that a transition re-executes everything on its target instant**, including parallel branches you did not intend to restart.
- **Several transitions to one instant** without realising the smallest loop wins and cuts the others short.
- **No minimum duration on a toggle**, so one press reads as two.
- **Expecting out-of-time material to run on play.** It will not, by design; that is what start on play is for.
- **Confusing a structure loop with a process loop.** A looping sound file inside a non-looping interval is a different statement from a looping interval.

## Exercise

Build a document with three parts: a phrase that repeats about four times and then continues, implemented with a maximum duration; a phrase inside a sub-scenario that repeats until you fire a trigger and then continues; and an out-of-time cue that can be fired at any moment while the rest plays.

**Success criterion:** the first part always ends without intervention, the second ends only when fired, and the third never runs unless fired. Then add a parallel layer to the first loop and say, before testing, whether it will restart with each repetition. Test, and see whether you were right.

## Going further

- [Looping]({{ site.docs_baseurl }}/common-practices/1-looping.html), the reference for transitions, nested loops, and repetition counts.
- [Switches]({{ site.docs_baseurl }}/common-practices/2-switches.html) for toggles and parallel switching.
- [Out-of-time triggering]({{ site.docs_baseurl }}/common-practices/3-out-of-time.html) for material outside the timeline.
- [Live coding]({{ site.docs_baseurl }}/common-practices/8-live-coding.html), which uses never-ending intervals to make a score behave like a patch.
