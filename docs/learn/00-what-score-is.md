---
layout: default
title: "Lesson 00: What score is, and what it is not"
description: "Where ossia score sits among Max, Pure Data, QLab, TouchDesigner, and a DAW, and which of your existing habits will transfer."
parent: Lessons
nav_order: 0
unit: "00"
permalink: /learn/00-what-score-is.html
score_version: "3.8.2"
reading_time: "12 min"
practice_time: "none"
score_file: 00-what-score-is/lesson-00.score
---

# Lesson 00: What *score* is, and what it is not

{% include lesson_meta.html %}

> **Before this lesson** nothing is required. This is the first unit of the course.
>
> **You will need** a web browser. *score* is installed in [Lesson 01]({{ site.baseurl }}/learn/01-install.html), not here.
>
> **You will build** a written map of your own project onto the five building blocks *score* gives you.

## Why this matters

Almost nobody arrives at *ossia score* without previous tools. You have patched in Max or Pure Data, cued a show in QLab, built a generative sketch in TouchDesigner or Processing, or produced a fixed piece in a digital audio workstation. Those habits are an asset, and they are also the reason the first hour with *score* can be frustrating: the software borrows a little from each of those families and then organises the result around a premise none of them share. The usability study conducted at the Société des Arts Technologiques found that respondents praised the software's versatility and stability while naming the learning curve as its least appreciated aspect, and the interviews traced much of that curve to unexamined expectations rather than to missing features.

This lesson therefore does no clicking. It establishes what *score* is for, which of your reflexes transfer, and which will mislead you, so that every subsequent lesson lands on a mental model that already fits.

## Concepts

**Intermedia sequencer.** *score* sequences heterogeneous material on a shared timeline: sound files, video, MIDI, Open Sound Control (OSC) messages, DMX and Art-Net lighting, gamepad and sensor input, plug-ins, and scripts. The word *intermedia* is doing real work here. The software has no privileged medium, no mixer at the centre, and no assumption that the thing being scored is music.

**The two paradigms it combines.** Most tools in this space pick one of two organising ideas. A timeline places events in time and plays them back. A dataflow graph connects producers to consumers and lets values circulate. *score* is built on both at once: a hierarchical, non-linear timeline whose contents are dataflow graphs. Reaching for one and finding the other is the single most common source of early confusion, and it is why the interface offers a temporal view and a nodal view of the same score.

**Flexible time.** In a linear sequencer, a duration is a number. In *score*, an interval can declare a minimum, a nominal, and a maximum duration, and the event ending it can wait for a condition, such as an incoming OSC message, a sensor threshold, or an operator's key press. The score is therefore a *structure of possible timings* rather than a single fixed rendering. This is the premise the other tools do not share, and everything distinctive about *score* follows from it.

**The five building blocks.** Five nouns account for almost every object you will meet: the **score** (the document), the **interval** (a stretch of time that can contain processes and other intervals), the **state** and its **event** and **trigger** (what happens at an instant, and the condition that decides when that instant arrives), the **process** (anything that produces or transforms values inside an interval, including automations, sound file players, shaders, and scripts), and the **device** (the outside world, addressed as a tree of named parameters). [Lesson 02]({{ site.baseurl }}/learn/02-vocabulary.html) defines each one precisely against the interface.

**Free software, several platforms.** *score* is free and open-source, and runs on Linux, both desktop and embedded, macOS, and Windows, with a web version in development. Nothing in this course depends on a paid component, and the extension mechanisms in Phase 3 are available to you on the same terms as to the people who wrote the software.

## Where *score* sits

| If you come from | What transfers | What will mislead you |
|---|---|---|
| **Max, Pure Data** | The dataflow reflex: signals and messages travelling between objects; the habit of building small utilities | A patch has no time structure of its own. In *score* the graph lives inside a stretch of time that starts, ends, loops, or waits. Asking "where is my main patcher window" has no good answer |
| **A digital audio workstation** | Timeline literacy: playhead, regions, automation lanes | There is no mixer at the centre and no track model. Audio is one kind of process among many, routing is explicit, and a region's duration may be a range rather than a number |
| **QLab** | Cue thinking: discrete, named, operator-fired steps | Cues in *score* are recallable states inside a running structure, not a flat list. Conversely, a *score* score can run unattended, with conditions rather than an operator deciding what happens next |
| **Isadora, TouchDesigner** | Node graphs, GPU pipelines, real-time media | Those tools are predominantly graphs that run continuously. *score* asks you to say *when* each part of the graph exists, which is more work up front and far less work when the piece has a dramaturgy |
| **Processing, openFrameworks, code** | Precision, version control, the reflex to script | You will look for a main loop. There is none: *score* schedules processes, and Phase 3 shows how to put your code inside one rather than around it |
| **Ableton Live, session-view improvisation** | Loops and clips launched by hand | Looping in *score* is a property of an interval, applied to anything, and interaction is a condition on an event rather than a clip launch quantised to a grid |

Two summary statements are worth memorising. *score* **is** the right tool when a work has a temporal shape that is neither fixed nor absent: an installation that waits for a visitor, a performance whose sections are cued live, a museum piece that runs for eight hours with branches. *score* is **not** the right tool when you want a signal-processing patch with no time structure, in which case a Max or Pure Data patch is simpler and *score* can host it later, or when you want a fixed stereo master, in which case a workstation will get you there faster.

## Walkthrough: read a score before touching one

The figure below is a small finished score, `lesson-00.score`, which ships with this lesson. Find each numbered element in turn; you are learning to read the notation before you write it. You cannot open the file yet, and that is deliberate: reading comes first.

![An annotated ossia score document showing a timeline with nested intervals, automations, a trigger, and two conditional branches]({{ site.img }}/00/00-01-annotated-score.png)

1. **The timeline and its direction.** Time runs left to right, and the ruler at the top reads in minutes and seconds. Everything else hangs off that axis.
2. **Nested intervals.** The interval named `Approach` holds a second scenario, `Scenario.10`, which holds an interval of its own, `Shutter`. Intervals contain intervals: this hierarchy is how a score gets sections, and it is why there is no flat track list.
3. **A process inside an interval.** The red curve is an automation, one kind of process. Note that it lives *inside* a stretch of time, not on a lane beside it, and that it is exactly as long as the interval holding it.
4. **States, on events.** The small circles on the vertical lines are states. Values are sent at those instants. The vertical line itself is the instant, shared by everything that happens there.
5. **The trigger.** This instant carries a distinct marker and a label, `waits for /lesson/go`. It does not fire at a fixed time; it waits. Everything after it therefore has a range of possible start times rather than one.
6. **The branch.** Two intervals, `Bright` and `Dark`, leave that same instant. Each is guarded by a condition on the value of `lesson:/level`, so exactly one of them runs. A linear reading of this document is impossible, which is precisely the point.
7. **Where the outside world appears.** Each automation's slot header names its destination, in the form `device:/parameter`, here `lesson:/colour`. The score writes values to names; what those names are attached to, a piece of software or a piece of hardware, is configured once and separately, in [Lesson 06]({{ site.baseurl }}/learn/06-device-model.html). The device itself, `lesson`, is listed in the panel on the left.

Now look at the same document the other way. Nothing about the file changed; only the view did.

![The same document drawn as a node graph, the root scenario containing its intervals as nested nodes]({{ site.img }}/00/00-02-nodal-view.png)

1. **The root scenario, as one node**, containing the same intervals you just read as a timeline. This is the second of the two paradigms named above, and the button that switches between them sits at the bottom left of the window. Lesson 03 finds it, and Lesson 11 is where the graph view starts to earn its place.

## Common mistakes

- **Looking for a mixer, a track list, or a master output.** None of the three is the centre of *score*. Audio routing is explicit and is covered in [Lesson 19]({{ site.baseurl }}/learn/19-audio-setup.html).
- **Treating devices as tracks.** A device is not a destination lane; it is a namespace. The same address can be written from anywhere in the score, and the usability study identifies this separation as one of the two concepts newcomers most often misread.
- **Assuming a duration is a number.** It may be a range. Reading a score as if it had one fixed length will make triggers look broken when they are working.
- **Expecting the nodal view to be a different document.** The temporal and nodal views show the same score. Switching between them changes nothing but your vantage point, and [Lesson 04]({{ site.baseurl }}/learn/04-first-process.html) covers how to get back.
- **Dismissing triggers as an advanced feature.** They are the reason the software exists. Postponing them produces a linear score that a workstation would have written faster.

## Exercise

Write one paragraph, in plain language and with no reference to software, describing a work you actually want to make. Then annotate your own paragraph: mark every element as a score, an interval, a state, a process, or a device.

**Success criterion:** every noun in your description receives exactly one mark, or you can name precisely what refused to be marked. Keep that list. Bring it to [Lesson 02]({{ site.baseurl }}/learn/02-vocabulary.html), and check it again after [Lesson 15]({{ site.baseurl }}/learn/15-triggers.html); anything still unmarked at that point is worth raising as a documentation issue, which [Lesson 38]({{ site.baseurl }}/learn/38-reading-the-docs.html) shows how to file.

## Going further

- [What is *score*]({{ site.docs_baseurl }}/quick-start/what-is-score.html), the project's own one-page positioning statement.
- [Interface overview]({{ site.docs_baseurl }}/quick-start/interface-overview.html), which Lesson 03 walks through in detail.
- [Execution]({{ site.docs_baseurl }}/in-depth/execution.html), for readers who want the scheduling model now rather than in Phase 3.
- The [examples library]({{ site.docs_baseurl }}/examples/), reachable from the *score* start screen; browsing it before Lesson 01 costs nothing.
