---
layout: default
title: "Lesson 20: Sound files and playback"
description: "Drop a file, loop it, fade it, analyse it, and keep its path portable: the sound file process and the media rules around it."
parent: Lessons
nav_order: 24
unit: "20"
permalink: /learn/20-sound-files.html
score_version: "3.8.2"
reading_time: "13 min"
practice_time: "25 min"
score_file: none
---

# Lesson 20: Sound files and playback

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 19]({{ site.baseurl }}/learn/19-audio-setup.html).
>
> **You will need** three or four sound files, ideally of different lengths and channel counts. Two ship with this lesson, drawn from the *Citizen DJ* packages; for more, install those packages through the package manager, per [Lesson 01]({{ site.baseurl }}/learn/01-install.html); they provide several thousand short, freely usable excerpts, and they appear in the user library ready to drag into a score.
>
> **You will build** a small sound-based document that plays, loops, fades, and reports what it is doing, and that travels without breaking.

## Why this matters

Playing a sound file is the easiest thing in this software: drag it in and it plays. That means this lesson can spend its time on the four things that are not obvious and that decide whether a sound-based piece survives production: looping, fading, analysis, and paths.

Paths in particular. Lesson 05 established that media is referenced rather than embedded; here it becomes concrete, because a piece with forty sound files is a piece with forty ways to break at a venue.

## Concepts

**Drag and drop, from anywhere.** A sound file can be dropped into the score from the user library or from the operating system's file manager. Dropping onto a scenario creates an interval containing it; dropping onto an existing interval adds it there.

**The interval's duration and the file's length are different things.** The interval is a stretch of time; the file has a length. Making the interval shorter does not shorten the file, it stops playing it early. This is obvious once stated and a frequent early confusion.

**Looping is a property.** Set in the sound file's inspector, which makes the file repeat for as long as its interval runs. This is the *process* loop of Lesson 17, not a structural loop, and the two combine: a looping file inside a looping interval is a legitimate and occasionally confusing construction.

**Fades are gain automations.** Per Lesson 19, every audio outlet carries a gain sub-port. Right-click it and create an automation. There is no separate fade object and no need for one.

**Analysis: the envelope process.** An **envelope** process turns an audio signal into a control value: its first output is a root-mean-square measure, its second a peak measure. Combined with a **signal display**, this puts a visible reading of the sound on the timeline, which is how you see what you are hearing.

**Routing audio into analysis removes it from the mix.** Because connecting a cable removes propagation, sending audio into an envelope means it stops reaching your ears. Switch **propagate** on in the source outlet's inspector to keep both. This is the single most common surprise in audio-reactive work, and Lesson 28 depends on knowing it.

**Portable paths.** A relative path is looked up in the project folder, meaning the directory containing the `.score` file. Two special prefixes make intent explicit: `<PROJECT>:/` resolves inside the project directory and `<LIBRARY>:/` inside the user library. Using them is how a document says where its media is supposed to come from instead of hoping.

## Walkthrough: from a file to a readable document

![Two intervals, each holding a sound file: the first plays once, the second loops to fill its interval]({{ site.img }}/20/20-01-sound-files.png)

The figure is `lesson-20.score`, which ships with this lesson: two excerpts from the Citizen DJ packages, one played once and one set to loop. Both are freely usable, and both are referenced with a project-relative path, so the document travels. See `checks/20-sound-files.md`.

1. **Make a project directory** and put your sound files in it, per Lesson 05, before you drop anything.
2. **Drop one file** onto an empty scenario. An interval appears containing the waveform. Play it.
3. **Shorten the interval** to half the file's length and play again: it stops early. Then lengthen it beyond the file: silence at the end. The interval is time, the file is content.
4. **Turn on looping** in the inspector and lengthen the interval again. Now the file repeats to fill it.
5. **Write a fade.** Right-click the gain port on the interval's audio outlet, create an automation, and draw a fade in and out. Play. Note that you did this without adding a process.
6. **Add a second file** in the same interval and play. Both are audible: each mixes into the parent, per Lesson 19's rule.
7. **Group them.** Put both into a sub-scenario and route that scenario's output through a single effect, which is the grouping technique from the previous lesson.
8. **Analyse.** Add an envelope process and a signal display, route the sound into the envelope and the envelope's first output into the display. Play, and watch the reading move with the sound.
9. **Notice the silence.** The sound has disappeared from your monitors, because the cable removed propagation. Turn propagate on in the source outlet's inspector to get both.
10. **Scale the reading.** If the display barely moves, insert a small mapping process between the envelope and the display to multiply it into a useful range, exactly as Lesson 13 taught.
11. **Make it portable.** Re-point each file using a path inside the project directory, save, move the whole directory elsewhere, and reopen. Nothing should be missing.

## Long files, many files

Two practical matters that decide whether a sound-heavy document stays workable.

**Long files.** A forty-minute file in a score is fine to play and awkward to work with, because the waveform drawing and the seeking both operate over the whole thing. When a long file is really a sequence of sections, splitting it into sections that match the score's structure makes the document rehearsable, per Lesson 18. When it is genuinely one continuous thing, keep it whole and use start markers instead.

**Many files.** Forty short files is a different problem: not performance, but legibility. Three habits help. Name intervals after their content rather than leaving default names, so a folded score is readable. Group related files into sub-scenarios, which also gives you one place to apply an effect. And keep the files themselves in a subdirectory of the project rather than beside the score, so the project directory has a structure a stranger can navigate.

Both cases share a rule: the structure of your media on disk should resemble the structure of your score. When those two diverge, every later change costs twice.

## Formats, and what to convert to

The choice of audio format matters less than in video and it is not free, so it is worth one decision made once.

**Uncompressed, for anything performed.** A file that decodes with no work is a file that will not glitch when the machine is busy with graphics. Disk space is cheap next to a dropout in front of an audience.

**Compressed, for long ambient material** where the file would otherwise be enormous and the timing is not critical. A forty-minute background bed is a reasonable exception.

**Sample rate should match the engine's.** A file at a different rate is converted at playback, which is work the machine does not need to do, and in some situations audibly.

**Channel count should be what you actually route.** A stereo file used as a mono source wastes a channel through every subsequent process; the fix belongs in the file, not in the score.

## Common mistakes

- **Expecting the interval to define the file's length.** It defines how long the file gets to play.
- **Looping in the wrong place.** A looping file and a looping interval are different statements; decide which you meant.
- **Adding a gain process** when the outlet already has a gain port.
- **Losing the sound when you add analysis.** Propagation was removed by the cable. Turn it back on.
- **An envelope reading that barely moves** and concluding the analysis is broken. It is scaled for signals, not for displays; insert a mapping.
- **Absolute paths.** They work until the piece travels, which is the definition of a bug in this field.
- **Dropping files from a downloads folder.** The path is now outside the project and the piece is one cleanup away from silence.

## Exercise

Build a two-minute document from at least four sound files: one that plays once, one that loops to fill its interval, two grouped through a shared effect, and one whose level is visibly analysed on the timeline with an envelope and a signal display while remaining audible. Then move the project directory and reopen it.

**Success criterion:** everything plays after the move, the analysed file is both audible and visible, and you can point at the setting that made both true at once. If your signal display is flat, scale it rather than assuming the envelope failed.

## Going further

- [Audio techniques]({{ site.docs_baseurl }}/common-practices/4-audio.html), including the analysis recipe used here.
- [The sound file process]({{ site.docs_baseurl }}/processes/soundfile.html) for every playback option.
- [Media management]({{ site.docs_baseurl }}/in-depth/media.html) for the `<PROJECT>:` and `<LIBRARY>:` prefixes.
- [Audio utilities]({{ site.docs_baseurl }}/processes/audio-utilities.html) for the envelope and its relatives.
