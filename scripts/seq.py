#!/usr/bin/env python3
"""Send timed input to score on the capture server and grab its window at set moments.

    python3 scripts/seq.py OUTDIR STEP...

capture.py checks every input for a visible change, which costs about a second per
command and makes "click at 2.5 s, capture at 6 s" impossible. This script sends raw
XTEST input with no verification and no window activation, so a whole run keeps its
timing. Each step is one of:

    k=COMBO    press a key or chord, e.g. k=space, k=Return, k=ctrl+z
    c=X,Y      click at screen coordinates
    m=X,Y      move the pointer (hover)
    w=SECONDS  wait until SECONDS after the run started
    s=NAME     grab score's window to OUTDIR/NAME.png

and each is printed with its elapsed time, for example:

    python3 scripts/seq.py /tmp/run k=Return w=1 k=space w=4 c=2100,374 w=7 s=after

Keys only reach score when it has keyboard focus, and the first click on an unfocused
window only focuses it, so start with a click on empty timeline when a previous command
raised another window. The grabs record no provenance; they are for testing, not figures.
Used on 2026-09-30 to show that a click before a trigger's minimum is ignored and that its
maximum releases it (checks/15-triggers.md).
"""

from __future__ import annotations

import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ["DISPLAY"] = os.environ.get("SEQ_DISPLAY", ":7")

import capture  # noqa: E402
from Xlib import X  # noqa: E402
from Xlib.ext import xtest  # noqa: E402


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    d = capture.dpy()
    found = capture.find_window(d, capture.WINDOW_MATCH)
    if not found:
        print("no score window on", os.environ["DISPLAY"])
        return 1
    win = found[0]
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    t0 = time.time()
    for step in sys.argv[2:]:
        op, arg = step.split("=", 1)
        if op == "w":
            delay = t0 + float(arg) - time.time()
            if delay > 0:
                time.sleep(delay)
        elif op == "k":
            codes = [capture.keycode(d, part) for part in arg.split("+")]
            for code in codes:
                xtest.fake_input(d, X.KeyPress, code)
            d.sync()
            time.sleep(0.05)
            for code in reversed(codes):
                xtest.fake_input(d, X.KeyRelease, code)
            d.sync()
        elif op in ("c", "m"):
            x, y = map(int, arg.split(","))
            xtest.fake_input(d, X.MotionNotify, x=x, y=y)
            d.sync()
            time.sleep(0.08)
            if op == "c":
                xtest.fake_input(d, X.ButtonPress, 1)
                d.sync()
                time.sleep(0.05)
                xtest.fake_input(d, X.ButtonRelease, 1)
                d.sync()
        elif op == "s":
            g = win.get_geometry()
            capture.grab_window(win, (0, 0, g.width, g.height)).save(f"{out}/{arg}.png")
        else:
            print(f"unknown step {step}")
            return 2
        print(f"{time.time() - t0:6.2f}s {step}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
