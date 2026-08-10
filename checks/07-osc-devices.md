# Re-verification note: 07-osc-devices

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 07-01 | The OSC protocol dialog with its two port settings, and the address editor | pending: needs interaction (modal dialogs) |

Figures are produced by the pipeline described in the README: `scripts/mkscore.py`,
`scripts/capture.py`, then `scripts/annotate.py` against a spec in `figures/`.
Anything marked pending needs synthetic input, which requires an unlocked session.

## Re-verify when the pinned version changes

- That the message log is Ctrl+Shift+G and the console Ctrl+Shift+C, since the diagnosis routine names them.
- That values can still be set from the explorer inspector, which step 5 relies on to separate connection problems from score problems.
- That a wrong destination port still fails silently, which the walkthrough asks the reader to observe. If score gains a warning here, step 9 must change.
- The supported parameter types, in particular that impulse exists and is distinct from a float.

## Claims that depend on external sources

- Port semantics and the address-declaration workflow come from the reference OSC device page.
