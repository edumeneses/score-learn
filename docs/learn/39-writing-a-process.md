---
layout: default
title: "Lesson 39: Writing your own process"
description: "Build score from source or use its SDK, write a process with Avendish where inputs are struct members, and publish it as an addon."
parent: Lessons
nav_order: 45
unit: "39"
permalink: /learn/39-writing-a-process.html
score_version: "3.8.2"
reading_time: "15 min"
practice_time: "60 min"
score_file: none
---

# Lesson 39: Writing your own process

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 38]({{ site.baseurl }}/learn/38-reading-the-docs.html).
>
> **You will need** CMake, Ninja, a C++ compiler, and on macOS Xcode. A day, realistically, for the first one.
>
> **You will build** a process of your own that appears in the library like any other, from the project's plug-in template.

## Why this matters

This is the last lesson because it is the last resort, and because everything before it usually suffices. Module J gave you four ways to write behaviour without leaving the application. A compiled process is worth building for three reasons the scripts cannot cover: an algorithm that must run at full speed with no compile-at-load step, an existing C++ codebase you want to use, and something you intend to give to other people as an installable addon.

The good news is that the barrier is much lower than it was. The **Avendish** API describes a process as a plain C++ structure whose inputs and outputs are simply **struct members**, requiring no library to be included, not even the standard one. Objects written this way are also not tied to *score*: the same code can be exported to other systems, including as a VST, which changes the economics of writing one.

## Concepts

**Two APIs, and you want the first.** *score* has its own internal plug-in API, which is powerful and verbose, and **Avendish**, which is declarative and much smaller. For a process, Avendish is the recommended route; the internal API is for extending the application itself rather than adding an object.

**Inputs and outputs are struct members.** You declare a structure, give it members for its ports, and write the processing function. The port names and ranges you declare become the ports you have been using all course, which is why your object behaves like a built-in one from the first build.

**No dependencies by design.** An Avendish object needs no headers of its own, which is what makes the objects portable to other hosts and easy to reason about.

**Several kinds of object.** Not only audio effects: control processes, generators, and others. Choose the kind that matches what you are making before writing code, because it determines the shape of the structure.

**Two ways to build.** Either **build *score* from source**, which gives you everything and takes the longest, or download the **SDK** and build only your plug-in against it, which is much faster and is what the template expects. For a first process, take the SDK route.

**A template exists.** The project provides a GitHub template for a dynamic *score* plug-in: create a repository from it, install CMake and Ninja, point the build at the SDK, and you have a compiling addon before you have written any of your own logic. Starting from a compiling skeleton rather than from a blank file is the single best piece of advice in this lesson.

**Publishing.** A built addon can be installed through the package manager, which is how the Faust libraries and shader collections you used in Modules G and I arrived. That is the path from "I wrote something" to "other people use it".

## Walkthrough: from template to library entry

{: .note }
> A figure for this lesson is pending: it needs the plug-in template's build output and the new process appearing in the library, which requires a full toolchain and interaction. See `checks/39-writing-a-process.md`.

1. **Read the Avendish documentation first.** An hour there saves a day of guessing, because the whole model is small and unusual enough that intuition from other plug-in formats misleads.
2. **Decide what kind of object you are making**, and check honestly whether a Faust script or a JavaScript process would do. If either would, do that instead and stop here.
3. **Create a repository from the template** rather than starting a project by hand.
4. **Install the toolchain**: CMake and Ninja on every platform, plus Xcode on macOS.
5. **Get the SDK** through the application's settings, and note whether you took the release or the continuous build, because that determines the path you configure.
6. **Configure and build the untouched template.** Do not write anything of your own yet: confirm that the skeleton compiles and that the resulting object appears in *score*'s library. This step is where a first attempt usually fails, and finding out with no code of your own is much cheaper.
7. **Now change one thing.** Rename the object and add one input member. Rebuild, and confirm the new port appears.
8. **Implement your actual processing**, in the smallest form that does something. Rebuild, drop it in a score, and cable it up.
9. **Automate one of its ports** from the timeline. Your object is now indistinguishable from a built-in process from the score's point of view, which is the moment the work pays off.
10. **Test it where it will run.** If the piece will be deployed to the embedded target of Lesson 35, build for that architecture too, and find out now rather than at the installation.
11. **Package it as an addon**, and install it through the package manager on a second machine to confirm the distribution path works.
12. **Document it.** One page: what it does, its ports and their ranges, and one example score. Without this it is a private tool rather than a contribution.

## Before you write C++

Four questions to answer honestly, because a compiled process carries a maintenance cost that scripts do not.

**Would a Faust script do?** For anything processing audio, usually yes, and the script travels inside the document, per Lesson 31, and compiles for the machine including ARM.

**Would a JavaScript process do?** For control-rate logic with state, usually yes, and it needs no toolchain.

**Would just-in-time C++ do?** If you need C++ specifically but not distribution, the process from Lesson 30 gives you the language without the build system.

**Will anyone else use it?** This is the question that actually justifies a compiled addon. If the answer is yes, the packaging and documentation work is worth it; if the answer is no, one of the three routes above is less work forever.

When the answer to all four points at a real plug-in, build it. Then contribute it, because the ecosystem this course depends on is made of exactly that.

## Contributing, not only building

The last thing worth saying in the last lesson: this software exists because people contributed to it, and the barrier to joining that list is lower than it looks.

**A documentation page** is the smallest useful contribution and the most needed one, per Lesson 38. If you understood something the hard way, the page you wished existed is a contribution you are uniquely placed to write.

**A preset or a fragment** in the user library. The shader you adapted, the conditioning chain you tuned, the cue structure you use in every piece: all of these are useful to somebody else and cost nothing to publish.

**An example score.** For anything you found underdocumented, a small working document is worth more than paragraphs, and this course's own experience confirms it: the shipped examples answered questions no page did.

**A process**, which is this lesson, and the largest of the four.

**A bug report with a reproduction**, which is a contribution even though it does not feel like one.

You have now spent a course's worth of time with a tool that a small number of people gave away. The reciprocal act does not have to be code.

## Common mistakes

- **Writing code before the template compiles.** Then two classes of problem are indistinguishable.
- **Choosing the internal API** for something Avendish handles.
- **Skipping the Avendish documentation**, and importing assumptions from another plug-in format.
- **Building only for your own architecture**, then discovering at deployment that the target needs another.
- **No documentation.** An undocumented addon is a private tool.
- **Reaching for a plug-in when a script would do**, which is the recurring theme of Module J.
- **Not publishing it.** If it was worth writing, somebody else has the same problem.

## Exercise

Build the untouched template until the object appears in *score*'s library, then modify it minimally: rename it, add one declared input, and make it do something you can verify, however trivial. Automate its new port from a score and confirm it behaves.

**Success criterion:** your object appears in the library, its port is automatable, and you can state which of the four questions above justified compiling it rather than scripting it. If none of them did, that is a legitimate result: you have learned the route exists and confirmed you do not need it yet.

## Going further

- [Plug-ins]({{ site.docs_baseurl }}/development/plug-ins.html) for the choice between the two APIs.
- [Plug-ins with Avendish]({{ site.docs_baseurl }}/development/plugins/plugins-with-avendish.html) and the [Avendish documentation](https://celtera.github.io/avendish).
- [Building from source]({{ site.docs_baseurl }}/development/build-from-source.html), if you need the whole application.
- [The architecture]({{ site.docs_baseurl }}/development/architecture.html), and [score-addon-tutorial](https://github.com/ossia/score-addon-tutorial) for the older API by example.
