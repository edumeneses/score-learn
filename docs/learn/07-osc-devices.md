---
layout: default
title: "Lesson 07: Creating and debugging an OSC device"
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

# Lesson 07: Creating and debugging an OSC device

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 06]({{ site.baseurl }}/learn/06-device-model.html) and bring the device map you wrote.
>
> **You will need** *score*, and something to receive OSC. Anything works: a Pure Data or Max patch, a Python script of six lines, an OSC monitor utility, or a second copy of *score*.
>
> **You will build** one hand-declared OSC device with a small tree of typed parameters, and a debugging routine you will use for the rest of the course.

## Why this matters

Open Sound Control is the lingua franca of this field, and it is also the protocol that tells you nothing. A plain OSC device cannot be interrogated: whatever you declare, *score* believes. Every mistake you make is therefore silent, which is exactly why this lesson spends half its length on how to see what is happening.

The debugging routine matters more than the declaration. "It does not work" has three quite different causes, and they have three different fixes: the message never left *score*, the message left and went somewhere else, or the message arrived and the receiver ignored it. Distinguishing them takes about thirty seconds once you know where to look, and can take an afternoon otherwise.

## Concepts

**Two ports, two directions.** The dialog names them precisely, and the names are worth learning because they are asymmetric: **`Device host`** and **`Device listening port`** are where *score* **sends**, meaning the address and port your receiver listens on; **`score listening port`** is where *score* **receives**. They are independent, and a working setup usually has different numbers for each. Sending to the port you are listening on is a classic self-inflicted silence.

**Declaring is asserting.** Adding an address to a plain OSC device asserts that the other end has a parameter of that name and type. Nothing verifies it. A typo produces a perfectly functional address that no receiver will ever answer.

**Type matters at the boundary.** Whether a parameter is a float, an integer, an impulse, a string, or a list changes the bytes on the wire. Receivers that expect a float and get an integer often do nothing at all, silently. This is the most common cause of a message that arrives and is ignored.

**An impulse is a message with no value.** Use it for bangs and triggers: the arrival is the information. Declaring a trigger as a float and sending 1 works with some receivers and not others; declaring it as an impulse says what you mean.

**The address tree is yours to shape.** Nothing forces a flat list. Grouping under intermediate nodes, `/lights/wash/level` rather than `/washlevel`, costs nothing and makes the explorer navigable when there are eighty parameters instead of three.

## Walkthrough: declare a device and prove it works

1. **Open the device explorer**, `Ctrl+Shift+D`, and right-click in it. Choose the OSC protocol.
2. **Name it after its function.** `lights`, `synth`, `sensors`. The name will prefix every address in the document; brand names age badly and equipment gets replaced.
3. **Set the ports.** `Device host` and `Device listening port` are where your receiver listens, so those are what *score* sends to. `score listening port` is where *score* receives, and it must not collide with anything else on the machine. Write both numbers down; you will need them in the receiver. If the dialog refuses with a note about names or ports being in use, as in the figure, either the name collides with an existing device or one of the ports is already taken.
4. **Add a parameter.** Right-click the device and add an address. Give it a name, a type, and a range. Repeat until you have a small tree, at least one group with two parameters inside it, plus one impulse.
5. **Test from the explorer, before touching the timeline.** Select a parameter and set its value in the panel inspector at the bottom. This sends a message immediately. Your receiver should show it. Doing this first isolates the connection from anything about your score.
6. **Watch what leaves.** Open the message log with `Ctrl+Shift+G`, and the console with `Ctrl+Shift+C`. These tell you whether *score* believes it sent something, which is the first of the three questions.
7. **Watch what arrives.** In your receiver, print everything it receives, not only what you expect. An address arriving with a slightly different name is invisible if you only listen for the right one.
8. **Now involve the timeline.** Drag one of your parameters onto an interval to create an automation, exactly as in Lesson 04, and play. The value should move continuously in the receiver.
9. **Break it deliberately.** Change the destination port to a wrong number and play again. Notice what the failure looks like from inside *score*: no error, no warning, the automation runs as before. That silence is the thing to recognise.
10. **Fix it and save.** The declaration lives in the document, so this device travels with your score, as Lesson 05 established.

![The Add device dialog: the protocol list, the devices already declared, and the OSC settings with both ports]({{ site.img }}/07/07-01-add-device.png)

## The thirty-second diagnosis

When a message does not seem to arrive, answer these in order. Do not skip ahead; the order is what makes it fast.

1. **Did *score* send it?** Message log, `Ctrl+Shift+G`. If nothing is logged, the problem is upstream: an automation with no destination, a state whose message you did not save, or a part of the score that never executed.
2. **Did it go to the right place?** Check the destination host and port against the receiver's listening port. Localhost and `127.0.0.1` are the same; a machine name and its address may not be, and a firewall may drop the difference.
3. **Did the receiver hear anything at all?** Print every incoming message there. If something arrives with an unexpected address or type, you have your answer.
4. **Is the type right?** Float against integer is the usual culprit. Check what you declared against what the receiver expects.
5. **Is the range doing something you did not intend?** An automation mapped 0 to 1 into a parameter that wants 0 to 255 sends values that are technically correct and practically invisible. [Lesson 08]({{ site.baseurl }}/learn/08-units-ranges-types.html) is next for exactly this reason.

## Choosing a receiver you can trust

Half of the diagnosis above depends on having a receiver that tells you the truth, so it is worth being deliberate about which one you test against.

**Prefer something that prints everything.** A patch or script that prints every incoming message, address and type included, is far more useful than one wired to react to the messages you expect. The failure you are hunting is usually an address or a type you did not expect, and a selective receiver is blind to exactly that.

**Test on one machine before two.** Localhost removes the network from the question. Once it works locally, move the receiver to another machine and you have isolated any remaining problem to the network: a firewall, a wrong address, or a subnet that does not route. Do it in that order and each step has one variable.

**Beware the loopback shortcut.** `localhost` and `127.0.0.1` are equivalent, but a machine's own hostname may resolve to an address that is not reachable from itself in the way you assume. When something works by address and not by name, that is your answer, and the fix belongs in the rider rather than in the score.

**Know what your receiver ignores.** Many applications silently discard messages whose type does not match what they expect, and some discard messages to unknown addresses without a word. Neither is a bug; both are indistinguishable, from inside *score*, from a message that never left.

## Common mistakes

- **Listening and sending on the same port.** Two applications cannot both bind it, and the symptom is that one of them silently receives nothing.
- **A typo in an address.** It is a valid address. It will never be answered. Copy names from the receiver's own documentation rather than retyping them.
- **Declaring everything as a float.** Convenient, and it breaks impulses and integer-typed controls.
- **Testing only through the timeline.** If you never test from the explorer, you cannot tell a connection problem from a score problem.
- **Assuming a value column means success.** Many receivers do not echo values back. An empty column proves nothing about whether your message arrived.
- **Leaving hostnames in a document that will travel.** An address that resolved in the studio may not resolve at the venue. Note the numbers in your rider, as [Lesson 34]({{ site.baseurl }}/learn/34-rehearsal-to-show.html) sets out.

## Exercise

Declare one OSC device with at least six parameters in at least two groups, including one impulse and one integer, and drive three of them from a fifteen-second score: one from a state, one from an automation, and the impulse from a state at the end.

Then break it three ways, one at a time, and record what each failure looks like from inside *score*: wrong destination port, wrong type on the integer parameter, and an address renamed in the receiver but not in *score*.

**Success criterion:** you can describe, for each of the three failures, which step of the thirty-second diagnosis would have caught it. If any of the three produced a visible error inside *score*, note it; most of them do not, and knowing which are silent is the point.

## Going further

- [The OSC device]({{ site.docs_baseurl }}/devices/osc-device.html) and [OSCQuery]({{ site.docs_baseurl }}/devices/oscquery-device.html), which does all of this automatically when the other end supports it.
- [Monitoring activity]({{ site.docs_baseurl }}/faq/monitor-activity.html), for the panels used above.
- [Controlling *score* with OSCQuery]({{ site.docs_baseurl }}/faq/controlling-score-with-oscquery.html), which [Lesson 36]({{ site.baseurl }}/learn/36-distributed-scores.html) builds on.
