---
layout: default
title: "Lesson 35: Headless and embedded"
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

# Lesson 35: Headless and embedded

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 34]({{ site.baseurl }}/learn/34-rehearsal-to-show.html).
>
> **You will need** your Milestone P4 installation, and ideally a Raspberry Pi 4 or a spare machine.
>
> **You will build** a deployment: the same document running with no interface, started automatically, and recoverable after a power cut.

## Why this matters

An installation that needs a laptop, a screen, and a person to press play is not an installation, it is a demonstration that has to be attended. The work in this lesson is what turns Milestone P4 into something a museum can switch on for three months.

Embedded deployment also imposes a discipline worth having. A small machine with a modest processor and no window manager forces you to know what your piece actually costs, and to remove what it does not need. Pieces that survive a Raspberry Pi are usually better engineered than pieces that only ever ran on a workstation.

## Concepts

**Headless operation.** *score* can run a document without its editing interface, which is what you want on a machine with no screen and no operator. Combined with the remote control of Lesson 33 or the OSC control of Lesson 36, a headless instance is still fully controllable from elsewhere.

**Embedded targets.** ARM builds are provided, and a Raspberry Pi 4 is the recommended board: better processor and, importantly, a more capable graphics unit than the 3. Builds exist for both 32-bit and 64-bit systems, and they must match the operating system you installed, which is the first thing to check when a download will not run.

**Graphics on a Pi needs configuration.** The full kernel-mode-setting driver has to be enabled through the Pi's configuration utility, which is what makes the graphics stack behave. Confirming that the corresponding overlay line is present in the boot configuration is the check that saves an evening.

**Two launchers, two purposes.** One script runs *score* inside the desktop environment, which is what you want while setting the machine up. The other renders full screen directly, bypassing the desktop entirely, which is more efficient and needs no window system at all, and is the right choice for a deployed player. The direct route has no window decorations, so it is for playing rather than editing.

**A lighter desktop helps measurably.** Replacing the Pi's default desktop with a minimal window manager makes a real difference to dropouts, which is worth knowing before concluding that the board is too slow.

**Minimal systems need libraries.** An operating system installed without a graphical environment will be missing shared libraries *score* expects. The reference documentation lists them; installing the list is faster than diagnosing them one at a time.

**Resolution is configured, not detected.** Under direct rendering you specify the output and mode in a small configuration file, with the environment pointed at it. This is a venue-dependent value in the sense of Milestone P6, and it belongs in your notes.

## Walkthrough: from laptop to appliance

{: .note }
> A figure for this lesson is pending: it needs a deployed machine and console output, which requires hardware and interaction. See `checks/35-headless-and-embedded.md`.

1. **Start with a document that passes Milestone P4's eight-hour test.** Deployment does not fix a piece that drifts; it makes drift harder to notice.
2. **Reduce it deliberately.** Lower the resolution, remove the layers that were nice rather than necessary, and confirm it still reads. This is the reduced version from Lesson 34, and on embedded hardware it is often the only version.
3. **Get the right build.** Match 32-bit or 64-bit to the installed operating system.
4. **Enable the graphics driver** through the configuration utility and reboot. Confirm the boot configuration contains the expected overlay line.
5. **Install the missing libraries** if you started from a system with no desktop.
6. **Run it inside the desktop first**, with the interface, and confirm the document opens and plays. Debug here, where you can see things.
7. **Measure honestly.** Watch for dropouts and frame-rate loss with the real content. Whatever you find is the true budget for the piece.
8. **Switch to direct rendering** with the full-screen launcher, and configure the output and mode. The interface is gone; the piece plays.
9. **Make it start by itself.** Configure the system to launch *score* with your document at boot, so that a power cut is followed by a working installation rather than by a phone call.
10. **Test the power cut.** Pull the plug, plug it back in, and time how long until the piece is running again. That number belongs in your documentation, and if it is unacceptable, this is when to find out.
11. **Add remote access.** Enable the control route from Lesson 33 or Lesson 36 so you can check on the piece and restart it without visiting.
12. **Leave it running for a day** and check in remotely. The eight-hour test, on the machine that will actually do the job.

## What to remove before deploying

Deployment is mostly subtraction, and these are the usual candidates.

**Resolution.** The single biggest lever, per Lesson 25. A projector's native resolution is the ceiling worth targeting, not your monitor's.

**Render passes.** A chain of filters costs a pass each. Combining them into one shader is the optimisation that most reliably pays on a small graphics unit.

**Unused devices.** Every declared device is a connection attempted at startup. A device that is not present on the deployed machine costs time and produces log noise that hides real problems.

**Monitoring.** Signal displays and observation processes were for you, during authoring. They cost, and nobody is watching them.

**Plug-ins.** Anything hosted is a dependency and often unavailable for the target architecture. This is the argument for Faust from Lesson 31, and the point at which it becomes concrete rather than theoretical.

**Your own convenience.** The scratch material, the alternative version of scene two, the layer you left muted. They are in the file, and some of them still execute.

## Why small hardware improves a piece

The constraint is worth welcoming rather than resenting, for three reasons that hold up in practice.

**It forces you to know what things cost.** On a workstation, a chain of eight filters and a 4K canvas are free. On a small board they are not, and finding out which parts of your piece are expensive usually reveals that the expensive parts were not the important ones.

**It removes the accidental.** A deployed document contains only what it needs: no monitoring, no alternative versions, no muted layers. That subtraction is a form of editing, and pieces are usually better for it.

**It makes the piece cheap to install.** A work that runs on a hundred-dollar board can be installed in three places at once, lent to a festival, or left somewhere for a year. A work that needs a workstation is a work that travels only when you do.

There is a fourth reason, less practical and worth saying: a piece that runs on a small computer with no screen and no keyboard stops feeling like software and starts feeling like an object. For installation work in particular, that is often the right relationship to the audience.

## Common mistakes

- **A build that does not match the operating system's word size.** It simply will not run, and the error is unhelpful.
- **Skipping the graphics driver configuration**, then concluding the board cannot do video.
- **Deploying the full version** and discovering the ceiling at the venue.
- **No automatic start.** Every power cut becomes a visit.
- **Not testing the power cut.** It will happen, and its timing is not yours to choose.
- **No remote access.** Then diagnosis requires travel.
- **Leaving monitoring processes in a deployed document.** They cost, and they help nobody.
- **Assuming a plug-in exists for ARM.** Usually it does not.

## Exercise

Deploy one installation to a second machine, ideally a Pi, so that it starts at boot with no interface and can be reached remotely. Then run three tests: a power cut, an eight-hour run, and a remote restart. Record the recovery time and the frame rate.

**Success criterion:** the piece recovers from a power cut with no human action, runs for eight hours without degrading, and can be restarted remotely. If any of the three failed, the failure and its cause belong in the failure plan from Lesson 34 rather than in your memory.

## Going further

- [Hardware support]({{ site.docs_baseurl }}/in-depth/embedded.html), the reference for Pi configuration, launchers, library lists, and display modes.
- [Running without a graphical interface]({{ site.docs_baseurl }}/faq/nogui.html).
- [Command line options]({{ site.docs_baseurl }}/reference-manual/references/command-line.html) for automated startup.
- [Monitoring activity]({{ site.docs_baseurl }}/faq/monitor-activity.html), for checking a deployed instance.
