---
layout: default
title: "Lesson 32: Pure Data patches inside score"
description: "Host an existing patch, map its inlets and outlets to ports, and decide what belongs in the patch and what belongs in the score."
parent: Lessons
nav_order: 38
unit: "32"
permalink: /learn/32-puredata.html
score_version: "3.8.2"
reading_time: "13 min"
practice_time: "25 min"
score_file: none
---

# Lesson 32: Pure Data patches inside score

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 31]({{ site.baseurl }}/learn/31-faust.html).
>
> **You will need** Pure Data installed and one patch, ideally one you already use.
>
> **You will build** a document that hosts a patch, drives it from the timeline, and reads values back out of it.

## Why this matters

A great deal of existing work in this field is Pure Data patches, and a great many practitioners have twenty years of them. Hosting rather than rewriting is therefore the pragmatic path: the patch keeps working, and *score* provides what a patch has never had, which is time structure.

That combination is the interesting part, and it is worth naming as a division of labour. A patch is very good at signal processing and very poor at saying "this happens for twelve seconds, then that happens when the performer is ready". A score is the reverse. Putting the two together plays to both, and Lesson 00's positioning table said exactly this: *score* can host your patch, and the patch does not need a time structure of its own any more.

## Concepts

**A patch becomes a process.** Add the Pure Data process, point it at a patch file, and it appears in the score like any other process, with its own place in an interval and its own ports.

**Inlets and outlets map to ports.** The patch's inlets and outlets become the process's ports, which is what makes the whole thing work: everything you know about ports applies. A patch inlet can be driven by an automation, by a mapping, by a sensor through the pipeline of Lesson 13; a patch outlet can drive a device parameter or another process.

**The patch is a referenced file.** Like a sound file, per Lesson 05, it is pointed at rather than embedded. It travels with the project directory and it must be found at the path you stored, which makes patch files subject to the same portability discipline as media.

**Pure Data must be present.** Hosting a patch is a dependency on the machine, in the sense Lesson 21 described for plug-ins. It belongs in your technical page.

**Audio and control both cross the boundary.** A patch can process audio inside a *score* audio chain, and it can exchange control values. Both directions work, and mixing them in one patch is normal.

## Walkthrough: host, drive, and read back

{: .note }
> A figure for this lesson is pending: it needs a patch file and the hosted process's ports, which requires interaction and a patch this course does not ship. See `checks/32-puredata.md`.

1. **Prepare a small patch first.** Not your most complex one: a patch with two inlets and one outlet, doing something audible, so that every step of this walkthrough is verifiable. Save it in your project directory.
2. **Add the Pure Data process** in an interval and point it at the patch.
3. **Find its ports.** Confirm that the patch's inlets and outlets appear on the process. If a port you expected is missing, the patch's declaration is where to look.
4. **Drive one inlet from an automation.** Right-click the port, create an automation, draw a curve, and play. The patch is now under the timeline's control.
5. **Drive a second inlet from your bench**, through the conditioning pipeline from Lesson 13, so a live input reaches the patch already scaled and smoothed.
6. **Read an outlet.** Cable the patch's outlet to a device parameter, or to a signal display so you can watch it, and confirm values leave the patch.
7. **Put audio through it.** If your patch processes signal, cable a sound file into it and its output onward, per Lesson 21. Watch for propagation, which the cable removed.
8. **Now use the timeline.** Put the patch's interval inside a structure with a trigger, so the patch runs only during one section, and stops when the section ends. That is the capability the patch did not have on its own.
9. **Make it run indefinitely** instead, with the never-satisfied trigger idiom from Lesson 11, and note that the patch now behaves exactly as it did standing alone, which is a useful baseline.
10. **Move the project** and reopen it, to confirm the patch path survived, exactly as you did with media in Lesson 05.
11. **Write down the dependency**: Pure Data, its version, and any externals the patch needs.

## Where to draw the line

The productive question is not whether to use a patch but *what belongs in it*. Three guidelines, learned by everyone who has done this.

**Signal processing belongs in the patch.** If it is a filter, a granulator, a physical model you have refined over years, leave it where it is. Rewriting it in another language is a project, not a step.

**Time structure belongs in the score.** Anything that is "then", "until", "when", or "for twelve seconds" should be *score*'s job. A patch that contains its own sequencing is fighting the host, and the symptoms are subtle: two clocks that drift, a patch that cannot be rehearsed from the middle, a piece that cannot be stopped cleanly.

**Parameters belong at the boundary.** Expose everything you might want to change as an inlet, even if you currently set it inside the patch. An exposed parameter is automatable, mappable, and recordable; an internal one is invisible to the score.

The refactoring this implies is usually small: delete the patch's sequencing, expose its constants as inlets, and let the score decide when and how much. What you get back is rehearsability, cue-based structure, and everything else this course has been about.

## Two ecosystems, one document

The wider point of this lesson generalises beyond Pure Data, and it is worth stating because it applies to Faust, to plug-ins, and to any script.

*score* is unusual in how many other systems it will host: patches, Faust code, shaders written for other tools, plug-ins in several formats, JavaScript, and compiled C++. That is a deliberate position, and it has a consequence for how you should plan a project. You do not have to choose an ecosystem. You can keep twenty years of patches, use a shader from a public collection, host the one plug-in whose sound you need, and write the glue in a few lines of script, all in one document that has a time structure.

The discipline this requires is the one this lesson describes: each hosted thing should do the job it is good at, and *score* should own the time. When that boundary is respected, a document assembled from four ecosystems is coherent. When it is not, you have four systems each with an opinion about when things happen, and debugging it means holding all four in your head at once.

A last observation about maintenance. A hosted patch is a second file that has to be versioned, backed up, and kept in step with the score that drives it. Treat the pair as one artefact: they belong in the same project directory, they should be committed together, and a change to the patch's inlets is a change to the score's interface, which is exactly the kind of thing that breaks silently six months later.

## Common mistakes

- **Hosting a patch that contains its own sequencer.** Two time systems, and neither is in charge.
- **Parameters buried inside the patch.** If it is not an inlet, the score cannot touch it.
- **A patch path outside the project directory.** Same failure as media, same fix.
- **Forgetting the dependency.** Pure Data and its externals must exist on the machine.
- **Expecting the patch's own interface.** You are hosting the processing, not the window; drive it through ports.
- **Testing with your most complex patch.** Start small, confirm the boundary works, then scale up.
- **Losing the dry signal** when cabling audio through, which is Lesson 19's propagation behaviour again.

## Exercise

Take a patch you already use that contains some form of sequencing, and refactor it: remove the sequencing, expose at least three internal constants as inlets, and rebuild the timing in *score* with an interval structure and one trigger. Then drive one of the new inlets from an automation and one from your bench.

**Success criterion:** the piece behaves as it did before, can now be rehearsed from the middle, and stops cleanly. Write one sentence on what the patch got worse at, if anything: an honest answer here is more useful than a claim that hosting is free.

## Going further

- [Pure Data integration]({{ site.docs_baseurl }}/in-depth/puredata.html) and [the Pure Data process]({{ site.docs_baseurl }}/processes/puredata.html).
- [The Pure Data integration example]({{ site.docs_baseurl }}/examples/audio/pd-integration.html), worth opening before building your own.
- [Media management]({{ site.docs_baseurl }}/in-depth/media.html) for path resolution, which applies to patch files.
- [Audio routing]({{ site.docs_baseurl }}/in-depth/audio-routing.html) for the propagation behaviour when a patch is in an audio chain.
