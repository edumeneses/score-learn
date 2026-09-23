---
layout: default
title: "Lesson 31: Faust DSP inside score"
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

# Lesson 31: Faust DSP inside score

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 30]({{ site.baseurl }}/learn/30-expressions-and-jit.html), and have Module G's audio working, because every step here assumes that a signal already reaches the interval.
>
> **You will need** a sound source and headphones, because each processor you compile is confirmed by listening to it.
>
> **You will build** a Faust processor of your own, compiled in *score*, with its controls automated from the timeline.

## Why this matters

Faust is a language for audio signal processing, and its presence inside *score* changes what a document can contain. A Faust processor is **text inside your score file**, which means that it travels with the document, compiles for whatever machine opens it, and needs no installation, whereas a plug-in depends on what is installed on the machine that runs it. For work that has to be installed by other people, in other countries, on machines you will never see, that property is worth more than it sounds.

Furthermore, Faust is fast, because it compiles to code optimised for the processor it is running on and takes advantage of vector instruction sets. That speed is why the spatialisation libraries in this ecosystem are written in Faust and not in hand-written C++, and it is one reason this course recommends Faust for audio.

## Concepts

### A script in the document

A Faust process is a script stored in your document. You add the process, open its editor with the window button, write or paste code, and press compile, after which the compiled result runs in the audio engine and the code is saved in the `.score` file.

### Declared controls become ports

Controls declared in the code become ports on the process. A slider or parameter declared in Faust appears as a port, and it is therefore automatable, mappable, and drivable from a sensor like every other port in the course, which is the same header-to-ports idea as the ISF (Interactive Shader Format) shaders of Lesson 26.

### Polyphony from a mono processor

Polyphony comes from writing a mono processor. As Lesson 21 established, a processor with one input and one output, `process = _ : _;` in Faust terms, is replicated to match the channel count arriving, so that eight channels in give eight processed channels out, and a list sent to one of its controls sets that control per channel. This mechanism is what makes multichannel work practical, and it is one of the reasons Faust is the recommended route for audio in this course.

### The Faust standard library

The standard library covers most of what a piece needs. Faust ships with filters, oscillators, reverbs, dynamics, and spatialisation, and two entries matter for this course: `sp.spat`, a circular spatialiser by Laurent Pottier which Lesson 22 mentioned, and the wider library of components that you can combine in a few lines.

## Walkthrough: from a one-liner to a spatialiser

![A Faust processor written in score's editor and compiled, chained after a sound file that is playing, with the two controls its code declares listed as ports on the process]({{ site.img }}/31/31-01-faust-editor.png)

The figure holds six lines of Faust, and every claim in this lesson is visible in it at once. The two `hslider` declarations became the `cutoff` and `gain` ports that the inspector lists on the right, and the same two appear on the process in the score. A moment earlier that process had sixteen ports, because it began as a library preset. In other words, ports are derived from the code alone, so recompiling replaced them.

{: .note }
> **There is no blank Faust process in the library.** `Plugins > Faust` holds presets and no empty processor, so the way to start is to add any preset and replace its code, which is what the figure did. The process keeps the preset's label afterwards, `16_channel_volume` here, while its ports are entirely yours, and recognising that mismatch saves a hunt for a bug that does not exist, since the label says where the process came from whereas the ports say what it now is.

1. **Add a Faust process in an interval that already receives audio**, per Lesson 21. Take any preset from `Plugins > Faust`, since there is no empty one and you are about to replace its code.
2. **Write the smallest possible processor, a pass-through**, `process = _ : _;`, and compile it. Sound goes through unchanged, which confirms the plumbing before any processing is involved.
3. **Make it do something by adding a gain with a declared control**, so that the code multiplies the signal by a slider. Compile, and find the new port on the process.
4. **Automate that port from the timeline**, so that you are automating a parameter of a processor you wrote, which is the moment the two halves of this course meet.
5. **Add a filter from the standard library, with its cutoff as a declared control**, and automate that control too.
6. **Break the code and confirm that the running audio is unaffected** while the error appears in the pane.

   {: .note }
   > **The compile loop is the one every scripting route shares.** `Ctrl+Enter` or the compile button applies the code; invalid code is refused, so that a mistake cannot produce a burst of noise; and errors appear in the pane below the editor.

7. **Test polyphony by feeding the pass-through processor a multichannel source**, and confirm that the channel count is preserved. Then send a list to the gain control and hear each channel take its own value.
8. **Load the spatialiser by bringing in the `sp.spat` preset from the user library**, cable a mono source into it, and connect its outputs. Its speaker count is a number in the code, so changing 8 to 4 and compiling gives the process four outputs.
9. **Compare it with Lesson 22's approach**, where the DBAP (distance-based amplitude panning) and matrix construction is object-based and adapts to any layout, whereas `sp.spat` assumes a ring and is a few lines. Neither is better, because they answer different questions.
10. **Install a package through the package manager and instantiate one of its objects**, so that you have used code you did not write and did not install by hand.
11. **Save your processor in the user library**, so that the next project starts from it.

## Why a script can be better than a plug-in

This comparison deserves to be made explicitly, because the instinct is usually to reach for a plug-in, whereas four properties of a script argue against it.

**A script travels with the document.** Because the code is in the file, there is no installation step, no version mismatch, and no licence server, which is decisive for a piece that will be installed by a technician who has not met you.

**A script is portable across architectures.** The same code compiles on the venue's machine, including the embedded ARM targets of [Lesson 35]({{ site.baseurl }}/learn/35-headless-and-embedded.html), where a compiled plug-in built for another architecture is useless.

**A script is readable and editable by a collaborator**, who can see what the processing does and change it, whereas a plug-in is a black box with knobs.

**A script is as big as you need and no bigger.** A three-line saturator is three lines, whereas the equivalent plug-in brings an interface, presets, and a megabyte of code you are not using.

Nevertheless, for a specific reverb, a mastering chain, or a spatialisation suite whose sound *is* the reason you chose it, hosting the plug-in remains the right choice, and Faust is the default for the small and specific processing that most of a piece consists of.

## What to write, and what to install

Faust's library situation should be understood before you write a line of code, because a great deal is already done.

**The standard library** covers filters, oscillators, delays, reverbs, dynamics, and the circular spatialiser, so that a processor which combines standard components is a few lines and not an implementation.

**Installable collections** through the package manager add the specialised material, among them abclib by Alain Bonardi and Paul Goutmann, which provides ambisonics up to high orders, decoders for various layouts, and geometric tools. For spatial work beyond amplitude panning, look here before writing, because installing a package is usually the right choice whenever it already contains the algorithm you were about to write.

**Your own code** is for what is specific to your piece, such as a distortion with a particular character, a gate with unusual timing, or a processor whose behaviour is part of the composition.

The failure to avoid is implementing an ambisonic decoder because the problem is interesting. However, the problem is also solved, the version in the library has been tested by people who do this for a living, and the part that deserves your time is the part that is yours.

A further practical recommendation is to keep each processor small, because a Faust script that does one thing is easy to read, easy to reuse in the next project, and easy to combine with another in a chain. In contrast, a single script that does five things is a private language, and the person who has to read it in a year is you.

## Common mistakes

- **Writing a stereo processor and expecting per-channel behaviour** defeats replication; if you want per-channel replication, write mono.
- **Not compiling** leaves the old code running, as with every scripting route.
- **Declaring no controls** and then finding no port to automate are the same fact, because ports come from declared parameters.
- **Editing `sp.spat`'s speaker count and forgetting to recompile** leaves the process with the old number of outputs.
- **Writing an algorithm that a package already provides** wastes time; check the package manager first, since ambisonics in particular is solved.
- **Treating the code as disposable** ignores that it is part of the document, so it deserves the same care as the rest: a comment saying what it does, and a copy in the library.

## Exercise

Write a Faust processor with at least two declared controls, one of which is automated from the timeline while the other is driven from your P3 bench, and confirm that it replicates across channels by feeding it a multichannel source and sending a list to one control. Additionally, replace it with an equivalent chain of built-in processes and compare the two on lines of code, number of objects, and how easy each would be for a collaborator to understand.

**Success criterion:** the processor works, both controls are driven from outside, and the channel replication is demonstrated. Your comparison should end with a stated preference and a reason, since a tie would mean that the comparison was not made.

## Going further

- [The Faust process]({{ site.docs_baseurl }}/processes/faust.html) and the [Faust documentation](https://faust.grame.fr), which together cover the process and the language.
- [Faust synthesis example]({{ site.docs_baseurl }}/examples/audio/faust-synthesis.html), a worked example to read alongside this lesson.
- [Polyphony]({{ site.docs_baseurl }}/in-depth/polyphony.html), which is short and directly relevant to the replication step.
- [Spatial audio]({{ site.docs_baseurl }}/common-practices/14-spatial-audio.html), which describes `sp.spat` and abclib and where each fits.

{% include lesson_files.html %}
