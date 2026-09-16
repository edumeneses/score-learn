---
layout: default
title: "Lesson 08: Units, ranges, and types"
description: "Why a working automation can produce no visible effect, and the address suffixes that select an array member, a component, or a unit."
parent: Lessons
nav_order: 9
unit: "08"
permalink: /learn/08-units-ranges-types.html
score_version: "3.8.2"
reading_time: "13 min"
practice_time: "20 min"
score_file: 00-what-score-is/lesson-00.score
---

# Lesson 08: Units, ranges, and types

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 07]({{ site.baseurl }}/learn/07-osc-devices.html) and keep the device you declared there.
>
> **You will need** `lesson-00.score` for the figure, and your own device for the exercise.
>
> **You will build** a reliable answer to the most common complaint about this software, which is that "the automation runs but nothing happens".

## Why this matters

Every step so far can be done correctly and still produce no visible effect, because a value has to be the right *kind* of value, in the right *range*, and in the right *unit* before the receiving end can make sense of it. This part of the work is unglamorous, and it is also where a large share of debugging time goes, which is why the lesson treats it as a diagnosis to make automatic.

Furthermore, this is where *score* offers something better than arithmetic in your head, since parameters can declare units and the software converts between them, while addresses can select one member of an array or one component of a colour. Learning the syntax takes about ten minutes, and it removes a whole category of hand-written conversion from your documents.

## Concepts

**Type says what kind of value a parameter holds.** The kinds are float, integer, boolean, impulse, string, a vector such as `vec2f` and `vec3f`, or a list. Type is decided when a parameter is declared, and it determines what goes on the wire, as Lesson 07 showed.

**Range, also called the domain, is the minimum and maximum a parameter accepts.** Two separate ranges are in play whenever you write an automation, and confusing them is the classic error. The **parameter's** range is declared on the device, whereas the **process's** minimum and maximum, shown in its slot header, map the curve's 0-to-1 space onto real values; the figure below shows the second kind, `Min: 0  Max: 1`, written next to the destination address.

**Clip mode decides what happens to a value outside the range.** The value can pass through, be clamped to the bounds, or be rejected, and a parameter that silently clamps looks like an automation that stops moving halfway.

**A unit gives a value a declared physical meaning.** Degrees against radians, RGB against HSV, and metres against feet are the typical pairs, and when both ends declare units, *score* converts between them. Moreover, the conversion is more than cosmetic, because it is the difference between writing a rotation in the unit you think in and writing it in the unit the device happens to want.

**Address suffixes narrow what an address writes to.** An address can carry a suffix in brackets that selects part of the parameter, as the table shows:

| Syntax | Writes to |
|---|---|
| `dev:/position` | every member of the array |
| `dev:/position@[1]` | the second member only, counting from zero |
| `dev:/matrix@[1][0]` | a member of a nested array |
| `dev:/colour@[color.rgb.r]` | the red component only |
| `dev:/tilt@[angle.radian]` | the whole parameter, expressed in radians |

The first row of the table deserves a second reading, because with no suffix an automation sent to an array parameter affects all of its members, which is occasionally what you want and frequently a surprise.

## Walkthrough: read the two ranges, then use a suffix

![A slot header showing an automation's destination address next to its minimum and maximum]({{ site.img }}/08/08-01-address-and-range.png)

1. **Find the process range** in `lesson-00.score` by looking at any slot header, which reads `Automation (float).3 -> lesson:/colour  Min: 0  Max: 1`; those two numbers belong to the automation.
2. **Find the parameter range** in the device explorer by selecting `colour` and reading its attributes in the panel inspector, where the range belongs to the device.
3. **Make them disagree on purpose** by setting an automation's maximum to 0.1 while the parameter accepts 0 to 1, and play. The curve sweeps its full height while the parameter barely moves, which is the single most common report of a broken automation, and it is now legible to you.
4. **Test the boundary** by setting the automation's maximum above the parameter's maximum and watching what happens at the top, which is a pass-through, a clamp, or no movement depending on the clip mode; note which one your device does.
5. **Use an array suffix** on your own device from Lesson 07 by declaring a `vec3f` parameter, for instance a position, and aiming one automation at `dev:/position@[1]`. When you play, only the second member moves, whereas removing the suffix and playing again moves all three together.
6. **Use a component suffix** by declaring a parameter with a colour unit and driving `@[color.rgb.r]` alone. Then, without changing the device, drive `@[color.hsv.h]` and watch *score* convert, since you are now writing hue into a parameter declared in RGB.
7. **Use a unit suffix** by declaring an angle in degrees and then driving it through `@[angle.radian]`, so that you write your curve in radians while the device receives degrees.
8. **Write the ranges down** for the device you are using, recording each parameter's type, range, and unit next to its address. This record becomes part of the technical documentation of your piece, and [Lesson 34]({{ site.baseurl }}/learn/34-rehearsal-to-show.html) uses it.

## When to convert where

The same conversion can happen in three places, and choosing one of them with intent keeps a project comprehensible.

- **On the device declaration**, by declaring an accurate range and unit, which is the best default because every process aimed at that parameter inherits correct behaviour.
- **On the process**, with its minimum and maximum, which is right when *this* curve should cover only part of the parameter's range.
- **In a mapping process**, when the relationship is not a straight line, or when one source drives several destinations differently, which is the subject of [Lesson 13]({{ site.baseurl }}/learn/13-mapping-and-scaling.html).

However, doing the same conversion in two of the three places is how a project becomes impossible to reason about, so pick one and note the choice beside the address.

## Where ranges bite hardest

The following three destinations produce range problems out of proportion to their complexity, and knowing them in advance spares you the diagnosis.

**MIDI (Musical Instrument Digital Interface) controller values run from 0 to 127 as integers.** An automation left at 0 to 1 therefore sends 0 or 1 out of 127, which is a barely perceptible change at the bottom of the range, and it looks like a broken connection. This is the most common instance of the whole problem. Moreover, [Lesson 23]({{ site.baseurl }}/learn/23-midi-in-practice.html) assumes you have met it here.

**Lighting channels carry modes as well as intensities.** DMX (Digital Multiplex) channels run from 0 to 255 as integers, and fixtures often use sub-ranges of one channel for modes in place of intensities. Sending a smooth curve across a channel that encodes discrete modes therefore produces a fixture that flickers between behaviours instead of fading, which is not a range error in the arithmetic sense and is certainly one in the practical sense.

**Angular values are where unit conversion earns its place.** In contrast to the two integer cases, rotations expose the problem because degrees and radians differ by a factor that no one notices until something spins thirty times too fast. Declare the unit and let the software convert, since multiplying by 57.29 in your head and hard-coding it into a curve leaves a number that someone else will later have to interpret.

In other words, when a destination's range is not 0 to 1, decide once where the conversion happens, write it down beside the address, and do not repeat it in a second place.

A last point concerns discovery, because the whole of this lesson is easier when the device declares its own types, ranges, and units, which is precisely what OSCQuery does and plain OSC cannot. When you have the choice of protocol, this lesson is the argument for the descriptive one.

## Common mistakes

- **Confusing the two ranges** is the classic error, since the slot header shows the process's range while the explorer shows the parameter's.
- **Leaving 0 to 1 everywhere** works only when the destination is also normalised, because that range is the default and not a considered choice.
- **Sending to an array without a suffix** moves every member at once, which is rarely the intention.
- **Counting array members from one** misses the target, since `@[0]` is the first.
- **Assuming a unit conversion happened** fails when the parameter declares no unit, because a parameter declared as a bare float has no unit to convert from, and the suffix will not invent one.
- **Declaring a trigger as a float** invites the mismatch that Lesson 07 described, so use an impulse, whose arrival is the message.
- **Fighting a clamp** wastes effort, because values that stop changing at a bound show the range doing its job; change the range and leave the curve alone.

## Exercise

On your own device, declare four parameters: a normalised float, an integer with a range of 0 to 127, a `vec3f` position, and an angle in degrees. Then write a twenty-second score that drives each one correctly, which means the float across its full range, the integer across its full range from a curve whose own range you set yourself, only the second member of the position, and the angle through a radian suffix.

**Success criterion:** all four move as intended in your receiver, and you can state for each whether the conversion happened on the device, on the process, or through a suffix. If one refused to move, say which of the two ranges was wrong, since that is the diagnosis this lesson exists to make automatic.

## Going further

- [The unit system]({{ site.docs_baseurl }}/in-depth/unit-system.html) is the reference for every syntax above.
- [The libossia unit list](https://ossia.io/ossia-docs/#units) gives the full set of supported units.
- [Mapping utilities]({{ site.docs_baseurl }}/processes/mapping-utilities.html) previews the processes that [Lesson 13]({{ site.baseurl }}/learn/13-mapping-and-scaling.html) builds on.
- [Data processing]({{ site.docs_baseurl }}/common-practices/12-data-processing.html) covers shaping values at scale, once a project has many of them.
