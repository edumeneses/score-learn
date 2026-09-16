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

> **Before this lesson** finish [Lesson 32]({{ site.baseurl }}/learn/32-puredata.html), and have a score with several controls that deserve to be exposed to an operator.
>
> **You will need** a browser or a second device on the same network, and optionally some familiarity with QML.
>
> **You will build** an operator's surface that hides your score, in the simplest form that works for the piece.

## Why this matters

The person running a piece is often not the person who built it. A gallery invigilator, a stage manager, a technician at a venue, or you yourself, tired, two hours before a show, should not be navigating a timeline to do the job, because the timeline exposes every decision in the piece when the job requires only a few of them. An interface that shows six controls and no more is therefore what makes a piece deployable, whereas leaving the operator in the editor makes every performance depend on someone who understands the whole score.

*score* offers three routes to such an interface, and they are ordered by effort, so that the sensible approach is to take the first one that suffices. In contrast, reaching for a custom application when a control surface would do is the most common over-engineering in this part of the software, because the custom application costs weeks where the surface costs minutes, and the rest of this lesson argues for that order by building each route in turn.

## Concepts

**The first route is a control surface, which is a process that gathers controls into a panel.** You add it, place the controls that matter on it, and you have an operator's view inside *score* itself, with no code, which for most pieces is the whole answer.

**The second route is a QML interface that replaces *score*'s own control interface.** QML is Qt's declarative interface language, which is GPU (graphics processing unit) accelerated and designed for interfaces of this kind, and an interface written in it talks to the score through the same scripting API (application programming interface) as Lesson 29, plus a small set of types under a user-interface namespace. The important type is a port source, which reads and writes a score control located by name or label. However, reading a value gives you the current *execution* value, so the score has to be playing for a reading to be meaningful.

**The third route is the WebSocket protocol, which *score* exposes for remote control with JSON (JavaScript Object Notation) messages.** It covers transport, triggers, interval speed and gain, sending values to any address, and enabling listening so that value changes are pushed back to the client. An existing graphical remote is built on it, and the protocol is documented so that you can write your own client.

**The protocol differs from the other two routes in that it runs on another device.** A tablet at the mixing position, a phone in a pocket, or a laptop in the booth can control the piece without *score* installed. Moreover, the same property means that a piece can be controlled by something that is not an interface at all, such as a script or another application.

**Triggers are first-class in the protocol.** The score tells a client when a trigger becomes active and when it finishes, and the client can fire it, which is the shape of a cue light and a cue button, and therefore what a stage manager wants from a remote.

**The local device offers a further way in, over OSC (Open Sound Control), which Lesson 36 covers.** Controlling *score* through its own local device over OSC and OSCQuery is often simpler than the WebSocket protocol when the client already speaks OSC.

## Walkthrough: three routes, cheapest first

{: .note }
> A figure for this lesson is pending: it needs a control surface populated with controls, and a remote client connected, both of which require interaction; see `checks/33-custom-interfaces.md`.

1. **List what the operator needs, on paper and before you build.** The list is usually start, stop, one or two levels, and a way to fire the next cue, and a list with more than eight items should be questioned.
2. **Add a control surface and put those controls on it and no others.** Play the score and operate it from the surface alone, without touching the timeline.
3. **Test the list by running the piece twice from the surface.** Whatever you had to leave the surface to do is either missing from it or should not be the operator's job.
4. **Turn to the WebSocket route by enabling the remote interface and connecting a client.** If you have no client to hand, a browser console can open a WebSocket and send JSON.
5. **Send a transport message and watch the score start**, which is the smallest possible proof that the protocol works.
6. **Fire a trigger remotely by listening for the message that announces it becoming active**, then sending the message that fires it, at which point you have built the core of a cue system.
7. **Send a value to an address in the protocol's typed form**, and confirm that it arrives in the device explorer.
8. **Enable listening on an address and watch values pushed back to your client**, which is what lets a remote show state as well as send commands.
9. **Consider stopping here, because for most pieces a control surface plus a small remote is enough**, whereas a custom application is a project in its own right.
10. **If you need the QML route, start from the documented user-interface types**, bind one port source to one control, and confirm that you can read and write it while the score plays; then build outward from that working pair.
11. **Write the operator's page against whichever interface you ended with**, and have somebody else run the piece from it while you stay silent.

## Designing for the person on the night

The principles that follow come from productions, and each one reduces the number of ways an operator can go wrong on the night.

**Put fewer controls on the surface than you think you need.** Every control is a decision the operator can get wrong, so a value that should never change during the show does not belong on the surface.

**Show state as well as controls.** An operator needs to know what the piece is doing, which scene is running and whether a trigger is waiting, and the protocol pushes that information. In contrast, an interface that only sends commands leaves the operator guessing.

**Make the dangerous action hard to take by accident.** A blackout button and a next-cue button should not be adjacent and should not look alike, because the layout of the surface is what separates a recoverable mistake from a disaster in front of an audience.

**Label in the operator's language, whereas your structure uses yours.** Where the score says `Scenario.3`, the surface should say "second movement", because the mapping from your structure to their vocabulary is your job, and it is most of what makes an interface usable by someone who has not read your score.

## Who is the interface for?

An interface serves one of three audiences, the operator, the author in rehearsal, or the public, and an interface designed for the wrong one can be worse than none because it presents the wrong controls with confidence.

**The operator on the night** needs six controls, clear state, and no way to break the piece, and this is the audience this lesson optimises for, since the control surface is usually sufficient for them.

**You, in rehearsal,** need fast access to whatever is being adjusted today. However, that is not a custom interface at all; it is the timeline plus a start marker, and building a surface for it wastes time you should spend rehearsing.

**The audience**, in an installation where the interface *is* the work, touches a tablet or a panel on a wall, which is a different design problem and is where the QML route earns its cost, because the interface has to look like it belongs to the artwork and not to a piece of software.

In other words, the mistake to avoid is building the operator's surface with the audience's polish, or the audience's surface with the operator's density, so decide which of the three you are making before you choose the route.

## Common mistakes

- **Building a custom application when a control surface would do** costs weeks where the surface costs minutes.
- **Exposing every control** produces a surface with forty controls, which is a timeline with extra steps.
- **A remote that only sends** leaves the operator without state, and therefore flying blind.
- **Reading a control while the score is stopped** and concluding that the interface is broken misreads the mechanism, because execution values need execution.
- **Adjacent destructive and routine buttons** guarantee that someone will eventually hit the wrong one.
- **Internal names in an operator's interface** are opaque to the person using it, who has not read your score.
- **No fallback** is a risk of its own; if the remote's network fails, the operator must still be able to run the piece from the machine, so design that path on purpose.

## Exercise

Build an operator's surface for one of your milestone documents with at most six controls, then add remote control of the transport and of one trigger from a second device or a browser. Have someone else run the piece from your surface, from a cold start, using only your operator's page, while you watch without intervening.

**Success criterion:** they can start it, advance a cue, adjust one level, and stop it safely, without asking you a question and without touching the timeline. Every question they did ask becomes either a control on the surface or a line on the page, so that the next run needs fewer of them.

## Going further

- [Custom UIs]({{ site.docs_baseurl }}/in-depth/custom-ui.html) for the QML route and its user-interface types.
- [Remote control]({{ site.docs_baseurl }}/in-depth/remote.html), the complete WebSocket protocol, which should be read in full before writing a client.
- [The control surface process]({{ site.docs_baseurl }}/processes/controlsurface.html), which is the reference page for the first and cheapest route.
- [Controlling *score* with OSCQuery]({{ site.docs_baseurl }}/faq/controlling-score-with-oscquery.html), which describes the OSC route and which [Lesson 36]({{ site.baseurl }}/learn/36-distributed-scores.html) develops at length.
