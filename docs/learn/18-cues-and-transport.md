---
layout: default
title: "Lesson 18: Start and stop cues, seeking, and transport"
description: "The four transport buttons, start and stop cues, playing from a point and what score computes to get there, and the unsynchronize control."
parent: Lessons
nav_order: 21
unit: "18"
permalink: /learn/18-cues-and-transport.html
score_version: "3.8.2"
reading_time: "14 min"
practice_time: "30 min"
score_file: none
---

# Lesson 18: Start and stop cues, seeking, and transport

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 17]({{ site.baseurl }}/learn/17-loops-and-out-of-time.html), which introduced the loops and out-of-time material that this lesson makes rehearsable.
>
> **You will need** a score with at least three sections and one condition, ideally your P1 cue extended, since the walkthrough refers back to it.
>
> **You will build** a document that you can rehearse from any point, that initialises itself when it starts, and that switches off what it turned on when it stops.

## Why this matters

The lessons before this one assumed that you play a document from the beginning. However, no rehearsal works that way, and no show survives a stop in the wrong place, so this lesson concerns the difference between a document that runs and a document that can be *operated*, which means a document that can be rehearsed in sections, entered in the middle, stopped safely, and reset to a known condition. Each of those four abilities depends on a transport feature that the previous lessons had no reason to use.

Furthermore, this lesson settles the control that the usability study conducted at the Société des Arts Technologiques reported as unclear until it was explained to participants, which is the **unsynchronize** function. Because the study describes that difficulty plainly, the function receives its own section below, where it is explained through the instants it separates.

## Concepts

### Local play and global play

The transport offers four buttons, which are local play, global play, stop, and reinitialise, and the distinction between the first two is the one to learn: **local play** plays the object you are looking at, which is how you rehearse a scene without the rest of the score, whereas **global play** plays the score from the top. Reinitialise stops the document and returns it to its starting condition, so that the next play begins from a known state.

### Start and stop cues

Start and stop cues occupy the first and last states of the score. A cue dropped on the **first** state, in timeline view, is sent whenever the score starts and whenever it is reinitialised, while a cue on the **last** state is sent whenever the score is stopped. These two states are therefore special, and they are the correct place for the parameters that must reach a known condition and for those that must be switched off. This mechanism closes the gap that Milestone P1 identified, because interrupted playback now has a defined ending: stopping sends the last state.

### Seeking with play from here

Play from here moves the playhead to a chosen point and starts there, so that you enter the score at an arbitrary position. In other words, this operation is seeking, and in an interactive score it needs a policy for the states and triggers it jumps over, which the next two concepts supply.

### Value compilation

Value compilation keeps a seek consistent with the material it skipped. When you seek into the middle of a score that is not playing, *score* computes every state from the beginning up to that point and sends the resulting values, keeping the last value for any address that is set more than once. Without it, jumping past the state that started an external player would leave that player silent, and the feature would be useless. A pair of preferences controls it, one for the first seek and one for subsequent seeks while the score is already running.

### Interactive points during a seek

Interactive points before the target are fired by the seek. The policy holds that the visual duration of an interval, even a fully interactive one, means the duration you expect it to last, so seeking fires the interactive points before your target and positions the intervals accordingly, which can surprise an operator who did not press them. Nevertheless, this is the only policy under which a seek lands in a predictable place, and knowing that it is the policy turns the surprise into an expectation.

### Start markers

A start marker fixes where every play begins during rehearsal, since once one is set, play always starts from that point; this is how you rehearse the same passage repeatedly without seeking each time.

### External transport with JACK

External transport, where a piece needs it, comes from JACK. *score* can synchronise with JACK transport, as client or master, from the global settings; other protocols are planned, but today this is the one that ships.

## Unsynchronize, plainly

When two intervals end at the same instant they are **synchronised**, which means that they finish together and that, if one of them waits, both of them wait. This behaviour is usually what you want, because it is what sharing an instant means.

In contrast, unsynchronizing separates the two intervals, so that each ends on its own instant and can finish and proceed independently of the other. The function exists because a layer that should keep running while another layer waits for a cue cannot be synchronised to that cue; if it were, it would wait too.

However, the control confuses people because it is an icon whose effect is invisible until execution, when the two intervals suddenly behave differently from how they are drawn. The `Object` menu names the two halves of it, `Synchronize`, `Shift+M`, and `Merge events`, which is the clearest way to find the function when the icon is not obvious. If you are unsure whether two intervals are synchronised, look at whether they share an instant, and test the arrangement by making one of them wait.

## Walkthrough: make a score operable

![The scenario's context menu offering play from here, above the transport bar]({{ site.img }}/18/18-01-transport.png)

1. **Take a score with three sections** and at least one condition, for which your extended P1 cue is ideal.
2. **Add a start cue** by dropping the parameters that must be in a known condition onto the very first state, then play, reinitialise, and confirm that the values are sent both times.
3. **Add a stop cue** by dropping the parameters that must be off onto the very last state, then play, stop halfway, and confirm that they are sent; your score can no longer leave a light on.
4. **Rehearse a section with local play** by entering the section and playing it locally, so that you hear that section without sitting through the whole document.

   {: .note }
   > **The `Play` menu names the four transport buttons with their shortcuts.** Local play, global play, stop, and reinitialise correspond to `space`, `Shift+Space`, `↵`, and `Ctrl+↵`. The same menu carries `Play (Network)` and `Stop (Network)`, which [Lesson 36]({{ site.baseurl }}/learn/36-distributed-scores.html) uses.

5. **Seek into the middle** by right-clicking at a point in the second section and choosing play from here, or by using the play tool, and watch what arrives: values compiled from the beginning, so that the external state is consistent even though you skipped the intervals that would have set it.
6. **Seek past a condition** and note which branch you land in, then set that condition's offset behaviour, per Lesson 16, and seek again; you have now made a branch rehearsable without staging its precondition.
7. **Set a start marker** by right-clicking in the musical metrics area at the top of the score, and press play repeatedly, which returns you to the same passage each time without a seek.
8. **Play a single state** with the play tool or the right-click menu, so that one cue fires on its own and you can test it without running the material around it.
9. **Unsynchronize on purpose** by giving two intervals a shared ending instant, making one of them wait on a trigger, and observing that both wait; then unsynchronize them, observe that one proceeds, and write down which behaviour you wanted.
10. **Write the operator's page** in three lines, stating what to press to start, what happens on stop, and what to do if a cue is missed; if you cannot write it, the document is not operable yet.

## Rehearsal as a design constraint

A score that cannot be rehearsed from the middle will not survive contact with a production, and rehearsability is a property you build in while authoring, whereas a document that acquires it during the first rehearsal does so at the cost of that rehearsal.

**Sections should be short enough to re-run.** If a section takes four minutes to reach its interesting moment, it is two sections, because the wait before each attempt is what makes a rehearsal slow.

**A start marker per section saves a seek on every attempt.** The marker is cheap to move during rehearsal, and it removes the seek from the loop of trying something and hearing it again.

**Every condition needs an offset behaviour chosen on purpose.** Each condition in a show should have an answer to what happens when the operator skips into that scene, since the default is not always the answer you want.

**A stop must always be safe.** Rehearsal means stopping abruptly, dozens of times, in arbitrary places, and if any of those stops leaves the room in a bad state, you will spend the rehearsal restoring it by hand.

**The operator's page should be written from the first rehearsal**, because a page written after the last one records only what you happened to remember. Moreover, writing it early is the fastest way to discover what you have not decided.

## Common mistakes

- **Omitting the stop cue** means that stopping mid-cue leaves the rig in whatever state the interruption caught, which is the failure Milestone P1 flagged and this lesson fixes.
- **Confusing local and global play** means that rehearsing a section with global play requires sitting through every section before it.
- **Assuming that a seek sends no values** ignores the compiled result of the material before the target, which is usually what you want and is occasionally startling.
- **Leaving the offset behaviour unset** on a condition you need to rehearse past means that a seek into that scene lands wherever the default sends it.
- **Unsynchronizing to fix a symptom** separates the ending instants whether or not you meant to, so two things that should end together should stay synchronised while you look for the real cause.
- **Rehearsing only from the top** leaves the middle of the piece untested until the performance, although that is where the transitions, the conditions, and the missable cues are concentrated.

## Exercise

Take a score with three sections, one condition, and one interactive trigger, and make it operable, which means giving it a start cue, a stop cue, a start marker on the second section, and a condition set so that the second branch can be rehearsed without staging its precondition. Then hand the three-line operator's page to someone who has never seen the piece, and watch them run it.

**Success criterion:** the operator can start the piece, stop it safely, and rehearse the second section without your help. Whatever they had to ask about belongs in the operator's page, which [Lesson 34]({{ site.baseurl }}/learn/34-rehearsal-to-show.html) turns into a full technical document.

## Going further

- [Seek and transport]({{ site.docs_baseurl }}/common-practices/9-seek-and-transport.html), the reference for every behaviour above, including value compilation.
- [Start and stop cues]({{ site.docs_baseurl }}/common-practices/7-start-stop-cues.html) for the special first and last states.
- [Cues]({{ site.docs_baseurl }}/cues.html) for firing cues manually and from outside.
- [Scenes]({{ site.docs_baseurl }}/common-practices/6-scenes.html) for the full-view workflow that makes local play useful.
