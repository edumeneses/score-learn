# Re-verification note: 32-puredata

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 32-01 | A hosted patch's ports in the nodal view | needs interaction + a patch file |

See `checks/FIGURES-PENDING.md` for the consolidated list.

## Re-verify when the pinned version changes

- That patch inlets and outlets map to process ports.
- That the patch is referenced by path, so it follows the media rules.
- That Pure Data must be installed for the process to work.

## Claims that depend on external sources

- Grounded in the reference pages linked under 'Going further' on the lesson page.

## Patch shipped with this lesson, 2026-08-11

`library/learn/32-puredata/lesson-32.pd`: two inlets (gain, offset), a multiply, an add,
one outlet. Verified to load with Pure Data 0.54.1. It exists so the port-mapping steps
can be followed without the reader supplying a patch, and it is small enough to print in
the lesson.

## Figure 32-01, attempt of 2026-08-11

Not captured. Searching the process library for `pure` returns Airwindows plug-ins
(PurestEcho, PurestAir, the PurestConsole family) and no Pure Data process, so the
library entry is named something else: try `pd`, or browse the `Script` category, which
is where the reference documentation groups the code-based processes.

The route that will work, once the entry is found: copy the patch to a short path, select
an interval, filter the library, double-click the entry to add and connect it, then set the
patch path in the inspector. The same select-then-double-click technique produced figures
11-01 and 13-01.
