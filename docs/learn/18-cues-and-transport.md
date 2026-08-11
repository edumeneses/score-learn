---
layout: default
title: "Lesson 18: Cues, seek, and transport control"
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

# Lesson 18: Cues, seek, and transport control

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 17]({{ site.baseurl }}/learn/17-loops-and-out-of-time.html).
>
> **You will need** a score with at least three sections and one condition, ideally your P1 cue extended.
>
> **You will build** a document you can rehearse from any point, that initialises itself, and that leaves nothing on when it stops.

## Why this matters

Everything before this lesson assumed you play from the beginning. No rehearsal works that way, and no show survives a stop in the wrong place. This lesson is about the difference between a document that runs and a document that can be *operated*: rehearsed in sections, entered in the middle, stopped safely, and reset.

It also settles the control the usability study named as unclear until it was explained to someone: the **unsynchronize** function. That report is worth taking at face value, so it gets its own section below rather than a passing mention.

## Concepts

**Four transport buttons, in order.** Local play, global play, stop, and reinitialise, which the `Play` menu names with their shortcuts: `space`, `Shift+Space`, `↵`, and `Ctrl+↵`. The distinction between local and global is the one to learn: **local play** plays the object you are looking at, which is how you rehearse a scene without the rest of the score; **global play** plays the score from the top. Reinitialise stops and returns the document to its starting condition. The same menu also carries `Play (Network)` and `Stop (Network)`, which [Lesson 36]({{ site.baseurl }}/learn/36-distributed-scores.html) uses.

**Start and stop cues.** A cue dropped on the **first** state of the score, in timeline view, is sent whenever the score starts and whenever it is reinitialised. A cue on the **last** state is sent whenever the score is stopped. These two states are therefore special, and they are the correct place for "everything to a known condition" and "everything off". This is the mechanism that answers the gap Milestone P1 identified: interrupted playback now has a defined ending, because stopping sends the last state.

**Play from here.** Right-click in a scenario and choose *play from here*, or use the play tool, to move the playhead to a point and start. This is seeking, and in an interactive score it needs a policy, which is the next concept.

**Value compilation.** When you seek into the middle of a score that is not playing, *score* computes every state from the beginning up to that point and sends the resulting values, keeping the last value for any address set more than once. Without this, jumping past the state that started an external player would leave that player silent and the feature would be useless. Two preferences control it: one for the first seek, one for subsequent seeks while already running.

**Interactive points before the target get triggered.** The policy is that the visual duration of an interval, even a fully interactive one, means "the duration I expect this to last". Seeking therefore fires the interactive points before your target and positions intervals accordingly. This is the only sane answer, and knowing it is the policy prevents surprise.

**A start marker.** Right-click in the musical metrics area at the top of the score to set one. Play then always starts from that point, which is how you rehearse the same passage repeatedly without seeking each time.

**External transport.** *score* can synchronise with JACK transport, as client or master, from the global settings. Other protocols are planned; today this is the one.

## Unsynchronize, plainly

Two intervals that end at the same instant are **synchronised**: they finish together, and if one waits, they both wait. That is usually what you want, because it is what an instant means.

Unsynchronizing separates them, so each interval ends on its own instant and can finish and proceed independently. The reason it exists: a layer that should keep running while another layer waits for a cue cannot be synchronised to that cue, or it will wait too.

The reason it confuses people is that the control is an icon whose effect is invisible until execution, when the two intervals suddenly behave differently from how they are drawn. The `Object` menu names the two halves of it, `Synchronize`, `Shift+M`, and `Merge events`, which is the clearest way to find the function when the icon is not obvious. If you are unsure whether two intervals are synchronised, look at whether they share an instant, and test by making one of them wait.

## Walkthrough: make a score operable

![The scenario's context menu offering play from here, above the transport bar]({{ site.img }}/18/18-01-transport.png)

1. **Take a score with three sections** and at least one condition. Your extended P1 cue is ideal.
2. **Add a start cue.** Drop the parameters that must be in a known condition onto the very first state. Play, then reinitialise, and confirm the values are sent both times.
3. **Add a stop cue.** Drop the parameters that must be off onto the very last state. Play, stop halfway, and confirm they are sent. Your score now cannot leave a light on.
4. **Rehearse a section with local play.** Enter a section and use local play rather than playing the whole document.
5. **Seek into the middle.** Right-click at a point in the second section and choose play from here. Watch what arrives: values compiled from the beginning, so the external state is consistent even though you skipped the intervals that would have set it.
6. **Seek past a condition** and note which branch you land in. Then set that condition's offset behaviour, per Lesson 16, and seek again. You have now made a branch rehearsable without staging its precondition.
7. **Set a start marker** in the metrics area at the top and press play repeatedly. Same passage, no seeking.
8. **Play a single state.** With the play tool or the right-click menu, fire one state on its own, to test one cue without running anything around it.
9. **Unsynchronize deliberately.** Give two intervals a shared ending instant, make one of them wait on a trigger, and observe that both wait. Then unsynchronize and observe that one proceeds. Write down which behaviour you wanted.
10. **Write the operator's page.** Three lines: what to press to start, what happens on stop, and what to do if a cue is missed. If you cannot write it, the document is not operable yet.

## Rehearsal as a design constraint

A score that cannot be rehearsed from the middle will not survive contact with a production, and rehearsability is something you build in rather than discover.

**Sections short enough to re-run.** If a section takes four minutes to reach its interesting moment, it is two sections.

**A start marker per section during rehearsal.** Cheap to move, and it removes the seek from the loop of trying something and hearing it again.

**Conditions with deliberate offset behaviour.** Every condition in a show should have an answer to "what happens if we skip into this scene". The default is not always the answer you want.

**A stop that is always safe.** Rehearsal means stopping abruptly, dozens of times, in arbitrary places. If any of those stops leaves the room in a bad state, you will spend the rehearsal fixing it manually.

**A written operator's page from the first rehearsal**, not the last. It is also the fastest way to discover what you have not decided.

## Common mistakes

- **No stop cue.** Then stopping mid-cue leaves the rig in whatever state the interruption caught, which is the failure Milestone P1 flagged and this lesson fixes.
- **Confusing local and global play.** Rehearsing a section with global play means sitting through everything before it.
- **Assuming a seek sends nothing.** It sends the compiled result of everything before the target, which is usually what you want and is occasionally startling.
- **Not setting offset behaviour** on conditions you need to rehearse past.
- **Unsynchronizing to fix a symptom** without understanding that it separates the ending instants; if two things should end together, they should stay synchronised.
- **Rehearsing only from the top.** The middle of a piece is where mistakes live.

## Exercise

Take a score with three sections, one condition, and one interactive trigger, and make it operable: start cue, stop cue, a start marker on the second section, and the condition set so the second branch can be rehearsed without staging its precondition. Then hand the three-line operator's page to someone who has never seen the piece and watch them run it.

**Success criterion:** they can start it, stop it safely, and rehearse the second section without your help. Anything they had to ask about belongs in the operator's page, which [Lesson 34]({{ site.baseurl }}/learn/34-rehearsal-to-show.html) turns into a full technical document.

## Going further

- [Seek and transport]({{ site.docs_baseurl }}/common-practices/9-seek-and-transport.html), the reference for every behaviour above, including value compilation.
- [Start and stop cues]({{ site.docs_baseurl }}/common-practices/7-start-stop-cues.html) for the special first and last states.
- [Cues]({{ site.docs_baseurl }}/cues.html) for firing cues manually and from outside.
- [Scenes]({{ site.docs_baseurl }}/common-practices/6-scenes.html) for the full-view workflow that makes local play useful.
