---
layout: default
title: "Lesson 11: Modulation sources"
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

# Lesson 11: Modulation sources

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 10]({{ site.baseurl }}/learn/10-automation-curves.html), which covered movement you draw.
>
> **You will need** a device with at least two float parameters.
>
> **You will build** a small patch in which one generator drives several destinations, and a working understanding of the nodal view.

## Why this matters

A drawn curve says exactly what happens and nothing about why. That is right for a fade and wrong for anything that should keep going: a flicker, a slow drift, a pulse locked to tempo. Those are better described than drawn, because a description has parameters you can change in one place, and a drawing has a shape you must redraw.

This lesson is also your introduction to the **nodal view**, which is the other half of the software. Everything so far has been temporal: things placed in time. Generators are where patching starts to pay, because their output usually wants to be shaped before it arrives anywhere, and that shaping is a chain of small objects rather than a property of the timeline.

## Concepts

**Generator against automation.** An automation is a value over its interval. A generator produces values continuously from parameters: a rate, a depth, a waveform. Change the rate and the whole behaviour changes; there is nothing to redraw.

**The LFO.** A low-frequency oscillator: a waveform, a frequency, an amplitude, an offset. It is the workhorse. Its parameters are ports, which means each of them can itself be automated or driven by something else, and that is the idea this whole module is built on.

**The step sequencer.** A list of values stepped through at a rate. Where an LFO is continuous, a step sequencer is discrete, which suits anything that should change in defined amounts: a lighting chase, a pattern of positions, a sequence of states.

**Interpolators and paths.** An **interpolator** moves between values on demand rather than on a clock. A **path generator** produces a trajectory, following a drawn line or a circular or spiral figure, and it exists because positions are the most common thing you want moving continuously. Module G uses it for spatialisation and Module I for placing images.

**Everything is a port.** A generator's output is a port; a destination's input is a port; and any port can be connected to any compatible port with a cable. The consequence, which takes a moment to accept, is that the interesting part of your work often has no timeline in it at all.

**Tempo awareness.** Processes that can use musical metrics do so automatically, LFOs among them. If an interval carries its own tempo and signature, a generator inside it follows them, which is how a pulse stays locked to a piece rather than drifting against it. [Lesson 24]({{ site.baseurl }}/learn/24-tempo-and-sync.html) is the full treatment.

## The nodal view, and why it exists

The switch between temporal and nodal views is at the bottom of the window, and it shows **the same document** two ways. In the temporal view you see what happens when; in the nodal view you see what feeds what. Some processes only ever appear in the nodal view, and there is a principle behind which ones: anything whose effect does not depend on where you are in time, audio effects and generators in particular, has nothing useful to draw on a timeline.

Three interactions make patching fast, and all three work by double-clicking in the process library rather than dragging:

- **With a cable selected**, double-clicking a process inserts it into that cable.
- **With an input port or control selected**, double-clicking a process connects the new process's output into that port. If that port had an address, the address moves to the new process's input, which is exactly the refactoring you want when inserting a mapping in front of something.
- **With a whole process selected**, double-clicking connects the new process after it, by first port. This is how effect chains get built quickly.

A newly created process is left selected, so chains can be built without returning to the score between steps. When the patching is done and the cables are in the way, `Alt+Shift+G` hides them.

## Walkthrough: one generator, three destinations

{: .note }
> A figure for this lesson is pending: it needs a patch assembled in the nodal view, which requires interaction. See `checks/11-modulation-sources.md`.

1. **Make an interval and put an LFO in it.** From the process library, `Ctrl+Shift+P`.
2. **Address its output** to one of your parameters and play. A parameter that oscillates: the point of arrival, quickly.
3. **Automate the LFO's rate.** Right-click the rate port and create an automation, as Lesson 10's fourth route described. You now have a drawn curve controlling a described movement, which is the combination that makes both worth having.
4. **Switch to the nodal view.** Find your LFO, its ports, and the cable to its destination. Nothing changed; you are looking at the same objects from the other side.
5. **Insert a mapping in front of the destination.** Select the destination port, then double-click a mapping process in the library. Note what happens to the address: it moves to the mapping's input, and a cable appears. That is the refactoring described above, done in one gesture.
6. **Fan out.** Connect the LFO's output to a second and third destination, each through its own scaling, so that one movement drives three things differently.
7. **Add a step sequencer beside it** and drive a fourth destination, so you can compare continuous and discrete movement in the same document.
8. **Hide the cables** with `Alt+Shift+G` and adjust the controls. This is what the view is for once the structure is settled.
9. **Make it run indefinitely.** A patch only runs while its interval is running. Give the interval's end a trigger that is never satisfied, and the patch keeps going for as long as the score plays, which is how a *score* document behaves like a Max or Pure Data patch when you want it to.

## The pattern behind all of this

Three ideas combine into the working method of this whole module, and they are worth stating as a pattern because everything from Module G onward reuses it.

**A generator produces movement.** It knows nothing about your piece; it produces a shape from parameters.

**A conditioning chain adapts it.** Scaling, offsetting, filtering, limiting: the movement is shaped for its destination, and it is shaped in objects rather than in your head.

**An automation controls the generator.** The parameters of the generator are themselves ports, so a drawn curve can decide how the described movement evolves over the piece.

That third layer is what makes the combination expressive rather than mechanical. A pulse whose rate is constant is a metronome; a pulse whose rate is drawn over ninety seconds is a shape that no single object in the library provides. You are not choosing between drawing and describing; you are describing the local behaviour and drawing its evolution.

The corollary is worth keeping: if you find yourself drawing something repetitive, you are missing a generator. If you find yourself with a generator whose settings you keep adjusting by hand during rehearsal, you are missing an automation on one of its ports.

## Common mistakes

- **Expecting a generator to run outside its interval.** Everything runs inside time. The trigger trick in step 9 is the idiom for "forever".
- **Drawing what an LFO would describe.** Four cycles hand-drawn is four times the work and cannot be changed as a whole.
- **Automating depth when you meant offset.** An LFO's amplitude and its centre are separate ports, and confusing them produces movement around the wrong point.
- **Forgetting that ports are automatable.** The most useful modulation in a piece is often a curve on a generator's parameter, not on the destination.
- **Patching in the temporal view.** It is possible and cramped. Switch views.
- **Leaving cables visible** while adjusting controls, then mis-clicking a cable instead of a knob.

## Exercise

Build a patch in which one LFO drives three destinations, each shaped differently: one directly, one inverted, and one scaled to a small range around a fixed offset. Automate the LFO's rate from a drawn curve so the movement accelerates over twenty seconds. Then make the whole patch run for as long as the score plays.

**Success criterion:** all three destinations move from one generator; the rate visibly changes over the twenty seconds; and the patch keeps running past the end of the interval you built it in. If you had to draw any repeating shape by hand, find the generator that would have described it.

## Going further

- [The LFO process]({{ site.docs_baseurl }}/processes/lfo.html) and [the step sequencer]({{ site.docs_baseurl }}/processes/step.html).
- [Path generator]({{ site.docs_baseurl }}/processes/path-generator.html) and [interpolator]({{ site.docs_baseurl }}/processes/interpolator.html).
- [The modular workflow]({{ site.docs_baseurl }}/in-depth/modular.html), which is the reference for every interaction in this lesson.
- [Musical metrics]({{ site.docs_baseurl }}/in-depth/musical.html) for tempo-locked modulation.
