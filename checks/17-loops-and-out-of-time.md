# Re-verification note: 17-loops-and-out-of-time

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 17-01 | A loop built from a transition, and out-of-time material | needs interaction: transitions are not emitted by mkscore.py |

See `checks/FIGURES-PENDING.md` for the consolidated list of figures that need
an interactive session, and why each one cannot be produced by the scripted
pipeline.

## Re-verify when the pinned version changes

- That transitions are instantaneous intervals and can connect backwards.
- That transitioning to an instant re-executes everything attached to it, and that the smallest loop restarts first.
- The maximum-duration idiom for repetition counts.
- Start-on-play for out-of-time material, and the hover play/stop buttons during playback.

## Claims that depend on external sources

- Grounded in the reference documentation for this topic; see the 'Going further'
  links on the lesson page, which are the pages this lesson was written against.

## Corrected 2026-08-11 against the running build

Encapsulate (Ctrl+Alt+E) and Decapsulate (Ctrl+Alt+D), in the Object menu, are the
commands that put a selection into a sub-scenario and take it back out.
