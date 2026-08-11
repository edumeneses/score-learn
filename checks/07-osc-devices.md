# Re-verification note: 07-osc-devices

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 07-01 | The Add device dialog: protocols, declared devices, OSC settings with both ports | **done**, docs/learn/assets/07/07-01-add-device.png |

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

## Corrected 2026-08-11 from the dialog itself

The OSC settings name the two directions asymmetrically, and the lesson now uses the
dialog's own words: `Device host` and `Device listening port` are where score **sends**,
`score listening port` is where score **receives**. The dialog also refuses with
"Cannot add device. Try changing the name to make it unique, or check that the ports
aren't already used", which the walkthrough now mentions.

Captured with a human click: five automated attempts failed. `Ctrl+B` does not fire under
synthetic input, and clicking the `Add device` menu row registers on the correct row
without the dialog appearing.

## A capture-harness finding

The dialog was invisible to `capture.py --popups` at first: a reparenting window manager
wraps it in a frame whose WM_CLASS is the manager's (`mutter-x11-frames`), not score's, so
the filter rejected it. `popups()` now descends into such frames to find the real window.
Any future dialog figure depends on this.
