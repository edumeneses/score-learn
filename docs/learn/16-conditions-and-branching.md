---
layout: default
title: "Lesson 16: Conditions and branching"
description: "Write a score that chooses: conditions on events, splitting an instant into branches, and what happens during a transport across a condition."
parent: Lessons
nav_order: 19
unit: "16"
permalink: /learn/16-conditions-and-branching.html
score_version: "3.8.2"
reading_time: "14 min"
practice_time: "30 min"
score_file: 16-conditions-and-branching/lesson-16.score
---

# Lesson 16: Conditions and branching

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 15]({{ site.baseurl }}/learn/15-triggers.html).
>
> **You will need** `lesson-16.score` and an input whose value you can set deliberately.
>
> **You will build** a score with two mutually exclusive branches, and a third that runs in parallel rather than instead.

## Why this matters

A trigger changes *when* something happens. A condition changes *what* happens. Together they are the whole of interactive structure, and the difference between them is worth stating plainly because they are easy to conflate: a trigger waits for a moment, a condition decides a path. A score can have either, both, or neither at any instant.

Branching is also where a *score* document stops being expressible as a linear rendering. Once two branches leave one instant, there is no single timeline any more, and that is precisely the capability that makes an installation possible: the same document behaves differently depending on what happened.

## Concepts

**A condition belongs to an event, not to a state.** Lesson 02 insisted on this distinction and here is where it pays. Messages live on states; conditions live on events. An instant can carry several events, each with its own condition, and that is the mechanism of a branch.

**Splitting an instant.** Two intervals leaving the same instant share one event by default, which means they run together. To make them alternatives, each branch needs its **own event**, and each event its own condition. The `Object` menu is where this lives: `Add Condition`, shortcut `C`, and `Remove Condition`, `Shift+C`, together with `Merge events` and `Synchronize`, `Shift+M`, which control whether things share an instant at all. This is the step people miss, and the symptom is unmistakable: both branches run.

**Parallel against exclusive.** Both are useful and the distinction is structural. Two intervals on the *same* event run in parallel, every time. Two intervals on *separate* events at the same instant, each with a condition, are alternatives. A score often wants both at once: a branch that chooses, alongside a layer that always runs.

**A condition is an expression.** Over device values, comparisons and combinations: `sensors:/level > 0.5`, and conjunctions of several such tests. Evaluation happens when the instant is reached, using the values at that moment. Nothing is retained from earlier unless you retained it yourself.

**Deleting a condition.** Select it and press `Delete` or `Backspace`. Worth knowing early, because an experimental condition left in place is a branch that silently never runs.

**Offset behaviour, for transport.** When you jump the playhead into the middle of a score, conditions must be evaluated without the world necessarily being in the right state. Each condition therefore has an **offset behaviour** setting: treat it as true, as false, or evaluate it against the live value in the device tree. This exists for a real rehearsal problem, and [Lesson 18]({{ site.baseurl }}/learn/18-cues-and-transport.html) uses it: you should be able to rehearse the branch where the performer stands downstage without asking them to go and stand downstage.

## Walkthrough: two branches and a layer

![Two conditional branches leaving one instant, with a third interval running in parallel]({{ site.img }}/16/16-01-branching.png)

1. **Open `lesson-16.score`.** One instant, two outgoing intervals with opposing conditions on the same address, so exactly one runs.
2. **Set the input low and play.** One branch runs. Stop, set the input high, play again: the other. Same document, two behaviours, decided at the instant.
3. **Set the value exactly on the boundary** and play. Whichever branch you wrote with the inclusive comparison runs. This is not a technicality: boundary values happen constantly with real sensors, and a pair of conditions that both exclude the boundary produces a score that occasionally stops dead.
4. **Now build your own.** Two chained intervals, then at the second instant, drag out a second outgoing interval so that two leave the same point.
5. **Play it, and watch both run.** They share one event. This is the parallel case, and it is worth seeing before you fix it.
6. **Split the condition.** Use the scenario's split function on that instant so the two branches sit on separate events.
7. **Give each event a condition**, opposing, and covering the boundary between them without a gap.
8. **Add a third interval on the original event**, with no condition, so it runs in every case. You now have a score that chooses between two paths while a common layer continues underneath, which is the shape of most real interactive work.
9. **Set the offset behaviour** on one condition to *true* and on the other to *false*, then jump the playhead past the branch with the transport tools of Lesson 18. Observe which branch you land in, and note that you chose that outcome deliberately.
10. **Delete a condition** and play again, to see how obviously a conditionless branch behaves, so that you recognise it when it happens by accident.

## Coverage: the discipline that makes branches reliable

Two rules, and violating either produces the two classic branching failures.

**Cover the whole input range.** For every value the input can take, at least one condition must be true. Two conditions, `> 0.5` and `< 0.5`, leave 0.5 uncovered, and a score that reaches that instant with exactly 0.5 proceeds nowhere. Write `>= 0.5` and `< 0.5` instead. This sounds pedantic until it happens in front of an audience.

**Do not overlap unless you mean to.** If two conditions can be true at once, both branches run. That is sometimes exactly right, and when it is not, it is a very confusing bug, because it only appears for part of the input range.

The reliable habit is to write conditions as a partition, in one place, and to state in a comment what happens at each boundary. When a branch has three or more alternatives, write them as a table in your project notes before writing them in the score.

## Where the state lives

A condition tests values at the moment the instant is reached. It has no memory. That single fact determines how you write anything that depends on history, and it is the most common structural confusion after the split-condition step.

If a branch should depend on **what happened earlier**, that history has to be stored somewhere a condition can read. Three places, in order of preference.

**In a device parameter.** Write a value from a state, read it in a later condition. The simplest and most visible option: the history is a number in the device explorer, which you can watch while rehearsing.

**In the structure itself.** Instead of remembering that the visitor already triggered the piece once, put the second interaction in a different part of the score, reached only by having been through the first. Structure as memory is more work to draw and impossible to get inconsistent.

**In a script.** A JavaScript process can hold state between ticks, which Module J covers. Powerful and invisible to anyone reading the score, so it is the last resort rather than the first.

What you cannot do is expect a condition to know what a previous condition decided. Nothing is retained unless you retained it, and the failure mode is a branch that works in rehearsal, where you performed the steps in order, and fails in front of an audience who did not.

## Common mistakes

- **Forgetting to split the instant**, so both branches run every time.
- **A gap at the boundary**, so the score occasionally stops progressing.
- **An overlap**, so two branches occasionally run together.
- **A condition on a state instead of an event.** Look in the right place; the field is on the event.
- **Leaving an experimental condition in place**, producing a branch that is silently unreachable.
- **Ignoring offset behaviour** until the first rehearsal where you need to skip into the middle of a scene.
- **Testing only the branch you expect.** Test each branch, and each boundary, deliberately. A branch that has never run is a branch that does not work.

## Exercise

Write a score that responds to one input with three alternatives, one common layer, and a written partition. Then test it six times: once in the middle of each of the three ranges, and once exactly on each of the two boundaries. Record what happened each time.

**Success criterion:** all six tests produce exactly one branch plus the layer, with no case where nothing runs and no case where two branches run. Then set one condition's offset behaviour and demonstrate that you can rehearse the third branch without setting the input at all.

## Going further

- [The scenario reference]({{ site.docs_baseurl }}/processes/scenario.html) for conditions and splitting.
- [Switches]({{ site.docs_baseurl }}/common-practices/2-switches.html), which builds toggles and reordering from conditional branches.
- [Seek and transport]({{ site.docs_baseurl }}/common-practices/9-seek-and-transport.html) for offset behaviour in context.
- [Scenes]({{ site.docs_baseurl }}/common-practices/6-scenes.html), the structural pattern [Milestone P4]({{ site.baseurl }}/learn/p4-interactive-installation.html) uses.
