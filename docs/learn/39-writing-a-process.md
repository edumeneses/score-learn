---
layout: default
title: "Lesson 39: Writing your own process in C++ with Avendish"
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

# Lesson 39: Writing your own process in C++ with Avendish

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 38]({{ site.baseurl }}/learn/38-reading-the-docs.html), since the contribution this lesson ends on builds on the reporting practice described there.
>
> **You will need** CMake, Ninja, a C++ compiler, and on macOS Xcode, together with a day, realistically, for the first process.
>
> **You will build** a process of your own that appears in the library like any other, starting from the project's plug-in template.

## Why this matters

This is the last lesson because it describes the last resort, and because the lessons before it usually suffice. Module J gave you four ways to write behaviour without leaving the application, so a compiled process is justified by three needs that the scripts cannot cover: an algorithm that must run at full speed with no compile-at-load step, an existing C++ codebase you want to use, and an object you intend to give to other people as an installable addon.

However, the barrier to writing one is much lower than it was, because the **Avendish** API (application programming interface) describes a process as a plain C++ structure whose inputs and outputs are **struct members**, requiring no library to be included, not even the standard one. Moreover, objects written this way are not tied to *score*, since the same code can be exported to other systems, including as a VST (Virtual Studio Technology), which changes the economics of writing one.

## Concepts

### Avendish and the internal API

Of the two APIs available, Avendish is the one to choose. *score* has its own internal plug-in API, which is capable and verbose, and it has **Avendish**, which is declarative and much smaller. For a process, Avendish is the recommended route, whereas the internal API serves those extending the application itself instead of adding an object to it.

### Ports as struct members

Inputs and outputs are struct members, so you declare a structure, give it members for its ports, and write the processing function; the port names and ranges you declare become the ports you have been using all course, which is why your object behaves like a built-in one from the first build.

### An API without dependencies

The API has no dependencies by design, because an Avendish object needs no headers of its own. In other words, the objects stay portable to other hosts and easy to reason about.

### Kinds of object

Several kinds of object are possible, since the API covers control processes, generators, and others as well as audio effects. Choose the kind that matches what you are making before writing code, because the kind determines the shape of the structure.

## Walkthrough: from template to library entry

{: .note }
> A figure for this lesson is pending: it needs the plug-in template's build output and the new process appearing in the library, which requires a full toolchain and interaction. See `checks/39-writing-a-process.md`.

1. **Read the Avendish documentation first**, because an hour there saves a day of guessing; the model is small and unusual enough that intuition from other plug-in formats misleads.
2. **Decide what kind of object you are making**, and check whether a Faust script or a JavaScript process would do; if either would, do that instead and stop here.
3. **Create a repository from the template** instead of starting a project by hand, because the project publishes a GitHub template for a dynamic *score* plug-in, which gives you a compiling addon before you have written any of your own logic. Starting from a compiling skeleton, and not from a blank file, is the single most useful piece of advice in this lesson.
4. **Install the toolchain**, which means CMake and Ninja on every platform, plus Xcode on macOS.
5. **Get the SDK** through the application's settings, and note whether you took the release or the continuous build, because that choice determines the path you configure.

   {: .note }
   > **There are two ways to build**, and **building *score* from source** gives you the whole application while taking the longest. In contrast, downloading the **SDK** (software development kit) and building only your plug-in against it is much faster and is what the template expects, so for a first process take the SDK route.

6. **Configure and build the untouched template** without writing anything of your own yet, and confirm that the skeleton compiles and that the resulting object appears in *score*'s library. This step is where a first attempt usually fails, and finding out with no code of your own is much cheaper.
7. **Change one thing** by renaming the object and adding one input member, then rebuild and confirm that the new port appears.
8. **Implement your actual processing** in the smallest form that does something, then rebuild, drop it in a score, and cable it up.
9. **Automate one of its ports** from the timeline, at which point your object is indistinguishable from a built-in process from the score's point of view, which is the moment the work pays off.
10. **Test it where it will run**, which means that if the piece will be deployed to the embedded target of Lesson 35, you build for that architecture too, and find out now instead of at the installation.
11. **Package it as an addon**, and install it through the package manager on a second machine to confirm that the distribution path works. The package manager is how the Faust libraries and shader collections you used in Modules G and I arrived, and it is the path from "I wrote something" to "other people use it".
12. **Document it** on one page that states what it does, its ports and their ranges, and one example score, because without that page it is a private tool instead of a contribution.

## Before you write C++

A compiled process carries a maintenance cost that scripts do not, so four questions should be answered before the toolchain is installed.

**Would a Faust script do?** For an object that processes audio, the answer is usually yes, and the script travels inside the document, as Lesson 31 showed, and compiles for the machine it runs on, including ARM.

**Would a JavaScript process do?** For control-rate logic with state, the answer is usually yes, and it needs no toolchain.

**Would just-in-time C++ do?** If you need C++ specifically but not distribution, the process from Lesson 30 gives you the language without the build system.

**Will anyone else use it?** This is the question that justifies a compiled addon, because if the answer is yes, the packaging and documentation work is justified. However, if the answer is no, one of the three routes above is less work for as long as the piece exists.

When the answers to all four point at a real plug-in, build it, and then contribute it, because the ecosystem this course depends on is made of such contributions.

## Contributing, not only building

The last thing to say in the last lesson is that this software exists because people contributed to it, and the barrier to joining that list is lower than it looks.

**A documentation page** is the smallest useful contribution and the most needed one, as Lesson 38 argued, and if you understood something the hard way, the page you wished existed is a contribution you are uniquely placed to write.

**A preset or a fragment** in the user library costs little to publish, and the shader you adapted, the conditioning chain you tuned, and the cue structure you use in every piece are all useful to somebody else.

**An example score** is the best answer to whatever you found underdocumented, because a small working document teaches more than paragraphs, and this course's own experience confirms it: the shipped examples answered questions that no page did.

**A process** is the subject of this lesson and the largest of the five kinds of contribution.

Additionally, **a bug report with a reproduction** is a contribution, even though it does not feel like one.

You have now spent a course's worth of time with a tool that a small number of people gave away, and the reciprocal act can take any of the five forms above, of which code is only the largest.

## Common mistakes

- **Writing code before the template compiles**, which makes two classes of problem indistinguishable.
- **Choosing the internal API** for an object that Avendish handles.
- **Skipping the Avendish documentation**, and importing assumptions from another plug-in format.
- **Building only for your own architecture**, then discovering at deployment that the target needs another.
- **Shipping no documentation**, so that the addon remains a private tool.
- **Reaching for a plug-in when a script would do**, which is the recurring theme of Module J.
- **Not publishing it**, although if it was worth writing, somebody else has the same problem.

## Exercise

Build the untouched template until the object appears in *score*'s library, then modify it minimally by renaming it, adding one declared input, and making it do something you can verify, however trivial. Automate its new port from a score and confirm that it behaves.

**Success criterion:** your object appears in the library, its port is automatable, and you can state which of the four questions above justified compiling it instead of scripting it. Nevertheless, if none of them did, that is a legitimate result, because you have learned that the route exists and confirmed that you do not need it yet.

## Going further

- [Plug-ins]({{ site.docs_baseurl }}/development/plug-ins.html) explains the choice between the two APIs and when each applies.
- [Plug-ins with Avendish]({{ site.docs_baseurl }}/development/plugins/plugins-with-avendish.html) and the [Avendish documentation](https://celtera.github.io/avendish) cover the recommended route in detail.
- [Building from source]({{ site.docs_baseurl }}/development/build-from-source.html) applies if you need the whole application.
- [The architecture]({{ site.docs_baseurl }}/development/architecture.html), and [score-addon-tutorial](https://github.com/ossia/score-addon-tutorial), show the older API by example.

{% include lesson_files.html %}
