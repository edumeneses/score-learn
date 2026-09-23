---
layout: default
title: "Lesson 07: OSC devices: sending, receiving, and debugging"
description: "Declare an OSC device by hand, build its address tree, and prove what is actually leaving score when a message seems not to arrive."
parent: Lessons
nav_order: 8
unit: "07"
permalink: /learn/07-osc-devices.html
score_version: "3.8.2"
reading_time: "14 min"
practice_time: "30 min"
score_file: 00-what-score-is/lesson-00.score
---

# Lesson 07: OSC devices: sending, receiving, and debugging

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 06]({{ site.baseurl }}/learn/06-device-model.html) and bring the device map you wrote there.
>
> **You will need** *score*, together with something that receives OSC; a Pure Data or Max patch, a Python script of six lines, an OSC monitor utility, or a second copy of *score* will all serve.
>
> **You will build** one hand-declared OSC device with a small tree of typed parameters, together with a debugging routine that you will use for the rest of the course.

## Why this matters

Open Sound Control (OSC) is the lingua franca of this field, and it is also the archetype of the blind protocols that Lesson 06 described. A plain OSC device cannot be interrogated, so *score* accepts whatever you declare. In other words, every mistake you make is silent, which is why this lesson spends half its length on how to see what is happening.

The debugging routine matters more than the declaration itself, because "it does not work" has three quite different causes with three different fixes: the message did not leave *score*, the message left and went somewhere else, or the message arrived and the receiver ignored it. Distinguishing them takes about thirty seconds once you know where to look. In contrast, the same distinction can take an afternoon without the routine.

## Concepts

### Sending and listening ports

The dialog names two ports, and they point in opposite directions. `Device host` and `Device listening port` are where *score* sends, meaning the address and port on which your receiver listens, whereas `score listening port` is where *score* receives. The two are independent, so a working setup usually has a different number for each, and sending to the port you are listening on is a common self-inflicted silence.

### Declared addresses

Declaring an address asserts what you believe the receiver contains. Adding an address to a plain OSC device asserts that the other end has a parameter of that name and type, and *score* does not verify that assertion; the address is valid as far as the document is concerned, and a receiver that lacks it will not answer.

### Types on the wire

The declared type changes the bytes on the wire. Whether a parameter is a float, an integer, an impulse, a string, or a list determines how the value is encoded. Moreover, receivers that expect a float and get an integer often do nothing at all, silently, which makes this mismatch the most common cause of a message that arrives and is ignored.

### Impulse messages

An impulse is a message that carries no value. Use it for bangs and triggers, since the arrival is the information. Declaring a trigger as a float and sending 1 works with some receivers and fails with others. In contrast, declaring it as an impulse says what you mean.

## Walkthrough: declare a device and prove it works

1. **Open the device explorer** with `Ctrl+Shift+D`, right-click in it, and choose the OSC protocol from the dialog that appears.
2. **Name the device after its function**, as `lights`, `synth`, or `sensors`, following the naming argument of Lesson 06, since the name will prefix every address in the document.
3. **Set the ports** by entering the address and port on which your receiver listens under `Device host` and `Device listening port`, and by choosing a `score listening port` that no other application on the machine is using; write both numbers down, because you will need them in the receiver. If the dialog refuses with a note about names or ports being in use, as in the figure, either the name collides with an existing device or one of the ports is already taken.
4. **Add a parameter** by right-clicking the device and adding an address with a name, a type, and a range, and repeat until you have a small tree: at least one group with two parameters inside it, plus one impulse. No rule forces a flat list, so grouping under intermediate nodes, `/lights/wash/level` in place of `/washlevel`, costs little and keeps the explorer navigable as the tree grows, for the reasons Lesson 06 gave.
5. **Test from the explorer before touching the timeline** by selecting a parameter and setting its value in the panel inspector at the bottom, which sends a message immediately. Your receiver should show the message as soon as you change the value. Additionally, doing this first isolates the connection from the score itself.
6. **Watch what leaves** by opening the message log with `Ctrl+Shift+G` and the console with `Ctrl+Shift+C`, which show whether a message left *score* at all; that is the first of the three questions.
7. **Watch what arrives** by making your receiver print every message it receives and not only the ones you expect, because an address arriving under a slightly different name is invisible if you listen only for the right one.
8. **Involve the timeline** by dragging one of your parameters onto an interval to create an automation, as in Lesson 04, and playing; the value should move continuously in the receiver.
9. **Break it on purpose** by changing the destination port to a wrong number and playing again. The failure looks like no failure from inside *score*, since no error or warning appears and the automation runs as before, and that silence is the thing to learn to recognise.
10. **Fix it and save**, because the declaration lives in the document and this device therefore travels with your score, as Lesson 05 established.

![The Add device dialog: the protocol list, the devices already declared, and the OSC settings with both ports]({{ site.img }}/07/07-01-add-device.png)

## The thirty-second diagnosis

When a message does not seem to arrive, answer the following questions in order, without skipping ahead, because the order is what makes the routine fast.

1. **Check whether *score* sent the message at all**, using the message log at `Ctrl+Shift+G`. If the log shows no message, the problem is upstream: an automation with no destination, a state whose message you did not save, or a part of the score that did not execute.
2. **Check whether it went to the right place** by comparing the destination host and port against the receiver's listening port. Localhost and `127.0.0.1` are the same address, whereas a machine name and its address may not be, and a firewall may drop the difference.
3. **Check whether the receiver heard the message** by printing every incoming message there; if something arrives with an unexpected address or type, you have your answer.
4. **Check whether the type is right**, since float against integer is the usual culprit; compare what you declared against what the receiver expects.
5. **Check whether the range is doing something you did not intend.** An automation mapped 0 to 1 into a parameter that wants 0 to 255 sends values that are technically correct and practically invisible, which is why [Lesson 08]({{ site.baseurl }}/learn/08-units-ranges-types.html) follows this one.

## Choosing a receiver you can trust

Half of the diagnosis above depends on having a receiver that reports faithfully, so the choice of what to test against deserves some care.

**A receiver that prints every message is more useful than one wired to react.** A patch or script that prints every incoming message, address and type included, shows you the failure you are hunting, which is usually an address or a type you did not expect, whereas a receiver wired only to the messages you expect is blind to precisely that.

**Testing on one machine before two removes the network from the question.** Once the setup works over localhost, moving the receiver to another machine isolates any remaining problem to the network, whether a firewall, a wrong address, or a subnet that does not route; done in that order, each step has one variable.

**The loopback shortcut can mislead.** `localhost` and `127.0.0.1` are equivalent, whereas a machine's own hostname may resolve to an address that is not reachable from itself in the way you assume. When something works by address and fails by name, that difference is your answer, and the fix belongs in the rider because a document that will travel should not depend on a name.

**Knowing what your receiver ignores explains many silences.** Many applications discard messages whose type does not match what they expect, and some discard messages to unknown addresses without a word. Neither behaviour counts as a bug in the receiving application. However, both are indistinguishable, from inside *score*, from a message that did not leave.

## Common mistakes

- **Listening and sending on the same port** fails because two applications cannot both bind it, and the symptom is that one of them silently receives no messages.
- **A typo in an address** produces a valid address that no receiver will answer, so copy names from the receiver's own documentation instead of retyping them.
- **Declaring every parameter as a float** is convenient and looks harmless. However, it breaks impulses and integer-typed controls.
- **Testing only through the timeline** means you cannot tell a connection problem from a score problem, which is why step 5 of the walkthrough comes before step 8.
- **Assuming a value column means success** overlooks that many receivers do not echo values back, so an empty column does not show whether your message arrived.
- **Leaving hostnames in a document that will travel** risks an address that resolved in the studio failing to resolve at the venue, so note the numbers in your rider, as [Lesson 34]({{ site.baseurl }}/learn/34-rehearsal-to-show.html) sets out.

## Exercise

Declare one OSC device with at least six parameters in at least two groups, including one impulse and one integer, and drive three of them from a fifteen-second score: one from a state, one from an automation, and the impulse from a state at the end.

Then break it three ways, one at a time, and record what each failure looks like from inside *score*: a wrong destination port, a wrong type on the integer parameter, and an address renamed in the receiver but not in *score*.

**Success criterion:** you can describe, for each of the three failures, which step of the thirty-second diagnosis would have caught it. If any of the three produced a visible error inside *score*, note it, because most of them do not, and knowing which failures are silent is what the exercise teaches.

## Going further

- [The OSC device]({{ site.docs_baseurl }}/devices/osc-device.html) is the reference page, and [OSCQuery]({{ site.docs_baseurl }}/devices/oscquery-device.html) does all of this automatically when the other end supports it.
- [Monitoring activity]({{ site.docs_baseurl }}/faq/monitor-activity.html) documents the message log and console panels used above.
- [Controlling *score* with OSCQuery]({{ site.docs_baseurl }}/faq/controlling-score-with-oscquery.html) is the page that [Lesson 36]({{ site.baseurl }}/learn/36-distributed-scores.html) builds on.

{% include lesson_files.html %}
