#!/usr/bin/env python3
"""Merge the doubled DFO 2016 entry in paper09 v32.

Dry-run by default; --apply writes the file.

Two entries in the reference list describe the same report:

    DFO, 2016. Stock Assessment of Northern cod (NAFO Divs. 2J3KL) in 2016.
    DFO Can. Sci. Advis. Sec. Sci. Advis. Rep.~2016/026.

    DFO (2016). Stock assessment of Northern cod (NAFO 2J3KL). \emph{Can.
    Sci. Advis. Sec. Sci. Advis. Rep.} 2016/026.

They came from two sources that cite the same work in different house styles.
The test applied was content identity: not byte-identical, but the differences
are pure citation style --

    NAFO Divs. 2J3KL   vs  NAFO 2J3KL
    Stock Assessment    vs  Stock assessment           (case)
    DFO Can. Sci...     vs  \emph{Can. Sci...}         (body named once)

-- with the same body, the same year, and the same report number, 2016/026.
Same report number is decisive: that IS the work. So this is one entry cited
twice, not two entries, and it is merged to one.

The form kept is the fuller one, which is also the form carried by the paper09
source chain (v30 L1961-1962):

    DFO, 2016. Stock Assessment of Northern cod (NAFO Divs. 2J3KL) in 2016.
    DFO Can. Sci. Advis. Sec. Sci. Advis. Rep.~2016/026.

Nothing else in the file changes.
"""
from __future__ import annotations

import io
import sys

PATH = "/home/user/papers/paper09_cod_certification_v32.tex"

OLD = ("DFO, 2016. Stock Assessment of Northern cod (NAFO Divs. 2J3KL) in 2016.\n"
       "DFO Can. Sci. Advis. Sec. Sci. Advis. Rep.~2016/026.\n"
       "\n"
       "DFO (2016). Stock assessment of Northern cod (NAFO 2J3KL). \\emph{Can.\n"
       "Sci. Advis. Sec. Sci. Advis. Rep.} 2016/026.\n")

NEW = ("DFO, 2016. Stock Assessment of Northern cod (NAFO Divs. 2J3KL) in 2016.\n"
       "DFO Can. Sci. Advis. Sec. Sci. Advis. Rep.~2016/026.\n")


def main() -> int:
    apply = "--apply" in sys.argv
    src = io.open(PATH, encoding="utf-8").read()
    n = src.count(OLD)
    if n != 1:
        print("expected 1 occurrence, found %d -- aborting" % n)
        return 2
    src = src.replace(OLD, NEW, 1)
    print("  ok merged DFO 2016 pair (1)")
    if not apply:
        print("\nDRY RUN - nothing written. Re-run with --apply.")
        return 0
    io.open(PATH, "w", encoding="utf-8").write(src)
    print("applied: %s" % PATH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
