#!/usr/bin/env python3
"""Drag with Control held: ctrldrag.py X0 Y0 X1 Y1"""
import sys, time
sys.path.insert(0, "/media/Storage/score-learn/scripts")
import capture
from Xlib import X
from Xlib.ext import xtest
x0,y0,x1,y1 = map(int, sys.argv[1:5])
d = capture.dpy()
code = capture.keycode(d, "Control_L")
xtest.fake_input(d, X.KeyPress, code); d.sync(); time.sleep(0.1)
capture.move(d, x0, y0); d.sync(); time.sleep(0.2)
xtest.fake_input(d, X.ButtonPress, 1); d.sync(); time.sleep(0.2)
for i in range(1, 26):
    capture.move(d, x0 + (x1-x0)*i//25, y0 + (y1-y0)*i//25); d.sync(); time.sleep(0.02)
time.sleep(0.2); xtest.fake_input(d, X.ButtonRelease, 1); d.sync(); time.sleep(0.1)
xtest.fake_input(d, X.KeyRelease, code); d.sync()
print(f"ctrl-dragged {x0},{y0} -> {x1},{y1}")
