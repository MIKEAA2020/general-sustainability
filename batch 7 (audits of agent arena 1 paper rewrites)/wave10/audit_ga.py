#!/usr/bin/env python3
"""Deterministic layout audit for a wave-10 graphical abstract generator.

Re-executes the generator's drawing body (minus its save/exit tail) and
measures every text's pixel bounding box against: (a) the figure bounds,
(b) every other text (no text-text overlap), (c) the three panel frames.
Usage: python3 audit_ga.py make_ga_pX.py
"""
import sys
from pathlib import Path

import __main__

src_path = Path(sys.argv[1])
src = src_path.read_text()
src = src.split("pdf = STEM.with_suffix")[0]
ns = {"__file__": str(__main__.__file__ if hasattr(__main__, "__file__") else src_path)}
exec(compile(src, src_path.stem + "_body", "exec"), ns)
ax, W, H, RENDER = ns["ax"], ns["W"], ns["H"], ns["RENDER"]

boxes = []
for t in ax.texts:
    bb = t.get_window_extent(RENDER)
    boxes.append((t.get_text()[:40], bb.x0, bb.x1, bb.y0, bb.y1))

def inter(a, b):  # (name, x0, x1, y0, y1); display coords, y down
    return not (a[2] <= b[1] or b[2] <= a[1] or a[4] <= b[3] or b[4] <= a[3])

print(f"{len(boxes)} texts; figure {W}x{H}")
issues = 0
for i in range(len(boxes)):
    name, x0, x1, y0, y1 = boxes[i]
    if x0 < 0 or y0 < 0 or x1 > W or y1 > H:
        print(f"OUT-OF-FIGURE: {name!r} bbox=({x0:.0f},{y0:.0f})-({x1:.0f},{y1:.0f})")
        issues += 1
    for j in range(i + 1, len(boxes)):
        if inter(boxes[i], boxes[j]):
            print(f"TEXT-TEXT OVERLAP: {name!r} vs {boxes[j][0]!r}")
            issues += 1
frames = [("A", 10, 426), ("B", 434, 854), ("C", 862, 1318)]
for name, x0, x1, y0, y1 in boxes:
    if y1 <= 62:  # headline zone at figure bottom (display y measured from bottom)
        continue
    cx = (x0 + x1) / 2
    for (fn, fx0, fx1) in frames:
        if fx0 <= cx <= fx1:
            if x0 < fx0 - 1 or x1 > fx1 + 1:
                print(f"TEXT-CROSSES-EDGE {fn}: {name!r} x=({x0:.0f},{x1:.0f})")
                issues += 1
            break
print("ISSUES:", issues)
sys.exit(1 if issues else 0)
