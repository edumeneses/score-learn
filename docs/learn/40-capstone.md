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

> **Before this capstone** finish every other unit, because this unit asks you to use the course instead of learning from it.
>
> **You will need** a piece you want to make, and as much time as it deserves.
>
> **You will build** one complete, documented, producible work, together with a submission that lets somebody else run it.

## Why this matters

The six milestones proved individual capabilities, whereas this unit asks for a piece, which is different in kind: it has an intention beyond demonstrating a technique, it has to survive being performed or installed more than once, and it has to be finishable. However, most people who learn this software well stop short of the last step from capable to finished, and that step depends mostly on scope and documentation, with technique playing a smaller part than they expect.

The deliverable consists of two things because the field requires both: a score file, and the paperwork that makes it producible by someone who is not you.

## The brief

The brief asks for one work that meets eight conditions:

1. has a **stated intention** in three sentences, written before you build, describing what an audience experiences instead of what the software does;
2. runs **five to fifteen minutes**, or indefinitely if it is an installation;
3. uses **at least two media**: sound, image, light, or physical output;
4. contains **at least one genuine interaction**, with a failure mode you designed instead of one you discovered;
5. **starts from a known state and ends in one**, and can be run twice in a row with no manual reset;
6. is **rehearsable in sections**, with named structure legible when folded;
7. ships as a **project directory** that opens on another machine, with the five documents from Lesson 34 and a one-page card;
8. has been **run once by somebody else**, from your card, without your help.

## The rubric

Score yourself against this rubric before submitting, because it is the same rubric a technical director would apply, and its weighting is intentional: reliability and documentation together outweigh ambition.

| Criterion | What full marks look like | Weight |
|---|---|---|
| **Intention** | The three sentences describe an experience, and the piece delivers it | 15 |
| **Reliability** | Runs twice identically; recovers from every failure you can cause | 25 |
| **Structure** | Folded score is legible; sections named; rehearsable from any point | 15 |
| **Interaction** | Genuinely responsive, with designed behaviour when input is absent | 15 |
| **Craft** | Curves shaped rather than linear; ranges correct; conversions in one place | 10 |
| **Documentation** | A stranger completed a cold start from your card | 20 |

The table carries two implications. Ambition is not a criterion, and neither is technical sophistication, so a simple piece that always works and can be installed by anyone scores higher than an impressive one that only you can run. Furthermore, documentation carries nearly as much weight as reliability, because a piece that no other person can run is a piece that will be performed once.

## Three reference solutions

These are offered to calibrate scope and not to be copied, since each is a complete answer to the brief at a different level of ambition, and all three would score well.

**The modest one is a seven-minute cued piece for one performer.** Its four sections of sound and projected image are advanced by a foot switch, with maximum durations so that the piece always ends, and two audio-reactive relationships tie the image to the live playing. It is built from Modules A to G, plus Lesson 25, in perhaps twenty hours, and its virtues are that every element in it is verifiable and that a stranger can run it. If you are unsure how much to attempt, attempt this one.

**The middle one is an installation for a room, running eight hours a day for a month.** A sensor at the entrance, an idle state that invites approach, two outcomes, an audio bed with spatialised elements, and a light wash on Art-Net make up the piece, which is deployed headless to a small machine that starts at boot, recovers from a power cut, and is reachable remotely for maintenance. It is built from Modules A to F plus Lessons 19 to 22 and 35. In contrast, its difficulty is not technical, because the difficulty is the eight-hour test from Milestone P4, repeated for thirty days.

**The ambitious one is a distributed dome performance.** It uses two machines, one for fisheye visuals and one for a spatial audio array, with cues crossing between them, an operator's surface on a tablet, and a piece that follows a live musician instead of a clock. It is built from most of the course, including Modules I and J and Lessons 33 and 36, and its risk is coordination, so its correct first version is the modest one above with a second machine added only once the single-machine version works.

## How to finish

The advice in this section matters most, since a first capstone seldom fails for lack of technique.

**Write the three sentences first, and keep them visible**, because every decision afterwards is measured against them. Moreover, a feature that does not serve them is scope you can cut without loss.

**Build the smallest complete version, then improve it.** A five-minute piece with one interaction that runs end to end is a work, whereas three impressive sections that do not connect are not, and building them is the most common way this goes wrong.

**Get somebody else to run it early**, at the halfway point instead of at the end, because their questions reshape the piece while reshaping is still cheap.

**Freeze, then document**, since documentation of a moving target is wasted work. Declare the piece finished, then write the five documents, and then fix only bugs.

**Keep a version that works.** Before every substantial change, commit or copy the project; Lesson 05 said this, and it matters most now, when the thing being risked is finished work.

## What to submit

The submission consists of three items, and adding a fourth does not improve it.

**The project directory** should be complete, open from any location, and contain the media and the `.score` file.

**The five documents plus the card** come from Lesson 34, and they consist of the dependency list, the rider, the cue sheet, the failure plan, and the one-page card.

**A capture**, as Lesson 37 described, means one unedited take, whatever its flaws, plus a shorter edit if you want one.

Additionally, write one page of reflection, for yourself and not for a marker, covering what you cut, what broke in front of somebody else, and which lesson in this course you had to go back and reread. That last question is the most useful feedback this course can get, and if you are willing to send it to the project, as Lesson 38 described, it is the most useful thing you can give back.

## On scope, honestly

The most common way a capstone fails is not technical, and naming that failure precisely lets you watch for it in yourself.

It fails because the piece kept growing: a fifth section seemed necessary, then the interaction needed a second sensor, then the second sensor needed a calibration routine, then the calibration routine needed an interface. Each step was reasonable, and the piece did not reach an end. This is the normal failure of ambitious work, and the defence is structural: decide the scope, write it down, and treat additions as requiring a deletion.

The second most common failure is finishing the artwork and not the paperwork, then discovering months later that the piece cannot be revived because the details are gone. The rubric weights documentation at a fifth of the total for this reason.

In other words, your deliverable is not a piece but a piece **plus the ability of somebody else to run it**, and that reframing addresses both failures. Judged that way, an hour spent on the card is worth more than an hour spent on a fifth section, and the choice stops feeling like a compromise.

A final note concerns judging your own work. The rubric above is mechanical by design. However, the quality it cannot measure is whether the piece is any good, and that judgement is yours; it improves in the same way the technical judgement did, by finishing things, showing them to people, and paying attention to what happened in the room instead of to what you intended. This course can get you to producible, whereas making the work interesting is a longer project, and the steps in the next section are where it continues.

## Going further

There is no next lesson, so the reasonable next steps are to make a second piece, which will take a third of the time; to contribute the process or the documentation page you wished existed, as Lessons 38 and 39 described; or to teach somebody, which is the fastest way to discover what you understand.

- [The examples]({{ site.docs_baseurl }}/examples/examples.html) and [common practices]({{ site.docs_baseurl }}/common-practices/common-practices.html) read differently now that you have finished a piece.
- [The user library](https://github.com/ossia/score-user-library) is where your presets and fragments can go.
- [The project](https://github.com/ossia/score) hosts the issues, the discussions, and the code.
