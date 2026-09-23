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

> **Before this lesson** finish [Lesson 31]({{ site.baseurl }}/learn/31-faust.html), because the idea that a hosted script exposes ports carries directly into this one.
>
> **You will need** Pure Data installed and one patch. If you have none to hand, `lesson-32.pd` ships with this lesson with an audio inlet and outlet, one control inlet named `gain`, and one control outlet named `level`, which is the smallest patch that makes the port mapping visible.
>
> **You will build** a document that hosts a patch, drives it from the timeline, and reads values back out of it.

## Why this matters

A great deal of the work in this field exists as Pure Data patches, and a great many practitioners have twenty years of them. Hosting a patch is therefore the pragmatic path, whereas rewriting it would discard work that already functions; the patch keeps working, and *score* provides what a patch has lacked, which is time structure.

That combination is the interesting part of the lesson, and it amounts to a division of labour. A patch is good at signal processing and poor at saying that this happens for twelve seconds and then that happens when the performer is ready, whereas a score expresses that timing directly and leaves signal processing to whatever it hosts. In other words, putting the two together plays to both, which is what Lesson 00's positioning table claimed: *score* can host your patch, and the patch no longer needs a time structure of its own.

## Concepts

### Hosted patches as processes

A patch becomes a process once it is hosted. You add the Pure Data process, point it at a patch file, and it appears in the score like any other process, with its own place in an interval and its own ports.

### Annotated receives as ports

Annotated receives and sends become the ports, whereas the patch's `inlet` and `outlet` objects do not. The natural guess is that inlets and outlets map to ports, and that guess is wrong; *score* reads the patch and creates a control port for every **receive** carrying its annotations:

```
r $0-gain @type float @range 0 1 @default 1
```

gives a `gain` control inlet with that range and default. A matching `s $0-name` send becomes an outlet, and `adc~` and `dac~` give the audio inlet and outlet. What you know about ports then applies, so that a control port can be driven by an automation, by a mapping, or by a sensor through the pipeline of Lesson 13.

### Audio and control across the boundary

Audio and control both cross the boundary. A patch can process audio inside a *score* audio chain, and it can exchange control values. Moreover, mixing the two in one patch is normal, since both directions work at once.

## Walkthrough: host, drive, and read back

![A hosted Pure Data patch as a process, with an audio inlet, an audio outlet, and a gain control derived from the patch]({{ site.img }}/32/32-01-hosted-patch.png)

1. **Prepare a small patch first, and not your most complex one**, so that every step of this walkthrough is verifiable: one control in, one control out, and audio through. The shipped `lesson-32.pd` is that patch, and its whole content is these six objects:

   ```
   adc~                                          audio in
   *~ 1                                          scaled by the control
   dac~                                          audio out
   r $0-gain @type float @range 0 1 @default 1    becomes a control inlet
   env~                                          follows the level
   s $0-level @type float                        becomes a control outlet
   ```

   Compare it with the `3band.pd` preset that ships in *score*'s default package, which declares four controls the same way.
2. **Add the Pure Data process in an interval and point it at the patch**, which is the whole of the hosting step.
3. **Find its ports, and confirm that `gain` appears as a control on the process** alongside the audio inlet and outlet, as in the figure. If a port you expected is missing, the patch's *annotation* is where to look, because a receive without `@type` is not a port.

   A consequence follows from how the ports are stored: the port list lives **in the document**, and *score* does not re-read the patch when the document opens. Adding a control to the patch therefore means re-selecting it in the inspector so that the ports are derived again, and a document hand-edited to point at a different patch keeps the old ports until you do.
4. **Drive one inlet from an automation** by right-clicking the port, creating an automation, drawing a curve, and playing, so that the patch is now under the timeline's control.
5. **Drive a second inlet from your bench**, through the conditioning pipeline from Lesson 13, so that a live input reaches the patch already scaled and smoothed.
6. **Read an outlet by cabling it to a device parameter**, or to a signal display so that you can watch it, and confirm that values leave the patch.
7. **Put audio through it if your patch processes signal**, by cabling a sound file into it and its output onward, per Lesson 21, and watch for propagation, which the cable removed.
8. **Use the timeline by putting the patch's interval inside a structure with a trigger**, so that the patch runs only during one section and stops when the section ends, which is the capability the patch did not have on its own.
9. **Conversely, make it run indefinitely with the never-satisfied trigger idiom from Lesson 11**, and note that the patch now behaves as it did standing alone, which is a useful baseline.
10. **Move the project and reopen it**, to confirm that the patch path survived, as you did with media in Lesson 05.

    {: .warning }
    > **The patch is a referenced file, like a sound file.** As Lesson 05 described for media, it is pointed at and not embedded, so it travels with the project directory and must be found at the path you stored, which makes patch files subject to the same portability rules as media.

11. **Write down the dependency**, which means Pure Data, its version, and any externals the patch needs.

    {: .warning }
    > **Pure Data must be present on the machine.** Hosting a patch is a dependency on the machine, in the sense Lesson 21 described for plug-ins, and it therefore belongs in your technical page.

## Where to draw the line

The productive question is not whether to use a patch but what belongs inside it, and the answer divides the work into signal processing, time structure, and the parameters that connect them.

**Signal processing belongs in the patch.** If it is a filter, a granulator, or a physical model you have refined over years, leave it where it is, because rewriting it in another language is a project and not a step.

**Time structure belongs in the score.** Whatever is a matter of then, until, when, or for twelve seconds should be *score*'s job, because a patch that contains its own sequencing is fighting the host, and the symptoms are subtle: two clocks that drift, a patch that cannot be rehearsed from the middle, and a piece that cannot be stopped cleanly.

**Parameters belong at the boundary.** Expose every value you might want to change as an inlet, even if you currently set it inside the patch, since an exposed parameter is automatable, mappable, and recordable, whereas an internal one is invisible to the score.

Nevertheless, the refactoring this implies is usually small, because it consists of deleting the patch's sequencing, exposing its constants as inlets, and letting the score decide when and how much. What you get back is rehearsability, cue-based structure, and the rest of what this course has been about.

## Two ecosystems, one document

The wider point of this lesson generalises beyond Pure Data, and it deserves to be stated because it applies to Faust, to plug-ins, and to any script.

*score* is unusual in how many other systems it will host: patches, Faust code, shaders written for other tools, plug-ins in several formats, JavaScript, and compiled C++. That breadth is a considered position, and it has a consequence for how you should plan a project, because you do not have to choose an ecosystem. You can keep twenty years of patches, use a shader from a public collection, host the one plug-in whose sound you need, and write the glue in a few lines of script, all in one document that has a time structure.

However, the requirement this places on you is the one this lesson describes: each hosted component should do the job it is good at, and *score* should own the time. When that boundary is respected, a document assembled from four ecosystems is coherent, whereas when it is not, you have four systems each with an opinion about when things happen, and debugging it means holding all four in your head at once.

Additionally, maintenance deserves a word, since a hosted patch is a second file that has to be versioned, backed up, and kept in step with the score that drives it. Treat the pair as one artefact: they belong in the same project directory, they should be committed together, and a change to the patch's inlets is a change to the score's interface, which is the kind of change that breaks silently six months later.

## Common mistakes

- **Hosting a patch that contains its own sequencer** produces two time systems with neither in charge.
- **Parameters buried inside the patch** stay out of reach, because if a value is not an annotated receive, the score cannot touch it.
- **A patch path outside the project directory** is the same failure as media outside it, with the same fix.
- **Forgetting the dependency** means Pure Data and its externals may be missing on the machine that has to run the piece.
- **Expecting the patch's own interface** misreads what hosting does, since you are hosting the processing and not the window, and you drive it through ports.
- **Testing with your most complex patch** hides which side of the boundary a problem is on; start small, confirm that the boundary works, then scale up.
- **Losing the dry signal** when cabling audio through is Lesson 19's propagation behaviour appearing again.

## Exercise

Take a patch you already use that contains some form of sequencing, and refactor it by removing the sequencing, exposing at least three internal constants as inlets, and rebuilding the timing in *score* with an interval structure and one trigger. Then drive one of the new inlets from an automation and one from your bench, so that the patch is driven from the timeline and from a live input.

**Success criterion:** the piece behaves as it did before, can now be rehearsed from the middle, and stops cleanly. Write one sentence on what the patch got worse at, if it did, because a candid answer here is more useful than a claim that hosting is free.

## Going further

- [Pure Data integration]({{ site.docs_baseurl }}/in-depth/puredata.html) and [the Pure Data process]({{ site.docs_baseurl }}/processes/puredata.html), which together cover the hosting mechanism and the process reference.
- [The Pure Data integration example]({{ site.docs_baseurl }}/examples/audio/pd-integration.html), which is the document to open before building your own.
- [Media management]({{ site.docs_baseurl }}/in-depth/media.html) for path resolution, which applies to patch files as much as to media.
- [Audio routing]({{ site.docs_baseurl }}/in-depth/audio-routing.html) for the propagation behaviour when a patch sits in an audio chain.
