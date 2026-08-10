---
layout: default
title: "Lesson 34: Rehearsal to show"
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

# Lesson 34: Rehearsal to show

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 33]({{ site.baseurl }}/learn/33-custom-interfaces.html), and have one of your milestone documents to hand.
>
> **You will need** the document, and the notes you have been keeping since Lesson 06.
>
> **You will build** the paperwork that turns a working document into a producible piece: a rider, a dependency list, a cue sheet, and a failure plan.

## Why this matters

Every lesson in this course has asked you to write something down: a device map in Lesson 06, ranges in Lesson 08, a channel map in Milestone P2, layout coordinates in Lesson 22, plug-in dependencies in Lesson 21, a venue block in Milestone P6. This lesson collects them, because scattered notes are not documentation and the difference shows at the load-in.

The framing worth adopting: your document is one deliverable, and the paperwork is the other. A piece that only you can install is a piece that will be performed as often as you are available, which is not the same as often.

## Concepts

**Score hygiene.** Names on every interval and state, colours used consistently, structure legible when folded with `Ctrl+Alt+F`. This is not tidiness for its own sake: a folded, named score is the thing you will read at eight in the morning when something is wrong.

**The dependency list.** Everything the document needs that it does not contain: *score*'s version, plug-ins with their formats, addons from the package manager, Pure Data and its externals, fonts, and any external application. Each with a version, and each with where it came from.

**The technical rider.** What the piece needs from the venue: audio channels and what each carries, video outputs and resolutions, network requirements, lighting universes, physical layout. Written for a technician who has never met you and will not read prose.

**The cue sheet.** What happens, in order, with the timings that matter and the interactions that are not automatic. This is the document a stage manager works from, and writing it usually reveals a decision you had not made.

**The failure plan.** For each part that can fail, what the piece does and what the operator should do. A sensor unplugged, a projector that does not wake, a network that is missing, a machine that reboots mid-show. Deciding this in advance is the difference between a pause and a cancellation.

**The reduced version.** A tested, smaller configuration for the venue that has less than the rider asks for. Milestone P6 introduced this; it applies to every piece with a media requirement.

## Walkthrough: five documents in ninety minutes

{: .note }
> A figure for this lesson is pending: it needs a folded, named score beside its documentation, which requires interaction. See `checks/34-rehearsal-to-show.md`.

1. **Fold your score** and read it. Every interval should have a name that means something. Fix the ones that do not; this is the cheapest legibility work available.
2. **Colour by function**, not by taste: one colour for interactive material, one for automatic, one for anything unfinished. Consistency matters more than the palette.
3. **Write the dependency list** by walking the document rather than by memory. Every hosted plug-in, every referenced patch, every addon, every media format. Then test it by opening the document on a machine that has none of them and recording what breaks.
4. **Write the rider** from the device map you have been keeping since Lesson 06: channels, outputs, universes, network. State what is essential and what is preferred, separately, because a venue can meet one and not the other.
5. **Write the cue sheet** from the folded score: sections, durations, and every point where a human does something. Where a cue is interactive, say what fires it and what the maximum wait is.
6. **Write the failure plan.** One line per failure mode: what the audience sees, what the operator does, and whether the piece can continue. Include the two failures nobody plans for: a projector that shows the desktop, and a machine that reboots during the show.
7. **Add the safety behaviours** if they are not already there: a start cue that puts the world in a known state, a stop cue that leaves nothing on, and a maximum duration on every waiting instant. Lessons 15 and 18 built these; this is the checklist that confirms they exist.
8. **Prepare the reduced version** and test it, rather than describing it.
9. **Do a cold start.** Reboot the machine, open the document, and run the piece from your own paperwork without touching anything else. Note every step you had to improvise, because each one is a gap in the documentation.
10. **Have somebody else do a cold start.** This is the real test, and it will find things the previous step could not.

## The thirty-second version

Because full documentation is often not read, every piece should also have a single card, on one side of one page, in the language of the person holding it. Four things:

**How to start it.** The exact sequence, including turning things on in order if that matters.

**What "working" looks like.** A sentence describing the idle or opening state, so the reader can tell whether it is running correctly without understanding it.

**How to stop it.** Including what stopping does, so nobody is surprised by a blackout.

**Who to call**, and what to tell them.

This card is what actually gets used. The rider, the dependency list, and the cue sheet exist so that the card can be short.

## The two-week test

A single question that predicts whether a piece will be performed again: could you reinstall it in two weeks, having forgotten everything?

Not could you rebuild it, could you *reinstall* it. Two weeks is long enough to lose the details and short enough that you cannot blame time. If the answer is no, the gap is documentation, and it is worth finding now while the knowledge still exists.

The test has a stronger form that is worth doing once in your working life: put the project directory and its documents aside, deliberately do not look at them for two weeks, and then install the piece from the paperwork alone, resisting the urge to remember. Every point where you had to remember something instead of reading it is a line missing from the documentation, and the list you produce that way is more accurate than any amount of careful writing at the time.

Pieces that pass this get programmed again, lent to festivals, and installed by other people. Pieces that fail it exist for as long as their author is available, which is a smaller life than the work deserves.

One more document worth having, for pieces that will travel: a photograph of the working setup. Cables, connections, the projector's menu settings, the position of the sensor. It takes a minute, it answers questions no written rider anticipates, and it is the first thing you will look for when something is different at the second venue.

## Common mistakes

- **Documentation written for yourself.** If it uses the words "scenario", "interval", or "process", the operator's card is not finished.
- **A dependency list from memory.** Walk the document; you will find something you forgot.
- **No cold start test.** Everything works on the machine where it was built, in the state it was left.
- **A rider that does not separate essential from preferred.** Venues will meet what they can, and they cannot guess which is which.
- **No failure plan.** Then the plan is improvisation, in front of an audience.
- **A reduced version that has never been run.** It is a promise, not a fallback.
- **Leaving the safety cues for later.** Later is the technical rehearsal, and it will be busy.

## Exercise

Produce the five documents for one milestone piece: dependency list, rider, cue sheet, failure plan, and the one-page card. Then perform two tests. First, open the document on a machine missing one dependency and confirm the failure is the one your list predicted. Second, have somebody who has never seen the piece start it, run it, and stop it using only the card.

**Success criterion:** the card alone is sufficient for a cold start by a stranger, and your dependency list correctly predicted what broke on the incomplete machine. Every question the stranger asked is now on the card or in the rider.

## Going further

- [Start and stop cues]({{ site.docs_baseurl }}/common-practices/7-start-stop-cues.html) and [seek and transport]({{ site.docs_baseurl }}/common-practices/9-seek-and-transport.html), the two mechanisms this lesson audits.
- [Scenes]({{ site.docs_baseurl }}/common-practices/6-scenes.html) for the structure that makes a cue sheet writable.
- [The package manager]({{ site.docs_baseurl }}/in-depth/package-manager.html) for addon dependencies.
- [Headless and embedded]({{ site.baseurl }}/learn/35-headless-and-embedded.html) next, for pieces that run on a machine with no operator at all.
