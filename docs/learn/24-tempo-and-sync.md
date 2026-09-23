---
layout: default
title: "Lesson 24: Tempo, quantisation, and sync with other software"
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

# Lesson 24: Tempo, quantisation, and sync with other software

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 23]({{ site.baseurl }}/learn/23-midi-in-practice.html), which introduced the MIDI (Musical Instrument Digital Interface) clock that this lesson returns to for synchronisation.
>
> **You will need** a document with an LFO (low-frequency oscillator) or a piano roll, so that the effect of quantisation is audible while you work through the steps.
>
> **You will build** a score with two sections in different metres, a trigger quantised to the bar, and a nested polyrhythm.

## Why this matters

Every lesson so far measured time in seconds, which is the right unit for lighting, video, and installation work, whereas a piece with a pulse needs a unit that counts beats and bars. This lesson adds musical time, and it does so through a mechanism that deserves understanding before memorising: tempo and metre are **properties of intervals**, propagated down the hierarchy, which means that different parts of a score can run in different tempi and different metres at the same time.

However, the rule is less a curiosity than the mechanism behind polyrhythm, cross-fading between two tempi, and quantised interaction, all of which become expressible without leaving the timeline you have been using all along. The Concepts below therefore describe a single rule and its consequences.

## Concepts

### Inherited musical metrics

Musical metrics belong to intervals, which either declare their own or inherit them. An interval either has its own tempo and signature, or it takes them from its nearest ancestor that does, recursively up to the root; you mark an interval as having its own metrics in its inspector while the interval is open in full view. That single rule produces every other behaviour in this lesson.

### Time signature, tempo, and quantisation

An interval's musical time is defined by three controls, each of which answers a different question. A **time signature** delimits bars, which is the unit quantisation counts in; a **tempo curve** gives an interval a speed, which can itself change over time; and a **quantisation setting** says at which musical division child elements are allowed to start.

### Quantising child elements

Quantisation governs when child elements are permitted to begin. Set an interval's quantisation to one bar, and a child element triggered mid-bar starts at the beginning of the next bar instead of immediately, so that the entry lands on the grid however imprecisely it was fired. Every quantisable place offers the musical divisions plus two special values, **parent** and **free**: the first defers to the ancestor's setting, whereas the second disables quantisation so that starts are immediate.

### Processes that follow the tempo

Processes that understand musical time follow it without any connection. Audio plug-ins, LFOs, and arpeggiators read tempo and metric information from their parent interval, so you do not connect a clock to them, and this inherited clock is why Lesson 11 could promise that an LFO stays locked to the piece.

### Polyrhythm by nesting

Polyrhythm is a matter of nesting. A root in four-four containing one child interval in three-four and another in seven-eight is already a polyrhythmic score, and it needs no special construction, because each interval declares its own metrics and the propagation rule does the rest.

### Quantised triggers

Interactive triggers can be quantised as well. A trigger fired mid-bar can be made to take effect on the next musical division, which in performance is the difference between an interaction that lands and one that sounds like a mistake; consequently a performer does not have to be metronomically precise for the entry to be.

### JACK transport and MIDI clock

External synchronisation covers JACK transport and MIDI clock. *score* speaks JACK transport, as client or master, configured in the global settings, while MIDI clock, per Lesson 23, gives a shared tempo with other machines. However, neither protocol decides which machine leads, which is the question that *Who is the master?*, below, asks you to settle before building.

## Walkthrough: two metres and a quantised cue

![An interval's inspector, showing the metrics button, the speed control, and the quantisation setting]({{ site.img }}/24/24-01-metrics.png)

The figure shows the place from which most of this lesson is operated, because an interval's inspector carries the metrics button, the speed control with its ratio presets, and the quantisation dropdown together in one panel. Speed and quantisation are easy to confuse although they do different jobs: speed scales how fast the interval's contents run, whereas quantisation decides at which musical division its children are allowed to begin. In other words, a section that runs at the wrong pace as a whole is corrected with speed, while a section whose entries land off the grid is corrected with quantisation.

1. **Give the root its own metrics** by entering the root interval in full view, marking it as having its own metrics, and setting four-four with a tempo you can hear comfortably.
2. **Add something that pulses**, either an LFO driving a parameter or a piano roll playing quarter notes, because you need an audible pulse to judge each step that follows.
3. **Confirm that the pulse follows the tempo** by changing the tempo and listening: the process followed without being reconnected, which is the inheritance rule made audible.
4. **Draw a tempo curve** that automates the tempo across twenty seconds, and listen to the pulse accelerate; this is an ordinary automation applied to a musical property, so the curve tools you already know apply unchanged.
5. **Add a second interval with its own metrics** in seven-eight, containing its own pulse, and play the document, which now holds two sections in two metres.
6. **Nest the two pulsing intervals inside one parent** so that they run at the same time; sequencing them would give two metres in turn, whereas nesting gives a polyrhythm, and the only construction involved was declaring metrics on each child.
7. **Set quantisation to one bar on the parent**, and add an interactive trigger, per Lesson 15, that starts a third layer when you fire it.
8. **Fire the trigger off the beat on purpose** and observe that the layer starts on the next bar instead of where you pressed, which is the point of the feature: your timing no longer has to be exact.
9. **Change quantisation to free** and fire again; the layer now starts immediately, and probably badly, so set it back to one bar before continuing.
10. **Try parent quantisation** on a nested element and confirm that it inherits, so that changing the setting in one place changes the behaviour of every element below it.
11. **Synchronise externally** if you have a second application that speaks JACK transport: enable the transport in *score* and confirm that starting one application starts the other.

## When musical time is the wrong choice

Musical time makes a piece harder to build in two situations: when the piece has no pulse, and when the reference it synchronises to is not musical.

**When the piece has no pulse, bars add no structure and quantisation actively hurts.** An installation whose events are minutes apart gains no benefit from bars, and an interaction that waits up to a bar before responding feels broken when the bar is four seconds long; use seconds and free quantisation in that case.

**When you are synchronising to a source that is not musical, seconds are the correct unit.** In contrast to a band or a click track, video frame rates, lighting desks, and network timing are not divisions of a bar, so trying to express a two-frame offset as a musical division fights the model; use seconds and, if needed, the transport features of Lesson 18.

The general test is whether a collaborator would describe the timing in bars, in which case musical metrics are appropriate, or in seconds or frames, in which case they are not. A score can do both in different parts, which is what the propagation rule is for.

## Who is the master?

Once two machines are involved, one question decides the whole design, namely which machine holds the tempo, and the three possible answers differ in what happens when a machine fails.

**score as master** means that *score* runs the transport and every other system follows, which is the right arrangement when the piece's structure lives in *score*, as it does for the work this course describes.

**score as follower** means that another application or a hardware sequencer holds the tempo and *score* follows it, which is the right arrangement when a band, a click track, or an existing production workflow already defines the pulse.

**No shared tempo at all** means two systems running independently, synchronised only at cue points by triggers. Nevertheless, this arrangement is more dependable than it sounds and is often the correct answer, because fewer components can fail and each system stays internally consistent; many productions that believe they need clock synchronisation in fact need two cues.

Decide this before building, and write the decision in the technical page. Furthermore, test the failure case, which is what happens when the other machine stops. A follower that freezes when its master disappears may be an acceptable design decision, although it should be one you made on purpose and not one you discover during a performance.

## Common mistakes

- **Expecting a tempo to exist by default**, whereas an interval without its own metrics uses its ancestor's, and if no interval declares any, the whole document runs in seconds.
- **Trying to set metrics without being in full view**, and then not finding the control, which the inspector shows in full view.
- **Quantising an installation**, so that the response feels late to a visitor who is not counting bars.
- **Using free quantisation in a musical piece**, and then blaming the performer for imprecise entries that the parent's quantisation would have placed on the beat.
- **Connecting a clock to an LFO**, although it reads its parent's metrics and there is no clock to connect.
- **Assuming that polyrhythm needs a special object**, when it needs two intervals with their own metrics inside one parent.
- **Depending on a synchronisation protocol that is planned but not yet present**, since broader synchronisation, including SMPTE and Ableton Link, is announced without being in this release; check the current release before promising it to a production.

## Exercise

Build a document with a root in four-four, two nested intervals in three-four and seven-eight running simultaneously, and a third layer started by an interactive trigger quantised to the bar. Additionally, draw a tempo curve on the root and listen to what happens to all three layers.

**Success criterion:** the two nested metres are audibly independent while sharing the root's tempo changes, and firing the trigger off the beat still produces an entry on the beat. Then set the root's quantisation to free and describe, in one sentence, what got worse.

## Going further

- [Musical metrics]({{ site.docs_baseurl }}/in-depth/musical.html), the reference for propagation, quantisation, and tempo curves.
- [The tempo process]({{ site.docs_baseurl }}/processes/tempo-control.html) and the [tempo examples]({{ site.docs_baseurl }}/examples/tempo/tempo.html).
- [Seek and transport]({{ site.docs_baseurl }}/common-practices/9-seek-and-transport.html) for JACK transport and start markers.
- [MIDI synchronisation]({{ site.docs_baseurl }}/processes/midi-sync.html) for clock, and [LTC]({{ site.docs_baseurl }}/processes/ltc-generator.html) for timecode.
