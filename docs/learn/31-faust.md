---
layout: default
title: "Lesson 31: Faust inside score"
description: "Write and compile a Faust audio processor in the score editor, expose its controls as ports, and use its libraries for spatialisation."
parent: Lessons
nav_order: 37
unit: "31"
permalink: /learn/31-faust.html
score_version: "3.8.2"
reading_time: "13 min"
practice_time: "25 min"
score_file: none
---

# Lesson 31: Faust inside score

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 30]({{ site.baseurl }}/learn/30-expressions-and-jit.html), and have Module G's audio working.
>
> **You will need** a sound source and headphones.
>
> **You will build** a Faust processor of your own, compiled in *score*, with its controls automated from the timeline.

## Why this matters

Faust is a language for audio signal processing, and its presence inside *score* changes what a document can contain. Instead of depending on a plug-in installed on the machine, a Faust processor is **text inside your score file**: it travels with the document, compiles for whatever machine opens it, and needs nothing installed. For work that has to be installed by other people, in other countries, on machines you will never see, that property is worth more than it sounds.

It is also fast. Faust compiles to code optimised for the processor it is running on, taking advantage of vector instruction sets, which is why the spatialisation libraries in this ecosystem are written in it rather than in hand-written C++.

## Concepts

**A Faust process is a script in your document.** Add the process, open its editor with the window button, write or paste code, press compile. The compiled result runs in the audio engine, and the code is saved in the `.score` file.

**Controls become ports.** A slider or parameter declared in the Faust code appears as a port on the process, and is therefore automatable, mappable, and drivable from a sensor, exactly like everything else in the course. This is the same header-to-ports idea as ISF shaders in Lesson 26.

**The compile loop is the same.** `Ctrl+Enter` or the compile button; invalid code is refused rather than applied, so a mistake cannot produce a burst of noise; errors appear in the pane below the editor.

**Polyphony comes from writing mono.** As Lesson 21 established, a processor with one input and one output, `process = _ : _;` in Faust terms, is replicated to match the channel count arriving. Send it eight channels and you get eight processed channels, and sending a list to one of its controls sets that control per channel. This is the mechanism that makes multichannel work practical, and it is one of the reasons Faust is the recommended route for audio.

**The standard library is large.** Faust ships with filters, oscillators, reverbs, dynamics, and spatialisation. Two entries matter for this course: `sp.spat`, a circular spatialiser by Laurent Pottier, which Lesson 22 mentioned, and the wider library of building blocks you can combine in a few lines.

**Installable libraries.** The package manager provides further collections, including abclib by Alain Bonardi and Paul Goutmann, which adds ambisonics up to high orders, decoders for various layouts, and geometric tools. Installing a package rather than writing the algorithm is usually the right choice.

## Walkthrough: from a one-liner to a spatialiser

![A Faust processor written in score's editor and compiled, chained after a sound file that is playing, with the two controls its code declares listed as ports on the process]({{ site.img }}/31/31-01-faust-editor.png)

Six lines of Faust, and every claim in this lesson is visible at once. The two `hslider` declarations became the `cutoff` and `gain` ports that the inspector lists on the right, and the same two appear on the process in the score. A moment earlier that process had sixteen ports, because it began as a library preset: ports are derived from the code and from nothing else, so recompiling replaced them.

{: .note }
> **There is no blank Faust process in the library.** `Plugins > Faust` holds presets rather than an empty processor, so the way to start is to add any preset and replace its code, which is what the figure did. Note that the process keeps the preset's label afterwards, `16_channel_volume` here, while its ports are entirely yours. That mismatch is worth recognising before you go hunting for a bug: the label says where the process came from, the ports say what it now is.

1. **Add a Faust process** in an interval that already receives audio, per Lesson 21. Take any preset from `Plugins > Faust`, since there is no empty one and you are about to replace its code.
2. **Write the smallest possible processor**, a pass-through: `process = _ : _;`. Compile. Sound goes through unchanged, and you have confirmed the plumbing.
3. **Make it do something.** Add a gain with a declared control, so the code multiplies the signal by a slider. Compile, and find the new port on the process.
4. **Automate that port** from the timeline. You are now automating a parameter of a processor you wrote, which is the moment the two halves of this course meet.
5. **Add a filter** from the standard library, with its cutoff as a declared control, and automate that too.
6. **Break it deliberately** and confirm the running audio is unaffected while the error appears in the pane.
7. **Test polyphony.** Feed the pass-through processor a multichannel source and confirm the channel count is preserved. Then send a list to the gain control and hear each channel take its own value.
8. **Load the spatialiser.** Bring in the `sp.spat` preset from the user library, cable a mono source into it, and connect its outputs. Its speaker count is a number in the code: change 8 to 4, compile, and the process now has four outputs.
9. **Compare with Lesson 22's approach.** The DBAP and matrix construction is object-based and adapts to any layout; `sp.spat` assumes a ring and is a few lines. Neither is better; they answer different questions.
10. **Install a package.** Use the package manager to add a Faust library, and instantiate one of its objects, so you have used code you did not write and did not install by hand.
11. **Save your processor.** Keep the code in the user library so the next project starts from it.

## Why a script can be better than a plug-in

A comparison worth making explicitly, because the instinct is usually to reach for a plug-in.

**It travels.** The code is in the document. There is no installation step, no version mismatch, and no licence server. For a piece that will be installed by a technician who has never met you, this is decisive.

**It is portable across architectures.** The same code compiles on the venue's machine, including the embedded ARM targets of [Lesson 35]({{ site.baseurl }}/learn/35-headless-and-embedded.html), where a compiled plug-in for another architecture is useless.

**It is readable and editable.** A collaborator can see what the processing does, and change it. A plug-in is a black box with knobs.

**It is exactly as big as you need.** A three-line saturator is three lines, where the equivalent plug-in brings an interface, presets, and a megabyte of code you are not using.

The honest counterweight: for a specific reverb, a mastering chain, or a spatialisation suite whose sound *is* the reason you chose it, host the plug-in. Faust is the right default for the small and specific, which is most of what a piece needs.

## What to write, and what to install

Faust's library situation is worth knowing before you write anything, because a great deal is already done.

**The standard library** covers filters, oscillators, delays, reverbs, dynamics, and the circular spatialiser. If your processor is a combination of standard building blocks, it is a few lines rather than an implementation.

**Installable collections** through the package manager add the specialised material: ambisonics of high order, decoders for specific layouts, geometric and spatial transformation tools. For anything spatial beyond amplitude panning, look here before writing.

**Your own code** is for the thing that is specific to your piece: a distortion with a particular character, a gate with unusual timing, a processor whose behaviour is part of the composition.

The failure mode worth avoiding is implementing an ambisonic decoder because it is interesting. It is interesting, and it is also solved, and the version in the library has been tested by people who do this for a living. Write the part that is yours.

One further practical note: keep each processor small. A Faust script that does one thing is easy to read, easy to reuse in the next project, and easy to combine with another in a chain. A single script that does five things is a private language, and the person who has to read it in a year is you.

## Common mistakes

- **Expecting stereo behaviour from a stereo processor.** If you want per-channel replication, write mono.
- **Not compiling.** As with every scripting route.
- **Declaring no controls**, then wondering why there is nothing to automate. Ports come from declared parameters.
- **Editing `sp.spat`'s speaker count and forgetting to recompile**, so the process still has the old number of outputs.
- **Writing an algorithm that a package already provides.** Check the package manager first; ambisonics in particular is solved.
- **Treating the code as disposable.** It is part of the document, so it deserves the same care as the rest: a comment saying what it does, and a copy in the library.

## Exercise

Write a Faust processor with at least two declared controls, one of which is automated from the timeline and one driven from your P3 bench. Confirm it replicates across channels by feeding it a multichannel source and sending a list to one control. Then replace it with an equivalent chain of built-in processes and compare: lines of code, number of objects, and how easy each would be for a collaborator to understand.

**Success criterion:** the processor works, both controls are driven from outside, and the channel replication is demonstrated. Your comparison should end with a stated preference and a reason, not with a tie.

## Going further

- [The Faust process]({{ site.docs_baseurl }}/processes/faust.html) and the [Faust documentation](https://faust.grame.fr).
- [Faust synthesis example]({{ site.docs_baseurl }}/examples/audio/faust-synthesis.html).
- [Polyphony]({{ site.docs_baseurl }}/in-depth/polyphony.html), short and directly relevant.
- [Spatial audio]({{ site.docs_baseurl }}/common-practices/14-spatial-audio.html) for `sp.spat`, abclib, and where each fits.
