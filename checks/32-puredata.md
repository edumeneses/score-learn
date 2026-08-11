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

## Figure 32-01, done 2026-08-11, and what it corrected

The library entry is `PureData`, under `Plugins`; searching for `pure` finds Airwindows
plug-ins instead. Process uuid `7b3b18ea-311b-40f9-b04e-60ec1fe05786`, with a `Script`
field holding the patch path.

**The lesson was wrong about how ports are made.** They do not come from the patch's
`inlet` and `outlet` objects. score parses the patch for annotated **receives**:

    r $0-gain @type float @range 0 1 @default 1

which becomes a `gain` control inlet with that range and default; a matching `s $0-name`
send becomes an outlet, and `adc~` / `dac~` provide the audio ports. This was found by
reading `packages/default/Presets/PureData/3band.pd`, which declares four controls that
way. `lesson-32.pd` was rewritten to match, and the lesson now teaches the real
convention.

**Two further findings, both now in the lesson or here:**

- The port list is stored in the document. score does **not** re-read the patch when a
  document opens, so hand-editing the `Script` path leaves the old ports in place; the
  patch must be re-selected in the inspector for ports to be derived again. This is why
  the first three attempts at this figure showed only Audio In and Audio Out.
- The `<PROJECT>:` prefix, which works for media paths, did not resolve for this field in
  testing; `lesson-32.score` therefore stores an absolute path, which means it must be
  re-pointed after the project moves. Worth re-checking at the next version pin.
