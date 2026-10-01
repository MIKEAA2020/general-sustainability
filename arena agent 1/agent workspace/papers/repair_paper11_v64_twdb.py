#!/usr/bin/env python3
"""Join the second detached tail in paper11 v64: Texas Water Development Board.

Dry-run by default; --apply writes the file.

Found by scan_continuations.py, NOT by the gate. The gate reported v64 clean
after the DFO 2009 tail was rejoined, but a second pair was still split:

    L3761  Texas Water Development Board.                  <- head, no title,
                                                              no year
    L3778  Water Data for Texas, well 6837203
           (J-17). https://waterdatafortexas.org/...       <- tail, no author

Seventeen lines apart, because the old splitter sorted head and tail
independently. Neither half is a valid reference on its own, and neither was
visible to K.split-refs: the head does not open with a journal token, and the
tail does not open with one either.

Ground truth: paper10b_edwards_aquifer_v1.tex L1115-1116, where the entry is
intact:

    Texas Water Development Board. Water Data for Texas, well 6837203
    (J-17). https://waterdatafortexas.org/groundwater/well/6837203

The same pair was already repaired in paper09 v32, which is why it looked done.
"""
from __future__ import annotations

import io
import sys

PATH = "/home/user/papers/paper11_forecasting_baselines_v64.tex"

EDITS = [
    # lift the tail out of its independently-sorted position
    ("lift tail",
     "Water Data for Texas, well 6837203\n"
     "(J-17). https://waterdatafortexas.org/groundwater/well/6837203\n",
     "", 1),
    # reattach it to the head
    ("reattach to TWDB head",
     "Texas Water Development Board.\n",
     "Texas Water Development Board. Water Data for Texas, well 6837203\n"
     "(J-17). https://waterdatafortexas.org/groundwater/well/6837203\n", 1),
]


def main() -> int:
    apply = "--apply" in sys.argv
    src = io.open(PATH, encoding="utf-8").read()

    for label, old, new, want in EDITS:
        n = src.count(old)
        if n != want:
            print("  !! %-24s expected %d, found %d -- aborting" % (label, want, n))
            return 2
        src = src.replace(old, new, want)
        print("  ok %-24s (%d)" % (label, n))

    if not apply:
        print("\nDRY RUN - nothing written. Re-run with --apply.")
        return 0
    io.open(PATH, "w", encoding="utf-8").write(src)
    print("applied: %s" % PATH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
