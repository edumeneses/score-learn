---
layout: default
title: "Lesson 10: Automation curves in depth"
description: "Segments, curvature, tweening, the three other ways to create an automation, and the two-dimensional and colour variants."
parent: Lessons
nav_order: 12
unit: "10"
permalink: /learn/10-automation-curves.html
score_version: "3.8.2"
reading_time: "12 min"
practice_time: "20 min"
score_file: 10-automation-curves/lesson-10.score
---

# Lesson 10: Automation curves in depth

{% include lesson_meta.html %}

> **Before this lesson** finish [Milestone P2]({{ site.baseurl }}/learn/p2-light-wash.html).
>
> **You will need** `lesson-10.score`, which holds four curves of different shapes.
>
> **You will build** fluency with curve shape as an expressive choice rather than a technical detail, and three faster ways to make an automation.

## Why this matters

A linear ramp is a decision, and usually the wrong one. Almost nothing in the physical world changes linearly: a light fading, a sound approaching, a projection dissolving. The difference between a piece that feels mechanical and one that feels intentional is very often nothing more than curvature, applied deliberately, in the same amount of work.

This lesson also fixes a workflow problem. Dragging a process from the library and then assigning its address is four gestures, and you will do it hundreds of times. There are three shorter routes, and knowing them changes how quickly you can try an idea.

## Concepts

**Segment and breakpoint.** A curve is a chain of segments meeting at breakpoints. A breakpoint is a value at a time; a segment is the shape between two of them. Adding a breakpoint subdivides; bending a segment changes character without adding structure.

**Curvature, or power.** Each segment carries a shape parameter, adjusted with `Shift+Drag`. A segment bent one way accelerates, the other decelerates. Two breakpoints and two bends express most of what a fade needs; ten breakpoints approximating a curve is the beginner's alternative and it is much harder to edit afterwards.

**Tweening.** An automation normally starts at its written start value, which produces a jump if the parameter is currently elsewhere. Enabled in the inspector, **tween** mode makes the curve ramp from the parameter's *current* value instead. This is the fix for a cue-driven piece where a section can be entered from more than one condition, and it is the single most useful option on this page.

**The three variants.** A one-dimensional float automation is what you have used. There are two others: the **2D spline**, which drives a pair of values along a drawn path, useful for positions and trajectories; and the **gradient**, which is an automation over colour. They are the same idea with a different value type.

**Ranges, again.** The minimum and maximum are properties of the automation, and Lesson 08 covered why. Here they matter for a second reason: changing the range after drawing does not redraw the curve, so a shape drawn against 0 to 1 keeps its shape when remapped to 0 to 255. That is usually what you want, and it means you can design shapes before you know the destination.

## Four faster ways to create one

Only the first is what Lesson 04 taught.

1. **Drag the process** from the library onto an interval, then assign the address. Fully general, four gestures.
2. **Drag a parameter** from the device explorer onto an interval. *score* creates an automation already addressed to that parameter. This is the one to use by default.
3. **Interpolate states.** Given two states holding different values for the same address, the scenario's *interpolate states* function writes the automation between them. This is the manual form of the auto-sequence behaviour from Lesson 09, and it is how you convert two looks into a transition after the fact.
4. **Right-click a value port** and choose *create automation*. This is the route for a control that is not a device parameter at all: the gain of an audio outlet, the cutoff of an effect, the opacity of a video filter. Everything with a value port can be automated, which is a much larger set than "things in the device explorer".

Route four deserves emphasis. It is how you automate the internals of your score rather than the outside world, and it is used constantly from Module G onward.

## Walkthrough: shape as a choice

![Four intervals, each holding one automation with a different curve shape]({{ site.img }}/10/10-01-curve-shapes.png)

1. **Open `lesson-10.score`.** Four intervals, four curves on the same address, numbered in the figure: linear, accelerating, decelerating, and a two-segment shape with a hold in the middle.
2. **Play it and watch one value.** The same start, the same end, the same duration, four quite different behaviours. Nothing else in the document differs.
3. **Bend a segment.** Select a segment in the linear curve and `Shift+Drag`. Note that the breakpoints do not move: you are changing the path between them.
4. **Add a breakpoint and then remove it.** Double-click inside the slot to add. Now delete it and get the same visual result with a bend instead. Prefer the bend: fewer objects, easier to change your mind.
5. **Edit at full size.** Double-click the process name for precision, `Ctrl+Alt+↑` to leave. On a four-curve document this is the difference between drawing and guessing.
6. **Turn on tween.** Select the second automation, enable tween in the inspector, and set the parameter to some other value from the device explorer before playing that section alone. The curve now starts where the parameter is, not where the curve was drawn.
7. **Try a gradient.** Add a gradient process on a colour parameter if you have one declared. It is the same interface with colour stops instead of a value axis.
8. **Try a 2D spline.** Add one, draw a path, and note that its output is a pair. Module G's spatialisation and Module I's positioning both consume exactly this.

## When a curve is the wrong tool

Three cases where reaching for an automation is the mistake, all of which the next lessons cover.

**When the shape should repeat.** A curve drawn four times is four things to maintain. An LFO, in [Lesson 11]({{ site.baseurl }}/learn/11-modulation-sources.html), is one thing with a rate.

**When the shape comes from outside.** If the movement should follow a performer, a sensor, or another parameter, the shape is not yours to draw. That is mapping, in [Lesson 13]({{ site.baseurl }}/learn/13-mapping-and-scaling.html), or recording, in [Lesson 12]({{ site.baseurl }}/learn/12-recording-live-input.html).

**When the duration is unknown.** A curve is defined over its interval. If the interval waits for a trigger, the curve is stretched by the wait, which may or may not be what you meant. [Lesson 15]({{ site.baseurl }}/learn/15-triggers.html) is where that becomes precise, and it is worth knowing in advance that a dashed duration means "as long as this takes".

## Reading a curve as an intention

A useful habit when reviewing your own work: describe each curve in words before deciding whether it is right.

**Accelerating**, slow then fast, reads as something gathering: a swell, an approach, pressure building. It is the default for anything that should feel inevitable rather than mechanical.

**Decelerating**, fast then slow, reads as arriving and settling: a light landing on its final level, a sound coming to rest. It is what most fades want and what almost nobody draws by default.

**Linear** reads as a machine, which is occasionally exactly right, for a scan, a sweep, anything that should feel indifferent.

**A hold in the middle** reads as a decision: something moves, waits, then moves again. Two segments and a flat one, and it is the shape that most often turns a transition into a gesture.

If you cannot describe a curve in one of these terms, you probably have not decided what it should do, which is worth noticing before a rehearsal rather than during one.

## Common mistakes

- **Accepting the linear default.** It is a starting point, not a shape.
- **Ten breakpoints instead of two and a bend.** Harder to adjust, and it hides the intention.
- **Forgetting tween on a cue-driven section.** The symptom is a visible or audible jump when a section is entered from an unexpected state.
- **Assuming a range change redraws the curve.** It does not, and that is a feature: design the shape once, remap it freely.
- **Using a 1D automation for a position.** Two curves that must stay in agreement are worse than one 2D spline.
- **Editing inside the slot band** when precision matters. Full-size edit exists for this.

## Exercise

Take one twenty-second interval and one parameter. Write five versions of the same fade, each in its own copy of the interval: linear; accelerating; decelerating; a two-segment shape that pauses in the middle; and one built by interpolating between two captured states rather than drawn. Play them in sequence and write one sentence describing what each one feels like.

**Success criterion:** you can name which of the five you would use for a light coming up on an empty stage, and why, and at least one of your five was created without dragging a process from the library.

## Going further

- [Automations in depth]({{ site.docs_baseurl }}/in-depth/automations.html) for the creation routes and tweening.
- [The automation process]({{ site.docs_baseurl }}/processes/automation_float.html) for every inspector option.
- [2D spline]({{ site.docs_baseurl }}/processes/2Dspline.html) and [gradient]({{ site.docs_baseurl }}/processes/gradient.html), the other two variants.
- [Interpolate states]({{ site.docs_baseurl }}/processes/scenario.html) in the scenario reference.
