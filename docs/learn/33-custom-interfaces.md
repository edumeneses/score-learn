---
layout: default
title: "Lesson 33: Custom interfaces"
description: "Build an operator's panel: control surfaces, a QML interface over the scripting API, and the WebSocket remote protocol."
parent: Lessons
nav_order: 39
unit: "33"
permalink: /learn/33-custom-interfaces.html
score_version: "3.8.2"
reading_time: "14 min"
practice_time: "30 min"
score_file: none
---

# Lesson 33: Custom interfaces

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 32]({{ site.baseurl }}/learn/32-puredata.html), and have a score with several controls worth exposing.
>
> **You will need** a browser or a second device on the same network, and optionally familiarity with QML.
>
> **You will build** an operator's surface that hides your score, in the simplest form that works.

## Why this matters

The person running a piece is often not the person who built it. A gallery invigilator, a stage manager, a technician at a venue, or you, tired, two hours before a show: none of them should be navigating a timeline to do their job. An interface that shows six controls and nothing else is not a convenience, it is what makes a piece deployable.

*score* offers three routes to this, and the useful insight is that they are ordered by effort and you should almost always take the first one that suffices. Reaching for a custom application when a control surface would do is the most common over-engineering in this part of the software.

## Concepts

**Route one: a control surface.** A process that gathers controls into a panel. Add it, put the controls that matter on it, and you have an operator's view inside *score* itself, with no code. For most pieces this is the whole answer.

**Route two: a QML interface.** *score*'s own control interface can be **replaced** by one you write in QML, Qt's declarative interface language, which is GPU-accelerated and designed for exactly this. Your interface talks to the score through the same scripting API as Lesson 29, plus a small set of types under a user-interface namespace. The important one is a port source, which reads and writes a score control located by name or label. Note one behaviour: reading a value gives you the current *execution* value, so the score has to be playing for a reading to mean anything.

**Route three: the WebSocket protocol.** *score* exposes a remote-control protocol over WebSockets, with JSON messages. It covers transport, triggers, interval speed and gain, sending values to any address, and enabling listening so that value changes are pushed back to the client. There is an existing graphical remote built on it, and the protocol is documented so you can write your own.

**What the protocol gives you that the others do not.** It runs on another device. A tablet at the mixing position, a phone in a pocket, a laptop in the booth: none of them needs *score* installed. It also means a piece can be controlled by something that is not an interface at all, a script or another application.

**Triggers are first-class in the protocol.** The score tells a client when a trigger becomes active and when it finishes, and the client can fire it. That is precisely the shape of a cue light and a cue button, which is what a stage manager wants.

**The local device, for the OSC route.** Lesson 36 covers the other way to control *score* from outside, through its own local device over OSC and OSCQuery, which is often simpler than the WebSocket protocol when the client already speaks OSC.

## Walkthrough: three routes, cheapest first

{: .note }
> A figure for this lesson is pending: it needs a control surface populated with controls, and a remote client connected, both of which require interaction. See `checks/33-custom-interfaces.md`.

1. **List what the operator needs.** On paper, before building anything. Usually it is: start, stop, one or two levels, and a way to fire the next cue. If your list has more than eight items, question it.
2. **Add a control surface** and put exactly those controls on it. Play the score and operate it from the surface alone, without touching the timeline.
3. **Test the list by using it.** Run the piece twice from the surface. Anything you had to leave the surface to do is either missing from it or should not be the operator's job.
4. **Now the WebSocket route.** Enable the remote interface and connect a client. If you have no client to hand, a browser console can open a WebSocket and send JSON.
5. **Send a transport message** and watch the score start. This is the smallest possible proof that the protocol works.
6. **Fire a trigger remotely.** Listen for the message that announces a trigger becoming active, then send the message that fires it. You have just built the essential half of a cue system.
7. **Send a value to an address**, in the protocol's typed form, and confirm it arrives in the device explorer.
8. **Enable listening on an address** and watch values pushed back to your client, which is what lets a remote show state rather than only sending commands.
9. **Consider stopping here.** For most pieces, a control surface plus a small remote is enough, and a custom application is a project.
10. **If you need the QML route**, start from the documented user-interface types, bind one port source to one control, and confirm you can read and write it while the score plays. Then build outward.
11. **Write the operator's page** against whichever interface you ended with, and have somebody else run the piece from it while you say nothing.

## Designing for the person on the night

Four principles, all learned from productions rather than from software.

**Fewer controls than you think.** Every control on the surface is a decision the operator can get wrong. If a value should never change during the show, it does not belong on the surface.

**Show state, not only controls.** An operator needs to know what the piece is doing: which scene is running, whether a trigger is waiting. The protocol pushes exactly this, and an interface that only sends commands leaves the operator guessing.

**Make the dangerous thing hard.** A blackout button and a next-cue button should not be adjacent and should not look alike. This is not decoration; it is the difference between a mistake and a disaster.

**Label in the operator's language.** Not `Scenario.3` but "second movement". The mapping from your structure to their vocabulary is your job, and it is most of what makes an interface usable by someone who has not read your score.

## Who is the interface for?

Three audiences, and an interface designed for the wrong one is worse than none.

**The operator on the night**, who needs six controls, clear state, and no way to break the piece. This is the audience this lesson optimises for, and the control surface is usually sufficient.

**You, in rehearsal**, who needs fast access to whatever is being adjusted today. That is not a custom interface at all; it is the timeline plus a start marker, and building a surface for it wastes time you should spend rehearsing.

**The audience**, in an installation where the interface *is* the work: a tablet visitors touch, a panel on a wall. This is a different discipline, and it is where the QML route earns its cost, because the interface has to look like it belongs to the artwork rather than to a piece of software.

The mistake worth naming: building the operator's surface with the audience's polish, or the audience's surface with the operator's density. Decide which of the three you are making before you choose the route.

## Common mistakes

- **Building a custom application when a control surface would do.** Weeks against minutes.
- **Exposing everything.** A surface with forty controls is a timeline with extra steps.
- **A remote that only sends.** Without state, the operator is flying blind.
- **Reading a control while the score is stopped** and concluding the interface is broken. Execution values need execution.
- **Adjacent destructive and routine buttons.** Someone will hit the wrong one.
- **Internal names in an operator's interface.** They mean nothing to the person using it.
- **No fallback.** If the remote's network fails, the operator must still be able to run the piece from the machine. Design that path deliberately.

## Exercise

Build an operator's surface for one of your milestone documents with at most six controls, then add remote control of the transport and one trigger from a second device or a browser. Have someone else run the piece from your surface, from a cold start, using only your operator's page.

**Success criterion:** they can start it, advance a cue, adjust one level, and stop it safely, without asking you anything and without touching the timeline. Every question they did ask becomes either a control on the surface or a line on the page.

## Going further

- [Custom UIs]({{ site.docs_baseurl }}/in-depth/custom-ui.html) for the QML route and its user-interface types.
- [Remote control]({{ site.docs_baseurl }}/in-depth/remote.html), the complete WebSocket protocol, worth reading in full before writing a client.
- [The control surface process]({{ site.docs_baseurl }}/processes/controlsurface.html).
- [Controlling *score* with OSCQuery]({{ site.docs_baseurl }}/faq/controlling-score-with-oscquery.html), which [Lesson 36]({{ site.baseurl }}/learn/36-distributed-scores.html) develops.
