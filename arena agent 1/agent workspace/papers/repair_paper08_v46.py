#!/usr/bin/env python3
"""Terminal repair of paper08_governance_delay_v46.tex.

v46 is the head of that paper and the artifact being posted to Preprints.org
(PAPERS_RESTRUCTURED.md lists it as #5 of the seven, from 8 + 7). It is
terminal, so the "fix the pipeline, not the output" discipline does not apply
here -- and every change below is also what a re-merge would now produce from
the corrected source, so the two cannot diverge.

Three things:

1. Remove 16 duplicated reference entries.
   finalise_paper08_refs.py sliced lines[rule1_i:rule2_i] to lift the
   Supplementary material section out of the bibliography, but in the source
   the second reference chunk sat between the prose and the closing rule, so
   that slice carried the chunk with it. Every entry from Nesic to World Bank
   therefore appears twice: once in the sorted list and once after the
   supplement section. The gate's ref_block() stops at the first rule, which
   is why the duplication was not caught at the time.

2. Fix the supplement pointer. paper4_supplementary_v8.md is the pre-rename
   ancestor of paper08_governance_delay_v46_supplementary_delay.md. Both
   supplement passages are kept -- verified 10/10 and 11/11 against the actual
   .md files -- and each is given the filename of the file it describes.

3. Collapse the two Declarations blocks into one integrated block.
   Preprints.org is not double-blind, so the four "Anonymized for review."
   placeholders from the v50 block are dropped and the substantive v45
   statements are kept. The two Data availability statements describe
   different data (Part I's validated-computation archive; Part II's RAM
   Legacy / DFO CSAS / preregistration record) so BOTH are retained.
   Author contributions is dropped: v45 has none and v50's is a placeholder;
   writing one would be inventing content.

Dry run by default; --apply writes.
"""
import io
import os
import re
import sys

from label_fetch import PAPERS

FN = "paper08_governance_delay_v46.tex"
RULE = r"\begin{center}\rule{0.5\linewidth}{0.5pt}\end{center}"

OLD_PTR = r"\texttt{paper4\_supplementary\_v8.md}"
NEW_PTR = r"\texttt{paper08\_governance\_delay\_v46\_supplementary\_delay.md}"
GOV_PTR = r"\texttt{paper08\_governance\_delay\_v46\_supplementary\_governance.md}"


def main():
    dry = "--apply" not in sys.argv
    p = os.path.join(PAPERS, FN)
    lines = io.open(p, encoding="utf-8", errors="replace").read().split("\n")
    L = lambda n: lines[n - 1]           # 1-based accessor

    # ---- locate the anchors -------------------------------------------------
    refs = next(i for i, l in enumerate(lines)
                if l.startswith(r"\subsection*{References}")) + 1
    sup = next(i for i, l in enumerate(lines)
               if l.startswith(r"\subsection{Supplementary material}")) + 1
    # the rule immediately above the supplement heading, and the next one below.
    # A plain "first rule in the file" picks up rules from the body.
    rule1 = max(i for i in range(refs, sup) if lines[i - 1].strip() == RULE) + 1
    rule2 = next(i for i in range(sup, len(lines))
                 if lines[i].strip() == RULE) + 1
    decls = [i + 1 for i, l in enumerate(lines)
             if l.startswith(r"\section*{Declarations}")]

    print("References heading   L%d" % refs)
    print("rule 1               L%d" % rule1)
    print("Supplementary mat.   L%d" % sup)
    print("rule 2               L%d" % rule2)
    print("Declarations blocks  %s" % decls)

    # ---- 1. the duplicated chunk: entries between end of passage A and rule 2
    #         Passage A ends at the first blank line after the supplement
    #         heading; everything up to rule 2 that looks like a reference is
    #         the duplicate.
    # passage A opens after the heading's blank line and ends at the NEXT
    # blank line; the duplicated references start after that.
    prose = next(i for i in range(sup + 1, rule2) if L(i).strip())
    a_end = next(i for i in range(prose, rule2) if not L(i).strip())
    dup = [i for i in range(a_end + 1, rule2)
           if L(i).strip() and not L(i).strip().startswith('\\')]
    print("\nduplicated reference lines: %d (L%d-L%d)"
          % (len(dup), dup[0], dup[-1]))

    # sanity: every duplicated entry must already exist in the sorted block
    sorted_blk = "\n".join(lines[refs:rule1 - 1])
    missing = []
    cur = []
    for i in range(a_end + 1, rule2):
        if L(i).strip():
            cur.append(L(i).strip())
        else:
            if cur and not cur[0].startswith('\\'):
                ent = re.sub(r"\s+", " ", " ".join(cur))
                probe = re.sub(r"[^a-z0-9]", "", ent.lower())[:60]
                if probe and probe not in re.sub(r"[^a-z0-9]", "",
                                                 sorted_blk.lower()):
                    missing.append(ent[:70])
            cur = []
    print("duplicated entries NOT already in the sorted list: %d" % len(missing))
    for m in missing:
        print("     !! %s" % m)
    if missing:
        print("\nrefusing to delete: some entries would be lost")
        return

    # ---- build the new tail -------------------------------------------------
    head = lines[:a_end]                       # through the end of passage A

    # passage B, with its filename supplied
    pb = []
    for i in range(rule2 + 1, decls[0]):
        if L(i).strip() == RULE:
            continue
        pb.append(L(i))
    # strip the leading rule/blank
    while pb and (not pb[0].strip() or pb[0].strip() == RULE):
        pb.pop(0)
    while pb and not pb[-1].strip():
        pb.pop()
    pb_txt = "\n".join(pb)
    pb_txt = pb_txt.replace(
        r"\textbf{Supplementary material} is deposited with this article "
        "(the accompanying Supplementary file):",
        r"\textbf{Supplementary material for the sampled-governance channel} is "
        "deposited with this article in the accompanying file " + GOV_PTR +
        ": the", 1)

    # ---- declarations: one integrated block --------------------------------
    def subsection(name, start, stop):
        """Text of \subsection*{name} within [start, stop)."""
        for i in range(start, stop):
            if L(i).startswith(r"\subsection*{%s}" % name):
                j = i + 1
                while j < stop and not L(j).startswith('\\'):
                    j += 1
                # i and j are 1-BASED line numbers; lines[] is 0-based
                body = "\n".join(L(k) for k in range(i, j)).strip()
                body = body.split('}', 1)[1].strip() if '}' in body else body
                return body
        return None

    d1, d2 = decls[0], decls[1]
    end_all = len(lines)
    da1 = subsection("Data availability", d1, d2)
    da2 = subsection("Data availability", d2, end_all)
    coi = subsection("Declaration of competing interest", d1, d2)
    fund = subsection("Funding", d1, d2)
    ai = subsection("AI declaration", d1, d2)
    for nm, v in (("Data availability (Part I)", da1),
                  ("Data availability (Part II)", da2),
                  ("Competing interest", coi), ("Funding", fund),
                  ("AI declaration", ai)):
        print("   %-30s %s" % (nm, (v[:58] + '...') if v else "ABSENT"))
    if not all([da1, da2, coi, fund, ai]):
        print("\nrefusing: a declarations subsection could not be located")
        return

    newdecl = [
        r"\section*{Declarations}",
        "",
        r"\subsection*{Data availability}",
        "",
        da1,
        "",
        da2,
        "",
        r"\subsection*{Declaration of competing interest}",
        "",
        coi,
        "",
        r"\subsection*{Funding}",
        "",
        fund,
        "",
        r"\subsection*{AI declaration}",
        "",
        ai,
        "",
    ]

    tail = [""] + pb_txt.split("\n") + [""] + newdecl + [r"\end{document}", ""]

    out = head + tail

    # ---- 2. fix the supplement pointer -------------------------------------
    joined = "\n".join(out)
    assert joined.count(OLD_PTR) == 1, joined.count(OLD_PTR)
    joined = joined.replace(OLD_PTR, NEW_PTR)
    # passage A cites S12 two lines above, and the delay supplement runs to S12
    joined = joined.replace("(S1--S10), together with the MPF",
                            "(S1--S12), together with the MPF", 1)
    out = joined.split("\n")

    print("\nnew length: %d lines (was %d)" % (len(out), len(lines)))
    print("Declarations blocks: %d"
          % sum(1 for l in out if l.startswith(r"\section*{Declarations}")))
    print("stale pointer remaining: %d" % joined.count(OLD_PTR))

    if dry:
        print("\n(re-run with --apply to write)")
        return
    io.open(p, "w", encoding="utf-8").write("\n".join(out))
    print("\nwritten")


if __name__ == "__main__":
    main()
