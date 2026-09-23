---
layout: default
title: "Lesson 14: Finding the right process in the library"
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

# Lesson 14: Finding the right process in the library

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 13]({{ site.baseurl }}/learn/13-mapping-and-scaling.html), because its conditioning chain is the example this lesson keeps returning to.
>
> **You will need** the process library open, `Ctrl+Shift+P`, and a blank page to write on.
>
> **You will build** a decision table you keep, with an intent on the left and the process that serves it on the right.

## Why this matters

The installation ships well over a hundred processes, which is at once the software's greatest practical strength and its most reported difficulty. The usability study found that people spend significant time hunting for what they need, that some category and object names do not match users' mental organisation, and that the search works on object names while users think in use cases. In other words, the software's breadth is only an advantage to a reader who can find things in it, and the study's recommendation was to improve the search and the descriptions; until that lands, the working solution is a reader who knows the families.

This lesson therefore teaches a way of looking things up instead of a list to memorise, because you will not remember a hundred names. However, you can remember five families and the two questions that lead you to one of them, and that is what the rest of this lesson builds.

## Concepts

### Library sections by domain

The library is grouped by domain, whereas this lesson sorts it by verb. Top-level sections cover control, audio, visuals, monitoring, structure, and scripting, and within control the two sections you will use constantly are `Mappings` and `Data Processing`, from Lesson 13.

### Two questions that locate a process

Two questions locate almost any process: what kind of value you hold, and what should happen to it. Most searches resolve quickly once you ask what type of value you are holding, which may be a number, an array, a texture, an audio signal, or a MIDI (Musical Instrument Digital Interface) stream, and then whether you want to *generate*, *transform*, *route*, *combine*, or *observe* it, because the intersection of the two answers is nearly always one family.

### The five families

The five verbs generate, transform, route, combine, and observe are the families. They repay internalising because they cut across every value type, so that the same question applies to a number and to a texture:

- **Generate** produces a value from parameters alone, as an LFO (low-frequency oscillator), a step sequencer, a path generator, the array generators, noise, and shaders with no input all do.
- **Transform** takes one value in and sends one out, changed, which covers the mapping curve, smooth, range filter, rate limiter, math expressions, audio effects, and image filters.
- **Route** sends the same value elsewhere or selects among destinations, which is what matrix and spatialisation objects, switches, and object filters do.
- **Combine** takes several values in and sends one out, as the array combiner, mixers, spatialisation matrices, and pattern combiners do.
- **Observe** makes a value visible without altering it, which is the role of the signal display, the LED view, the monitoring processes, and the message log.

## The decision table

Keep this table, extend it as you go, and note the family as well as the object, since the family is what transfers to the next problem.

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

The last row matters as much as the others, because when no process fits, a script is a legitimate answer, and Module J is about writing one. However, what you should not do is force a mapping curve into being a state machine.

## Walkthrough: five searches, done properly

![The process library filtered by a search, showing the Control and Mappings families]({{ site.img }}/14/14-01-library-search.png)

The figure shows the library filtered by four characters, which is enough to reveal the `Control > Mappings` family with the objects Lesson 13 used and a good deal more besides.

For each of the following, find the process before reading the answer, using the two questions instead of the search box, so that the method is tested instead of your memory of the table.

1. **"A sensor sends values a hundred times a second and my receiver stutters."** The value is a number and the verb is transform, applied to the frequency of the values instead of their size, so the answer is the rate limiter, because it caps how often values pass while leaving each value unchanged.
2. **"I want to see whether my envelope follower is producing any output at all."** The verb is observe, so the answer is a signal display inserted after the envelope follower, which shows its output over time without changing it.
3. **"I have three arrays of red, green, and blue values and need one interleaved array for a strip."** The value is an array and the verb is combine, so the answer is the array combiner in intersperse mode, which takes the three arrays in and sends one interleaved array out.
4. **"The projection should pulse in time with the piece instead of at a fixed rate."** The verb is generate, with tempo awareness added, so the answer is an LFO inside an interval carrying its own musical metrics, which Lesson 24 explains.
5. **"When the sensor is out of range, the output should freeze instead of jumping to the bound."** The verb is transform, in its discarding form, so the answer is a range filter set to reject instead of clamp, because in reject mode no value passes at all, which is what freezing means.

Now do the same for three problems from your own project, and write the results into your table, so that the table starts to describe your work and not only this course.

## Reading a process you have never used

An unfamiliar process yields to four moves taken in order, and they work for any of the hundred-plus in the library.

**Press `F1` first**, because contextual help opens that process's reference page, which is the fastest route to an answer. Nevertheless, it is the most underused of the four moves, which is why it comes first here.

**Read its ports**, since their names and types tell you most of what it does; a process with an array in and an array out is doing something structural, whereas one with a float in and a float out is conditioning.

**Drop it in and watch it** with an observe process on its output, because ten seconds of playing tells you more than the page did.

**Check the user library**, where many objects ship with presets, and a preset is a worked example of what the author expected the object to be used for.

The third move scales from one object to a whole chain, since observation is more than a debugging aid. When a chain misbehaves, inserting an *observe* process at each stage answers faster than reasoning about it, because a signal display between two objects settles in seconds what an argument settles in minutes, and that is the most useful practice this lesson offers.

## Building your own vocabulary

The decision table is a start, whereas what accumulates over a career is a personal library of saved chains, which is easier to build from now than to reconstruct at the end of a project.

**Save chains as well as objects.** The calibrate-filter-map-smooth chain from Lesson 13 is four objects you will assemble dozens of times, and saved as a fragment with `Alt+Drag` it becomes one gesture that carries your tuning decisions with it.

**Name each fragment for its intent**, because `sensor-conditioning-jittery` tells you when to reach for it. In contrast, `chain-3` tells you only that two others came before it, and since you are the person who will search your own library, the name is its index.

**Keep the failures for a while**, because a fragment that did not work, named for why, reminds you the second time you have the same idea that you tried it. Furthermore, that reminder is information you do not otherwise retain, since a discarded fragment leaves no trace.

**Revisit the library sections quarterly**, since processes are added between releases and packages add more; ten minutes browsing the two `Control` sections after an update regularly surfaces an object that would have saved a previous project an afternoon.

## Common mistakes

- **Searching by the name you would have chosen**, when the search matches the author's names; search by family instead, or browse the two `Control` sections.
- **Reaching for a script too early**, although a mapping curve, a range filter, and a combiner cover an enormous amount of ground and are visible to collaborators in a way a script is not.
- **Reaching for a script too late**, because twelve chained utility objects imitating a formula are worse than four lines of code.
- **Not observing intermediate values**, which is where most of the time lost in this software goes.
- **Ignoring `F1`**, which answers the question you have about the object you are holding.
- **Building the same small chain repeatedly** instead of saving it to the user library as a fragment, per Lesson 05.

## Exercise

Write your decision table with at least twelve rows, of which at least four come from your own project instead of from the table above. For three of the twelve, drop the process into a score, put an observe process on its output, and confirm in ten seconds of playback that it does what you assumed.

**Success criterion:** every row names a family as well as an object, and you found at least one case where the process you assumed was wrong. Moreover, that case is the value of the exercise, because it is where the method corrected your memory.

## Going further

- [The process reference]({{ site.docs_baseurl }}/processes.html), the complete list, which is best read as a map instead of front to back.
- [Data processing]({{ site.docs_baseurl }}/common-practices/12-data-processing.html) and [LED design]({{ site.docs_baseurl }}/common-practices/13-led-design.html), two worked pipelines that use many of these families together.
- [The user library]({{ site.docs_baseurl }}/reference-manual/panels/) for presets and your own saved fragments.
- [The package manager]({{ site.docs_baseurl }}/in-depth/package-manager.html), because some families arrive as installable packages.

{% include lesson_files.html %}
