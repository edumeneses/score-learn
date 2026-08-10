# Re-verification note: 05-saving-and-reopening

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 05-01 | The project folder panel beside a project directory on disk | pending: needs a document with media, which this lesson does not ship |

Figures are produced by the pipeline described in the README: `scripts/mkscore.py`,
`scripts/capture.py`, then `scripts/annotate.py` against a spec in `figures/`.
Anything marked pending needs synthetic input, which requires an unlocked session.

## Re-verify when the pinned version changes

- That media is referenced rather than embedded, by moving a project and reopening it.
- That Alt+Drag into the user library still writes a .scenario file.
- That the document still records the writing version, and that older documents still open in newer builds.
- That the project folder panel still shows the current document's files.

## Claims that depend on external sources

- The scenario-preset mechanism and the absence of per-process presets come from the reference presets page; that asymmetry is likely to change and should be re-read at each pin.
