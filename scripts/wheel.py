#!/usr/bin/env python3
"""Send mouse-wheel steps at a point, optionally with Ctrl held: wheel.py X Y STEPS [--ctrl]
STEPS > 0 scrolls down (button 5), < 0 scrolls up (button 4)."""
import sys, time
sys.path.insert(0, "/media/Storage/score-learn/scripts")
import capture
from Xlib import X
from Xlib.ext import xtest
x, y, steps = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
ctrl = "--ctrl" in sys.argv
d = capture.dpy()
capture.move(d, x, y); d.sync(); time.sleep(0.2)
button = 5 if steps > 0 else 4
if ctrl:
    code = capture.keycode(d, "Control_L"); xtest.fake_input(d, X.KeyPress, code); d.sync(); time.sleep(0.1)
for _ in range(abs(steps)):
    xtest.fake_input(d, X.ButtonPress, button); xtest.fake_input(d, X.ButtonRelease, button); d.sync(); time.sleep(0.15)
if ctrl:
    xtest.fake_input(d, X.KeyRelease, code); d.sync()
print(f"wheel {'down' if steps>0 else 'up'} x{abs(steps)} at {x},{y} ctrl={ctrl}")
