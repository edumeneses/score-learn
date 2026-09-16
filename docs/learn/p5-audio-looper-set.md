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

> **Before this milestone** finish Lessons 19 to 22, because this unit introduces no new technique and combines the audio ones you already have.
>
> **You will need** four to six sound files and a computer keyboard, while a foot controller or MIDI (Musical Instrument Digital Interface) pad is optional.
>
> **You will build** a set that can be performed: layers toggled live, a mix that can be shaped, and an ending that can be trusted.

## Why this matters

The *ossia score* workshop given by the software's authors ends on an audio looper, and for good reason, since it is the smallest project that requires every earlier skill at once. Structure, triggers, conditions, audio routing, gain automation, and rehearsal all appear, and none of them can be faked, because the person performing the set is the same person who built it.

Furthermore, this milestone answers a question Phase 1 left open, because an interactive installation runs without a performer. In contrast, a performance runs *with* one, so the document's job is not autonomy but **playability**, which means being predictable under the hands, forgiving of a mistimed press, and recoverable when something goes wrong mid-set.

## The brief

Build a document that:

1. has **at least four independent layers**, each a looping sound file or group;
2. lets each layer be **started and stopped live**, from a key or a controller, in any order;
3. gives you **live control of at least two mix parameters**, through gain sub-ports and without inserted effects;
4. runs **indefinitely** without drifting or accumulating;
5. can be **rehearsed in sections**, with a start marker and local play;
6. has a **defined ending**, so that one action brings every layer down and leaves none running;
7. ships with a **one-page performance sheet** listing what each key does, in the order you will need them.

No item in this brief requires hardware beyond your computer, so map the toggles to keyboard keys through a device, and note in your performance sheet what the equivalent controller mapping would be.

## Concepts you are assembling

**A layer is a sound file set to loop inside an interval whose end waits on a trigger**, per Lesson 17, and it runs from the moment it is fired until it is stopped.

**A toggle is two triggers, one at each end of the looping interval, both firing on the same key.** A minimum duration keeps one press from being read as two. In other words, the whole arrangement is the switch pattern from Module F applied to audio.

**Out-of-time layers are not connected to the start of the score, and each has start-on-play enabled.** Consequently all of them are available from the moment the set begins and none of them runs until it is fired, which is what makes the set playable in any order instead of in a sequence decided while authoring.

**Mix control comes through the gain sub-port that every audio outlet carries.** Address one from a controller, or automate it, and the result is a fader without any inserted effect.

**A defined ending is a stop cue on the last state**, per Lesson 18, together with an explicit choice about what stopping does to layers that are still running.

## Walkthrough

{: .note }
> A figure for this lesson is pending: it needs a set with audio content and a controller mapping, so it requires media and interaction. See `checks/p5-audio-looper-set.md`.

1. **Build one layer completely** before building four, with a looping file, an interval that waits at both ends, a key that toggles it, and a minimum duration, and rehearse it alone until it is reliable.
2. **Confirm that the toggle survives abuse** by pressing the key rapidly ten times, and if the layer ends up in a state you did not intend, raise the minimum duration before continuing.
3. **Duplicate it three times** by saving the working layer as a fragment in the user library, per Lesson 05, then dropping it back in three times and re-pointing each copy at a different file and a different key.
4. **Make them all out-of-time**, with start on play, so that none of them starts by itself while all of them are available at once.
5. **Play the set**, firing layers in different orders, and listen for the first structural problem, which is usually two layers that only work together if started in one order and are therefore not as independent as they seemed.
6. **Add mix control** by addressing two gain sub-ports from your controller or from keys, so that the balance can be shaped live instead of being committed while authoring.
7. **Add the ending** as a stop cue that brings every layer's gain to zero, together with a decision about whether stopping also stops the layers or leaves them silent but running, and test the option you chose.
8. **Rehearse in sections** by setting a start marker and using local play on individual layers, and confirm that layer three can be worked on without hearing the whole set.
9. **Perform it twice with the recorder running**, since listening back is the only reliable way to find the moment where the document fought you; the recording is for you and not a deliverable.
10. **Write the performance sheet** on one page, listing each key, what it does, and the order you expect to need them in; if writing it reveals a key you cannot justify, remove that key.

## What makes a set playable

Playability can be reduced to four properties, and the rest of this section states each one with the structural choice that provides it.

**Independence means that any layer can start or stop at any time without breaking another**, and if two layers must be co-ordinated the solution is to make them one layer.

**Forgiveness means that a mistimed press produces something acceptable instead of something broken**, and it comes from minimum durations and from toggles in place of sequences.

**Legibility under pressure means that the key mapping has to be memorable without the screen**, with adjacent keys for related layers and a consistent direction for up and down, because a performer does not read the timeline while playing.

**Recoverability means that one action returns the set to a known state**, and that the action has been rehearsed, because without it a mistake mid-set has no floor.

However, none of the four properties is about sound; they concern the document as an instrument, which is what a milestone at this stage should be teaching, and which the rehearsal practices below take further.

## Rehearsing your own instrument

Rehearsal has two practices that sound obvious and are routinely skipped, and both of them expose faults that playing the set correctly does not reveal.

**Rehearsing the failures teaches more than rehearsing the piece.** Ten minutes spent pressing wrong keys on purpose, starting layers in impossible orders, and firing every layer at once shows what the set does when a mistake happens, which is the thing a performer needs to know on stage; a set that has only been rehearsed correctly is a set whose failure modes are still unknown.

**Performing to a recording once per session is uncomfortable and reliable.** Listening back is the only dependable way to hear the difference between a transition that worked and one that was covered for. Additionally, it catches the layer that is always slightly too loud, which cannot be judged from behind the keyboard.

Moreover, a third practice is specific to this software: keep the score visible but do not read it. If you find yourself watching the timeline to know what to press, the key mapping is wrong, and the fix belongs in the mapping and not in your memory.

## Common mistakes

- **Building four layers before one works** multiplies every flaw by four, which is what the fragment step in the walkthrough prevents.
- **Leaving out the minimum duration on the toggles** lets one press read as two, so the layer you meant to start stops immediately.
- **Layers connected to the start of the score** make the set begin with every layer playing, which removes the choice of order that the set exists for.
- **Committing the mix while authoring** assumes that the balance chosen in the studio is the balance the room needs, which it seldom is.
- **A set with no ending**, which has to be ended by stopping the application, is not finished.
- **A key mapping that cannot be remembered** needs the screen, and a mapping that needs the screen needs redesigning.
- **Not rehearsing** misses that this milestone is the first one where the document is only half the work.

## Exercise

Choose one of the two extensions below and leave the other for a later session, since each changes how the set has to be rehearsed.

Either **make it responsive to itself** by analysing one layer with an envelope, per Lesson 20, and using that reading to modulate a parameter in another layer, so that the set has an internal relationship that does not have to be performed.

Or **make it spatial** by sending one layer through the four-speaker scene from Lesson 22, so that one layer moves while the others stay in place; fold down to stereo for rehearsal, and note in the performance sheet what changes with a real rig.

**Success criterion:** the set can be performed twice, in different orders, without a broken state, and ended with one action, while the performance sheet fits on one page and the screen was not consulted during either performance. Keep the document, because [Milestone P6]({{ site.baseurl }}/learn/p6-fulldome-scene.html) is the same shape with visuals.

## Going further

- [Audio techniques]({{ site.docs_baseurl }}/common-practices/4-audio.html) and [switches]({{ site.docs_baseurl }}/common-practices/2-switches.html), the two recipes this milestone combines.
- [Live coding]({{ site.docs_baseurl }}/common-practices/8-live-coding.html), for editing the set while it plays, which is legitimate and useful in rehearsal.
- [The audio looper process]({{ site.docs_baseurl }}/processes/audio_looper.html), which repays comparison with the structure you built by hand.
- [Seek and transport]({{ site.docs_baseurl }}/common-practices/9-seek-and-transport.html) for start markers and local play.
