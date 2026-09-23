---
layout: default
title: "Lesson 19: Audio setup and routing"
description: "Backends, buffer size, and the one rule that explains all of score's audio routing: everything mixes into its parent unless you say otherwise."
parent: Lessons
nav_order: 23
unit: "19"
permalink: /learn/19-audio-setup.html
score_version: "3.8.2"
reading_time: "13 min"
practice_time: "20 min"
score_file: none
---

# Lesson 19: Audio setup and routing

{% include lesson_meta.html %}

> **Before this lesson** finish [Milestone P4]({{ site.baseurl }}/learn/p4-interactive-installation.html), since Phase 2 of the course begins here and assumes the installation it produced.
>
> **You will need** working sound output, which on Linux ideally means JACK or PipeWire.
>
> **You will build** a configured audio engine and a mental model of routing that lets you predict where a signal goes, whereas trial and error would only tell you afterwards.

## Why this matters

Audio in *score* has no mixer window, and readers arriving from a digital audio workstation reasonably conclude that routing is therefore hidden or absent. However, routing follows one rule applied recursively, and once you know the rule you can predict where any signal goes without looking for a mixer.

The setup half of the lesson matters for a duller reason, which is that most reports of *score* making no sound are configuration problems, whereas the document is usually correct and the fix is usually two settings. Configuring the engine once, and writing down what you chose, saves you from suspecting your score every time the room goes quiet.

## Concepts

### The audio backend

The backend is the system's audio layer, which the application uses without owning the sound card. It is chosen in the audio preferences, and on Linux, JACK or PipeWire give reliable low latency and let *score* coexist with other audio software, whereas ALSA works and is less flexible; on macOS and Windows the defaults are normally correct.

### Buffer size and latency

Buffer size trades latency against safety. A smaller buffer means lower latency and more risk of dropouts, while a larger one is safer and less responsive. For authoring, comfort matters more than latency. In contrast, a percussive interactive piece needs latency more than comfort, so the right value depends on the piece, which is why this lesson closes by asking you to write it down.

### Channel count beyond stereo

Channel count is not fixed at two. *score* passes arbitrary channel counts through its ports, which is what makes speaker arrays and domes possible, and no part of the model assumes stereo, which changes how you think about a signal once you have internalised it.

### The recursive routing rule

A single routing rule governs the default behaviour. Every process mixes its audio output into its parent interval; every interval mixes into its parent scenario; and so on, recursively, up to the top of the score, whose output goes to the main output of the audio interface configured in the preferences. In other words, that recursion is the whole default behaviour, and it is why a sound file dropped anywhere in a score is audible without configuration.

### Cables and propagation

Connecting a cable removes propagation. The moment you connect an audio outlet to another process's audio inlet, the source stops mixing into its parent, because you have stated explicitly where its output should go and its dry signal no longer reaches the parent. This is almost always what you want when you draw a cable. Nevertheless, it is the single most surprising behaviour in the model, so it has a toggle: select the port and switch **propagate** back on in the inspector if you want both the dry path and the routed one.

### The gain sub-port

Every audio outlet carries a gain sub-port. Any output can therefore be faded without inserting an effect, because you right-click the gain port and create an automation, per Lesson 10's fourth route. This is how fades are written in *score*, and it is much less work than the alternatives.

## Walkthrough: configure, then predict

![The Audio page of score's settings, showing the driver, buffer size, output device, and reported channel count, beside the inspector of a sound file's audio outlet with its propagate toggle]({{ site.img }}/19/19-01-audio-preferences.png)

Both halves of the lesson appear in that one image. On the left is the `Audio` page, with a backend chosen, a buffer size, an output device, and the channel count the driver reports underneath, which here is 64 in and 64 out and is what an unfixed channel count looks like in practice. On the right is the inspector for a sound file, whose `Outputs` section carries the `Propagate` toggle that step 8 turns back on.

{: .note }
> **The buffer size is not always yours to set from inside the application.** Under `ALSA (PortAudio)`, captured above, the buffer size and the rate are fields in the dialog, whereas under `PipeWire` *score* replaces them with a line telling you to set an environment variable before it starts, `export PIPEWIRE_QUANTUM=256/48000`. Choosing PipeWire therefore makes the buffer size a property of how you launch the application, which you should know before you write the number into a technical rider.

1. **Open the audio preferences**, which are the `Audio` page of the dialog that `Settings` opens from the menu bar, and note the six backends listed there: a dummy one that makes no sound, JACK, three ALSA routes, and PipeWire.
2. **Set the buffer size** somewhere comfortable and write the number down; under PipeWire, set `PIPEWIRE_QUANTUM` before launching instead, per the note above.
3. **Confirm the output device** and the channel count, which *score* reports directly under the device and which `Rescan` refreshes; if you have a multichannel interface, note how many channels are available, because Lesson 22 uses them.
4. **Drop a sound file into a score** and play it, and if you hear it, the engine works and the routing rule has done its job with no configuration from you.
5. **Check the two usual causes if you hear no sound**, which are the engine and the connection. If the time cursor is not advancing, the engine is not running, which is a configuration problem; if the sound file's interval is not connected to the start of the score, it does not execute, which is a document problem. That pair of questions separates the two halves of this lesson.
6. **Predict, then verify**, by putting a second sound file inside a sub-scenario, three levels deep, and saying where its audio goes before you play; it is audible, because each level mixed into its parent.
7. **Add an effect and connect a cable** from the sound file's output to the effect's input, then play again and notice that you now hear only the processed signal, because connecting the cable removed the dry propagation.
8. **Turn propagate back on** in the source outlet's inspector and play once more, so that you hear both paths. In other words, the cable decides where the signal goes, and propagate decides whether it also goes where it used to.
9. **Write a fade without an effect** by right-clicking the gain port on the sound file's outlet, creating an automation, and drawing a fade, which is the idiomatic way to fade anything in *score*.
10. **Find the top-level output** by scrolling to the bottom of your root scenario to its audio output port, which reducing its slot height makes visible; every signal in the document arrives here, which is where a global filter would go.

## Where to put a global effect

The recursive rule gives you a clean answer to a need that workstations meet with a master bus. Because the root scenario has its own audio output, connecting that output to a process applies that process to the entire score, so a limiter, a room correction filter, or a master equaliser belongs there, and no other object in the document has to know about it.

Furthermore, the same technique one level down is how you group. Put several sound files inside one sub-scenario and route that scenario's output into an effect, and the effect processes all of them through one cable, whereas cabling each file separately would need one cable per file. This is the *score* equivalent of a group bus, and it costs no extra setup because the hierarchy already exists.

For complex routing, switch to the nodal view, per Lesson 11, since a routing that would need a matrix in another tool is a patch here, and the temporal view gives no useful picture of it.

## Two numbers worth writing down

Every project that involves sound should record two values, because both change what the piece *is* and neither is visible in the document.

**The buffer size sets the latency of the whole piece.** A piece rehearsed at 512 samples and performed at 2048 feels different under the hand, and an interactive piece can cross from responsive to sluggish on that change alone. If the piece depends on immediacy, the buffer size is therefore part of its specification, whereas treating it as machine configuration leaves it to whoever installs the machine.

**The channel count, and what each channel is, decides which rooms the piece fits.** Stereo is a choice that a document makes, whereas a document that assumes two channels without saying so has to be rewritten for a four-speaker room. Writing "output 1 and 2, front pair" costs a line and saves a load-in.

Moreover, both values belong in the same project notes as the device map from Lesson 06, and both are the first questions a venue technician will ask.

## Common mistakes

- **Assuming that there is a mixer** sends you looking for a window that does not exist, whereas the hierarchy that replaces it behaves predictably once you know the rule.
- **Being surprised that a cable silences the dry signal** means that propagation was removed, and the toggle that restores it is in the port inspector.
- **Hunting for a document bug when the engine is not running** wastes the search, because a time cursor that does not advance means that no document could have played.
- **Leaving a sound file unconnected to the start of the score** means that it does not play, although the file itself is correct.
- **Choosing the smallest buffer during authoring** means spending the session fighting dropouts for latency you do not need until the rehearsal.
- **Forgetting the gain sub-port** and inserting a gain effect adds a process for a function that every outlet already carries.
- **Assuming stereo** ignores that ports carry whatever channel count arrives, which Lesson 22 depends on.

## Exercise

Build a document with four sound files, two routed straight to the top and two grouped in a sub-scenario whose output passes through one effect, and then add a global effect on the root scenario's output. Before playing, write down what you expect to hear from each of the four files and which of them are affected by which effect, then play and check your predictions against the result.

**Success criterion:** your predictions match what you hear, and you can state for each cable you drew whether it removed a dry path. If any file was silent, say whether the cause was configuration or connection, because separating those two causes is what this lesson set out to teach.

## Going further

- [Audio routing]({{ site.docs_baseurl }}/in-depth/audio-routing.html), the three-sentence reference for the whole model.
- [Audio techniques]({{ site.docs_baseurl }}/common-practices/4-audio.html), which this lesson and the next two follow.
- [The audio device]({{ site.docs_baseurl }}/devices/audio-device.html) for live inputs, used in Lesson 21.
- [Preferences]({{ site.docs_baseurl }}/reference-manual/references/preferences.html) for the backend and buffer settings.
