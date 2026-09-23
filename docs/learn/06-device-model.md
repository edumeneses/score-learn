---
layout: default
title: "Lesson 06: Devices and addresses: the device model"
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

# Lesson 06: Devices and addresses: the device model

{% include lesson_meta.html %}

> **Before this lesson** finish [Milestone P1]({{ site.baseurl }}/learn/p1-automated-cue.html). You have been writing to addresses for several lessons, and this lesson explains what sits on the other end of them.
>
> **You will need** `lesson-00.score` open, together with a list of the software and hardware that your own project involves.
>
> **You will build** a device map for your project, which records what talks to what, over which protocol, and what each side is able to say.

## Why this matters

The device model is where the usability study found the sharpest difficulty. Interviewees misconfigured devices because they misunderstood what the parameters meant, and they reported that the relationship between devices and scenarios did not match their expectations. The study recommended teaching this model explicitly and with examples, because it is a new idea for people who arrive from tools in which an output is only a track destination.

The model repays the effort because of what it buys. A score written against `lesson:/level` neither knows nor cares whether that address belongs to a Max patch, a lighting desk, or a Raspberry Pi across the room. In other words, the device can change while the score stays as written, and that indirection is why the same document can be authored on a laptop and performed on a rig.

## Concepts

### Devices as named connections

A device is a named connection to something outside the document. It carries a name, a protocol, and protocol settings such as host and port; `lesson` in `lesson-00.score`, for instance, is an OSC (Open Sound Control) device pointed at localhost. The name is yours to choose, and every address in the document begins with it.

### Address spaces and paths

An address space is a tree of parameters with a path to each. A device exposes its parameters hierarchically, and an address is a path through that tree, either short like `lesson:/level` or deeper like `synth:/voice/2/filter/cutoff`. The device explorer draws that tree, and Lesson 07 covers building one by hand when the device cannot describe itself.

### Parameter attributes

A parameter carries several attributes in addition to its value. It has a type, a range, sometimes a unit, and an access mode that says whether it can be read, written, or both. Those attributes are what let *score* convert, clamp, and check. Moreover, a device that declares them is considerably easier to work with than one that does not, which is why Lesson 08 is entirely about them.

### Declaration and connection

Devices are declared in the document, whereas connections are made at run time. The declaration is saved in the `.score` file, so opening a document with no equipment attached still works because the tree is there even though the connection is not live. This property is what makes offline authoring possible, and the walkthrough below asks you to hold the two halves of it apart.

### Descriptive, blind, and fixed-shape protocols

Protocols differ in what they can tell you about the other end. This distinction concerns description and has little to do with speed, and it is the one that matters when choosing a protocol:

- **Descriptive protocols** can be asked what they contain, so the tree arrives complete. **OSCQuery** is the important one, because connecting to a compliant application lets *score* populate the whole tree automatically, with types, ranges, and units; **Minuit** is the older ossia protocol in the same family.
- **Blind protocols** send and receive messages but cannot describe what they contain. Plain **OSC** is the archetype, since you must declare by hand what you believe is on the other side and no part of the software checks that declaration; **MIDI** (Musical Instrument Digital Interface) is similarly fixed in shape, with channels and controller numbers and no discoverable tree.
- **Fixed-shape protocols** have a structure that the software already knows, which spares you the declaration: **Art-Net** for lighting, with universes and channels; **audio**, with inputs and outputs; and **joystick** and **gamepad**, with known axes and buttons.

## The protocols available

The table below groups the protocols as the `Add device` dialog groups them, and it was read from *score* {{ page.score_version }} because the manual is a release or two behind:

| Group | Protocols |
|---|---|
| Network | OSCQuery, OSC, Minuit, CoAP, MQTT, LSL, Bitfocus |
| Lights | Art-Net, NeoPixel LEDs |
| Audio | Audio, covered in [Lesson 19]({{ site.baseurl }}/learn/19-audio-setup.html) |
| Hardware | MIDI Input, MIDI Output, MIDI Controller, Serial, Joystick, Wiimote, Evdev, Raw I/O, Bluetooth Low Energy |
| Video | Window, Camera input, NDI Input, NDI Output, Shmdata Input, Shmdata Output, Sh4lt Input, Sh4lt Output |
| Web | HTTP, WebSocket |

The list in the dialog scrolls beyond one screen, and it also carries two devices that are not equipment at all, **local** and **mapper**, which are discussed below. However, treat the table as a record of what one build offered, since several entries in it, LSL and NeoPixel LEDs among them, do not appear in the reference table at all.

Neither of those two devices corresponds to equipment, which is why they deserve a note now. The **local** device exposes *score*'s own parameters, which is how a score controls itself and how [Lesson 36]({{ site.baseurl }}/learn/36-distributed-scores.html) drives one machine from another. In contrast, the **mapper** device is a device whose parameters are computed from other parameters, which is one way to keep conversion logic out of the timeline; [Lesson 13]({{ site.baseurl }}/learn/13-mapping-and-scaling.html) compares it with the alternatives.

## Walkthrough: read a device before creating one

1. **Open the device explorer** with `Ctrl+Shift+D` and look at `lesson` in `lesson-00.score`, which is one device carrying three parameters.
2. **Expand it and select `level`**, so that an inspector appears at the bottom of the panel with that parameter's attributes: its type, its range, and its current value if the device reports one back.
3. **Change the value from the inspector**, which writes to the parameter directly from the explorer. This is how you test a connection without playing the score at all, and it is therefore the first thing to try when a cue seems not to arrive.
4. **Compare what the document knows with what is live on the network.** With no receiver running on the other end, the tree is still there because it is the declaration, and being able to hold those two ideas apart, declared and connected, is most of what this lesson teaches.
5. **Inspect the protocol settings** by right-clicking the device and choosing `Edit`. For this OSC device you will see a listening port and a destination host and port; change none of them, but note that they are properties of the device and that no address carries them.
6. **Look at how the score refers to the device** by clicking any automation and reading its address in the inspector, where no port, host, or protocol appears because the timeline knows the device only by its name.
7. **Draw your own map** on paper by listing every piece of software and hardware in your project and writing, for each, the protocol you would use and whether it can describe itself. That list is the input to Lesson 07, which builds the first device from it.

![The device explorer's own menu, with Add device and the per-device actions]({{ site.img }}/06/06-01-device-menu.png)

The figure shows the menu through which all of this happens, reached by right-clicking in the device explorer. `Add device`, which is also reached with `Ctrl+B`, appears in this menu. Additionally, the same menu carries `Edit`, `Refresh namespace`, `Disconnect`, and `Reconnect`, so that creating, editing, and reconnecting a device happen in one place instead of being spread across the interface.

## Naming addresses so they survive the project

Address names outlive the equipment they were written for, so they deserve a moment's thought at declaration time, which costs far less than a rewrite once the whole document refers to them.

**Naming by function keeps an address meaningful after the equipment changes.** `lights:/wash/level` still makes sense after the fixture is replaced, whereas `chauvet:/ch1` does not, and the same argument applies to the device name itself because it prefixes every address.

**Grouping under intermediate nodes keeps the tree navigable as it grows.** A tree with intermediate nodes remains readable at eighty parameters, whereas a flat list does not. When you have the choice, group by the thing in the room, so that the tree reads `stage/left/tilt` where a grouping by protocol would read `dmx/universe1/ch3`.

**One convention for compound values should hold across the whole project.** A position can be one three-component parameter or three separate ones, and both work. However, mixing them in one project means every piece of downstream logic has to handle both. [Lesson 08]({{ site.baseurl }}/learn/08-units-ranges-types.html) covers the syntax for addressing one member of a compound value, which is what makes the single-parameter choice practical.

**The reasoning behind the map belongs in a text file outside *score*.** The document holds the declaration, whereas the reasoning, which parameter means what, what range is safe, and what must not be sent during a performance, belongs in a text file beside the score. That file is the beginning of the technical rider that [Lesson 34]({{ site.baseurl }}/learn/34-rehearsal-to-show.html) assembles, and the moment to start it is now, while the project has three parameters and the list is still short.

## Common mistakes

- **Treating a device as an output lane** misreads what it is, because a device is a namespace: any part of the score may write to any address, and one device serves the whole document.
- **Choosing plain OSC when the target speaks OSCQuery** means hand-declaring a tree that the software could have imported complete with types and ranges.
- **Expecting values to appear without an echo** leads to false alarms, since many devices accept messages without reporting values back; an empty value column means the other end is not telling you, and it does not by itself mean that the message failed to arrive. [Lesson 07]({{ site.baseurl }}/learn/07-osc-devices.html) covers how to see what left *score*.
- **Renaming a device late** means rewriting every address in the document, which is why the naming advice above applies from the first declaration.
- **Assuming the connection is what is saved** confuses the two halves of the model, since the declaration is saved while the connection is made at run time.

## Exercise

Write the device map for a project you want to make, listing for each device the name you would use in addresses, the protocol, whether it is descriptive, blind, or fixed-shape, and one sentence on what breaks if that device is absent at show time. Writing the map now takes a few minutes, whereas the same thinking after the score is written means renaming addresses throughout the document.

**Success criterion:** every device has a name short enough to live at the front of an address, and you can say for each whether you will have to declare its parameters by hand. Bring the map to Lesson 07, which builds the first device for real.

## Going further

- [Working with devices]({{ site.docs_baseurl }}/quick-start/working-with-devices.html) is the reference version of this material.
- [The devices reference]({{ site.docs_baseurl }}/devices.html) gives one page per protocol with its settings.
- [Protocols]({{ site.docs_baseurl }}/reference-manual/references/protocols.html) is the reference manual's full list of supported protocols.
- [Monitoring activity]({{ site.docs_baseurl }}/faq/monitor-activity.html) describes the panels that Lesson 07 uses for debugging.
