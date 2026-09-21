#!/usr/bin/env python3
"""
v43 — Environmental Modeling & Assessment (EMA) restructure of paper 1, per the
journal's technical requirements (p1 tech.txt):

1. Insert a "List of abbreviations" section (CES, MSY, PROMETHEE — the
   abbreviations actually used in the text) after Conclusions, before the
   appendices.
2. Rebuild the end-matter "Declarations" block with the seven required entries
   (Ethics approval and consent to participate; Consent for publication;
   Availability of data and materials; Competing interests; Funding;
   Authors' contributions; Acknowledgements) plus the existing brief AI
   declaration, kept last as in v42.
3. Availability of data and materials now points to the figshare deposit
   (10.6084/m9.figshare.33764023), replacing v42's incorrect pointer to the
   superseded Zenodo preprint record; a matching DataCite-style data citation
   is added to the reference list, as the requirements encourage.
4. Authors' contributions and Acknowledgements use the user-specified texts
   ("A.A. conceptualized..." / "Not applicable.").

No other content is modified. v42 is left untouched.
"""

SRC = "/home/user/paper1_assessment_separation_v42.tex"
DST = "/home/user/arena agent 1/paper rewrites/latex/paper1_assessment_separation_v43.tex"

OLD_HEADER = "% Amin Abaee. Revision v42 (JEDC/elsarticle; abstract: weak/strong-sustainability as inline parenthetical glosses). Compiles with tectonic, pdflatex, or xelatex."
NEW_HEADER = "% Amin Abaee. Revision v43 (EMA/elsarticle; Declarations per journal technical requirements; data availability: figshare DOI 10.6084/m9.figshare.33764023). Compiles with tectonic, pdflatex, or xelatex."

APPENDIX_ANCHOR = "\\begin{center}\\rule{0.5\\linewidth}{0.5pt}\\end{center}\n\n\n\\appendix"

LIST_OF_ABBREV = """\\section*{List of abbreviations}\\label{list-of-abbreviations}

\\begin{itemize}
\\item \\textbf{CES} --- constant elasticity of substitution
\\item \\textbf{MSY} --- maximum sustainable yield
\\item \\textbf{PROMETHEE} --- Preference Ranking Organisation Method for Enrichment Evaluation
\\end{itemize}

"""

DATA_REF_ANCHOR = "Abaee, A. (2026). \\emph{Typed flux ledgers and depletion arithmetic: conservation, componentwise diagnostics, and the semantics of depletion horizons}. Zenodo. https://doi.org/10.5281/zenodo.22554177."

DATA_REF_NEW = DATA_REF_ANCHOR + "\n\nAbaee, A. (2026). \\emph{Verification code and figure pipeline for Aggregate Indices and Transition Safety: A Quantifier-Order Separation Between Scalarized and Coordinate-Wise Feasibility}. figshare. https://doi.org/10.6084/m9.figshare.33764023."

OLD_DECLARATIONS = """\\section*{Declarations}

\\subsection*{Data availability statement}

The verification code for the finite rational instance (all 25 checks; deterministic exact-integer arithmetic) is archived at \\url{https://zenodo.org/records/22545740}.

\\subsection*{Declaration of competing interest}

None.

\\subsection*{AI declaration}
GLM (Z.ai), Qwen (Alibaba Cloud) and DeepSeek AI assisted with drafting and iterative review.
"""

NEW_DECLARATIONS = """\\section*{Declarations}\\label{declarations}

\\subsection*{Ethics approval and consent to participate}

Not applicable.

\\subsection*{Consent for publication}

Not applicable.

\\subsection*{Availability of data and materials}

All datasets and code generated and analysed during the current study are available in the figshare repository: the exact-arithmetic verification artifact for the finite rational instance (all 25 checks; deterministic exact-integer arithmetic), the figure-generation code, the manuscript figure files, and the preserved novelty-search strings. \\url{https://doi.org/10.6084/m9.figshare.33764023}

\\subsection*{Competing interests}

The authors declare that they have no competing interests.

\\subsection*{Funding}

Not applicable.

\\subsection*{Authors' contributions}

A.A. conceptualized the entire work, wrote, edited and reviewed the manuscript.

\\subsection*{Acknowledgements}

Not applicable.

\\subsection*{AI declaration}
GLM (Z.ai), Qwen (Alibaba Cloud) and DeepSeek AI assisted with drafting and iterative review.
"""


def replace_once(text, old, new, what):
    n = text.count(old)
    assert n == 1, f"{what}: expected exactly 1 occurrence, found {n}"
    return text.replace(old, new)


def main():
    t = open(SRC, encoding="utf-8").read()

    t = replace_once(t, OLD_HEADER, NEW_HEADER, "header comment")
    t = replace_once(t, APPENDIX_ANCHOR,
                     LIST_OF_ABBREV + APPENDIX_ANCHOR, "appendix anchor")
    t = replace_once(t, DATA_REF_ANCHOR, DATA_REF_NEW, "data reference")
    t = replace_once(t, OLD_DECLARATIONS, NEW_DECLARATIONS, "declarations block")

    assert "22545740" not in t, "stale Zenodo preprint pointer still present"
    assert "33764023" in t
    for required in ["List of abbreviations", "Ethics approval and consent to participate",
                     "Consent for publication", "Availability of data and materials",
                     "Competing interests", "Funding", "Authors' contributions",
                     "Acknowledgements", "AI declaration"]:
        assert required in t, f"missing: {required}"

    open(DST, "w", encoding="utf-8").write(t)
    print(f"wrote {DST} ({len(t)} bytes)")


if __name__ == "__main__":
    main()
