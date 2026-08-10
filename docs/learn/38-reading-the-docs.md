---
layout: default
title: "Lesson 38: Reading the documentation, and reporting what is missing"
description: "Navigate the reference manual, use contextual help properly, and turn a gap you found into a report someone can act on."
parent: Lessons
nav_order: 44
unit: "38"
permalink: /learn/38-reading-the-docs.html
score_version: "3.8.2"
reading_time: "10 min"
practice_time: "15 min"
score_file: none
---

# Lesson 38: Reading the documentation, and reporting what is missing

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 37]({{ site.baseurl }}/learn/37-recording-and-streaming.html).
>
> **You will need** the list of unanswered questions this course has been asking you to keep.
>
> **You will build** one good issue report, and the habit of turning your own confusion into something useful.

## Why this matters

*ossia score* is made by a small number of people, largely one, and its documentation reflects that: excellent in places, thin in others, and improved mainly when a user says precisely what was missing. Complaining that the documentation is incomplete is accurate and useless; saying "the page on X does not mention that Y is required, and here is the sentence that would have saved me an hour" is a contribution that takes five minutes.

This is also self-interested. A gap you report is a gap you will not fall into again, and a project that answers your questions is a project you can rely on. The usability study rated the documentation as middling; the fastest way to change that is for the people who hit its limits to say where.

## Concepts

**The manual has four parts, and knowing which one you want is most of the skill.** A **quick start** that is short and linear. **Common practices**, organised as recipes for whole tasks: looping, scenes, spatial audio, LED design. **In depth**, for the concepts underneath: execution, routing, musical metrics, scripting. And a **reference** with one page per process and per device. When you cannot find something, you are usually looking in the wrong one of the four.

**Contextual help is the fastest route.** Select an object and press `F1`. It opens that object's reference page. Most questions are about a specific object, and this answers them without a search.

**The examples are documentation.** A shipped example score that does the thing you are attempting is worth more than a page describing it, and the examples section is large. Open them, take them apart, and keep the ones that taught you something.

**The glossary is incomplete, and that is useful information.** Several entries have headings and no text. When you find one that matters to you, that is an ideal first contribution: you now know what the word means, and writing two sentences is a smaller job than anything else on the maintainers' list.

**An issue is a bug report or a documentation gap.** Both belong on the project's tracker, and documentation gaps are genuinely welcome, because they are cheap to fix and hard for a maintainer to notice alone.

## Walkthrough: from confusion to contribution

{: .note }
> A figure for this lesson is pending: it needs contextual help open beside a selected object, which requires interaction. See `checks/38-reading-the-docs.md`.

1. **Take out your list.** Every lesson since Lesson 02 has asked you to note what you could not answer. If your list is empty, you have not been keeping it, and the next-best source is the last thing that took you longer than it should have.
2. **Classify each item.** Is it a gap in the documentation, an actual bug, an unimplemented feature, or something you simply had not read yet? These get different treatment, and mislabelling wastes a maintainer's time.
3. **Try `F1` on the relevant object** for each remaining item. Some will be answered immediately, which tells you the gap was in your habits rather than in the manual.
4. **Search the four parts deliberately.** If you were looking in the reference for something that is a workflow, look in common practices instead, and vice versa.
5. **Check the examples.** For a surprising number of questions, an example score is the answer.
6. **Now write one report** for the best remaining item. What you were trying to do, what you expected, what happened, what version, and what sentence would have prevented it.
7. **Include a reproduction** if it is a bug: the smallest document that shows it, which for this software usually means a `.score` file you can attach. A bug with a reproduction gets fixed; one without is a conversation.
8. **Offer the fix if you can.** For a documentation gap you have just understood, the two sentences you would have wanted are a better contribution than a request for them.
9. **Say what version you are on.** `3.8.2` for this course. Behaviour differs between releases, and a report without a version costs a round trip.
10. **Then improve your own notes.** Whatever you just explained to a stranger belongs in your own project documentation too, which is the same discipline Lesson 34 asked for.

## What makes a report worth acting on

Five properties, in order of how often they are missing.

**A version.** Behaviour differs across releases, and the first question is always which build.

**A reproduction.** For a bug, the smallest document that exhibits it. For a documentation gap, the page and the sentence you expected to find.

**The expectation, stated separately from the result.** "I expected the automation to send values; nothing arrived" is actionable. "The automation is broken" is not, and is also usually wrong, per Lesson 08.

**One issue per report.** Three problems in one thread get one of them fixed.

**A tone that assumes good faith.** The person reading it wrote the software and gave it away. This is not only politeness: reports that read as demands get answered last, and the person on the other end is usually one individual with a long list.

## What this course cannot tell you

Worth saying plainly at the end of a course: parts of this software are documented thinly, and a few are documented not at all. Three areas where you will be reading source code, examples, or asking, rather than reading a page.

**Newer processes.** The library grows faster than its reference pages. When a process has no page, its ports and its example presets are the documentation, and `F1` will tell you which case you are in.

**The edges of the graph model.** Exactly what happens when an unusual combination of loops, conditions, and out-of-time material interact is not fully written down, and the answer is often "try it and observe", which is a legitimate method as long as you write down what you found.

**Anything experimental.** Distributed authoring, the web build, and some newer integrations are research rather than product. Treat their documentation as a description of intent.

This is normal for a project of this size, and it is why the reporting habit matters. Each of these areas gets better in exactly one way: somebody who worked it out writes it down.

One habit worth carrying past this course: keep the list. The questions you cannot answer are the most valuable notes you make, because they are the only record of where the tool and your understanding do not yet meet. Reviewing that list every few months is how you find out which gaps closed by themselves, which closed because you learned something, and which are still worth reporting.

There is one more reason to file rather than to work around, and it is about the health of the tool rather than about you. A project whose users report gaps gets documentation that reflects real use; a project whose users quietly develop private workarounds accumulates folklore instead, and folklore does not survive its holders moving on. Every report is a small transfer from private knowledge into shared knowledge.

## Common mistakes

- **Never using `F1`**, and concluding there is no per-object documentation.
- **Searching the reference for a workflow**, or common practices for a parameter.
- **Reporting three things at once.**
- **No version.**
- **No reproduction**, for something that clearly needs one.
- **Describing a diagnosis rather than a symptom.** Say what you saw; let the maintainer diagnose.
- **Not contributing the answer** once you have found it. You are the last person who will ever be as well placed to write that sentence.

## Exercise

File one report: either a documentation gap with the two sentences you would have wanted, or a bug with a minimal reproducing document. Then take a second item from your list and answer it yourself using only the manual and the examples, recording which of the four parts held the answer.

**Success criterion:** the report contains a version, one issue, and either a reproduction or proposed wording. For the self-answered item, you can name the part of the manual that held it, which tells you where to look first next time.

## Going further

- [The documentation]({{ site.docs_baseurl }}) itself, and its four sections, worth browsing once as a map.
- [The glossary]({{ site.docs_baseurl }}/reference-manual/references/glossary.html), including its unfinished entries.
- [The examples]({{ site.docs_baseurl }}/examples/examples.html), which are underused.
- The project on [GitHub](https://github.com/ossia/score), for the tracker, and [score-docs](https://github.com/ossia/score-docs) if you would rather write the page than request it.
