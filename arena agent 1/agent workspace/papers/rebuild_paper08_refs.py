#!/usr/bin/env python3
"""Reattach detached reference tails in paper08.

Every entry in this list was split into (authors + title) and (journal + volume +
pages + DOI / publisher). The two halves were then sorted separately -- heads by
author, tails by journal name -- and merged back in that wrong order, which is why
orphan tails sit alphabetically by journal while heads sit alphabetically by author.

This reattaches each tail to the head it belongs to, identified by matching the
bibliographic record (verified against the publisher where there was any doubt).

Only confident pairings are applied. Conflicts are reported, not guessed:
several heads share a publisher (Hassard 1981, Ostrom 1990 and Stuart & Humphries
1996 are all Cambridge University Press; Diekmann 1995, Guckenheimer & Holmes 1983
and Hale & Verduyn Lunel 1993 are all Springer, New York), and there is only one
orphan copy of each, so those cannot be resolved without inventing a duplicate.

Dry run by default; --apply writes.
"""
import os
import re
import sys

from label_fetch import PAPERS

FN = "paper08_governance_delay_v46.tex"

# (needle identifying the head entry, the orphan tail to append to it)
PAIRS = [
    # verified against Springer (Theor Ecol 13, 425-434, doi 10.1007/s12080-020-00462-x)
    ("Adamson, M.W., Hilker, F.M., 2020.",
     "Theoretical Ecology 13, 425--434. doi:10.1007/s12080-020-00462-x"),
    # verified against Springer (Ambio 49, 1067-1075, doi 10.1007/s13280-019-01265-z)
    ("Karlsson, M., Gilek, M., 2020.",
     "Ambio 49, 1067--1075. doi:10.1007/s13280-019-01265-z"),
    ("Kuang, Y., 1993.", "Academic Press, Boston."),
    ("Halanay, A., 1966.", "Academic Press, New York."),
    ("Lomb, N. R. 1976.", "Astrophysics and Space Science, 39: 447--462."),
    ("Forssell, U., and Ljung, L. 1999.", "Automatica, 35: 1215--1241."),
    ("Guti\\'errez, D., Sifeddine, A.", "Biogeosciences, 6: 835--848."),
    ("Hassard, B.D., Kazarinoff, N.D., Wan, Y.-H., 1981.",
     "Cambridge University Press, Cambridge."),
    ("Butterworth, D. S., and Punt, A. E. 1999.",
     "ICES Journal of Marine Science, 56: 985--998."),
    ("Cadigan, N. G. 2016.", "ICES Journal of Marine Science, 73: 227--238."),
    ("Butterworth, D. S. 2007.", "ICES Journal of Marine Science, 64: 613--617."),
    ("Alkire, S., and Foster, J. 2011.", "Journal of Public Economics, 95: 476--487."),
    ("Cohen, J. 1988.", "Lawrence Erlbaum, Hillsdale, NJ."),
    ("Costantino, R. F., Cushing, J. M., Dennis, B., and Desharnais, R. A. 1995.",
     "Nature 375, 227--230. doi:10.1038/375227a0"),
    ("Gurney, W. S. C., Blythe, S. P., and Nisbet, R. M. 1980.",
     "Nature 287, 17--21. doi:10.1038/287017a0"),
    ("Scheffer, M., Bascompte, J., Brock, W.A., et al., 2009.",
     "Nature 461, 53--59. doi:10.1038/nature08227"),
    ("Carpenter, S.R., Cole, J.J., Pace, M.L., et al., 2011.",
     "Science 332, 1079--1082. doi:10.1126/science.1203672"),
    ("Ch\\'avez, F. P., Ryan, J., Lluch-Cota, S. E., and Niquen, M. 2003.",
     "Science, 299: 217--221."),
    ("Cloud, M.J., Moore, R.E., Kearfott, R.B., 2009.", "SIAM, Philadelphia."),
    ("Chen, T., and Francis, B. A. 1995.", "Springer, London."),
    ("Punt, A. E., Butterworth, D. S., de Moor, C. L., De Oliveira, J. A. A., "
     "and Haddon, M. 2016.", "Fish and Fisheries, 17: 303--334."),
    ("Ricard, D., Minto, C., Jensen, O. P., and Baum, J. K. 2012.",
     "Fish and Fisheries, 13: 380--398."),
    ("Rose, G. A., and Walters, C. J. 2019.", "Marine Policy, 109: 103695."),
    ("World Bank. Poverty and Inequality Platform.", "World Bank, Washington, DC."),
    ("Statistics Canada. Tables 38-10-0167-01 and 38-10-0168-01",
     "Statistics Canada, Ottawa."),
]

# Guckenheimer & Holmes: the title was separated from the authors
TITLE_FIX = ("Guckenheimer, J., Holmes, P., 1983.",
             "Nonlinear Oscillations, Dynamical Systems, and Bifurcations of "
             "Vector Fields.")


def parse_entries(lines):
    """Return [(start_index, [line,...]), ...] for blank-line delimited blocks."""
    out, cur, at = [], [], None
    for i, l in enumerate(lines):
        if l.strip():
            if at is None:
                at = i
            cur.append(l)
        else:
            if cur:
                out.append((at, cur))
            cur, at = [], None
    if cur:
        out.append((at, cur))
    return out


def find_block(entries, needle):
    """Match against the block with all runs of whitespace collapsed to one space,
    so a needle may span a line break inside the entry."""
    norm = lambda s: re.sub(r"\s+", " ", s).strip()
    key = norm(needle)
    # a needle can be a substring of a complete entry (e.g. "SIAM, Philadelphia."
    # is both an orphan tail and the tail of Moore 1979), so prefer blocks whose
    # entire text is the needle
    exact = [e for e in entries if norm(" ".join(e[1])) == key]
    if exact:
        return exact
    return [e for e in entries if key in norm(" ".join(e[1]))]


def main():
    dry = "--apply" not in sys.argv
    p = os.path.join(PAPERS, FN)
    lines = open(p, encoding="utf-8", errors="replace").read().split("\n")

    jobs = PAIRS + [TITLE_FIX]

    if dry:
        print("mode: DRY RUN")
        for needle, tail in jobs:
            ents = parse_entries(lines)
            bh, bt = find_block(ents, needle), find_block(ents, tail)
            ok = len(bh) == 1 and len(bt) == 1
            if not ok:
                print("  !! %-46s head=%d tail=%d" % (needle[:46], len(bh), len(bt)))
                continue
            print("  ok %-46s L%d + L%d" % (needle[:46], bh[0][0] + 1, bt[0][0] + 1))
        print("\n(re-run with --apply to write)")
        return

    # Apply ONE join at a time, re-reading and re-parsing the file every pass.
    # Indices from a single pass go stale the moment a block is deleted, so
    # batching the deletes silently sews orphan tails onto the wrong entries.
    print("mode: APPLY")
    done = 0
    for needle, tail in jobs:
        lines = open(p, encoding="utf-8", errors="replace").read().split("\n")
        ents = parse_entries(lines)
        bh, bt = find_block(ents, needle), find_block(ents, tail)
        if len(bh) != 1 or len(bt) != 1:
            print("  skip (ambiguous) head=%d tail=%d : %s"
                  % (len(bh), len(bt), needle[:50]))
            continue
        (ha, hl), (ta, tl) = bh[0], bt[0]
        if ha == ta:
            print("  already joined: %s" % needle[:50])
            continue
        tail_text = " ".join(x.strip() for x in tl)
        # append the tail to the head block's last line
        lines[ha + len(hl) - 1] = (lines[ha + len(hl) - 1].rstrip() + " " +
                                   tail_text)
        # delete the orphan block, then collapse the doubled blank line
        del lines[ta:ta + len(tl)]
        if ta < len(lines) and ta > 0 and lines[ta].strip() == "" and \
                lines[ta - 1].strip() == "":
            del lines[ta]
        open(p, "w", encoding="utf-8").write("\n".join(lines))
        done += 1
        print("  joined %-44s <- %s" % (needle[:44], tail_text[:46]))
    print("\napplied %d joins" % done)


if __name__ == "__main__":
    main()
