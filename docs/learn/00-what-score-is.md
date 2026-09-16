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

> **Before this lesson** no preparation is required, because this is the first unit of the course.
>
> **You will need** only a web browser, since *score* is installed in [Lesson 01]({{ site.baseurl }}/learn/01-install.html) and this unit involves no clicking.
>
> **You will build** a written map of your own project onto the five objects from which every *score* document is assembled.

## Why this matters

Most readers arrive at *ossia score* carrying habits formed in other tools: you have patched in Max or Pure Data, cued a show in QLab, built a generative sketch in TouchDesigner or Processing, or produced a fixed piece in a digital audio workstation. Those habits are an asset, and they are also the reason the first hour with *score* can be frustrating, because the software borrows a little from each of those families and then organises the result around a premise that none of them share. The usability study conducted at the Société des Arts Technologiques found that respondents praised the software's versatility and stability while naming the learning curve as its least appreciated aspect, and the interviews traced much of that curve to unexamined expectations rather than to missing features.

This lesson therefore involves no clicking, and instead establishes what *score* is for, which of your reflexes transfer, and which will mislead you, so that every subsequent lesson lands on a mental model that already fits.

## Concepts

**An intermedia sequencer places heterogeneous material on one shared timeline.** In *score* that material includes sound files, video, MIDI (Musical Instrument Digital Interface) data, Open Sound Control (OSC) messages, DMX (Digital Multiplex) and Art-Net lighting, gamepad and sensor input, plug-ins, and scripts. The word *intermedia* carries a precise meaning here, because the software has no privileged medium, no mixer at the centre, and no assumption that the material being scored is music.

**The software combines two paradigms that most tools keep apart.** Most tools in this space pick one of two organising ideas: a timeline places events in time and plays them back. In contrast, a dataflow graph connects producers to consumers and lets values circulate, and *score* is built on both at once, as a hierarchical, non-linear timeline whose contents are dataflow graphs. Reaching for one and finding the other is the single most common source of early confusion, which is why the interface offers a temporal view and a nodal view of the same score.

**In a linear sequencer, a duration is a fixed number.** However, an interval in *score* can declare a minimum, a nominal, and a maximum duration, while the event ending it can wait for a condition, such as an incoming OSC message, a sensor threshold, or an operator's key press. The score is therefore a *structure of possible timings* rather than a single fixed rendering, and this is the premise the other tools do not share; the features that distinguish *score* follow from it.

**Five nouns account for almost every object you will meet in the interface.** They are the **score** (the document), the **interval** (a stretch of time that can contain processes and other intervals), the **state** and its **event** and **trigger** (what happens at an instant, and the condition that decides when that instant arrives), the **process** (any object that produces or transforms values inside an interval, including automations, sound file players, shaders, and scripts), and the **device** (the outside world, addressed as a tree of named parameters). [Lesson 02]({{ site.baseurl }}/learn/02-vocabulary.html) defines each one precisely against the interface.

**The software is free and open-source, and it runs on several platforms.** Those platforms are Linux, both desktop and embedded, macOS, and Windows, with a web version in development. No part of this course depends on a paid component. Moreover, the extension mechanisms in Phase 3 are available to you on the same terms as to the people who wrote the software.

## Where *score* sits

| If you come from | What transfers | What will mislead you |
|---|---|---|
| **Max, Pure Data** | The dataflow reflex: signals and messages travelling between objects; the habit of building small utilities | A patch has no time structure of its own. In *score* the graph lives inside a stretch of time that starts, ends, loops, or waits. Asking "where is my main patcher window" has no good answer |
| **A digital audio workstation** | Timeline literacy: playhead, regions, automation lanes | There is no mixer at the centre and no track model. Audio is one kind of process among many, routing is explicit, and a region's duration may be a range rather than a number |
| **QLab** | Cue thinking: discrete, named, operator-fired steps | Cues in *score* are recallable states inside a running structure, not a flat list. Conversely, a *score* score can run unattended, with conditions rather than an operator deciding what happens next |
| **Isadora, TouchDesigner** | Node graphs, GPU pipelines, real-time media | Those tools are predominantly graphs that run continuously. *score* asks you to say *when* each part of the graph exists, which is more work up front and far less work when the piece has a dramaturgy |
| **Processing, openFrameworks, code** | Precision, version control, the reflex to script | You will look for a main loop. There is none: *score* schedules processes, and Phase 3 shows how to put your code inside one rather than around it |
| **Ableton Live, session-view improvisation** | Loops and clips launched by hand | Looping in *score* is a property of an interval, applied to anything, and interaction is a condition on an event rather than a clip launch quantised to a grid |

The table reduces to a pair of statements about fit. *score* **is** the right tool when a work has a temporal shape that is neither fixed nor absent: an installation that waits for a visitor, a performance whose sections are cued live, a museum piece that runs for eight hours with branches. In contrast, *score* is **not** the right tool when you want a signal-processing patch with no time structure, in which case a Max or Pure Data patch is simpler and *score* can host it later, or when you want a fixed stereo master, in which case a workstation will get you there faster.

## Walkthrough: read a score before touching one

The figure below shows a small finished score, `lesson-00.score`, which ships with this lesson. Find each numbered element in turn, because you are learning to read the notation before you write it; you cannot open the file yet, since *score* is installed in the next lesson.

![An annotated ossia score document showing a timeline with nested intervals, automations, a trigger, and two conditional branches]({{ site.img }}/00/00-01-annotated-score.png)

1. **The timeline runs left to right**, and the ruler at the top reads in minutes and seconds, so that every other element in the figure hangs off that axis.
2. **Intervals nest inside intervals**, which is how a score gets sections. The interval named `Approach` holds a second scenario, `Scenario.10`, which holds an interval of its own, `Shutter`, and this hierarchy is the reason the interface has no flat track list.
3. **A process lives inside an interval**, and the red curve is one kind of process, an automation, which sits *inside* a stretch of time and is therefore precisely as long as the interval that holds it.
4. **States sit on the vertical lines as small circles**, and values are sent at those instants; the vertical line itself is the instant, which is shared by every object placed there.
5. **The trigger waits instead of firing at a fixed time.** This instant carries a distinct marker and a label, `waits for /lesson/go`, and it does not fire when the playhead arrives; it waits. Every element after it therefore has a range of possible start times, whereas a fixed timeline would give each of them one.
6. **The branch leaves one instant along two paths**, since the intervals `Bright` and `Dark` both leave that same instant, and each is guarded by a condition on the value of `lesson:/level`, so that only one of them runs. In other words, a linear reading of this document is impossible, and that impossibility is the feature the trigger and the conditions provide.
7. **The outside world appears as named addresses** in each automation's slot header, which names its destination in the form `device:/parameter`, here `lesson:/colour`; the score writes values to names. However, the software or hardware those names are attached to is configured once and separately, in [Lesson 06]({{ site.baseurl }}/learn/06-device-model.html); the device itself, `lesson`, is listed in the panel on the left.

Now look at the same document the other way, since the second figure shows the same file drawn as a graph; the file itself did not change between the two figures, although the drawing looks unrelated to the timeline, and only the view differs.

![The same document drawn as a node graph, the root scenario containing its intervals as nested nodes]({{ site.img }}/00/00-02-nodal-view.png)

1. **The root scenario appears as one node** containing the same intervals you just read as a timeline. This is the second of the two paradigms named above, and the button that switches between them sits at the bottom left of the window; [Lesson 11]({{ site.baseurl }}/learn/11-modulation-sources.html) introduces that switch, and it is where the graph view starts to earn its place.

## Common mistakes

- **Looking for a mixer, a track list, or a master output** finds none of the three at the centre of *score*, because audio routing is explicit, as [Lesson 19]({{ site.baseurl }}/learn/19-audio-setup.html) covers.
- **Treating a device as a track** misreads a namespace as a destination lane, whereas the same address can in fact be written from any point in the score; the usability study identifies this separation as one of the two concepts newcomers most often misread.
- **Assuming a duration is a number** ignores that it may be a range, and reading a score as if it had one fixed length will make triggers look broken while they are working as designed.
- **Expecting the nodal view to be a different document** misses that the temporal and nodal views show the same score, so switching between them changes only your vantage point; [Lesson 11]({{ site.baseurl }}/learn/11-modulation-sources.html) introduces the switch and covers how to get back.
- **Dismissing triggers as an advanced feature** postpones the reason the software exists, and a score written without them is a linear score that a workstation would have written faster.

## Exercise

Write one paragraph, in plain language and with no reference to software, describing a work you intend to make. Then annotate your own paragraph by marking every element as a score, an interval, a state, a process, or a device.

**Success criterion:** every noun in your description receives a single mark, or you can name which nouns refused to be marked. Keep that list, bring it to [Lesson 02]({{ site.baseurl }}/learn/02-vocabulary.html), and check it again after [Lesson 15]({{ site.baseurl }}/learn/15-triggers.html); a noun still unmarked at that point indicates a gap in the documentation, which [Lesson 38]({{ site.baseurl }}/learn/38-reading-the-docs.html) shows how to file.

## Going further

- [What is *score*]({{ site.docs_baseurl }}/quick-start/what-is-score.html) is the project's own one-page positioning statement.
- [Interface overview]({{ site.docs_baseurl }}/quick-start/interface-overview.html) is the reference tour of the window, which Lesson 03 walks through in detail.
- [Execution]({{ site.docs_baseurl }}/in-depth/execution.html) describes the scheduling model, for readers who want it before Phase 3 reaches it.
- The [examples library]({{ site.docs_baseurl }}/examples/) is reachable from the *score* start screen, and browsing it before Lesson 01 prepares you for that lesson's exercise.
