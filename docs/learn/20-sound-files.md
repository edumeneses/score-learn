---
layout: default
title: "Lesson 20: Playing sound files: loops, fades, and envelopes"
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

# Lesson 20: Playing sound files: loops, fades, and envelopes

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 19]({{ site.baseurl }}/learn/19-audio-setup.html), whose routing rule this lesson applies to sound files.
>
> **You will need** three or four sound files, ideally of different lengths and channel counts. Two ship with this lesson, drawn from the *Citizen DJ* packages, and for more you can install those packages through the package manager, per [Lesson 01]({{ site.baseurl }}/learn/01-install.html), since they provide several thousand short, freely usable excerpts that appear in the user library ready to drag into a score.
>
> **You will build** a small sound-based document that plays, loops, fades, and reports what it is doing, and that travels to another machine without breaking.

## Why this matters

Playing a sound file is the easiest operation in this software, because you drag the file in and it plays. This lesson can therefore spend its time on the four properties that are not obvious and that decide whether a sound-based piece survives production, which are looping, fading, analysis, and paths, and each of them is a small setting with a large consequence.

Paths deserve particular attention because Lesson 05 established that media is referenced by the document and not embedded in it, and here that principle becomes concrete, since a piece with forty sound files is a piece with forty ways to break at a venue. In contrast, a piece whose paths are all relative to the project folder moves as a single directory, which is the condition that the exercise at the end of this lesson tests.

## Concepts

### Dropping a sound file

A sound file can be dropped into the score from anywhere. It can come from the user library or from the operating system's file manager, and the target decides what happens: dropping onto a scenario creates an interval containing the file, whereas dropping onto an existing interval adds the file there.

### Interval duration and file length

The interval's duration and the file's length are different quantities. The interval is a stretch of time on the score, whereas the file has a length of its own, so making the interval shorter does not shorten the file; it stops playing the file early. However, the waveform drawn inside the interval suggests that the two are one thing, which is why the distinction is obvious once stated and still a frequent early confusion.

### Looping a sound file

Looping is a property of the sound file process. It is set in the file's inspector, and it makes the file repeat for as long as its interval runs. This is the *process* loop of Lesson 17 and not a structural loop, and the two combine, so that a looping file inside a looping interval is a legitimate and occasionally confusing construction in which each level repeats on its own terms.

### Fades as gain automations

Fades are gain automations. Per Lesson 19, every audio outlet carries a gain sub-port, so you right-click it and create an automation; there is no separate fade object, and none is needed, because the automation already gives you the curve, the duration, and the means to edit both.

### The envelope process

The envelope process turns an audio signal into a control value. Its first output is an RMS (root mean square) measure and its second a peak measure, and combined with a **signal display** it puts a visible reading of the sound on the timeline, which is how you see what you are hearing.

### Portable media paths

Portable paths are resolved against the project folder. A relative path is looked up in the project folder, which means the directory containing the `.score` file, and two special prefixes make the intent explicit: `<PROJECT>:/` resolves inside the project directory and `<LIBRARY>:/` inside the user library. Using them is how a document states where its media is supposed to come from. In contrast, a bare absolute path only records where the media happened to be on the authoring machine.

## Walkthrough: from a file to a readable document

![Two intervals, each holding a sound file: the first plays once, the second loops to fill its interval]({{ site.img }}/20/20-01-sound-files.png)

The figure shows `lesson-20.score`, which ships with this lesson and holds two excerpts from the Citizen DJ packages, one played once and one set to loop. Both excerpts are freely usable, and both are referenced with a project-relative path, so that the document travels; the details are in `checks/20-sound-files.md`.

1. **Make a project directory** and put your sound files in it, per Lesson 05, before you drop any of them into a score.
2. **Drop one file** onto an empty scenario, so that an interval appears containing the waveform, and play it.
3. **Shorten the interval** to half the file's length and play again, and the file stops early; then lengthen the interval beyond the file, and the end is silent, because the interval is time while the file is content.
4. **Turn on looping** in the inspector and lengthen the interval again, so that the file now repeats to fill it.
5. **Write a fade** by right-clicking the gain port on the interval's audio outlet, creating an automation, and drawing a fade in and out, then play and note that you did this without adding a process.
6. **Add a second file** in the same interval and play, and both files are audible because each mixes into the parent, per Lesson 19's rule.
7. **Group them** by putting both into a sub-scenario and routing that scenario's output through a single effect, which is the grouping technique from the previous lesson.
8. **Analyse the sound** by adding an envelope process and a signal display, routing the sound into the envelope and the envelope's first output into the display, then play and watch the reading move with the sound.
9. **Notice the silence**, because the sound has disappeared from your monitors now that the cable removed propagation, and turn propagate on in the source outlet's inspector to get both.

   {: .warning }
   > **Routing audio into analysis removes it from the mix.** Lesson 19's rule applies to an envelope as to any other destination, so a cable into analysis silences the source until you switch **propagate** back on. Moreover, Lesson 28 depends on your knowing where the toggle is, because this is the most common surprise in audio-reactive work.

10. **Scale the reading** if the display barely moves, by inserting a small mapping process between the envelope and the display to multiply it into a useful range, as Lesson 13 taught.
11. **Make it portable** by re-pointing each file to a path inside the project directory, saving, moving the whole directory elsewhere, and reopening; no file should be missing.

## Long files, many files

The length of the files and the number of them raise different practical problems, and each has a remedy that keeps a sound-heavy document workable.

**A long file is fine to play and awkward to work with**, because the waveform drawing and the seeking both operate over the whole forty minutes. When a long file is really a sequence of sections, splitting it into files that match the score's structure makes the document rehearsable, per Lesson 18. Conversely, when it is one continuous thing, keeping it whole and using start markers preserves the continuity.

**Many short files raise a problem of legibility, whereas performance is rarely the issue.** Forty short files are readable only if the intervals are named after their content, since a folded score with default names gives no clue to what it plays; grouping related files into sub-scenarios helps further, and gives you one place to apply an effect. Additionally, keeping the files in a subdirectory of the project, and not beside the score file, gives the project directory a structure that a stranger can navigate.

Both cases share a rule. In other words, the structure of your media on disk should resemble the structure of your score, because every later change costs twice when the two diverge.

## Formats, and what to convert to

The choice of audio format matters less than it does in video, although it is not free of consequences, so it deserves one decision made once and applied to every file in the project.

**Uncompressed formats suit anything that is performed**, because a file that decodes with no work is a file that does not glitch when the machine is busy with graphics, and disk space is cheap next to a dropout in front of an audience.

**Compressed formats suit long ambient material**, where the file would otherwise be enormous and the timing is not critical; a forty-minute background bed is therefore a reasonable exception to the rule above.

**The sample rate should match the engine's.** A file at a different rate is converted at playback, which is work the machine does not need to do and which, in some situations, is audible.

**The channel count should match what you route.** A stereo file used as a mono source wastes a channel through every subsequent process, so the fix belongs in the file, where it is made once, and not in the score.

## Common mistakes

- **Expecting the interval to define the file's length** confuses two quantities, since the interval defines only how long the file gets to play.
- **Looping in the wrong place** happens because a looping file and a looping interval are different statements, and you have to decide which of the two you meant.
- **Adding a gain process** duplicates a function, because the outlet already has a gain port.
- **Losing the sound when you add analysis** means that the cable removed propagation, which the toggle in the outlet's inspector turns back on.
- **Concluding that a barely moving envelope is broken** misreads a value that is scaled for signals and not for displays, so insert a mapping between the two.
- **Using absolute paths** works until the piece travels, which in this field is the definition of a bug.
- **Dropping files from a downloads folder** places the path outside the project, leaving the piece one cleanup away from silence.

## Exercise

Build a two-minute document from at least four sound files: one that plays once, one that loops to fill its interval, two grouped through a shared effect, and one whose level is visibly analysed on the timeline with an envelope and a signal display while remaining audible. Then move the project directory to another location and reopen the document from there.

**Success criterion:** every file plays after the move, the analysed file is both audible and visible, and you can point at the setting that made both true at once. If your signal display is flat, scale the reading before assuming the envelope failed, because the scale is the likelier cause.

## Going further

- [Audio techniques]({{ site.docs_baseurl }}/common-practices/4-audio.html), including the analysis recipe used here.
- [The sound file process]({{ site.docs_baseurl }}/processes/soundfile.html) for every playback option.
- [Media management]({{ site.docs_baseurl }}/in-depth/media.html) for the `<PROJECT>:` and `<LIBRARY>:` prefixes.
- [Audio utilities]({{ site.docs_baseurl }}/processes/audio-utilities.html) for the envelope and its relatives.
