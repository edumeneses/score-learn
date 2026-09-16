---
layout: default
title: "Lesson 36: Distributed scores"
description: "Control one score from another machine, share a performance across several computers, and choose what actually needs synchronising."
parent: Lessons
nav_order: 42
unit: "36"
permalink: /learn/36-distributed-scores.html
score_version: "3.8.2"
reading_time: "15 min"
practice_time: "40 min"
score_file: none
---

# Lesson 36: Distributed scores

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 35]({{ site.baseurl }}/learn/35-headless-and-embedded.html), since the controlled instance is often the headless one described there.
>
> **You will need** two machines on a network, or two instances of *score* running on one machine and listening on different ports.
>
> **You will build** a two-machine piece in which one instance controls another, with a defined answer for what happens when the network fails.

## Why this matters

Work outgrows one computer for ordinary reasons: a projector on one machine and a speaker array on another, a sensor in one room and the sound in the next, or a piece spread across three rooms of a building. The *ossia* project has explored distributed authoring and performance for years, and the practical result available today is direct: **a score can control another score**. Furthermore, *score* itself can be controlled by any program that speaks OSC (Open Sound Control) or WebSockets.

However, the important lesson concerns restraint. Most multi-machine pieces do not need synchronised timelines; they need a handful of cues to arrive reliably, whereas a piece that tries to keep two timelines in lockstep pays for that ambition in fragility. Deciding which messages need to cross the network is the design work, and the mechanisms that carry them are simple once that decision has been made.

## Concepts

**The local device exposes *score* itself as a device**, which means one instance can be addressed in the same way as a synthesiser or a light. When you declare an OSC or OSCQuery device on machine A that points at machine B's local device, A can drive B with the same automations, states, and mappings you have used throughout the course, so that a distributed piece requires no new concept.

**OSCQuery lets the controlled instance be discovered.** Because the local device can describe itself, a controlling instance can import the whole tree instead of declaring it by hand, which is the argument from Lesson 06 for descriptive protocols paying off at the moment an address space becomes large.

**The WebSocket protocol from Lesson 33 is the other route** into a running instance, since it carries transport, triggers, interval speed and gain, values to addresses, and listening. In contrast to the local device, it is the right choice when the controller is not *score* but a browser, a tablet, or a program written for the purpose.

**Four kinds of information can be shared, in increasing order of difficulty.** Cues are discrete messages by which one machine tells another to fire a trigger; values are continuous parameters sent between machines; transport covers start, stop, and position; content is audio or video streamed between machines through the share protocols of Lesson 25. Each step up that list costs more bandwidth and tolerates less latency, which is why the later section on synchronisation follows the same order.

**The network is part of the piece**, because latency, jitter, and packet loss are properties of your production, and a wired connection behaves predictably where a wireless one does not. For any work that is performed, use a cable. However, where a cable is impossible, design so that a late message is survivable.

**A machine outside your network can still be reached.** For remote installations, a virtual private network such as ZeroTier puts machines on one logical network regardless of where they are physically, which is how a piece in another city gets maintained without travel. The *ossia* community has published this workflow.

## Walkthrough: two instances, one piece

{: .note }
> A figure for this lesson is pending: it needs two machines and their device trees, which requires interaction and hardware. See `checks/36-distributed-scores.md`.

1. **Start on one machine with two instances** listening on different ports, because every step below then works identically while the network cannot yet be blamed for any fault.
2. **Enable the local device** on the instance that will be controlled, and note the ports it announces, since the controlling instance will need them in the next step.
3. **Declare a device on the controlling instance** that points at the controlled one. If OSCQuery is available, import the tree; if it is not, declare the few addresses you need by hand.
4. **Fire a cue across the link** by sending a value that fires a trigger on the controlled instance, as Lesson 15 described. This is the smallest useful distributed piece, and for many productions it is the whole design.
5. **Send a continuous value** and watch it arrive, then send it as fast as you can and observe what the network does to it. Add a rate limiter on the sending side, as in Lesson 13, so that the link carries only the values it can deliver.
6. **Control the transport** by starting and stopping the controlled instance from the controller, and note the delay between the command and the response, because that figure becomes the baseline for the measurements that follow.
7. **Separate the machines** by moving the second instance to another computer over a wired connection, and repeat every step. Record the latency you measure, which will differ from the latency you expected.
8. **Introduce a failure** by unplugging the network in the middle of the piece, and write down what each machine did, whether it kept running, froze, held its last value, or went dark. Whatever happened was a default, and the next step turns it into a decision.
9. **Make the failure behaviour a decision** by giving the controlled instance a defined response to missing control: it continues autonomously, falls to a safe state, or holds. Implement that response with a timeout, using the maximum-duration idiom from Lesson 15.
10. **Repeat the measurements over wireless** and compare them with the wired figures, since this comparison decides whether your production can use a wireless link at all.
11. **Add remote access** through a virtual private network if the piece will live somewhere you are not, and confirm that you can reach both machines from outside the venue.
12. **Document the topology** so that a collaborator can draw it: which machine does what, which addresses cross the network, what the failure behaviour is, and what the piece needs from the venue's network.

## What to synchronise, and what to leave alone

The choice of what to share across the network determines whether a distributed piece survives a run or fails during one, so each candidate deserves an argument before it crosses the link.

**Share cues by default**, because a handful of discrete messages at structural moments is dependable, easy to verify, and easy to fire by hand if the automation fails. This is the starting point for most productions. Moreover, it suffices far more often than people expect.

**Share values sparingly**, rate-limited, and only where continuity across machines matters. A position that must match on both machines is a real requirement, whereas a level that could be set locally is a requirement only in appearance.

**Share transport only when the piece demands it**, since two machines with a shared clock are two machines that can disagree about it. In contrast, when each machine runs its own timeline and is nudged by cues, the piece tolerates more and degrades more gracefully than it would under a shared transport.

**Do not share content unless the piece requires it**, because streaming video between machines costs bandwidth and adds latency, as Lesson 25 showed. Local playback with a shared cue is usually indistinguishable to the audience and considerably more dependable.

The test to apply to each candidate is a single question: if this message were lost, would the audience notice? A message that survives that question needs sharing, while the remaining candidates can be handled locally without loss.

## Failure is the design

The distinguishing property of a distributed piece is not that it uses two machines; it is that it acquires a new class of failure, and that class is a design surface to be worked through in advance.

**A single lost message should not break the piece.** Prefer state to events where you can, so that a repeated message corrects the situation instead of compounding it. In other words, "set level to 0.7" recovers from a loss, whereas "increase level by 0.1" does not.

**A late message needs a definition of late.** Decide what late means for your piece and what happens then, because a cue arriving two seconds late in a slow installation is harmless, while in a musical passage it is worse than one that does not arrive.

**A silent partner must be survivable**, which is the behaviour you implemented in step 9 of the walkthrough. Every machine should be able to continue, degrade, or move to a safe state on its own.

**A machine that restarts has lost its place in the piece.** After a power cut, machine B comes back without knowing where the piece is, so either it can be told, which means the controller must periodically restate the state instead of only announcing changes, or it starts from a known point.

Designing all four takes about an hour, and that hour is the difference between a distributed piece that survives a run and one that acquires a reputation.

## Common mistakes

- **Synchronising timelines when cues would do** is the most common and most expensive design error in distributed work.
- **Using wireless for any performed work** without measuring it first, which the comparison in step 10 exists to settle.
- **Leaving the behaviour for a lost network undefined**, so that the default becomes whatever the software happens to do.
- **Sending unlimited continuous values across a network**, which floods the link and starves the messages that mattered.
- **Testing only on one machine**, because two instances on one computer are a useful stage but are not the same as two machines.
- **Assuming latency is symmetric or constant**, when it should be measured in both directions.
- **Providing no remote access to a remote installation**, so that every fault requires travel.
- **Leaving the topology undocumented**, because a collaborator cannot maintain a distributed piece they cannot draw.

## Exercise

Build a two-machine piece in which machine A holds the structure and fires three cues to machine B, which plays its media locally. Measure the latency of a cue, then define and implement what B does if A goes silent for ten seconds, and test that behaviour by unplugging the network in the middle of the piece.

**Success criterion:** the cues arrive reliably, you can state the measured latency, and B's behaviour on losing A is a response you chose in advance instead of one you discovered. Then answer, in one sentence, which of your three cues would have been better handled locally.

## Going further

- [Remote control]({{ site.docs_baseurl }}/in-depth/remote.html) documents the WebSocket protocol used to drive a running instance.
- [Controlling *score* with OSCQuery]({{ site.docs_baseurl }}/faq/controlling-score-with-oscquery.html) and [the local device]({{ site.docs_baseurl }}/devices/local-device.html) cover the walkthrough's route.
- The paper *Networked Performances with Ossia Score*, by Celerier and Baltazar, describes where the project's distributed work is heading.
- [Livestreaming]({{ site.docs_baseurl }}/common-practices/10-livestreaming.html) and [Lesson 37]({{ site.baseurl }}/learn/37-recording-and-streaming.html) cover moving content across a network, whereas this lesson moved control.
