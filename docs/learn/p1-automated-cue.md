---
layout: default
title: "Milestone P1: a sixty-second automated cue"
description: "Assemble Lessons 02 to 05 into a timed cue with three chained intervals, four automations, and a documented project layout."
parent: Lessons
nav_order: 6
unit: "P1"
permalink: /learn/p1-automated-cue.html
score_version: "3.8.2"
reading_time: "15 min"
practice_time: "45 min"
score_file: p1-automated-cue/p1-solution.score
---

# Milestone P1: a sixty-second automated cue

{% include lesson_meta.html %}

> **Before this milestone** finish Lessons 02 to 05, because this unit introduces no new technique; if something here is unclear, the gap is in a lesson you can name.
>
> **You will need** an empty document and about forty-five minutes.
>
> **You will build** a sixty-second cue that starts from a known state, develops in three sections, ends dark, and travels as a self-contained project directory.

## Why this matters

A milestone is the point at which separate techniques are assembled into a document that runs from beginning to end. Until now you have placed one process at a time, whereas the difficulty of a real cue lies in coordinating its elements: sections that hand over cleanly, a defined starting condition, and an ending you can trust.

The brief is modest in ambition and strict about finish, because sixty seconds is long enough to need structure and short enough to rebuild if you go wrong. However, "ends dark" is a requirement and not a decoration, since a cue that leaves a parameter high has broken the next cue, and that is a real failure mode in installations and shows.

## The brief

The brief asks for a document that meets six conditions:

1. runs for **sixty seconds** across **three chained sections**, each an interval;
2. **sets a known starting state** before anything moves: every parameter you will touch, given an explicit value at the first instant;
3. drives **at least three parameters**, with at least one interval holding **two automations at once**;
4. uses **at least two different curve shapes**, not three linear ramps;
5. **ends in a defined state**, with the parameters you raised returned to zero;
6. is delivered as a **project directory** that opens from a different location on disk.

No item in this list needs a trigger, a condition, or a device beyond the `lesson` device you borrowed from `lesson-04.score`. Those arrive in Module F, and adding them now would be building on ground the course has not yet laid.

## Concepts you are assembling

### Chained intervals

Chaining joins two intervals at a shared instant, so that they hand over without a gap and the state ending one begins the next. Moreover, chained intervals are how a score gets sections, and they are the reason you do not need one long interval containing the whole cue.

### A known starting state

A known starting state makes the cue repeatable, because the first state in the document is not scene-setting; without it, the cue's effect depends on whatever the previous run left behind.

### Stacked processes

Stacked processes share one interval, which can hold several processes at once, each in its own slot, or several automations sharing one band, so that one stretch of time can move several parameters together.

### A defined ending

A defined ending mirrors the starting state, and it is the reason your cue can be run twice in a row without a manual reset.

## Walkthrough: the reference solution

[![Three chained intervals named Rise, Hold, and Fall, with four automations and states carrying messages at the start and end]({{ site.img }}/p1/p1-01-cue-structure.png)]({{ site.scores }}/p1-automated-cue/p1-solution.score){: download="" title="Download p1-solution.score, the document in this figure" }

`p1-solution.score` ships with this milestone, so build yours first and read this afterwards to compare.

1. **The structure is three chained intervals**, with `Rise` from 0 to 20 seconds, `Hold` from 20 to 40, and `Fall` from 40 to 60. Each begins where the previous ends, so the document has four instants in total.
2. **A starting state opens the cue**, since the instant at 0 carries a message setting `lesson:/level` to 0; in a real piece it would carry every parameter the cue touches, but here one is enough to make the pattern visible.
3. **`Rise` holds one automation** on `lesson:/level`, from 0 to 1, with a slow start, so that the curve accelerates instead of ramping linearly.
4. **`Hold` holds two automations at once**, one on `lesson:/colour` and one on `lesson:/shutter`, in two slots, which makes it the interval that proves point 3 of the brief.
5. **`Fall` holds one automation** on `lesson:/level`, from 1 back to 0, with the opposite curvature to `Rise`, fast at first and then settling.
6. **A closing state ends the cue**, since the instant at 60 seconds returns `lesson:/level` to 0, so that the parameter's final value does not depend on when the automation was interrupted.
7. **The project directory is minimal here**, because `p1-solution.score` references no media and therefore sits alone; your version, if it uses a sound file, needs the layout from Lesson 05.

## How to know it is finished

Run this list against your own document before reading the next lesson, because each item catches a failure that the lessons so far have named.

- Play it from the start twice in a row without touching the document between runs, because the second run must behave like the first. In other words, a second run that differs reveals an incomplete starting state.
- Stop it in the middle with `↵`, then play again from the beginning, which is the same test made harder, since it catches parameters that only get their value from an automation that did not run.
- Fold every interval with `Ctrl+Alt+F` and read the structure alone, because three sections should be legible with no slots visible at all, and a shape that is unclear folded will be unclear to a collaborator.
- Check every slot header for a `->` destination, since an automation with no address is the most common silent failure.
- Move the project directory and open it from the new location, which is the test point 6 of the brief asks for.
- Name every interval, because `Rise`, `Hold`, and `Fall` cost a few seconds now and save real time later, whereas `Interval.4` leaves a collaborator, and you in a month, with no idea what the section does.

## Rehearsing in sections

The brief insists on three intervals instead of one because sections can be rehearsed, and this is the first point in the course where that pays.

Playing from the top every time is fine for a sixty-second cue. In contrast, it is unworkable for a twenty-minute piece, and because your document is divided, you can work on `Hold` without sitting through `Rise`: select what you care about, and use the arrow keys, which walk the structure rather than the pixels, to move between linked elements. [Lesson 18]({{ site.baseurl }}/learn/18-cues-and-transport.html) adds seeking and transport control, at which point rehearsing a middle section becomes a single action.

Furthermore, a document divided into named sections is a document you can talk about, which is a second and less obvious payoff. "The transition into `Hold` is late" is a sentence a collaborator can act on, whereas "about twenty-five seconds in" is not. Sections are as much a communication tool as a technical one, which is why naming them was a requirement rather than a suggestion.

A caution about the ending is needed as well. Your closing state returns `lesson:/level` to zero, which is right. However, it does not stop the automation that was running, because the interval has already ended and no process remains to stop. If you interrupt the cue mid-`Fall` with `↵`, the parameter keeps whatever value it had at that instant, and the closing state does not run. Interrupted playback is not a defined ending, and [Lesson 18]({{ site.baseurl }}/learn/18-cues-and-transport.html) is where that gap gets closed properly with a stop cue.

## Common mistakes

- **A single long interval holding the whole cue**, which plays correctly but cannot be rehearsed in sections, although sections exist for that purpose.
- **No starting state**, so that the cue works once, from a fresh launch, and then subtly differs.
- **Linear ramps throughout**, which fail the fourth item of the brief and teach you little about curvature; bend at least two of them with `Shift+Drag`.
- **Leaving a parameter high at the end**, which running the cue twice will reveal.
- **Stacking automations and then losing one**, because when several share a band the frontmost is red and the rest are greyed, so click the address bar at the top of the slot to bring one forward for editing, and right-click a slot background to remove one on purpose.
- **Leaving the default names in place**, so that the folded score is unreadable, which defeats the point of folding.

## Exercise

Extend your finished cue in one of two directions, and in only one.

Either **make it musical**, by giving the three sections durations in a ratio you chose instead of three equal twenty-second blocks, and by adjusting the curves so that the transitions land where you want them.

Or **make it operable**, by adding a fourth parameter that stays constant through the whole cue and is set only by the opening state, and then by writing down, in three lines, what an operator would need to know to run this cue cold.

**Success criterion:** the cue passes the six-point finish list, plus your chosen extension. Keep the file, because [Milestone P2]({{ site.baseurl }}/learn/p2-light-wash.html) starts from a cue of this shape, and [Lesson 18]({{ site.baseurl }}/learn/18-cues-and-transport.html) turns it into something an operator can drive.

## Going further

- [States and automations in practice]({{ site.docs_baseurl }}/quick-start/states-and-automations-in-practice.html), especially its section on stacked automations, which the walkthrough relied on.
- [Common practices]({{ site.docs_baseurl }}/common-practices/common-practices.html) is organised as recipes and deserves a skim now that you have built something.
- [Automations in depth]({{ site.docs_baseurl }}/in-depth/automations.html) prepares the ground before [Lesson 10]({{ site.baseurl }}/learn/10-automation-curves.html).

{% include lesson_files.html %}
