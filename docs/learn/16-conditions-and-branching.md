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

> **Before this lesson** finish [Lesson 15]({{ site.baseurl }}/learn/15-triggers.html), because conditions and triggers act on the same instants.
>
> **You will need** `lesson-16.score` and an input whose value you can set by hand.
>
> **You will build** a score with two mutually exclusive branches, and a third that runs in parallel with whichever of them is chosen.

## Why this matters

A trigger changes *when* something happens, whereas a condition changes *what* happens. Together they are the whole of interactive structure, and the difference between them needs stating plainly because they are easy to conflate. In other words, a trigger waits for a moment while a condition decides a path, and a score can have either, both, or neither at any instant.

Moreover, branching is where a *score* document stops being expressible as a linear rendering, because once two branches leave one instant there is no single timeline any more. That is the capability that makes an installation possible, since the same document then behaves differently depending on what happened, and the walkthrough below builds the simplest case of it.

## Concepts

### Conditions belong to events

A condition belongs to an event and not to a state. Lesson 02 insisted on this distinction, and here is where it pays, because messages live on states while conditions live on events; an instant can carry several events, each with its own condition, and that is the mechanism of a branch.

### Splitting an instant

Splitting an instant is what turns parallel branches into alternatives. By default, two intervals leaving the same instant share one event, which means they run together, so each branch needs its **own event** and each event its own condition before they can exclude one another.

### Parallel and exclusive branches

Parallel and exclusive branches are both useful, and the distinction is structural. Intervals on the *same* event run in parallel every time. In contrast, intervals on *separate* events at the same instant, each with a condition, are alternatives; a score often wants both at once, with a branch that chooses alongside a layer that always runs.

### Condition expressions

A condition is an expression over the values in the device tree. It is built from comparisons and combinations, such as `sensors:/level > 0.5` or a conjunction of several such tests, and it is evaluated when the instant is reached, using the values at that moment; no earlier value is retained unless you retained it yourself, which the section on where the state lives develops.

### Offset behaviour

Offset behaviour decides how a condition is read during a transport jump. When you jump the playhead into the middle of a score, conditions must be evaluated although the world is not necessarily in the right state, so each condition has an **offset behaviour** setting that treats it as true, treats it as false, or evaluates it against the live value in the device tree. The setting exists for a real rehearsal problem, which [Lesson 18]({{ site.baseurl }}/learn/18-cues-and-transport.html) solves with it: you should be able to rehearse the branch where the performer stands downstage without asking them to go and stand there.

## Walkthrough: two branches and a layer

![Two conditional branches leaving one instant, with a third interval running in parallel]({{ site.img }}/16/16-01-branching.png)

1. **Open `lesson-16.score`**, which contains one instant with two outgoing intervals carrying opposing conditions on the same address, so that one of them runs and only one.
2. **Set the input low and play**, so that one branch runs; stop, set the input high, and play again, so that the other runs, which shows the same document producing two behaviours decided at the instant.
3. **Set the value on the boundary itself** and play, and the branch written with the inclusive comparison runs. This is more than a technicality, because boundary values happen constantly with real sensors, and a pair of conditions that both exclude the boundary produces a score that occasionally stops dead.
4. **Now build your own**, with two chained intervals, and at the second instant drag out a second outgoing interval so that two leave the same point.
5. **Play it and watch both run**, because they share one event; this is the parallel case, and seeing it once makes the symptom recognisable before you fix it.
6. **Split the condition** using the scenario's split function on that instant, so that the two branches sit on separate events.

   {: .note }
   > **The commands for this step live in the `Object` menu.** `Add Condition`, shortcut `C`, and `Remove Condition`, `Shift+C`, sit there together with `Merge events` and `Synchronize`, `Shift+M`, which control whether things share an instant at all.

7. **Give each event a condition**, the two opposing each other and covering the boundary between them without a gap.
8. **Add a third interval on the original event** with no condition, so that it runs in every case; you now have a score that chooses between two paths while a common layer continues underneath, which is the shape of most real interactive work.
9. **Set the offset behaviour** on one condition to *true* and on the other to *false*, then jump the playhead past the branch with the transport tools of Lesson 18, and observe which branch you land in, which is the outcome you chose in the settings.
10. **Delete a condition**, by selecting it and pressing `Delete` or `Backspace`, and play again, so that you see how a conditionless branch behaves and recognise it when it happens by accident.

## Coverage: the discipline that makes branches reliable

A set of conditions at one instant obeys two rules, and violating either produces one of the two classic branching failures.

**Cover the whole input range**, so that for every value the input can take, at least one condition is true. The pair `> 0.5` and `< 0.5` leaves 0.5 uncovered, and a score that reaches that instant with a reading of 0.5 proceeds nowhere, whereas `>= 0.5` and `< 0.5` cover the boundary; the case seems marginal on paper, although step 3 showed how easily a real sensor produces it.

**Do not overlap unless you mean to**, because if two conditions can be true at once, both branches run. That is sometimes what you want, although when it is not, it is a confusing bug, because it only appears for part of the input range.

Both rules are satisfied at once when the conditions form a partition of the input range, written in one place, with a comment stating what happens at each boundary; when a branch has three or more alternatives, writing them as a table in your project notes before writing them in the score makes gaps and overlaps visible before they reach a rehearsal.

## Where the state lives

A condition tests values at the moment the instant is reached and has no memory of earlier moments, which determines how you write any behaviour that depends on history, and which is the most common structural confusion after the split-condition step.

If a branch should depend on **what happened earlier**, that history has to be stored somewhere a condition can read, and three places serve, in order of preference.

**A device parameter is the simplest and most visible place.** Write a value from a state and read it in a later condition, so that the history is a number in the device explorer, which you can watch while rehearsing.

**The structure itself can hold the memory**, when instead of remembering that the visitor already triggered the piece once, you put the second interaction in a different part of the score, reached only by having been through the first. Structure as memory is more work to draw. Nevertheless, it cannot become inconsistent, which is the reason it ranks above a script.

**A script is the last resort among the three places.** A JavaScript process can hold state between ticks, which Module J covers. However, that state is invisible to anyone reading the score, which is why it comes after the two visible options.

What you cannot do is expect a condition to know what a previous condition decided, because no value is retained unless you retained it; the failure mode is a branch that works in rehearsal, where you performed the steps in order, and fails in front of an audience who did not.

## Common mistakes

- **Forgetting to split the instant**, so that both branches run every time; it is the step people miss, and the symptom is unmistakable.
- **A gap at the boundary**, so that the score occasionally stops progressing.
- **An overlap between conditions**, so that two branches occasionally run together.
- **A condition looked for on a state instead of an event**, when the field is on the event.
- **Leaving an experimental condition in place**, which produces a branch that is silently unreachable.
- **Ignoring offset behaviour** until the first rehearsal where you need to skip into the middle of a scene.
- **Testing only the branch you expect**, when each branch and each boundary needs its own test, because a branch that has not run yet is a branch that does not work.

## Exercise

Write a score that responds to one input with three alternatives, one common layer, and a written partition, then test it six times, once in the middle of each of the three ranges and once on each of the two boundaries, recording what happened each time.

**Success criterion:** all six tests produce one branch plus the layer, with no case where no branch runs and no case where two branches run. Additionally, set one condition's offset behaviour and demonstrate that you can rehearse the third branch without setting the input at all.

## Going further

- [The scenario reference]({{ site.docs_baseurl }}/processes/scenario.html) for conditions and splitting.
- [Switches]({{ site.docs_baseurl }}/common-practices/2-switches.html), which builds toggles and reordering from conditional branches.
- [Seek and transport]({{ site.docs_baseurl }}/common-practices/9-seek-and-transport.html) for offset behaviour in context.
- [Scenes]({{ site.docs_baseurl }}/common-practices/6-scenes.html), the structural pattern [Milestone P4]({{ site.baseurl }}/learn/p4-interactive-installation.html) uses.
