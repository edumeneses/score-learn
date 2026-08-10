---
layout: default
title: "Lesson 21: Effects and plug-ins"
description: "Build effect chains in the nodal view, host VST and other plug-in formats, take a live input, and understand per-channel polyphony."
parent: Lessons
nav_order: 25
unit: "21"
permalink: /learn/21-effects-and-plugins.html
score_version: "3.8.2"
reading_time: "14 min"
practice_time: "30 min"
score_file: none
---

# Lesson 21: Effects and plug-ins

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 20]({{ site.baseurl }}/learn/20-sound-files.html).
>
> **You will need** a sound file, one plug-in you own or a free one, and optionally a microphone or line input.
>
> **You will build** an effect chain assembled in the nodal view, with one automated parameter and one live input.

## Why this matters

Effects are where the nodal view stops being an alternative and becomes the natural place to work. A chain is a graph; drawing it as a graph is not a preference, it is the shape of the thing. The temporal view will show you the same objects and give you no useful picture of the signal path.

This lesson also introduces two ideas with consequences well beyond audio. **Plug-ins** are the first dependency your document has that does not travel with it, which changes what a technical rider must say. And **polyphony** is *score*'s answer to multichannel processing: rather than making you instantiate an effect per channel, a mono processor is replicated to match the channel count arriving, and its controls can be addressed per channel with a list. That behaviour is what makes Lesson 22's speaker arrays practical.

## Concepts

**A chain is cables.** Drop an effect from the library, connect the source's audio output to its input, then that effect's output to the next. Nothing is implicit; the graph is what runs.

**Fast chaining.** Per Lesson 11's interactions: with a process selected, double-clicking a new process in the library connects it after the selected one by first port. Since audio effects have audio in and out as their first ports by convention, this builds a chain without touching the score between steps, and each new process is left selected so the next double-click continues the chain.

**Plug-in formats.** *score* hosts several external formats, VST among them, as well as script-based processors covered in Module J. A hosted plug-in appears as a process with ports for its parameters, which means its parameters are automatable exactly like anything else.

**A plug-in is an installation requirement.** It lives on the machine, not in the document. A score that needs three plug-ins is a score with a three-line prerequisite, and saying so in writing is the difference between a piece that installs in ten minutes and one that does not install at all.

**Live input.** Declare the audio device in the device explorer, then use its input addresses as the input of an effect. A live signal is then a source like any other, and everything in this lesson applies to it unchanged.

**Polyphony.** When a processor is mono, one input and one output, *score* instantiates as many copies as there are channels arriving: send three channels in, get three processed channels out. Better still, its controls accept a **list** instead of a single value, mapping one element to each channel. Today this works with Faust processors and selected others, which is worth knowing before you plan a design around it.

## Walkthrough: a chain, an automation, an input

{: .note }
> A figure for this lesson is pending: it needs an effect chain drawn in the nodal view with a hosted plug-in visible, which requires interaction and a plug-in this course cannot ship. See `checks/21-effects-and-plugins.md`.

1. **Start from a sound file** in an interval, playing.
2. **Switch to the nodal view.** From here on, work there.
3. **Add one effect** and cable the file's output into it. Play: you hear the processed signal only, because the cable removed propagation, as Lesson 19 established.
4. **Chain a second effect** using the fast route: select the first effect, then double-click the next process in the library. Confirm the cable appeared.
5. **Reorder deliberately.** Move an effect earlier in the chain and listen. Order is not a detail; a filter before a distortion is a different instrument from the reverse.
6. **Automate a parameter.** Right-click one of the effect's control ports and create an automation, then draw a sweep. You are now automating the inside of your score rather than the outside world, which is the same mechanism Lesson 10 introduced.
7. **Host a plug-in.** Add one from the library, cable it into the chain, and open its interface. Automate one of its parameters the same way.
8. **Write down the dependency.** One line in your project notes: the plug-in's name, its format, and where it came from.
9. **Add a live input.** Declare the audio device, then cable one of its inputs into a fresh effect. Speak or play into it, with headphones on to avoid feedback.
10. **Try polyphony.** Feed a multichannel source into a mono Faust processor and confirm you get the same number of channels out. Then send a list to one of its controls and hear each channel take its own value.
11. **Group and treat.** Put two sources in a sub-scenario, route the scenario's output into your chain, and confirm one chain now treats both, per Lesson 19.

## Latency, and why chains get quiet

Two practical effects of chaining that surprise people, both with straightforward causes.

**Level loss.** Every gain stage in a chain multiplies. Three effects each at a conservative output level produce something much quieter than the source, and the instinct is to raise the last one, which raises its noise too. Set levels going forward through the chain rather than fixing them at the end, and use the gain sub-port on the outlet for the final adjustment.

**Latency accumulation.** Some processors introduce delay, and the delays add. For a stereo master this is invisible. In two situations it is not: when a processed signal is mixed with an unprocessed copy of itself, where a few milliseconds of difference produces comb filtering rather than the sound you wanted; and in an interactive piece where a gesture must feel immediate. If a chain feels late, count the processors before doubting the buffer size from Lesson 19.

Both problems are easier to avoid than to diagnose, and both are reasons to keep chains as short as the material allows.

## Built in, or hosted?

For most effects you have a choice between a *score* process and an external plug-in, and the trade is worth naming.

**A built-in process travels.** It is in the document's dependency list already, its parameters are ports, and it works on every platform *score* runs on, including the embedded targets of Lesson 35. For a piece that will be installed by somebody else, this matters more than the last five percent of sound quality.

**A plug-in brings its own quality and its own interface.** For a specific reverb, a mastering chain, or a spatialisation suite, hosting is the right answer and the reason hosting exists.

**A Faust script is the third option**, and often the best one for something small and specific: it travels inside the document, it compiles for the machine it runs on, and Lesson 31 shows how little code an effect needs.

The habit worth forming: host plug-ins where their quality is the point, and use built-in processes or scripts everywhere else. A document with two carefully chosen plug-ins installs; a document with fifteen does not.

## Common mistakes

- **Building a chain in the temporal view.** It works and it tells you nothing. Switch.
- **Forgetting that the cable removed the dry signal**, then adding gain to compensate for a sound that is not missing but simply unrouted.
- **Automating a plug-in parameter by moving its own interface** and expecting the movement to be saved. Automation lives on ports, in the score.
- **Not recording plug-in dependencies.** The most common cause of a document that will not run on the venue's machine.
- **Assuming polyphony everywhere.** It is implemented for Faust and selected processors; check before designing around it.
- **Monitoring a live input on speakers.** Feedback is loud and it is not the software's fault.
- **A chain so long that nothing can be reasoned about.** If you cannot say what each stage contributes, remove one and listen.

## Exercise

Build a chain of three effects on one sound file, in the nodal view, with one parameter automated across twenty seconds. Then reorder the chain and keep whichever order you prefer, writing one sentence about why. Finally, add a live input through a separate copy of the same chain and confirm both paths work.

**Success criterion:** the chain is legible as a graph, the automation moves an effect parameter rather than a device parameter, and your project notes name every plug-in the document now requires. If the output is noticeably quieter than the source, fix it going forward through the chain rather than at the end.

## Going further

- [Audio techniques]({{ site.docs_baseurl }}/common-practices/4-audio.html) for chaining, grouping, and live input.
- [Audio plug-ins]({{ site.docs_baseurl }}/processes/audio-plugins.html) for the hosted formats.
- [Polyphony]({{ site.docs_baseurl }}/in-depth/polyphony.html), which is short and worth reading in full before Lesson 22.
- [The modular workflow]({{ site.docs_baseurl }}/in-depth/modular.html) for the fast chaining interactions.
