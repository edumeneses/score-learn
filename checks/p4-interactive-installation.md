# Re-verification note: p4-interactive-installation

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| p4-01 | Idle loop, visitor trigger, two branches, return transitions | **done**, docs/learn/assets/p4/p4-01-installation-structure.png |

## Re-verify when the pinned version changes

- Every mechanism this milestone composes, since it introduces none of its own.
- That maximum durations still bound a waiting instant.

## Claims that depend on external sources

- Grounded in the reference documentation for this topic; see the 'Going further'
  links on the lesson page, which are the pages this lesson was written against.

## How p4-solution.score is built, 2026-08-18

`python3 scripts/mkscore.py P4`. No interaction: the builder learned transitions on
2026-08-18, so this milestone's structure is generated like the early figures and can be
re-shot when the pinned version changes.

The structure, which is the brief translated into instants and edges:

```
0s --[ Idle ]-- 4s --(visitor)--+-- level > 0.5 --[ Bright ]-- 10s --+
     ^                          |                                    |
     |                          +-- level <= 0.5 --[ Quiet ]-- 8s ---+
     |                                                               |
     +---------------- return transitions ---------------------------+
```

Points worth keeping:

- **The trigger and the conditions are separate objects.** The instant at 4s is `Active`,
  which makes it wait; the two events leaving it carry the conditions. One releases, the
  other chooses.
- **Each branch has its own end instant**, per the note in `CLAUDE.md`: three intervals
  cannot share one end state, and score silently drops a scenario that tries.
- **Both return transitions arrive at the score's first instant**, so its event carries
  three states: the chain's start plus one arrival per transition.
- **The branches differ in length on purpose**, 6 s against 4 s, so the return path is
  exercised for both rather than only for the symmetric case.
- **The document is endless**, `document(..., endless=True)` plus `max_inf` on the root,
  which is what "repeats indefinitely" requires. See
  `checks/17-loops-and-out-of-time.md` for why both settings are needed.

What the figure does **not** show, and the milestone still asks for: maximum durations on
the waiting instants, the start and stop cues, and the eight-hour test. Those are the
reader's work, and none of them is visible as structure.

## 2026-09-25: the reference solution's trigger does not wait

Found while testing the capture server, and **not yet fixed**. In `p4-solution.score` the
instant labelled `a visitor arrives` follows `Idle`, which `mkscore.py` builds rigid at
exactly 4 s (min = max = 4 s). A trigger waits only between the preceding interval's
minimum and maximum, so this one fires by itself at 4 s with no visitor, which
contradicts the page ("the instant at its end waits for the visitor"). Played on the
capture server with no input at all, at 7.3 s both `Bright` and `Quiet` showed as
running, although their conditions partition `lesson:/level`; why both conditions passed
was not established. The fix is `lesson_00`'s: make `Idle` elastic. How long it may wait
is a design decision, because step 6 asks for a maximum on every waiting instant, so it is
Edu's to choose. Then re-shoot `p4-01`, whose `Idle` will gain a flexible end.
