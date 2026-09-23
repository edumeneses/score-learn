---
layout: default
title: "Lesson 35: Headless playback and the Raspberry Pi"
description: "Run a score with no interface, deploy it to a Raspberry Pi, choose between X11 and direct rendering, and make it survive a power cut."
parent: Lessons
nav_order: 41
unit: "35"
permalink: /learn/35-headless-and-embedded.html
score_version: "3.8.2"
reading_time: "14 min"
practice_time: "40 min"
score_file: none
---

# Lesson 35: Headless playback and the Raspberry Pi

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 34]({{ site.baseurl }}/learn/34-rehearsal-to-show.html), because the failure plan and the reduced version it produced are the inputs to deployment.
>
> **You will need** your Milestone P4 installation, and ideally a Raspberry Pi 4 or a spare machine to deploy it to.
>
> **You will build** a deployment, which is the same document running with no interface, started automatically, and recoverable after a power cut.

## Why this matters

An installation that needs a laptop, a screen, and a person to press play is a demonstration that has to be attended, whereas an installation in the proper sense can be switched on and left. The work in this lesson is what turns Milestone P4 into something a museum can switch on for three months, because the document itself does not change; the machine, the launcher, and the recovery behaviour around it do.

Moreover, embedded deployment improves the piece, because a small machine with a modest processor and no window manager forces you to know what your piece costs and to remove what it does not need. Consequently, pieces that survive a Raspberry Pi tend to be better engineered than pieces that only ever ran on a workstation, and a section near the end of this lesson returns to why that constraint is useful.

## Concepts

### Headless operation

Headless operation runs a document without its editing interface, on a machine with no screen and no operator. Combined with the remote control of Lesson 33 or the OSC (Open Sound Control) control of Lesson 36, a headless instance remains fully controllable from elsewhere, which is the property the rest of this lesson relies on.

### ARM builds and the Raspberry Pi

Embedded targets are served by ARM builds, and a Raspberry Pi 4 is the recommended board. It has a better processor than the 3 and, more importantly, a more capable graphics unit; builds exist for both 32-bit and 64-bit systems, and a build runs only on an operating system of the same word size, which step 3 checks.

### Two launchers

The two launchers serve different purposes, one for setting up and one for playing. The first script runs *score* inside the desktop environment, which is what you want while setting the machine up, whereas the second renders full screen directly, bypassing the desktop entirely, which is more efficient and needs no window system at all. The direct route has no window decorations, so it is for playing and not for editing, and it is the right choice for a deployed player.

## Walkthrough: from laptop to appliance

{: .note }
> A figure for this lesson is pending: it needs a deployed machine and console output, which requires hardware and interaction; see `checks/35-headless-and-embedded.md`.

1. **Start with a document that passes Milestone P4's eight-hour test**, because deployment does not fix a piece that drifts; it only makes the drift harder to notice.
2. **Reduce it on purpose, by lowering the resolution and removing the layers that were pleasant but unnecessary**, and confirm that it still reads. In other words, this is the reduced version from Lesson 34, and on embedded hardware it is often the only version.
3. **Get the right build by matching 32-bit or 64-bit to the installed operating system**, since a mismatch is the first thing to check when a download will not run.
4. **Enable the full kernel-mode-setting graphics driver through the Pi's configuration utility and reboot**, since graphics on a Pi needs this configuration before the stack behaves as it should, then confirm that the boot configuration contains the expected overlay line, because a missing line is the usual reason a board seems unable to do video.
5. **Install the missing libraries if you started from a system with no desktop**, because an operating system installed without a graphical environment lacks shared libraries that a desktop install would have brought; the reference documentation lists them, and installing the list is faster than diagnosing them one by one.
6. **Run it inside the desktop first, with the interface**, and confirm that the document opens and plays, because this is the place to debug, where you can see what is happening.
7. **Measure with the real content**, watching for dropouts and frame-rate loss, since whatever you find is the true budget for the piece.

   {: .note }
   > **Replacing the Pi's default desktop with a minimal window manager helps measurably.** The change makes a real difference to dropouts, which you should know before concluding that the board is too slow.

8. **Switch to direct rendering with the full-screen launcher**, and configure the output and mode. Once the interface is gone, the piece plays as it did in the editor, and that continuity is what justifies the extra configuration that headless deployment requires.

   {: .warning }
   > **Under direct rendering the resolution is a configured value, since the mode is not detected.** You specify the output and mode in a small configuration file, with the environment pointed at it, which makes it a venue-dependent value in the sense of Milestone P6, and it belongs in your notes.

9. **Make it start by itself by configuring the system to launch *score* with your document at boot**, so that a power cut is followed by a working installation and not by a phone call.
10. **Test the power cut by pulling the plug, plugging it back in, and timing how long the piece takes to run again.** That number belongs in your documentation, and if it is unacceptable, this is the moment to find out.
11. **Add remote access by enabling the control route from Lesson 33 or Lesson 36**, so that you can check on the piece and restart it without visiting.
12. **Leave it running for a day and check in remotely**, which repeats the eight-hour test on the machine that will do the job, where the result is the one that counts.

## What to remove before deploying

Deployment is mostly subtraction, and the items below are the usual candidates for removal, together with what each one costs a deployed machine.

**Resolution is the single biggest lever, as Lesson 25 established.** A projector's native resolution is the ceiling to target. In contrast, your monitor's resolution has no bearing on the venue.

**Render passes cost one pass per filter in a chain**, so combining them into one shader is the optimisation that most reliably pays on a small graphics unit.

**Every unused device still costs a connection attempt at startup**, and a device that is not present on the deployed machine costs time and produces log noise that hides real problems.

**Monitoring processes were for you during authoring, and they still cost on the deployed machine.** Signal displays and observation processes keep costing after authoring ends, and no one is watching them once the piece is deployed.

**Plug-ins are dependencies, and they are often unavailable for the target architecture.** This is the argument for Faust from Lesson 31, and it is the point at which that argument becomes concrete.

**Your own convenience material is still in the file and still executes.** The scratch material, the alternative version of scene two, and the layer you left muted travel with the document, and some of them still execute.

## Why small hardware improves a piece

The constraint is one to welcome, because it improves the piece in three practical ways and in one way that is less practical.

**The constraint forces you to know what each part of the piece costs.** On a workstation a chain of eight filters and a 4K canvas are free. In contrast, on a small board they are not, and finding out which parts of your piece are expensive usually reveals that the expensive parts were not the important ones.

**The constraint removes the accidental material that a workstation lets you keep.** A deployed document contains only what it needs, with no monitoring, no alternative versions, and no muted layers, and that subtraction is a form of editing, which pieces are usually better for.

**The constraint makes the piece cheap to install and therefore easy to lend.** A work that runs on a hundred-dollar board can be installed in three places at once, lent to a festival, or left somewhere for a year. Conversely, a work that needs a workstation travels only when you do.

Additionally, a fourth reason is less practical: a piece that runs on a small computer with no screen and no keyboard stops feeling like software and starts feeling like an object, which for installation work in particular is often the right relationship to the audience.

## Common mistakes

- **A build that does not match the operating system's word size** will not run, and the error is unhelpful.
- **Skipping the graphics driver configuration** leads to the conclusion that the board cannot do video, when the driver was the problem.
- **Deploying the full version** means discovering the ceiling at the venue.
- **No automatic start** turns every power cut into a visit.
- **Not testing the power cut** leaves its timing to chance, and it will happen at a time you did not choose and when you are not there.
- **No remote access** means that every diagnosis requires travel to the venue.
- **Leaving monitoring processes in a deployed document** costs performance and helps no one.
- **Assuming a plug-in exists for ARM** is usually wrong, which is the reason Lesson 31 argued for Faust.

## Exercise

Deploy one installation to a second machine, ideally a Pi, so that it starts at boot with no interface and can be reached remotely, then run three tests: a power cut, an eight-hour run, and a remote restart. Additionally, record the recovery time and the frame rate, because both belong in the documentation from Lesson 34.

**Success criterion:** the piece recovers from a power cut with no human action, runs for eight hours without degrading, and can be restarted remotely. If any of the three tests failed, the failure and its cause belong in the failure plan from Lesson 34, where the next person to install the piece will find them.

## Going further

- [Hardware support]({{ site.docs_baseurl }}/in-depth/embedded.html), the reference for Pi configuration, launchers, library lists, and display modes.
- [Running without a graphical interface]({{ site.docs_baseurl }}/faq/nogui.html), which is the FAQ entry for headless operation.
- [Command line options]({{ site.docs_baseurl }}/reference-manual/references/command-line.html), the reference for the flags that an automated startup passes to *score*.
- [Monitoring activity]({{ site.docs_baseurl }}/faq/monitor-activity.html), which describes how to check whether a deployed instance is doing what it should.

{% include lesson_files.html %}
