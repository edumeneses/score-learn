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

> **Before this lesson** finish [Lesson 35]({{ site.baseurl }}/learn/35-headless-and-embedded.html).
>
> **You will need** two machines on a network, or two instances of *score* on one machine using different ports.
>
> **You will build** a two-machine piece: one instance controlling another, with a defined answer for what happens when the network fails.

## Why this matters

Work outgrows one computer for ordinary reasons: a projector on one machine and a speaker array on another, a sensor in one room and the sound in the next, a piece in three rooms of a building. The *ossia* project has explored distributed authoring and performance for years, and the practical result available today is direct: **a score can control another score**, and *score* can be controlled by anything that speaks OSC or WebSockets.

The important lesson is about restraint. Most multi-machine pieces do not need synchronised timelines. They need a handful of cues to arrive reliably, and every piece that tries to keep two timelines in lockstep pays for it in fragility. Deciding what actually needs to be shared is the design work; the mechanisms are simple.

## Concepts

**The local device.** *score* exposes its own parameters as a device, which means one instance can be addressed exactly like a synthesiser or a light. Declare an OSC or OSCQuery device on machine A pointing at machine B's local device, and A can drive B with the same automations, states, and mappings you have used all course. No new concepts, which is the point.

**OSCQuery, for discovery.** Because the local device can describe itself, a controlling instance can import the whole tree rather than declaring it by hand, which is the Lesson 06 argument for descriptive protocols paying off.

**The WebSocket protocol**, from Lesson 33, is the other route: transport, triggers, interval speed and gain, values to addresses, and listening. It is the right choice when the controller is not *score*.

**What can be shared.** Four things, in increasing order of difficulty. **Cues**: one machine tells another to fire a trigger. **Values**: continuous parameters sent between machines. **Transport**: start, stop, and position. **Content**: audio or video streamed between machines, per Lesson 25's share protocols.

**Networks are part of the piece.** Latency, jitter, and packet loss are properties of your production, not accidents. Wired is predictable; wireless is not. For anything performed, use a cable, and where you cannot, design so that a late message is survivable.

**Reaching a machine that is not on your network.** For remote installations, a virtual private network such as ZeroTier puts machines on one logical network regardless of where they are, which is how a piece in another city gets maintained. The *ossia* community has published exactly this workflow.

## Walkthrough: two instances, one piece

{: .note }
> A figure for this lesson is pending: it needs two machines and their device trees, which requires interaction and hardware. See `checks/36-distributed-scores.md`.

1. **Start on one machine, two instances**, with different ports. Everything below works identically and nothing can be blamed on the network yet.
2. **Enable the local device** on the instance that will be controlled, and note its ports.
3. **On the controlling instance**, declare a device pointing at it. If OSCQuery is available, import the tree; if not, declare the few addresses you need.
4. **Fire a cue across.** Send a value that fires a trigger on the controlled instance, per Lesson 15. This is the smallest useful distributed piece, and for many productions it is the whole design.
5. **Send a continuous value** and watch it arrive. Then send it as fast as you can and watch what the network does to it. Add a rate limiter, per Lesson 13, on the sending side.
6. **Control transport.** Start and stop the controlled instance from the controller, and note the delay between the command and the response.
7. **Now separate the machines.** Move the second instance to another computer, wired, and repeat every step. Record the latency you measure rather than the latency you expect.
8. **Introduce a failure.** Unplug the network mid-piece. Write down what each machine did: kept running, froze, held its last value, went dark. Whatever it was, it was a default rather than a decision.
9. **Make it a decision.** Give the controlled instance a defined behaviour for missing control: continue autonomously, fall to a safe state, or hold. Implement it with a timeout, using the maximum-duration idiom from Lesson 15.
10. **Try wireless** and compare. This is the measurement that decides whether your production can use it.
11. **Add remote access** through a virtual private network if the piece will live somewhere you are not, and confirm you can reach both machines.
12. **Document the topology**: which machine does what, which addresses cross the network, what the failure behaviour is, and what the piece needs from the venue's network.

## What to synchronise, and what to leave alone

The decision that determines whether a distributed piece is robust or fragile.

**Share cues.** A handful of discrete messages at structural moments. Robust, easy to verify, and easy to fire by hand if the automation fails. This should be the default and it is sufficient far more often than people expect.

**Share values sparingly**, rate-limited, and only where continuity matters. A position that must match across machines is a real requirement; a level that could be set locally is not.

**Share transport only if you must.** Two machines with a shared clock are two machines that can disagree about it. When each machine can run its own timeline and be nudged by cues, that is more robust than a shared transport, and it degrades better.

**Do not share content unless the piece requires it.** Streaming video between machines costs bandwidth and adds latency, per Lesson 25. Local playback with a shared cue is usually indistinguishable to the audience and enormously more reliable.

The test to apply to each candidate: if this message were lost, would the audience notice? Everything that survives that question honestly needs sharing; everything else is a habit imported from single-machine thinking.

## Failure is the design

The distinguishing property of a distributed piece is not that it uses two machines; it is that it has a new class of failure, and that class is a design surface rather than an accident.

**A lost message.** Design so that any single message can be lost without the piece breaking: prefer state to events where you can, so that a repeated message corrects the situation rather than compounding it. "Set level to 0.7" recovers from a loss; "increase level by 0.1" does not.

**A late message.** Decide what late means and what happens then. A cue arriving two seconds late in a slow installation is fine; in a musical passage it is worse than not arriving.

**A silent partner.** The behaviour you implemented in step 9 of the walkthrough. Every machine should be able to continue, degrade, or safe itself alone.

**A machine that restarts.** After a power cut, machine B comes back not knowing where the piece is. Either it can be told, which means the controller must periodically restate the state rather than only announcing changes, or it starts at a known point.

Designing all four takes an hour and is the difference between a distributed piece that survives a run and one that gets a reputation.

## Common mistakes

- **Synchronising timelines when cues would do.** The most common and most expensive design error here.
- **Wireless for anything performed.** Measure it before you rely on it.
- **No defined behaviour for a lost network.** The default is whatever the software happens to do.
- **Unlimited continuous values across a network**, flooding it and starving the messages that mattered.
- **Testing only on one machine.** Two instances locally is a useful stage and not the same as two machines.
- **Assuming latency is symmetric or constant.** Measure both directions.
- **No remote access to a remote installation.** Then every fault becomes a journey.
- **An undocumented topology.** Nobody else can maintain a distributed piece they cannot draw.

## Exercise

Build a two-machine piece in which machine A holds the structure and fires three cues to machine B, which plays media locally. Measure the latency of a cue, then define and implement what B does if A goes silent for ten seconds. Test it by unplugging the network mid-piece.

**Success criterion:** the cues arrive reliably, you can state the measured latency, and B's behaviour on losing A is something you chose rather than something you discovered. Then answer, in one sentence, which of your three cues would have been better handled locally.

## Going further

- [Remote control]({{ site.docs_baseurl }}/in-depth/remote.html) for the WebSocket protocol.
- [Controlling *score* with OSCQuery]({{ site.docs_baseurl }}/faq/controlling-score-with-oscquery.html) and [the local device]({{ site.docs_baseurl }}/devices/local-device.html).
- Celerier and Baltazar, *Networked Performances with Ossia Score*, for where the project's distributed work is heading.
- [Livestreaming]({{ site.docs_baseurl }}/common-practices/10-livestreaming.html) and [Lesson 37]({{ site.baseurl }}/learn/37-recording-and-streaming.html) for moving content rather than control.
