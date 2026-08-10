---
layout: default
title: "Lesson 23: MIDI in practice"
description: "MIDI in and out devices, the piano roll and MIDI files, pattern and arpeggiator processes, and MIDI over a network."
parent: Lessons
nav_order: 28
unit: "23"
permalink: /learn/23-midi-in-practice.html
score_version: "3.8.2"
reading_time: "14 min"
practice_time: "30 min"
score_file: none
---

# Lesson 23: MIDI in practice

{% include lesson_meta.html %}

> **Before this lesson** finish [Milestone P5]({{ site.baseurl }}/learn/p5-audio-looper-set.html).
>
> **You will need** a MIDI keyboard or controller, or a virtual MIDI port, and something that makes sound from MIDI.
>
> **You will build** a document that receives MIDI, sends MIDI, plays a MIDI file, and transforms a stream on the way through.

## Why this matters

MIDI is the oldest protocol in this field and the one most likely to be in the room. It is also the protocol whose ranges bite hardest, as Lesson 08 warned: controller values run 0 to 127 as integers, and an automation left at 0 to 1 produces a change nobody can hear. If you skipped that warning, this is where it collects.

The useful surprise is that MIDI in *score* is not a special subsystem. It arrives as devices in the explorer and flows through ports like anything else, which means everything you learned in Modules C to F applies unchanged: you can map it, condition it, record it, and fire triggers from it.

## Concepts

**Two devices, two directions.** A **MIDI input** device brings a keyboard or controller into *score*. A **MIDI output** device sends to an external instrument or sequencer. They are separate declarations, and a setup that both receives and sends needs both.

**Addressing a channel or a whole device.** MIDI processes can write to a specific channel or to the device as a whole. In practice you connect them by dropping either the device's node or one of its channel nodes onto the port you want to feed, which is the same drag-and-drop grammar as everywhere else.

**The piano roll.** The central MIDI process: notes on a grid, editable by hand, and it reads **MIDI files**. Dropping a `.mid` file onto a scenario or an interval, from the library or the file manager, gives you its contents as an editable piano roll rather than as an opaque player.

**Pattern and transformation processes.** A **patternist** process generates rhythmic patterns; the **MIDI utilities** family transforms a stream on the way through, an arpeggiator among them. This is the crucial difference from a workstation: MIDI here is a stream you can process, not only a sequence you can play.

**Custom processors.** When no built-in process does what you want, a JavaScript or C++ script can transform MIDI directly, which Module J covers. This is a normal answer rather than an exotic one, because MIDI transformations are usually a few lines.

**MIDI over a network.** Not built into *score*: use an RTP MIDI daemon. On Linux, `rtpmidid`; on macOS it is part of the operating system; on Windows, Tobias Erichsen's `rtpMIDI`. The daemon presents remote ports as local ones, and *score* then sees ordinary MIDI devices.

**Integer ranges, again.** Note numbers, velocities, and controller values are integers in 0 to 127. Every automation aimed at one of them needs its range set accordingly, and Lesson 08's diagnosis is the one to run when nothing moves.

## Walkthrough: receive, transform, send

{: .note }
> A figure for this lesson is pending: it needs a piano roll with note content and a MIDI device tree, which requires interaction. See `checks/23-midi-in-practice.md`.

1. **Declare a MIDI input device** and confirm in the device explorer that your keyboard's values arrive. As always, do this before touching the timeline.
2. **Fire a trigger from a key**, using Lesson 15's technique: drop a note or controller address onto a trigger. You now have a MIDI-cued score, which is most of what a lot of theatre work needs.
3. **Map a controller to a gain.** Address a knob to the gain sub-port of an audio outlet from Module G, with the range set to 0 to 127 on the source side. Move the knob and hear the level change.
4. **Declare a MIDI output device** and connect something that makes sound.
5. **Add a piano roll** in an interval, draw a few notes, connect its output to the MIDI output device's node, and play. You are now sequencing an external instrument.
6. **Drop a MIDI file** onto the scenario. It arrives as a piano roll you can edit. Play it, then change a few notes: the file was a starting point, not a black box.
7. **Insert an arpeggiator** from the MIDI utilities between the piano roll and the output, and play again. The stream is being transformed on the way through, which is the mental model to keep.
8. **Add a patternist** on a second channel, so you have generated material alongside written material.
9. **Record a MIDI performance** into automations, per Lesson 12, and note what it gives you: continuous controller movements become curves you can edit, which is often more useful than the notes.
10. **Try the network path** if you have two machines: run an RTP MIDI daemon on both and confirm the remote ports appear as ordinary devices.

## MIDI as control, not only as notes

The most productive habit in this lesson is to stop thinking of MIDI as music and start thinking of it as the cheapest reliable control surface available.

**A cheap controller is a cue panel.** Eight faders and sixteen buttons, for very little money, mapped to triggers and gains, gives you an operator's console for a theatre piece. Lesson 33 builds a custom interface in software; a physical controller needs no software at all.

**Notes are discrete events.** A key press is an ideal trigger source: unambiguous, low latency, and physically satisfying to hit on a cue. Velocity gives you a value alongside the event, which is more than most sensors provide.

**Controllers are conditioned inputs.** A knob is already smooth, already ranged 0 to 127, and already free of the jitter that makes a real sensor need the pipeline from Lesson 13. This makes MIDI the right input for a first version of almost any interactive idea: prove the structure with a knob, then replace the knob with the sensor.

**Clock is a shared time reference.** MIDI clock lets *score* and another machine agree on tempo, which [Lesson 24]({{ site.baseurl }}/learn/24-tempo-and-sync.html) takes up directly.

## Latency, and where it comes from

MIDI feels instantaneous and is not, and in an interactive piece the difference matters. Three contributors, in the order they usually dominate.

**The audio buffer**, from Lesson 19. A note triggering a sound cannot be heard before the next buffer is computed, so buffer size sets the floor on how tight a MIDI-driven instrument can feel.

**The controller itself.** Cheap controllers scan their keys at a rate, and some add several milliseconds before a message leaves. Nothing downstream can recover that, and it is worth measuring rather than assuming, by playing something percussive and listening.

**The network, if any.** RTP MIDI over a busy wireless network is unpredictable in a way that wired MIDI is not. For anything performed, use a cable.

The practical consequence: when a MIDI-driven piece feels late, work through those three before adjusting the score. And when a piece must feel tight, budget for it in the buffer size and note the number, per Lesson 19.

## Common mistakes

- **A 0 to 1 range on a MIDI destination.** The single most common failure, and it looks like a dead connection.
- **One device where two are needed.** Input and output are separate declarations.
- **Expecting a dropped MIDI file to be a player.** It becomes editable content, which is better and occasionally surprising.
- **Treating MIDI as a subsystem.** It is devices and ports, so everything from Modules C to F applies.
- **Ignoring channels.** Two processes writing to the same channel of the same device will interleave, and the result is confusing rather than broken.
- **Expecting network MIDI to be built in.** It needs a daemon, per platform.
- **Recording notes when you wanted gestures.** Continuous controllers recorded as automations are usually the more useful capture.

## Exercise

Build a document in which: a key on your controller fires a trigger that starts a section; a knob controls the gain of a sound file from Module G; a piano roll plays four bars to a MIDI output; and an arpeggiator transforms that piano roll's output on the way. Then replace the arpeggiator with a patternist and compare.

**Success criterion:** all four paths work, and you can state the range you set on every MIDI destination. If any of them did nothing, run Lesson 07's diagnosis and note which step found it.

## Going further

- [MIDI communication]({{ site.docs_baseurl }}/in-depth/midi.html), the reference for devices, processes, and network MIDI.
- [The piano roll]({{ site.docs_baseurl }}/processes/piano-roll.html) and [MIDI utilities]({{ site.docs_baseurl }}/processes/midi-utilities.html).
- [Patternist]({{ site.docs_baseurl }}/processes/patternist.html) for generated patterns.
- [MIDI input]({{ site.docs_baseurl }}/devices/midiin-device.html) and [MIDI output]({{ site.docs_baseurl }}/devices/midiout-device.html) device references.
