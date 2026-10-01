#!/usr/bin/env python3
"""Reattach one detached bibliography tail in paper11 v64.

Dry-run by default; --apply writes the file.

The gate reports a single fatal finding:

    K.split-refs  L3688  detached tail: no year, and it is the
                         journal/publisher half of an entry whose head is
                         elsewhere

The tail is "Fisheries and Oceans Canada, Ottawa." at L3688. Its head is the
DFO 2009 entry at L3666, four entries away -- the tail sorted under F while its
head sorted under D, because the old merge splitter cut at "period + Word, " and
the sort key was the first 24 alphanumeric characters, so head and tail sorted
independently.

Ground truth is the source chain, where the entry is intact in all three
predecessors (v61 L2382-2383, v62 L2409-2410, v63 L2419-2421):

    DFO, 2009. A fishery decision-making framework incorporating the
    Precautionary Approach. Fisheries and Oceans Canada, Ottawa.

So: delete the orphan paragraph, append it to the head. Nothing else is touched
-- v64 already has one Declarations block and no duplicate references.
"""
from __future__ import annotations

import io
import sys

PATH = "/home/user/papers/paper11_forecasting_baselines_v64.tex"

OLD_HEAD = ("DFO, 2009. A fishery decision-making framework incorporating the\n"
            "Precautionary Approach.\n")
NEW_HEAD = ("DFO, 2009. A fishery decision-making framework incorporating the\n"
            "Precautionary Approach. Fisheries and Oceans Canada, Ottawa.\n")

# the orphan, with the blank line that separates it from the previous entry
ORPHAN = "Fish. Res. 240, 105959.\n\nFisheries and Oceans Canada, Ottawa.\n"
ORPHAN_NEW = "Fish. Res. 240, 105959.\n"


def main() -> int:
    apply = "--apply" in sys.argv
    src = io.open(PATH, encoding="utf-8").read()

    for label, old, new, want in [
        ("delete orphan tail", ORPHAN, ORPHAN_NEW, 1),
        ("reattach to DFO 2009", OLD_HEAD, NEW_HEAD, 1),
    ]:
        n = src.count(old)
        if n != want:
            print("  !! %-24s expected %d, found %d -- aborting" % (label, want, n))
            return 2
        src = src.replace(old, new, want)
        print("  ok %-24s (%d)" % (label, n))

    print()
    print("no other changes made")

    if not apply:
        print("\nDRY RUN - nothing written. Re-run with --apply.")
        return 0
    io.open(PATH, "w", encoding="utf-8").write(src)
    print("applied: %s" % PATH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
