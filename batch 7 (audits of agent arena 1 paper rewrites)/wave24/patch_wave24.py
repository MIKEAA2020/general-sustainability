#!/usr/bin/env python3
"""Wave-24 / Task 102: generate build_latex_v24.py and check_pdf_v41.py
from their wave-23 parents by surgical, fail-loud anchored replacement.

Every anchor is asserted to occur exactly once before replacement, so
any drift in the parent script aborts loudly instead of silently
producing a broken derivative.  The parents are never modified.
"""
from __future__ import annotations

import re
from pathlib import Path

W23 = Path(__file__).resolve().parent.parent / "wave23"
W24 = Path(__file__).resolve().parent


def patch(src_name: str, dst_name: str,
          patches: list[tuple[str, str]],
          regexes: list[tuple[str, str, str]]) -> None:
    src = (W23 / src_name).read_text(encoding="utf-8")
    for old, new in patches:
        assert src.count(old) == 1, (
            f"{src_name}: anchor not unique ({src.count(old)}): "
            f"{old[:90]!r}"
        )
        src = src.replace(old, new)
    for pattern, repl, flags in regexes:
        # re.sub processes backslash escapes in string replacements
        # (\n -> newline, \\ -> backslash); all our regex replacements
        # are plain literals, so pre-double every backslash and let
        # re.sub's unescaping restore it byte-for-byte
        safe = repl.replace("\\", "\\\\")
        new_src, n = re.subn(pattern, safe, src, flags=getattr(re, flags))
        assert n == 1, f"{src_name}: regex matched {n} times: {pattern[:80]}"
        src = new_src
    (W24 / dst_name).write_text(src, encoding="utf-8")
    print(f"  {dst_name}: {len(patches)} anchored patches + "
          f"{len(regexes)} regex patches applied")


VERIFIED_DOIS = [
    "10.1016/0025-5564(90)90019-u",
    "10.1126/science.1203672",
    "10.1016/j.physd.2021.133072",
    "10.1007/s10884-023-10279-x",
    "10.1038/375227a0",
    "10.1145/513001.513002",
    "10.1006/jdeq.1995.1144",
    "10.1038/287017a0",
    "10.1287/mnsc.44.9.1234",
    "10.1016/j.tree.2003.09.002",
    "10.1038/nature08227",
    "10.1007/s11071-013-0928-2",
    "10.2307/1881734",
    "10.1112/jlms/s1-25.3.226",
    "10.1111/j.1749-6632.1948.tb39854.x",
    "10.2307/3939",
]
DOI_LIST_LITERAL = ",\n".join(f'    "{d}"' for d in VERIFIED_DOIS)

# =====================================================================
# 1. build_latex_v24.py  (from build_latex_v23.py)
# =====================================================================
BLD_DOCSTRING = '''#!/usr/bin/env python3
"""Wave-24 / Task 102, part 2: build paper4_delay_dynamics_v41.tex/.pdf
from paper4_delay_dynamics_v41.md (authored by wave24/make_v41.py).

The wave-19/20/21/22/23 pipeline with every fail-loud check inherited,
retargeted to v41 (the DOI insertion round plus the abstract honesty
decision, serving the journal-portal submission zip): the 16
Crossref-verified journal-article DOIs of the Task-100 round
(humanizing audits/V41 Part II: title, container, volume and pages
matched against the manuscript's entries; never guessed) are pasted as
anchored doi: suffixes --- one per reference entry, after the terminal
period --- and the abstract takes Task 97's honesty resolution: "those
studied so far are ecological or informational" with V38's recorded
compensating one-word trim ("the two rules respond oppositely" ->
"the rules respond oppositely"), holding the below-260 bound at 259
journal words.  NOTHING else changes: the Task-98 title stands, the
pointer stays at the unchanged v8 supplement, and the edits are
math-free.

(a) md level: math-span multiset EQUALITY vs v40 (nothing moved); the
cross-reference resolver (every Section-construct number resolves to an
existing heading); the section-reference multiset == v40's; the label
counts unchanged; content numerics == the 16 DOI strings' own digits
EXACTLY (nothing else, verified raw and stripped);
(b) the full inherited needle battery (v33 style markers + frozen v32
scientific claims + v34/v35/v36 devices) PLUS the rotation and E1-E4
sentinels PLUS the dropped-caveat regression gates PLUS the reference/
citation needles PLUS the aligned supplementary pointer PLUS the
wave-23 gate PLUS THE WAVE-24 GATES: the honest abstract form present,
the trimmed phrase absent, and all 16 verified DOIs present in the tex;
(c) the rejection scanner (49 banned strings: the 47 inherited + 2 new
wave-24 regression gates) --- zero hits on markdown AND final LaTeX;
(d) 'if and only if' still exactly 5 times;
(e) tex-level numeric discipline vs the v40 tex by the same stripped
comparison (delta == the 16 DOI strings' digits only), the tex-level
resolver, and the section-order gate (7 < 8 < 9).

Outputs: arena agent 1/paper rewrites/latex/paper4_delay_dynamics_v41.tex
and .pdf.  v40 tex/pdf remain untouched (version discipline).  Run three
times to pin byte-reproducibility.
"""
'''

BLD_HEADER_COMMENT = '''def header_comment(paper: str) -> str:
    return (
        f"% LaTeX source generated from {paper}.md by "
        f"wave24/build_latex_v24.py\\n"
        f"% (batch 7 (audits of agent arena 1 paper rewrites)/wave24; md "
        f"authored by\\n"
        f"% wave24/make_v41.py from paper4_delay_dynamics_v40.md).\\n"
        f"% Task 102, owner-directed: the DOI insertion round plus the "
        f"abstract\\n"
        f"% honesty decision, serving the journal-portal submission "
        f"zip.\\n"
        f"% The 16 Crossref-verified journal-article DOIs (V41 Part II; "
        f"title,\\n"
        f"% container, volume and pages matched; never guessed) are "
        f"pasted as\\n"
        f"% anchored suffixes in the doi form --- the reference list now "
        f"carries 23\\n"
        f"% of them (7 pinned + 16 verified); the frozen gate "
        f"re-baselined\\n"
        f"% v38==v39==v40 -> v41 == v40 + the 16 appends.  The abstract: "
        f"Task 97's\\n"
        f"% phrase flag resolved by the owner (choose honesty) --- the "
        f"opening\\n"
        f"% claim's qualifier list gains 'or informational' (+2 words), "
        f"with V38's\\n"
        f"% recorded compensating one-word trim of the rules-response "
        f"phrase\\n"
        f"% holding the below-260 bound at 259 journal words.  Everything "
        f"else is\\n"
        f"% frozen and machine-verified (all 1,473 math spans "
        f"byte-identical;\\n"
        f"% keywords, declarations, Data availability and figure "
        f"byte-identical;\\n"
        f"% the v8 supplement pointer unchanged).\\n"
        f"% Front matter: Amin Abaee, Independent Researcher, clickable "
        f"ORCID\\n"
        f"%(https://orcid.org/0000-0002-0019-1842) and email "
        f"(amin_abaee@ut.ac.ir)\\n"
        f"% beneath the name; date September 6, 2026.\\n"
        f"% Back matter: the paper's own declarations, each a titled "
        f"subsection, plus\\n"
        f"% the AI declaration (GLM (Z.ai), Qwen (Alibaba Cloud) and "
        f"DeepSeek AI\\n"
        f"% assisted with drafting and iterative review).\\n"
        f"% Edit the markdown source and re-run the build script to "
        f"regenerate.\\n"
        f"% Compiles error-free with tectonic (also compatible with "
        f"pdflatex/xelatex).\\n"
    )
'''

BLD_NUM_BLOCK = (
    "# --- the wave-24 declared numeric deltas: the 16 DOI strings' "
    "digits ---\n"
    "NUM_ADD = Counter()\n"
    "for _d in VERIFIED_DOIS:\n"
    "    NUM_ADD.update(re.findall(r\"\\d+(?:\\.\\d+)?\", _d))\n"
    "NUM_LOST = Counter()"
)

BLD_NEEDLES_TAIL_OLD = '''        # the wave-23 edit gate: the sentence's new form, clause removed
        + ["analysed within one frame. Fisheries supply the motivating "
           "instance"]
    )
}'''
BLD_NEEDLES_TAIL_NEW = '''        # the wave-23 edit gate: the sentence's new form, clause removed
        + ["analysed within one frame. Fisheries supply the motivating "
           "instance"]
        # the wave-24 gates: the honest abstract form and the
        # compensating trim
        + [
            "those studied so far are ecological or informational",
            "Under periodic review the rules respond oppositely",
        ]
        # the wave-24 reference gates: all 16 verified DOIs
        + [f"doi:{d}" for d in VERIFIED_DOIS]
    )
}'''

BLD_BANNED_TAIL_OLD = '''    # wave-23 phantom-strawman regression gates
    "opposed in caricature",
    "in caricature",
    "caricature",
]'''
BLD_BANNED_TAIL_NEW = '''    # wave-23 phantom-strawman regression gates
    "opposed in caricature",
    "in caricature",
    "caricature",
    # wave-24 regression gates: the pre-honesty abstract form (terminal
    # period included, so the new honest form can never match it) and
    # the trimmed phrase must never return
    "those studied so far are ecological.",
    "the two rules respond oppositely",
]'''

BLD_DOI_NOSPACE_GATE_OLD = '''    assert "paper4\\\\_supplementary\\\\_v8.md" in final_flat, (
        f"{paper}: supplementary pointer missing in tex"
    )'''
BLD_DOI_NOSPACE_GATE_NEW = '''    assert "paper4\\\\_supplementary\\\\_v8.md" in final_flat, (
        f"{paper}: supplementary pointer missing in tex"
    )
    # the wave-24 DOI gates, wrapping-tolerant (nospace matching)
    final_nospace = re.sub(r"\\s+", "", final)
    for d in VERIFIED_DOIS:
        assert f"doi:{d}" in final_nospace, (
            f"{paper}: verified DOI missing from tex: {d}"
        )
    assert final_nospace.count("doi:") == 23, (
        f"{paper}: expected 23 doi: suffixes, found "
        f"{final_nospace.count('doi:')}"
    )'''

patch(
    "build_latex_v23.py", "build_latex_v24.py",
    patches=[
        ('PAPERS = ["paper4_delay_dynamics_v40"]',
         'PAPERS = ["paper4_delay_dynamics_v41"]'),
        ('PARENT_MD = "paper4_delay_dynamics_v39"',
         'PARENT_MD = "paper4_delay_dynamics_v40"'),
        ('PARENT_TEX = "paper4_delay_dynamics_v39"',
         'PARENT_TEX = "paper4_delay_dynamics_v40"'),
        ('# --- the wave-23 declared numeric deltas: NONE (the edit is '
         'digit-free) ---\nNUM_ADD = Counter()\nNUM_LOST = Counter()',
         BLD_NUM_BLOCK),
        ('\nV33_STYLE_NEEDLES = [',
         '\nVERIFIED_DOIS = [\n' + DOI_LIST_LITERAL + ',\n]\n\n'
         'V33_STYLE_NEEDLES = ['),
        ('V36_NEEDLES = {\n    "paper4_delay_dynamics_v40": (',
         'V36_NEEDLES = {\n    "paper4_delay_dynamics_v41": ('),
        (BLD_NEEDLES_TAIL_OLD, BLD_NEEDLES_TAIL_NEW),
        (BLD_BANNED_TAIL_OLD, BLD_BANNED_TAIL_NEW),
        ('if "by wave23/build_latex_v23.py" in old:',
         'if "by wave24/build_latex_v24.py" in old:'),
        (BLD_DOI_NOSPACE_GATE_OLD, BLD_DOI_NOSPACE_GATE_NEW),
    ],
    regexes=[
        (r'#!/usr/bin/env python3\n""".*?"""\n', BLD_DOCSTRING, "S"),
        (r'def header_comment\(paper: str\) -> str:\n    return \(\n.*?'
         r'\n    \)\n', BLD_HEADER_COMMENT, "S"),
    ],
)

# =====================================================================
# 2. check_pdf_v41.py  (from check_pdf_v40.py)
# =====================================================================
CHK_DOCSTRING = '''#!/usr/bin/env python3
"""Wave-24 / Task 102, part 3: structural PDF verification of
paper4_delay_dynamics_v41.pdf (PyMuPDF), plus page renders for VLM
verification.

Checks (all fail-loud): the wave-20/21/22/23 battery inherited and
retargeted, PLUS THE WAVE-24 GATES:
1. Page 1: the TITLE (rendered verbatim), byline (name / affiliation /
   clickable ORCID / clickable email), pinned date, the abstract's
   device sentences, keywords; the old title's fragments ABSENT from
   the whole rendered text (retitle regression gates).
2. Exactly the two expected URI annotations on page 1 (orcid.org,
   mailto:).
3. The restructured spine renders in order: Section 7 before Section 8
   before Section 9.
4. The renumbered labels and pointers render (Theorem/Proposition 7.1
   readings, the E1 cross-reference repairs).
5. The E2/E3/E4 completions render.
6. The inherited device and frozen-scientific-claim battery.
7. The wave-21 reference-round needles (Adamson & Hilker lineage +
   echo; the Hocherman citations; both entries with their DOIs).
8. The supplementary-pointer gate: the v8 filename renders; the stale
   v7 pointer is absent.
9. Declarations structure: Data availability + Declaration of
   competing interest as titled subsections; the AI declaration as the
   FINAL subsection with its verbatim text.
10. Figure 1 present exactly once; rejection scan on the rendered text
    (the inherited list + the artifact-class + retitle + wave-23 +
    WAVE-24 regression gates).
11. THE WAVE-23 EDIT GATE (the Section 1.1 sentence in its new form)
    and THE WAVE-24 EDIT GATES: the abstract's honest form ("those
    studied so far are ecological or informational") rendered; the
    pre-honesty form and the trimmed phrase absent everywhere; the
    rendered abstract at 259 journal words (below the 260 bound).
12. THE WAVE-24 REFERENCE GATES: all 16 newly inserted Crossref-verified
    DOIs render in the references; 23 doi: suffixes total in the
    rendered text.
13. Renders pages (1, the abstract page, the Section 1.1 edit page,
    the Section 7 opening, the Section 9 opening, the ecological
    reading, the regime table, the references pages, the
    supplementary-pointer page, the final declarations) to
    wave24/logs/ for VLM verification.
"""
'''

CHK_P12_OLD = '''    "more frequent assessment is not always safer",
    "a local spectral design parameter",
    "grounding scales, not coefficients",
    "Keywords:",'''
CHK_P12_NEW = '''    "more frequent assessment is not always safer",
    "a local spectral design parameter",
    "grounding scales, not coefficients",
    # the wave-24 abstract-honesty gates (the abstract opens on page 1)
    "those studied so far are ecological or informational",
    "Under periodic review the rules respond oppositely",
    "Keywords:",'''

CHK_BODY_DOIS_OLD = '''    "doi:10.1080/02755947.2016.1167145",
    "doi:10.1002/mcf2.10221",
    "doi:10.1139/f94-214",
    "doi:10.1007/BF00182340",'''
CHK_BODY_DOIS_NEW = (
    CHK_BODY_DOIS_OLD + "\n    # the wave-24 reference gates: the 7 "
    "pinned + 16 newly inserted verified DOIs all render\n"
    '    "doi:10.1016/j.jde.2020.03.039",\n'
    + "\n".join(f'    "doi:{d}",' for d in VERIFIED_DOIS)
)

CHK_REJ_OLD = '''    # wave-23 phantom-strawman regression gates: the removed clause and
    # the bare word must stay absent from the rendered text
    "opposed in caricature", "in caricature", "caricature",
]'''
CHK_REJ_NEW = '''    # wave-23 phantom-strawman regression gates: the removed clause and
    # the bare word must stay absent from the rendered text
    "opposed in caricature", "in caricature", "caricature",
    # wave-24 regression gates: the pre-honesty abstract form (terminal
    # period included) and the trimmed phrase must stay absent
    "those studied so far are ecological.",
    "the two rules respond oppositely",
]'''

CHK_EDIT_GATE_OLD = '''    # THE WAVE-23 EDIT GATE: the edited Section 1.1 sentence renders in
    # its new form (clause removed, continuous flow)
    assert has(EDIT_NEW_FORM, full_a, full_b), (
        "the edited sentence's new form missing from rendered text"
    )'''
CHK_EDIT_GATE_NEW = '''    # THE WAVE-23 EDIT GATE: the edited Section 1.1 sentence renders in
    # its new form (clause removed, continuous flow)
    assert has(EDIT_NEW_FORM, full_a, full_b), (
        "the edited sentence's new form missing from rendered text"
    )

    # THE WAVE-24 EDIT GATES: the honest abstract form rendered; the
    # pre-honesty form and the trimmed phrase absent everywhere
    assert has("those studied so far are ecological or informational",
               full_a, full_b), (
        "the honest abstract form missing from rendered text"
    )
    for gone in ("those studied so far are ecological.",
                 "the two rules respond oppositely"):
        assert not has(gone, full_a, full_b), (
            f"the retired phrase rendered: {gone!r}"
        )

    # THE WAVE-24 REFERENCE GATES: all 16 verified DOIs render; 23
    # doi: suffixes total in the rendered text (wrapping-tolerant:
    # both hyphen-break variants, whitespace-stripped)
    nospace_a = re.sub(r"\\s+", "", full_a)
    nospace_b = re.sub(r"\\s+", "", full_b)
    for d in VERIFIED_DOIS:
        assert (f"doi:{d}" in nospace_a or f"doi:{d}" in nospace_b), (
            f"verified DOI missing from rendered text: {d}"
        )
    assert nospace_a.count("doi:") == 23, (
        f"expected 23 doi: suffixes rendered, found "
        f"{nospace_a.count('doi:')}"
    )'''

CHK_DOIS_CONST_OLD = '''AI_TEXT = (
    "GLM (Z.ai), Qwen (Alibaba Cloud) and DeepSeek AI assisted with "
    "drafting and iterative review."
)'''
CHK_DOIS_CONST_NEW = CHK_DOIS_CONST_OLD + '''

VERIFIED_DOIS = [
''' + DOI_LIST_LITERAL + ''',
]'''

patch(
    "check_pdf_v40.py", "check_pdf_v41.py",
    patches=[
        ('PDF = LATEX / "paper4_delay_dynamics_v40.pdf"',
         'PDF = LATEX / "paper4_delay_dynamics_v41.pdf"'),
        (CHK_DOIS_CONST_OLD, CHK_DOIS_CONST_NEW),
        (CHK_P12_OLD, CHK_P12_NEW),
        (CHK_BODY_DOIS_OLD, CHK_BODY_DOIS_NEW),
        (CHK_REJ_OLD, CHK_REJ_NEW),
        (CHK_EDIT_GATE_OLD, CHK_EDIT_GATE_NEW),
        ('out = LOGS / f"v40_{name}.png"',
         'out = LOGS / f"v41_{name}.png"'),
    ],
    regexes=[
        (r'#!/usr/bin/env python3\n""".*?"""\n', CHK_DOCSTRING, "S"),
    ],
)

print("\npatch_wave24: ALL PATCHES APPLIED")
