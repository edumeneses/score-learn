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

> **Before this lesson** finish [Lesson 02]({{ site.baseurl }}/learn/02-vocabulary.html); this lesson names places, and that one named things.
>
> **You will need** `lesson-00.score` open.
>
> **You will build** the ability to reach any part of the interface deliberately, and to get back when you end up somewhere unexpected.

## Why this matters

*score* puts everything in one window. That is a real advantage over tools that scatter work across floating palettes, and it has one cost: the window is dense, and a reader who does not know its regions experiences that density as clutter. The usability study is blunt here. Controls and shortcuts were rated two out of five. Interviewees reported losing objects and panels, and reported ending up in views they had not meant to enter, with no obvious way back.

This lesson is therefore mostly about orientation and recovery. Nothing in it produces an artefact; everything in it prevents twenty minutes of confusion later.

## Concepts

**Three areas.** The window is an explorer panel on the left, the scenario editor in the centre, and the object inspector on the right. Almost every action in the course is: find something on the left, put it in the middle, adjust it on the right.

**Four explorers, one panel.** The left panel is not only the device explorer, although that is its default face. Icons along its bottom switch it between the **device explorer** (the devices your project talks to), the **processes explorer** (the library of processes you can place), the **user library** (your own saved devices, presets, and process collections), and the **project folder** (the files belonging to the current document). Readers who never notice the switch conclude that *score* has no process library, and then wonder how anyone adds an automation.

**The inspector has two halves.** The top shows the selected object's structural context: for a process, the interval holding it; for a state, the instant it sits on and the intervals it links. The bottom shows the object's own parameters: durations, addresses, ranges. When you cannot find a setting, you are usually reading the wrong half.

**Zoom is two gestures.** `Ctrl` with the mouse wheel zooms horizontally, in time. `Shift` with the wheel zooms vertically, in space. They are independent, and confusing them accounts for a good share of "my score disappeared".

**Transport is not a tape deck.** The bar along the bottom shows position, play, and stop, plus a speed control and a master volume. Because a score can wait at a trigger and can branch, the position readout tells you where the playhead is in the document, not how far through a fixed duration you are.

## Walkthrough: the window, region by region

![The score window with its three areas, the explorer panel switch, the time ruler, and the transport bar marked]({{ site.img }}/03/03-01-window-regions.png)

1. **The explorer panel** and its title, `DEVICE EXPLORER`. With `lesson-00.score` open it lists one device, `lesson`. Expand it and click `level`: an inspector appears at the bottom of the panel showing that parameter's attributes, including its current value if the device echoes values back.
2. **The panel switch.** The row of icons at the bottom left changes which explorer is shown. Learn the four shortcuts instead: `Ctrl+Shift+D` device explorer, `Ctrl+Shift+P` processes library, `Ctrl+Shift+B` system library, `Ctrl+Shift+L` project library. Two more panels are worth knowing when something misbehaves: `Ctrl+Shift+C` opens the console and `Ctrl+Shift+G` the message log.
3. **The scenario editor**, the large central area. This is the only place where the document is edited. Above it is the time ruler, reading in minutes and seconds.
4. **The document breadcrumb**, just under the ruler, reading `lesson-00 /`. This tells you which level of the hierarchy you are looking at, and it is clickable. Remember it: it is your way out of a nested view.
5. **The object inspector** on the right, with its two halves. In the figure it is empty, because nothing is selected, and the panel above it is the history. Click `Approach` and read both halves.
6. **The transport bar**: position readout, play, stop, speed, and volume. Press `space` to play and `↵` to stop. Do it now with `lesson-00.score`: playback will run through `Approach` and then stop at the trigger, waiting. That is not a freeze. Click the trigger's T marker to release it and watch one of the two branches run.

## Moving around without getting lost

- **Zoom in time** with `Ctrl`+wheel; **zoom in height** with `Shift`+wheel. If everything looks wrong, zoom out in both before assuming you deleted something.
- **Navigate by structure** with the arrow keys: `↑`, `↓`, `→`, `←` move between linked elements on the timeline rather than by pixels. This is the fastest way to walk a score you did not write.
- **Go up a level** with `Ctrl+Alt+↑`, or `Cmd+↑` on macOS. This is the answer to "I double-clicked something and now I am inside it". The breadcrumb under the ruler does the same job with the mouse.
- **Fold and unfold** an interval's processes with `Ctrl+Alt+F` and `Ctrl+Alt+U`. Use this on a dense score before anything else; most of the apparent complexity is drawings, not structure.
- **Deselect** in the device explorer with `Esc`. Selection there is sticky, and a stale selection makes later drag-and-drop behave in ways that look random.
- **Right-click to edit precisely.** Most controls accept a typed value through their context menu, which matters as soon as you need a number rather than a gesture.

## The panels you need when something misbehaves

Four panels are worth knowing before you need them, because each answers a different question, and hunting for the right one while something is broken is a poor use of a rehearsal.

**The console**, `Ctrl+Shift+C`, reports what the application itself is doing: plug-ins loaded, devices connected, errors raised at startup. It is the first place to look when *score* behaves oddly rather than when your score does.

**The message log**, `Ctrl+Shift+G`, reports traffic: what has been sent and received. [Lesson 07]({{ site.baseurl }}/learn/07-osc-devices.html) builds a diagnostic routine on it, and it is the difference between "the cue did not work" and "the cue was sent to the wrong port".

**The history panel**, visible on the right in the figure above, lists your edits. Beyond undo, it tells you what you actually changed in the last ten minutes, which is useful when a document stops behaving and you cannot remember what you touched.

**The device explorer's own inspector**, at the bottom of the left panel, shows one parameter's attributes and lets you write to it directly. It is not a debugging panel by name, but testing a connection from there, before involving the timeline at all, isolates half of all faults.

## Common mistakes

- **Not knowing the left panel switches.** If the processes library seems missing, press `Ctrl+Shift+P`.
- **Reading a wait as a hang.** A score stopped at a trigger looks identical to a score that has crashed, except that the progress bar of the preceding interval has stopped at the trigger and the playhead has not moved. Lesson 15 makes this readable.
- **Collapsing a panel and losing its buttons.** The usability study flagged this specifically: reduced panels can hide controls, recoverable through a small and not very visible arrow. If a button vanished, widen the panel before searching the menus.
- **Zooming vertically when you meant horizontally.** The two gestures differ by one modifier and produce very different confusion.
- **Editing in the wrong half of the inspector**, then concluding a setting does not exist.
- **Assuming the position readout is a progress bar.** In a score with triggers and branches there is no single total duration to be a fraction of.

## Exercise

With `lesson-00.score` open and without using the mouse for navigation, do the following: reach the processes library, return to the device explorer, select the `Dark` interval using only arrow keys, fold and unfold its processes, and play the score until it waits at the trigger. Then deliberately get lost: double-click the name above an automation slot to enter its full-size view, and find your way back to the top of the document.

**Success criterion:** you can state which key returned you to the parent scenario, and you can describe what the score looked like while it was waiting at the trigger, in terms of the elements Lesson 02 named. If you could not tell waiting from stopped, write that down; Lesson 15 is where it gets resolved.

## Going further

- [Interface overview]({{ site.docs_baseurl }}/quick-start/interface-overview.html), the reference version of this tour.
- [Shortcuts]({{ site.docs_baseurl }}/reference-manual/references/shortcuts.html), the full list. Worth reading once in full; it is short.
- [Preferences]({{ site.docs_baseurl }}/reference-manual/references/preferences.html), including a global interface zoom, which is the right fix if the whole window is too small on a high-density display.
- [Panels]({{ site.docs_baseurl }}/reference-manual/panels/) for what each panel does in detail.
