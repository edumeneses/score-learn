---
layout: default
title: "Lesson 02: Vocabulary of a score"
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

# Lesson 02: Vocabulary of a score

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 01]({{ site.baseurl }}/learn/01-install.html); you need *score* installed to open the file.
>
> **You will need** `lesson-00.score`, the document you read in Lesson 00. Open it now.
>
> **You will build** a vocabulary you can use for the rest of the course without ambiguity, and the reflex of confirming a term in the inspector.

## Why this matters

This lesson defines eight words. That sounds like a poor use of twelve minutes until you notice what the usability study found: interviewees said, in their own words, that they leave parts of the interface alone because they do not know what those parts are for, and one named triggers specifically as an unfamiliar concept. Both are vocabulary problems wearing the costume of interface problems. A reader who cannot name what they are looking at cannot search for it, cannot press `F1` usefully on it, and cannot ask a precise question about it.

Every definition below is checkable. Open `lesson-00.score`, click the object, and read the inspector on the right. That loop, click and confirm, is the actual skill this lesson teaches; the definitions are its content.

## Concepts

**Score.** The document. One `.score` file, one score. It contains a single root **interval** which contains everything else, plus the declarations of the devices the document expects. When people say "my score", they mean this file, and Lesson 05 covers what travels with it.

**Interval.** A stretch of time. It has a start, a duration, and contents. The word replaces several you may be carrying: it is not a track, not a clip, and not a region, because it can contain other intervals, and because its duration may be a range rather than a number. In `lesson-00.score`, `Approach`, `Bright`, and `Dark` are intervals, and so is the outermost bar named `lesson-00` that holds them.

**State.** What happens at a single instant: a set of messages to send, each one an address paired with a value. In the interface a state is drawn as a small disc on a vertical line. Click one in `lesson-00.score` and the inspector lists its messages as a tree. A state with no messages is still meaningful, because it is where intervals attach.

**Event.** The thing a state sits on, and the thing that can carry a **condition**. Several events can share one instant, and that is precisely how a branch is written: each outgoing event carries a different condition, and the ones whose conditions hold are the ones that fire. Most of the time you interact with states and let events stay implicit; you need the distinction the moment you write a branch, in Lesson 16.

**Trigger.** A property of an instant: instead of firing when the playhead arrives, it *waits*. Something must trigger it, a mouse click, a value from a device, a condition becoming true. The interface draws it as a T-shaped marker above the state, and it draws the preceding interval's duration as a dashed line, because that duration is now open-ended. `lesson-00.score` has exactly one, labelled `waits for /lesson/go`.

**Process.** Anything that produces or transforms values inside an interval. Automations, sound file players, MIDI readers, shaders, scripts, and whole sub-scenarios are all processes. Two consequences are worth stating now: a process always lives inside a stretch of time, and a scenario is itself a process, which is why intervals can nest without any special mechanism.

**Slot.** The horizontal band an interval gives a process so it can be drawn and edited. One interval can hold several processes, so it can have several slots, and slots can be stacked so that several automations share one band. The distinction between a process and its slot matters when you resize things: dragging a slot's edge changes how much room the drawing gets, which is not the same as changing how long the process runs.

**Device and address.** A device is the outside world as *score* sees it: a piece of software or hardware, reachable over some protocol, exposing a tree of named parameters. An address names one parameter in the form `device:/path/to/parameter`, for example `lesson:/level`. Addresses are how the score refers to the world without knowing what the world is, and Lesson 06 is entirely about that separation.

## The relations, in one paragraph

A **score** contains one root **interval**. An interval contains **processes**, each drawn in a **slot**, and among those processes may be scenarios, which contain more intervals. Intervals are bounded by **states**, which sit on **events**, which sit at instants; an instant may be a **trigger**, and an event may carry a **condition**. States hold messages, each message pairing an **address** with a value, and every address belongs to a **device**. Learn that paragraph and the interface stops being a set of unfamiliar shapes.

## Walkthrough: confirm each word in the inspector

Open `lesson-00.score` and work down the list. For each step, click the object and read the right-hand panel before moving on.

![One instant of a score, zoomed: a state on its event, and the trigger marker above it]({{ site.img }}/02/02-01-instant.png)

The figure zooms on one instant of `lesson-00.score`, with the two objects that are easiest to confuse marked: the **state**, step 5 below, and the **trigger** on the instant it sits at, step 7.

1. **The root interval.** Click the outermost horizontal bar. The inspector shows its duration and its name, `lesson-00`. Note that it has a duration at all: the document is an interval like any other.
2. **A nested interval.** Click `Approach`. Confirm that the inspector describes an interval, and that its contents include a scenario, `Scenario.10`, which in turn holds `Shutter`. Three levels, one mechanism.
3. **A process.** Click the slot header reading `Automation (float).2 -> lesson:/level`. The inspector now describes an automation: its address, and the minimum and maximum it drives between. This is the moment to notice that a process's destination is a property of the process, not of the interval.
4. **A slot against a process.** With that automation selected, look at how it is drawn: the band is the slot, the curve is the process. `Ctrl+Alt+F` folds an interval's processes, `Ctrl+Alt+U` unrolls them. The processes did not change; their slots did.
5. **A state.** Click the disc at the very start of the timeline. The inspector lists a message: `lesson:/level` set to `0`. That is a cue, and Lesson 09 does nothing but this.
6. **An event and its condition.** Select the state at the start of `Bright`. Its event carries a condition on `lesson:/level`. Note that the condition belongs to the event, while the message belongs to the state, even though the interface draws them close together.
7. **The trigger.** Select the instant labelled `waits for /lesson/go` and confirm the T marker in the inspector. Press `T` with a state selected to toggle a trigger; do it, look, and undo.
8. **The device.** In the `Device explorer` on the left, expand `lesson`. Its three parameters, `level`, `colour`, and `shutter`, are the addresses every automation and message in this document refers to.

## The same words, inside the file

Because a `.score` file is JSON, as [Lesson 05]({{ site.baseurl }}/learn/05-saving-and-reopening.html) covers, every word defined above has a written counterpart you can search for. Opening `lesson-00.score` in a text editor and searching for these strings is a fast way to confirm that the vocabulary is the software's own and not this course's invention.

| Word | What to search for in the file |
|---|---|
| Interval | `Scenario::IntervalModel` |
| State | `Scenario::StateModel` |
| Event, with its condition | `Scenario::EventModel`, then `Condition` |
| Trigger, on its instant | `Scenario::TimeSyncModel`, then `Active` and `Expression` |
| Process | the process name, for instance `Automation` |
| Slot | `SmallViewRack` and `FullViewRack` |
| Address | the plain text `lesson:/level` |

Two details in that table are worth pausing on. A trigger is not an object of its own: it is the `Active` flag on an instant, which is exactly why Lesson 00 described a trigger as a property rather than a thing. And a slot appears twice, once for the compact view and once for the full view, because an interval can be drawn two ways without changing what runs.

## Common mistakes

- **Using "track" for interval.** It costs you the two properties that matter: nesting, and elastic duration.
- **Conflating state and event.** Messages live on the state; conditions live on the event. Looking for a condition field on a state is a common two-minute detour.
- **Thinking a scenario is special.** It is a process like an automation. Once that lands, nesting needs no further explanation.
- **Resizing a slot and expecting the process to stretch.** Slot geometry and process duration are separate. Lesson 04 covers the modifier that changes which one you are editing.
- **Reading `lesson:/level` as a file path.** It is `device:/parameter`. The part before the colon is a device name, and Lesson 08 covers the suffixes that can follow.

## Exercise

Take the paragraph you wrote for the Lesson 00 exercise and rewrite it using only the eight words defined here. Where your description needs something these words cannot express, write that down as a question rather than inventing a term.

**Success criterion:** every element of your project maps to exactly one of score, interval, state, event, trigger, process, slot, or device. Keep your list of unanswerable questions: [Lesson 15]({{ site.baseurl }}/learn/15-triggers.html) and [Lesson 16]({{ site.baseurl }}/learn/16-conditions-and-branching.html) resolve most of them, and anything still open at the end of Module F is worth reporting as described in [Lesson 38]({{ site.baseurl }}/learn/38-reading-the-docs.html).

## Going further

- [Glossary]({{ site.docs_baseurl }}/reference-manual/references/glossary.html), the project's own definitions; compare them with the ones above.
- [What is *score*]({{ site.docs_baseurl }}/quick-start/what-is-score.html) for the same ground at a higher altitude.
- [Execution]({{ site.docs_baseurl }}/in-depth/execution.html), for how these objects behave once the playhead is running.
