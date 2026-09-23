---
layout: default
title: "Lesson 38: Using the documentation and reporting issues"
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

# Lesson 38: Using the documentation and reporting issues

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 37]({{ site.baseurl }}/learn/37-recording-and-streaming.html), because this lesson works from the list you have been keeping since Lesson 02.
>
> **You will need** the list of unanswered questions that this course has asked you to keep.
>
> **You will build** one good issue report, together with a routine for turning your own confusion into a contribution the project can use.

## Why this matters

*ossia score* is made by a small number of people, largely one, and its documentation reflects that circumstance: it is excellent in places, thin in others, and improved mainly when a user says precisely what was missing. Complaining that the documentation is incomplete is accurate but useless, whereas saying "the page on X does not mention that Y is required, and here is the sentence that would have saved me an hour" is a contribution that takes five minutes to make.

Furthermore, reporting a gap serves you as much as it serves the project, because a gap you report is a gap you will not fall into again, and a project that answers your questions is a project you can rely on. The usability study conducted at the Société des Arts Technologiques rated the documentation as middling, and the fastest way to change that rating is for the people who hit the documentation's limits to say where those limits are.

## Concepts

### The four parts of the manual

The manual has four parts, and knowing which one you want is most of the skill. A **quick start** is short and linear; **common practices** are organised as recipes for whole tasks, such as looping, scenes, spatial audio, and LED design; **in depth** covers the concepts underneath, including execution, routing, musical metrics, and scripting; and a **reference** holds one page per process and per device. When you cannot find something, you are usually looking in the wrong one of the four, which is why the walkthrough asks you to search them separately.

### Examples as documentation

The examples are documentation in their own right, since a shipped example score that does the thing you are attempting teaches more than a page describing it. Moreover, the examples section is large, so open them, take them apart, and keep the ones that taught you something.

### Bug reports and documentation gaps

An issue is either a bug report or a documentation gap. Both belong on the project's tracker, and documentation gaps are welcome there, because they are cheap to fix and hard for a maintainer to notice alone.

## Walkthrough: from confusion to contribution

{: .note }
> A figure for this lesson is pending: it needs contextual help open beside a selected object, which requires interaction. See `checks/38-reading-the-docs.md`.

1. **Take out your list**, because every lesson since Lesson 02 has asked you to note what you could not answer. If your list is empty, you have not been keeping it, and the next-best source is the last task that took you longer than it should have.
2. **Classify each item** as a gap in the documentation, an actual bug, an unimplemented feature, or something you had not yet read, since these receive different treatment and mislabelling one wastes a maintainer's time.
3. **Try `F1` on the relevant object** for each remaining item, because contextual help is the fastest route to an answer: selecting an object and pressing `F1` opens that object's reference page, and most questions are about a specific object. Some will be answered immediately, which tells you that the gap was in your reading rather than in the manual.
4. **Search the four parts separately**, because if you were looking in the reference for a workflow, the answer is in common practices instead. Conversely, if you were looking in common practices for a parameter, look in the reference.
5. **Check the examples**, because for a surprising number of questions an example score is the answer.
6. **Write one report** for the best remaining item, stating what you were trying to do, what you expected, what happened, which version you were on, and which sentence would have prevented the confusion.
7. **Include a reproduction** if the item is a bug, which means the smallest document that shows it, and for this software that usually means a `.score` file you can attach. A bug with a reproduction gets fixed, whereas one without becomes a conversation.
8. **Offer the fix if you can**, because for a documentation gap you have just understood, the two sentences you would have wanted are a better contribution than a request for them.

   {: .note }
   > **The glossary is incomplete, which is itself useful information**, because several entries have headings and no text. However, when you find one that matters to you, it is an ideal first contribution, since you now know what the word means, and writing two sentences is a smaller job than any other item on the maintainers' list.

9. **Say which version you are on**, which is `3.8.2` for this course, because behaviour differs between releases and a report without a version costs a round trip.
10. **Improve your own notes afterwards**, since whatever you just explained to a stranger belongs in your own project documentation too, which is the same practice Lesson 34 asked for.

## What makes a report worth acting on

A report gets acted on when it carries five properties, and the list below runs in order of how often each one is missing.

**A version comes first**, because behaviour differs across releases and the first question a maintainer asks is which build produced the problem.

**A reproduction comes next**, and for a bug it is the smallest document that exhibits the problem, while for a documentation gap it is the page and the sentence you expected to find there.

**The expectation should be stated separately from the result.** "I expected the automation to send values; nothing arrived" is actionable. In contrast, "the automation is broken" is not, and it is usually wrong as well, as Lesson 08 showed.

**Each report should carry one issue**, because three problems in one thread get one of them fixed.

**The tone should assume good faith**, since the person reading the report wrote the software and gave it away. Politeness is only part of the reason, because reports that read as demands get answered last, and the person on the other end is usually one individual with a long list.

## What this course cannot tell you

A course should say plainly, near its end, that parts of this software are documented thinly and a few are documented not at all. In three areas in particular, you will be reading source code, opening examples, or asking, instead of reading a page.

**Newer processes arrive before their reference pages**, because the library grows faster than the manual. When a process has no page, its ports and its example presets are the documentation, and `F1` will tell you which case you are in.

**The edges of the graph model are not fully written down.** What happens when an unusual combination of loops, conditions, and out-of-time material interact is not documented in full, and the answer is often "try it and observe", which is a legitimate method as long as you write down what you found.

**Experimental features describe intent**, since distributed authoring, the web build, and some newer integrations are research rather than product, so their documentation should be read as a description of where the project is going.

Nevertheless, this situation is normal for a project of this size, and it is why the reporting routine matters, because each of these areas improves in only one way, which is that somebody who worked it out writes it down.

Keep the list beyond this course, since the questions you cannot answer are the most valuable notes you make; they are the only record of where the tool and your understanding do not yet meet. Reviewing that list every few months shows you which gaps closed by themselves, which closed because you learned something, and which are still worth reporting.

There is one more reason to file a report instead of working around a gap, and it concerns the health of the tool rather than your own convenience. A project whose users report gaps gets documentation that reflects real use, whereas a project whose users quietly develop private workarounds accumulates folklore instead, and folklore does not survive its holders moving on. In other words, every report is a small transfer from private knowledge into shared knowledge.

## Common mistakes

- **Not using `F1`**, and concluding from that omission that no per-object documentation exists.
- **Searching the reference for a workflow**, or common practices for a parameter, when each part answers a different kind of question.
- **Reporting three things at once**, so that at most one of them gets fixed.
- **Omitting the version**, which costs the maintainer a round trip before work can start.
- **Omitting a reproduction** for a bug that needs one.
- **Describing a diagnosis instead of a symptom**, when the maintainer needs to hear what you saw and to draw the conclusion themselves.
- **Not contributing the answer** once you have found it, although you are the best-placed person who will ever exist to write that sentence.

## Exercise

File one report, either a documentation gap with the two sentences you would have wanted or a bug with a minimal reproducing document. Then take a second item from your list and answer it yourself using only the manual and the examples, recording which of the four parts held the answer.

**Success criterion:** the report contains a version, one issue, and either a reproduction or proposed wording. For the self-answered item, you can name the part of the manual that held it, which tells you where to look first next time.

## Going further

- [The documentation]({{ site.docs_baseurl }}) itself, with its four sections, deserves one browse as a map before you need it.
- [The glossary]({{ site.docs_baseurl }}/reference-manual/references/glossary.html), including its unfinished entries, shows where a first contribution could land.
- [The examples]({{ site.docs_baseurl }}/examples/examples.html) remain underused, although they answer many questions that no page does.
- The project on [GitHub](https://github.com/ossia/score) holds the tracker, and [score-docs](https://github.com/ossia/score-docs) is where to go if you would rather write the page than request it.
