#!/usr/bin/env bash
# Re-shoot figure 00-02 (the nodal view) with the graph fitted to the editor.
# Needs an UNLOCKED desktop session: launch and capture work while locked, but every
# synthetic click is swallowed, and the only symptom is a capture identical to the last.
#
# Produces figures/raw/raw-00-02.png. Then set the crop in figures/00-02.json to the
# fitted node's bounds (view the raw first), point badge 1 at the "Scenario.1" title,
# and run:  python3 scripts/annotate.py figures/00-02.json
set -euo pipefail
cd "$(dirname "$0")/.."
export DISPLAY="${DISPLAY_OVERRIDE:-:0}"
export QT_QPA_PLATFORM=xcb
export XAUTHORITY="$(ls /run/user/$(id -u)/.mutter-Xwaylandauth.* | head -1)"
PY="${PY:-/home/edu/Assistant/venv/bin/python3}"
CAP="$PY scripts/capture.py --match score\ 3.8.2"

pgrep -f 'ossia[-]score' | xargs -r kill; sleep 2
$CAP launch --qt-scale 2 --fullscreen --open "$PWD/library/learn/00-what-score-is/lesson-00-nodal.score"
sleep 6
$CAP click 899 2112            # third view-mode button: nodal view
sleep 2
$CAP click 768 182             # fourth small icon of the nodal slot: fit graph to view
sleep 2
$CAP shot figures/raw/raw-00-02.png
$CAP shot /tmp/raw-00-02-check.png
if cmp -s figures/raw/raw-00-02.png /tmp/raw-00-02-check.png; then
  echo "captured; now compare against git to confirm the clicks landed:"
  echo "  git diff --stat figures/raw/raw-00-02.png   (no change means input was swallowed)"
fi
pgrep -f 'ossia[-]score' | xargs -r kill
