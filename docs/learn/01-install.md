---
layout: default
title: "Lesson 01: Install, first run, and finding your way to help"
description: "Install ossia score on Linux, macOS, or Windows, confirm it runs, and learn the four places the software answers questions."
parent: Lessons
nav_order: 1
unit: "01"
permalink: /learn/01-install.html
score_version: "3.8.2"
reading_time: "12 min"
practice_time: "15 min"
score_file: none
---

# Lesson 01: Install, first run, and finding your way to help

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 00]({{ site.baseurl }}/learn/00-what-score-is.html), which explains what you are installing and why.
>
> **You will need** a 64-bit computer running Linux, macOS, or Windows, and about 400 MB of disk space.
>
> **You will build** a working installation of *score* {{ page.score_version }}, and a habit: knowing where to look before asking.

## Why this matters

This course pins one version, *score* **{{ page.score_version }}**, and every figure in it was captured from that build. Interface details move between releases, so if you install a newer one, expect small differences in wording and icon placement; the concepts hold. Pinning is not fussiness. It is the difference between a course that can be corrected and a course that slowly stops matching what the reader sees.

The second half of this lesson is about help, and it comes this early on purpose. The usability study conducted at the Société des Arts Technologiques rated the documentation as middling, and separately found that closing the start screen loses easy access to the bundled examples, which are among the most useful things shipped with the software. Both findings have the same practical consequence: readers who do not know where the answers live conclude there are none.

## Concepts

**Release channels.** *score* publishes tagged releases and development builds. The tagged release is what a download page gives you and what this course targets. Development builds carry features that are not documented yet; useful later, distracting now.

**Portable against installed.** On Linux the AppImage is a single executable file: nothing is installed, nothing is registered, and you can keep several versions side by side, which is exactly what you want while following a pinned course. Flatpak and distribution packages integrate better with the desktop and update with the system. On macOS and Windows the usual installers apply.

**The audio backend.** *score* does not own the sound card; it talks to whatever audio system your machine runs. On Linux that means JACK or PipeWire for reliable low latency, and ALSA otherwise. Getting this right matters from Lesson 19 onward, not today, but a machine that produces no sound in Module G usually has a backend problem rather than a score problem.

## Installing

Minimum requirements are modest: a 64-bit operating system, a GPU supporting OpenGL 3.2, Vulkan, Direct3D 11, or Metal, and 512 MB of RAM. Video work and dense scenarios want considerably more than the minimum, and Module I assumes a GPU from the last decade.

**Linux, AppImage, recommended for this course.** Download the AppImage for your architecture from <https://ossia.io/score/download.html> or from the [GitHub releases page](https://github.com/ossia/score/releases). Make it executable and run it:

```bash
chmod +x ossia.score-3.8.2-linux-x86_64.AppImage
./ossia.score-3.8.2-linux-x86_64.AppImage
```

Keeping it in a directory such as `~/Applications` lets several pinned versions coexist. AArch64 builds cover Raspberry Pi and Asahi Linux; Lesson 35 returns to them.

**Linux, packaged.** Flatpak, `flatpak install flathub io.ossia.score` then `flatpak run io.ossia.score`; the Arch User Repository, `yay -S ossia-score`; nixpkgs, `nix-shell -p ossia-score`. FreeBSD has a port.

**macOS.** Download the `.dmg` matching your machine, Apple Silicon or Intel, and drag *score* into Applications. Intel builds need macOS 10.15 or later. Homebrew works too: `brew install --cask ossia-score`. Some VST plug-ins and virtual cameras need permissions granted in System Settings; that surfaces in Module G, not now.

**Windows.** Run the installer from the download page, or `winget install ossia.score`, or under MSYS2 `pacman -S mingw-w64-x86_64-ossia-score`. One extra step matters later: the OSCQuery protocol, which Lesson 06 covers, needs [Bonjour Print Services](https://support.apple.com/kb/DL999) for network discovery.

## Walkthrough: first run

1. **Launch it.** Startup takes a few seconds the first time while plug-ins are scanned.
2. **Confirm the three areas.** A correct installation shows the `Device explorer` on the left, the scenario editor in the centre, and the object inspector on the right. If any is missing, you have almost certainly collapsed a panel rather than broken an install; Lesson 03 covers panel management.
3. **Open something that already works.** The start screen offers bundled examples. Open one, look at it, and close it without saving. You are not expected to understand it; you are confirming that playback, audio, and graphics initialise on your machine.
4. **Note where the examples live.** Before dismissing the start screen, notice how you got to the examples. This is the single most common early annoyance: the resources are easy to reach at launch and easy to lose afterwards. If you cannot find them again later, reopen the start screen from the `File` menu rather than hunting the filesystem.
5. **Check the version.** It appears in the window title, and on the command line as `--version`. It should read `3.8.2` if you are following the pinned course.
6. **Leave a scratch project.** Save an empty document somewhere you will find it, for example `~/score/scratch.score`. Lesson 05 explains what that file contains and what travels with it.

{: .note }
> A figure for this lesson is pending: it needs the start screen and the `File` menu photographed, and those require interaction rather than a document opened from the command line. See `checks/01-install.md`.

## The four places help lives

1. **Contextual help, `F1`.** Select an object in the scenario or a process in the library and press `F1`. This opens the reference page for that specific object. It is the fastest route from "what is this thing" to an answer, and it is why the reference manual is worth having offline.
2. **The reference manual**, at [ossia.io/score-docs]({{ site.docs_baseurl }}). Its shape is worth learning now: a [quick start]({{ site.docs_baseurl }}/quick-start) that is short and linear, [common practices]({{ site.docs_baseurl }}/common-practices/common-practices.html) organised as recipes, [in-depth]({{ site.docs_baseurl }}/in-depth/in-depth.html) for the concepts underneath, and a per-object reference for processes and devices. This course is a path through that material, not a replacement for it.
3. **The bundled examples.** Reading a working document is often faster than reading prose about it, which is the premise of Lesson 00.
4. **The community.** The issue tracker and the forum, when the first three have failed. Lesson 38 covers how to ask in a way that gets an answer, and how to turn a gap you found into a documentation fix.

## If it will not start, or will not make a sound

Four causes account for nearly every failed first run, and they are quick to separate.

**Nothing appears at all.** On Linux this is usually the AppImage's runtime: older systems need FUSE available, and the fallback is to extract the image with `--appimage-extract` and run the binary inside. On macOS it is usually the quarantine flag on a downloaded application, cleared by opening it once through the right-click menu rather than by double-clicking.

**It starts and the window is blank or garbled.** That is graphics: the machine does not have a working OpenGL 3.2 or better driver, which is common on virtual machines and on remote desktops. *score* draws its timeline through the GPU, so this is not a cosmetic problem.

**It starts, plays, and stays silent.** That is the audio backend, and it is worth confirming that nothing else has taken exclusive control of the sound card. On Linux, prefer JACK or PipeWire; on macOS and Windows the default backend is normally correct. Nothing in the course before Module G needs audio at all, so a silent installation is not a reason to stop here.

**It starts but a plug-in scan hangs.** A single misbehaving VST can stall startup. The remedy is to move the offending plug-in out of the scan path; the console panel, which [Lesson 03]({{ site.baseurl }}/learn/03-interface-and-transport.html) introduces, names the last plug-in attempted.

## Common mistakes

- **Installing a nightly build to follow a pinned course.** Small interface differences then read as your own errors. If you want the newest features, install both and keep them separate.
- **Expecting sound before configuring audio.** Silence in early lessons is usually the audio backend, not the score. Nothing before Module G needs sound at all.
- **Dismissing the start screen and concluding the examples are gone.** They are reachable from the `File` menu.
- **Skipping `F1`.** Readers who never discover contextual help spend the rest of the course guessing what a control does.
- **On Windows, skipping Bonjour and then finding OSCQuery discovery silently empty.** The protocol works; the discovery mechanism it relies on is missing.

## Exercise

Install *score* {{ page.score_version }}, open one bundled example, and play it. Then answer, in writing, three questions about that example without reading anything except the software itself: what does its longest interval contain, what is the first thing it sends to a device, and what stops it. Use `F1` on at least two objects you cannot name.

**Success criterion:** you can name the two objects you pressed `F1` on and say which reference page appeared. If `F1` produced nothing for an object, note which one; that is a real documentation gap and Lesson 38 shows how to report it.

## Going further

- [Installation]({{ site.docs_baseurl }}/quick-start/installation.html), the reference version of this page, including FreeBSD and embedded targets.
- [Troubleshooting]({{ site.docs_baseurl }}/troubleshooting.html), for a build that will not start or will not make sound.
- [The package manager]({{ site.docs_baseurl }}/in-depth/package-manager.html), which installs addons and the user library; Lesson 34 uses it.
- [Preferences]({{ site.docs_baseurl }}/reference-manual/references/preferences.html). Do not change anything yet, but note that one option, `auto-sequence`, is switched off by default and Lesson 09 turns it on deliberately.
