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

> **Before this lesson** finish [Lesson 07]({{ site.baseurl }}/learn/07-osc-devices.html) and keep the device you declared.
>
> **You will need** `lesson-00.score` for the figure, and your own device for the exercise.
>
> **You will build** a reliable answer to the most common complaint in this software: "the automation runs but nothing happens".

## Why this matters

Every step so far can be done correctly and still produce nothing, because a value has to be the right *kind* of value, in the right *range*, in the right *unit*, before it means anything to the thing receiving it. This is dull and it is where hours go.

It is also where *score* offers something better than arithmetic in your head. Parameters can declare units, and the software converts between them; addresses can select one member of an array or one component of a colour. Learning the syntax takes ten minutes and removes a whole category of hand-written conversion.

## Concepts

**Type.** What kind of value: float, integer, boolean, impulse, string, or a vector such as `vec2f` and `vec3f`, or a list. Type is decided when a parameter is declared and it determines what goes on the wire.

**Range, also called the domain.** The minimum and maximum a parameter accepts. Two separate ranges are in play whenever you write an automation, and confusing them is the classic error: the **parameter's** range, declared on the device, and the **process's** minimum and maximum, shown in its slot header, which map the curve's 0-to-1 space onto real values. The figure below shows the second kind, `Min: 0  Max: 1`, written right next to the destination address.

**Clip mode.** What happens to a value outside the range: pass it through, clamp it to the bounds, or reject it. A parameter that silently clamps looks like an automation that stops moving halfway.

**Unit.** A declared physical meaning: degrees against radians, RGB against HSV, metres against feet. When both ends declare units, *score* converts. This is not cosmetic; it is the difference between writing a rotation in the unit you think in and writing it in the unit the device happens to want.

**Address suffixes.** An address can carry a suffix in brackets that narrows what it writes to:

| Syntax | Writes to |
|---|---|
| `dev:/position` | every member of the array |
| `dev:/position@[1]` | the second member only, counting from zero |
| `dev:/matrix@[1][0]` | a member of a nested array |
| `dev:/colour@[color.rgb.r]` | the red component only |
| `dev:/tilt@[angle.radian]` | the whole parameter, expressed in radians |

The first row is worth reading twice: with no suffix, an automation sent to an array parameter affects **all** its members. That is occasionally what you want and frequently a surprise.

## Walkthrough: read the two ranges, then use a suffix

![A slot header showing an automation's destination address next to its minimum and maximum]({{ site.img }}/08/08-01-address-and-range.png)

1. **Find the process range.** In `lesson-00.score`, look at any slot header: `Automation (float).3 -> lesson:/colour  Min: 0  Max: 1`. Those two numbers belong to the automation.
2. **Find the parameter range.** In the device explorer, select `colour` and read its attributes in the panel inspector. That range belongs to the device.
3. **Make them disagree on purpose.** Set an automation's maximum to 0.1 while the parameter accepts 0 to 1, and play. The curve sweeps its full height and the parameter barely moves. This is the single most common report of a broken automation, and it is now legible to you.
4. **Test the boundary.** Set the automation's maximum above the parameter's maximum and watch what happens at the top: pass through, clamp, or nothing, depending on the clip mode. Note which one your device does.
5. **Use an array suffix.** On your own device from Lesson 07, declare a `vec3f` parameter, for instance a position. Aim one automation at `dev:/position@[1]` and play: only the second member moves. Remove the suffix and play again: all three move together.
6. **Use a component suffix.** Declare a parameter with a colour unit and drive `@[color.rgb.r]` alone. Then, without changing the device, drive `@[color.hsv.h]` and watch *score* convert: you are writing hue into a parameter declared in RGB.
7. **Use a unit suffix.** Declare an angle in degrees, then drive it through `@[angle.radian]`. Write your curve in radians; the device receives degrees.
8. **Write the ranges down.** For the device you are actually using, record each parameter's type, range, and unit next to its address. This becomes part of the technical documentation of your piece, and [Lesson 34]({{ site.baseurl }}/learn/34-rehearsal-to-show.html) uses it.

## When to convert where

Three places can do the same conversion, and choosing deliberately keeps a project comprehensible.

- **On the device declaration**, by declaring an honest range and unit. Best default: every process aimed at that parameter inherits correct behaviour.
- **On the process**, with its minimum and maximum. Right when *this* curve should cover only part of the parameter's range.
- **In a mapping process**, when the relationship is not a straight line, or when one source drives several destinations differently. That is [Lesson 13]({{ site.baseurl }}/learn/13-mapping-and-scaling.html).

Doing the same conversion in two of the three places is how a project becomes impossible to reason about. Pick one and note the choice.

## Where ranges bite hardest

Three destinations produce range problems out of proportion to their complexity, and knowing them in advance saves the diagnosis.

**MIDI.** Controller values run 0 to 127, integers. An automation left at 0 to 1 sends 0 or 1 out of 127, which is a barely perceptible change at the very bottom of the range, and it looks exactly like a broken connection. This is the most common instance of the whole problem, and [Lesson 23]({{ site.baseurl }}/learn/23-midi-in-practice.html) assumes you have met it here.

**Lighting.** DMX channels are 0 to 255, integers, and fixtures often use sub-ranges of one channel for modes rather than intensities. Sending a smooth curve across a channel that encodes discrete modes produces a fixture that flickers between behaviours rather than fading, which is not a range error in the arithmetic sense and is certainly a range error in the practical one.

**Anything angular.** Rotations are where unit conversion earns its keep, because degrees and radians differ by a factor no one notices until something spins thirty times too fast. Declare the unit and let the software convert, rather than multiplying by 57.29 in your head and hard-coding it into a curve that someone else will later have to interpret.

The general rule behind all three: when a destination's range is not 0 to 1, decide once where the conversion happens, write it down beside the address, and do not repeat it anywhere else.

A last note on discovery. Everything in this lesson is easier when the device declares its own types, ranges, and units, which is precisely what OSCQuery does and plain OSC cannot. When you have the choice of protocol, this lesson is the argument for the descriptive one.

## Common mistakes

- **Confusing the two ranges.** The slot header shows the process's; the explorer shows the parameter's.
- **Leaving 0 to 1 everywhere.** It is the default and it is right only when the destination is also normalised.
- **Sending to an array without a suffix** and moving every member at once.
- **Counting array members from one.** `@[0]` is the first.
- **Assuming a unit conversion happened.** It happens when the parameter declares a unit. A parameter declared as a bare float has no unit to convert from, and the suffix will not invent one.
- **Declaring a trigger as a float.** Use an impulse; the arrival is the message.
- **Fighting a clamp.** If values stop changing at a bound, the range is doing its job. Change the range, not the curve.

## Exercise

On your own device, declare four parameters: a normalised float, an integer with a range of 0 to 127, a `vec3f` position, and an angle in degrees. Then write a twenty-second score that drives each one correctly: the float across its full range, the integer across its full range from a curve whose own range you set deliberately, only the second member of the position, and the angle through a radian suffix.

**Success criterion:** all four move as intended in your receiver, and you can state for each whether the conversion happened on the device, on the process, or through a suffix. If one refused to move, say which of the two ranges was wrong; that is the diagnosis this lesson exists to make automatic.

## Going further

- [The unit system]({{ site.docs_baseurl }}/in-depth/unit-system.html), the reference for every syntax above.
- [The libossia unit list](https://ossia.io/ossia-docs/#units), for the full set of supported units.
- [Mapping utilities]({{ site.docs_baseurl }}/processes/mapping-utilities.html), a preview of [Lesson 13]({{ site.baseurl }}/learn/13-mapping-and-scaling.html).
- [Data processing]({{ site.docs_baseurl }}/common-practices/12-data-processing.html), for shaping values at scale.
