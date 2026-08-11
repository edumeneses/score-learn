---
layout: default
title: "Lesson 24: Tempo, metre, and synchronisation"
description: "Give an interval its own tempo and time signature, quantise triggers to musical positions, and build a polyrhythm from nested intervals."
parent: Lessons
nav_order: 29
unit: "24"
permalink: /learn/24-tempo-and-sync.html
score_version: "3.8.2"
reading_time: "14 min"
practice_time: "25 min"
score_file: none
---

# Lesson 24: Tempo, metre, and synchronisation

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 23]({{ site.baseurl }}/learn/23-midi-in-practice.html).
>
> **You will need** a document with an LFO or a piano roll, so you can hear quantisation take effect.
>
> **You will build** a score with two sections in different metres, a trigger quantised to the bar, and a nested polyrhythm.

## Why this matters

Everything so far measured time in seconds, which is the right unit for lighting, video, and installation work and the wrong one for anything with a pulse. This lesson adds musical time, and it does so in a way that is unusual and worth understanding rather than memorising: tempo and metre are **properties of intervals**, propagated down the hierarchy, which means different parts of a score can be in different tempi and different metres at the same time.

That is not a novelty feature. It is the mechanism that makes polyrhythm, cross-fading between two tempi, and quantised interaction expressible without leaving the timeline you have been using all along.

## Concepts

**Musical metrics belong to intervals.** An interval either has its own tempo and signature, or it takes them from its nearest ancestor that does, recursively up to the root. You mark an interval as having its own metrics in its inspector, in full view. That single rule produces everything else in this lesson.

**Three controls.** A **time signature** delimits bars, which is what quantisation counts in. A **tempo curve** gives an interval a speed, which can itself change over time. A **quantisation setting** says at which musical division child elements are allowed to start.

**Quantisation is about when things are permitted to begin.** Set an interval's quantisation to one bar, and a child element triggered mid-bar starts at the beginning of the next bar instead of immediately. Every quantisable place offers the musical divisions plus two special values: **parent**, which defers to the ancestor's setting, and **free**, which means no quantisation and immediate starts.

**Processes follow automatically.** Anything that can use tempo and metric information does: audio plug-ins, LFOs, arpeggiators. You do not connect a clock to them; they read it from their parent. This is why Lesson 11 could promise that an LFO stays locked to the piece.

**Polyrhythm is nesting.** A root in four-four containing one child interval in three-four and another in seven-eight is a polyrhythmic score, and it needs no special construction: each interval declares its own metrics and the propagation rule does the rest.

**Triggers can be quantised.** An interactive trigger fired mid-bar can be made to take effect on the next musical division. For performance this is the difference between an interaction that lands and one that sounds like a mistake, and it means a performer does not have to be metronomically precise.

**External synchronisation.** *score* speaks JACK transport, as client or master, configured in the global settings. MIDI clock, per Lesson 23, gives a shared tempo with other machines. Broader synchronisation, including SMPTE and Ableton Link, is planned rather than present, which matters if a production depends on it.

## Walkthrough: two metres and a quantised cue

![An interval's inspector, showing the metrics button, the speed control, and the quantisation setting]({{ site.img }}/24/24-01-metrics.png)

1. **Give the root its own metrics.** Enter the root interval in full view, mark it as having its own metrics, and set four-four with a tempo you can hear.
2. **Add something that pulses.** An LFO driving a parameter, or a piano roll playing quarter notes. You need an audible pulse to judge everything that follows.
3. **Confirm the pulse follows the tempo.** Change the tempo and listen: the process followed without being reconnected.
4. **Draw a tempo curve.** Automate the tempo across twenty seconds and listen to the pulse accelerate. Note that this is an ordinary automation on a musical property.
5. **Add a second interval with its own metrics** in seven-eight, containing its own pulse. Play: two sections, two metres, one document.
6. **Nest, do not sequence.** Put both pulsing intervals inside one parent so they run at the same time. You now have a polyrhythm, and the only construction involved was declaring metrics on each child.
7. **Set quantisation to one bar** on the parent, and add an interactive trigger, per Lesson 15, that starts a third layer.
8. **Fire the trigger deliberately off the beat.** The layer starts on the next bar rather than where you pressed. This is the whole point: your timing no longer has to be exact.
9. **Change quantisation to free** and fire again. The layer starts immediately, and probably badly. Set it back.
10. **Try parent quantisation** on a nested element and confirm it inherits, so that changing the setting in one place changes the behaviour of everything below.
11. **Synchronise externally** if you have a second application: enable JACK transport and confirm that starting one starts the other.

## When musical time is the wrong choice

Two situations where reaching for tempo makes a piece harder rather than easier, worth naming because the feature is attractive.

**When the piece has no pulse.** An installation whose events are minutes apart gains nothing from bars, and quantisation actively hurts: an interaction that waits up to a bar before responding feels broken when the bar is four seconds long. Use seconds and free quantisation.

**When you are synchronising to something that is not musical.** Video frame rates, lighting desks, and network timing are not divisions of a bar. Trying to express a two-frame offset as a musical division is fighting the model; use seconds and, if needed, the transport features of Lesson 18.

The general test: if a collaborator would describe the timing in bars, use musical metrics. If they would describe it in seconds or frames, do not. A score can of course do both in different parts, which is exactly what the propagation rule is for.

## Who is the master?

Once two machines are involved, one question decides the whole design: which one holds the tempo?

**score as master.** *score* runs the transport and everything else follows. Right when the piece's structure is in *score*, which is the usual case for the work this course describes.

**score as follower.** Another application or a hardware sequencer holds the tempo and *score* follows. Right when a band, a click track, or an existing production workflow already defines the pulse.

**No shared tempo at all.** Two systems running independently, synchronised only at cue points by triggers. This is more robust than it sounds and often the correct answer: fewer things to go wrong, and each system stays internally consistent. Many productions that believe they need clock synchronisation actually need two cues.

Decide this before building, write it in the technical page, and test the failure: what happens when the other machine stops. A follower that freezes when its master disappears is a design decision you should make deliberately rather than discover.

One detail visible in the figure is worth naming, because it is where most of this lesson is actually operated from. An interval's inspector carries the metrics button, the speed control with its ratio presets, and the quantisation dropdown, all in one place. Speed and quantisation are easy to confuse and do different jobs: speed scales how fast the interval's contents run, while quantisation decides at which musical division its children are allowed to begin. A section that feels rushed wants speed; a section whose entries land untidily wants quantisation.

## Common mistakes

- **Expecting a tempo to exist by default.** An interval without its own metrics uses its ancestor's, and if nothing declares any, everything is in seconds.
- **Setting metrics without being in full view**, then not finding the control.
- **Quantising an installation.** Response feels late, and nobody is counting bars.
- **Free quantisation in a musical piece**, then blaming the performer for imprecise entries.
- **Connecting a clock to an LFO.** It reads its parent's; there is nothing to connect.
- **Assuming polyrhythm needs a special object.** It needs two intervals with their own metrics.
- **Depending on a synchronisation protocol that is planned rather than present.** Check before promising it to a production.

## Exercise

Build a document with a root in four-four, two nested intervals in three-four and seven-eight running simultaneously, and a third layer started by an interactive trigger quantised to the bar. Then draw a tempo curve on the root and listen to what happens to all three layers.

**Success criterion:** the two nested metres are audibly independent while sharing the root's tempo changes, and firing the trigger off the beat still produces an entry on the beat. Then set the root's quantisation to free and describe, in one sentence, what got worse.

## Going further

- [Musical metrics]({{ site.docs_baseurl }}/in-depth/musical.html), the reference for propagation, quantisation, and tempo curves.
- [The tempo process]({{ site.docs_baseurl }}/processes/tempo-control.html) and the [tempo examples]({{ site.docs_baseurl }}/examples/tempo/tempo.html).
- [Seek and transport]({{ site.docs_baseurl }}/common-practices/9-seek-and-transport.html) for JACK transport and start markers.
- [MIDI synchronisation]({{ site.docs_baseurl }}/processes/midi-sync.html) for clock, and [LTC]({{ site.docs_baseurl }}/processes/ltc-generator.html) for timecode.
