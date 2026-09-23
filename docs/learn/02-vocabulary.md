---
layout: default
title: "Lesson 02: Vocabulary: intervals, states, triggers, and processes"
description: "Precise definitions of interval, state, event, trigger, process, slot, device, and address, checked against what the interface draws."
parent: Lessons
nav_order: 2
unit: "02"
permalink: /learn/02-vocabulary.html
score_version: "3.8.2"
reading_time: "12 min"
practice_time: "15 min"
score_file: 00-what-score-is/lesson-00.score
---

# Lesson 02: Vocabulary: intervals, states, triggers, and processes

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 01]({{ site.baseurl }}/learn/01-install.html), because you need *score* installed to open the file.
>
> **You will need** `lesson-00.score`, the document you read in Lesson 00, which you should open now.
>
> **You will build** a vocabulary you can use for the rest of the course without ambiguity, and the reflex of confirming a term in the inspector.

## Why this matters

This lesson defines eight words, which sounds like a poor use of twelve minutes until you consider what the usability study found: interviewees said, in their own words, that they leave parts of the interface alone because they do not know what those parts are for, and one named triggers specifically as an unfamiliar concept. However, both reports describe vocabulary problems that present as interface problems, because a reader who cannot name what they are looking at cannot search for it, cannot press `F1` usefully on it, and cannot ask a precise question about it.

Every definition below is checkable, since you can open `lesson-00.score`, click the object, and read the inspector on the right. That loop of clicking and confirming is the skill this lesson teaches. In contrast, the definitions are its content, and the loop is what remains useful once the definitions have been memorised.

## Concepts

### The score document

A score is the document, and each `.score` file holds one score. It contains a single root **interval**, which contains every other object, plus the declarations of the devices the document expects; when people say "my score", they mean this file, and Lesson 05 covers what travels with it.

### The interval

An interval is a stretch of time with a start, a duration, and contents. The word replaces several you may be carrying, because an interval differs from a track, a clip, and a region in two ways: it can contain other intervals, and its duration may be a range rather than a number. In `lesson-00.score`, `Approach`, `Bright`, and `Dark` are intervals, and so is the outermost bar named `lesson-00` that holds them.

### The state

A state is what happens at a single instant, which means a set of messages to send, each one an address paired with a value. In the interface a state is drawn as a small disc on a vertical line, and clicking one in `lesson-00.score` makes the inspector list its messages as a tree. A state with no messages is still meaningful, because it is where intervals attach.

### The event

An event is what a state sits on, and it is the object that can carry a condition. Several events can share one instant, which is how a branch is written: each outgoing event carries a different condition, and the ones whose conditions hold are the ones that fire. Most of the time you interact with states and let events stay implicit. However, you need the distinction the moment you write a branch, in Lesson 16.

### The trigger

A trigger is a property of an instant that makes it *wait* instead of firing when the playhead arrives. In other words, something must release it: a mouse click, a value from a device, or a condition becoming true. The interface draws it as a T-shaped marker above the state, and it draws the preceding interval's duration as a dashed line, because that duration is now open-ended; `lesson-00.score` has one trigger, labelled `waits for /lesson/go`.

### The process

A process is any object that produces or transforms values inside an interval. Automations, sound file players, MIDI (Musical Instrument Digital Interface) readers, shaders, scripts, and whole sub-scenarios are all processes. The definition has two consequences that matter now: a process always lives inside a stretch of time, and a scenario is itself a process, which is why intervals can nest without any special mechanism.

### The slot

A slot is the horizontal band an interval gives a process so that it can be drawn and edited. One interval can hold several processes, so it can have several slots. Moreover, slots can be stacked so that several automations share one band. The distinction between a process and its slot matters when you resize things, because dragging a slot's edge changes how much room the drawing gets, whereas changing how long the process runs is a separate operation.

### Devices and addresses

A device is the outside world as *score* sees it, and an address names one parameter inside it. A device is a piece of software or hardware, reachable over some protocol, exposing a tree of named parameters, while an address names one parameter in the form `device:/path/to/parameter`, for example `lesson:/level`. Addresses are how the score refers to the world without knowing what the world is, and Lesson 06 is entirely about that separation.

## The relations, in one paragraph

A **score** contains one root **interval**, and an interval contains **processes**, each drawn in a **slot**; among those processes may be scenarios, which contain more intervals. Intervals are bounded by **states**, which sit on **events**, which sit at instants; an instant may be a **trigger**, and an event may carry a **condition**. States hold messages, each message pairing an **address** with a value, and every address belongs to a **device**. Once that paragraph is learned, the interface stops being a set of unfamiliar shapes, because every shape on screen corresponds to one of its nouns.

## Walkthrough: confirm each word in the inspector

Open `lesson-00.score` and work down the list, clicking the object at each step and reading the right-hand panel before moving on.

![One instant of a score, zoomed: a state on its event, and the trigger marker above it]({{ site.img }}/02/02-01-instant.png)

The figure zooms on one instant of `lesson-00.score`, with the two objects that are easiest to confuse marked: the **state**, which step 5 below covers, and the **trigger** on the instant it sits at, which step 7 covers.

1. **The root interval is the outermost horizontal bar**, so click it and read the inspector, which shows its duration and its name, `lesson-00`; the fact that it has a duration at all confirms that the document is an interval like any other.
2. **A nested interval looks the same in the inspector as the root**, so click `Approach` and confirm that the inspector describes an interval whose contents include a scenario, `Scenario.10`, which in turn holds `Shutter`. The three levels of nesting come from one mechanism, because each level is an interval holding a scenario that holds intervals.
3. **A process is selected through its slot header**, so click the header reading `Automation (float).2 -> lesson:/level`, and the inspector describes an automation: its address, and the minimum and maximum it drives between. This is the moment to notice that a process's destination is a property of the process, whereas the interval that holds it declares no destination at all.
4. **A slot and a process are drawn together but are separate objects.** With that automation selected, look at how it is drawn, because the band is the slot while the curve is the process; `Ctrl+Alt+F` folds an interval's processes and `Ctrl+Alt+U` unrolls them, and after either shortcut the processes did not change although their slots did.
5. **A state is the disc at the very start of the timeline**, so click it, and the inspector lists a message, `lesson:/level` set to `0`; that message is a cue, and Lesson 09 is devoted to this mechanism alone.
6. **An event and its condition appear when you select the state at the start of `Bright`.** Its event carries a condition on `lesson:/level`, and the condition belongs to the event while the message belongs to the state, even though the interface draws them close together.
7. **The trigger sits on the instant labelled `waits for /lesson/go`**, so select it and confirm the T marker in the inspector; pressing `T` with a state selected toggles a trigger, so do it, look, and undo.
8. **The device appears in the `Device explorer` on the left**, so expand `lesson` and find its three parameters, `level`, `colour`, and `shutter`, which are the addresses every automation and message in this document refers to.

## The same words, inside the file

Because a `.score` file is JSON (JavaScript Object Notation), as [Lesson 05]({{ site.baseurl }}/learn/05-saving-and-reopening.html) covers, every word defined above has a written counterpart you can search for. Opening `lesson-00.score` in a text editor and searching for these strings is a fast way to confirm that the vocabulary is the software's own, whereas an invented vocabulary would leave no trace in the file.

| Word | What to search for in the file |
|---|---|
| Interval | `Scenario::IntervalModel` |
| State | `Scenario::StateModel` |
| Event, with its condition | `Scenario::EventModel`, then `Condition` |
| Trigger, on its instant | `Scenario::TimeSyncModel`, then `Active` and `Expression` |
| Process | the process name, for instance `Automation` |
| Slot | `SmallViewRack` and `FullViewRack` |
| Address | the plain text `lesson:/level` |

The table contains two details that repay a pause before moving on. A trigger is not an object of its own, since it is the `Active` flag on an instant, which is why Lesson 00 described a trigger as a property rather than a thing. Furthermore, a slot appears twice, once for the compact view and once for the full view, because an interval can be drawn two ways without changing what runs.

## Common mistakes

- **Using "track" for interval** costs you the two properties that matter, which are nesting and elastic duration.
- **Conflating state and event** leads to a common two-minute detour, because messages live on the state while conditions live on the event, so a condition field will not be found on a state.
- **Thinking a scenario is special** obscures the fact that it is a process like an automation, and once that lands, nesting needs no further explanation.
- **Resizing a slot and expecting the process to stretch** confuses slot geometry with process duration, which are separate; Lesson 04 covers the modifier that changes which one you are editing.
- **Reading `lesson:/level` as a file path** misses that it is `device:/parameter`, in which the part before the colon is a device name, and Lesson 08 covers the suffixes that can follow.

## Exercise

Take the paragraph you wrote for the Lesson 00 exercise and rewrite it using only the eight words defined here. Where your description needs something these words cannot express, write that down as a question, because inventing a term hides the gap that the question would expose.

**Success criterion:** every element of your project maps to one of score, interval, state, event, trigger, process, slot, or device. Keep your list of unanswerable questions, since [Lesson 15]({{ site.baseurl }}/learn/15-triggers.html) and [Lesson 16]({{ site.baseurl }}/learn/16-conditions-and-branching.html) resolve most of them, and a question still open at the end of Module F should be reported as described in [Lesson 38]({{ site.baseurl }}/learn/38-reading-the-docs.html).

## Going further

- [Glossary]({{ site.docs_baseurl }}/reference-manual/references/glossary.html) holds the project's own definitions, which you should compare with the ones above.
- [What is *score*]({{ site.docs_baseurl }}/quick-start/what-is-score.html) covers the same ground at a higher altitude.
- [Execution]({{ site.docs_baseurl }}/in-depth/execution.html) describes how these objects behave once the playhead is running.
