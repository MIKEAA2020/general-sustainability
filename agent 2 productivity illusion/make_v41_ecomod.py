#!/usr/bin/env python3
"""make_v41_ecomod.py — ECOMOD v40 -> v41 supplementary-list removal.

Owner directive (follow-up to the Task-125 declarations round): the five
bullet supplementary-file points listed directly under the References are
part of the lengthy "(Data availability.)" statement the owner ordered
deleted in v40 --- that paragraph closed with "(Supplementary material.)
A supplementary package accompanies this manuscript.", the very sentence
that introduced this itemize block. v40 deleted the lead-in but retained
the list; the owner now confirms the list itself is a remnant of the
deleted statement. Independent grounds, all verified against v40:

  R1  Orphaned: the block hangs directly after the References with no
      introducing sentence (its lead-in was deleted in v40).
  R2  Duplicate declaration: the DATA_AVAILABILITY.md bullet is itself a
      second data-availability statement ("data & code availability
      statement (Zenodo / GitHub release)") --- precisely the duplication
      the owner's deletion directive targeted.
  R3  Portal-meaningless paths: the bullets cite repo-internal paths
      (supplementary/...) that do not exist in the flattened Editorial
      Manager upload layout; EM renames and flattens all uploads.
  R4  Upload artifacts, not manuscript content: the ABSTRACT_submission.tex
      bullet references the EM abstract upload item; the SI package is
      uploaded as separate EM items per the submission recipe, and the
      body's S-pointers (Supplementary S5.x etc.) reference the SI
      independently of this list.

Op (family discipline: anchored, asserted, exact-match; fails loudly):

  S1  The orphaned supplementary-material itemize block (5 items:
      SUPPLEMENTARY_information_v2.md, FIGURES/ S1--S15,
      REPRODUCTION_GUIDE.md, DATA_AVAILABILITY.md, ABSTRACT_submission.tex)
      deleted ENTIRELY --- from its \\begin{itemize} through its
      \\end{itemize} --- leaving References to run straight into the
      Declarations section.

No scientific content changed: everything outside the block (and the new
provenance header) is asserted byte-identical to v40.
"""
import sys

SRC = "manuscript_ECOMOD_v40.tex"
DST = "manuscript_ECOMOD_v41.tex"


def main():
    with open(SRC, encoding="ascii") as f:
        src = f.read()
    out = src

    # ---- S1: delete the orphaned supplementary itemize block ---------------
    b_start = ("\\begin{itemize}\n"
               "\\item \\texttt{supplementary/SUPPLEMENTARY\\_information\\_v2.md}")
    b_end = ("--- the abstract as LaTeX (mathematics kept as LaTeX for the "
             "submitted manuscript).\n\\end{itemize}\n\n")
    assert out.count(b_start) == 1, "S1 anchor start not unique"
    assert out.count(b_end) == 1, "S1 anchor end not unique"
    i = out.index(b_start)
    j = out.index(b_end) + len(b_end)
    deleted = out[i:j]
    # the block must be exactly the five supplementary bullets, in order
    assert deleted.count("\\item ") == 5, "S1 block does not hold 5 items"
    for needle in [
        "supplementary/SUPPLEMENTARY\\_information\\_v2.md",
        "supplementary/FIGURES/",
        "supplementary/REPRODUCTION\\_GUIDE.md",
        "supplementary/DATA\\_AVAILABILITY.md",
        "supplementary/ABSTRACT\\_submission.tex",
    ]:
        assert needle in deleted, f"S1 block missing {needle}"
    assert "\\section*{Declarations}" not in deleted, \
        "S1 over-reach: deletion crossed into Declarations"
    assert "Wilson" not in deleted, "S1 over-reach: deletion crossed up into References"
    out = out[:i] + out[j:]
    # seam check: References itemize now runs straight into Declarations
    seam = "\\end{itemize}\n\n\\section*{Declarations}"
    assert out.count(seam) == 1, "S1 seam malformed after deletion"
    print(f"  ok  S1 orphaned supplementary itemize deleted "
          f"({len(deleted)} chars, 5 items)")

    # ---- invariance on the body (before the header insertion) ---------------
    # everything outside the deleted block is byte-identical to v40:
    # (a) preamble/body up to the deleted block
    assert out[:i] == src[:i], "FATAL: content changed before the deleted block"
    # (b) from the Declarations section onward to the end
    assert out[out.index("\\section*{Declarations}"):] == src[j:], \
        "FATAL: content changed after the deleted block"
    print("  ok  body invariant outside the deletion")

    # ---- header provenance ---------------------------------------------------
    v40_anchor = "% v40 (2026-10-04): declarations round per the owner's directives ---"
    v41_block = (
        "% v41 (2026-10-04): supplementary-list removal per the owner's\n"
        "% follow-up --- the five bullet supplementary-file points listed\n"
        "% under the References were the payload of the (Supplementary\n"
        "% material.) sentence that closed the lengthy (Data availability.)\n"
        "% paragraph deleted in v40 (that sentence, the block's lead-in,\n"
        "% was removed then; the list itself is now deleted as the\n"
        "% statement's remnant). The bullets were also redundant with the\n"
        "% Declarations (the DATA_AVAILABILITY.md bullet was itself a\n"
        "% second data-availability statement) and cited repo-internal\n"
        "% paths that do not exist in the flattened Editorial Manager\n"
        "% upload layout. References now run directly into Declarations.\n"
        "% No scientific content changed.\n")
    assert out.count(v40_anchor) == 1, "header anchor not unique"
    out = out.replace(v40_anchor, v41_block + v40_anchor)
    print("  ok  header v41 provenance block")

    # ---- sanity ---------------------------------------------------------------
    try:
        out.encode("ascii")
    except UnicodeEncodeError as e:
        sys.exit(f"FATAL: non-ASCII introduced: {e}")
    print("  ok  pure ASCII")

    # fingerprints: the five rendered repo-internal paths gone everywhere
    # (the preamble \graphicspath entry "supplementary/FIGURES/" is
    # compile-time figure-search plumbing --- invisible in the PDF, part of
    # the v39 portal hardening --- and is deliberately retained)
    for needle in [
        "supplementary/SUPPLEMENTARY\\_information\\_v2.md",
        "\\texttt{supplementary/FIGURES/}",
        "supplementary/REPRODUCTION\\_GUIDE.md",
        "supplementary/DATA\\_AVAILABILITY.md",
        "supplementary/ABSTRACT\\_submission.tex",
        "A supplementary package accompanies this manuscript",
    ]:
        assert out.count(needle) == 0, \
            f"fingerprint {needle!r} still present: {out.count(needle)}"
    # fingerprints: the v40 Declarations block carries over untouched
    for needle, n in [
        (r"\subsection*{Data availability}", 1),
        ("Code and data are available at", 1),
        (r"\subsection*{Funding}", 1),
        ("No funding was received.", 1),
        (r"\subsection*{Competing interests}", 1),
        ("The author declares no competing interests.", 1),
        (r"\subsection*{CRediT authorship contribution statement}", 1),
        (r"\textbf{Amin Abaee:} Conceptualization", 1),
        (r"\subsection*{AI declarations}", 1),
        ("DeepSeek AI and Claude (Anthropic) assisted with", 1),
        ("zenodo.org/records/22554480", 1),
        (r"\section*{References}", 1),
        ("Wilson, E. O. (2016).", 1),
    ]:
        assert out.count(needle) == n, \
            f"fingerprint {needle!r}: {out.count(needle)} != {n}"
    # the reference list itself is intact: item count drops by exactly 5
    n_items_src = src.count("\n\\item ") + (1 if src.startswith("\\item ")
                                            else 0)
    n_items_out = out.count("\n\\item ") + (1 if out.startswith("\\item ")
                                            else 0)
    assert n_items_src - n_items_out == 5, \
        f"item delta {n_items_src - n_items_out} != 5 (must be exactly the 5 bullets)"
    print("  ok  all fingerprints; \\item count down by exactly 5")
    print("  ok  Declarations + References carry over untouched")

    with open(DST, "w", encoding="ascii") as f:
        f.write(out)
    print(f"wrote {DST} ({out.count(chr(10)) + 1} lines; "
          f"v40 had {src.count(chr(10)) + 1})")


if __name__ == "__main__":
    main()
