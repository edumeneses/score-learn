---
layout: default
title: "Lesson 06: The device model"
description: "Why score separates devices from the timeline, what an address space is, and how the supported protocols differ in what they can tell you."
parent: Lessons
nav_order: 7
unit: "06"
permalink: /learn/06-device-model.html
score_version: "3.8.2"
reading_time: "13 min"
practice_time: "15 min"
score_file: 00-what-score-is/lesson-00.score
---

# Lesson 06: The device model

{% include lesson_meta.html %}

> **Before this lesson** finish [Milestone P1]({{ site.baseurl }}/learn/p1-automated-cue.html). You have been writing to addresses; this lesson explains what is on the other end.
>
> **You will need** `lesson-00.score` open, and a list of the software and hardware your own project involves.
>
> **You will build** a device map for your project: what talks to what, over which protocol, and what each side is able to say.

## Why this matters

The device model is where the usability study found the sharpest difficulty. Interviewees misconfigured devices because parameters were misunderstood, and reported that the relationship between devices and scenarios did not match their expectations. The study's own recommendation was to teach this explicitly, with examples, because it is genuinely a new idea for people arriving from tools where an output is just a track destination.

The idea is worth the effort because of what it buys: a score written against `lesson:/level` does not know or care whether that is a Max patch, a lighting desk, or a Raspberry Pi across the room. Change the device, keep the score. That indirection is why the same document can be authored on a laptop and performed on a rig.

## Concepts

**A device is a named connection.** It has a name, a protocol, and protocol settings such as host and port. `lesson` in `lesson-00.score` is an OSC device pointed at localhost. The name is yours to choose, and every address in the document begins with it.

**An address space is a tree.** A device exposes parameters organised hierarchically, and an address is a path through that tree: `lesson:/level`, or something deeper like `synth:/voice/2/filter/cutoff`. The device explorer draws that tree, and Lesson 07 covers building one by hand when the device cannot describe itself.

**A parameter has attributes, not just a value.** A type, a range, sometimes a unit, an access mode saying whether it can be read, written, or both. Those attributes are what let *score* convert, clamp, and check; a device that declares them is much easier to work with than one that does not. Lesson 08 is entirely about them.

**Devices are declared, not discovered, in the document.** The declaration is saved in the `.score` file. Opening a document with no equipment attached works: the tree is there, the connection is not live. This is the property that makes offline authoring possible.

**Protocols differ in what they can tell you.** This is the distinction that matters when choosing one, and it is not about speed:

- **Descriptive protocols** can be asked what they contain. **OSCQuery** is the important one: connect to a compliant application and *score* populates the whole tree, with types, ranges, and units, automatically. **Minuit** is the older ossia protocol in the same family.
- **Blind protocols** send and receive but cannot describe themselves. Plain **OSC** is the archetype: you must declare by hand what you believe is on the other side, and nothing checks you. **MIDI** is similarly fixed in shape: channels and controller numbers, no discoverable tree.
- **Fixed-shape protocols** have a structure the software already knows: **Art-Net** for lighting, with universes and channels; **audio**, with inputs and outputs; **joystick** and **gamepad**, with known axes and buttons.

## The protocols available

Grouped by what they are for, not by how they work:

| For | Protocols |
|---|---|
| Network and general purpose | OSCQuery, OSC, Minuit, CoAP, MQTT |
| Web | HTTP, WebSocket |
| Musical hardware and control | MIDI in, MIDI out, serial, joystick, Wiimote, GPS, Leap Motion, raw I/O, Bluetooth Low Energy |
| Lighting | Art-Net |
| Audio | the audio device, covered in [Lesson 19]({{ site.baseurl }}/learn/19-audio-setup.html) |
| Video sharing | window, camera, Spout, Syphon, shmdata, NDI |
| Inside *score* | local, mapper |

Two entries deserve a note now. The **local** device exposes *score*'s own parameters, which is how a score controls itself, and how [Lesson 36]({{ site.baseurl }}/learn/36-distributed-scores.html) drives one machine from another. The **mapper** device is a device whose parameters are computed from other parameters, which is one way to keep conversion logic out of the timeline; [Lesson 13]({{ site.baseurl }}/learn/13-mapping-and-scaling.html) compares it with the alternatives.

## Walkthrough: read a device before creating one

1. **Open the device explorer** with `Ctrl+Shift+D` and look at `lesson` in `lesson-00.score`. One device, three parameters.
2. **Expand it and select `level`.** An inspector appears at the bottom of the panel with that parameter's attributes: its type, its range, its current value if the device reports one back.
3. **Change the value from the inspector.** You can write to a parameter directly from the explorer. This is how you test a connection without playing the score at all, and it is the first thing to try when a cue seems not to arrive.
4. **Ask what the document knows against what is live.** With nothing running on the other end, the tree is still there. That is the declaration. Being able to hold those two ideas apart, declared and connected, is most of what this lesson teaches.
5. **Inspect the protocol settings.** Right-click the device and choose `Edit`. For this OSC device you will see a listening port and a destination host and port. Change nothing; note that these are properties of the device, not of any address.
6. **Look at how the score refers to it.** Click any automation and read its address in the inspector. Nothing in the timeline mentions ports, hosts, or protocols. That separation is the point.
7. **Draw your own map.** On paper, list every piece of software and hardware in your project. For each, write the protocol you would use and, crucially, whether it can describe itself. That list is the input to Lesson 07.

{: .note }
> A figure for this lesson is pending: it needs the protocol chooser and the device edit dialog photographed, which requires interaction rather than a document opened from the command line. See `checks/06-device-model.md`.

## Naming addresses so they survive the project

Address names outlive the equipment they were written for, so they are worth a moment's thought at declaration time rather than a rewrite later.

**Name by function, not by product.** `lights:/wash/level` still makes sense after the fixture is replaced; `chauvet:/ch1` does not. The same argument applies to the device name itself, which prefixes everything.

**Group.** A tree with intermediate nodes stays navigable at eighty parameters; a flat list does not. Group by the thing in the room, not by the protocol: `stage/left/tilt` rather than `dmx/universe1/ch3`, when you have the choice.

**Keep one convention for compound values.** A position can be one three-component parameter or three separate ones. Both work; mixing them in one project means every piece of downstream logic has to handle both. [Lesson 08]({{ site.baseurl }}/learn/08-units-ranges-types.html) covers the syntax for addressing one member of a compound value, which is what makes the single-parameter choice practical.

**Write the map down outside *score*.** The document holds the declaration, but the reasoning, which parameter means what, what range is safe, what must never be sent during a performance, belongs in a text file beside the score. This is the beginning of the technical rider that [Lesson 34]({{ site.baseurl }}/learn/34-rehearsal-to-show.html) assembles, and the moment to start it is now, while the project has three parameters rather than eighty.

## Common mistakes

- **Treating a device as an output lane.** It is a namespace. Any part of the score may write to any address, and one device serves the whole document.
- **Choosing plain OSC when the target speaks OSCQuery.** You then hand-declare a tree that the software could have imported complete with types and ranges.
- **Expecting values to appear without an echo.** Many devices accept messages without reporting values back. An empty value column means the other end is not telling you, not necessarily that nothing arrived. [Lesson 07]({{ site.baseurl }}/learn/07-osc-devices.html) covers how to see what actually left.
- **Renaming a device late.** Every address in the document begins with the device name. Choose names you can live with: short, lowercase, and about function rather than brand, so that replacing the equipment does not mean rewriting the score.
- **Assuming the connection is what is saved.** The declaration is saved; the connection is made at run time.

## Exercise

Write the device map for a project you actually want to make. For each device: a name you would use in addresses, the protocol, whether it is descriptive, blind, or fixed-shape, and one sentence on what breaks if that device is absent at show time.

**Success criterion:** every device has a name short enough to live at the front of an address, and you can say for each whether you will have to declare its parameters by hand. Bring the map to Lesson 07, which builds the first one for real.

## Going further

- [Working with devices]({{ site.docs_baseurl }}/quick-start/working-with-devices.html), the reference version of this material.
- [The devices reference]({{ site.docs_baseurl }}/devices.html), one page per protocol with its settings.
- [Protocols]({{ site.docs_baseurl }}/reference-manual/references/protocols.html), for the full list.
- [Monitoring activity]({{ site.docs_baseurl }}/faq/monitor-activity.html), which Lesson 07 uses for debugging.
