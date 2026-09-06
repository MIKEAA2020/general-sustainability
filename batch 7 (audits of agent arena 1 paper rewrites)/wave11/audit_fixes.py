#!/usr/bin/env python3
"""Wave-11 targeted verification of the owner-directed GA fixes.

Root cause first: the wave-10 vlines stacker drew each box's line list
BOTTOM-TO-TOP, so every multi-line box in all five graphical abstracts
rendered in REVERSE reading order (bold headline at the bottom). The
owner's two E2 comments exposed it - "zone rule holds ... does not make
sense" quotes the TOP line of the reversed panel-B lower box, and "first
and second sentence should swap" describes the two reversed fragments of
the panel-C margin sentence. All five generators now render vlines lists
in reading order (headline on top, the ECOMOD house convention; stack
geometry unchanged). Reading order across all five is VLM-verified on
the rendered PNGs; this script adds the deterministic checks the
wave-10 auditor lacks (text-vs-strip clearance, box order, positions):

  E2  (a) the panel-B lower box carries the paper's registered sentence
          "zero catch and the moratorium hold the safe set; the critical-zone
          and / cascade rules hold the LRP from itself" in READING order
          (bold headline on top) and no trace of the mangled wave-10 text;
      (b) the panel-C lower box is in the owner-directed margin-first
          order: "the margin good years must supply is" (top) above
          "smaller than the frozen convention implied" (italic grey) above
          the bold "the LRP is protected by good years" (bottom), with the
          wave-10 "they"-wording absent.
  P4  the right column's "review interval T_r (yr, log)" bbox top is
      clear of the protective strip's bottom edge (244) by >= 3 px, and
      the middle column's label is still at its wave-10 position (the
      owner scoped the instruction to the right column).
  P5  the four row labels (prot.exact / prot.Euler / extr.exact /
      extr.Euler) end at x <= 588 (>= 6 px clear of the strips' left
      end at 594) and stay inside the panel B frame (x >= 434).

Usage: python3 wave11/audit_fixes.py   (from the batch-7 directory)
"""
import sys
from pathlib import Path

import __main__

HERE = Path(__file__).resolve().parent
WAVE10 = HERE.parent / "wave10"


def body(path: str):
    src = Path(path).read_text().split("pdf = STEM.with_suffix")[0]
    ns = {"__file__": str(Path(path))}
    exec(compile(src, Path(path).stem + "_body", "exec"), ns)
    return ns


def texts_of(ns):
    R = ns["RENDER"]
    return [(t.get_text(), t.get_window_extent(R)) for t in ns["ax"].texts]

def positions_of(ns):
    return {t.get_text(): t.get_position() for t in ns["ax"].texts}


def find(pairs, s):
    hits = [bb for (t, bb) in pairs if t == s]
    assert hits, f"string not found: {s!r}"
    return hits[0]


issues = 0

# ---------------------------------------------------------------- E2 ----
ns = body(str(WAVE10 / "make_ga_e2.py"))
pairs = texts_of(ns)
find(pairs, "zero catch and the moratorium")
mid_l2 = find(pairs, "hold the safe set; the critical-zone and")
mid_l3 = find(pairs, "cascade rules hold the LRP from itself")
for bad in ("hold the safe set; the critical-", "zone rule holds the LRP itself"):
    assert not [t for (t, _) in pairs if t == bad], f"mangled wave-10 text remains: {bad!r}"
# box geometry: box(446, 96, 394, 74) -> x 446..840, y 96..170
for (name, bb) in (("mid-l2", mid_l2), ("mid-l3", mid_l3)):
    if not (446 <= bb.x0 and bb.x1 <= 840 and 96 <= bb.y0 and bb.y1 <= 170):
        print(f"E2 {name} outside its box: {bb.x0:.1f},{bb.y0:.1f}-{bb.x1:.1f},{bb.y1:.1f}")
        issues += 1
right_l1 = find(pairs, "the margin good years must supply is")
right_l2 = find(pairs, "smaller than the frozen convention implied")
right_l3 = find(pairs, "the LRP is protected by good years")
assert not [t for (t, _) in pairs if t in ("the margin they must supply is smaller",
                                           "than the frozen convention implied")], \
    "wave-10 right-box wording remains"
# swapped order: margin line ABOVE the protected line
if not (right_l1.y0 > right_l3.y1 and right_l2.y0 > right_l3.y1):
    print("E2 right box not in swapped (margin-first) order")
    issues += 1
# box geometry: box(876, 96, 422, 74) -> x 876..1298, y 96..170
for (name, bb) in (("right-l1", right_l1), ("right-l2", right_l2), ("right-l3", right_l3)):
    if not (876 <= bb.x0 and bb.x1 <= 1298 and 96 <= bb.y0 and bb.y1 <= 170):
        print(f"E2 {name} outside its box: {bb.x0:.1f},{bb.y0:.1f}-{bb.x1:.1f},{bb.y1:.1f}")
        issues += 1
print("E2: registered sentence restored; right box swapped to margin-first order; "
      f"box bboxes mid=({mid_l2.x0:.0f},{mid_l2.y0:.0f})-({mid_l3.x1:.0f},{mid_l3.y1:.0f}) "
      f"right=({right_l1.x0:.0f},{right_l1.y0:.0f})-({right_l3.x1:.0f},{right_l1.y1:.0f})")

# ---------------------------------------------------------------- P4 ----
ns = body(str(WAVE10 / "make_ga_p4.py"))
pairs = texts_of(ns)
right = find(pairs, "review interval T_r (yr, log)")
STRIP_BOTTOM = 244.0
if right.y1 >= STRIP_BOTTOM - 3:
    print(f"P4 right label still grazes the strip: top {right.y1:.1f} vs edge {STRIP_BOTTOM}")
    issues += 1
mid = find(pairs, "\u03c4 (yr, log)")
pos = positions_of(ns)["\u03c4 (yr, log)"]
if pos != (715.0, 238.0):  # wave-10 position: centred at y=238
    print(f"P4 middle label moved from its wave-10 position: {pos}")
    issues += 1
print(f"P4: right label top {right.y1:.1f} (strip bottom {STRIP_BOTTOM}, clearance "
      f"{STRIP_BOTTOM - right.y1:.1f}px); middle label unchanged at wave-10 position")

# ---------------------------------------------------------------- P5 ----
ns = body(str(WAVE10 / "make_ga_p5.py"))
pairs = texts_of(ns)
STRIP_LEFT = 594.0
for lbl in ("prot \u00b7 exact", "prot \u00b7 Euler", "extr \u00b7 exact", "extr \u00b7 Euler"):
    bb = find(pairs, lbl)
    if bb.x1 > STRIP_LEFT - 3:
        print(f"P5 label {lbl!r} still rides the strip: right {bb.x1:.1f} vs strip {STRIP_LEFT}")
        issues += 1
    if bb.x0 < 434 + 3:
        print(f"P5 label {lbl!r} leaves panel B frame: left {bb.x0:.1f}")
        issues += 1
    print(f"P5 label {lbl!r}: x {bb.x0:.1f}-{bb.x1:.1f} "
          f"({STRIP_LEFT - bb.x1:.1f}px clear of the strip)")

print("ISSUES:", issues)
sys.exit(1 if issues else 0)
