# Re-verification note: 18-cues-and-transport

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 18-01 | Play-from-here in the context menu, above the transport bar | **done**, docs/learn/assets/18/18-01-transport.png |

See `checks/FIGURES-PENDING.md` for the consolidated list of figures that need
an interactive session, and why each one cannot be produced by the scripted
pipeline.

## Re-verify when the pinned version changes

- The transport button order: local play, global play, stop, reinitialise.
- That a cue on the first state fires on start and on reinitialise, and a cue on the last state fires on stop.
- Value compilation on seek, and the two preferences controlling it.
- The start marker in the musical metrics area.
- That JACK is still the only external transport.

## Claims that depend on external sources

- Grounded in the reference documentation for this topic; see the 'Going further'
  links on the lesson page, which are the pages this lesson was written against.

## Corrected 2026-08-11 against the running build

The Play menu names all four transport actions and their shortcuts: Play (space),
Play (global) (Shift+Space), Stop (Return), Reinitialize (Ctrl+Return), plus
Play (Network) and Stop (Network). The Object menu carries Synchronize (Shift+M)
and Merge events, which is the clearest way to find the synchronisation function.
