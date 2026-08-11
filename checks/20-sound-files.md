# Re-verification note: 20-sound-files

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 20-01 | Two sound files, one played once and one looping | **done**, docs/learn/assets/20/20-01-sound-files.png |

See `checks/FIGURES-PENDING.md` for the consolidated list of figures that need an
interactive session or media, and why each cannot be produced by the scripted
pipeline.

## Re-verify when the pinned version changes

- Drag-and-drop of a sound file from the library and from the file manager.
- The loop toggle in the sound file inspector.
- The envelope process's two outputs: RMS first, peak second.
- The <PROJECT>: and <LIBRARY>: path prefixes.

## Claims that depend on external sources

- Grounded in the reference pages linked under 'Going further' on the lesson page.

## How this document was built, 2026-08-11

Generated rather than assembled by hand. `scripts/mkscore.py 20` emits a Sound process
(uuid 63174570-d608-44bf-a9cb-e6f5a11f73cc) whose `File` field uses the `<PROJECT>:`
prefix, so the two excerpts resolve from the project folder and the document travels. The
excerpts are copied from the installed `citizen-dj-free-music` and `citizen-dj-musicbox`
packages, which are freely usable.

The shape of the Sound process was read out of score's own `all-media.score` example
rather than guessed, which is the general method for teaching mkscore.py a new process.
