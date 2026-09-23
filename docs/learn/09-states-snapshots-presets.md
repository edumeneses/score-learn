---
layout: default
title: "Lesson 09: States, snapshots, and presets"
description: "Capture a device's condition as a cue, update it in place, chain cues with auto-sequence, and save a fragment for reuse."
parent: Lessons
nav_order: 10
unit: "09"
permalink: /learn/09-states-snapshots-presets.html
score_version: "3.8.2"
reading_time: "13 min"
practice_time: "25 min"
score_file: 09-states-snapshots-presets/lesson-09.score
---

# Lesson 09: States, snapshots, and presets

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 08]({{ site.baseurl }}/learn/08-units-ranges-types.html), so that the values you capture mean what you think they mean.
>
> **You will need** your own device, together with `lesson-09.score` as the reference.
>
> **You will build** a three-cue sequence captured from live values instead of typed, and one reusable fragment in your user library.

## Why this matters

The lessons so far have dealt with continuous movement, which is curves that change over time, whereas this lesson covers the discrete half of the work. A **state** sends a set of messages at one instant, which is what the rest of the world calls a cue, and for a great deal of practical work in installations, exhibitions, and theatre it is the primary tool. Moreover, *score*'s particular strength is that cues and curves are not separate systems, because they live in the same document, on the same timeline, and one workflow moves between them.

The productive part of the workflow is capture, because you do not type values into a cue; you set your equipment up until it looks right and then take a snapshot. Typing values by hand is the reason people find cue authoring tedious, whereas capturing them keeps the cue tied to what you saw and heard.

## Concepts

### States and their messages

A state holds a set of messages and sends them at one instant. Each message is an address and a value, and any address from any device may appear in one state. In the interface, a state is a disc on a vertical line, and selecting it makes the inspector list its messages as a tree.

### Snapshots by dragging

Dragging parameters from the device explorer onto the timeline takes a snapshot. The drag creates a state containing the selected parameters with their current values, and selecting a node selects every parameter beneath it.

### Snapshot and refresh

The two refresh commands differ in what they change. With a state selected, the inspector offers two camera icons. **Snapshot**, `Ctrl+L`, takes whatever is currently selected in the device explorer and copies it into the cue, so it can add addresses. In contrast, **Refresh**, `Ctrl+R`, takes the addresses already in the cue and updates their stored values to the live ones, changing values without changing which parameters are stored.

### Auto-sequence transitions

Auto-sequence turns two captured looks into a timed transition. With it on, chaining a new state from an existing one, using the blue `+` beside the state, captures the new values *and* writes automations for every parameter that changed between the two. In contrast, without it the same gesture still reuses the previous selection but writes no automations.

### Scenario presets

Scenario presets save a fragment of a score for reuse. Select part of a score and drag it into the user library with `Alt` held, and *score* writes a `.scenario` file that you can drag back into any document. The reference documentation is explicit about an asymmetry here: *scenario* presets exist, whereas per-process presets do not yet.

## Walkthrough: three cues, captured not typed

![Two intervals chained between three states, each state carrying its own messages, drawn as a plain cue list with no processes]({{ site.img }}/09/09-01-cue-list.png)

1. **Look at the reference** by opening `lesson-09.score`, which holds three states, two intervals, and no processes at all. This is what a cue list looks like in *score*, because the intervals only carry time and the whole of the action happens at the instants.
2. **Set your equipment to its opening look** by using the device explorer's inspector to write values directly until the state of the world is what you want at the start.
3. **Select the parameters that matter** in the explorer, where `Shift+click` extends a selection, `Ctrl+click` adds to it, and `Esc` clears it, and drag them onto the timeline at position zero, so that a disc appears. Select it and read its messages, which are your captured values.
4. **Change the world** by setting new values in the explorer, enough that several parameters differ.
5. **Chain a second cue** by selecting the first state and dragging from the blue `+` beside it to a later point on the timeline. Because the selection is remembered, the same parameters are captured with their new values.
6. **Turn on auto-sequence and do it again**, by enabling it in `Settings`, under the user interface tab where it is off by default, and chaining a third cue the same way. This time *score* also writes automations between cue two and cue three for every parameter that changed, so look at the slots it created: stacked automations, with the frontmost drawn in red and the rest greyed.
7. **Edit what it wrote** by clicking the address bar at the top of a stacked slot to bring one automation forward, adjusting its curve, and removing any you did not want by right-clicking a slot background and choosing remove. Generated material saves the drawing and leaves the judgement to you, since auto-sequence ramps every parameter that changed.
8. **Fix a value without rebuilding** by changing one parameter in the explorer, selecting the cue that should hold the new value, and pressing `Ctrl+R`, which updates only the stored values. Then select an extra parameter in the explorer, select the same cue, and press `Ctrl+L` to add it. Dropping parameters from the explorer onto an existing state adds them in the same way, and an address already present is replaced by the dropped value, so the gesture that creates a cue also extends one.
9. **Play it** with `space`, so that each cue fires as the playhead reaches it. Stop with `↵`, and note that stopping does not undo what a cue sent: the world stays where the last cue left it, which is why [Milestone P1]({{ site.baseurl }}/learn/p1-automated-cue.html) insisted on a defined ending.
10. **Save the pattern** by selecting your three cues and the intervals between them, holding `Alt`, and dragging into the user library. Start a new document and drag the fragment back in.

## Cues that do not wait for the playhead

A cue does not have to sit in the flow of time, because a state can be given a trigger and left floating in the scenario, so that it fires when something external says so and not when the playhead arrives. The setup uses a trigger with **auto-trigger** and **start on play** enabled, and it is how an operator-fired cue, or a cue fired from MIDI (Musical Instrument Digital Interface), is built.

However, this lesson does not build one, because triggers are the subject of [Lesson 15]({{ site.baseurl }}/learn/15-triggers.html) and their transport implications belong to [Lesson 18]({{ site.baseurl }}/learn/18-cues-and-transport.html). Knowing that the possibility exists is enough for now, since if your instinct is that cues should be fired and not scheduled, that instinct is sound and the course gets there in Module F.

## Cue lists that grow

Three cues fit on a screen, whereas forty do not, and a cue list becomes unusable at about the point it becomes useful unless a few practices are in place from the start.

**Naming every cue makes the list readable when folded and speakable in rehearsal.** A state's name is what you will read when the document is folded and what you will say out loud in a rehearsal, so `house-to-half` is a cue while `State.17` is a puzzle.

**Grouping belongs to intervals, whereas distance on the timeline is duration.** Resist spacing cues apart to make room visually and zoom instead, with `Ctrl` and the mouse wheel, because using distance as layout means your rehearsal timings drift as you tidy.

**Capturing narrowly keeps each cue legible.** A cue holding every parameter of every device is easy to make with one drag from a parent node and painful to reason about, because you can no longer see what the cue is *for*. Capture the parameters the cue is about, and let the ones that do not change stay where the previous cue left them.

**Storing recurring shapes saves rebuilding them.** A three-cue fade-in you use in every piece belongs in the user library as a `.scenario` fragment, named for what it does. Furthermore, over a few projects this collection becomes a personal vocabulary, and it is the difference between building a show and rebuilding the same twenty minutes of work.

Capturing narrowly has one consequence that deserves stating, because a cue only sets what it names. In other words, the state of the world at any moment is the accumulation of every cue that has run, and that accumulation is efficient; it is also why the opening cue matters so much, as [Milestone P1]({{ site.baseurl }}/learn/p1-automated-cue.html) established.

## Common mistakes

- **Typing values instead of capturing them** is slower, and it divorces the cue from what you saw and heard.
- **Confusing `Ctrl+L` with `Ctrl+R`** mixes up two operations, since snapshot adds from the current selection while refresh updates what is already stored, so the wrong one either floods a cue with parameters you did not want or quietly fails to add the one you did.
- **A stale explorer selection** captures the wrong thing, because selecting a parent node captures every parameter beneath it, which is occasionally what you want; `Esc` clears the selection.
- **Trusting auto-sequence blindly** leaves ramps where jumps belong, since it writes an automation for every parameter that changed; delete the ones that should have jumped.
- **Losing an automation in a stack** happens because the frontmost is red and the others greyed, so use the slot's address bar to choose.
- **Forgetting that stopping does not reset** leaves the last cue's values in place, which is why a sequence needs a closing cue that puts the world where you want it left.

## Exercise

Build a four-cue sequence for your own device, captured entirely from live values, in which cue two and cue three are joined by automations written by auto-sequence and then edited by hand, while cue three and cue four jump with no transition at all. Then change your mind about one value in cue two and correct it with `Ctrl+R` instead of rebuilding.

**Success criterion:** playing from the start twice in a row produces identical behaviour, at least one auto-generated automation has been deleted on purpose, and the sequence exists as a `.scenario` fragment in your user library. If the second run differed from the first, your first cue does not capture every parameter that the later cues change.

## Going further

- [Saving and recalling devices' state]({{ site.docs_baseurl }}/quick-start/saving-and-recalling-devices-state.html) and [states and automations in practice]({{ site.docs_baseurl }}/quick-start/states-and-automations-in-practice.html) are the reference versions of this material.
- [Cues in depth]({{ site.docs_baseurl }}/cues.html) covers floating cues and external control.
- [Presets]({{ site.docs_baseurl }}/presets.html) documents the scenario fragment mechanism.
- [Start and stop cues]({{ site.docs_baseurl }}/common-practices/7-start-stop-cues.html) is a recipe that [Lesson 18]({{ site.baseurl }}/learn/18-cues-and-transport.html) returns to.
