---
layout: default
title: "Lesson 03: Interface layout and transport"
description: "The three areas of the score window, the four explorer panels, zooming, navigation, and what the transport bar actually controls."
parent: Lessons
nav_order: 3
unit: "03"
permalink: /learn/03-interface-and-transport.html
score_version: "3.8.2"
reading_time: "13 min"
practice_time: "20 min"
score_file: 00-what-score-is/lesson-00.score
---

# Lesson 03: Interface layout and transport

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 02]({{ site.baseurl }}/learn/02-vocabulary.html), because this lesson names places, whereas that one named things.
>
> **You will need** `lesson-00.score` open, since the walkthrough refers to it throughout.
>
> **You will build** the ability to reach any part of the interface on purpose, and to get back when you end up somewhere unexpected.

## Why this matters

*score* puts the whole working environment in one window, which is a real advantage over tools that scatter work across floating palettes. However, that arrangement has one cost: the window is dense, and a reader who does not know its regions experiences that density as clutter. The usability study documented that cost, since controls and shortcuts were rated two out of five, and interviewees reported losing objects and panels, and ending up in views they had not meant to enter, with no obvious way back.

In other words, this lesson is mostly about orientation and recovery, and although no step in it produces an artefact, each one prevents a stretch of confusion later, when the timeline is full and a lost panel matters more.

## Concepts

**The window has three areas**, which are an explorer panel on the left, the scenario editor in the centre, and the object inspector on the right; almost every action in the course follows the same path, which is to find something on the left, put it in the middle, and adjust it on the right.

**The left panel holds four explorers behind one frame.** The device explorer is its default face, although icons along its bottom switch it between the **device explorer** (the devices your project talks to), the **processes explorer** (the library of processes you can place), the **user library** (your own saved devices, presets, and process collections), and the **project folder** (the files belonging to the current document). Readers who do not notice the switch conclude that *score* has no process library, and then wonder how anyone adds an automation.

**The inspector has two halves that answer different questions.** The top shows the selected object's structural context, which for a process is the interval holding it, and for a state is the instant it sits on and the intervals it links. In contrast, the bottom shows the object's own parameters, such as durations, addresses, and ranges, so when you cannot find a setting, you are usually reading the wrong half.

**Zoom is two independent gestures**, since `Ctrl` with the mouse wheel zooms horizontally, in time, whereas `Shift` with the wheel zooms vertically, in space; confusing them accounts for a good share of "my score disappeared".

**The transport does not behave like a tape deck.** The bar along the bottom shows position, play, and stop, plus a speed control and a master volume. However, because a score can wait at a trigger and can branch, the position readout tells you where the playhead is in the document, whereas a tape counter would tell you how far through a fixed duration you are.

## Walkthrough: the window, region by region

![The score window with its three areas, the explorer panel switch, the time ruler, and the transport bar marked]({{ site.img }}/03/03-01-window-regions.png)

1. **The explorer panel** carries the title `DEVICE EXPLORER`, and with `lesson-00.score` open it lists one device, `lesson`. Expand it and click `level`, and an inspector appears at the bottom of the panel showing that parameter's attributes, including its current value if the device echoes values back.
2. **The panel switch** is the row of icons at the bottom left, which changes which explorer is shown, although the four shortcuts are faster to learn: `Ctrl+Shift+D` device explorer, `Ctrl+Shift+P` processes library, `Ctrl+Shift+B` system library, `Ctrl+Shift+L` project library. Additionally, two panels matter when something misbehaves, since `Ctrl+Shift+C` opens the console and `Ctrl+Shift+G` the message log.
3. **The scenario editor** is the large central area, and it is the only place where the document is edited; above it is the time ruler, reading in minutes and seconds.
4. **The document breadcrumb** sits just under the ruler, reading `lesson-00 /`, and it tells you which level of the hierarchy you are looking at; it is clickable, which makes it your way out of a nested view.
5. **The object inspector** on the right has the two halves described above, and in the figure it is empty because no object is selected, while the panel above it is the history. Click `Approach` and read both halves, so that the structural context and the parameters are seen side by side.
6. **The transport bar** holds the position readout, the four transport buttons, speed, and volume, and the `Play` menu names all four buttons and their shortcuts: play, `space`; play globally, `Shift+Space`; stop, `↵`; reinitialise, `Ctrl+↵`. Press `space` now with `lesson-00.score`, and playback will run through `Approach` and then stop at the trigger, waiting rather than frozen; click the trigger's T marker to release it and watch one of the two branches run.

## Moving around without getting lost

- **Zoom in time** with `Ctrl`+wheel and **zoom in height** with `Shift`+wheel, and if the view looks wrong, zoom out in both before assuming you deleted an object.
- **Navigate by structure** with the arrow keys, since `↑`, `↓`, `→`, `←` move between linked elements on the timeline instead of by pixels, which is the fastest way to walk a score you did not write.
- **Go up a level** with `Ctrl+Alt+↑`, or `Ctrl+↑` on macOS, which is the answer to "I double-clicked something and now I am inside it"; the breadcrumb under the ruler does the same job with the mouse.
- **Fold and unfold** an interval's processes with `Ctrl+Alt+F` and `Ctrl+Alt+U`, and use this on a dense score before any other step, because most of the apparent complexity comes from the drawings and only a little from the structure.
- **Deselect** in the device explorer with `Esc`, because selection there is sticky, and a stale selection makes later drag-and-drop behave in ways that look random.
- **Right-click to edit precisely**, since most controls accept a typed value through their context menu, which matters as soon as you need a number rather than a gesture.

## The panels you need when something misbehaves

Each of four panels answers a different question, and knowing them before you need them matters, because hunting for the right one while something is broken is a poor use of a rehearsal.

**The console**, `Ctrl+Shift+C`, reports what the application itself is doing: plug-ins loaded, devices connected, errors raised at startup. It is the first place to look when *score* behaves oddly, whereas a misbehaving document points elsewhere.

**The message log**, `Ctrl+Shift+G`, reports traffic, which means what has been sent and received. [Lesson 07]({{ site.baseurl }}/learn/07-osc-devices.html) builds a diagnostic routine on it, because it is the difference between "the cue did not work" and "the cue was sent to the wrong port".

**The history panel**, visible on the right in the figure above, lists your edits, and its first use is undo. Moreover, it tells you what you changed in the last ten minutes, which is useful when a document stops behaving and you cannot remember what you touched.

**The device explorer's own inspector**, at the bottom of the left panel, shows one parameter's attributes and lets you write to it directly. Although it is not a debugging panel by name, testing a connection from there, before involving the timeline at all, isolates half of all faults.

## Common mistakes

- **Not knowing that the left panel switches** makes the processes library seem missing, in which case `Ctrl+Shift+P` brings it back.
- **Reading a wait as a hang** is easy, because a score stopped at a trigger looks identical to a score that has crashed, except that the progress bar of the preceding interval has stopped at the trigger and the playhead has not moved; Lesson 15 makes this readable.
- **Collapsing a panel and losing its buttons** was flagged by the usability study specifically, since reduced panels can hide controls that are recoverable only through a small and not very visible arrow; if a button vanished, widen the panel before searching the menus.
- **Zooming vertically when you meant horizontally** happens because the two gestures differ by one modifier, although they produce quite different confusion.
- **Editing in the wrong half of the inspector** leads to the conclusion that a setting does not exist, when it sits in the other half.
- **Assuming the position readout is a progress bar** fails in a score with triggers and branches, because there is no single total duration to be a fraction of.

## Exercise

With `lesson-00.score` open and without using the mouse for navigation, do the following: reach the processes library, return to the device explorer, select the `Dark` interval using only arrow keys, fold and unfold its processes, and play the score until it waits at the trigger. Then get lost on purpose by double-clicking the name above an automation slot to enter its full-size view, and find your way back to the top of the document.

**Success criterion:** you can state which key returned you to the parent scenario, and you can describe what the score looked like while it was waiting at the trigger, in terms of the elements Lesson 02 named. If you could not tell waiting from stopped, write that down, because Lesson 15 is where that distinction gets resolved.

## Going further

- [Interface overview]({{ site.docs_baseurl }}/quick-start/interface-overview.html) is the reference version of this tour.
- [Shortcuts]({{ site.docs_baseurl }}/reference-manual/references/shortcuts.html) is the full list, which is short enough to read once in full.
- [Preferences]({{ site.docs_baseurl }}/reference-manual/references/preferences.html) includes a global interface zoom, which is the right fix if the whole window is too small on a high-density display.
- [Panels]({{ site.docs_baseurl }}/reference-manual/panels/) describes what each panel does in detail.
