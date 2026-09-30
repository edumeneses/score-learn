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
practice_time: "20 min"
score_file: 17-loops-and-out-of-time/lesson-17.score
---

# Lesson 17: Loops, repetition, and out-of-time material

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 16]({{ site.baseurl }}/learn/16-conditions-and-branching.html), because the structures here are drawn between the same instants that Lesson 16 branched from.
>
> **You will need** an empty document and the bench from P3 for the walkthrough, and your sketch for the exercise.
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

A repetition count is expressed through a maximum duration on the interval that contains the loop. The idiomatic way to say "about four times" is to put the loop inside a sub-scenario, leave the trigger at the end of the interval that holds it unsatisfied, and give that interval a maximum duration, so that the loop repeats until the maximum ends its container, and the count is tuned by moving the maximum. The count is arithmetic instead of a counter, which feels indirect at first. However, it composes better with the rest of the score than a counter would.

### Out-of-time material

Out-of-time material is material not connected to the start of the score, which therefore does not run when the score plays. Give its first instant a trigger with **start on play** enabled, and it becomes available to fire at any moment, from a click or from a device value, without having been on the main timeline. In other words, it is how a cue that fires "whenever" is built, and some people use it as a sandbox as well.

### Process loops and structure loops

Process loops are a different mechanism from structure loops. An interval can loop a process internally, which is not the same as looping structure. In contrast to the structure loops this lesson is about, a sound file set to loop in its inspector is the other kind, and the two are often used together.

## Walkthrough: three structures

[![A two-interval phrase with a dash-dot transition running back from its end to the instant before it, and below, an interval joined to nothing, carrying a trigger armed on play]({{ site.img }}/17/17-01-loop-and-out-of-time.png)]({{ site.scores }}/17-loops-and-out-of-time/lesson-17.score){: download="" title="Download lesson-17.score, the document in this figure" }

Both structures are in `lesson-17.score`. The dash-dot line with the arrowhead is the transition, which leaves the instant at the end of `Phrase` and arrives at the instant before it, so that `Phrase` repeats indefinitely. Below it, `On demand` is joined to no instant the score starts from, which is the whole of what "out of time" means, while the yellow marker on its first instant is a trigger with start on play enabled, the only way the material will run.

1. **Build a two-interval phrase**, with an automation in each, so that you can hear or see where you are.
2. **Add a transition back** by selecting the phrase's last circle and dragging the red plus that appears below it onto the phrase's first circle, then play, and the phrase repeats indefinitely.

   {: .warning }
   > **A loop with no exit runs forever**, which is either what you want, for an installation, or a bug. Steps 3 and 4 bound it by containing it, since the loop goes inside a sub-scenario whose interval ends on a trigger, released by hand or by a maximum duration.

3. **Put the loop in a container** by undoing the transition, selecting both intervals and the circle between them with `Ctrl` held for the second and third clicks, and using `Object > Encapsulate`, `Ctrl+Alt+E`, while `Decapsulate`, `Ctrl+Alt+D`, is the inverse. Double-click the new interval's name to enter it, draw the transition again inside, and return by clicking the document's name at the top left.

   {: .warning }
   > **Encapsulate does nothing if the circle between the intervals is left out**, because the selection then has two entry points, which {{ page.score_version }} refuses without a message.

4. **Bound the container** by putting a trigger on its last circle, then play and fire it, so that the loop and every process in it stop and the score continues. For a bound in time instead, tick `Max` for the container in the inspector and drag the closing bracket that appears, and the loop repeats until the maximum ends it.

   {: .warning }
   > **A trigger and a maximum on the loop's own closing instant do not bound it**, because each pass then waits for the maximum and loops again; the bound belongs on the interval that contains the loop.

5. **Add a parallel layer** and see what a transition does to it, by putting a second interval on the loop's starting instant so that it runs alongside, then letting the loop restart; the layer restarts as well, because the transition targets the instant.
6. **Isolate the layer** with a second transition, so that the layer's own loop is separate, which disturbs no timing, since transitions are instantaneous.
7. **Build a toggle** by putting a trigger at both ends of a looping interval, both firing on a value from your bench, so that pressing starts it and releasing returns it to the start and waits; a minimum duration on the interval prevents a double tap from skipping a cycle.
8. **Build out-of-time material** by making an interval that is *not* connected to the start of the score, and play to confirm that it does not run. Give its start a trigger and turn on `Start on play`, the right-hand of the two buttons at the top of the trigger's inspector, then fire it while the score plays, and it runs on demand from outside the timeline.
9. **Try the re-trigger option**, the left-hand button, `Auto-trigger`, because with it enabled, firing it again restarts the material from the beginning, whereas without it, firing again stops the material, and it needs another event to start.
10. **Try the hover controls**, since while the score plays, hovering an interval shows play and stop buttons that start or stop it directly, ignoring the score's semantics while respecting its quantisation, which suits rehearsal.

## Which bound to choose

The three ways to stop a loop suit different situations, and the choice follows from whether the exit is a time, an event, or a count.

**A maximum duration on the containing interval** suits the case where the count is approximate and the piece is timed, as in "this figure repeats for about twenty seconds"; once the loop is contained it is one bracket to drag, and it makes the score's total duration predictable.

**A sub-scenario with a trigger on the containing interval** suits the case where the exit is an event, as in "this repeats until the performer arrives"; it is the cleanest structurally, because the loop is one object that can be stopped as a unit.

In contrast, **a condition on the loop's closing instant** suits the case where the exit depends on a value, since the loop continues only while the condition holds; counting is the same mechanism with a parameter you increment each cycle, and it is the only option when "exactly seven times" is a requirement instead of a feeling.

## The mental model that makes this click

The timeline is better understood as a graph whose edges happen to be drawn left to right than as a line, because that description accounts for every structure in this lesson: instants are nodes, intervals are edges with duration, and transitions are edges with none.

Seen that way, the structures of this lesson are one mechanism, since a loop is an edge pointing backwards, a state machine is a set of nodes with conditional edges, out-of-time material is a node with no path from the start, and parallel layers are two edges from one node. In other words, there is no separate looping feature or state machine mode, only a graph whose left-to-right drawing suits the common case where time moves forward.

## Common mistakes

- **A loop with no exit in a piece that has to end**, which is acceptable in an installation that runs all day, whereas in a concert it means the score cannot reach its final cue.
- **Forgetting that a transition re-executes every branch on its target instant**, including parallel ones you did not intend to restart.
- **Several transitions to one instant** without realising that the smallest loop restarts first and cuts short whatever else was running.
- **No minimum duration on a toggle**, so that one press reads as two.
- **Confusing a structure loop with a process loop**, when a looping sound file inside a non-looping interval is a different statement from a looping interval.

## Exercise

Give the sketch a pulse that repeats until you send it away, and a sound you fire whenever you like, because a loop needs an exit and a cue that fires "whenever" needs an armed trigger.

1. **Drop a one-shot** from the `one_shots` folder of `citizen-dj-free-music` in the user library onto the empty timeline below the excerpts; one about a second long, found by auditioning, makes a clear pulse.
2. **Draw the loop** by selecting the circle at its right end and dragging the red plus below it onto the circle at its left end, as in walkthrough step 2; play, and the one-shot repeats for as long as the score plays.
3. **Give the loop an exit** by selecting that right-hand circle, pressing `C`, and giving the condition `Window:/cursor/scaled@[1]`, `<`, and `0.5`, as in [Lesson 16]({{ site.baseurl }}/learn/16-conditions-and-branching.html). The pulse then repeats while the pointer rests in the upper half of the window and stops at the end of the pass during which you lower it.
4. **Drop a second one-shot** further down, select the empty interval that leads to it, and press `Delete`, so that nothing joins it to the start; play, and it stays silent.
5. **Arm it** by selecting its left-hand circle, pressing `T`, and turning on `Start on play` as in walkthrough step 8; play, and click its T marker whenever you like.

**You are done when** the pulse repeats until you lower the pointer, and the second one-shot sounds each time you click it and never by itself.

## Going further

- [Looping]({{ site.docs_baseurl }}/common-practices/1-looping.html), the reference for transitions, nested loops, and repetition counts.
- [Switches]({{ site.docs_baseurl }}/common-practices/2-switches.html) for toggles and parallel switching.
- [Out-of-time triggering]({{ site.docs_baseurl }}/common-practices/3-out-of-time.html) for material outside the timeline.
- [Live coding]({{ site.docs_baseurl }}/common-practices/8-live-coding.html), which uses never-ending intervals to make a score behave like a patch.

{% include lesson_files.html %}
