---
layout: default
title: "Lesson 10: Automation curves: shape, tweening, and splines"
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

# Lesson 10: Automation curves: shape, tweening, and splines

{% include lesson_meta.html %}

> **Before this lesson** finish [Milestone P2]({{ site.baseurl }}/learn/p2-light-wash.html).
>
> **You will need** `lesson-10.score`, which holds four curves of different shapes.
>
> **You will build** fluency with curve shape as an expressive choice instead of a technical detail, together with three faster ways to make an automation.

## Why this matters

A linear ramp is the default shape of an automation, and it is a choice whether or not you make it consciously, because few things in the physical world change linearly; a light fading, a sound approaching, and a projection dissolving all accelerate or settle. The difference between a piece that feels mechanical and one that feels intentional is often no more than curvature applied with intent, and it costs the same amount of work as leaving the default in place.

Furthermore, this lesson addresses a workflow problem, because dragging a process from the library and then assigning its address takes four gestures, and you will repeat them hundreds of times. There are three shorter routes, and knowing them changes how quickly you can try an idea.

## Concepts

### Breakpoints and segments

A curve is a chain of segments meeting at breakpoints. A breakpoint is a value at a time, whereas a segment is the shape between two of them; adding a breakpoint subdivides the curve, while bending a segment changes its character without adding structure.

### Segment curvature

Curvature, also called power, is a shape parameter carried by each segment. It is adjusted with `Shift+Drag`, and a segment bent one way accelerates while one bent the other way decelerates.

### Tweening from the current value

Tweening makes a curve start from the parameter's current value. An automation normally starts at its written start value, which produces a jump if the parameter is currently elsewhere. However, **tween** mode, enabled in the inspector, makes the curve ramp from the parameter's *current* value instead, which is the fix for a cue-driven piece in which a section can be entered from more than one condition; it is the single most useful option on this page.

### The three automation variants

The automation family has three variants. A one-dimensional float automation is what you have used so far. The other two are the **2D spline**, which drives a pair of values along a drawn path and suits positions and trajectories, and the **gradient**, which is an automation over colour; they are the same idea with a different value type.

## Four faster ways to create one

Only the first of the four is what Lesson 04 taught.

1. **Drag the process** from the library onto an interval, then assign the address, which is fully general and takes four gestures.
2. **Drag a parameter** from the device explorer onto an interval, so that *score* creates an automation already addressed to that parameter; this is the route to use by default.
3. **Interpolate states** when two of them hold different values for the same address, since the scenario's *interpolate states* function writes the automation between them. This is the manual form of the auto-sequence behaviour from Lesson 09, and it is how you convert two looks into a transition after the fact.
4. **Right-click a value port** and choose *create automation*, which is the route for a control that is not a device parameter at all, such as the gain of an audio outlet, the cutoff of an effect, or the opacity of a video filter. Every control with a value port can be automated, which is a much larger set than the contents of the device explorer.

Route four deserves emphasis because it addresses the internals of your score, whereas the other three address the outside world, and it is used constantly from Module G onward.

## Walkthrough: shape as a choice

[![Four intervals, each holding one automation with a different curve shape]({{ site.img }}/10/10-01-curve-shapes.png)]({{ site.scores }}/10-automation-curves/lesson-10.score){: download="" title="Download lesson-10.score, the document in this figure" }

1. **Open `lesson-10.score`**, which holds four intervals with four curves on the same address, numbered in the figure: linear, accelerating, decelerating, and a two-segment shape with a hold in the middle.
2. **Play it and watch one value**, which shows the same start, the same end, and the same duration producing four quite different behaviours, while no other part of the document differs.
3. **Bend a segment** by selecting one in the linear curve and using `Shift+Drag`, and note that the breakpoints do not move because you are changing the path between them.

   {: .warning }
   > **Changing the range after drawing does not redraw the curve.** Lesson 08 covered why the minimum and maximum are properties of the automation, and here they matter for a second reason: a shape drawn against 0 to 1 keeps its shape when remapped to 0 to 255, which is usually what you want. Moreover, it means you can design shapes before you know the destination.

4. **Add a breakpoint and then remove it** by double-clicking inside the slot to add one, then deleting it and obtaining the same visual result with a bend instead. However, the bend is the better choice, because it leaves fewer objects to maintain and it is easier to revise when you change your mind.
5. **Edit at full size** by double-clicking the process name for precision and pressing `Ctrl+Alt+↑` to leave; on a four-curve document this is the difference between drawing and guessing.
6. **Turn on tween** by selecting the second automation and enabling tween in the inspector, then set the parameter to some other value from the device explorer before playing that section alone. The curve now starts from wherever the parameter happens to be. In contrast, before you enabled tween it started where the curve was drawn.
7. **Try a gradient** by adding a gradient process on a colour parameter, if you have one declared; it is the same interface with colour stops in place of a value axis.
8. **Try a 2D spline** by adding one, drawing a path, and noting that its output is a pair, which is what Module G's spatialisation and Module I's positioning both consume.

## When a curve is the wrong tool

Reaching for an automation is the mistake in three cases, all of which the next lessons cover.

**When the shape should repeat, a generator replaces the drawing.** A curve drawn four times is four things to maintain. In contrast, an LFO (low-frequency oscillator), in [Lesson 11]({{ site.baseurl }}/learn/11-modulation-sources.html), is one thing with a rate.

**When the shape comes from outside, the movement is mapped or recorded.** If the movement should follow a performer, a sensor, or another parameter, the shape is not yours to draw; that is mapping, in [Lesson 13]({{ site.baseurl }}/learn/13-mapping-and-scaling.html), or recording, in [Lesson 12]({{ site.baseurl }}/learn/12-recording-live-input.html).

**When the duration is unknown, the curve stretches with the wait.** A curve is defined over its interval, so if the interval waits for a trigger, the curve is stretched by the wait, which may or may not be what you meant. [Lesson 15]({{ site.baseurl }}/learn/15-triggers.html) is where that becomes precise, and knowing in advance that a dashed duration means "as long as this takes" saves confusion when you first see one.

## Reading a curve as an intention

When reviewing your own work, describing each curve in words before deciding whether it is right exposes shapes you have not chosen, and the vocabulary below is one way to do it.

**An accelerating curve, slow then fast, reads as something gathering.** A swell, an approach, and pressure building all take this shape, and it is the default for anything that should feel inevitable instead of mechanical.

**A decelerating curve, fast then slow, reads as arriving and settling.** A light landing on its final level and a sound coming to rest both take this shape, which is what most fades want and what few people draw by default.

**A linear curve reads as a machine**, which is occasionally right, for a scan, a sweep, or any movement that should feel indifferent.

**A hold in the middle reads as a decision**, since something moves, waits, and then moves again. The shape is two segments and a flat one, and it is the one that most often turns a transition into a gesture.

In other words, if you cannot describe a curve in one of these terms, you probably have not decided what it should do, and that is a discovery to make before a rehearsal, whereas making it during one costs the room's time.

## Common mistakes

- **Accepting the linear default** leaves the shape undecided, since the default is where a curve begins and seldom where it should end.
- **Drawing ten breakpoints instead of two and a bend** makes the curve harder to adjust, and it hides the intention, whereas two breakpoints and two bends express most of what a fade needs.
- **Forgetting tween on a cue-driven section** shows as a visible or audible jump when the section is entered from an unexpected state.
- **Assuming a range change redraws the curve** misreads a feature, because the curve keeps its shape so that you can design it once and remap it freely.
- **Using a 1D automation for a position** means two curves that must stay in agreement, which is worse than one 2D spline.
- **Editing inside the slot band** when precision matters ignores the full-size editor, which exists for this purpose.

## Exercise

Take one twenty-second interval and one parameter, and write five versions of the same fade, each in its own copy of the interval: linear; accelerating; decelerating; a two-segment shape that pauses in the middle; and one built by interpolating between two captured states instead of drawn. Play them in sequence and write one sentence describing what each one feels like, because the description is what tells you whether the shape was chosen.

**Success criterion:** you can name which of the five you would use for a light coming up on an empty stage, and why, and at least one of your five was created without dragging a process from the library.

## Going further

- [Automations in depth]({{ site.docs_baseurl }}/in-depth/automations.html) covers the creation routes and tweening.
- [The automation process]({{ site.docs_baseurl }}/processes/automation_float.html) documents every inspector option.
- [2D spline]({{ site.docs_baseurl }}/processes/2Dspline.html) and [gradient]({{ site.docs_baseurl }}/processes/gradient.html) are the other two variants.
- [Interpolate states]({{ site.docs_baseurl }}/processes/scenario.html) is described in the scenario reference.

{% include lesson_files.html %}
