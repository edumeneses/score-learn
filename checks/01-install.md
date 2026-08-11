# Re-verification note: 01-install

Pinned build: **ossia score 3.8.2**

## Figures

| ID | Content | Status |
|---|---|---|
| 01-01 | Start screen with the bundled examples, and the File menu showing how to reopen it | pending: needs interaction (menu open), see below |

Figures are produced by the pipeline described in the README: `scripts/mkscore.py`,
`scripts/capture.py`, then `scripts/annotate.py` against a spec in `figures/`.
Anything marked pending needs synthetic input, which requires an unlocked session.

## Re-verify when the pinned version changes

- Every install command: winget, pacman/MSYS2, brew cask, flatpak, AUR, nix, and the AppImage filename pattern.
- The minimum requirements list, in particular the graphics API versions.
- That the Windows OSCQuery note still requires Bonjour.
- That the start screen still exposes the examples, and that the File menu still reopens it. The usability study's finding depends on this.
- The four help routes, especially that F1 still opens per-object reference pages.

## Claims that depend on external sources

- Platform and packaging details come from the reference installation page; re-read it at each pin.
- The documentation-quality and start-screen findings come from the SAT Ossia score UI/UX study report.

## Corrected 2026-08-11 against the running build

The start screen **cannot be reopened from any menu** in 3.8.2. File offers New, Load,
Recent files, Save, Save as, Close, Quit, Make Server, Join Server; View, Play, and
Help have no entry for it. An earlier draft of this lesson said it could be reopened
from the File menu, which was wrong.
