#!/usr/bin/env python3
"""make_v40_ecomod.py — ECOMOD v39 -> v40 declarations round.

Owner directives (six), executed verbatim as anchored, exact-match
operations (family discipline: every op asserted to occur exactly once;
the builder fails loudly rather than guessing):

  D1  The back-matter "(Data availability.)" paragraph --- the longer of
      the two data-availability statements, carrying the (Reproducibility.)
      and (Supplementary material.) sentences --- deleted ENTIRELY.
  D2  Declarations / Data availability restated: code and data at the
      Zenodo record 22554480; no new empirical dataset; the only
      empirical inputs are published values used to bound the
      regeneration lag and to demonstrate the composition sign.
  D3  Funding: "No funding was received."
  D4  Competing interests: "The author declares no competing interests."
  D5  The generative-AI subsection retitled "AI declarations" (from
      "Declaration of generative AI and AI-assisted technologies in the
      writing process") and restated: DeepSeek AI and Claude (Anthropic)
      assisted with computational-reproducibility checks under the
      author's supervision. (Owner wrote "Deepseek"; capitalised to the
      official "DeepSeek" branding --- mechanical proper-noun fix.)
  D6  New CRediT authorship contribution statement: Amin Abaee ---
      Conceptualization; Writing -- original draft; Writing -- review &
      editing. (Placed between Competing interests and AI declarations.)

No scientific content changed: everything before the deleted paragraph and
the supplementary-itemize block between the deletion and the Declarations
section are asserted byte-identical to v39.
"""
import sys

SRC = "manuscript_ECOMOD_v39.tex"
DST = "manuscript_ECOMOD_v40.tex"


def main():
    with open(SRC, encoding="ascii") as f:
        src = f.read()
    out = src

    # ---- D1: delete the longer data-availability paragraph entirely -------
    p_start = r"\noindent\textbf{(Data availability.)}"
    p_end = "accompanies this manuscript.\n\n"
    assert out.count(p_start) == 1, "D1 anchor start not unique"
    assert out.count(p_end) == 1, "D1 anchor end not unique"
    i, j = out.index(p_start), out.index(p_end) + len(p_end)
    deleted = out[i:j]
    assert "twoland" in deleted and "(Reproducibility.)" in deleted
    out = out[:i] + out[j:]
    print(f"  ok  D1 long data-availability paragraph deleted "
          f"({len(deleted)} chars)")

    # ---- header provenance --------------------------------------------------
    v39_anchor = "% v39 (2026-10-04): portal-tex hardening per the owner's directive --- the"
    v40_block = (
        "% v40 (2026-10-04): declarations round per the owner's directives ---\n"
        "% the back-matter (Data availability.) paragraph (the longer of the\n"
        "% two statements, carrying the reproducibility and supplementary-\n"
        "% material sentences) deleted entirely; the Declarations block\n"
        "% restated: Data availability (code and data at Zenodo record\n"
        "% 22554480; no new empirical dataset; only empirical inputs are\n"
        "% published values used to bound the regeneration lag and to\n"
        "% demonstrate the composition sign), Funding (no funding was\n"
        "% received), Competing interests (the author declares no competing\n"
        "% interests), a new CRediT authorship contribution statement\n"
        "% (A.A.: Conceptualization; Writing -- original draft; Writing --\n"
        "% review & editing), and the generative-AI subsection retitled\n"
        "% \"AI declarations\" (DeepSeek AI and Claude (Anthropic) assisted\n"
        "% with computational-reproducibility checks under the author's\n"
        "% supervision). No scientific content changed.\n")
    assert out.count(v39_anchor) == 1, "header anchor not unique"
    out = out.replace(v39_anchor, v40_block + v39_anchor)
    print("  ok  header v40 provenance block")

    # ---- D2: Data availability restated -------------------------------------
    old = ("The code and data supporting the findings are in the accompanying "
           "supplementary package. A version of this manuscript together with "
           "the supplementary package is deposited at "
           "\\url{https://zenodo.org/records/22554480}. This study reports no "
           "new empirical dataset; the only empirical inputs are published "
           "values used to bound the regeneration lag and to demonstrate the "
           "composition sign.")
    new = ("Code and data are available at "
           "\\url{https://zenodo.org/records/22554480}. This study reports no "
           "new empirical dataset; the only empirical inputs are published "
           "values used to bound the regeneration lag and to demonstrate the "
           "composition sign.")
    assert out.count(old) == 1, "D2 old text not unique"
    out = out.replace(old, new)
    print("  ok  D2 Data availability restated")

    # ---- D3: Funding ----------------------------------------------------------
    old = ("This research received no specific grant from any funding agency "
           "in the public, commercial, or not-for-profit sectors.")
    new = "No funding was received."
    assert out.count(old) == 1, "D3 old text not unique"
    out = out.replace(old, new)
    print("  ok  D3 Funding restated")

    # ---- D4: Competing interests ---------------------------------------------
    old = ("The author declares that he has no known competing financial "
           "interests or personal relationships that could have appeared to "
           "influence the work reported in this paper.")
    new = "The author declares no competing interests."
    assert out.count(old) == 1, "D4 old text not unique"
    out = out.replace(old, new)
    print("  ok  D4 Competing interests restated")

    # ---- D5 + D6: AI subsection retitled/restated + CRediT inserted ----------
    old = (r"\subsection*{Declaration of generative AI and AI-assisted "
           "technologies in the writing process}" + "\n" +
           "During the preparation of this work the author used AI-assisted "
           "tools for editorial support, including language refinement, "
           "formatting, and computational-reproducibility checks on the "
           "accompanying model code. After using these tools, the author "
           "reviewed and validated the content as needed and takes full "
           "responsibility for the content of the publication.")
    new = (r"\subsection*{CRediT authorship contribution statement}" + "\n" +
           r"\textbf{Amin Abaee:} Conceptualization; Writing -- original "
           r"draft; Writing -- review \& editing." + "\n\n" +
           r"\subsection*{AI declarations}" + "\n" +
           "DeepSeek AI and Claude (Anthropic) assisted with "
           "computational-reproducibility checks under the author's "
           "supervision.")
    assert out.count(old) == 1, "D5/D6 old AI block not unique"
    out = out.replace(old, new)
    print("  ok  D5 AI declarations retitled + restated")
    print("  ok  D6 CRediT statement inserted")

    # ---- invariance + sanity --------------------------------------------------
    try:
        out.encode("ascii")
    except UnicodeEncodeError as e:
        sys.exit(f"FATAL: non-ASCII introduced: {e}")
    print("  ok  pure ASCII")

    marker = "\\begin{document}"
    v39_body = src[src.index(marker):]
    v40_body = out[out.index(marker):]
    # (a) everything up to the deleted paragraph is byte-identical
    cut = v39_body.index(p_start)
    assert v40_body.startswith(v39_body[:cut]), \
        "FATAL: content changed before the deleted paragraph"
    # (b) the supplementary-itemize block (between the deletion and the
    #     Declarations section) is byte-identical
    si = "\\begin{itemize}\n\\item \\texttt{supplementary/SUPPLEMENTARY"
    assert v39_body.count(si) == 1 and v40_body.count(si) == 1
    dec = "\\section*{Declarations}"
    b39 = v39_body[v39_body.index(si):v39_body.index(dec)]
    b40 = v40_body[v40_body.index(si):v40_body.index(dec)]
    assert b39 == b40, "FATAL: supplementary-itemize block changed"
    print("  ok  body invariant outside the six directed edits")
    # (c) directed-edit fingerprints
    for needle, n in [
        ("This study is a mathematical and computational analysis", 0),
        ("(Reproducibility.)", 0),
        ("Declaration of generative AI", 0),
        (r"\subsection*{AI declarations}", 1),
        (r"\subsection*{CRediT authorship contribution statement}", 1),
        ("No funding was received.", 1),
        ("The author declares no competing interests.", 1),
        ("zenodo.org/records/22554480", 1),
        ("assisted with computational-reproducibility checks under the "
         "author's supervision.", 1),
        (r"\textbf{Amin Abaee:} Conceptualization", 1),
    ]:
        assert out.count(needle) == n, f"fingerprint {needle!r}: {out.count(needle)} != {n}"
    print("  ok  all ten directed-edit fingerprints")

    with open(DST, "w", encoding="ascii") as f:
        f.write(out)
    print(f"wrote {DST} ({out.count(chr(10)) + 1} lines; "
          f"v39 had {src.count(chr(10)) + 1})")


if __name__ == "__main__":
    main()
