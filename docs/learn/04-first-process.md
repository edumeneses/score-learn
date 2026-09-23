---
layout: default
title: "Lesson 04: Your first automation"
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

# Lesson 04: Your first automation

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 03]({{ site.baseurl }}/learn/03-interface-and-transport.html), so that the panels and shortcuts below are familiar.
>
> **You will need** a new empty document, since `lesson-04.score` ships with this lesson as the finished result and is for comparison after you have built your own.
>
> **You will build** one interval holding one automation that drives one parameter from 0 to 1 over eight seconds.

## Why this matters

This is the first lesson that writes into a document, and every later lesson in the course is a variation on the loop you are about to perform: choose a process, place it in time, give it a destination, shape it, play it. Doing it once slowly teaches more than reading three pages about the process library, because the loop is what remains once the names of individual processes have been forgotten.

Furthermore, the lesson settles a distinction that causes real trouble later, between a **process** and the **slot** that draws it, because resizing one is a different operation from resizing the other, and the interface uses the same gesture with a different modifier for each.

## Concepts

### The automation process

An automation is a breakpoint curve that drives one value over the length of its interval. In the library it is called `automation (float)`, and it is the process to reach for whenever a value should change continuously over a known stretch of time.

### Automation destinations

An automation has no effect until it knows where to send its output. That destination is an address, in the `device:/parameter` form of Lesson 02. Moreover, it is set on the process, whereas the interval that holds the process carries no address of its own.

### Minimum and maximum

The minimum and maximum map the curve onto real values. A curve runs between 0 and 1 in its own space, and the minimum and maximum map that space onto the values the parameter expects, which is why they are shown in the slot header. However, a curve that appears to have no effect is often a curve mapped to a range where no audible or visible change happens.

## Walkthrough: from empty document to running curve

![One interval named Fade in, holding a single automation whose slot header reads its destination address and its range]({{ site.img }}/04/04-01-first-automation.png)

1. **Start a new document**, which needs a device to aim at: for now, either open `lesson-04.score` to borrow its `lesson` device, or read ahead to [Lesson 07]({{ site.baseurl }}/learn/07-osc-devices.html) and declare one, since the rest of this lesson works either way.
2. **Make an interval** by clicking and dragging in the empty scenario editor, which gives you an interval with a state at each end; give it about eight seconds, because precision comes later, from the inspector.
3. **Open the processes library** with `Ctrl+Shift+P`, the left panel's second face, which lists every process the installation provides, from automations to shaders; it is large, which is why Lesson 14 is about navigating it by intent rather than by name. Find `automation (float)`, which is the process this lesson uses.
4. **Drag it onto the interval** and release inside it, and a slot appears containing a straight line rising from left to right, which is a one-segment linear automation, the default.
5. **Give it a destination** by clicking the slot's top bar so that the inspector describes the automation, then dragging a parameter from the `Device explorer` onto the inspector's address field. The slot header now reads something like `Automation (float).2 -> lesson:/level`, which is the same header you read in Lesson 00's figure.
6. **Play it** with `space`, and the playhead crosses the interval while the parameter ramps; watch the value move in the device explorer as it goes, and stop with `↵`.
7. **Shape the curve** by double-clicking inside the slot to add a breakpoint, and by selecting a segment and using `Shift+Drag` to bend it, which changes curvature without adding a point. A slow start followed by a fast rise is two drags away, and it sounds and looks entirely different from the linear default.
8. **Edit it at full size**, because editing a curve inside a 140-pixel band is imprecise, by double-clicking the process name above the slot so that the process fills the editor, adjusting precisely, and then pressing `Ctrl+Alt+↑`, or `Ctrl+↑` on macOS, to come back out; clicking the document name under the time ruler does the same. The zoomed view is the same document at a different magnification, and knowing the way back is what turns it from a trap into a tool.
9. **Set the range on purpose** by entering, in the inspector, the minimum and maximum your parameter expects, because leaving 0 to 1 while driving a parameter that expects 0 to 127 is the most common cause of "the automation runs but nothing happens".
10. **Compare** what you built with the reference by opening `lesson-04.score`, which holds one interval named `Fade in`, one automation on `lesson:/level`, and a curve with a slow start.

## Slot against process, in practice

A pair of gestures look almost identical and mean different things, so knowing which one you want before you drag saves redrawing.

- **Dragging the blue dot** at a slot's top right along the timeline extends the *slot* while preserving the automation's length, which gives you room to keep writing, and the curve you already drew does not stretch.
- In contrast, **`Ctrl+Drag`** on that same dot scales the automation as the slot changes, so the curve you drew stretches with it.

The same distinction explains folding, because `Ctrl+Alt+F` and `Ctrl+Alt+U` change how much room slots take without changing what runs.

The default straight line deserves a final remark, since it is a single segment, and a single segment is the least interesting automation you can write. Readers who do not move past it conclude that automations are ramps. However, they are curves, and the two gestures in step 7 are what separate the two ideas.

## What the inspector tells you about an automation

With an automation selected, the inspector's lower half is the authoritative view of it, and reading it in full once shows you what can be set precisely rather than by gesture.

**Its start and duration** appear as numbers, and because dragging is convenient and imprecise, a section that must last precisely eight seconds should have that value typed.

**Its destination address** can be edited here by hand as well as by dragging a parameter onto it, which is useful when the address needs a suffix, the subject of [Lesson 08]({{ site.baseurl }}/learn/08-units-ranges-types.html).

**Its minimum and maximum** are the two numbers that map the curve's own 0-to-1 space onto real values; they are the same numbers printed in the slot header, and they are the first thing to check when a curve appears to have no effect.

**Its parent interval** appears in the upper half, which matters more than it looks, because it is how you confirm that the process you are editing belongs to the interval you think it does, a mistake that is easy to make once slots are stacked.

A further control deserves a mention now and a lesson later: an automation can be set to *tween* mode, in which it interpolates from wherever the parameter currently is instead of from its own written start value. That is how a cue-driven piece avoids jumps when a section is entered from an unexpected condition, and [Lesson 10]({{ site.baseurl }}/learn/10-automation-curves.html) returns to it.

## Common mistakes

- **An automation with no address** runs and draws its curve but sends no value anywhere, so check the slot header first, because a header without `->` means a process without a destination.
- **A range left at 0 to 1** on a parameter that wants another range produces no visible error, and it produces no visible effect either, which is why the range is the first setting to check.
- **Confusing curvature with a breakpoint** is common, because double-click adds a point while `Shift+Drag` bends a segment, and readers who only know the first end up with twenty points where two and a bend would do.
- **Editing inside the band** is imprecise, so use full-size edit for precise work; the usability study noted that people enter these zoomed views by accident and cannot get out. Nevertheless, entering on purpose, and knowing `Ctrl+Alt+↑`, converts that view into a tool.
- **Assuming the interval owns the destination** fails as soon as two automations in one interval drive two different parameters, which they can, because the destination belongs to each process.

## Exercise

Build a ten-second interval containing two automations that drive two different parameters of the same device: one rising with a slow start, one falling in a straight line. Then, without changing either curve, make the interval fifteen seconds long and decide, before you drag, whether you want the curves to stretch or to keep their shape; do it both ways and keep the version you prefer.

**Success criterion:** you can say which gesture stretched the curves and which preserved them, and both automations show a `->` destination in their slot headers. If either parameter did not move when you played the score, check the range before any other setting.

## Going further

- [Writing automations]({{ site.docs_baseurl }}/quick-start/writing-automations.html) is the reference version of this walkthrough.
- [The automation process]({{ site.docs_baseurl }}/processes/automation_float.html) lists every option this lesson skipped, including tween mode.
- [States and automations in practice]({{ site.docs_baseurl }}/quick-start/states-and-automations-in-practice.html) is the page that [Lesson 09]({{ site.baseurl }}/learn/09-states-snapshots-presets.html) takes up in full.
- [Automations in depth]({{ site.docs_baseurl }}/in-depth/automations.html) is the page that [Lesson 10]({{ site.baseurl }}/learn/10-automation-curves.html) builds on.
