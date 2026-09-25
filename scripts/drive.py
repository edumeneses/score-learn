#!/usr/bin/env python3
"""Drive score from inside, through its own scripting API, and capture as it goes.

    python3 scripts/drive.py library/learn/00-what-score-is/lesson-00.score \
        scripts/drive/00-trigger-waits.js

score 3.8.2 runs a QML file given with `--ui-debug FILE`, next to its normal
interface, and that file sees the same `Score` object as the console: 83
members, among them play, pause, stop, find, createProcess, createCable,
setValue, automate, zoom, scroll, saveAs, and serializeAsJson (listed on
2026-09-25 by enumerating the object). `Util.shell` runs a command and reports
its exit code, which is how a step captures the window at an exact moment.
Nothing here clicks, so it works on any display; figures still belong on the
capture server (capture.py server start), where the pinned settings apply.

The steps file is plain JavaScript that sets `steps` to a list built from
these helpers, run in order, each starting when the previous one ends:

    call(function () { ... })   run code; Score, Util, and find(name) are in scope
    sleep(ms)                   wait
    shot("figures/raw/x.png")   capture score's window, recording provenance
    shot("out.png", "--popups") extra capture.py shot options
    log("text")                 write to the run's log
    lower("Window")             put a Window device's output beneath score, since
                                it opens over the main window and captures black
    runDir                      a scratch directory for this run

For example:

    var steps = [
      call(function () { Score.play(); }),
      sleep(8500),
      call(function () { Score.pause(); }),
      shot("figures/raw/raw-00-03.png"),
    ];

Found while probing, and handled here: the QML file gets a top-level window of
its own, 1280x960 at the origin, which lands inside every capture on a display
without a compositor; it is hidden once it exists, about 300 ms after load.
`Score.scrub` reset the clock without moving the drawn progress, so position
the playhead by playing and pausing instead. Ports are found by their displayed
label (`Score.port(lfo, "Freq.")`, not "Frequency"), or by index with
`Score.inlet`. `Score.availableProcesses()` returned undefined.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)

QML = r"""import QtQuick
import QtQuick.Window

Item {
  id: root
  width: 8; height: 8

  property string runDir: "__RUN__"
  property var queue: []
  property var pending: null

  function find(name) { return Score.find(name); }
  function call(fn) { return function (next) { fn(); next(); }; }
  function log(text) { return function (next) { console.log("DRIVE " + text); next(); }; }
  function sleep(ms) {
    return function (next) { root.pending = next; waiter.interval = ms; waiter.restart(); };
  }
  function shot(path, extra) {
    return function (next) {
      var cmd = __CAPTURE__ + " shot " + (extra || "") + " '" + path + "'";
      Util.shell(cmd, function (code) {
        console.log("DRIVE shot " + path + " exit " + code);
        if (code != 0) root.fail("capture failed: " + path);
        else next();
      });
    };
  }
  function lower(name) {
    return function (next) {
      Util.shell(__CAPTURE__ + " lower '" + name + "'", function (code) { next(); });
    };
  }
  function fail(msg) {
    console.log("DRIVE failed " + msg);
    Util.shell("echo " + JSON.stringify(msg) + " > '__DONE__.failed'", function () {});
  }
  function advance() {
    if (root.queue.length === 0) {
      console.log("DRIVE done");
      Util.shell("touch '__DONE__'", function () {});
      return;
    }
    var step = root.queue.shift();
    try { step(advance); } catch (e) { root.fail(String(e)); }
  }

  Timer { id: waiter; repeat: false; onTriggered: { var n = root.pending; root.pending = null; n(); } }

  Timer {
    // The QML window exists only after load; hide it, or it covers the capture.
    interval: 300; running: true
    onTriggered: {
      var w = root.Window.window;
      if (w) w.visible = false;
      console.log("DRIVE window " + (w ? "hidden" : "not found"));
    }
  }

  Timer {
    interval: __SETTLE__; running: true
    onTriggered: {
      try {
__STEPS__
        root.queue = steps.slice();
      } catch (e) { root.fail("steps file: " + e); return; }
      advance();
    }
  }
}
"""


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("document")
    p.add_argument("steps", help="JavaScript file that sets `steps`")
    p.add_argument("--settle", type=int, default=2500,
                   help="ms after load before the first step, so the view is laid out")
    p.add_argument("--timeout", type=float, default=120.0)
    p.add_argument("--keep", action="store_true", help="leave score running afterwards")
    p.add_argument("--log", default=None, help="score's output; default in the run directory")
    args = p.parse_args()

    if not os.environ.get("DISPLAY"):
        print("DISPLAY is unset; start the capture server and export DISPLAY=:7")
        return 1
    run = tempfile.mkdtemp(prefix="score-drive-")
    done = os.path.join(run, "done")
    capture = (f"'{sys.executable}' '{os.path.join(HERE, 'capture.py')}' "
               f"--match 'score 3.8.2'")
    steps = open(args.steps, encoding="utf8").read()
    qml = (QML.replace("__CAPTURE__", json.dumps(capture))
              .replace("__DONE__", done)
              .replace("__RUN__", run)
              .replace("__SETTLE__", str(args.settle))
              .replace("__STEPS__", "\n".join("        " + l for l in steps.splitlines())))
    qml_path = os.path.join(run, "drive.qml")
    with open(qml_path, "w", encoding="utf8") as f:
        f.write(qml)
    log = args.log or os.path.join(run, "score.log")

    document = os.path.abspath(args.document)
    subprocess.run([sys.executable, os.path.join(HERE, "capture.py"), "stop"],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, cwd=REPO)
    r = subprocess.run(
        [sys.executable, os.path.join(HERE, "capture.py"), "--match", "score 3.8.2",
         "launch", "--qt-scale", "2", "--fullscreen", "--log", log,
         "--open", f"--ui-debug '{qml_path}' '{document}'"],
        cwd=REPO,
    )
    if r.returncode:
        return r.returncode

    deadline = time.time() + args.timeout
    status = 1
    while time.time() < deadline:
        if os.path.exists(done + ".failed"):
            print(f"failed: {open(done + '.failed').read().strip()}")
            break
        if os.path.exists(done):
            status = 0
            break
        time.sleep(0.5)
    else:
        print(f"timed out after {args.timeout:.0f}s")

    for line in open(log, errors="replace"):
        if "DRIVE" in line or "Error" in line:
            print("  " + line.rstrip())
    if not args.keep:
        subprocess.run([sys.executable, os.path.join(HERE, "capture.py"), "stop"], cwd=REPO)
    print(f"run directory: {run}")
    return status


if __name__ == "__main__":
    sys.exit(main())
