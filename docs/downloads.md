---
layout: default
title: Downloads
description: "Every example document the course ships, individually or as one archive."
nav_order: 2
permalink: /downloads
---

# Downloads

*ossia score* {{ site.score_version }}
{: .label .label-green}

Every document the course ships, with the media it references. They open in *score* {{ site.score_version }}; older builds may refuse them, as [Lesson 05]({{ site.baseurl }}/learn/05-saving-and-reopening.html) explains.

[Download all of it]({{ site.baseurl }}/library/learn/all-scores.zip) <small>(7.5 MB)</small>
{: .btn .btn-primary }

Keep each unit's folder together: the documents reference their media by a project-relative path, so a `.score` moved away from its folder opens with the media missing.

| Unit | Title | Files |
|---|---|---|
| [00]({{ site.baseurl }}/learn/00-what-score-is.html) | 00-what-score-is | [lesson-00-nodal.score]({{ site.baseurl }}/library/learn/00-what-score-is/lesson-00-nodal.score) <small>(score document, 43.7 kB)</small> · [lesson-00.score]({{ site.baseurl }}/library/learn/00-what-score-is/lesson-00.score) <small>(score document, 43.7 kB)</small> |
| [04]({{ site.baseurl }}/learn/04-first-process.html) | Interface layout and transport | [lesson-04.score]({{ site.baseurl }}/library/learn/04-first-process/lesson-04.score) <small>(score document, 16.3 kB)</small> |
| [09]({{ site.baseurl }}/learn/09-states-snapshots-presets.html) | Units, ranges, and types | [lesson-09.score]({{ site.baseurl }}/library/learn/09-states-snapshots-presets/lesson-09.score) <small>(score document, 19.5 kB)</small> |
| [10]({{ site.baseurl }}/learn/10-automation-curves.html) | Make it work 2: one fader drives a light wash | [lesson-10.score]({{ site.baseurl }}/library/learn/10-automation-curves/lesson-10.score) <small>(score document, 35.2 kB)</small> |
| [15]({{ site.baseurl }}/learn/15-triggers.html) | Make it work 3: a sensor to sound and light mapping bench | [lesson-15.score]({{ site.baseurl }}/library/learn/15-triggers/lesson-15.score) <small>(score document, 23.0 kB)</small> |
| [16]({{ site.baseurl }}/learn/16-conditions-and-branching.html) | Interactive triggers | [lesson-16.score]({{ site.baseurl }}/library/learn/16-conditions-and-branching/lesson-16.score) <small>(score document, 39.6 kB)</small> |
| [17]({{ site.baseurl }}/learn/17-loops-and-out-of-time.html) | Conditions and branching | [lesson-17.score]({{ site.baseurl }}/library/learn/17-loops-and-out-of-time/lesson-17.score) <small>(score document, 32.5 kB)</small> |
| [20]({{ site.baseurl }}/learn/20-sound-files.html) | Audio setup and the routing model | [excerpt-ghosts.wav]({{ site.baseurl }}/library/learn/20-sound-files/excerpt-ghosts.wav) <small>(audio, 1.4 MB)</small> · [excerpt-rocking-chair.wav]({{ site.baseurl }}/library/learn/20-sound-files/excerpt-rocking-chair.wav) <small>(audio, 3.3 MB)</small> · [lesson-20.score]({{ site.baseurl }}/library/learn/20-sound-files/lesson-20.score) <small>(score document, 21.7 kB)</small> |
| [25]({{ site.baseurl }}/learn/25-video-pipeline.html) | Tempo, metre, and synchronisation | [lesson-25.score]({{ site.baseurl }}/library/learn/25-video-pipeline/lesson-25.score) <small>(score document, 23.1 kB)</small> · [mock-bars.mp4]({{ site.baseurl }}/library/learn/25-video-pipeline/mock-bars.mp4) <small>(video, 1.3 MB)</small> · [mock-second.avi]({{ site.baseurl }}/library/learn/25-video-pipeline/mock-second.avi) <small>(video, 3.1 MB)</small> |
| [32]({{ site.baseurl }}/learn/32-puredata.html) | Faust inside score | [lesson-32.pd]({{ site.baseurl }}/library/learn/32-puredata/lesson-32.pd) <small>(Pure Data patch, 408 B)</small> · [lesson-32.score]({{ site.baseurl }}/library/learn/32-puredata/lesson-32.score) <small>(score document, 20.7 kB)</small> |
| [P1]({{ site.baseurl }}/learn/p1-automated-cue.html) | Saving, versioning, and reopening | [p1-solution.score]({{ site.baseurl }}/library/learn/p1-automated-cue/p1-solution.score) <small>(score document, 32.0 kB)</small> |
| [P2]({{ site.baseurl }}/learn/p2-light-wash.html) | States, snapshots, and presets | [p2-solution.score]({{ site.baseurl }}/library/learn/p2-light-wash/p2-solution.score) <small>(score document, 24.7 kB)</small> |
| [P4]({{ site.baseurl }}/learn/p4-interactive-installation.html) | Cues, seek, and transport control | [p4-solution.score]({{ site.baseurl }}/library/learn/p4-interactive-installation/p4-solution.score) <small>(score document, 36.5 kB)</small> |

## How these were made

Most are generated rather than hand-built: `scripts/mkscore.py` writes them as JSON, which is what a `.score` file is. That is what makes them reproducible when the pinned version changes, and it is why the figures in this course can be re-shot by script. The audio excerpts come from the Citizen DJ packages, installable through *score*'s package manager and free to use; the video clips are generated with `ffmpeg`, with the commands printed in [Lesson 25]({{ site.baseurl }}/learn/25-video-pipeline.html).
