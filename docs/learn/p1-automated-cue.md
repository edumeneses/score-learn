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

> **Before this milestone** finish Lessons 02 to 05. This unit introduces nothing new; if something here is unclear, the gap is in a lesson you can name.
>
> **You will need** an empty document and about forty-five minutes.
>
> **You will build** a sixty-second cue that starts from a known state, develops in three sections, ends dark, and travels as a self-contained project directory.

## Why this matters

A milestone is where separate techniques become a thing that runs. Until now you have placed one process at a time; the difficulty of a real cue is not any single element but their coordination: sections that hand over cleanly, a defined starting condition, and an ending you can trust.

The brief is deliberately modest in ambition and strict about finish. Sixty seconds is long enough to need structure and short enough to rebuild if you go wrong. "Ends dark" is not decoration: a cue that leaves a parameter high has broken the next cue, and that is a real failure mode in installations and shows.

## The brief

Build a document that:

1. runs for **sixty seconds** across **three chained sections**, each an interval;
2. **sets a known starting state** before anything moves: every parameter you will touch, given an explicit value at the first instant;
3. drives **at least three parameters**, with at least one interval holding **two automations at once**;
4. uses **at least two different curve shapes**, not three linear ramps;
5. **ends in a defined state**, with the parameters you raised returned to zero;
6. is delivered as a **project directory** that opens from a different location on disk.

Nothing in this list needs a trigger, a condition, or a device beyond the one you declared earlier. Those arrive in Module F, and adding them now would be building on ground the course has not laid.

## Concepts you are assembling

**Chaining.** Two intervals that share an instant hand over without a gap: the state ending one begins the next. Chained intervals are how a score gets sections, and they are why you do not need one long interval containing everything.

**A known starting state.** The first state in the document is not scene-setting; it is the thing that makes the cue repeatable. Without it, the cue's effect depends on whatever the previous run left behind.

**Stacked processes.** One interval can hold several processes at once, each in its own slot, or several automations sharing one band. When automations are stacked, the frontmost is drawn as a red line and the others are greyed; click the address bar at the top of the slot to bring one forward for editing.

**A defined ending.** The mirror of the starting state, and the reason your cue can be run twice in a row without a manual reset.

## Walkthrough: the reference solution

![Three chained intervals named Rise, Hold, and Fall, with four automations and states carrying messages at the start and end]({{ site.img }}/p1/p1-01-cue-structure.png)

`p1-solution.score` ships with this milestone. Build yours first; read this afterwards and compare.

1. **Three intervals, chained.** `Rise` from 0 to 20 seconds, `Hold` from 20 to 40, `Fall` from 40 to 60. Each begins where the previous ends, so the document has four instants in total.
2. **A starting state.** The instant at 0 carries a message setting `lesson:/level` to 0. In a real piece it would carry every parameter the cue touches; here one is enough to make the pattern visible.
3. **`Rise`** holds one automation on `lesson:/level`, from 0 to 1, with a slow start: the curve accelerates rather than ramping linearly.
4. **`Hold`** holds two automations at once, one on `lesson:/colour` and one on `lesson:/shutter`, in two slots. This is the interval that proves point 3 of the brief.
5. **`Fall`** holds one automation on `lesson:/level`, from 1 back to 0, with the opposite curvature to `Rise`: fast at first, then settling.
6. **A closing state.** The instant at 60 seconds returns `lesson:/level` to 0, so that the parameter's final value does not depend on when the automation was interrupted.
7. **The project directory.** `p1-solution.score` sits alone because it references no media; your version, if it uses a sound file, needs the layout from Lesson 05.

## How to know it is finished

Run this list against your own document before reading the next lesson.

- Play it from the start twice in a row without touching anything between runs. The second run must behave exactly like the first. If it does not, your starting state is incomplete.
- Stop it in the middle with `↵`, then play again from the beginning. Same test, harder: it catches parameters that only get their value from an automation that did not run.
- Fold every interval with `Ctrl+Alt+F` and read the structure alone. Three sections should be legible with no slots visible at all. If the shape is unclear folded, it will be unclear to a collaborator.
- Check every slot header for a `->` destination. An automation with no address is the most common silent failure.
- Move the project directory and open it from the new location.
- Name everything. Intervals called `Rise`, `Hold`, and `Fall` cost nothing now and save real time later; `Interval.4` tells nobody anything, including you in a month.

## Rehearsing in sections

The reason the brief insists on three intervals rather than one is that sections can be rehearsed, and this is the first point in the course where that pays.

Playing from the top every time is fine for a sixty-second cue and unworkable for a twenty-minute piece. Because your document is divided, you can work on `Hold` without sitting through `Rise`: select what you care about, and use the arrow keys, which walk the structure rather than the pixels, to move between linked elements. [Lesson 18]({{ site.baseurl }}/learn/18-cues-and-transport.html) adds seeking and transport control, at which point rehearsing a middle section becomes a single action.

There is a second, less obvious payoff. A document divided into named sections is a document you can talk about. "The transition into `Hold` is late" is a sentence a collaborator can act on; "about twenty-five seconds in" is not. Sections are as much a communication tool as a technical one, which is why naming them was a requirement rather than a suggestion.

And a caution about the ending. Your closing state returns `lesson:/level` to zero, which is right, but note what it does *not* do: it does not stop the automation that was running, because there is nothing left to stop, the interval having ended. If you interrupt the cue mid-`Fall` with `↵`, the parameter keeps whatever value it had at that instant, and the closing state never runs. Interrupted playback is not a defined ending, and [Lesson 18]({{ site.baseurl }}/learn/18-cues-and-transport.html) is where that gap gets closed properly with a stop cue.

## Common mistakes

- **One long interval with everything in it.** It plays correctly and it cannot be rehearsed in sections, which is what sections are for.
- **No starting state.** The cue works once, from a fresh launch, and then subtly differs.
- **Three linear ramps.** Technically satisfying the brief, and it teaches nothing about curvature. Bend at least two of them with `Shift+Drag`.
- **Leaving a parameter high at the end.** Test by running the cue twice.
- **Stacking automations and then losing one.** When several share a band, the frontmost is red and the rest are greyed; use the slot's address bar to bring one forward, and right-click a slot background to remove one deliberately.
- **Naming nothing.** A folded score with default names is unreadable, which defeats the point of folding.

## Exercise

Extend your finished cue in one of two directions, and only one.

Either **make it musical**: give the three sections durations in a ratio you chose rather than three equal twenty-second blocks, and adjust the curves so the transitions land where you want them.

Or **make it operable**: add a fourth parameter that stays constant through the whole cue and is set only by the opening state, then write down, in three lines, what an operator would need to know to run this cue cold.

**Success criterion:** the cue passes the six-point finish list, plus your chosen extension. Keep the file; [Milestone P2]({{ site.baseurl }}/learn/p2-light-wash.html) starts from a cue of exactly this shape, and [Lesson 18]({{ site.baseurl }}/learn/18-cues-and-transport.html) turns it into something an operator can drive.

## Going further

- [States and automations in practice]({{ site.docs_baseurl }}/quick-start/states-and-automations-in-practice.html), especially the section on stacked automations.
- [Common practices]({{ site.docs_baseurl }}/common-practices/common-practices.html), which is organised as recipes and is worth skimming now that you have built something.
- [Automations in depth]({{ site.docs_baseurl }}/in-depth/automations.html) before [Lesson 10]({{ site.baseurl }}/learn/10-automation-curves.html).
