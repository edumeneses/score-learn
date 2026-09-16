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

> **Before this lesson** finish [Milestone P5]({{ site.baseurl }}/learn/p5-audio-looper-set.html), since the exercise controls a sound file from Module G with a knob.
>
> **You will need** a MIDI keyboard or controller, or a virtual MIDI port, and something that makes sound from MIDI.
>
> **You will build** a document that receives MIDI, sends MIDI, plays a MIDI file, and transforms a stream on the way through.

## Why this matters

MIDI (Musical Instrument Digital Interface) is the oldest protocol in this field and the one most likely to be in the room. It is also the protocol whose ranges bite hardest, as Lesson 08 warned, because controller values run 0 to 127 as integers and an automation left at 0 to 1 produces a change too small to hear. If you skipped that warning, this lesson returns to it, since each MIDI destination you address needs its range set before it moves.

However, the useful surprise is that MIDI in *score* is not a special subsystem. It arrives as devices in the explorer and flows through ports like any other data, which means that what you learned in Modules C to F applies unchanged: you can map it, condition it, record it, and fire triggers from it.

## Concepts

**MIDI arrives and leaves through two separate devices.** A **MIDI input** device brings a keyboard or controller into *score*. In contrast, a **MIDI output** device sends to an external instrument or sequencer, and since the two are separate declarations, a setup that both receives and sends needs both.

**A process can address a channel or the whole device.** MIDI processes can write to a specific channel or to the device as a whole, and in practice you connect them by dropping either the device's node or one of its channel nodes onto the port you want to feed, which is the same drag-and-drop grammar as everywhere else.

**The piano roll is the central MIDI process.** It presents notes on a grid that you edit by hand. Moreover, it reads **MIDI files**, so that dropping a `.mid` file onto a scenario or an interval, from the library or the file manager, gives you its contents as an editable piano roll and not as an opaque player.

**Pattern and transformation processes treat MIDI as a stream.** A **patternist** process generates rhythmic patterns, while the **MIDI utilities** family transforms a stream on the way through, an arpeggiator among them. This is the decisive difference from a workstation, because MIDI here is a stream you can process and not only a sequence you can play.

**A script can transform MIDI when no built-in process does what you want.** A JavaScript or C++ script can transform MIDI directly, which Module J covers. Furthermore, this is a normal answer and not an exotic one, because MIDI transformations are usually a few lines long.

**MIDI over a network requires an RTP MIDI daemon, because the transport is not built in.** On Linux, `rtpmidid` provides it; on macOS it is part of the operating system; on Windows, Tobias Erichsen's `rtpMIDI` does. The daemon presents remote ports as local ones, so that *score* then sees ordinary MIDI devices.

**Integer ranges apply to every MIDI destination.** Note numbers, velocities, and controller values are integers in 0 to 127, so every automation aimed at one of them needs its range set accordingly, and Lesson 08's diagnosis is the one to run when a destination does not move.

## Walkthrough: receive, transform, send

![A MIDI input and a MIDI output declared in the device explorer, a piano roll carrying a written phrase, and the inspector showing the channel, the note range, and the output device the roll feeds]({{ site.img }}/23/23-01-piano-roll.png)

Both devices are declared before any object is drawn, which is the order this course keeps insisting on. The output device is expanded on the left, and its shape shows sixteen channels, each carrying `on`, `off`, `control`, `program`, and `pitchbend`; that is what addressing a channel, as opposed to a device, means in practice, and it is an ordinary address tree, no different in kind from the OSC (Open Sound Control) one above it. The inspector supplies the rest: this piano roll writes to channel 1, its grid covers notes 60 to 71, and its output goes to `MIDI Out`. That range is this lesson's warning made concrete, since the roll speaks in note numbers and 60 to 71 is one octave upward from middle C.

{: .note }
> **Notes are placed by double-clicking the grid.** Dragging across an empty lane has no effect, although it is the first thing most people try, and the `Min` and `Max` fields in the inspector bound the range of notes the grid covers, so a phrase that needs two octaves needs them widened before there is anywhere to put it.
>
> **The address tree is an option, and only on the output.** `Create whole tree`, in the add-device dialog, is what builds those sixteen channels and their addresses, and it is offered for `MIDI Output` and greyed out for `MIDI Input`, where *score* fills the tree from what arrives, which is why an input device with no hardware plugged into it shows as a bare row. Additionally, there are three MIDI protocols and not two: `MIDI Input`, `MIDI Output`, and `MIDI Controller`, all under `Hardware`.

1. **Declare a MIDI input device** and confirm in the device explorer that your keyboard's values arrive, before touching the timeline, as always; with no hardware attached you will still find `Midi Through Port-0` listed under software inputs, which is enough to build against.
2. **Fire a trigger from a key** using Lesson 15's technique, dropping a note or controller address onto a trigger; you now have a MIDI-cued score, which is most of what much theatre work needs.
3. **Map a controller to a gain** by addressing a knob to the gain sub-port of an audio outlet from Module G, with the range set to 0 to 127 on the source side, then move the knob and hear the level change.
4. **Declare a MIDI output device** and connect it to something that makes sound.
5. **Add a piano roll** in an interval, double-click the grid a few times to place notes, set its output to the MIDI output device in the inspector, and play; you are now sequencing an external instrument.
6. **Drop a MIDI file** onto the scenario, where it arrives as a piano roll you can edit; play it, then change a few notes, since the file was a starting point and not a black box.
7. **Insert an arpeggiator** from the MIDI utilities between the piano roll and the output, and play again; the stream is being transformed on the way through, which is the mental model to keep.
8. **Add a patternist** on a second channel, so that you have generated material alongside written material.
9. **Record a MIDI performance** into automations, per Lesson 12, and note what it gives you: continuous controller movements become curves you can edit, which is often more useful than the notes.
10. **Try the network path** if you have two machines, by running an RTP MIDI daemon on both and confirming that the remote ports appear as ordinary devices.

## MIDI as control, not only as notes

The most productive shift in this lesson is to stop thinking of MIDI as music and to start thinking of it as the cheapest reliable control surface available.

**A cheap controller becomes a cue panel once it is mapped.** Eight faders and sixteen buttons, for little money, mapped to triggers and gains, give you an operator's console for a theatre piece. In contrast, Lesson 33 builds a custom interface in software; a physical controller needs no software at all.

**Notes are discrete events, which makes a key an ideal trigger source.** A key press is unambiguous, low in latency, and physically satisfying to hit on a cue, and velocity gives you a value alongside the event, which is more than most sensors provide.

**Controllers arrive already conditioned.** A knob is already smooth, already ranged 0 to 127, and already free of the jitter that makes a real sensor need the pipeline from Lesson 13. In other words, MIDI is the right input for a first version of almost any interactive idea: prove the structure with a knob, then replace the knob with the sensor.

**MIDI clock is a shared time reference between machines.** It lets *score* and another machine agree on tempo, which [Lesson 24]({{ site.baseurl }}/learn/24-tempo-and-sync.html) takes up directly.

## Latency, and where it comes from

MIDI feels instantaneous and is not, and in an interactive piece the difference matters, so the three contributors follow, in the order in which they usually dominate.

**The audio buffer from Lesson 19 sets the floor.** A note triggering a sound cannot be heard before the next buffer is computed, so buffer size sets the floor on how tight a MIDI-driven instrument can feel.

**The controller itself adds a scan delay.** Cheap controllers scan their keys at a rate, and some add several milliseconds before a message leaves; no downstream stage can recover that time, so measure it by playing something percussive and listening.

**The network, if there is one, is the least predictable contributor.** RTP MIDI over a busy wireless network is unpredictable in a way that wired MIDI is not, so a performed piece should reach its instruments over a cable.

When a MIDI-driven piece feels late, work through those three contributors before adjusting the score, and when a piece must feel tight, budget for it in the buffer size and note the number, per Lesson 19.

## Common mistakes

- **A 0 to 1 range on a MIDI destination** is the single most common failure, and it looks like a dead connection.
- **Declaring one device where two are needed** leaves one direction unserved, since input and output are separate declarations.
- **Expecting a dropped MIDI file to be a player** misses that it becomes editable content, which is better and occasionally surprising.
- **Treating MIDI as a subsystem** ignores that it is devices and ports, to which Modules C to F apply.
- **Ignoring channels** means that two processes writing to the same channel of the same device interleave, and the result is confusing although not broken.
- **Expecting network MIDI to be built in** overlooks the daemon it needs on each platform.
- **Recording notes when you wanted gestures** misses that continuous controllers recorded as automations are usually the more useful capture.

## Exercise

Build a document in which a key on your controller fires a trigger that starts a section, a knob controls the gain of a sound file from Module G, a piano roll plays four bars to a MIDI output, and an arpeggiator transforms that piano roll's output on the way through. Then replace the arpeggiator with a patternist and compare.

**Success criterion:** all four paths work, and you can state the range you set on every MIDI destination. If any of the four produced no result, run Lesson 07's diagnosis and note which step found the cause.

## Going further

- [MIDI communication]({{ site.docs_baseurl }}/in-depth/midi.html), the reference for devices, processes, and network MIDI.
- [The piano roll]({{ site.docs_baseurl }}/processes/piano-roll.html) and [MIDI utilities]({{ site.docs_baseurl }}/processes/midi-utilities.html).
- [Patternist]({{ site.docs_baseurl }}/processes/patternist.html) for generated patterns.
- [MIDI input]({{ site.docs_baseurl }}/devices/midiin-device.html) and [MIDI output]({{ site.docs_baseurl }}/devices/midiout-device.html) device references.
