---
layout: default
title: "Lesson 04: Your first process"
description: "Place an automation on the timeline, give it a destination address, shape its curve, and learn the difference between a slot and a process."
parent: Lessons
nav_order: 4
unit: "04"
permalink: /learn/04-first-process.html
score_version: "3.8.2"
reading_time: "13 min"
practice_time: "25 min"
score_file: 04-first-process/lesson-04.score
---

# Lesson 04: Your first process

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 03]({{ site.baseurl }}/learn/03-interface-and-transport.html).
>
> **You will need** a new empty document. `lesson-04.score` ships with this lesson as the finished result; build your own first and compare afterwards.
>
> **You will build** one interval holding one automation that drives one parameter from 0 to 1 over eight seconds.

## Why this matters

This is the first lesson that writes something. Everything later in the course is a variation on the loop you are about to perform: choose a process, place it in time, give it a destination, shape it, play it. Doing it once slowly is worth more than reading three pages about the process library.

The lesson also settles a distinction that causes real trouble later, between a **process** and the **slot** that draws it. Resizing one is not resizing the other, and the interface uses the same gesture with a different modifier for each.

## Concepts

**The processes library.** The left panel's second face, `Ctrl+Shift+P`. It lists every process the installation provides, from automations to shaders. You place a process by dragging it from this list onto the timeline. The library is large; Lesson 14 is about navigating it by intent rather than by name.

**Automation.** A breakpoint curve that drives one value over the length of its interval. In the library it is called `automation (float)`, and it is the process to reach for whenever something should change continuously over a known stretch of time.

**Destination address.** An automation does nothing until it knows where to send its output. That destination is an address, in the `device:/parameter` form of Lesson 02, and it is set on the process, not on the interval.

**Domain: minimum and maximum.** A curve runs between 0 and 1 in its own space. The minimum and maximum map that space onto real values, and they are shown in the slot header. A curve that appears to do nothing is very often a curve mapped to a range where nothing audible or visible happens.

**Full-size edit.** Editing a curve inside a 140-pixel band is imprecise. Double-clicking the process name above the slot zooms that process to fill the editor; `Ctrl+Alt+↑`, or `Cmd+↑` on macOS, returns to the parent. This is not a different document, only a different magnification.

## Walkthrough: from empty document to running curve

![One interval named Fade in, holding a single automation whose slot header reads its destination address and its range]({{ site.img }}/04/04-01-first-automation.png)

1. **Start a new document.** You need a device to aim at. For now, either open `lesson-04.score` to borrow its `lesson` device, or read ahead to [Lesson 07]({{ site.baseurl }}/learn/07-osc-devices.html) and declare one; the rest of this lesson works either way.
2. **Make an interval.** Click and drag in the empty scenario editor. You get an interval with a state at each end. Give it about eight seconds; precision comes later, from the inspector.
3. **Open the processes library** with `Ctrl+Shift+P` and find `automation (float)`.
4. **Drag it onto the interval.** Release inside the interval. A slot appears containing a straight line rising from left to right: a one-segment linear automation, the default.
5. **Give it a destination.** Click the slot's top bar so the inspector describes the automation. Then drag a parameter from the `Device explorer` onto the inspector's address field. The slot header now reads something like `Automation (float).2 -> lesson:/level`, which is the same thing you read in Lesson 00's figure.
6. **Play it.** `space`. The playhead crosses the interval and the parameter ramps. Watch the value move in the device explorer as it goes, and stop with `↵`.
7. **Shape the curve.** Double-click inside the slot to add a breakpoint. Select a segment and `Shift+Drag` to bend it: that is curvature, not a new point. A slow start followed by a fast rise is two drags away, and it sounds and looks entirely different from the linear default.
8. **Edit it properly.** Double-click the process name above the slot to enter full-size edit, adjust precisely, then `Ctrl+Alt+↑` back out. Clicking the document name under the time ruler does the same.
9. **Set the range deliberately.** In the inspector, set the minimum and maximum to the values your parameter actually wants. Leaving 0 to 1 while driving a parameter that expects 0 to 127 is the most common cause of "the automation runs but nothing happens".
10. **Compare.** Open `lesson-04.score` and look at what you built against the reference: one interval named `Fade in`, one automation on `lesson:/level`, a curve with a slow start.

## Slot against process, in practice

Two gestures look almost identical and mean different things.

- **Dragging the blue dot** at a slot's top right along the timeline extends the *slot*, preserving the automation's length, which gives you room to keep writing. The curve you already drew does not stretch.
- **`Cmd+Drag`** on that same dot scales the automation as the slot changes, so the curve you drew stretches with it.

Knowing which one you want before you drag saves redrawing. The same distinction explains folding: `Ctrl+Alt+F` and `Ctrl+Alt+U` change how much room slots take, and change nothing about what runs.

One more thing about that default straight line: it is a single segment, and a single segment is the least interesting automation you can write. Readers who never move past it conclude that automations are ramps. They are curves, and the two gestures in step 7 are what separate the two ideas.

## What the inspector tells you about an automation

With an automation selected, the inspector's lower half is the authoritative view of it, and it is worth reading in full once so that you know what can be set precisely rather than by gesture.

**Its start and duration**, as numbers. Dragging is convenient and imprecise; if a section must be exactly eight seconds, type it.

**Its destination address**, which you can also edit here by hand rather than by dragging a parameter onto it. Useful when the address needs a suffix, which is [Lesson 08]({{ site.baseurl }}/learn/08-units-ranges-types.html).

**Its minimum and maximum**, the two numbers that map the curve's own 0-to-1 space onto real values. These are the same numbers printed in the slot header, and they are the first thing to check when a curve appears to have no effect.

**Its parent interval**, in the upper half. This matters more than it looks: it is how you confirm that the process you are editing belongs to the interval you think it does, which is easy to get wrong once slots are stacked.

One further control deserves a mention now and a lesson later. An automation can be set to *tween* mode, in which it interpolates from wherever the parameter currently is rather than from its own written start value. That is how a cue-driven piece avoids jumps when a section is entered from an unexpected condition, and [Lesson 10]({{ site.baseurl }}/learn/10-automation-curves.html) returns to it.

## Common mistakes

- **An automation with no address.** It runs, it draws, it sends nothing. Check the slot header first: no `->` means no destination.
- **A range left at 0 to 1** on a parameter that wants something else. Nothing appears broken; nothing appears to happen either.
- **Confusing curvature with a breakpoint.** Double-click adds a point; `Shift+Drag` bends a segment. Readers who only know the first end up with twenty points where two and a bend would do.
- **Editing inside the band.** For anything precise, use full-size edit. The usability study noted that people enter these zoomed views by accident and cannot get out; entering deliberately, and knowing `Ctrl+Alt+↑`, converts that into a tool.
- **Assuming the interval owns the destination.** Two automations in one interval can drive two different parameters, because the destination belongs to each process.

## Exercise

Build a ten-second interval containing two automations that drive two different parameters of the same device: one rising with a slow start, one falling in a straight line. Then, without changing either curve, make the interval fifteen seconds long and decide, before you drag, whether you want the curves to stretch or to keep their shape. Do it both ways and keep the version you prefer.

**Success criterion:** you can say which gesture stretched the curves and which preserved them, and both automations show a `->` destination in their slot headers. If either parameter did not move when you played the score, check the range before anything else.

## Going further

- [Writing automations]({{ site.docs_baseurl }}/quick-start/writing-automations.html), the reference version of this walkthrough.
- [The automation process]({{ site.docs_baseurl }}/processes/automation_float.html), for every option this lesson skipped, including tween mode.
- [States and automations in practice]({{ site.docs_baseurl }}/quick-start/states-and-automations-in-practice.html), which [Lesson 09]({{ site.baseurl }}/learn/09-states-snapshots-presets.html) takes up in full.
- [Automations in depth]({{ site.docs_baseurl }}/in-depth/automations.html), which [Lesson 10]({{ site.baseurl }}/learn/10-automation-curves.html) builds on.
