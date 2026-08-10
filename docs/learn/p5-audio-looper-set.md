---
layout: default
title: "Milestone P5: an audio looper performance set"
description: "A performable set: layers you start and stop from the keyboard, a defined ending, and a document you can rehearse in sections."
parent: Lessons
nav_order: 27
unit: "P5"
permalink: /learn/p5-audio-looper-set.html
score_version: "3.8.2"
reading_time: "15 min"
practice_time: "60 min"
score_file: none
---

# Milestone P5: an audio looper performance set

{% include lesson_meta.html %}

> **Before this milestone** finish Lessons 19 to 22. This unit introduces nothing new.
>
> **You will need** four to six sound files and a computer keyboard. A foot controller or MIDI pad is optional.
>
> **You will build** a set you can actually perform: layers toggled live, a mix you can shape, and an ending you can trust.

## Why this matters

The *ossia score* workshop given by the software's authors ends on an audio looper, and for good reason: it is the smallest project that requires everything at once. Structure, triggers, conditions, audio routing, gain automation, and rehearsal discipline all appear, and none of them can be faked, because you will be performing it in front of yourself.

It is also the milestone that answers a question Phase 1 left open. An interactive installation runs without you. A performance runs *with* you, which means the document's job is not to be autonomous but to be **playable**: predictable under your hands, forgiving of a mistimed press, and recoverable when something goes wrong mid-set.

## The brief

Build a document that:

1. has **at least four independent layers**, each a looping sound file or group;
2. lets each layer be **started and stopped live**, from a key or a controller, in any order;
3. gives you **live control of at least two mix parameters**, through gain sub-ports rather than inserted effects;
4. runs **indefinitely** without drifting or accumulating;
5. can be **rehearsed in sections**, with a start marker and local play;
6. has a **defined ending**: one action brings everything down and leaves nothing running;
7. ships with a **one-page performance sheet**: what each key does, in the order you will need them.

Nothing here requires hardware beyond your computer. Map the toggles to keyboard keys through a device, and note in your performance sheet what the equivalent controller mapping would be.

## Concepts you are assembling

**A layer is a looping interval.** A sound file set to loop, inside an interval whose end waits on a trigger, per Lesson 17. It runs from when you fire it until you stop it.

**A toggle is two triggers.** One at each end of the looping interval, both firing on your key, with a minimum duration so one press is not read as two. This is the switch pattern from Module F, applied to audio.

**Out-of-time layers.** Layers not connected to the start of the score, each with start-on-play enabled, so that all of them are available from the moment the set begins and none of them runs until you say so. This is what makes the set playable in any order rather than in a sequence you decided while authoring.

**Mix control through gain ports.** Every audio outlet has a gain sub-port. Address one from your controller, or automate it, and you have a fader without inserting anything.

**A defined ending.** A stop cue on the last state, per Lesson 18, plus a deliberate choice about what stopping does to layers still running.

## Walkthrough

{: .note }
> A figure for this lesson is pending: it needs a set with audio content and a controller mapping, so it requires media and interaction. See `checks/p5-audio-looper-set.md`.

1. **Build one layer completely** before building four. A looping file, an interval that waits at both ends, a key that toggles it, a minimum duration. Rehearse it alone until it is reliable.
2. **Confirm the toggle survives abuse.** Press the key rapidly ten times. If the layer ends up in a state you did not intend, raise the minimum duration before continuing.
3. **Duplicate it three times.** Save the working layer as a fragment in the user library, per Lesson 05, then drop it back in three times and re-point each copy at a different file and a different key.
4. **Make them all out-of-time**, with start on play, so none of them starts by itself and all are available at once.
5. **Play the set.** Fire layers in different orders, and listen for the first structural problem: usually two layers that only work together if started in one order, which means something is not as independent as you thought.
6. **Add mix control.** Address two gain sub-ports from your controller or from keys, so you can shape the balance live rather than committing to it while authoring.
7. **Add the ending.** A stop cue that brings every layer's gain to zero, and a decision about whether stopping also stops the layers or leaves them silent but running. Test the one you chose.
8. **Rehearse in sections.** Set a start marker, use local play on individual layers, and confirm you can work on layer three without hearing the whole set.
9. **Perform it twice, recorded.** Not as a deliverable, but because listening back is the only reliable way to find the moment where the document fought you.
10. **Write the performance sheet.** One page: each key, what it does, and the order you expect to need them in. If writing it reveals a key you cannot justify, remove it.

## What makes a set playable

Four properties, learned the hard way by everyone who has done this.

**Independence.** Any layer can start or stop at any time without breaking another. If two layers must be co-ordinated, make them one layer.

**Forgiveness.** A mistimed press produces something acceptable rather than something broken. Minimum durations, and toggles rather than sequences, are how you get this.

**Legibility under pressure.** You will not read the screen while performing. The key mapping has to be memorable: adjacent keys for related layers, a consistent direction for up and down.

**Recoverability.** There is one action that returns the set to a known state, and you have rehearsed using it. Without this, a mistake mid-set has no floor.

Notice that none of the four is about sound. They are about the document as an instrument, which is what a milestone at this stage should be teaching.

## Rehearsing your own instrument

Two practices from performers who do this regularly, both of which sound obvious and are routinely skipped.

**Rehearse the failures, not the piece.** Ten minutes deliberately pressing wrong keys, starting layers in impossible orders, and firing everything at once teaches you what the set does when you make a mistake, which is the thing you actually need to know on stage. A set you have only rehearsed correctly is a set you have not rehearsed.

**Perform to a recording once per session.** Listening back is uncomfortable and it is the only reliable way to hear the difference between a transition that worked and one you covered for. It also catches the layer that is always slightly too loud, which is invisible from behind the keyboard.

One more, specific to this software: keep the score visible but do not read it. If you find yourself watching the timeline to know what to press, the key mapping is wrong, and the fix is in the mapping rather than in your memory.

## Common mistakes

- **Building four layers before one works.** Every flaw gets multiplied by four.
- **No minimum duration on the toggles.** One press reads as two, and the layer you meant to start stops immediately.
- **Layers connected to the start of the score**, so the set begins with everything playing.
- **Committing the mix while authoring.** The balance you chose in the studio is not the balance the room wants.
- **No ending.** A set that has to be ended by stopping the application is not finished.
- **A key mapping you cannot remember.** If it needs the screen, it needs redesigning.
- **Not rehearsing.** This milestone is the first one where the document is only half the work.

## Exercise

Extend the set in one direction, and only one.

Either **make it responsive to itself**: analyse one layer with an envelope, per Lesson 20, and use that reading to modulate something in another layer, so the set has an internal relationship you do not have to perform.

Or **make it spatial**: send one layer through the four-speaker scene from Lesson 22, so that one of your layers moves while the others stay in place. Fold down to stereo for rehearsal, and note in the performance sheet what changes with a real rig.

**Success criterion:** you can perform the set twice, in different orders, without a broken state, and end it with one action. Your performance sheet fits on one page and you did not consult the screen while playing. Keep the document: [Milestone P6]({{ site.baseurl }}/learn/p6-fulldome-scene.html) is the same shape with visuals.

## Going further

- [Audio techniques]({{ site.docs_baseurl }}/common-practices/4-audio.html) and [switches]({{ site.docs_baseurl }}/common-practices/2-switches.html), the two recipes this milestone combines.
- [Live coding]({{ site.docs_baseurl }}/common-practices/8-live-coding.html), for editing the set while it plays, which is legitimate and useful in rehearsal.
- [The audio looper process]({{ site.docs_baseurl }}/processes/audio_looper.html), which is worth comparing with the structure you built by hand.
- [Seek and transport]({{ site.docs_baseurl }}/common-practices/9-seek-and-transport.html) for start markers and local play.
