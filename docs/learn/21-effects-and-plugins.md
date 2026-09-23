---
layout: default
title: "Lesson 21: Audio effects, plug-ins, and live input"
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

# Lesson 21: Audio effects, plug-ins, and live input

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 20]({{ site.baseurl }}/learn/20-sound-files.html), since the sound files it set up are the sources that this lesson processes.
>
> **You will need** a sound file, one plug-in you own or a free one, and optionally a microphone or line input.
>
> **You will build** an effect chain assembled in the nodal view, with one automated parameter and one live input.

## Why this matters

Effects are where the nodal view stops being an alternative and becomes the natural place to work, because a chain is a graph and drawing it as a graph shows the signal path as it runs. In contrast, the temporal view shows you the same objects while giving you no useful picture of the order in which the signal passes through them.

Furthermore, this lesson introduces two ideas whose consequences reach well beyond audio, which are plug-ins and polyphony. **Plug-ins** are the first dependency your document has that does not travel with it, which changes what a technical rider must say. **Polyphony** is the answer that *score* gives to multichannel processing: a mono processor is replicated to match the channel count arriving, so that you do not instantiate an effect per channel, and its controls can be addressed per channel with a list. That second behaviour is what makes the speaker arrays of Lesson 22 practical.

## Concepts

### Effect chains

A chain is made of cables. Drop an effect from the library, connect the source's audio output to its input, and then connect that effect's output to the next, since the graph you draw is the one that runs and no connection is implied for you.

### Hosted plug-in formats

Several plug-in formats are hosted. *score* hosts several external formats, VST (Virtual Studio Technology) among them, as well as the script-based processors covered in Module J. A hosted plug-in appears as a process with ports for its parameters, which means that its parameters are automatable in the same way as those of any built-in process.

### Polyphony

Polyphony replicates a mono processor per channel. When a processor is mono, with one input and one output, *score* instantiates as many copies as there are channels arriving, so that three channels in give three processed channels out. Moreover, its controls accept a **list** in place of a single value, mapping one element to each channel. Today this works with Faust processors and selected others, which you should confirm before you plan a design around it.

## Walkthrough: a chain, an automation, an input

![A sound file feeding a built-in flanger and then a hosted JSFX limiter, drawn as connected nodes, with the process library filtered to the plug-in and the plug-in's ports listed in the inspector]({{ site.img }}/21/21-01-effect-chain.png)

The chain in the figure is two effects deep, since the sound file's output reaches a built-in `Flanger` and the flanger's output reaches `MGA_JSLimiterST`, a hosted JSFX plug-in. The inspector on the right is where the lesson's central claim becomes visible, because the plug-in's `Threshold`, `Release`, `Link Stereo`, and `Ceiling` are listed under `Inputs`, as ports, in the same way that a built-in process's parameters are; automating them is no different from automating any other port.

{: .note }
> **You do not have to own a plug-in to do this lesson.** The package manager in *score* offers `jsfx_pack`, a large collection of JSFX effects under free licences, and the figure above uses one of them. Installed plug-ins appear in the process library under `Plugins`, which in 3.8.2 holds `Airwindows`, `CLAP`, `Faust`, `JSFX`, `LV2`, `PureData`, `VST`, and `VST 3`, and filtering the library by name, as in the figure, is faster than opening that tree, because `JSFX` alone has dozens of folders.

1. **Start from a sound file** in an interval, playing, so that you have a source to hear each change against.
2. **Switch to the nodal view**, and work there for the rest of the lesson.
3. **Add one effect** and cable the file's output into it, then play; you hear the processed signal only, because the cable removed propagation, as Lesson 19 established.
4. **Chain a second effect** using the fast route, which means selecting the first effect and double-clicking the next process in the library, and confirm that the cable appeared.

   {: .note }
   > **Fast chaining connects by first port.** Per Lesson 11's interactions, the double-click connects the new process after the selected one by its first port, and since audio effects have audio in and out as their first ports by convention, the chain builds without touching the score between steps. Moreover, each new process is left selected, so that the next double-click continues the chain.

5. **Reorder the chain on purpose** by moving an effect earlier and listening, because order is not a detail; a filter before a distortion is a different instrument from the reverse.
6. **Automate a parameter** by right-clicking one of the effect's control ports, creating an automation, and drawing a sweep; you are now automating the inside of your score, whereas Lesson 10 automated the outside world through the same mechanism.
7. **Host a plug-in** by adding one from the library, cabling it into the chain, and opening its interface, then automate one of its parameters the same way.
8. **Write down the dependency** as one line in your project notes, giving the plug-in's name, its format, and where it came from.

   {: .warning }
   > **A plug-in is an installation requirement.** It lives on the machine, whereas the document only records that it is needed, so a score that needs three plug-ins is a score with a three-line prerequisite. Saying so in writing is the difference between a piece that installs in ten minutes and one that does not install at all.

9. **Add a live input** by declaring the audio device in the device explorer and cabling one of its input addresses into a fresh effect, then speak or play into it, with headphones on to avoid feedback; from that point the live signal is a source like any other, and every technique in this lesson applies to it unchanged.
10. **Try polyphony** by feeding a multichannel source into a mono Faust processor and confirming that you get the same number of channels out, then send a list to one of its controls and hear each channel take its own value.
11. **Group and treat** by putting two sources in a sub-scenario and routing the scenario's output into your chain, and confirm that one chain now treats both, per Lesson 19.

## Latency, and why chains get quiet

Chaining has two practical effects that surprise people, a loss of level and an accumulation of latency, and both have straightforward causes.

**Level loss comes from multiplied gain stages.** Every gain stage in a chain multiplies, so three effects each at a conservative output level produce something much quieter than the source, and the instinct is to raise the last one, which raises its noise too. Set the levels going forward through the chain, and reserve the gain sub-port on the outlet for the final adjustment.

**Latency accumulates through the chain.** Some processors introduce delay, and the delays add, which for a stereo master is invisible. However, in two situations it is not: when a processed signal is mixed with an unprocessed copy of itself, a few milliseconds of difference produces comb filtering in place of the sound you wanted; and in an interactive piece, a gesture that must feel immediate arrives late. If a chain feels late, count the processors before doubting the buffer size from Lesson 19.

Both problems are easier to avoid than to diagnose, and both are reasons to keep chains as short as the material allows.

## Built in, or hosted?

For most effects you have a choice between a built-in *score* process and an external plug-in, and the trade between them decides how the piece installs.

**A built-in process travels with the document.** It is in the document's dependency list already, its parameters are ports, and it works on every platform *score* runs on, including the embedded targets of Lesson 35. For a piece that will be installed by somebody else, this matters more than the last five percent of sound quality.

**A plug-in brings its own quality and its own interface.** For a specific reverb, a mastering chain, or a spatialisation suite, hosting is the right answer and the reason hosting exists.

**A Faust script is the third option**, and often the best one for something small and specific, because it travels inside the document, it compiles for the machine it runs on, and Lesson 31 shows how little code an effect needs.

In other words, host plug-ins where their quality is the point, and use built-in processes or scripts everywhere else, because a document with two carefully chosen plug-ins installs, whereas a document with fifteen does not.

## Common mistakes

- **Building a chain in the temporal view** produces a chain that runs while giving you no picture of the signal path, so switch to the nodal view.
- **Forgetting that the cable removed the dry signal** leads to adding gain to compensate for a sound that is not missing but only unrouted.
- **Automating a plug-in parameter by moving its own interface** and expecting the movement to be saved fails, because automation lives on ports, in the score.
- **Not recording plug-in dependencies** is the most common cause of a document that will not run on the venue's machine.
- **Assuming polyphony everywhere** overreaches, since it is implemented for Faust and selected processors; check before designing around it.
- **Monitoring a live input on speakers** produces feedback, which is loud and which is not the software's fault.
- **Building a chain so long that no stage can be reasoned about** defeats the graph; if you cannot say what each stage contributes, remove one and listen.

## Exercise

Build a chain of three effects on one sound file, in the nodal view, with one parameter automated across twenty seconds. Then reorder the chain and keep whichever order you prefer, writing one sentence about why, and finally add a live input through a separate copy of the same chain and confirm that both paths work.

**Success criterion:** the chain is legible as a graph, the automation moves an effect parameter and not a device parameter, and your project notes name every plug-in the document now requires. If the output is noticeably quieter than the source, fix the levels going forward through the chain.

## Going further

- [Audio techniques]({{ site.docs_baseurl }}/common-practices/4-audio.html) for chaining, grouping, and live input.
- [Audio plug-ins]({{ site.docs_baseurl }}/processes/audio-plugins.html) for the hosted formats.
- [Polyphony]({{ site.docs_baseurl }}/in-depth/polyphony.html), which is short and should be read in full before Lesson 22.
- [The modular workflow]({{ site.docs_baseurl }}/in-depth/modular.html) for the fast chaining interactions.

{% include lesson_files.html %}
