---
layout: default
title: "Lesson 19: Audio setup and the routing model"
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

# Lesson 19: Audio setup and the routing model

{% include lesson_meta.html %}

> **Before this lesson** finish [Milestone P4]({{ site.baseurl }}/learn/p4-interactive-installation.html). Phase 2 begins here.
>
> **You will need** working sound output, and on Linux ideally JACK or PipeWire.
>
> **You will build** a configured audio engine and a mental model of routing you can predict from, rather than discover by trial.

## Why this matters

Audio in *score* has no mixer window, and readers arriving from a workstation reasonably conclude that routing is therefore hidden or absent. It is neither: it follows one rule applied recursively, and once you know the rule you can predict where any signal goes without looking for a mixer.

The setup half of the lesson matters for a duller reason. Most reports of "*score* makes no sound" are configuration, not documents, and the fix is usually two settings. Doing this once, deliberately, saves you from suspecting your score every time.

## Concepts

**The backend.** *score* does not own the sound card; it uses the system's audio layer, chosen in the audio preferences. On Linux, JACK or PipeWire give reliable low latency and let *score* coexist with other audio software; ALSA works and is less flexible. On macOS and Windows the defaults are normally correct.

**Buffer size and latency.** A smaller buffer means lower latency and more risk of dropouts; a larger one is safer and less responsive. For authoring, comfort matters more than latency; for a percussive interactive piece, the opposite. Change it deliberately and note the value in your project documentation, because it is a real part of how the piece behaves.

**Channel count is not two.** *score* passes arbitrary channel counts through its ports, which is what makes speaker arrays and domes possible. Nothing in the model assumes stereo, which is worth internalising early because it changes how you think about a "signal".

**The one routing rule.** Every process mixes its audio output into its parent interval; every interval mixes into its parent scenario; and so on, recursively, up to the top of the score. The top interval's output goes to the main output of the audio interface configured in the preferences. That is the whole default behaviour, and it is why a sound file dropped anywhere in a score is simply audible.

**Connecting a cable removes propagation.** The moment you connect an audio outlet to another process's audio inlet, the source stops mixing into its parent: its dry output no longer reaches the parent, because you have said explicitly where it should go. This is almost always what you want, and it is the single most surprising behaviour in the model, so it has a toggle: select the port and switch **propagate** back on in the inspector if you want both the dry path and the routed one.

**Every audio outlet has a gain.** Each audio outlet carries a gain sub-port, which means any output can be faded without inserting an effect: right-click the gain port and create an automation, per Lesson 10's fourth route. This is how fades are written in *score*, and it is much less work than the alternatives.

## Walkthrough: configure, then predict

![The Audio page of score's settings, showing the driver, buffer size, output device, and reported channel count, beside the inspector of a sound file's audio outlet with its propagate toggle]({{ site.img }}/19/19-01-audio-preferences.png)

Both halves of the lesson are in that one image. On the left is the `Audio` page, with a backend chosen, a buffer size, an output device, and the channel count the driver reports underneath: 64 in and 64 out, which is what "channel count is not two" looks like in practice. On the right is the inspector for a sound file, whose `Outputs` section carries the `Propagate` toggle that step 8 turns back on.

{: .note }
> **The buffer size is not always yours to set.** Under `ALSA (PortAudio)`, captured above, the buffer size and the rate are fields. Under `PipeWire` they are not: *score* replaces them with a line telling you to set an environment variable before it starts, `export PIPEWIRE_QUANTUM=256/48000`. Choosing PipeWire therefore makes the buffer size a property of how you launch the application rather than a preference you can change while it runs, which is worth knowing before you write the number into a technical rider.

1. **Open the audio preferences.** They are the `Audio` page of the dialog that `Settings` opens from the menu bar. Six backends are listed here: a dummy one that makes no sound, JACK, three ALSA routes, and PipeWire.
2. **Set the buffer size** somewhere comfortable, and write the number down. Under PipeWire, set `PIPEWIRE_QUANTUM` before launching instead, per the note above.
3. **Confirm the output device** and the channel count. The counts *score* reports sit directly under the device, and `Rescan` refreshes them. If you have a multichannel interface, note how many channels are actually available; Lesson 22 uses them.
4. **Drop a sound file into a score** and play. If you hear it, the engine works and the routing rule just did its job with no configuration from you.
5. **Check the two usual suspects if you hear nothing.** Is the time cursor advancing? If not, the engine is not running, which is a configuration problem. Is the sound file's interval connected to the start of the score? If not, it never executes, which is a document problem. That pair of questions separates the two halves of this lesson.
6. **Predict, then verify.** Put a second sound file inside a sub-scenario, three levels deep. Before playing, say where its audio goes. Play: it is audible, because each level mixed into its parent.
7. **Add an effect and connect a cable** from the sound file's output to the effect's input. Play again, and notice that you now hear only the processed signal: connecting the cable removed the dry propagation.
8. **Turn propagate back on** in the source outlet's inspector and play once more. Now you hear both. Understanding this one behaviour prevents most confusion about "where did my sound go".
9. **Write a fade without an effect.** Right-click the gain port on the sound file's outlet and create an automation. Draw a fade. This is the idiomatic way to fade anything in *score*.
10. **Find the top-level output.** Scroll to the bottom of your root scenario and find its audio output port. Reducing its slot height makes it visible. Everything in the document arrives here, which is where a global filter would go.

## Where to put a global effect

The recursive rule gives you a clean answer to something workstations solve with a master bus.

Because the root scenario has its own audio output, connecting that output to a process applies it to the entire score. A limiter, a room correction filter, a master equaliser: all of them belong there, and nothing else in the document has to know about it.

The same technique one level down is how you group. Put several sound files inside one sub-scenario, route that scenario's output into an effect, and the effect processes all of them, with one cable instead of one per file. This is the *score* equivalent of a group bus, and it costs nothing to set up because the hierarchy already exists.

For complex routing, switch to the nodal view, per Lesson 11. Anything that would need a matrix in another tool is a patch here, and the temporal view is simply the wrong place to draw it.

## Two numbers worth writing down

Every project that involves sound should record two values, because both change what the piece *is* and neither is visible in the document.

**The buffer size**, which sets latency. A piece rehearsed at 512 samples and performed at 2048 feels different under the hand, and an interactive piece can cross from responsive to sluggish on that change alone. If the piece depends on immediacy, the buffer size is part of its specification, not part of the machine's configuration.

**The channel count and what each channel is.** Stereo is a choice, not a default, and a document that assumes two channels is a document that has to be rewritten for a four-speaker room. Writing "output 1 and 2, front pair" costs a line and saves a load-in.

Both belong in the same project notes as the device map from Lesson 06, and both are the first things a venue technician will ask.

## Common mistakes

- **Assuming there is a mixer.** There is a hierarchy, and it behaves predictably.
- **Being surprised that a cable silences the dry signal.** That is propagation being removed. The toggle is in the port inspector.
- **Hunting for a document bug when the engine is not running.** Check the cursor first.
- **A sound file not connected to the start of the score.** It will never play, and nothing about the file is wrong.
- **Choosing the smallest buffer during authoring.** You will spend the session fighting dropouts for latency you do not need until the rehearsal.
- **Forgetting the gain sub-port** and inserting a gain effect instead. It is already there on every outlet.
- **Assuming stereo.** Ports carry whatever channel count arrives, and Lesson 22 depends on that.

## Exercise

Build a document with four sound files: two routed straight to the top, and two grouped in a sub-scenario whose output passes through one effect. Then add a global effect on the root scenario's output. Before playing, write down what you expect to hear from each of the four, and which of them are affected by which effect. Play and check your predictions.

**Success criterion:** your predictions match what you hear, and you can state for each cable you drew whether it removed a dry path. If any file was silent, say whether it was configuration or connection; that distinction is the lesson.

## Going further

- [Audio routing]({{ site.docs_baseurl }}/in-depth/audio-routing.html), the three-sentence reference for the whole model.
- [Audio techniques]({{ site.docs_baseurl }}/common-practices/4-audio.html), which this lesson and the next two follow.
- [The audio device]({{ site.docs_baseurl }}/devices/audio-device.html) for live inputs, used in Lesson 21.
- [Preferences]({{ site.docs_baseurl }}/reference-manual/references/preferences.html) for the backend and buffer settings.
