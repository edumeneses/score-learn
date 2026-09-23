---
layout: default
title: "Lesson 11: LFOs, step sequencers, and other modulation sources"
description: "LFOs, step sequencers, interpolators, and path generators: movement that is described rather than drawn, and the nodal view where it gets patched."
parent: Lessons
nav_order: 13
unit: "11"
permalink: /learn/11-modulation-sources.html
score_version: "3.8.2"
reading_time: "13 min"
practice_time: "25 min"
score_file: none
---

# Lesson 11: LFOs, step sequencers, and other modulation sources

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 10]({{ site.baseurl }}/learn/10-automation-curves.html), which covered movement you draw.
>
> **You will need** a device with at least two float parameters.
>
> **You will build** a small patch in which one generator drives several destinations, together with a working understanding of the nodal view.

## Why this matters

A drawn curve specifies what happens without saying why, which is right for a fade and wrong for movement that should keep going, such as a flicker, a slow drift, or a pulse locked to tempo. Movement of that kind is better described than drawn, because a description has parameters you can change in one place, whereas a drawing has a shape you must redraw.

Furthermore, this lesson introduces the **nodal view**, which is the other half of the software, since the lessons so far have placed things in time and this one connects them. Generators are where patching starts to pay, because their output usually needs to be shaped before it arrives anywhere, and that shaping happens in a chain of small objects that the timeline itself cannot express.

## Concepts

### Generators and automations

A generator produces values continuously from parameters, whereas an automation is a value over its interval. A generator has a rate, a depth, and a waveform, so changing the rate changes the whole behaviour with no drawing to redo.

### The LFO

The LFO (low-frequency oscillator) is the generator you will use most. It has a waveform, a frequency, an amplitude, and an offset, and its parameters are ports, which means each of them can itself be automated or driven by something else; that is the idea this whole module is built on.

### The step sequencer

The step sequencer steps through a list of values at a rate. An LFO produces a continuous waveform that passes through every intermediate value. In contrast, a step sequencer is discrete, which suits movement that should change in defined amounts, such as a lighting chase, a pattern of positions, or a sequence of states.

### Interpolators and path generators

Interpolators and path generators handle values on demand and trajectories. An **interpolator** moves between values on demand and not on a clock, whereas a **path generator** produces a trajectory, following a drawn line or a circular or spiral figure, and it exists because positions are the most common thing you want moving continuously. Module G uses it for spatialisation and Module I for placing images.

### Ports and cables

Every input and output is a port, and compatible ports connect with a cable. A generator's output is a port and a destination's input is a port, so any port can be connected to any compatible port. The consequence, which takes a moment to accept, is that the interesting part of your work often has no timeline in it at all.

### Tempo-locked generators

Tempo awareness comes automatically to processes that can use musical metrics. LFOs are among them, so if an interval carries its own tempo and signature, a generator inside it follows them, which is how a pulse stays locked to a piece and does not drift against it. [Lesson 24]({{ site.baseurl }}/learn/24-tempo-and-sync.html) is the full treatment.

## The nodal view, and why it exists

The switch between temporal and nodal views is at the bottom of the window, and it shows the same document two ways: in the temporal view you see what happens when, whereas in the nodal view you see what feeds what. However, some processes only ever appear in the nodal view, and there is a principle behind which ones, because a process whose effect does not depend on where you are in time, audio effects and generators in particular, has no useful shape to draw on a timeline.

Patching is fast because of three interactions, all of which work by double-clicking in the process library instead of dragging:

- **With a cable selected**, double-clicking a process inserts it into that cable.
- **With an input port or control selected**, double-clicking a process connects the new process's output into that port. If that port had an address, the address moves to the new process's input, which is the refactoring you want when inserting a mapping in front of something.
- **With a whole process selected**, double-clicking connects the new process after it, by first port, which is how effect chains get built quickly.

Additionally, a newly created process is left selected, so chains can be built without returning to the score between steps, and when the patching is done and the cables are in the way, `Alt+Shift+G` hides them.

## Walkthrough: one generator, three destinations

![An automation feeding an LFO's frequency, whose output passes through two conditioning objects]({{ site.img }}/11/11-01-lfo-patch.png)

The figure shows the patch this walkthrough builds, and its slot header reads `Automation (float).2 -> Freq. (LFO)` because dropping the LFO onto a selected process connected it automatically, which is the interaction described above.

1. **Make an interval and put an LFO in it**, taking the LFO from the process library at `Ctrl+Shift+P`.
2. **Address its output** to one of your parameters and play, so that the parameter oscillates; that oscillation is the point of arrival, reached in two steps.
3. **Automate the LFO's rate** by right-clicking the rate port and creating an automation, as Lesson 10's fourth route described. You now have a drawn curve controlling a described movement, which is the combination that justifies having both.
4. **Switch to the nodal view** and find your LFO, its ports, and the cable to its destination, which are the same objects seen from the other side.
5. **Insert a mapping in front of the destination** by selecting the destination port and then double-clicking a mapping process in the library. The address moves to the mapping's input and a cable appears, which is the refactoring described above, done in one gesture.
6. **Fan out** by connecting the LFO's output to a second and third destination, each through its own scaling, so that one movement drives three things differently.
7. **Add a step sequencer beside it** and drive a fourth destination, so that you can compare continuous and discrete movement in the same document.
8. **Hide the cables** with `Alt+Shift+G` and adjust the controls, which is what the view is for once the structure is settled.
9. **Make it run indefinitely**, since a patch only runs while its interval is running. Give the interval's end a trigger that is never satisfied, and the patch keeps going for as long as the score plays, which is how a *score* document behaves like a Max or Pure Data patch when you want it to.

## The pattern behind all of this

The working method of this whole module combines three ideas, which deserve stating as a pattern because the modules from G onward reuse it.

**A generator produces movement from parameters.** It has no knowledge of your piece, because it produces a shape from its parameters alone.

**A conditioning chain adapts the movement to its destination.** Scaling, offsetting, filtering, and limiting shape the movement for where it is going. Moreover, they do so in objects that you can read and change, whereas arithmetic done in your head leaves no trace in the document.

**An automation controls the generator over the course of the piece.** The parameters of the generator are themselves ports, so a drawn curve can decide how the described movement evolves.

That third layer is what makes the combination expressive instead of mechanical, because a pulse whose rate is constant is a metronome, whereas a pulse whose rate is drawn over ninety seconds is a shape that no single object in the library provides. In other words, you are not choosing between drawing and describing; you are describing the local behaviour and drawing its evolution.

The corollary works as a diagnostic in both directions: if you find yourself drawing something repetitive, you are missing a generator, and if you find yourself with a generator whose settings you keep adjusting by hand during rehearsal, you are missing an automation on one of its ports.

## Common mistakes

- **Expecting a generator to run outside its interval** ignores that every process runs inside time, so the trigger trick in step 9 is the idiom for "forever".
- **Drawing what an LFO would describe** costs four times the work for four cycles, and the result cannot be changed as a whole.
- **Automating depth when you meant offset** moves the value around the wrong point, because an LFO's amplitude and its centre are separate ports.
- **Forgetting that ports are automatable** hides the most useful modulation in a piece, which is often a curve on a generator's parameter and not on the destination.
- **Patching in the temporal view** is possible and cramped, so switch views.
- **Leaving cables visible** while adjusting controls leads to mis-clicking a cable in place of a knob.

## Exercise

Build a patch in which one LFO drives three destinations, each shaped differently: one directly, one inverted, and one scaled to a small range around a fixed offset. Then automate the LFO's rate from a drawn curve so that the movement accelerates over twenty seconds, and make the whole patch run for as long as the score plays.

**Success criterion:** all three destinations move from one generator; the rate visibly changes over the twenty seconds; and the patch keeps running past the end of the interval you built it in. If you had to draw any repeating shape by hand, find the generator that would have described it.

## Going further

- [The LFO process]({{ site.docs_baseurl }}/processes/lfo.html) and [the step sequencer]({{ site.docs_baseurl }}/processes/step.html) are the reference pages for the two generators used here.
- [Path generator]({{ site.docs_baseurl }}/processes/path-generator.html) and [interpolator]({{ site.docs_baseurl }}/processes/interpolator.html) cover the other two families.
- [The modular workflow]({{ site.docs_baseurl }}/in-depth/modular.html) is the reference for every interaction in this lesson.
- [Musical metrics]({{ site.docs_baseurl }}/in-depth/musical.html) covers tempo-locked modulation.
