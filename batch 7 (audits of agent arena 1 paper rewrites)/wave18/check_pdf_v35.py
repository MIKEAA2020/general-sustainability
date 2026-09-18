#!/usr/bin/env python3
"""Wave-18 / Task 91, part 3: structural PDF verification of
paper4_delay_dynamics_v35.pdf (PyMuPDF), plus page renders for VLM
verification.

Checks (all fail-loud):
1. Page 1: title, byline (name / affiliation / clickable ORCID / clickable
   email), pinned date, the abstract's new device sentences, keywords.
2. Exactly the two expected URI annotations on page 1 (orcid.org, mailto:).
3. The new devices render in the text layer: the numbered two-rule contrast,
   the governance-delay naming, the two-default-assumptions sentence, the
   Section 1.1 literature list, the Section 2.1 structural-features list,
   the Section 8 review-cadence naming, the What-this-says readings, the
   Governance warning / Management caution call-outs, the five-regime
   summary table (header + all five rows), the extended translation table
   rows, the two-cautions bullets, the three-tier certification list.
4. The frozen scientific claims sampled across the paper (cod record,
   certification discipline, scheme-dependence caveat, mesh-range caveat,
   references with DOIs).
5. Declarations structure: Data availability + Declaration of competing
   interest as titled subsections; the AI declaration as the FINAL
   subsection with its verbatim text.
6. Figure 1 present exactly once.
7. Renders pages (1, regime-table page, three-tier/declarations page) to
   wave17/logs/ for VLM verification.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import fitz  # PyMuPDF

ROOT = Path(__file__).resolve().parents[2]
LATEX = ROOT / "arena agent 1/paper rewrites/latex"
LOGS = Path(__file__).resolve().parent / "logs"
PDF = LATEX / "paper4_delay_dynamics_v35.pdf"

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
    # section 5/8 devices and grok fixes
    "Its behavioural reading is direct",
    "the review cadence",
    "the length of time between successive assessments",
    "What Theorem 8.1 says",
    "What Proposition 8.1 says",
    "Governance warning",
    "Management caution",
    "if and only if",
    # section 9.2 regime table
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
    # the new Discussion 11.7 (the ecological reading)
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
]


LIGATURES = {
    "\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl",
    "\ufb03": "ffi", "\ufb04": "ffl",
}


def flat(s: str) -> str:
    for k, v in LIGATURES.items():
        s = s.replace(k, v)
    s = re.sub(r"-\s+", "-", s)  # line-breaks at hyphens (e.g. 'large-\namplitude')
    return re.sub(r"\s+", " ", s)


def main() -> int:
    doc = fitz.open(PDF)
    n_pages = doc.page_count
    print(f"  pages: {n_pages}")

    p1 = flat(doc[0].get_text())
    for nd in PAGE1_NEEDLES:
        assert nd in p1, f"page-1 needle missing: {nd!r}"

    p12 = flat(doc[0].get_text() + doc[1].get_text())
    for nd in PAGES12_NEEDLES:
        assert nd in p12, f"pages-1-2 needle missing: {nd!r}"

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

    full = flat("".join(doc[i].get_text() for i in range(n_pages)))
    for nd in BODY_NEEDLES:
        assert nd in full, f"body needle missing: {nd!r}"

    # rejection scan on the rendered text layer
    hits = [b for b in REJECTION_SCAN if b in full]
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
    regime_page = three_tier_page = None
    for i in range(n_pages):
        t = flat(doc[i].get_text())
        if regime_page is None and "Attractor record" in t:
            regime_page = i
        if three_tier_page is None and "Declared-status numerical results" in t:
            three_tier_page = i
    assert regime_page is not None, "regime-table page not found"
    assert three_tier_page is not None, "three-tier-list page not found"

    eco_page = None
    for i in range(n_pages):
        if "The exposed life histories are doubly selected" in flat(doc[i].get_text()):
            eco_page = i
            break
    assert eco_page is not None, "ecological-reading page not found"
    renders = {
        "p1_byline_abstract": 0,
        "p_ecological_reading": eco_page,
        "p_regime_table": regime_page,
        "p_final_declarations": n_pages - 1,
    }
    for name, idx in renders.items():
        pix = doc[idx].get_pixmap(dpi=110)
        out = LOGS / f"v35_{name}.png"
        pix.save(out)
        print(f"  rendered {out.name} (pdf page {idx + 1})")

    print(
        f"  ALL PDF CHECKS PASS: {len(PAGE1_NEEDLES)} page-1 needles, "
        f"{len(BODY_NEEDLES)} body needles, 2 URI annotations, "
        f"0 rejection hits, AI declaration last; regime table on pdf page "
        f"{regime_page + 1}, three-tier list on pdf page "
        f"{three_tier_page + 1}, ecological reading on pdf page "
        f"{eco_page + 1}, declarations end on page {n_pages}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
