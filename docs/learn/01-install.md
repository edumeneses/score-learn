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
> **You will need** a 64-bit computer running Linux, macOS, or Windows, about 400 MB of disk space, and speakers or headphones.
>
> **You will build** a working installation of *score* {{ page.score_version }}, a map of where the software answers questions, and a first sketch that plays a sound and shows a colour.

## Why this matters

This course pins one version, *score* **{{ page.score_version }}**, and every figure in it was captured from that build. Interface details move between releases, so a newer build shows small differences in wording and icon placement, although the concepts hold; pinning is the difference between a course that can be corrected and one that slowly stops matching what the reader sees.

The second half of this lesson is about help, and it comes this early because the usability study conducted at the Société des Arts Technologiques rated the documentation as middling and found that closing the start screen loses easy access to the bundled examples. Both findings have the same practical consequence: readers who do not know where the answers live conclude there are none.

## Concepts

### Releases and development builds

The software publishes tagged releases and development builds. The tagged release is what a download page gives you and what this course targets. In contrast, development builds carry features that are not documented yet, which makes them useful later and distracting now.

### Portable and installed builds

A portable build and an installed build serve different needs. On Linux the AppImage is a single executable file that installs and registers no component, so several versions can sit side by side, as a pinned course requires. Conversely, Flatpak and distribution packages integrate better with the desktop and update with the system, while on macOS and Windows the usual installers apply.

### The audio backend

The audio backend sits between *score* and the sound card. The software talks to whatever audio system your machine runs, which on Linux means JACK or PipeWire for reliable low latency, and ALSA otherwise. Getting this right matters from this lesson's exercise onward, and Lesson 19 covers it in depth; a machine that produces no sound usually has a backend problem rather than a score problem.

## Installing

The minimum requirements for the software are modest: a 64-bit operating system, a GPU (graphics processing unit) supporting OpenGL 3.2, Vulkan, Direct3D 11, or Metal, and 512 MB of RAM. However, video work and dense scenarios want considerably more than the minimum, and Module I assumes a GPU from the last decade.

**On Linux, this course recommends the AppImage build.** Download the AppImage for your architecture from <https://ossia.io/score/download.html> or from the [GitHub releases page](https://github.com/ossia/score/releases), then make it executable and run it:

```bash
chmod +x ossia.score-3.8.2-linux-x86_64.AppImage
./ossia.score-3.8.2-linux-x86_64.AppImage
```

Keeping it in `~/Applications` lets several pinned versions coexist, while AArch64 builds cover Raspberry Pi and Asahi Linux, as Lesson 35 shows.

**Packaged builds exist for several Linux distributions.** Flatpak uses `flatpak install flathub io.ossia.score` then `flatpak run io.ossia.score`; the Arch User Repository uses `yay -S ossia-score`; nixpkgs uses `nix-shell -p ossia-score`; and FreeBSD has a port.

**On macOS, download the `.dmg` matching your machine**, Apple Silicon or Intel, and drag *score* into Applications; Intel builds need macOS 10.15 or later, and Homebrew offers `brew install --cask ossia-score`. Some VST (Virtual Studio Technology) plug-ins and virtual cameras need permissions granted in System Settings, which surfaces in Module G.

**On Windows, run the installer from the download page**, or `winget install ossia.score`, or under MSYS2 `pacman -S mingw-w64-x86_64-ossia-score`. An extra step matters later, because the OSCQuery protocol, which Lesson 06 covers, needs [Bonjour Print Services](https://support.apple.com/kb/DL999) for network discovery.

## Walkthrough: first run

![The ossia score start screen, with recent files, Examples, and Tutorials]({{ site.img }}/01/01-01-start-screen.png)

1. **Launch the application**, whose startup takes a few seconds the first time while plug-ins are scanned, and you arrive at the start screen in the figure.
2. **Confirm the three areas of the window.** A correct installation shows the `Device explorer` on the left, the scenario editor in the centre, and the object inspector on the right; if any is missing, you have almost certainly collapsed a panel instead of breaking the install, which Lesson 03 covers.
3. **Open a document that already works**, which the start screen offers as bundled examples: open one, look at it, and close it without saving, since the purpose is only to confirm that playback, audio, and graphics initialise.
4. **Note where the examples live before you dismiss the start screen.** The start screen appears when *score* is launched with no document, and it is the only place that offers `Examples` and `Tutorials` directly, alongside recent files and `Restore last session`. Once dismissed it **cannot be reopened from any menu** in {{ page.score_version }}, which the usability study flagged. Nevertheless, three routes lead to the same material: relaunching *score* with no document; the user library and project folder panels, `Ctrl+Shift+B` and `Ctrl+Shift+L`; and `Help > Documentation`.
5. **Check the version**, which appears in the window title and on the command line as `--version`; it should read `3.8.2` for this course.

## Installing packages

Much of what this course uses does not ship with the application, since sound and MIDI material, Faust libraries, shader collections, and models all arrive through the **package manager**, which lives in the application's settings. Packages are installed on your machine, into `~/Documents/ossia/score/packages/` on Linux, and from there they appear in the **user library**, the third face of the left panel, `Ctrl+Shift+B`, where they can be dragged into a score like your own files.

**Four packages repay installing now.** *Citizen DJ* gives several thousand short audio excerpts from the Library of Congress collections, free to use, which the exercise below and the audio lessons need; `free-midi-chords` serves [Lesson 23]({{ site.baseurl }}/learn/23-midi-in-practice.html); `abclib` provides the spatial tools of [Lesson 22]({{ site.baseurl }}/learn/22-spatial-audio-1.html); and the JSFX pack gives free plug-ins for [Lesson 21]({{ site.baseurl }}/learn/21-effects-and-plugins.html). Furthermore, a package belongs to your machine and not to your document, so a score that uses a packaged sample has that package as a dependency, which [Lesson 34]({{ site.baseurl }}/learn/34-rehearsal-to-show.html) puts in writing.

## The four places help lives

1. **Contextual help is bound to the `F1` key**: select an object in the scenario or a process in the library and press `F1` to open the reference page for that object. It is the fastest route from "what is this thing" to an answer, and the reason to keep the reference manual offline.
2. **The reference manual** lives at [ossia.io/score-docs]({{ site.docs_baseurl }}), and its shape repays learning now: a [quick start]({{ site.docs_baseurl }}/quick-start) that is short and linear, [common practices]({{ site.docs_baseurl }}/common-practices/common-practices.html) organised as recipes, [in-depth]({{ site.docs_baseurl }}/in-depth/in-depth.html) for the concepts underneath, and a per-object reference for processes and devices. This course is a path through that material and does not replace it.
3. **The bundled examples** matter because reading a working document is often faster than reading prose about it, the premise of Lesson 00.
4. **The community**, through the issue tracker and the forum, is where to turn when the first three have failed; Lesson 38 covers how to ask in a way that gets an answer, and how to turn a gap into a documentation fix.

## If it will not start, or will not make a sound

Nearly every failed first run has one of four causes.

**No window appears at all** when, on Linux, the AppImage's runtime is missing: older systems need FUSE available, and the fallback is to extract the image with `--appimage-extract` and run the binary inside. On macOS the same symptom is usually the quarantine flag on a downloaded application, which double-clicking does not clear but opening once through the right-click menu does.

**It starts and the window is blank or garbled** when the machine lacks a working OpenGL 3.2 or better driver, which is common on virtual machines and remote desktops; *score* draws its timeline through the GPU, so the problem is more than cosmetic.

**It starts, plays, and stays silent** when the audio backend is misconfigured or another application holds exclusive control of the sound card, so check both first. On Linux, prefer JACK or PipeWire, whereas on macOS and Windows the default backend is normally correct. With the PipeWire driver, `Settings > Audio` carries an `Auto-connect ports` option, and when it is off nothing links *score* to your speakers, so the clock under the timeline stays at zero after you press play; turning it on, or choosing another driver, is the first thing to try.

**It starts but a plug-in scan hangs** when a single misbehaving VST stalls startup, so move that plug-in out of the scan path; the console panel of [Lesson 03]({{ site.baseurl }}/learn/03-interface-and-transport.html) names the last one attempted.

## Common mistakes

- **Installing a nightly build to follow a pinned course** makes small interface differences read as your own errors; if you want the newest features, install both and keep them separate.
- **Blaming the document for silence** overlooks the audio backend, which is the usual cause on a new installation and therefore the first thing to check when the sketch below stays quiet.
- **Skipping `F1`** leaves readers who do not discover contextual help guessing what a control does for the rest of the course.
- **On Windows, skipping Bonjour** leaves OSCQuery discovery silently empty, because the protocol works while the discovery mechanism it relies on is missing.

## Exercise

Build the small document that the next exercises return to, a *sketch* that plays a sound and shows a colour, because a first document you can hear and see turns every later change into something you can check by listening.

1. **Install a sound package** through the package manager, as described above; `citizen-dj-free-music` is enough, since its excerpts are dedicated to the public domain and free to reuse.
2. **Start an empty document** with `File > New`, and open the user library with `Ctrl+Shift+B`.
3. **Find an excerpt** by typing `free` in the library's search field, which filters by folder name rather than by file name, then open `citizen-dj-free-music` and its `excerpts` folder. Select a few files and press the play button under the list, which auditions each one before you commit to it.
4. **Drag the excerpt you like onto the timeline**, near its left edge, and *score* creates an interval holding a sound process, drawn as its waveform.
5. **Add a window for the image** by right-clicking the empty `Device explorer`, `Ctrl+Shift+D`, choosing `Add device`, then `Video > Window` and `Add`; a black window opens, which is where the colour will appear.
6. **Find a shader** in the process library, `Ctrl+Shift+P`, by typing `Solid`, and drag `Visuals > ISF Shader > generator > Solid Color` onto the empty timeline well below the sound, which creates a second interval holding the shader.
7. **Send the shader to the window** by clicking the shader's title, so that the inspector on the right describes it, and choosing `Window` in the list under `Outputs`.
8. **Press `space` to play**, and save the document as `sketch.score` in a folder of its own, for example `~/score/sketch/`, since Lesson 05 turns that folder into a portable project.

**You are done when** you hear the excerpt and see the window turn red. If the window stays black, the shader's output is still unset. However, silence with a clock that does not move points to the audio backend, which the section on silent starts above covers.

## Going further

- [Installation]({{ site.docs_baseurl }}/quick-start/installation.html) is the reference version of this page, including FreeBSD and embedded targets.
- [Troubleshooting]({{ site.docs_baseurl }}/troubleshooting.html) covers a build that will not start or will not make sound.
- [The package manager]({{ site.docs_baseurl }}/in-depth/package-manager.html) installs addons and the user library.
- [Preferences]({{ site.docs_baseurl }}/reference-manual/references/preferences.html) lists every option, although none needs changing yet.

{% include lesson_files.html %}
