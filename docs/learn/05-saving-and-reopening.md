---
layout: default
title: "Lesson 05: Saving, versioning, and reopening"
description: "What a .score file contains, what it only points at, and how to package a project so it opens on another machine."
parent: Lessons
nav_order: 5
unit: "05"
permalink: /learn/05-saving-and-reopening.html
score_version: "3.8.2"
reading_time: "10 min"
practice_time: "15 min"
score_file: 04-first-process/lesson-04.score
---

# Lesson 05: Saving, versioning, and reopening

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 04]({{ site.baseurl }}/learn/04-first-process.html), so you have a document worth saving.
>
> **You will need** the interval and automations you built, plus a text editor.
>
> **You will build** a project layout that survives being moved to another machine, and the habit of reading your own score as text when the interface will not tell you something.

## Why this matters

This lesson is short and unglamorous, and it prevents the single most demoralising failure in this field: a piece that worked in the studio and does not open at the venue. Nothing here is specific to *score*; what is specific is knowing exactly which parts of a document are self-contained and which are references to the outside world.

There is a second reason. A `.score` file is JSON, which means you can read it, search it, and put it under version control usefully. Every example score in this course was produced that way. You will not hand-write documents, but knowing that you *could* changes how you debug them.

## Concepts

**What the file contains.** The whole temporal structure, every process and its settings, every state's messages, and the declarations of the devices the document expects, including their protocol settings. Open `lesson-04.score` in a text editor and you can find `lesson:/level` as plain text.

**What the file only points at.** Media and code the document uses but does not embed: sound files, video files, images, 3D models, shader and script files, plug-ins. The document stores a path. If the path breaks, the structure still opens and the content is missing, which is a much better failure than not opening at all, and still a failure.

**Absolute against relative paths.** A path relative to the document survives being moved as a set. An absolute path survives nothing but the machine that wrote it. Keep media beside the score, in the project folder, and this problem stops existing.

**The project folder.** The left panel's fourth face shows the files belonging to the current document. It is the natural home for the media a score references, and the reason the panel exists at all.

**Devices are expectations, not equipment.** Reopening a document on a machine with no synthesiser attached still opens the score: the device declaration is present, the connection simply is not live. This is why a score can be authored on a laptop and run on a rig, and it is the practical payoff of the separation [Lesson 06]({{ site.baseurl }}/learn/06-device-model.html) explains.

## Walkthrough: package a project properly

![The project folder panel, listing the documents that sit beside the score]({{ site.img }}/05/05-01-project-folder.png)

1. **Make a project directory.** One directory per piece, for example `~/score/fade-study/`. Put the `.score` file in it. The project folder panel, `Ctrl+Shift+L`, then lists what is in it, as in the figure.
2. **Put media beside the score.** Copy, do not link, every sound file, image, and script the document uses into that directory, or a `media/` subdirectory of it.
3. **Re-point the document at the copies.** Reselect each media file from inside the project directory, so the stored paths are the ones you control.
4. **Save, close, and reopen.** Confirm nothing is missing. This step is not optional: it is the only way to know that what you think is stored is stored.
5. **Read the file as text.** Open the `.score` in an editor and find one address you recognise and one media path. Two minutes here makes the next diagnosis much faster.
6. **Move the whole directory** somewhere else on disk, for instance to `/tmp`, and open it again from there. Anything that breaks now is an absolute path, and better found by you than by a technician during a load-in.
7. **Put it under version control**, if you use it. `git init` in the project directory. Because the document is JSON, a diff between two saves is readable, and you can see that yesterday's edit changed a curve rather than guessing.
8. **Save a fragment for reuse.** Select part of your scenario and drag it, with `Alt` held, into the user library. *score* writes a `.scenario` file, which you can drag back into any document. This is how you build a personal vocabulary of structures rather than rebuilding them.

## What "versioning" means here

Two things, and they are worth separating.

**Your versions.** Saves of your own work, ideally in version control, ideally with a message about intent. A show that has run three times has three states worth being able to return to.

**The software's version.** Every document records the version of *score* that wrote it. Newer builds open older documents; the reverse is not guaranteed, so authoring on a nightly and playing back on a release is a risk you take deliberately or not at all. This is why the course pins {{ page.score_version }}, and why the version pin appears in the badge at the top of every lesson.

## Reading a document as text

Three searches turn a `.score` file into a diagnostic tool, and none of them requires understanding the whole format.

**Search for an address**, for instance `lesson:/level`. Every process and every message that touches that parameter appears. This answers "what in this document writes to this thing", which the interface makes you hunt for.

**Search for a file extension**, `.wav` or `.glsl` or `.js`. Every media and code reference in the document appears, with the exact path stored. This is the definitive answer to what a project depends on, and it is how you build the media list for the packaging step above.

**Search for `Tag`**, near the end of the file. That is the version of *score* that wrote the document. When a colleague reports that a file misbehaves, this is the first thing to establish.

A caution worth stating plainly: reading is safe, editing is not. The format contains internal identifiers that refer to each other, and a hand edit that breaks one of those relations produces a document that fails to open rather than one that opens with a small error. Use the text view to understand and to diagnose; use the interface to change.

## Handing a score to someone else

Sending a colleague a `.score` file alone is the most common way to waste an afternoon of theirs, because everything the document only points at is missing. A handover worth the name is four things.

**The project directory**, complete, as assembled above, so that media resolves.

**The version of *score* that wrote it.** Found near the end of the file, as described above, and worth stating explicitly rather than making them guess from behaviour.

**The device expectations**, in plain language: what the document expects to talk to, over which protocol, on which ports. The declarations are in the file, but a reader who does not yet know the piece should not have to reverse-engineer them from the device explorer.

**What is not included**, most importantly plug-ins and any addon installed through the package manager. A one-paragraph note saying "this needs the following two VSTs" turns a broken open into a five-minute install.

## Common mistakes

- **Media outside the project directory.** It works perfectly until the piece travels.
- **Assuming plug-ins travel.** A VST is not in the document. A score that depends on one is a score with an installation requirement, and it should say so in writing, which [Lesson 34]({{ site.baseurl }}/learn/34-rehearsal-to-show.html) turns into a technical rider.
- **One giant file per project.** Nothing forbids it, and nothing helps you when a section breaks. Fragments in the user library make structures reusable.
- **Never reopening from a different location.** The test costs a minute and catches the whole class of path failures.
- **Treating the JSON as off-limits.** It is a supported, readable format. Reading it is a debugging technique; editing it by hand is a last resort, but knowing it is possible is useful.

## Exercise

Package your Lesson 04 document as a self-contained project directory including at least one media file, even a placeholder sound. Move the directory to a different location and confirm it opens with nothing missing. Then save a two-interval fragment of it into the user library with `Alt+Drag`, start a new empty document, and drag the fragment back in.

**Success criterion:** the moved project opens with no missing media, and the fragment reappears in a fresh document with its structure intact. If a path broke, note whether it was absolute or relative; that distinction is the whole lesson.

## Going further

- [The course's own documents]({{ site.baseurl }}/downloads), every one of which is packaged the way this lesson describes.
- [The project folder panel]({{ site.docs_baseurl }}/reference-manual/panels/), for what *score* considers part of a project.
- [Presets]({{ site.docs_baseurl }}/presets.html), for scenario fragments in the user library, which [Lesson 09]({{ site.baseurl }}/learn/09-states-snapshots-presets.html) uses again.
- [The package manager]({{ site.docs_baseurl }}/in-depth/package-manager.html), for addons a document may depend on.
- [Rehearsal to show]({{ site.baseurl }}/learn/34-rehearsal-to-show.html), later in the course, for the full pre-performance checklist this lesson starts.
