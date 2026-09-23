---
layout: default
title: "Lesson 34: From rehearsal to show: riders, cue sheets, and failure plans"
description: "Score hygiene, a dependency list, a technical rider, and a failure plan: turning a document that works into a piece that can be produced."
parent: Lessons
nav_order: 40
unit: "34"
permalink: /learn/34-rehearsal-to-show.html
score_version: "3.8.2"
reading_time: "12 min"
practice_time: "20 min"
score_file: none
---

# Lesson 34: From rehearsal to show: riders, cue sheets, and failure plans

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 33]({{ site.baseurl }}/learn/33-custom-interfaces.html), and have one of your milestone documents to hand, because the paperwork is written against a real piece.
>
> **You will need** the document, and the notes you have been keeping since Lesson 06.
>
> **You will build** the paperwork that turns a working document into a producible piece, which consists of a rider, a dependency list, a cue sheet, and a failure plan.

## Why this matters

Every lesson in this course has asked you to write something down: a device map in Lesson 06, ranges in Lesson 08, a channel map in Milestone P2, layout coordinates in Lesson 22, plug-in dependencies in Lesson 21, and a venue block in Milestone P6. However, scattered notes do not amount to documentation, and the difference shows at the load-in when a technician needs an answer and you are not there to give it, so this lesson collects them into a set of documents.

The framing to adopt is that your document is one deliverable and the paperwork is the other. A piece that only you can install will be performed as often as you are available, which is a smaller number than it sounds. In other words, the ninety minutes this lesson asks for buy every future performance that would otherwise not happen.

## Concepts

### A legible score

A legible score has names on every interval and state, colours used consistently, and a structure that reads when folded with `Ctrl+Alt+F`. This is not tidiness for its own sake, because a folded, named score is the document you will read at eight in the morning when something is wrong. In contrast, an unnamed one answers no question at that hour.

### The dependency list

The dependency list names what the document needs that it does not contain. That means *score*'s version, plug-ins with their formats, addons from the package manager, Pure Data and its externals, fonts, and any external application, each with a version and each with where it came from.

### The technical rider

The technical rider states what the piece needs from the venue. It covers audio channels and what each carries, video outputs and resolutions, network requirements, lighting universes, and physical layout, and it is written for a technician who has not met you and will not read prose.

### The cue sheet

The cue sheet says what happens, in order, with the timings that matter and the interactions that are not automatic. It is the document a stage manager works from, and writing it usually reveals a decision you had not made.

### The failure plan

The failure plan says, for each part that can fail, what the piece does and what the operator should do. A sensor unplugged, a projector that does not wake, a network that is missing, and a machine that reboots mid-show each need a line, because deciding this in advance is the difference between a pause and a cancellation.

### The reduced version

The reduced version is a tested, smaller configuration for a venue that has less than the rider asks for. Milestone P6 introduced it, and it applies to every piece with a media requirement.

## Walkthrough: five documents in ninety minutes

![The milestone cue folded: three named sections, with their processes reduced to badges]({{ site.img }}/34/34-01-folded.png)

The figure shows Milestone P1's cue with every interval folded, which is what step 1 asks you to produce: three named sections, no slot contents, and a structure readable in one glance. Compared with the same document unfolded in [Milestone P1]({{ site.baseurl }}/learn/p1-automated-cue.html), the folded view is the one you want when the house opens in an hour and a section is misbehaving.

1. **Fold your score and read it, so that every interval has a name that means something.** Fix the ones that do not, because this is the cheapest legibility work available.
2. **Colour by function and not by preference**, with one colour for interactive material, one for automatic, and one for whatever is unfinished, since consistency matters more than the palette.
3. **Write the dependency list by walking the document and not from memory.** Record every hosted plug-in, every referenced patch, every addon, and every media format, then test the list by opening the document on a machine that has none of them and recording what breaks.
4. **Write the rider from the device map you have been keeping since Lesson 06**, covering channels, outputs, universes, and network. State what is essential and what is preferred separately, because a venue can meet one and not the other.
5. **Write the cue sheet from the folded score**, with sections, durations, and every point where a human does something. Where a cue is interactive, say what fires it and what the maximum wait is.
6. **Write the failure plan with a line per failure mode**, saying what the audience sees, what the operator does, and whether the piece can continue. Include the two failures that plans usually omit, a projector that shows the desktop and a machine that reboots during the show.
7. **Add the safety behaviours if they are not already there**, which means a start cue that puts the world in a known state, a stop cue that leaves no output on, and a maximum duration on every waiting instant. Lessons 15 and 18 built these, so this step is the checklist that confirms they exist.
8. **Prepare the reduced version and test it**, since describing it is not the same as having it.
9. **Do a cold start by rebooting the machine, opening the document, and running the piece from your own paperwork** without touching any other source. Note every step you had to improvise, because each one is a gap in the documentation.
10. **Have somebody else do a cold start**, which is the real test, because it finds what the previous step could not.

## The thirty-second version

Because full documentation is often not read, every piece should also have a single card, on one side of one page, in the language of the person holding it, and the card carries four items.

**The card says how to start the piece**, as an exact sequence, including turning things on in order if the order matters.

**It says what "working" looks like**, in a sentence describing the idle or opening state, so that the reader can tell whether the piece is running correctly without understanding it.

**It says how to stop the piece**, including what stopping does, so that no one is surprised by a blackout.

**It says who to call and what to tell them**, so that the first phone call already contains the information you will ask for.

This card is the document that gets used on the night, whereas the rider, the dependency list, and the cue sheet exist so that the card can be short.

## The two-week test

A single question predicts whether a piece will be performed again: could you reinstall it in two weeks, having forgotten the details?

The question asks about reinstalling and not about rebuilding, because two weeks is long enough to lose the details and short enough that time cannot be blamed. If the answer is no, the gap is documentation, and the moment to find it is now, while the knowledge still exists.

Furthermore, the test has a stronger form that deserves to be done once in your working life: put the project directory and its documents aside, refrain from looking at them for two weeks, and then install the piece from the paperwork alone, resisting the urge to remember. Every point where you had to remember something that you should have been able to read is a line missing from the documentation, and the list you produce that way is more accurate than any amount of careful writing at the time.

Pieces that pass this test get programmed again, lent to festivals, and installed by other people. Conversely, pieces that fail it exist for as long as their author is available, which is a smaller life than the work deserves.

Additionally, a photograph of the working setup is a document to have for pieces that will travel, showing cables, connections, the projector's menu settings, and the position of the sensor. It takes a minute, it answers questions no written rider anticipates, and it is the first thing you will look for when something is different at the second venue.

## Common mistakes

- **Documentation written for yourself** is not finished for an operator; if the card uses the words "scenario", "interval", or "process", the operator's card still needs work.
- **A dependency list from memory** misses something, so walk the document instead.
- **No cold start test** means that the piece has only ever worked on the machine where it was built, in the state it was left.
- **A rider that does not separate essential from preferred** leaves the venue guessing, because venues will meet what they can and cannot know which is which.
- **No failure plan** means the plan is improvisation, in front of an audience.
- **A reduced version that has never been run** is a promise and not a fallback.
- **Leaving the safety cues for later** puts them in the technical rehearsal, which will be busy.

## Exercise

Produce the five documents for one milestone piece, which are the dependency list, the rider, the cue sheet, the failure plan, and the one-page card, and then perform two tests. First, open the document on a machine missing one dependency and confirm that the failure is the one your list predicted; second, have somebody who has never seen the piece start it, run it, and stop it using only the card.

**Success criterion:** the card alone is sufficient for a cold start by a stranger, and your dependency list correctly predicted what broke on the incomplete machine. Every question the stranger asked is now on the card or in the rider, so that the next stranger asks fewer.

## Going further

- [Start and stop cues]({{ site.docs_baseurl }}/common-practices/7-start-stop-cues.html) and [seek and transport]({{ site.docs_baseurl }}/common-practices/9-seek-and-transport.html), the two mechanisms this lesson audits.
- [Scenes]({{ site.docs_baseurl }}/common-practices/6-scenes.html) for the structure that makes a cue sheet writable.
- [The package manager]({{ site.docs_baseurl }}/in-depth/package-manager.html), the source of the addon dependencies the list must record.
- [Headless and embedded]({{ site.baseurl }}/learn/35-headless-and-embedded.html) next, for pieces that run on a machine with no operator at all.
