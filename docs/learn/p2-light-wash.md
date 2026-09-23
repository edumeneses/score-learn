---
layout: default
title: "Milestone P2: one fader drives a light wash"
description: "Drive a group of fixtures from a single control through Art-Net, with snapshots at both ends and a software receiver so no hardware is needed."
parent: Lessons
nav_order: 11
unit: "P2"
permalink: /learn/p2-light-wash.html
score_version: "3.8.2"
reading_time: "15 min"
practice_time: "45 min"
score_file: p2-light-wash/p2-solution.score
---

# Milestone P2: one fader drives a light wash

{% include lesson_meta.html %}

> **Before this milestone** finish Lessons 06 to 09, because this unit introduces no new technique and relies on those four lessons.
>
> **You will need** a software Art-Net receiver, or any DMX (Digital Multiplex) visualiser that listens on the network; no lighting hardware is required.
>
> **You will build** a lighting look driven from one control, with a captured start state, a captured end state, and a channel map written down before the timeline is touched.

## Why this matters

Module C taught you devices, addresses, types, ranges, and cues in the abstract, and lighting is where those five subjects stop being abstract, because a lighting rig punishes every one of the mistakes those lessons warned about. Channels are integers, ranges run from 0 to 255, and a fixture often assigns one channel to discrete modes, so that a value on it selects a behaviour where you expected to set an intensity. A wrong range therefore does not produce a subtle error; it produces a fixture that strobes when you asked it to fade.

Furthermore, this milestone is the first time you build against a protocol that cannot describe itself and cannot answer back, since an Art-Net device sends and does not report. What you learned about testing from the device explorer, and about the thirty-second diagnosis in Lesson 07, is what makes a silent protocol tractable, and the brief below leans on each of those lessons in turn.

## The brief

Build a document that:

1. declares an **Art-Net device** and a **channel map** that you wrote down before touching the timeline;
2. drives **at least four fixtures**, or four channel groups, from **one control value**;
3. **captures a start state and an end state** instead of typing values, per Lesson 09;
4. respects each channel's **real range**, with the conversion done in one place only, per Lesson 08;
5. runs for a **fixed duration** with one transition between the two looks;
6. is verified against a **software receiver**, with a screenshot or a log line proving that the channels moved.

## Concepts you are assembling

### Raw Art-Net channels

An Art-Net device created without fixture definitions exposes the raw DMX channels, plus a whole-device message. That rawness is an advantage while learning, because you see what a channel is with no fixture definition interpreting it for you, so the range and meaning of each channel are yours to establish and write down.

### The channel map

A channel map records, for every channel, its universe, its number, what it controls, its range, and what is unsafe. It is written down outside *score*, per Lesson 06, because the document holds the declaration whereas the reasoning behind each value has no place in the device tree, and the reasoning is what a collaborator, or a later version of you, will need.

### Fan-out from one control

Driving many destinations from one control is the central problem of this milestone. There are three defensible ways to do it, and choosing one on purpose is the exercise: a separate automation per channel, all reading the same shape; a single automation into a mapping that fans out; or a single address written with a pattern so that one curve reaches several channels at once.

### Address pattern matching

Pattern matching lets *score* send one value to many addresses at once. An address such as `dmx:/fixture/*/intensity` reaches every fixture's intensity. Additionally, patterns support alternatives, `{foo,boo}`, numeric ranges, `foo.{5..23}`, character classes, `foo[1-5]`, and a recursive form, `device://intensity`. For a wash, where every fixture does the same thing, a pattern is the shortest correct answer, although the section on fan-out below explains what it cannot express.

## Walkthrough: the reference solution

![One interval holding four automations, one per channel group, with captured states at both ends]({{ site.img }}/p2/p2-01-light-wash.png)

`p2-solution.score` ships with this milestone, and it uses an OSC (Open Sound Control) device in place of Art-Net so that it runs for readers with no receiver installed; the structure is identical, and the exercise below asks you to rebuild it against Art-Net.

1. **Write the channel map before you open the timeline**, listing four groups with one channel each, a range of 0 to 255, and a note that channel 5 on your imaginary fixture is a mode channel which must not be faded.
2. **Declare an Art-Net device with no fixture definitions**, so that the device explorer shows raw channels and the map you wrote is the only description of what they mean.
3. **Capture the opening look** by setting the channels from the device explorer until the receiver shows what you want, then selecting them and dragging them onto the timeline at zero.
4. **Add a twenty-second interval holding a single automation** whose destination is a pattern reaching all four groups, with a minimum of 0 and a maximum of 255 set once on that automation.
5. **Capture the closing look** at the end of the interval, so that the document ends in a defined condition instead of wherever the curve happened to stop.
6. **Play, and watch the receiver**, where all four channels should move together from the captured start to the captured end.
7. **Break one thing on purpose** by setting the automation's maximum back to 1 and playing again. The channels then move by one part in 255, which is the failure Lesson 08 described, and seeing it once where the consequence is visible makes the range check below meaningful.

## Choosing where the fan-out happens

The three approaches to fan-out differ less in what they cost now than in what they cost later, when the rig grows or one fixture needs to differ, and that difference is the lesson of this milestone.

**A separate automation for each channel is explicit and immediately readable.** However, it scales badly, because forty fixtures mean forty curves to edit whenever the shape changes, and curves edited separately drift out of agreement.

**A single automation into a mapping lets the curve exist once while the mapping decides how each destination responds.** In contrast to a curve per channel, it is the right answer when the fixtures should *not* all do the same thing, as in a wash where the outer fixtures come up later than the centre, and [Lesson 13]({{ site.baseurl }}/learn/13-mapping-and-scaling.html) is the full treatment.

**A single automation addressed through a pattern is the shortest solution when every destination does the same thing.** Nevertheless, it cannot express a difference between individual fixtures, so the moment one of them needs to differ you are back to one of the other two approaches.

Pick one, write down why in your channel map, and do not mix two of them for the same set of fixtures, because a collaborator needs a single place to look for the fan-out.

## How to know it is finished

- The receiver shows all four channels moving, and their values reach 0 and 255 at the ends of the curve, whereas values that stop at 1 leave the rig dark.
- The document plays twice in a row identically, because the captured start state resets every channel before the curve begins.
- The channel map exists as a text file beside the score, and it names the mode channel you must not fade.
- The conversion from the curve's 0-to-1 space to 0-to-255 happens in a single place, and you can say which place that is.
- Folding the intervals with `Ctrl+Alt+F` leaves a structure that a collaborator can read.

## Why lighting punishes sloppy ranges

Lighting is the first destination in this course that is unforgiving, and naming why matters because the same care with ranges transfers to every destination after it.

A sound that is 1 part in 255 too quiet is inaudible and harmless, whereas a light at 1 out of 255 is off. Furthermore, a fixture sent a value on a channel that encodes a mode does something categorical: it strobes, it changes colour wheel position, or it resets. In other words, there is no graceful degradation, because the value is either in the range the fixture expects for the behaviour you want or it produces a different behaviour entirely.

The practical consequence is that the channel map stops being paperwork and becomes the one document that prevents a mistake you cannot see coming. Write it before the score, keep it beside the score, and record for each channel not only its range but what happens outside that range, since that second column is what stops a fade on a mode channel.

## Common mistakes

- **Leaving the range at 0 to 1** is the single most likely reason a rig appears dead, because the highest value the curve can then reach is one part in 255.
- **Fading a mode channel** happens because fixtures use channels for discrete behaviours as well as for intensities, and the channel map is what stops you from doing it.
- **Assuming that Art-Net confirms a value** misreads a protocol that does not report back; an empty value column is expected, and the receiver is your only ground truth.
- **Typing the looks instead of capturing them** ignores that lighting looks are judged by eye, so set them, look at the receiver, and then snapshot.
- **Sending to a whole device by accident** is possible because a raw Art-Net device accepts a message to the device itself, which writes every channel at once; that is useful when intended and alarming when it is not.
- **Assuming a single universe** fails when the four groups live in different universes, and the map is where each group's universe is recorded.

## Exercise

Rebuild the reference against a real Art-Net device and a software receiver, and then extend it in one of two directions.

Either **make the wash asymmetric**, so that the outer groups reach full intensity one second after the centre, using a mapping in place of four hand-edited curves.

Or **make it operable** by adding a second interval that returns every channel to the opening look, and a state at the end of the score that sets all channels to zero, so that stopping the score cannot leave a light on. [Lesson 18]({{ site.baseurl }}/learn/18-cues-and-transport.html) explains why the last state of a score is special.

**Success criterion:** the receiver shows the intended movement, the score ends dark, and your channel map matches what the document sends. If you used a pattern, write down what would break if one fixture needed a different curve, because that note tells you when to move to the mapping approach.

## Going further

- [The Art-Net device]({{ site.docs_baseurl }}/devices/artnet-device.html) for fixture definitions and universes.
- [LED design]({{ site.docs_baseurl }}/common-practices/13-led-design.html), which takes this much further with array tools and shader-driven pixels.
- [Pattern matching]({{ site.docs_baseurl }}/in-depth/pattern-matching.html) for the full address syntax.
- [Data processing]({{ site.docs_baseurl }}/common-practices/12-data-processing.html), the bridge into Module E.
