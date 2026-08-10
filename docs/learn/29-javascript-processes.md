---
layout: default
title: "Lesson 29: JavaScript processes"
description: "Write a process in JavaScript: declared ports, the tick function, state between ticks, and the scripting API that edits the score itself."
parent: Lessons
nav_order: 35
unit: "29"
permalink: /learn/29-javascript-processes.html
score_version: "3.8.2"
reading_time: "14 min"
practice_time: "30 min"
score_file: none
---

# Lesson 29: JavaScript processes

{% include lesson_meta.html %}

> **Before this lesson** finish [Milestone P6]({{ site.baseurl }}/learn/p6-fulldome-scene.html). Phase 3 begins here.
>
> **You will need** a device with a couple of parameters, and the console panel, `Ctrl+Shift+C`.
>
> **You will build** a JavaScript process with its own ports, a script that holds state between ticks, and a console command that edits your score.

## Why this matters

Phase 3 is about the point where the library runs out. Every lesson so far said "reach for a process"; this one says what to do when no process fits. JavaScript is the gentlest of the four scripting routes and the one with the widest reach, because it appears in three quite different places:

**As a process** inside a score, with declared ports, running every tick. **As a console**, for one-off calculations and inspection. And **as a script that edits the document**, which is a genuinely different power: a few lines can generate a hundred intervals, randomise every control in a process, or build structures that would take an afternoon by hand.

That third use is the one people do not expect, and it is the reason this lesson comes before the other scripting lessons.

## Concepts

**A process declares its ports.** A script process begins by declaring inlets and outlets, which then appear on it like any other process's ports: automatable, cable-able, addressable. The script is a process, not an exception to the model.

**The tick function.** The body runs on each execution tick, receiving a token describing where in time it is and the current state. Reading an inlet, computing, and writing an outlet is the whole shape of a control script.

**State between ticks.** A script can keep variables across ticks, which is what makes it capable of things no combination of utility processes can do: counting, remembering, waiting for a pattern of inputs. This is also the answer to the question Lesson 16 left open, about where a condition's history can live.

**The console.** `Ctrl+Shift+C` opens a read-evaluate-print panel with the same API available. It is the right place to test a line before putting it in a script, and it doubles as a calculator.

**The scripting API edits the score.** A global `Score` object exposes the document: find an object by its name, create intervals and processes, set addresses and curve points, undo, redo, start and stop playback. A `Util` object adds helpers such as reading a file. Because these are commands, they participate in undo: wrapping a batch between a macro start and end makes the whole generated structure undoable in one step, which you will want the first time a script generates sixteen intervals you did not intend.

**Scripts in the library, and in the menu.** A `.js` file in the user library can be double-clicked to run in the global context. A JavaScript module in the system library can register actions in the application's `Scripts` menu, with keyboard shortcuts, by exporting an `initialize` function and an `actions` array. That is how a personal tool becomes part of your interface.

## Walkthrough: three uses, smallest first

{: .note }
> A figure for this lesson is pending: it needs the script editor and the console panel, both of which require interaction. See `checks/29-javascript-processes.md`.

1. **Open the console** and evaluate something trivial, `2+2`, to confirm you have a working environment.
2. **Inspect the score from the console.** Select an interval, then evaluate a call that returns the selected object and print it. You are now holding a piece of your document in a variable.
3. **Play it from the console.** Call the play function on that object. This alone is a useful rehearsal tool.
4. **Add a JavaScript process** to an interval, and open its editor with the window button on its header.
5. **Declare one value inlet and one value outlet**, and write a tick that doubles the input. Compile. Two ports appear.
6. **Cable it in.** Feed it from an automation and send its output to a device parameter. Play, and confirm the doubling.
7. **Add state.** Keep a counter across ticks and output it, so the process does something no stateless utility could. Compile and watch it climb.
8. **Make it wait for a pattern.** Extend the script to output only after the input has crossed a threshold three times. This is the shape of most useful control scripts, and it is where scripting earns its place.
9. **Generate structure.** In the console, write a short loop that creates several intervals after a selected state, each with a process, wrapped in a macro. Run it, look at what appeared, then undo it in one step.
10. **Randomise a process.** Write a function that walks a process's inlets, reads each one's type and range, and sets a random value within it. This is the canonical example, and it is genuinely useful when looking for material.
11. **Install it as an action.** Put a module in the system library that registers your randomiser in the `Scripts` menu with a shortcut, and use it from the menu.

## When to script, and when not to

The judgement is worth stating plainly, because both errors are common and both are expensive.

**Script when the behaviour is stateful or conditional.** Counting, remembering, waiting for a sequence, applying a rule that depends on history: these are a few lines of code and an unbounded number of utility objects.

**Script when you are generating.** Sixteen similar intervals, forty addresses, a set of randomised variants: a loop is the right tool, and the macro makes it safe.

**Do not script what a process already does.** A mapping curve is visible to a collaborator, editable without reading code, and impossible to get subtly wrong. A script that reimplements it is a liability.

**Do not script the structure of a piece if you want to edit it later.** Generated structure is a starting point. Once it exists, it is an ordinary document, and the script that made it is a tool rather than the source of truth. Keep the script, but do not expect to maintain the piece by editing it.

**Prefer a script inside a process to a script that edits the document**, when both would work. A process is part of the score, versioned with it, and legible in the graph; a document-editing script is a tool that lives beside it.

## The three places code lives

Worth separating explicitly, because the same language in three contexts does three different jobs and conflating them wastes an afternoon.

**Inside a process, computing values.** Runs every tick, reads its inlets, writes its outlets. It cannot edit the document, and it should not want to: it is a signal-processing object that happens to be written in JavaScript.

**In the console, inspecting and driving.** Runs once, when you evaluate it. It can see and change the document, play objects, and undo. This is a workbench, not part of the piece.

**In the library, as a tool.** Runs when you double-click it or when you fire its menu action. Same powers as the console, saved and named, available in every project. This is where a one-off console experiment becomes something you use for years.

A useful rule of thumb: if it should happen while the piece runs, it is a process. If it should happen while you work, it is a console line or a library script. Code that tries to be both is usually a process that would have been simpler as two.

## Common mistakes

- **Editing and not compiling.** The engine runs the compiled version.
- **Expecting a process script to edit the document.** A process computes values; the editing API is the console and library scripts.
- **Generating without a macro**, then discovering that undo takes sixteen presses.
- **Scripting a mapping.** Use the process; keep the code for what code is for.
- **Holding state and forgetting to reset it.** A counter that never resets is a piece that behaves differently on the second run, which is exactly the fault Milestone P1 warned about.
- **Reaching for the console for something a port would do.** Ports are the interface; the console is for tools.
- **Not saving useful scripts to the library.** The randomiser you wrote once is worth having in the menu.

## Exercise

Write three things. A process script that outputs a value only after its input has crossed a threshold three times, with the counter reset on a second inlet. A console one-liner that finds an interval by name and plays it. And a library script, registered in the `Scripts` menu with a shortcut, that randomises every control of the selected process within each control's declared range.

**Success criterion:** the process behaves correctly on a second run without reloading the document, the console line works on any named interval, and the menu action is undoable in one step. If the randomiser produced values outside a control's range, you read the range from the wrong place.

## Going further

- [Scripting]({{ site.docs_baseurl }}/in-depth/scripting.html), which contains the worked generation examples this lesson describes.
- [The scripting API]({{ site.docs_baseurl }}/in-depth/scripting-api.html), the complete reference for the `Score` object.
- [The JavaScript process]({{ site.docs_baseurl }}/processes/javascript.html) for the process form and its port declarations.
- [The console]({{ site.docs_baseurl }}/reference-manual/panels/), and [live coding]({{ site.docs_baseurl }}/common-practices/8-live-coding.html) for the compile loop.
