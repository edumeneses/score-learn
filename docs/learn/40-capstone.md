---
layout: default
title: "Capstone: score a complete work"
description: "A brief, a rubric, and three reference solutions of different ambitions: make one finished, documented, producible piece."
parent: Lessons
nav_order: 46
unit: "40"
permalink: /learn/40-capstone.html
score_version: "3.8.2"
reading_time: "15 min"
practice_time: "none"
score_file: none
---

# Capstone: score a complete work

{% include lesson_meta.html %}

> **Before this capstone** finish everything else. This unit asks you to use the course rather than to learn from it.
>
> **You will need** a piece you actually want to make, and as much time as it deserves.
>
> **You will build** one complete, documented, producible work, and a submission that lets somebody else run it.

## Why this matters

Six milestones proved individual capabilities. This asks for a piece, which is different in kind: it has an intention that is not "demonstrate a technique", it has to survive being performed or installed more than once, and it has to be finishable. Most people who learn this software well never make the last step from capable to finished, and the step is mostly about scope and documentation rather than about technique.

The deliverable is deliberately two things, because that is what the field actually requires: a score file, and the paperwork that makes it producible by someone who is not you.

## The brief

Make one work that:

1. has a **stated intention** in three sentences, written before you build, describing what an audience experiences rather than what the software does;
2. runs **five to fifteen minutes**, or indefinitely if it is an installation;
3. uses **at least two media**: sound, image, light, or physical output;
4. contains **at least one genuine interaction**, whose failure mode is designed rather than discovered;
5. **starts from a known state and ends in one**, and can be run twice in a row with no manual reset;
6. is **rehearsable in sections**, with named structure legible when folded;
7. ships as a **project directory** that opens on another machine, with the five documents from Lesson 34 and a one-page card;
8. has been **run once by somebody else**, from your card, without your help.

## The rubric

Score yourself honestly against this before submitting. It is the same rubric a technical director would apply, and the weighting is deliberate: reliability and documentation together outweigh ambition.

| Criterion | What full marks look like | Weight |
|---|---|---|
| **Intention** | The three sentences describe an experience, and the piece delivers it | 15 |
| **Reliability** | Runs twice identically; recovers from every failure you can cause | 25 |
| **Structure** | Folded score is legible; sections named; rehearsable from any point | 15 |
| **Interaction** | Genuinely responsive, with designed behaviour when input is absent | 15 |
| **Craft** | Curves shaped rather than linear; ranges correct; conversions in one place | 10 |
| **Documentation** | A stranger completed a cold start from your card | 20 |

Two observations about that table. Ambition is not a criterion, and neither is technical sophistication: a simple piece that always works and can be installed by anyone scores higher than an impressive one that only you can run. And documentation carries as much weight as reliability, because a piece nobody else can run is a piece that will be performed once.

## Three reference solutions

Not to copy, but to calibrate scope. Each is a complete answer to the brief at a different level of ambition, and all three would score well.

**The modest one: a seven-minute cued piece for one performer.** Four sections of sound and projected image, advanced by a foot switch, with maximum durations so it always ends. Two audio-reactive relationships tie the image to the live playing. Built from Modules A to G, plus Lesson 25, in perhaps twenty hours. Its virtues are that everything in it is verifiable and that a stranger can run it. If you are unsure how much to attempt, attempt this.

**The middle one: an installation for a room, running eight hours a day for a month.** A sensor at the entrance, an idle state that invites approach, two outcomes, an audio bed with spatialised elements, and a light wash on Art-Net. Deployed headless to a small machine that starts at boot and recovers from a power cut, reachable remotely for maintenance. Built from Modules A to F plus Lessons 19 to 22 and 35. Its difficulty is not technical; it is the eight-hour test from Milestone P4, repeated for thirty days.

**The ambitious one: a distributed dome performance.** Two machines, one for fisheye visuals and one for a spatial audio array, cues crossing between them, an operator's surface on a tablet, and a piece that follows a live musician rather than a clock. Built from most of the course, including Modules I and J and Lessons 33 and 36. Its risk is coordination, and its correct first version is the modest one above with a second machine added only once the single-machine version works.

## How to finish

The advice that matters most, since almost nobody's first capstone fails for lack of technique.

**Write the three sentences first, and keep them visible.** Every decision afterwards is measured against them. A feature that does not serve them is scope you can cut without loss.

**Build the smallest complete version, then improve it.** A five-minute piece with one interaction that runs end to end is a work. Building three impressive sections that never connect is not, and it is the most common way this goes wrong.

**Get somebody else to run it early**, at the halfway point rather than at the end. Their questions reshape the piece while reshaping is still cheap.

**Freeze, then document.** Documentation of a moving target is wasted work. Declare the piece finished, then write the five documents, then only fix bugs.

**Keep a version that works.** Before every substantial change, commit or copy. Lesson 05 said this; it matters most now, when the thing being risked is finished work.

## What to submit

Three items, and no more.

**The project directory**, complete, opening from any location, with the media and the `.score` file.

**The five documents plus the card**, from Lesson 34: dependency list, rider, cue sheet, failure plan, one-page card.

**A capture**, per Lesson 37: one unedited take, whatever its flaws, plus a shorter edit if you want one.

Then one page of reflection, for yourself rather than for a marker: what you cut, what broke in front of somebody else, and which lesson in this course you had to go back and reread. That last question is the most useful feedback this course can get, and if you are willing to send it to the project, per Lesson 38, it is the most useful thing you can give back.

## On scope, honestly

The most common way a capstone fails is not technical, and it is worth naming precisely so you can watch for it in yourself.

It fails because the piece grew. A fifth section seemed necessary, then the interaction needed a second sensor, then the second sensor needed a calibration routine, then the calibration routine needed an interface. Each step was reasonable and the piece never reached an end. This is the normal failure of ambitious work, and the defence is structural rather than moral: decide the scope, write it down, and treat additions as requiring a deletion.

The second most common failure is finishing the artwork and not the paperwork, then discovering months later that the piece cannot be revived because the details are gone. The rubric weights documentation at a fifth of the total for exactly this reason.

A useful reframing for both: your deliverable is not a piece, it is a piece **plus the ability of somebody else to run it**. Judged that way, an hour spent on the card is worth more than an hour spent on a fifth section, and the choice stops feeling like a compromise.

A final note on judging your own work. The rubric above is deliberately mechanical, and the thing it cannot measure is whether the piece is any good. That judgement is yours, and it improves the same way the technical judgement did: by finishing things, showing them to people, and paying attention to what actually happened in the room rather than to what you intended. This course can get you to producible. Interesting is a longer project, and it is the one worth having.

## Going further

There is no next lesson. The reasonable next steps are: make a second piece, which will take a third of the time; contribute the process or the documentation page you wished existed, per Lessons 38 and 39; or teach somebody, which is the fastest way to discover what you actually understand.

- [The examples]({{ site.docs_baseurl }}/examples/examples.html) and [common practices]({{ site.docs_baseurl }}/common-practices/common-practices.html), which read differently now.
- [The user library](https://github.com/ossia/score-user-library), where your presets and fragments can go.
- [The project](https://github.com/ossia/score), for issues, discussions, and the code.
