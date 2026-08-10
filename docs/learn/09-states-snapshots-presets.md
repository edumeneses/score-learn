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
> **You will need** your own device, and `lesson-09.score` as the reference.
>
> **You will build** a three-cue sequence captured from live values rather than typed, and one reusable fragment in your user library.

## Why this matters

Everything so far has been continuous: curves that move over time. This lesson is the other half of the craft, the discrete half. A **state** sends a set of messages at one instant, which is what the rest of the world calls a cue, and for a great deal of practical work, installations, exhibitions, theatre, it is the primary tool. *score*'s particular strength is that cues and curves are not separate systems: they live in the same document, on the same timeline, and one workflow moves between them.

The productive part is capture. You do not type values into a cue; you set your equipment up until it looks right, and then take a snapshot. That is how this work is actually done, and doing it any other way is why people find cue authoring tedious.

## Concepts

**State as cue.** A state holds a set of messages, each an address and a value, and sends them all at the instant it is reached. Any address from any device may appear in one state. In the interface, a state is a disc on a vertical line; select it and the inspector lists its messages as a tree.

**Snapshot by drag.** Dragging a selection of parameters from the device explorer onto the timeline creates a state containing them with their current values. Selecting a node selects everything beneath it. `Shift+click` extends a selection, `Ctrl+click` adds to it, and `Esc` clears it, which matters because a stale selection makes the next drag capture the wrong thing.

**Two ways to refresh, and they are not the same.** With a state selected, the inspector offers two camera icons. **Snapshot**, `Ctrl+L`, takes whatever is currently selected in the device explorer and copies it into the cue, so it can add addresses. **Refresh**, `Ctrl+R`, takes the addresses already in the cue and updates their stored values to the live ones, changing values without changing which parameters are stored. Reaching for the wrong one either floods a cue with parameters you did not want or quietly fails to add the one you did.

**Adding to an existing cue.** Dropping parameters onto an existing state adds them; an address already present is replaced by the dropped value.

**Auto-sequence.** An option, off by default, in `Settings` under the user interface tab. With it on, chaining a new state from an existing one, using the blue `+` beside the state, captures the new values *and* writes automations for every parameter that changed between the two. It is the fastest route from two static looks to a timed transition between them. Without it, the same gesture still reuses the previous selection but writes no automations.

**Scenario presets.** Select part of a score and drag it into the user library with `Alt` held; *score* writes a `.scenario` file you can drag back into any document. Note the asymmetry, which the reference documentation is explicit about: *scenario* presets exist, per-process presets do not yet.

## Walkthrough: three cues, captured not typed

![Two intervals chained between three states, each state carrying its own messages, drawn as a plain cue list with no processes]({{ site.img }}/09/09-01-cue-list.png)

1. **Look at the reference.** Open `lesson-09.score`. Three states, two intervals, no processes at all. This is what a cue list looks like in *score*: the intervals only carry time, and everything that happens happens at the instants.
2. **Set your equipment to its opening look.** Use the device explorer's inspector to write values directly until the state of the world is what you want at the start.
3. **Select the parameters that matter** in the explorer, and drag them onto the timeline at position zero. A disc appears. Select it and read its messages: those are your captured values.
4. **Change the world.** Set new values in the explorer, enough that several parameters differ.
5. **Chain a second cue.** With the first state selected, drag from the blue `+` beside it to a later point on the timeline. Because the selection is remembered, the same parameters are captured with their new values.
6. **Turn on auto-sequence and do it again.** In `Settings`, user interface tab, enable auto-sequence. Chain a third cue the same way. This time *score* also writes automations between cue two and cue three for every parameter that changed. Look at the slots it created: stacked automations, the frontmost drawn in red, the rest greyed.
7. **Edit what it wrote.** Click the address bar at the top of a stacked slot to bring one automation forward, adjust its curve, and remove any you did not want by right-clicking a slot background and choosing remove. Generated material is a starting point, not a verdict.
8. **Fix a value without rebuilding.** Change one parameter in the explorer, select the cue that should hold the new value, and press `Ctrl+R`. Only stored values update. Then select an extra parameter in the explorer, select the same cue, and press `Ctrl+L` to add it.
9. **Play it.** `space`. Each cue fires as the playhead reaches it. Stop with `↵`, and note that stopping does not undo anything a cue sent: the world stays where the last cue left it, which is why [Milestone P1]({{ site.baseurl }}/learn/p1-automated-cue.html) insisted on a defined ending.
10. **Save the pattern.** Select your three cues and the intervals between them, hold `Alt`, and drag into the user library. Start a new document and drag the fragment back in.

## Cues that do not wait for the playhead

A cue does not have to sit in the flow of time. A state can be given a trigger and left floating in the scenario, so that it fires when something external says so rather than when the playhead arrives. The setup uses a trigger with **auto-trigger** and **start on play** enabled, and it is how an operator-fired or MIDI-fired cue is built.

This lesson does not build one, because triggers are [Lesson 15]({{ site.baseurl }}/learn/15-triggers.html) and their transport implications are [Lesson 18]({{ site.baseurl }}/learn/18-cues-and-transport.html). Knowing the possibility exists is enough for now: if your instinct is that cues should be fired rather than scheduled, you are right, and the course gets there in Module F.

## Cue lists that grow

Three cues fit on a screen. Forty do not, and a cue list becomes unusable at about the point it becomes useful, unless a few habits are in place from the start.

**Name every cue.** A state's name is what you will read when the document is folded and what you will say out loud in a rehearsal. `house-to-half` is a cue; `State.17` is a puzzle.

**Group with intervals, not with distance.** Resist spacing cues apart to make room visually; zoom instead, with `Ctrl` and the mouse wheel. Distance on the timeline is duration, and using it as layout means your rehearsal timings drift as you tidy.

**Capture narrowly.** A cue holding every parameter of every device is easy to make with one drag from a parent node and painful to reason about, because you can no longer see what the cue is *for*. Capture the parameters the cue is about; let the ones that do not change stay where the previous cue left them.

**Store the recurring shapes.** A three-cue fade-in you use in every piece belongs in the user library as a `.scenario` fragment, named for what it does. Over a few projects this becomes a personal vocabulary, and it is the difference between building a show and rebuilding the same twenty minutes of work.

One consequence of capturing narrowly deserves stating: because a cue only sets what it names, the state of the world at any moment is the accumulation of every cue that has run. That is efficient and it is why the opening cue matters so much, as [Milestone P1]({{ site.baseurl }}/learn/p1-automated-cue.html) established.

## Common mistakes

- **Typing values instead of capturing them.** Slower, and it divorces the cue from what you actually saw and heard.
- **Confusing `Ctrl+L` with `Ctrl+R`.** Snapshot adds from the current selection; refresh updates what is already stored.
- **A stale explorer selection.** Select a parent node and you capture every parameter beneath it, which is occasionally what you want. `Esc` clears.
- **Trusting auto-sequence blindly.** It writes an automation for every parameter that changed, including ones that should have jumped rather than ramped. Delete those.
- **Losing an automation in a stack.** The frontmost is red, the others greyed; use the slot's address bar to choose.
- **Forgetting that stopping does not reset.** The last cue's values persist. Design an ending.

## Exercise

Build a four-cue sequence for your own device, captured entirely from live values, in which cue two and cue three are joined by automations written by auto-sequence and then edited by hand, while cue three and cue four jump with no transition at all. Then change your mind about one value in cue two and correct it with `Ctrl+R` rather than rebuilding.

**Success criterion:** playing from the start twice in a row produces identical behaviour, at least one auto-generated automation has been deliberately deleted, and the sequence exists as a `.scenario` fragment in your user library. If the second run differed from the first, your first cue does not capture everything the later cues change.

## Going further

- [Saving and recalling devices' state]({{ site.docs_baseurl }}/quick-start/saving-and-recalling-devices-state.html) and [states and automations in practice]({{ site.docs_baseurl }}/quick-start/states-and-automations-in-practice.html), the reference versions.
- [Cues in depth]({{ site.docs_baseurl }}/cues.html), including floating cues and external control.
- [Presets]({{ site.docs_baseurl }}/presets.html), for the scenario fragment mechanism.
- [Start and stop cues]({{ site.docs_baseurl }}/common-practices/7-start-stop-cues.html), a recipe [Lesson 18]({{ site.baseurl }}/learn/18-cues-and-transport.html) returns to.
