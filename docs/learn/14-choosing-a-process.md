---
layout: default
title: "Lesson 14: Choosing the right utility process"
description: "A decision table for the process library: search by intent rather than by name, and know which family answers which question."
parent: Lessons
nav_order: 16
unit: "14"
permalink: /learn/14-choosing-a-process.html
score_version: "3.8.2"
reading_time: "13 min"
practice_time: "15 min"
score_file: none
---

# Lesson 14: Choosing the right utility process

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 13]({{ site.baseurl }}/learn/13-mapping-and-scaling.html).
>
> **You will need** the process library open, `Ctrl+Shift+P`, and a blank page.
>
> **You will build** a decision table you keep: intent on the left, the process that serves it on the right.

## Why this matters

The installation ships well over a hundred processes. That is the software's greatest practical strength and its most reported difficulty: the usability study found that people spend significant time hunting for what they need, that some category and object names do not match users' mental organisation, and that the search works on object names rather than on use cases. The study's recommendation was to improve the search and the descriptions; until that lands, the working solution is a reader who knows the families.

This lesson therefore teaches a lookup habit rather than a list. You will not remember a hundred names. You can remember eight families and one question to ask about each.

## Concepts

**The library is grouped by domain, not by verb.** Top-level sections cover control, audio, visuals, monitoring, structure, and scripting. Within control, the two sections you will use constantly are `Mappings` and `Data Processing`, from Lesson 13.

**Ask what kind of thing, then what it does to it.** Most searches resolve quickly with two questions: what type of value am I holding, a number, an array, a texture, an audio signal, a MIDI stream; and do I want to *generate*, *transform*, *route*, *combine*, or *observe* it? The intersection is nearly always one family.

**Generate, transform, route, combine, observe.** Five verbs, and they are worth internalising because they cut across every value type:

- **generate**: something from nothing, given parameters. LFO, step sequencer, path generator, array generators, noise, shaders with no input.
- **transform**: one in, one out, changed. Mapping curve, smooth, range filter, rate limiter, math expressions, audio effects, image filters.
- **route**: the same value sent elsewhere, or selected among. Matrix and spatialisation objects, switches, object filters.
- **combine**: several in, one out. Array combiner, mixers, spatialisation matrices, pattern combiners.
- **observe**: a value made visible without being altered. Signal display, LED view, monitoring processes, the message log.

**Observation is not a debugging luxury.** The single most useful habit from this lesson: when a chain misbehaves, insert an *observe* process at each stage rather than reasoning about it. A signal display between two objects settles in seconds what an argument settles in minutes.

## The decision table

Keep this, extend it as you go, and note the family rather than only the object.

| When you want to | Reach for | Family |
|---|---|---|
| A repeating movement | LFO, step sequencer | generate |
| A trajectory in space | path generator, 2D spline | generate |
| A number relating to another number | mapping curve, math expressions, Micromap | transform |
| To tame a noisy sensor | calibrator, smooth, range filter, rate limiter | transform |
| To ignore some values entirely | range filter (reject), object filter | transform |
| One value to reach many addresses | address pattern, array combiner | route |
| Many values in one message | array tool, array combiner, array flattener | combine |
| An audio signal's loudness as a number | envelope follower | transform |
| To see a value over time | signal display | observe |
| To see an array as pixels | LED view, point 2D view | observe |
| To position sound in space | DBAP, GBAP, matrix spatialisation | route |
| A texture from code | ISF shader, texture generator, bytebeat | generate |
| To alter MIDI on the way through | MIDI utilities, patternist | transform |
| Behaviour no process covers | JavaScript, C++ JIT, Faust, Pure Data | any |

The last row matters as much as the others. When nothing fits, a script is a legitimate answer and Module J is about it. What you should not do is force a mapping curve into being a state machine.

## Walkthrough: five searches, done properly

{: .note }
> A figure for this lesson is pending: it needs the process library panel with a search in progress, which requires interaction. See `checks/14-choosing-a-process.md`.

For each of the following, find the process before reading the answer, using the two questions rather than the search box.

1. **"A sensor sends values a hundred times a second and my receiver stutters."** Value type: number. Verb: transform, specifically frequency rather than value. Answer: rate limiter.
2. **"I want to see whether my envelope follower is producing anything at all."** Verb: observe. Answer: signal display, inserted after the envelope.
3. **"I have three arrays of red, green, and blue values and need one interleaved array for a strip."** Value type: array. Verb: combine. Answer: array combiner, in intersperse mode.
4. **"The projection should pulse in time with the piece, not at a fixed rate."** Verb: generate, with tempo awareness. Answer: an LFO inside an interval carrying its own musical metrics, per Lesson 24.
5. **"When the sensor is out of range, everything should freeze rather than jump to the bound."** Verb: transform, discarding. Answer: range filter set to reject rather than clamp, so no value passes at all.

Now do the same for three problems from your own project, and write the results into your table.

## Reading a process you have never used

Four moves, in order, and they work for any of the hundred-plus.

**Press `F1`.** Contextual help opens that process's reference page. This is the fastest route and the most underused.

**Read its ports.** Names and types tell you most of what it does. A process with an array in and an array out is doing something structural; one with a float in and a float out is conditioning.

**Drop it in and watch it.** With an observe process on its output, ten seconds of playing tells you more than the page did.

**Check the library.** Many objects ship with presets in the user library, and a preset is a worked example of what the author expected the object to be used for.

## Building your own vocabulary

The decision table is a start, and the thing that actually accumulates is a personal library, which is worth being deliberate about from now rather than at the end of a project.

**Save chains, not only objects.** The calibrate-filter-map-smooth chain from Lesson 13 is four objects you will assemble dozens of times. Saved as a fragment with `Alt+Drag`, it is one gesture, and it carries your tuning decisions with it.

**Name for intent.** `sensor-conditioning-jittery` tells you when to reach for it; `chain-3` does not. The name is the index of your own library, and you are the person who will search it.

**Keep the failures.** A fragment that did not work, named for why, is worth keeping for a while. The second time you have the same idea, you will remember that you tried it, which is information you do not otherwise retain.

**Revisit the library sections quarterly.** Processes are added between releases, and packages add more. Ten minutes browsing the two `Control` sections after an update regularly surfaces an object that would have saved a previous project an afternoon.

## Common mistakes

- **Searching by the name you would have chosen.** The search matches the author's names. Search by family instead, or browse the two `Control` sections.
- **Reaching for a script too early.** A mapping curve, a range filter, and a combiner cover an enormous amount of ground, and they are visible to collaborators in a way a script is not.
- **Reaching for a script too late.** Twelve chained utility objects imitating a formula is worse than four lines of code.
- **Not observing.** Most of the time lost in this software is lost to not looking at intermediate values.
- **Ignoring `F1`.** It answers the exact question you have, about the exact object you are holding.
- **Building the same small chain repeatedly** instead of saving it to the user library as a fragment, per Lesson 05.

## Exercise

Write your decision table with at least twelve rows, of which at least four come from your own project rather than from the table above. For three of the twelve, drop the process into a score, put an observe process on its output, and confirm in ten seconds of playback that it does what you assumed.

**Success criterion:** every row names a family as well as an object, and you found at least one case where the process you assumed was wrong. That case is the value of the exercise.

## Going further

- [The process reference]({{ site.docs_baseurl }}/processes.html), the complete list, best read as a map rather than front to back.
- [Data processing]({{ site.docs_baseurl }}/common-practices/12-data-processing.html) and [LED design]({{ site.docs_baseurl }}/common-practices/13-led-design.html), two worked pipelines that use many of these families together.
- [The user library]({{ site.docs_baseurl }}/reference-manual/panels/) for presets and your own saved fragments.
- [The package manager]({{ site.docs_baseurl }}/in-depth/package-manager.html), because some families arrive as installable packages.
