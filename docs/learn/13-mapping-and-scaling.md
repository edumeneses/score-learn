---
layout: default
title: "Lesson 13: Mapping, scaling, and curves"
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

# Lesson 13: Mapping, scaling, and curves

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 12]({{ site.baseurl }}/learn/12-recording-live-input.html).
>
> **You will need** one input that produces a stream of values, and two outputs to drive.
>
> **You will build** a working pipeline from a live input to two outputs, with calibration, smoothing, and an explicit relationship in between.

## Why this matters

Mapping is the whole craft of interactive work. A sensor produces numbers in units nobody chose, over a range nobody documented, with noise nobody wanted; an output expects something specific. Everything between those two facts is mapping, and the quality of a piece that responds to people is mostly determined here rather than in the timeline.

The mistake to avoid is treating this as arithmetic. Scaling a range is arithmetic. Deciding *how* a movement should feel, where it should be sensitive, where it should saturate, how much it should smooth, is design work, and *score* gives it real tools instead of a multiplication.

## Concepts

**The pipeline.** Input, condition, relate, output. Four stages, and problems get much easier when you keep them separate: **condition** the raw value, then **relate** it to what you want, then send it. Mixing conditioning and relating in one object is how a mapping becomes impossible to adjust.

**The mapping curve.** The central object: a drawn curve relating an input value to an output value. Unlike an automation, its horizontal axis is not time, it is the input. A mapping curve is where "sensitive at the bottom, saturating at the top" gets expressed, and it is editable exactly like an automation.

**Range filter.** Passes, clamps, or rejects values outside a window. This is how you keep a wild sensor from driving something dangerous, and how you ignore a region of an input you do not care about.

**Calibrator.** Learns the actual range of an input by watching it. Essential with physical sensors, whose real-world range is never the range on the datasheet, and whose range changes when someone moves the installation.

**Smoothing.** Filters jitter, at the cost of latency. The trade-off is the point: more smoothing means a calmer output and a later one. For a light, smooth generously; for a percussive trigger, barely at all. In the library this is `Exp Smoothing`, under `Control > Mappings`, with a `Smoother` in the analysis family as well.

**Rate limiter.** Caps how often values pass. Where smoothing changes values, rate limiting changes their frequency, which is what you need when a sensor floods the network or when a receiver cannot keep up.

**Math expressions.** For relationships that are easier to write than to draw. The **Micromap** object multiplies and offsets a value in one small step, which is the single most common conditioning operation; the fuller expression objects evaluate arbitrary formulas.

**Where the library keeps these.** In the process library under `Control > Mappings` and `Control > Data Processing`. Learning those two category names now saves you searching by guessed object names, which is what [Lesson 14]({{ site.baseurl }}/learn/14-choosing-a-process.html) is about.

## Order matters

Put the same four objects in a different order and you get a different instrument.

**Calibrate, then filter, then relate, then smooth.** The usual default. Calibration first, so that everything downstream works in a known normalised range; filtering next, to discard what you do not want; the mapping curve to express the relationship; smoothing last, closest to the output, so that the smoothing you hear is the smoothing you set.

**Smoothing before the curve** is occasionally right: when the curve is steep somewhere, jitter in that region is amplified, and filtering earlier avoids amplifying it.

**Rate limiting last**, almost always, because its job is to protect the destination.

Write the order down in your channel map. A pipeline whose order was chosen deliberately can be tuned; one that grew by accident can only be rebuilt.

## Walkthrough: sensor to two outputs

{: .note }
> A figure for this lesson is pending: it needs a patch assembled in the nodal view, which requires interaction. See `checks/13-mapping-and-scaling.md`.

1. **Get the input arriving** and confirm it in the device explorer, as always.
2. **Make an interval to hold the pipeline**, and remember that a mapping only runs while its interval runs. Give the interval's end a trigger that is never satisfied so that the pipeline runs for the whole score, which is the idiom from Lesson 11.
3. **Add a calibrator** and feed it the raw input. Move the sensor through its full physical range so it learns the bounds. Note what it learned; that number belongs in your documentation.
4. **Add a range filter** and decide what to do with values outside your window: clamp for a continuous control, reject when out-of-range values mean "not present".
5. **Add a mapping curve** and draw the relationship. Start with a straight line, play, then bend it where you want more sensitivity. This is the step where you stop calculating and start deciding.
6. **Send it to the first output** and play. You now have a working instrument, in four objects.
7. **Add a smooth** just before the output and increase it until the output stops twitching. Then reduce it until the response stops feeling late. That interval between the two is your working range and it is worth knowing.
8. **Fan out to a second output** with a different relationship: a second mapping curve fed from the same conditioned value, inverted or scaled differently. One gesture, two behaviours, which is where mapping starts to be expressive.
9. **Add a rate limiter** in front of any output that is on a network, and watch the message log to confirm the traffic dropped.
10. **Write it down.** Input, its calibrated range, each stage in order, and each output with its range. This is the document your future self needs when the piece is reinstalled.

## The three places mapping can live

*score* offers more than one home for this logic, and choosing consciously keeps a project legible.

**In the score, as processes.** What this lesson does. Visible, editable, versioned with the document. The default.

**In a mapper device.** A device whose parameters are computed by a small script, so that the conversion appears in the device tree as if it were a real parameter. Right when the same conversion is needed from many places in the score, or when you want the score to see clean values only.

**In the destination.** Sometimes the receiving software or fixture can do the scaling. Cheapest, and invisible: nobody reading the score can tell it happens.

There is no universal answer, only a rule: one conversion, one home, written down.

## Two curves that feel completely different

Worth building once, because the difference is not obvious on paper and is unmistakable in the hand.

A **curve that is steep at the bottom and flat at the top** gives fine control over small values and saturates early. It suits anything where the interesting range is near zero: the first part of a fade, the quiet end of a dynamic range, proximity where close matters and far does not.

A **curve that is flat at the bottom and steep at the top** ignores small movements and then responds dramatically. It suits inputs with a noisy resting state, and interactions where you want a deliberate commitment rather than a continuous response.

Both are two breakpoints and one bend. Build them, drive the same light with each, and move the input identically. The instrument is different, and nothing about the input, the output, or the code changed.

## Common mistakes

- **A pipeline in the wrong order**, most often smoothing before calibration, which makes the calibration learn smoothed bounds.
- **No calibration on a physical sensor.** Datasheet ranges are fiction in a room.
- **Smoothing a trigger.** Latency where you needed immediacy.
- **Fighting noise with a mapping curve.** A curve relates values; it does not filter them.
- **Forgetting that the pipeline needs a running interval.** A mapping in an interval that already ended is a mapping that does nothing.
- **Doing the same conversion twice**, once in a range and once in a curve, then wondering why the response is squared.
- **No documentation.** A mapping is a set of decisions, and undocumented decisions get reverted by the next person, who may be you.

## Exercise

Build the pipeline above from one real input to two outputs, then tune it against a stated intention: one output should feel immediate and slightly nervous, the other calm and deliberate, both driven by the same gesture. Record, in writing, the smoothing value you chose for each and why.

**Success criterion:** the same input produces two clearly different behaviours; the pipeline survives the sensor being moved and re-calibrated; and your written map lets someone else rebuild it without asking you a question.

## Going further

- [Data processing]({{ site.docs_baseurl }}/common-practices/12-data-processing.html), the reference recipe for this pipeline.
- [Mapping curve]({{ site.docs_baseurl }}/processes/mapping.html), [range filter]({{ site.docs_baseurl }}/processes/range-filter.html), [calibrator]({{ site.docs_baseurl }}/processes/calibrator.html), [smooth]({{ site.docs_baseurl }}/processes/smooth.html), [rate limiter]({{ site.docs_baseurl }}/processes/rate-limiter.html).
- [Math expressions]({{ site.docs_baseurl }}/processes/exprtk.html) for formula-based relationships.
- [The mapper device]({{ site.docs_baseurl }}/devices/mapper-device.html) for conversions that live outside the timeline.
