#!/usr/bin/env python3
"""Second pass on paper08's reference list.

Pass 1 (rebuild_paper08_refs.py) reattached detached tails. That left behind:

  A. bare duplicate heads -- the same work entered twice, once with its tail and
     once stripped of it (Adamson, Karlsson, Shertzer, Brown, Astrom).
  B. orphan tails that duplicate a tail already reattached (Ambio 49, ICES JMS
     64:149, Management Science 44, Nature 287, Nature 375, Prentice Hall).
  C. four entries sitting in a second block after the Supplementary material
     prose (Aiello, Beretka, Carpenter, Brown) instead of in the alphabetical
     list. Aiello, Beretka and Carpenter exist nowhere else and are cited in
     the text, so they are moved, not deleted.

Each deletion is checked against the exact full block text before it is made.

Dry run by default; --apply writes.
"""
import os
import re
import sys

from label_fetch import PAPERS

FN = "paper08_governance_delay_v46.tex"

# (label, exact block text to delete, expected number of occurrences)
DELETE = [
    ("dup Adamson head",
     "Adamson, M. W., and Hilker, F. M. 2020. Resource-harvester cycles caused by "
     "delayed knowledge of the harvested population state can be dampened by "
     "harvester forecasting.", 1),
    ("dup Karlsson head",
     "Karlsson, M., and Gilek, M. 2020. Mind the gap: Coping with delay in "
     "environmental governance.", 1),
    ("dup Shertzer head",
     "Shertzer, K. W., and Prager, M. H. 2007. Delay in fishery management: "
     "diminished yield, longer rebuilding, and increased probability of stock "
     "collapse.", 1),
    # Astrom is handled by START_DELETE below: the accented surname makes an
    # exact literal match fragile, and only the bare duplicate lacks "Prentice".
    ("Brown 2012 without DOI (superseded by the copy that has it)",
     "Brown, C. J., Fulton, E. A., Possingham, H. P., and Richardson, A. J. 2012. "
     "How long can fisheries management delay action in response to ecosystem and "
     "climate change? Ecological Applications, 22: 298--310.", 1),
    # orphan tails that duplicate a tail already reattached
    ("orphan Ambio 49 (Karlsson already has it)", "Ambio, 49: 1067--1075.", 1),
    ("orphan ICES JMS 64:149 (Shertzer already has it)",
     "ICES Journal of Marine Science, 64: 149--159.", 1),
    ("orphan Management Science 44 (Moxnes already has it)",
     "Management Science, 44: 1234--1248.", 1),
    ("orphan Nature 287 (Gurney already has it)", "Nature, 287: 17--21.", 1),
    ("orphan Nature 375 (Costantino already has it)", "Nature, 375: 227--230.", 1),
    ("orphan Prentice Hall (Astrom already has it)",
     "Prentice Hall, Upper Saddle River, NJ.", 1),
]

# (label, block must contain this, block must NOT contain this)
# The Astrom entry appears twice: the main-list copy carries "Prentice Hall",
# the trailing copy is a bare head. Delete the bare one.
START_DELETE = [
    ("dup bare Astrom head",
     "and Wittenmark, B. 1997. Computer-Controlled Systems: Theory and Design, "
     "3rd edn.", "Prentice"),
]

# entries to lift out of the trailing block and insert into the alphabetical list
RELOCATE = [
    ("Aiello",
     "Aiello, W.G., Freedman, H.I., 1990. A time-delay model of single-species "
     "growth with stage structure. Mathematical Biosciences 101(2), 139--153. "
     "doi:10.1016/0025-5564(90)90019-u",
     "after", "Adamson, M.W., Hilker, F.M., 2020."),
    ("Beretka",
     "Beretka, S., Vas, G., 2020. Saddle-node bifurcation of periodic orbits for a "
     "delay differential equation. J. Differ. Equ. 269(5), 4215--4252. "
     "doi:10.1016/j.jde.2020.03.039",
     "after", "Benjamini, Y., and Yekutieli, D. 2001."),
    ("Carpenter 2011",
     "Carpenter, S.R., Cole, J.J., Pace, M.L., et al., 2011. Early warnings of "
     "regime shifts: a whole-ecosystem experiment. Science 332, 1079--1082. "
     "doi:10.1126/science.1203672",
     "before", "Ch\\'avez, F. P., Ryan, J., Lluch-Cota, S. E., and Niquen, M. 2003."),
    ("Brown 2012 (with DOI)",
     "Brown, C.J., Fulton, E.A., Possingham, H.P., Richardson, A.J., 2012. How "
     "long can fisheries management delay action in response to ecosystem and "
     "climate change? Ecological Applications 22, 298--310. doi:10.1890/11-0419.1",
     "before", "Butterworth, D. S., and Punt, A. E. 1999."),
]

WRAP = 78


def blocks(lines):
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


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def find(lines, text):
    """Blocks whose normalised text equals `text`."""
    key = norm(text)
    return [e for e in blocks(lines) if norm(" ".join(e[1])) == key]


def wrap(text):
    out, line = [], ""
    for w in text.split():
        if len(line) + len(w) + 1 > WRAP and line:
            out.append(line)
            line = w
        else:
            line = (line + " " + w).strip()
    if line:
        out.append(line)
    return out


def main():
    dry = "--apply" not in sys.argv
    p = os.path.join(PAPERS, FN)
    print("mode: %s\n" % ("DRY RUN" if dry else "APPLY"))

    lines = open(p, encoding="utf-8", errors="replace").read().split("\n")

    print("--- deletions ---")
    for label, text, want in DELETE:
        hits = find(lines, text)
        status = "ok " if len(hits) == want else "!! "
        print("  %s%-52s %d block(s)" % (status, label[:52], len(hits)))
        if len(hits) != want:
            if hits:
                print("      found: %s" % norm(" ".join(hits[0][1]))[:100])
            continue
        if dry:
            continue
        a, bl = hits[0]
        del lines[a:a + len(bl)]
        if a < len(lines) and a > 0 and lines[a].strip() == "" and \
                lines[a - 1].strip() == "":
            del lines[a]

    print("\n--- substring deletions ---")
    for label, has, not_has in START_DELETE:
        hits = [e for e in blocks(lines)
                if has in norm(" ".join(e[1])) and not_has not in norm(" ".join(e[1]))]
        status = "ok " if len(hits) == 1 else "!! "
        print("  %s%-52s %d block(s)" % (status, label[:52], len(hits)))
        if len(hits) == 1 and not dry:
            a, bl = hits[0]
            del lines[a:a + len(bl)]
            if a < len(lines) and a > 0 and lines[a].strip() == "" and \
                    lines[a - 1].strip() == "":
                del lines[a]

    print("\n--- relocations ---")
    for label, text, where, anchor in RELOCATE:
        src = find(lines, text)
        anch = [e for e in blocks(lines)
                if norm(" ".join(e[1])).startswith(norm(anchor)[:40])]
        if len(src) != 1 or len(anch) != 1:
            print("  !! %-24s src=%d anchor=%d" % (label, len(src), len(anch)))
            continue
        print("  ok %-24s %s %s" % (label, where, anchor[:44]))
        if dry:
            continue
        (sa, sl), (aa, al) = src[0], anch[0]
        # remove from its current position
        del lines[sa:sa + len(sl)]
        if sa < len(lines) and sa > 0 and lines[sa].strip() == "" and \
                lines[sa - 1].strip() == "":
            del lines[sa]
        # anchor moved if it sat below the removal
        if aa > sa:
            aa -= len(sl) + 1
        anch = [e for e in blocks(lines)
                if norm(" ".join(e[1])).startswith(norm(anchor)[:40])]
        if len(anch) != 1:
            print("  !! anchor lost after removal: %s" % label)
            continue
        aa, al = anch[0]
        at = (aa + len(al) + 1) if where == "after" else aa
        lines[at:at] = wrap(text) + [""]

    if dry:
        print("\n(re-run with --apply to write)")
        return
    open(p, "w", encoding="utf-8").write("\n".join(lines))
    print("\nwritten")


if __name__ == "__main__":
    main()
