#!/usr/bin/env python3
"""Wave-19 / Task 93, part 3: structural PDF verification of
paper4_delay_dynamics_v36.pdf (PyMuPDF), plus page renders for VLM
verification.

Checks (all fail-loud):
1. Page 1: title, byline (name / affiliation / clickable ORCID / clickable
   email), pinned date, the abstract's device sentences, keywords.
2. Exactly the two expected URI annotations on page 1 (orcid.org, mailto:).
3. The restructured spine renders in order: Section 7 (The Review
   Interval as Control) before Section 8 (Global Numerics) before
   Section 9 (The Delayed-Recruitment (Maturation-Delay) System).
4. The renumbered labels and pointers render: Theorem/Proposition 7.1
   readings, (Theorem 7.1, Proposition 7.1), Sections 2.3, 9, and 8.3,
   the model of Sections 2-6 and 9, the repaired E1 cross-references.
5. The E2/E3/E4 completions render (delay stages, identification layer,
   parameter-box open task).
6. The inherited device and frozen-scientific-claim battery (v34/v35
   devices with the label renumber, cod record, certification
   discipline, scheme-dependence caveat, mesh-range caveat, DOIs).
7. Declarations structure: Data availability + Declaration of competing
   interest as titled subsections; the AI declaration as the FINAL
   subsection with its verbatim text.
8. Figure 1 present exactly once; rejection scan on the rendered text.
9. Renders pages (1, the Section 7 opening, the Section 9 opening, the
   ecological reading, the regime table, the final declarations) to
   wave19/logs/ for VLM verification.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import fitz  # PyMuPDF

ROOT = Path(__file__).resolve().parents[2]
LATEX = ROOT / "arena agent 1/paper rewrites/latex"
LOGS = Path(__file__).resolve().parent / "logs"
PDF = LATEX / "paper4_delay_dynamics_v36.pdf"

AI_TEXT = (
    "GLM (Z.ai), Qwen (Alibaba Cloud) and DeepSeek AI assisted with "
    "drafting and iterative review."
)

PAGE1_NEEDLES = [
    "Delay-Induced Regime Change in Harvested Stocks",
    "Amin Abaee",
    "Independent Researcher",
    "ORCID: 0000-0002-0019-1842",
    "amin_abaee@ut.ac.ir",
    "September 6, 2026",
    # compressed-abstract devices (the abstract opens on page 1)
    "governance delay",
    "the lag from observed decline to institutional response",
    "the mobilising rule",
    "the protective rule",
]

# the abstract may run onto page 2; these must appear within pages 1-2
PAGES12_NEEDLES = [
    "intermediate delay stabilises the equilibrium",
    "a no-Hopf theorem",
    "discretisation artefact",
    "restabilising only above 6.5 yr through a Neimark",
    "The attractor topology is five-regime",
    "an unverified large-amplitude attractor",
    "more frequent assessment is not always safer",
    "a local spectral design parameter",
    "grounding scales, not coefficients",
    "Keywords:",
    "delay differential equations",
    "renewable resource management",
    "regime shifts",
]

BODY_NEEDLES = [
    # section 1.1 / 2.1 devices
    "The classic results all place the delay inside the ecology itself",
    "Hutchinson (1948) showed",
    "Gurney, Blythe, and Nisbet (1980) gave",
    "Three structural features of (1) carry everything that follows",
    "Depletion filtering",
    "The multiplicative gate.",
    "The institutional delay.",
    "The effort law reads the filtered memory at one fixed lag",
    # the restructured spine and its arc sentence
    "Section 7 treats sample-and-hold review",
    "together they carry the sign separation",
    "not the delay equation sampled at the review interval",
    "7. The Review Interval as Control",
    "8. Global Numerics at Declared Certification Levels",
    "9. The Delayed-Recruitment (Maturation-Delay) System",
    "9.1 The registered system",
    "8.6 The scaffold companion: registered and verified records",
    # renumbered labels / pointers
    "What Theorem 7.1 says",
    "What Proposition 7.1 says",
    "(Theorem 7.1, Proposition 7.1)",
    "Sections 2.3, 9, and 8.3",
    "the model of Sections 2",
    "relocated from Sections 8.3 and 10.4",
    # E1 repairs
    "subcritical (Section 5.2)",
    "mobilising weight (Section 5.4)",
    "provably not a Hopf of the continuous system (Sections 6.2 and 6.4)",
    # E2 / E4 completions
    "Identification is its own layer",
    "latent structural parameters",
    "a reduced compression of the observation, assessment, decision, "
    "deployment, and compliance stages",
    "what the single lag absorbs is their composite timing",
    # E3 completion
    "A third stated open task is parameter-box certification",
    "the one-at-a-time windows of Section 8.5 are not boxes",
    # section 5/7 devices and grok fixes (label-renumbered)
    "Its behavioural reading is direct",
    "the review cadence",
    "the length of time between successive assessments",
    "Governance warning",
    "Management caution",
    "if and only if",
    # section 8.2 regime table
    "Regime",
    "Delay range",
    "Attractor record",
    "closed at the fold",
    "a basin boundary inside this window, not a fold",
    # section 11 devices
    "the two rules carry opposite mathematics",
    "The harvest control rule in force between assessments",
    "tipping point for cycles",
    "Inter-assessment stability margin",
    "Two cautions travel with the translation:",
    "Proved theorems",
    "Interval certificates",
    "Declared-status numerical results",
    # frozen scientific claims (sampled across the paper)
    "fell from about 735 kt in the 1991 assessment to about 31 kt in the "
    "1994 assessment",
    "2 July 1992",
    "26 June 2024",
    "A mesh-range caveat is registered with the fine map",
    "they are not a calibration, and no institutional coefficient is "
    "identified from them",
    "other discretisations have different monodromies",
    "The saddle-node-of-periodic-orbits classification remains",
    "The reversed-gain linearisation has loop gain",
    "(H5) non-feedback mass compartments stay outside the delay loop",
    "doi:10.1080/02755947.2016.1167145",
    "doi:10.1002/mcf2.10221",
    "doi:10.1139/f94-214",
    "doi:10.1007/BF00182340",
    "The influence of stock assessment frequency",
    "Effects of altered stock assessment frequency",
    "Lessons for stock assessment from the northern cod collapse",
    "Stock Assessment of Northern Cod (NAFO Divs. 2J3KL) in 2016",
    "The method of Church and Lessard (2022)",
    "The five-regime attractor topology from the two pre-registered "
    "continuation records",
    # the ecological reading
    "11.7 The ecological reading",
    "The exposed life histories are doubly selected",
    "sit in different compartments and",
    "The form of extraction is ecological even where the local mathematics is not",
    "Growth-coupled ecology cannot widen the window",
    "decoupled storage, not growth-coupled ecology, is what can slow the loop",
    "the predicted exposed class, not an illustrative example",
    "11.8 Limitations",
    "11.9 Open problems",
    "the ecological reading of the registered records",
]

REJECTION_SCAN = [
    "mobilizing", "artifact", "stabilizing", "destabilizing",
    "plain name", "stated plainly", "is collected in one display",
    "Global Stability", "narrow window", "saddle-node of limit cycles",
    "non-autonomous and spatial domains", "anchoveta", "sardine",
    "cephalopod", "haddock", "rockfish", "orange roughy",
    "deep-sea teleost", "large sharks", "ICES", "N_min", "12.1",
    "0.2, 0.8", "Fisheries Research",
    "performance of alternative assessment frequencies",
    "Evaluation of management strategy performance",
    "Effects of assessment frequency and harvest control rules",
    # batch-8 coinages
    "Sign Separation Theorem", "viability bleed",
    "phase-stabilisation trap", "administrative hunting", "basin lock-in",
    "A stable eigenvalue is not a stable fishery",
    "A stable eigenvalue is not a sustainable resource system",
]

LIGATURES = {
    "\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl",
    "\ufb03": "ffi", "\ufb04": "ffl",
}


def hyb_variants(s: str) -> tuple[str, str]:
    """Two normalisations of hyphenated line-breaks: (a) the hyphen is a
    soft break of an unhyphenated word (removed); (b) the hyphen is part
    of a real compound (kept).  A needle passes if it appears in either."""
    for k, v in LIGATURES.items():
        s = s.replace(k, v)
    s = re.sub(r"-\s*\n\s*", "<HBRK>", s)
    a = s.replace("<HBRK>", "")
    b = s.replace("<HBRK>", "-")
    return re.sub(r"\s+", " ", a), re.sub(r"\s+", " ", b)


def flat(s: str) -> str:
    a, _ = hyb_variants(s)
    return a


def has(nd: str, va: str, vb: str) -> bool:
    return nd in va or nd in vb


def main() -> int:
    doc = fitz.open(PDF)
    n_pages = doc.page_count
    print(f"  pages: {n_pages}")

    p1_a, p1_b = hyb_variants(doc[0].get_text())
    for nd in PAGE1_NEEDLES:
        assert has(nd, p1_a, p1_b), f"page-1 needle missing: {nd!r}"

    p12_a, p12_b = hyb_variants(doc[0].get_text() + doc[1].get_text())
    for nd in PAGES12_NEEDLES:
        assert has(nd, p12_a, p12_b), f"pages-1-2 needle missing: {nd!r}"

    uris = sorted(
        a.get("uri", "") for a in doc[0].get_links() if a.get("uri")
    )
    assert uris == [
        "https://orcid.org/0000-0002-0019-1842",
        "mailto:amin_abaee@ut.ac.ir",
    ], f"unexpected page-1 URI annotations: {uris}"

    # abstract word cap on the rendered text layer (pages 1-2, up to
    # the Keywords line)
    raw12 = " ".join(doc[i].get_text() for i in range(2))
    abs_txt = raw12.split("Abstract", 1)[1].split("Keywords:")[0]
    abs_txt = re.sub(r"-\s+", "-", abs_txt)  # rejoin hyphen line-breaks
    abs_w = sum(1 for w in re.findall(r"\S+", abs_txt)
                if re.search(r"[A-Za-z0-9]", w))
    assert abs_w <= 259, f"rendered abstract runs {abs_w} words"
    print(f"  rendered abstract: {abs_w} journal words (cap 259)")

    full_a, full_b = hyb_variants(
        "".join(doc[i].get_text() for i in range(n_pages))
    )
    full = full_a
    for nd in BODY_NEEDLES:
        assert has(nd, full_a, full_b), f"body needle missing: {nd!r}"

    # the restructured spine must appear in this order in the body
    o1 = full.find("7. The Review Interval as Control")
    o2 = full.find("8. Global Numerics at Declared Certification Levels")
    o3 = full.find("9. The Delayed-Recruitment (Maturation-Delay) System")
    assert 0 <= o1 < o2 < o3, f"spine order gate failed: {o1}, {o2}, {o3}"
    # ... and after the two channel sections
    o5 = full.find("5. The Mobilising Channel")
    o6 = full.find("6. The Protective Channel")
    assert 0 <= o5 < o6 < o1, "channel sections do not precede Section 7"

    # rejection scan on the rendered text layer (both hyphen forms)
    hits = [b for b in REJECTION_SCAN if has(b, full_a, full_b)]
    assert not hits, f"rejection-list hits in rendered PDF text: {hits}"

    # figure count: exactly one Figure 1 caption
    assert full.count("Figure 1:") == 1, "Figure 1 caption not unique"

    # declarations: AI declaration last, verbatim, on the final pages
    tail = flat("".join(doc[i].get_text() for i in range(n_pages - 3, n_pages)))
    assert "Declarations" in tail, "Declarations section not in final pages"
    assert "Data availability" in tail and (
        "Declaration of competing interest" in tail
    ), "declaration subsections missing"
    assert "AI declaration" in tail, "AI declaration missing"
    assert AI_TEXT in tail, "AI declaration text not verbatim"
    ai_pos = tail.rfind(AI_TEXT)
    assert ai_pos > tail.rfind("Declaration of competing interest"), (
        "AI declaration is not the final declaration subsection"
    )

    # locate the device pages for rendering
    def page_of(needle: str) -> int:
        for i in range(n_pages):
            if needle in flat(doc[i].get_text()):
                return i
        return -1

    sec7_page = page_of("7. The Review Interval as Control")
    sec9_page = page_of("9. The Delayed-Recruitment (Maturation-Delay) System")
    regime_page = page_of("Attractor record")
    eco_page = page_of("The exposed life histories are doubly selected")
    assert sec7_page >= 0, "Section 7 opening page not found"
    assert sec9_page >= 0, "Section 9 opening page not found"
    assert regime_page >= 0, "regime-table page not found"
    assert eco_page >= 0, "ecological-reading page not found"
    renders = {
        "p1_byline_abstract": 0,
        "p_sec7_review_interval": sec7_page,
        "p_sec9_maturation": sec9_page,
        "p_ecological_reading": eco_page,
        "p_regime_table": regime_page,
        "p_final_declarations": n_pages - 1,
    }
    for name, idx in renders.items():
        pix = doc[idx].get_pixmap(dpi=110)
        out = LOGS / f"v36_{name}.png"
        pix.save(out)
        print(f"  rendered {out.name} (pdf page {idx + 1})")

    print(
        f"  ALL PDF CHECKS PASS: {len(PAGE1_NEEDLES)} page-1 needles, "
        f"{len(BODY_NEEDLES)} body needles, spine order 5<6<7<8<9 "
        f"verified, 2 URI annotations, 0 rejection hits "
        f"({len(REJECTION_SCAN)} banned strings), AI declaration last; "
        f"Section 7 opens on pdf page {sec7_page + 1}, Section 9 on "
        f"pdf page {sec9_page + 1}, regime table on pdf page "
        f"{regime_page + 1}, ecological reading on pdf page "
        f"{eco_page + 1}, declarations end on page {n_pages}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
