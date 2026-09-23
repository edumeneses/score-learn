---
layout: default
title: "Lesson 13: Mapping sensor data: scaling, smoothing, and filtering"
description: "Build a pipeline from a sensor to an output: mapping curves, range filters, calibration, smoothing, and rate limiting, in the right order."
parent: Lessons
nav_order: 15
unit: "13"
permalink: /learn/13-mapping-and-scaling.html
score_version: "3.8.2"
reading_time: "14 min"
practice_time: "30 min"
score_file: none
---

# Lesson 13: Mapping sensor data: scaling, smoothing, and filtering

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 12]({{ site.baseurl }}/learn/12-recording-live-input.html), whose recorded curves are the fastest way to see the faults this lesson conditions away.
>
> **You will need** one input that produces a stream of values, and two outputs to drive from it.
>
> **You will build** a working pipeline from a live input to two outputs, with calibration, smoothing, and an explicit relationship in between.

## Why this matters

Mapping is where most of the quality of interactive work is decided. A sensor produces numbers in arbitrary units, over an undocumented range, and with unwanted noise, whereas an output expects a specific value in a specific range; every operation between those two facts is mapping, and a piece that responds to people is judged mostly on how well that middle is built, while the timeline contributes less to that judgement.

However, treating this work as arithmetic is the mistake to avoid, because scaling a range is arithmetic while deciding *how* a movement should feel, where it should be sensitive, where it should saturate, and how much it should smooth is design work. *score* gives that design work real tools instead of a single multiplication, and this lesson introduces them in the order you will use them.

## Concepts

### The four-stage pipeline

The pipeline has four stages, which are input, condition, relate, and output. Problems become much easier when you keep the stages separate, so that you **condition** the raw value first, then **relate** it to what you want, and then send it; mixing conditioning and relating in one object is how a mapping becomes impossible to adjust, because a change to either then disturbs the other.

### The mapping curve

The mapping curve is the central object. It is a drawn curve relating an input value to an output value. In contrast to an automation, its horizontal axis is the input and not time; a mapping curve is where "sensitive at the bottom, saturating at the top" gets expressed, and it is edited in the same way as an automation.

### Range filters

A range filter passes, clamps, or rejects values outside a window. This is how you keep a wild sensor from driving something dangerous, and how you ignore a region of an input you do not care about.

### Calibrators

A calibrator learns the actual range of an input by watching it. It is essential with physical sensors, whose real-world range differs from the range on the datasheet and changes again when someone moves the installation.

### Smoothing and latency

Smoothing filters jitter at the cost of latency. The trade-off is the point, because more smoothing means a calmer output and a later one; a light can be smoothed generously, whereas a percussive trigger should barely be smoothed at all.

### Rate limiters

A rate limiter caps how often values pass. Where smoothing changes values, rate limiting changes their frequency, which is what you need when a sensor floods the network or when a receiver cannot keep up.

### Math expressions and Micromap

Math expressions serve relationships that are easier to write than to draw. The **Micromap** object multiplies and offsets a value in one small step, which is the single most common conditioning operation. Moreover, the fuller expression objects evaluate arbitrary formulas, for relationships that need more than a multiply and an offset.

## Order matters

Put the same four objects in a different order and you get a different instrument, so the order deserves a decision of its own.

**Calibrate, then filter, then relate, then smooth** is the usual default. Calibration comes first so that every downstream stage works in a known normalised range; filtering comes next, to discard what you do not want; the mapping curve then expresses the relationship; and smoothing comes last, closest to the output, so that the smoothing you hear is the smoothing you set.

Nevertheless, **smoothing before the curve** is occasionally right, because where the curve is steep the jitter in that region is amplified, and filtering earlier avoids amplifying it.

**Rate limiting goes last** in nearly every case, because its job is to protect the destination.

Write the order down in your channel map, because a pipeline whose order was chosen for a reason can be tuned, whereas one that grew by accident can only be rebuilt.

## Walkthrough: sensor to two outputs

![The conditioning pipeline as a patch: calibrator, range filter, mapping curve, and smoothing in a chain]({{ site.img }}/13/13-01-pipeline.png)

The figure shows the pipeline in order, with a calibrator carrying its range and its averaging window, a range filter with a minimum, a maximum, and an invert, a mapping curve, and an exponential smoothing object with its alpha. Every stage is visible and adjustable on its own, which is the argument for building the chain this way instead of inside one script.

{: .note }
> **The library keeps these objects under `Control > Mappings` and `Control > Data Processing`.** Smoothing is `Exp Smoothing`, under `Control > Mappings`, and a `Smoother` in the analysis family serves as well. Learning those two category names now saves you searching by guessed object names, which is the difficulty [Lesson 14]({{ site.baseurl }}/learn/14-choosing-a-process.html) takes up.

1. **Confirm the input is arriving** in the device explorer before building the chain, as always.
2. **Make an interval to hold the pipeline**, remembering that a mapping only runs while its interval runs; give the interval's end a trigger that is never satisfied, so that the pipeline runs for the whole score, which is the idiom from Lesson 11.
3. **Add a calibrator** and feed it the raw input, then move the sensor through its full physical range so that it learns the bounds, and note what it learned, because that number belongs in your documentation.
4. **Add a range filter** and decide what to do with values outside your window, clamping for a continuous control and rejecting when an out-of-range value means "not present".
5. **Add a mapping curve** and draw the relationship, starting with a straight line, playing, and then bending it where you want more sensitivity; this is the step at which you stop calculating and start deciding.
6. **Send it to the first output** and play, at which point you have a working instrument in four objects.
7. **Add a smooth** just before the output and increase it until the output stops twitching, then reduce it until the response stops feeling late; the interval between those two settings is your working range.
8. **Fan out to a second output** with a different relationship, using a second mapping curve fed from the same conditioned value and inverted or scaled differently, so that one gesture produces two behaviours, which is where mapping starts to be expressive.
9. **Add a rate limiter** in front of any output that sits on a network, and watch the message log to confirm that the traffic dropped.
10. **Write the pipeline down**, listing the input, its calibrated range, each stage in order, and each output with its range, because this is the document your future self needs when the piece is reinstalled.

## The three places mapping can live

*score* offers more than one home for this logic, and choosing consciously keeps a project legible.

**The score itself, as processes, is where this lesson keeps the logic.** The logic is then visible, editable, and versioned with the document, which makes this the default.

**In a mapper device, the conversion appears in the device tree.** A mapper is a device whose parameters are computed by a small script, so that the conversion looks like a real parameter to the rest of the score; it is the right choice when the same conversion is needed from many places, or when you want the score to see clean values only.

**In the destination, the receiver does the scaling.** Sometimes the receiving software or fixture can scale for itself, which is the cheapest option and the least visible, since a reader of the score cannot tell that it happens.

No one of the three is right for every project, because each trades visibility against convenience differently. However, a project stays legible when each conversion happens in one place only, and when that place is written in the channel map, so that a collaborator who finds a suspicious value knows where to look.

## Two curves that feel completely different

The same two endpoints can be joined by curves that feel completely different, and building two of them once teaches the difference, which is not obvious on paper and is unmistakable in the hand.

A **curve that is steep at the bottom and flat at the top** gives fine control over small values and saturates early, so it suits any parameter whose interesting range is near zero: the first part of a fade, the quiet end of a dynamic range, or proximity where close matters and far does not.

In contrast, a **curve that is flat at the bottom and steep at the top** ignores small movements and then responds dramatically, which suits inputs with a noisy resting state, and interactions where you want a committed movement instead of a continuous response.

Both curves are two breakpoints and one bend, so build them, drive the same light with each, and move the input identically; the instrument is different although the input, the output, and the code are unchanged, which is the clearest demonstration that mapping is design work.

## Common mistakes

- **A pipeline in the wrong order**, most often smoothing before calibration, which makes the calibration learn smoothed bounds.
- **No calibration on a physical sensor**, when the range printed on the datasheet is the component's nominal range, whereas the range that reaches *score* depends on where and how the sensor is installed.
- **Smoothing a trigger**, which adds latency where you needed immediacy.
- **Fighting noise with a mapping curve**, when a curve relates values and does not filter them.
- **Forgetting that the pipeline needs a running interval**, because a mapping in an interval that has already ended does not run.
- **Doing the same conversion twice**, once in a range and once in a curve, then wondering why the response is squared.
- **No documentation**, although a mapping is a set of decisions, and undocumented decisions get reverted by the next person, who may be you.

## Exercise

Build the pipeline above from one real input to two outputs, then tune it against a stated intention: one output should feel immediate and slightly nervous, the other calm and deliberate, both driven by the same gesture. Furthermore, record in writing the smoothing value you chose for each and why, since a collaborator will need the reasoning.

**Success criterion:** the same input produces two clearly different behaviours; the pipeline survives the sensor being moved and re-calibrated; and your written map lets someone else rebuild it without asking you a question.

## Going further

- [Data processing]({{ site.docs_baseurl }}/common-practices/12-data-processing.html), the reference recipe for this pipeline.
- [Mapping curve]({{ site.docs_baseurl }}/processes/mapping.html), [range filter]({{ site.docs_baseurl }}/processes/range-filter.html), [calibrator]({{ site.docs_baseurl }}/processes/calibrator.html), [smooth]({{ site.docs_baseurl }}/processes/smooth.html), [rate limiter]({{ site.docs_baseurl }}/processes/rate-limiter.html).
- [Math expressions]({{ site.docs_baseurl }}/processes/exprtk.html) for formula-based relationships.
- [The mapper device]({{ site.docs_baseurl }}/devices/mapper-device.html) for conversions that live outside the timeline.

{% include lesson_files.html %}
