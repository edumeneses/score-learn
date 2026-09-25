---
layout: default
title: "Lesson 05: Saving a project, media paths, and reopening"
description: "What a .score file contains, what it only points at, and how to package a project so it opens on another machine."
parent: Lessons
nav_order: 5
unit: "05"
permalink: /learn/05-saving-and-reopening.html
score_version: "3.8.2"
reading_time: "10 min"
practice_time: "10 min"
score_file: 04-first-process/lesson-04.score
---

# Lesson 05: Saving a project, media paths, and reopening

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 04]({{ site.baseurl }}/learn/04-first-process.html), so that you have a document of your own to save.
>
> **You will need** the interval and automations you built, your sketch from Lesson 01, and a text editor.
>
> **You will build** a project layout that survives being moved to another machine, and the reflex of reading your own score as text when the interface will not tell you something.

## Why this matters

This lesson is short and unglamorous, and it prevents the single most demoralising failure in this field: a piece that worked in the studio and does not open at the venue. The principle is not specific to *score*, whereas the detail is, because you need to know which parts of a document are self-contained and which are references to the outside world.

A second reason concerns the file format, since a `.score` file is JSON (JavaScript Object Notation), which means you can read it, search it, and put it under version control usefully; every example score in this course was produced that way. You will not hand-write documents in this course. However, knowing that you *could* changes how you debug them.

## Concepts

### What the file contains

The file contains the whole temporal structure, which means every process and its settings, every state's messages, and the declarations of the devices the document expects, including their protocol settings; opening `lesson-04.score` in a text editor lets you find `lesson:/level` as plain text.

### Referenced media and code

The file only points at media and code that it does not embed, such as sound files, video files, images, 3D models, shader and script files, and plug-ins, for which the document stores a path. However, if the path breaks, the structure still opens while the content is missing, which is a much better failure than not opening at all, and still a failure.

### Relative and absolute paths

A relative path survives a move, whereas an absolute path does not. A path relative to the document, which the file writes as `<PROJECT>:`, survives being moved as a set, while an absolute path survives only on the machine that wrote it. A third form, `<LIBRARY>:`, is relative to the user library, so a packaged sound follows the package instead of the document; keeping media beside the score removes both problems.

### Devices as expectations

Devices are expectations rather than equipment, so reopening a document on a machine with no synthesiser attached still opens the score, because the device declaration is present while the connection is not live. This is why a score can be authored on a laptop and run on a rig, and it is the practical payoff of the separation [Lesson 06]({{ site.baseurl }}/learn/06-device-model.html) explains.

## Walkthrough: package a project properly

![The project folder panel, listing the documents that sit beside the score]({{ site.img }}/05/05-01-project-folder.png)

1. **Make a project directory**, one per piece, for example `~/score/fade-study/`, and put the `.score` file in it; the project folder panel, `Ctrl+Shift+L`, then lists what is in it, as in the figure. Furthermore, that panel, the left panel's fourth face, is the natural home for the media a score references, and the reason it exists at all.
2. **Put media beside the score** by copying rather than linking every sound file, image, and script the document uses into that directory, or a `media/` subdirectory of it.
3. **Re-point the document at the copies** by reselecting each media file from inside the project directory, so that the stored paths are the ones you control.
4. **Save, close, and reopen** the document, and confirm that no element is missing; this step is the only way to know that what you think is stored is stored.
5. **Read the file as text** by opening the `.score` in an editor and finding one address you recognise and one media path, because two minutes here makes the next diagnosis much faster.
6. **Move the whole directory** somewhere else on disk, for instance to `/tmp`, and open it again from there, because a reference that breaks now is an absolute path, and it is better found by you than by a technician during a load-in.
7. **Put it under version control**, if you use it, with `git init` in the project directory; because the document is JSON, a diff between two saves is readable, and you can see that yesterday's edit changed a curve instead of guessing.
8. **Save a fragment for reuse** by selecting part of your scenario and dragging it, with `Alt` held, into the user library, where *score* writes a `.scenario` file that you can drag back into any document. This is how you build a personal vocabulary of structures rather than rebuilding them.

## What "versioning" means here

The word covers two distinct operations, which this section separates because they are easy to confuse.

**Your versions are saves of your own work**, ideally in version control, and ideally with a message about intent, because a show that has run three times has three states you may need to return to.

**The software's version is recorded in every document**, which stores the version of *score* that wrote it. Newer builds open documents written by older ones. Conversely, the reverse is not guaranteed, so authoring on a nightly and playing back on a release is a risk to take knowingly or not at all; this is why the course pins {{ page.score_version }}, and why the version pin appears in the badge at the top of every lesson.

## Reading a document as text

A `.score` file becomes a diagnostic tool through three searches, none of which requires understanding the whole format.

**Search for an address**, for instance `lesson:/level`, and every process and every message that touches that parameter appears, which answers "what in this document writes to this thing", a question the interface makes you hunt for.

**Search for a file extension**, `.wav` or `.glsl` or `.js`, and every media and code reference in the document appears, with the exact path stored; this is the definitive answer to what a project depends on, and it is how you build the media list for the packaging step above.

**Search for `Tag`**, near the end of the file, which gives the version of *score* that wrote the document; when a colleague reports that a file misbehaves, this is the first thing to establish.

Reading the file is safe, whereas editing it by hand is not, because the format contains internal identifiers that refer to each other, and a hand edit that breaks one of those relations produces a document that fails to open instead of one that opens with a small error. In other words, use the text view to understand and to diagnose, and use the interface to change.

## Handing a score to someone else

Sending a colleague a `.score` file alone is the most common way to waste an afternoon of theirs, because each item the document only points at is missing. A complete handover consists of four things, which the following paragraphs list.

**The project directory** comes first, complete and as assembled above, so that media resolves.

**The version of *score* that wrote it** comes second, found near the end of the file as described above, and stated explicitly so that the recipient does not have to guess it from behaviour.

**The device expectations** come third, in plain language: what the document expects to talk to, over which protocol, on which ports. The declarations are in the file already. Nevertheless, a reader who does not yet know the piece should not have to reverse-engineer them from the device explorer.

**What is not included** comes last, most importantly plug-ins such as VST (Virtual Studio Technology) instruments and any addon installed through the package manager, because a one-paragraph note saying "this needs the following two VSTs" turns a broken open into a five-minute install.

## Common mistakes

- **Media outside the project directory** works until the piece travels, and then it does not.
- **Assuming plug-ins travel** fails because a VST is not in the document, so a score that depends on one is a score with an installation requirement, and it should say so in writing, which [Lesson 34]({{ site.baseurl }}/learn/34-rehearsal-to-show.html) turns into a technical rider.
- **A single giant file per project** is permitted, although no part of it helps you when a section breaks, whereas fragments in the user library make structures reusable.
- **Skipping the reopen from a different location** forgoes a test that costs a minute and catches the whole class of path failures.
- **Treating the JSON as off-limits** wastes a supported, readable format, since reading it is a debugging technique, while editing it by hand is a last resort that is nevertheless useful to know about.

## Exercise

Make your sketch self-contained, because a document that plays only on the machine that made it is not yet a project.

1. **Read the sound's path** by opening `sketch.score` in a text editor and searching for `.wav`. The path begins with `<LIBRARY>:`, so the sketch plays on any machine with the same package installed and loses its sound everywhere else.
2. **Copy the excerpt into the sketch's folder** from `~/Documents/ossia/score/packages/citizen-dj-free-music/excerpts/`.
3. **Drag the copy from the project folder panel**, `Ctrl+Shift+L`, onto the timeline, then select the old sound's interval and delete it; redo the fade of Lesson 04 if you want it, since it belonged to the old sound.
4. **Save and read the file again**, where the path now begins with `<PROJECT>:`, relative to the document.
5. **Move or rename the folder**, reopen the sketch from its new place, and play.

**You are done when** the moved sketch plays its sound, and the file names it with `<PROJECT>:`.

## Going further

- [The course's own documents]({{ site.baseurl }}/downloads) are each packaged the way this lesson describes.
- [The project folder panel]({{ site.docs_baseurl }}/reference-manual/panels/) defines what *score* considers part of a project.
- [Presets]({{ site.docs_baseurl }}/presets.html) covers scenario fragments in the user library, which [Lesson 09]({{ site.baseurl }}/learn/09-states-snapshots-presets.html) uses again.
- [The package manager]({{ site.docs_baseurl }}/in-depth/package-manager.html) installs the addons a document may depend on.
- [Rehearsal to show]({{ site.baseurl }}/learn/34-rehearsal-to-show.html), later in the course, holds the full pre-performance checklist this lesson starts.

{% include lesson_files.html %}
