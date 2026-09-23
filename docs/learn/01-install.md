---
layout: default
title: "Lesson 01: Installing score, first run, and getting help"
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

# Lesson 01: Installing *score*, first run, and getting help

{% include lesson_meta.html %}

> **Before this lesson** finish [Lesson 00]({{ site.baseurl }}/learn/00-what-score-is.html), which explains what you are installing and why.
>
> **You will need** a 64-bit computer running Linux, macOS, or Windows, and about 400 MB of disk space.
>
> **You will build** a working installation of *score* {{ page.score_version }}, and a map of where the software answers questions.

## Why this matters

This course pins one version, *score* **{{ page.score_version }}**, and every figure in it was captured from that build. Interface details move between releases, so a newer build shows small differences in wording and icon placement, although the concepts hold; pinning is the difference between a course that can be corrected and one that slowly stops matching what the reader sees.

The second half of this lesson is about help, and it comes this early because the usability study conducted at the Société des Arts Technologiques rated the documentation as middling and separately found that closing the start screen loses easy access to the bundled examples, among the most useful things it ships. Both findings have the same practical consequence: readers who do not know where the answers live conclude there are none.

## Concepts

### Releases and development builds

The software publishes tagged releases and development builds. The tagged release is what a download page gives you and what this course targets. In contrast, development builds carry features that are not documented yet, which makes them useful later and distracting now.

### Portable and installed builds

A portable build and an installed build serve different needs. On Linux the AppImage is a single executable file that installs and registers no component, so several versions can sit side by side, as a pinned course requires. Conversely, Flatpak and distribution packages integrate better with the desktop and update with the system, while on macOS and Windows the usual installers apply.

### The audio backend

The audio backend sits between *score* and the sound card. The software talks to whatever audio system your machine runs, which on Linux means JACK or PipeWire for reliable low latency, and ALSA otherwise. Getting this right matters from Lesson 19 onward, although a machine that produces no sound in Module G usually has a backend problem rather than a score problem.

## Installing

The minimum requirements for the software are modest: a 64-bit operating system, a GPU (graphics processing unit) supporting OpenGL 3.2, Vulkan, Direct3D 11, or Metal, and 512 MB of RAM. However, video work and dense scenarios want considerably more than the minimum, and Module I assumes a GPU from the last decade.

**On Linux, this course recommends the AppImage build.** Download the AppImage for your architecture from <https://ossia.io/score/download.html> or from the [GitHub releases page](https://github.com/ossia/score/releases), then make it executable and run it:

```bash
chmod +x ossia.score-3.8.2-linux-x86_64.AppImage
./ossia.score-3.8.2-linux-x86_64.AppImage
```

Keeping it in a directory such as `~/Applications` lets several pinned versions coexist, while AArch64 builds cover Raspberry Pi and Asahi Linux, which Lesson 35 returns to.

**Packaged builds exist for several Linux distributions.** Flatpak uses `flatpak install flathub io.ossia.score` then `flatpak run io.ossia.score`; the Arch User Repository uses `yay -S ossia-score`; nixpkgs uses `nix-shell -p ossia-score`; and FreeBSD has a port.

**On macOS, download the `.dmg` matching your machine**, Apple Silicon or Intel, and drag *score* into Applications; Intel builds need macOS 10.15 or later, and Homebrew offers `brew install --cask ossia-score`. Some VST (Virtual Studio Technology) plug-ins and virtual cameras need permissions granted in System Settings, which surfaces in Module G.

**On Windows, run the installer from the download page**, or `winget install ossia.score`, or under MSYS2 `pacman -S mingw-w64-x86_64-ossia-score`. An extra step matters later, because the OSCQuery protocol, which Lesson 06 covers, needs [Bonjour Print Services](https://support.apple.com/kb/DL999) for network discovery.

## Walkthrough: first run

![The ossia score start screen, with recent files, Examples, and Tutorials]({{ site.img }}/01/01-01-start-screen.png)

1. **Launch the application**, whose startup takes a few seconds the first time while plug-ins are scanned, and you arrive at the start screen in the figure.
2. **Confirm the three areas of the window.** A correct installation shows the `Device explorer` on the left, the scenario editor in the centre, and the object inspector on the right; if any is missing, you have almost certainly collapsed a panel rather than broken an install, which Lesson 03 covers.
3. **Open a document that already works**, which the start screen offers as bundled examples: open one, look at it, and close it without saving, since the purpose is only to confirm that playback, audio, and graphics initialise.
4. **Note where the examples live before you dismiss the start screen.** The start screen appears when *score* is launched with no document, and it is the only place that offers `Examples` and `Tutorials` directly, alongside recent files and `Restore last session`. Once dismissed it **cannot be reopened from any menu** in {{ page.score_version }}, because `File` offers new, load, recent files, save, close, quit, and the two server entries, while `View`, `Play`, and `Help` have no entry for it; the usability study flagged this. Nevertheless, three routes lead to the same material: relaunching *score* with no document, which brings the start screen back; the user library and project folder panels, `Ctrl+Shift+B` and `Ctrl+Shift+L`; and `Help > Documentation`.
5. **Check the version**, which appears in the window title and on the command line as `--version`; it should read `3.8.2` for this course.
6. **Leave a scratch project** by saving an empty document somewhere you will find it, for example `~/score/scratch.score`; Lesson 05 explains what it contains and what travels with it.

## Installing packages

Much of what this course uses later does not ship with the application: sound and MIDI material, Faust libraries, shader collections, and models. All of it arrives through the **package manager**, which lives in the application's settings, and installing a few now spares an interruption later.

**Packages are installed on your machine**, into `~/Documents/ossia/score/packages/` on Linux, one directory per package, and from there they appear in the **user library**, the third face of the left panel, `Ctrl+Shift+B`; an installed package is then draggable into a score like your own files.

**Material packages and code libraries both repay installing before Module G:**

- **Material packages** such as *Citizen DJ* are the most useful, because it contains several thousand short audio excerpts drawn from the Library of Congress collections, free to use, which is what the audio lessons and milestones need; `dirt-samples` and the drum kits give percussive material, and `free-midi-chords` gives MIDI files for [Lesson 23]({{ site.baseurl }}/learn/23-midi-in-practice.html).
- **Code libraries** matter next, since `abclib` provides the ambisonics and spatial tools [Lesson 22]({{ site.baseurl }}/learn/22-spatial-audio-1.html) mentions, and the JSFX pack gives hosted plug-ins for [Lesson 21]({{ site.baseurl }}/learn/21-effects-and-plugins.html) at no cost.

**Confirm the install** by opening the user library panel and finding the package by name; if it is not there, it did not install, and the package directory above is where to look.

Furthermore, a package is installed on *your machine* rather than into your document, so a score that uses a packaged Faust object or sample has that package as a dependency, like a plug-in, and [Lesson 34]({{ site.baseurl }}/learn/34-rehearsal-to-show.html) puts it in writing.

## The four places help lives

1. **Contextual help is bound to the `F1` key**: select an object in the scenario or a process in the library and press `F1` to open the reference page for that object. It is the fastest route from "what is this thing" to an answer, and the reason to keep the reference manual offline.
2. **The reference manual** lives at [ossia.io/score-docs]({{ site.docs_baseurl }}), and its shape repays learning now: a [quick start]({{ site.docs_baseurl }}/quick-start) that is short and linear, [common practices]({{ site.docs_baseurl }}/common-practices/common-practices.html) organised as recipes, [in-depth]({{ site.docs_baseurl }}/in-depth/in-depth.html) for the concepts underneath, and a per-object reference for processes and devices. This course is a path through that material and does not replace it.
3. **The bundled examples** matter because reading a working document is often faster than reading prose about it, the premise of Lesson 00.
4. **The community**, through the issue tracker and the forum, is where to turn when the first three have failed; Lesson 38 covers how to ask in a way that gets an answer, and how to turn a gap into a documentation fix.

## If it will not start, or will not make a sound

Nearly every failed first run has one of four causes.

**No window appears at all** when, on Linux, the AppImage's runtime is missing: older systems need FUSE available, and the fallback is to extract the image with `--appimage-extract` and run the binary inside. On macOS the same symptom is usually the quarantine flag on a downloaded application, which double-clicking does not clear but opening once through the right-click menu does.

**It starts and the window is blank or garbled** when the machine lacks a working OpenGL 3.2 or better driver, which is common on virtual machines and remote desktops; *score* draws its timeline through the GPU, so the problem is more than cosmetic.

**It starts, plays, and stays silent** when the audio backend is misconfigured or another application holds exclusive control of the sound card, so check both first. On Linux, prefer JACK or PipeWire, whereas on macOS and Windows the default backend is normally correct. However, no lesson before Module G needs audio at all, so a silent installation is not a reason to stop here.

**It starts but a plug-in scan hangs** when a single misbehaving VST stalls startup, and the remedy is to move the offending plug-in out of the scan path; the console panel, which [Lesson 03]({{ site.baseurl }}/learn/03-interface-and-transport.html) introduces, names the last plug-in attempted.

## Common mistakes

- **Installing a nightly build to follow a pinned course** makes small interface differences read as your own errors; if you want the newest features, install both and keep them separate.
- **Expecting sound before configuring audio** raises a false alarm, because silence in early lessons usually comes from the audio backend, and no lesson before Module G needs sound at all.
- **Dismissing the start screen and concluding the examples are gone** overlooks the three routes step 4 gives: relaunching *score* with no document, the user library and project folder panels, and `Help > Documentation`.
- **Skipping `F1`** leaves readers who do not discover contextual help guessing what a control does for the rest of the course.
- **On Windows, skipping Bonjour** leaves OSCQuery discovery silently empty, because the protocol works while the discovery mechanism it relies on is missing.

## Exercise

Install *score* {{ page.score_version }}, open one bundled example, and play it, then answer, in writing, three questions about it while reading only the software itself: what does its longest interval contain, what is the first thing it sends to a device, and what stops it. Use `F1` on at least two objects you cannot name.

**Success criterion:** you can name the two objects you pressed `F1` on and say which reference page appeared. If `F1` produced no page for an object, note which one, since that is a documentation gap Lesson 38 shows how to report.

## Going further

- [Installation]({{ site.docs_baseurl }}/quick-start/installation.html) is the reference version of this page, including FreeBSD and embedded targets.
- [Troubleshooting]({{ site.docs_baseurl }}/troubleshooting.html) covers a build that will not start or will not make sound.
- [The package manager]({{ site.docs_baseurl }}/in-depth/package-manager.html) installs addons and the user library, and Lesson 34 uses it.
- [Preferences]({{ site.docs_baseurl }}/reference-manual/references/preferences.html) lists every option; change none yet, although `auto-sequence` is off by default and Lesson 09 turns it on for a reason.

{% include lesson_files.html %}
