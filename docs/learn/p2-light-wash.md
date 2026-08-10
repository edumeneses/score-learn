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

> **Before this milestone** finish Lessons 06 to 09. This unit introduces nothing new.
>
> **You will need** a software Art-Net receiver, or any DMX visualiser that listens on the network. No lighting hardware is required.
>
> **You will build** a lighting look driven from one control, with a captured start state, a captured end state, and a documented channel map.

## Why this matters

Module C taught you devices, addresses, types, ranges, and cues in the abstract. Lighting is where those four subjects stop being abstract, because a lighting rig punishes every one of the mistakes those lessons warned about: channels are integers, ranges are 0 to 255, and a fixture often uses one channel for discrete modes rather than for intensity. If your ranges are wrong, you do not get a subtle error; you get a fixture that strobes when you asked it to fade.

The milestone is also the first time you build against a protocol that cannot describe itself and cannot answer back. An Art-Net device sends and does not report. Everything you learned about testing from the device explorer, and about the thirty-second diagnosis in Lesson 07, is what makes this tractable.

## The brief

Build a document that:

1. declares an **Art-Net device** and a **channel map** you wrote down before touching the timeline;
2. drives **at least four fixtures**, or four channel groups, from **one control value**;
3. **captures a start state and an end state** rather than typing values, per Lesson 09;
4. respects each channel's **real range**, with the conversion done in exactly one place, per Lesson 08;
5. runs for a **fixed duration** with one transition between the two looks;
6. is verified against a **software receiver**, with a screenshot or a log line proving the channels moved.

## Concepts you are assembling

**Art-Net as a fixed-shape protocol.** Created without fixture definitions, an Art-Net device exposes the raw DMX channels, plus the ability to send a whole-device message. That rawness is an advantage while learning: you see exactly what a channel is, with nothing interpreting it for you.

**A channel map is documentation, not a formality.** Universe, channel, what it controls, its range, and what is unsafe. Written down outside *score*, per Lesson 06, because the document holds the declaration and not the reasoning.

**One control, many destinations.** The point of the milestone. There are three defensible ways to do it, and choosing deliberately is the exercise: one automation per channel, all reading the same shape; one automation into a mapping that fans out; or one address written with a pattern so that a single curve reaches several channels at once.

**Pattern matching over addresses.** *score* can send one value to many addresses by matching a pattern: `dmx:/fixture/*/intensity` reaches every fixture's intensity. Patterns support alternatives, `{foo,boo}`, numeric ranges, `foo.{5..23}`, character classes, `foo[1-5]`, and a recursive form, `device://intensity`. For a wash, where every fixture does the same thing, this is the shortest correct answer.

## Walkthrough: the reference solution

![One interval holding four automations, one per channel group, with captured states at both ends]({{ site.img }}/p2/p2-01-light-wash.png)

`p2-solution.score` ships with this milestone. It uses an OSC device rather than Art-Net, so that it runs for readers with no receiver installed; the structure is identical and the exercise below asks you to rebuild it against Art-Net.

1. **Write the channel map first.** Four groups, one channel each, 0 to 255, plus a note that channel 5 on your imaginary fixture is a mode channel and must never be faded.
2. **Declare the device.** An Art-Net device with no fixtures, so you get raw channels.
3. **Capture the opening look.** Set the channels from the device explorer until the receiver shows what you want, select them, and drag them onto the timeline at zero.
4. **One interval, one automation.** A twenty-second interval holding a single automation whose destination is a pattern reaching all four groups, with minimum 0 and maximum 255, set once.
5. **Capture the closing look** at the end of the interval, so the document ends in a defined condition rather than wherever the curve stopped.
6. **Play, and watch the receiver.** All four channels should move together, from the captured start to the captured end.
7. **Break one thing on purpose.** Set the automation's maximum back to 1 and play again. The channels move by one part in 255, which is the exact failure Lesson 08 described, and it is worth seeing once in a context where you can see the consequence.

## Choosing where the fan-out happens

The three approaches differ in what they cost you later, which is the real lesson of this milestone.

**Four automations, one per channel.** Explicit and immediately readable. It scales badly: forty fixtures means forty curves to edit whenever the shape changes, and they will drift out of agreement.

**One automation into a mapping.** The curve exists once, and the mapping decides how each destination responds. This is the right answer when the fixtures should *not* all do the same thing: a wash where the outer fixtures come up later than the centre. [Lesson 13]({{ site.baseurl }}/learn/13-mapping-and-scaling.html) is the full treatment.

**One automation, one pattern.** Shortest and exactly right when every destination does the same thing. Its limitation is that it says nothing about individual fixtures, so the moment one of them needs to differ you are back to one of the other two.

Pick one, write down why in your channel map, and do not mix two of them for the same set of fixtures.

## How to know it is finished

- The receiver shows all four channels moving, and their values reach the real bounds, not 0 to 1.
- The document plays twice in a row identically, which the captured start state is what guarantees.
- The channel map exists as a text file beside the score, and it names the mode channel you must not fade.
- The conversion from the curve's 0-to-1 space to 0-to-255 happens in exactly one place, and you can say which.
- Folding the intervals with `Ctrl+Alt+F` leaves a structure a collaborator can read.

## Why lighting punishes sloppy ranges

Lighting is the first destination in this course that is unforgiving, and it is worth naming why so that the habit transfers to everything after it.

A sound that is 1 part in 255 too quiet is inaudible and harmless. A light at 1 out of 255 is off, and a fixture sent a value in a channel that encodes a mode rather than an intensity does something categorical: it strobes, it changes colour wheel position, it resets. There is no graceful degradation. The value is either in the range the fixture expects for the behaviour you want, or it produces a different behaviour entirely.

The practical consequence is that the channel map stops being paperwork and becomes the thing that prevents a mistake you cannot see coming. Write it before the score, keep it beside the score, and record for each channel not only its range but what happens outside that range.

## Common mistakes

- **Leaving the range at 0 to 1.** The single most likely reason a rig appears dead.
- **Fading a mode channel.** Fixtures use channels for discrete behaviours as well as intensities. The channel map is what stops you.
- **Assuming Art-Net confirms anything.** It does not report back. If the value column is empty, that is expected; the receiver is your only ground truth.
- **Typing the looks instead of capturing them.** Lighting looks are judged by eye. Set them, look, then snapshot.
- **Sending to a whole device by accident.** A raw Art-Net device also accepts a message to the device itself, which writes every channel at once. Useful deliberately, alarming otherwise.
- **One universe assumed.** Four groups may live in different universes. The map is where that is recorded.

## Exercise

Rebuild the reference against a real Art-Net device and a software receiver, then extend it in one of two directions.

Either **make the wash asymmetric**: the outer groups reach full intensity one second after the centre, using a mapping rather than four hand-edited curves.

Or **make it operable**: add a second interval that returns everything to the opening look, and add a state at the very end of the score that sets all channels to zero, so that stopping the score cannot leave a light on. [Lesson 18]({{ site.baseurl }}/learn/18-cues-and-transport.html) explains why the last state of a score is special.

**Success criterion:** the receiver shows the intended movement, the score ends dark, and your channel map matches what the document actually sends. If you used a pattern, write down what would break if one fixture needed a different curve.

## Going further

- [The Art-Net device]({{ site.docs_baseurl }}/devices/artnet-device.html) for fixture definitions and universes.
- [LED design]({{ site.docs_baseurl }}/common-practices/13-led-design.html), which takes this much further with array tools and shader-driven pixels.
- [Pattern matching]({{ site.docs_baseurl }}/in-depth/pattern-matching.html) for the full address syntax.
- [Data processing]({{ site.docs_baseurl }}/common-practices/12-data-processing.html), the bridge into Module E.
