#!/usr/bin/env python3
"""03_SUPPLEMENTARY_INFORMATION_v2.md -> v3

v46: the cereal-sentinel row in S5.3b was internally inconsistent and
carried an older data vintage.

  * growth reported as 3.11x, while the same section reports
    d ln b_f = +1.128 for the same quantity. e^1.128 = 3.089, so the
    two figures disagreed.
  * the 2022 endpoint was given as 4.21 t/ha. The OWID series shipped
    in the repo gives 4.1826 t/ha for 2022 (4.2283 for 2023), so 4.21
    reflects an older vintage and sits between the two years.

The calibration script run against the repo's own data files gives
1961 = 1.3532, 2022 = 4.1826, ratio 3.0909, d ln = +1.1285 -- which
matches the section's existing log-change exactly.

Fix: 4.21 -> 4.18 and 3.11x -> 3.09x (two places), plus a one-line
note recording the vintage so the next reader can re-derive it.

Source is never overwritten; v3 is a new file.
"""
import io, os

SRC = "/home/user/si.md"
DST = "/home/user/03_SUPPLEMENTARY_INFORMATION_v3.md"

OLD_ROW = "| cereal yield `b_f` (physical, numerator) | 1.35 t/ha | 4.21 t/ha | 3.11× |"
NEW_ROW = "| cereal yield `b_f` (physical, numerator) | 1.35 t/ha | 4.18 t/ha | 3.09× |"

OLD_PROSE = "`b_f` (yield) rose 3.11× while `A_f` (area) rose only 1.17×"
NEW_PROSE = "`b_f` (yield) rose 3.09× while `A_f` (area) rose only 1.17×"

OLD_NOTE = ("the physical cereal sentinel (continuous, no splicing, `d ln b_f = +1.128`) and the measured NFA "
            "cropland\nbiocapacity per area (model units, `d ln b_f = +0.888`); both give the same qualitative "
            "conclusion.")
NEW_NOTE = (OLD_NOTE +
            " The cereal figures above are recomputed from the OWID/FAOSTAT series shipped with this\n"
            "supplement (`cereal_yield_owid.csv`, world aggregate): 1961 = 1.3532 t/ha, 2022 = 4.1826 t/ha,\n"
            "ratio 3.09×, `d ln b_f = +1.1285`. Earlier drafts quoted 4.21 t/ha and 3.11× from an older\n"
            "vintage; the ratio and the log-change now agree, which they did not before.")

PATCHES = [
    (OLD_ROW,   NEW_ROW,   "table row: 4.21 -> 4.18, 3.11x -> 3.09x"),
    (OLD_PROSE, NEW_PROSE, "prose: 3.11x -> 3.09x"),
    (OLD_NOTE,  NEW_NOTE,  "vintage note"),
]

def main():
    s = io.open(SRC, encoding="utf-8", newline="").read()
    for old, new, label in PATCHES:
        if old in s:
            s = s.replace(old, new, 1)
            print(f"ok   {label}")
        else:
            print(f"MISS {label}")
    io.open(DST, "w", encoding="utf-8", newline="").write(s)
    t = io.open(DST, encoding="utf-8", newline="").read()
    print("residual '3.11':", t.count("3.11"), "| residual '4.21':", t.count("4.21"))
    print("lines:", len(t.splitlines()), "| bytes:", os.path.getsize(DST))

if __name__ == "__main__":
    main()
