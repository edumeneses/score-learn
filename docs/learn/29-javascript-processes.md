---
layout: default
title: "Lesson 29: JavaScript processes and scripting the score"
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

# Lesson 29: JavaScript processes and scripting the score

{% include lesson_meta.html %}

> **Before this lesson** finish [Milestone P6]({{ site.baseurl }}/learn/p6-fulldome-scene.html), since Phase 3 begins here.
>
> **You will need** a device with a couple of parameters, and the console panel, which opens with `Ctrl+Shift+C`.
>
> **You will build** a JavaScript process with its own ports, a script that holds state between ticks, and a console command that edits your score.

## Why this matters

Phase 3 addresses the point where the library runs out, because every lesson so far said "reach for a process" while this one says what to do when no process fits. JavaScript is the gentlest of the four scripting routes and the one with the widest reach, because it appears in three quite different places: as **a process** inside a score, with declared ports, running every tick; as **a console**, for one-off calculations and inspection; and as **a script that edits the document**, which is a different power, since a few lines can generate a hundred intervals, randomise every control in a process, or build structures that would take an afternoon by hand.

However, that third use is the one people do not expect, and it is the reason this lesson comes before the other scripting lessons.

## Concepts

### Declared ports

A process declares its ports, and the script is a process like any other. A script process begins by declaring inlets and outlets, which then appear on it like any other process's ports, automatable, cable-able, and addressable, so the script fits the model.

### The tick function

The tick function runs once per execution tick. It receives a token describing where in time it is and the current state, so that reading an inlet, computing, and writing an outlet is the whole shape of a control script.

### State between ticks

State between ticks is what separates a script from any combination of utilities. A script can keep variables across ticks, so that it can count, remember, and wait for a pattern of inputs, which no chain of utility processes can do. Furthermore, that state is the answer to the question Lesson 16 left open about where a condition's history can live.

### The console

The console is a read-evaluate-print panel with the same API (application programming interface). `Ctrl+Shift+C` opens it, and it is the right place to test a line before putting it in a script. Moreover, it doubles as a calculator, which is how the walkthrough first uses it.

### The scripting API

The scripting API edits the score itself. A global `Score` object exposes the document, so that you can find an object by its name, create intervals and processes, set addresses and curve points, undo, redo, and start and stop playback, while a `Util` object adds helpers such as reading a file. Because these are commands, they participate in undo, and wrapping a batch between a macro start and end makes the whole generated structure undoable in one step, which you will want the first time a script generates sixteen intervals you did not intend.

## Walkthrough: three uses, smallest first

![The script editor open on the shipped average example, the console panel below it having evaluated 2+2, and the ports the script declared listed in the process inspector]({{ site.img }}/29/29-01-script-editor-and-console.png)

The script in the figure is `average`, one of the JavaScript examples that ships in the process library under `Script > Javascript`, and it is a better starting point than an empty editor because it contains every element the lesson describes. Its first three lines declare a `ValueInlet`, a `ValueOutlet`, and an `IntSlider`, and those declarations are what produced the two ports and the `milliseconds` control that the inspector lists on the right; `property var avg: []` is the state that survives between ticks, and `tick: function(token, state)` takes the token and the state described above. Additionally, the console below it has evaluated `2+2` and answered `4`.

{: .note }
> **The editor opens in a window of its own**, so that you can leave it open beside the score. It carries two tabs, `Execution` and `GUI`, a log pane under the code where errors appear, and `Clear log`, `Close`, and `Compile` along the bottom, while the button that opens it is on the process's header in the score and again in the process inspector.

1. **Open the console** and evaluate something trivial, such as `2+2`, to confirm that you have a working environment; the panel announces itself as a JavaScript ES7 environment when it opens.
2. **Inspect the score from the console** by selecting an interval, then evaluating a call that returns the selected object and printing it, so that you hold a piece of your document in a variable.
3. **Play it from the console** by calling the play function on that object, which is a useful rehearsal tool.
4. **Add a JavaScript process** to an interval, and open its editor with the window button on its header.
5. **Declare one value inlet and one value outlet**, write a tick that doubles the input, and compile, so that two ports appear.
6. **Cable it in** by feeding it from an automation and sending its output to a device parameter, then play and confirm the doubling.
7. **Add state** by keeping a counter across ticks and outputting it, so that the process does something no stateless utility could; compile and watch it climb.
8. **Make it wait for a pattern** by extending the script to output only after the input has crossed a threshold three times, which is the shape of most useful control scripts.
9. **Generate structure** by writing, in the console, a short loop that creates several intervals after a selected state, each with a process, wrapped in a macro; run it, look at what appeared, and undo it in one step.
10. **Randomise a process** by writing a function that walks a process's inlets, reads each one's type and range, and sets a random value within it; this is the canonical example.
11. **Install it as an action** by putting a module in the system library that registers your randomiser in the `Scripts` menu with a shortcut, and use it from the menu.

    {: .note }
    > **Scripts can live in the library and register in the menu.** A `.js` file in the user library can be double-clicked to run in the global context, and a JavaScript module in the system library can register actions in the application's `Scripts` menu, with keyboard shortcuts, by exporting an `initialize` function and an `actions` array; that is how a personal tool becomes part of your interface.

## When to script, and when not to

The judgement deserves stating plainly, because both errors are common and expensive: scripting what a process already does, and building by hand what a loop would generate.

**Script when the behaviour is stateful or conditional.** Counting, remembering, waiting for a sequence, and applying a rule that depends on history are each a few lines of code, whereas the same behaviour in utility objects needs an unbounded number of them.

**Script when you are generating.** Sixteen similar intervals, forty addresses, or a set of randomised variants are the work of a loop, and the macro makes that loop safe.

**Do not script what a process already does.** A mapping curve is visible to a collaborator, editable without reading code, and impossible to get subtly wrong. In contrast, a script that reimplements it is a liability.

**Do not script the structure of a piece that you intend to edit later.** Generated structure is a starting point, and once it exists it is an ordinary document, so the script that made it becomes a tool and not the source of truth; keep the script, but do not expect to maintain the piece by editing it.

**Prefer a script inside a process to a script that edits the document when both would work.** A process is part of the score, versioned with it, and legible in the graph, whereas a document-editing script is a tool that lives beside it.

## The three places code lives

The same language in three contexts does three different jobs, and conflating them wastes an afternoon.

**Inside a process, code computes values.** It runs every tick, reads its inlets, and writes its outlets; it cannot edit the document, and it should not need to, because it is a signal-processing object that happens to be written in JavaScript.

**In the console, code inspects and drives.** It runs once, when you evaluate it, and it can see and change the document, play objects, and undo. In other words, the console is a workbench and not part of the piece.

**In the library, code becomes a tool.** It runs when you double-click it or when you fire its menu action, with the same powers as the console but saved, named, and available in every project, which is how a one-off experiment becomes something you use for years.

A useful test is whether the code should happen while the piece runs, in which case it is a process, or while you work, in which case it is a console line or a library script. However, code that tries to be both is usually a process that would have been simpler as two.

## Common mistakes

- **Editing and not compiling**, whereas the engine runs the compiled version.
- **Expecting a process script to edit the document**, although the editing API belongs to the console and library scripts.
- **Generating without a macro**, and then discovering that undo takes sixteen presses.
- **Scripting a mapping**, when the process is visible and editable.
- **Holding state and forgetting to reset it**, so that a counter that never resets makes a piece behave differently on the second run, which is the fault Milestone P1 warned about.
- **Reaching for the console for something a port would do**, although ports are the interface and the console is for tools.
- **Not saving useful scripts to the library**, when the randomiser you wrote once belongs in the menu.

## Exercise

The exercise covers the three places code lives. Write a process script that outputs a value only after its input has crossed a threshold three times, with the counter reset on a second inlet; write a console one-liner that finds an interval by name and plays it; and write a library script, registered in the `Scripts` menu with a shortcut, that randomises every control of the selected process within each control's declared range.

**Success criterion:** the process behaves correctly on a second run without reloading the document, the console line works on any named interval, and the menu action is undoable in one step. If the randomiser produced values outside a control's range, you read the range from the wrong place.

## Going further

- [Scripting]({{ site.docs_baseurl }}/in-depth/scripting.html), which contains the worked generation examples this lesson describes.
- [The scripting API]({{ site.docs_baseurl }}/in-depth/scripting-api.html), the complete reference for the `Score` object.
- [The JavaScript process]({{ site.docs_baseurl }}/processes/javascript.html) for the process form and its port declarations.
- [The console]({{ site.docs_baseurl }}/reference-manual/panels/), and [live coding]({{ site.docs_baseurl }}/common-practices/8-live-coding.html) for the compile loop.
