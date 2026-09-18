#!/usr/bin/env python3
"""Wave-18 / Task 91, part 2: build paper4_delay_dynamics_v35.tex/.pdf from
paper4_delay_dynamics_v35.md (authored by wave18/make_v35.py).

The wave-17 pipeline with every fail-loud check inherited, retargeted to
v35 (owner directive: abstract below 260 words; the meta-commentary
removed; the merited ecological-insights consolidation implemented as the
new Discussion 11.7 with the 11.8/11.9 renumber):

(a) md-level math-subset vs v34: every math span of v35 is byte-identical
    to a v34 span (EMPTY whitelist --- the ecological reading reuses the
    paper's own registered spans verbatim);
(b) the v35 content needles = the full inherited battery (v33 style
    markers where still present + frozen v32 scientific claims + the v34
    device sentinels that survive) PLUS the compressed-abstract sentinels
    PLUS the ecological-reading sentinels PLUS the dropped-caveat
    regression gates;
(c) the rejection scanner (Task-89 fabrications + americanised spellings)
    extended with this round's bans: the meta-commentary phrase, v33's
    announcement sentence, and the regime-table signpost --- zero hits on
    markdown AND final LaTeX;
(d) 'if and only if' still exactly 5 times;
(e) tex-level numeric discipline vs the v34 tex: superset with the single
    declared renumber token 11.9 (longtable column-spec digits stripped
    from both bodies as before).

Outputs: arena agent 1/paper rewrites/latex/paper4_delay_dynamics_v35.tex
and .pdf.  v34 tex/pdf remain untouched (version discipline).  Run three
times to pin byte-reproducibility.
"""
from __future__ import annotations

import hashlib
import re
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PR = ROOT / "arena agent 1/paper rewrites"
LATEX = PR / "latex"
LOGS = Path(__file__).resolve().parent / "logs"
LATEX.mkdir(exist_ok=True)
LOGS.mkdir(exist_ok=True)

PAPERS = ["paper4_delay_dynamics_v35"]

# --- front matter (identical to wave-13/14/15/16) ------------------------------
AUTHOR = (
    "\\author{Amin Abaee\\\\[0.35em]\n"
    "{\\small Independent Researcher}\\\\[0.55em]\n"
    "{\\small\\href{https://orcid.org/0000-0002-0019-1842}"
    "{ORCID: 0000-0002-0019-1842}}\\\\[0.3em]\n"
    "{\\small\\href{mailto:amin\\_abaee@ut.ac.ir}"
    "{amin\\_abaee@ut.ac.ir}}}"
)
DATE = "\\date{September 6, 2026}"
AUTHOR_NEEDLES = (
    "Amin Abaee", "Independent Researcher",
    "\\href{https://orcid.org/0000-0002-0019-1842}"
    "{ORCID: 0000-0002-0019-1842}",
    "\\href{mailto:amin\\_abaee@ut.ac.ir}",
    DATE,
)

# --- back matter (identical to wave-13/14/15/16) --------------------------------
AI_TEXT = (
    "GLM (Z.ai), Qwen (Alibaba Cloud) and DeepSeek AI assisted with "
    "drafting and iterative review."
)
BACK_NEEDLES = (
    "\\section*{Declarations}",
    "\\subsection*{AI declaration}",
    AI_TEXT,
)

DECL_EXACT = {
    "data availability",
    "data availability statement",
    "credit authorship contribution statement",
    "author contributions",
    "funding",
    "declaration of competing interest",
    "conflicts of interest",
}

# --- inherited needle batteries (wave-16) ---------------------------------------
# (a) v33 rewrite markers --- the reader-oriented sentences that must survive
V33_STYLE_NEEDLES = [
    "The delay studied in this paper sits elsewhere",
    "intermediate delay stabilises the equilibrium",
    "subcritical Hopf crossings",
    "oscillatory dynamics are born",
    "What the dynamical-systems literature has not supplied",
    "Two questions follow, and the paper takes up both",
    "It is a hard saturation architecture, not a generic effort law",
    "a phase filter that can either stabilise or destabilise",
    "the calibrated quota-tracking law is the protective direction the loop should take",
    "a controller knob, not a governance recommendation",
    "Where the delay sits determines what it does",
    "The mechanism is available wherever an institution answers an observed decline with a lagged rule",
]
# (b) frozen scientific claims carried from v32 (verbatim)
V32_FROZEN_NEEDLES = [
    "Documented timelines occupy the same scales",
    "northern cod ran from annual assessment with incremental response",
    "The management record supplies the field-scale counterpart",
    "the documented institutional timelines that ground the two timing coordinates",
    "11.4 Documented institutional timelines",
    "the northern cod (NAFO 2J3KL) record is the canonical instance",
    "fell from about 735 kt in the 1991 assessment to about 31 kt in the 1994 assessment",
    "a stock falling by a factor of more than twenty between annual assessments",
    "less frequent assessment reduced relative yield",
    "the empirical counterpart of this paper's reading of",
    "are the subject of the companion sampled-governance paper",
    "not the coefficients of any theorem",
    "(Section 11.5's first stated open task",
    "11.5 Certification levels",
    "they are not a calibration, and no institutional coefficient is identified from them",
    "no clean two-crossing",
    "the review interval is a local spectral design parameter",
    "Local spectral stabilisation is not governance",
    "the restabilisation is a property of review cadence",
    "What can be learned from the collapse of a renewable resource",
    "The influence of stock assessment frequency",
    "Effects of altered stock assessment frequency",
    "Lessons for stock assessment from the northern cod collapse",
    "Stock Assessment of Northern Cod (NAFO Divs. 2J3KL) in 2016",
]
# (c) v34 device sentinels --- the humanizing revision's new devices
V34_DEVICE_NEEDLES = [
    # compressed-abstract sentinels
    "governance delay",
    "the lag from observed decline to institutional response",
    "the mobilising rule",
    "the protective rule",
    "intermediate delay stabilises the equilibrium",
    "two subcritical Hopf crossings",
    "a no-Hopf theorem",
    "discretisation artefact",
    "restabilising only above 6.5 yr through a Neimark--Sacker-type crossing",
    "The attractor topology is five-regime",
    "an unverified large-amplitude attractor",
    "more frequent assessment is not always safer",
    "a local spectral design parameter",
    "grounding scales, not coefficients",
    # surviving v34 devices
    "The classic results all place the delay inside the ecology itself",
    "Three structural features of (1) carry everything that follows",
    "Depletion filtering",
    "The effort law reads the filtered memory at one fixed lag",
    "Its behavioural reading is direct",
    "the review cadence",
    "the length of time between successive assessments",
    "What Theorem 8.1 says",
    "What Proposition 8.1 says",
    "Governance warning",
    "Management caution",
    "Attractor record",
    "the two rules carry opposite mathematics",
    "The harvest control rule in force between assessments",
    "tipping point for cycles",
    "Inter-assessment stability margin",
    "Proved theorems",
    "Interval certificates",
    "Declared-status numerical results",
    "Two cautions travel with the translation:",
    # the ecological reading (new 11.7)
    "11.7 The ecological reading",
    "The exposed life histories are doubly selected",
    "sit in different compartments and produce different cycles",
    "The form of extraction is ecological even where the local mathematics is not",
    "Growth-coupled ecology cannot widen the window",
    "decoupled storage, not growth-coupled ecology, is what can slow the loop",
    "the predicted exposed class, not an illustrative example",
    "the institutional-delay question becomes moot there",
    "the ecological reading of the registered records",
    "11.8 Limitations",
    "11.9 Open problems",
]
# (d) dropped-caveat regression gates (plan III.D)
CAVEAT_NEEDLES = [
    "A mesh-range caveat is registered with the fine map",
    "they are not a calibration, and no institutional coefficient is "
    "identified from them",
    "other discretisations have different monodromies, and the "
    "continuous-delay and periodic-review recommendations are not "
    "interchangeable",
    "(H5) non-feedback mass compartments stay outside the delay loop",
    "The saddle-node-of-periodic-orbits classification remains",
    "The reversed-gain linearisation has loop gain",
    "The stable arm is not generically reachable near the fold",
]
V35_NEEDLES = {
    "paper4_delay_dynamics_v35": (
        V33_STYLE_NEEDLES + V32_FROZEN_NEEDLES + V34_DEVICE_NEEDLES
        + CAVEAT_NEEDLES
    )
}

# --- rejection list (Task-89 joint assessment Part III.D): zero-hit gates -------
BANNED = [
    # gemini's fabricated reference forms (both output variants)
    "performance of alternative assessment frequencies",
    "fisheries management performance: A simulation approach",
    "Evaluation of management strategy performance under variable "
    "assessment intervals",
    "Effects of assessment frequency and harvest control rules",
    "ICES", "Fisheries Research",
    "183, 313", "313–323", "175, 94", "94–105", "42(4),", "843–861",
    # the invented archetype column
    "anchoveta", "sardine", "cephalopod", "haddock", "rockfish",
    "orange roughy", "deep-sea teleost", "large sharks",
    # the invented table cells
    "12.1", "4.5, 12.1", "[4.5,", "0.2, 0.8", "[0.2, 0.8]",
    # the M3-LC channel inversion (gemini's notation)
    "N_min", "N\\_min",
    # title/wording overclaims and the misattributed loop gain
    "Global Stability", "narrow window", "saddle-node of limit cycles",
    "non-autonomous and spatial domains", "pure mobilizing governance",
    # americanised spellings of the paper's register words (stylometric
    # gate against gemini-voice leakage; grok is British-spelled too)
    "mobilizing", "artifact", "stabilizing", "destabilizing",
    # this round's bans (owner items 1-2): the meta-commentary, the
    # announcement sentences, and the abstract word-cap regression phrases
    "plain name",
    "is collected in one display",
    "It has a plain name",
]

RENUMBER_TOKENS = {"11.9"}  # the Discussion renumber: new 11.7 inserted;
                                    # Open problems 11.8 -> 11.9 (11.7/11.8 neutral)

MAKETITLE_SEP = "\n" + r"\maketitle" + "\n\n"
LONGTABLE_SPEC = re.compile(r"\\begin\{longtable\}\[\]\{@{}.*?@\{\}\}", re.S)


def dash_variants(s: str) -> list[str]:
    """A banned string and its pandoc-converted form (en/em dashes become
    '--'/'---' in LaTeX output)."""
    out = [s]
    v = s.replace("–", "--").replace("—", "---")
    if v != s:
        out.append(v)
    return out


def scan_banned(text: str, where: str) -> None:
    hits = []
    for b in BANNED:
        for v in dash_variants(b):
            if v in text:
                hits.append(v)
                break
    assert not hits, f"{where}: rejection-list hits: {hits}"


def header_comment(paper: str) -> str:
    return (
        f"% LaTeX source generated from {paper}.md by "
        f"wave18/build_latex_v18.py\n"
        f"% (batch 7 (audits of agent arena 1 paper rewrites)/wave18; md "
        f"authored by\n"
        f"% wave18/make_v35.py from paper4_delay_dynamics_v34.md via five "
        f"surgical\n"
        f"% edits).\n"
        f"% Task 91, owner-directed: (1) the abstract compressed below 260 "
        f"words\n"
        f"% (258; every claim, number and caveat retained; the "
        f"meta-commentary\n"
        f"% removed); (2) v34's content spine otherwise frozen and "
        f"machine-verified\n"
        f"% (all math spans byte-identical; numeric superset with the single "
        f"declared\n"
        f"% renumber token 11.9); (3) the merited ecological-insights "
        f"consolidation\n"
        f"% as the new Discussion 11.7 'The ecological reading' (four "
        f"findings from\n"
        f"% the paper's own registered records, spans reused verbatim), "
        f"with the\n"
        f"% Discussion renumbered (Limitations 11.8, Open problems 11.9; "
        f"zero live\n"
        f"% cross-references to the old numbers).\n"
        f"% Front matter: Amin Abaee, Independent Researcher, clickable "
        f"ORCID\n"
        f"%(https://orcid.org/0000-0002-0019-1842) and email "
        f"(amin_abaee@ut.ac.ir)\n"
        f"% beneath the name; date September 6, 2026.\n"
        f"% Back matter: the paper's own declarations, each a titled "
        f"subsection, plus\n"
        f"% the AI declaration (GLM (Z.ai), Qwen (Alibaba Cloud) and "
        f"DeepSeek AI\n"
        f"% assisted with drafting and iterative review).\n"
        f"% Edit the markdown source and re-run the build script to "
        f"regenerate.\n"
        f"% Compiles error-free with tectonic (also compatible with "
        f"pdflatex/xelatex).\n"
    )


# --- Unicode -> LaTeX macros (wave-13, unchanged) ------------------------------
SUBMAP = {c: str(i) for i, c in enumerate("₀₁₂₃₄₅₆₇₈₉")}
SUBMAP.update({"₊": "+", "₋": "-"})
SUPMAP = {c: str(i) for i, c in enumerate("⁰¹²³⁴⁵⁶⁷⁸⁹")}
SUPMAP.update({"⁺": "+", "⁻": "-"})

CHARMAP = {
    "§": r"\S{}", "−": r"\ensuremath{-}", "□": r"\ensuremath{\square}",
    "±": r"\ensuremath{\pm}", "×": r"\ensuremath{\times}",
    "·": r"\ensuremath{\cdot}", "≈": r"\ensuremath{\approx}",
    "→": r"\ensuremath{\rightarrow}", "≤": r"\ensuremath{\leq}",
    "≥": r"\ensuremath{\geq}", "≡": r"\ensuremath{\equiv}",
    "∈": r"\ensuremath{\in}", "∞": r"\ensuremath{\infty}",
    "γ": r"\ensuremath{\gamma}", "ε": r"\ensuremath{\varepsilon}",
    "π": r"\ensuremath{\pi}", "β": r"\ensuremath{\beta}",
    "δ": r"\ensuremath{\delta}", "ρ": r"\ensuremath{\rho}",
    "α": r"\ensuremath{\alpha}", "Δ": r"\ensuremath{\Delta}",
    "†": r"\dag{}", "…": r"\ldots{}", "“": "``", "”": "''", "’": "'",
    "é": r"\'e", "á": r"\'a", "í": r"\'i", "ć": r"\'c",
    "ä": r'\"a', "ö": r'\"o', "ü": r'\"u', "ô": r"\^o",
    "ã": r"\~a", "ñ": r"\~n", "Å": r"\AA{}", "ø": r"\o{}", "Ø": r"\O{}",
    "š": r"\v{s}",
}
PHRASES = [
    ("β\u0302", r"\(\hat{\beta}\)"),
    ("γ\u0302", r"\(\hat{\gamma}\)"),
    ("P\u0304", r"\(\bar{P}\)"),
    ("\U0001D49F", r"\(\mathcal{D}\)"),
]


def unicode_fixes(t: str) -> str:
    t = re.sub(
        f"[{''.join(SUPMAP)}]+",
        lambda m: "\\textsuperscript{" + "".join(SUPMAP[c] for c in m.group(0)) + "}",
        t,
    )
    t = re.sub(
        f"[{''.join(SUBMAP)}]+",
        lambda m: "\\textsubscript{" + "".join(SUBMAP[c] for c in m.group(0)) + "}",
        t,
    )
    for old, new in PHRASES:
        t = t.replace(old, new)
    for old, new in CHARMAP.items():
        t = t.replace(old, new)
    return t


def strip_cmds(s: str) -> str:
    s = re.sub(r"\\[a-zA-Z]+", " ", s)
    s = re.sub(r"\\[^a-zA-Z]", " ", s)
    s = re.sub(r"[{}]", " ", s)
    return s


def tokens_numeric(s: str) -> Counter:
    return Counter(re.findall(r"\d+(?:\.\d+)?", s))


def tokens_words(s: str) -> Counter:
    return Counter(w.lower() for w in re.findall(r"[A-Za-z]+", s))


INFRA_WORDS = {
    "figure", "minipage", "verbatim", "longtable", "abstract", "itemize",
    "tabular", "array", "document", "table", "center", "quote",
    "enumerate", "b", "htbp", "width", "declarations",
}

PREAMBLE = r"""\documentclass[11pt]{article}
\usepackage[a4paper,margin=1in]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{booktabs,longtable,array,calc}
\usepackage{xcolor}
\usepackage[colorlinks=true,allcolors=blue!45!black]{hyperref}
\usepackage[font=small,labelfont=bf]{caption}
\usepackage{etoolbox}
\AtBeginEnvironment{longtable}{\small}  % dense data tables
\setlength{\tabcolsep}{4pt}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\setcounter{secnumdepth}{-1}
\emergencystretch=3em
\graphicspath{{../}}
\begin{document}
"""

FIG_RE = re.compile(
    r"\\begin\{figure\}\s*\n\\centering\s*\n\\includegraphics\{([^}]+)\}\s*\n"
    r"\\caption\{Figure (\d+)\}\s*\n\\end\{figure\}\s*\n+\s*"
    r"\\textbf\{Figure (\d+)\.\}[ \t]*(.*?)"
    r"(?=\n\s*\n|\Z)",
    re.S,
)


def fig_repl(m: re.Match) -> str:
    path, n1, n2, cap = m.group(1), m.group(2), m.group(3), m.group(4)
    assert n1 == n2, f"figure number mismatch: {n1} vs {n2}"
    cap = re.sub(r"\s+", " ", cap).strip()
    return (
        "\\begin{figure}[htbp]\n\\centering\n"
        f"\\includegraphics[width=\\linewidth]{{{path}}}\n"
        f"\\caption{{{cap}}}\n\\end{{figure}}"
    )


SUBSEC_RE = re.compile(r"\\subsection\{([^}]+)\}(\\label\{[^}]*\})?", re.S)


def relocate_declarations(tex: str, paper: str) -> tuple[str, list[tuple[str, str]]]:
    spans: list[tuple[int, int, str, str]] = []
    for m in SUBSEC_RE.finditer(tex):
        title_raw = re.sub(r"\s+", " ", m.group(1)).strip()
        key = title_raw.lower()
        if key not in DECL_EXACT and key != "declarations":
            continue
        rest = tex[m.end():]
        b = re.search(r"\\subsection\{|\\section\{|\\begin\{center\}\\rule", rest)
        content = rest[: b.start()] if b else rest
        span_end = m.end() + (b.start() if b else len(rest))
        spans.append((m.start(), span_end, title_raw, content))

    assert spans, f"{paper}: no declaration subsections found"
    moved: list[tuple[str, str]] = []
    for _start, _end, title_raw, content in spans:
        if title_raw.lower() == "declarations":
            raise AssertionError(f"{paper}: unexpected bold-label Declarations form")
        c = content.strip()
        assert "\\subsection{" not in c and "\\section{" not in c, (
            f"{paper}: nested heading inside declaration {title_raw!r}"
        )
        moved.append((title_raw, c))

    for start, end, _t, _c in reversed(spans):
        tex = tex[:start] + tex[end:]

    block = "\\section*{Declarations}\n"
    for title, content in moved:
        block += f"\n\\subsection*{{{title}}}\n\n{content}\n"
    tex = tex.rstrip() + "\n\n" + block
    return tex, moved


def build_paper(paper: str) -> dict:
    src = PR / f"{paper}.md"
    md = src.read_text(encoding="utf-8")

    # 1. fail-loud math check at md level (every span verbatim in v34;
    #    empty whitelist: v35 adds no mathematics of its own --- the
    #    ecological reading reuses the paper's registered spans verbatim)
    t34 = (PR / "paper4_delay_dynamics_v34.md").read_text(encoding="utf-8")
    spans = re.findall(r"\$\$.*?\$\$|\$[^\$\n]+\$", md, flags=re.S)
    missing = [s for s in spans if s not in t34]
    assert not missing, f"{paper}: math spans missing from v34: {missing[:5]}"

    # 1b. rejection scanner at md level
    scan_banned(md, f"{paper} md")

    # 2. pandoc
    r = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "latex"],
        input=md, capture_output=True, text=True, check=True,
    )
    tex = r.stdout

    # 3a. title extraction
    m = re.search(r"\\section\{(.+?)\}(?:\\label\{[^}]*\})?\s*\n", tex, re.S)
    assert m, f"{paper}: no \\section title found"
    title = re.sub(r"\s+", " ", m.group(1)).strip()
    assert "\\" not in title, f"{paper}: title extraction swallowed a command: {title!r}"
    tex = tex[: m.start()] + tex[m.end():]

    # 3b. abstract environment
    m = re.search(r"\\subsection\{Abstract\}(?:\\label\{[^}]*\})?", tex)
    assert m, f"{paper}: no Abstract subsection"
    abs_pos = m.start()
    tex = tex[: m.start()] + "\\begin{abstract}\n" + tex[m.end():]
    terms = [
        mm.start()
        for mm in re.finditer(r"\\textbf\{Keywords:\}|\\subsection\{|\\section\{", tex)
        if mm.start() > abs_pos
    ]
    assert terms, f"{paper}: no abstract terminator found"
    end = min(terms)
    tex = tex[:end] + "\\end{abstract}\n\n" + tex[end:]

    # 3c. figure + caption merge
    expected_figs = len(re.findall(r"!\[Figure", md))
    tex, n_merged = FIG_RE.subn(fig_repl, tex)
    assert n_merged == expected_figs, (
        f"{paper}: merged {n_merged} figures, expected {expected_figs}"
    )
    assert "\\caption{Figure" not in tex, f"{paper}: unmerged figure caption remains"
    assert not re.search(r"\\textbf\{Figure \d+\.\}", tex), f"{paper}: bold figure caption remains"

    # 3d. centred journal-format note
    note = re.search(
        r"(\\textbf\{Prepared in the format[^}]*\}"
        r"|\\emph\{Methodology and case study[^}]*\})",
        tex,
    )
    if note:
        tex = tex.replace(
            note.group(1), "{\\centering\\small " + note.group(1) + "\\par}", 1
        )

    # 3e/3f. literal-star normalisation; Unicode -> macros
    tex = tex.replace("^\\*", "^{\\ast}").replace("_\\*", "_{\\ast}")
    tex = unicode_fixes(tex)
    bad = sorted({c for c in tex if ord(c) > 127})
    assert not bad, f"{paper}: unmapped non-ASCII: {[hex(ord(c)) for c in bad]}"

    # 3g. emphasis mis-parse symptom
    assert not re.search(r"[A-Za-z0-9]\\emph\{[,.:;)]", tex), (
        f"{paper}: emphasis-span mis-parse symptom present"
    )

    # 3h. declaration relocation
    tex, moved = relocate_declarations(tex, paper)

    # 4. integrity checks
    corpus = title + "\n" + tex
    corpus = re.sub(r"\\begin\{longtable\}\[\]\{@{}.*?@\{\}\}", " ", corpus, flags=re.S)
    corpus = re.sub(r"\\rule\{[^}]*\}\{[^}]*\}", " ", corpus)
    corpus = re.sub(r"\\label\{[^}]*\}", " ", corpus)
    corpus = re.sub(r"\\def\\labelenumi[^{]*\{[^}]*\}", " ", corpus)
    corpus = re.sub(r"\\setcounter\{enumi\}\{\d+\}", " ", corpus)
    md_check = unicode_fixes(md)

    fig_nums = [int(n) for n in re.findall(r"!\[Figure (\d+)\]", md_check)]
    marker_re = re.compile(r"^(\s*)\(?([0-9]+|[ivxl]+|[a-z])[.)] +")
    marker_digits: list[int] = []
    marker_words: list[str] = []
    state = "blank"
    in_fence = False
    for line in md_check.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
            state = "blank"
            continue
        if in_fence:
            continue
        if not line.strip():
            state = "blank"
            continue
        if line.startswith("#"):
            state = "blank"
            continue
        lm = marker_re.match(line)
        if lm and state in ("blank", "in_list"):
            tok = lm.group(2)
            if tok.isdigit():
                marker_digits.append(int(tok))
            else:
                marker_words.append(tok)
            state = "in_list"
        elif lm:
            state = "text"
        else:
            if state != "in_list":
                state = "text"

    num_md = tokens_numeric(strip_cmds(md_check))
    for n in marker_digits:
        num_md[str(n)] -= 1
    for n in fig_nums:
        num_md[str(n)] -= 2
    num_tex = tokens_numeric(strip_cmds(corpus))
    assert num_md == num_tex, (
        f"{paper}: numeric-token mismatch: "
        f"md-only={dict((num_md - num_tex).most_common(10))} "
        f"tex-only={dict((num_tex - num_md).most_common(10))}"
    )

    w_md = tokens_words(strip_cmds(md_check))
    for _ in fig_nums:
        w_md["figure"] -= 2
    for w in marker_words:
        w_md[w] -= 1
    w_tex = tokens_words(strip_cmds(corpus))
    lost = w_md - w_tex
    assert not lost, f"{paper}: markdown words lost: {dict(lost.most_common(10))}"
    extras = w_tex - w_md
    extras = Counter({w: c for w, c in extras.items() if w not in INFRA_WORDS})
    assert not extras, (
        f"{paper}: unexpected extra LaTeX words: {dict(extras.most_common(10))}"
    )

    # 5. assemble
    final = (
        header_comment(paper)
        + PREAMBLE
        + f"\\title{{{title}}}\n" + AUTHOR + "\n" + DATE + "\n\\maketitle\n\n"
        + tex.strip()
        + "\n\n\\subsection*{AI declaration}\n" + AI_TEXT + "\n\n\\end{document}\n"
    )
    for needle in AUTHOR_NEEDLES:
        assert needle in final, f"{paper}: author block missing {needle!r}"
    for needle in BACK_NEEDLES:
        assert needle in final, f"{paper}: back matter missing {needle!r}"
    final_flat = re.sub(r"\s+", " ", final)
    for needle in V35_NEEDLES[paper]:
        assert needle in final_flat, (
            f"{paper}: v35 content needle missing: {needle!r}"
        )
    assert final_flat.count("if and only if") == 5, (
        f"{paper}: expected 5 'if and only if', found "
        f"{final_flat.count('if and only if')}"
    )
    assert final_flat.count("governance delay") >= 2, (
        f"{paper}: 'governance delay' should appear at least twice "
        f"(abstract + Section 1.1)"
    )
    # abstract word cap, verified on the LaTeX abstract environment too
    m_abs = re.search(r"\\begin\{abstract\}\n(.*?)\\end\{abstract\}", final, re.S)
    assert m_abs, f"{paper}: no abstract environment in final tex"
    abs_words = sum(
        1 for w in re.findall(r"\S+", m_abs.group(1))
        if re.search(r"[A-Za-z0-9]", w)
    )
    assert abs_words <= 259, f"{paper}: tex abstract runs {abs_words} words"
    scan_banned(final, f"{paper} tex")
    assert final.count("\\section*{Declarations}") == 1, f"{paper}: Declarations section not unique"
    assert "\\thanks" not in final, f"{paper}: thanks footnote present"
    tail_parts = final.rsplit("\n\n\\end{document}", 1)[0].rsplit("\n", 2)
    assert tail_parts[-2] == "\\subsection*{AI declaration}" and tail_parts[-1] == AI_TEXT, (
        f"{paper}: AI declaration is not the final subsection"
    )

    texfile = LATEX / f"{paper}.tex"
    if texfile.exists():
        old = texfile.read_text(encoding="utf-8")
        if "by wave18/build_latex_v18.py" in old:
            assert final == old, f"{paper}: non-idempotent rebuild (output changed)"
        else:
            raise AssertionError(f"{paper}: unrecognised existing tex header")
    texfile.write_text(final, encoding="utf-8")

    # 6. tex-level numeric discipline vs the v34 tex: every frozen token
    #    survives (superset) and no new token VALUE appears except the
    #    declared renumber token 11.9.  Longtable column-spec digits are
    #    pandoc formatting artifacts --- stripped from both bodies.
    v34tex = (LATEX / "paper4_delay_dynamics_v34.tex").read_text(encoding="utf-8")
    v34body_old = v34tex.split(MAKETITLE_SEP, 1)[1]
    v35body = final.split(MAKETITLE_SEP, 1)[1]
    v34body_old = LONGTABLE_SPEC.sub(" ", v34body_old)
    v35body = LONGTABLE_SPEC.sub(" ", v35body)
    t34n = tokens_numeric(strip_cmds(v34body_old))
    t35n = tokens_numeric(strip_cmds(v35body))
    lost_t = {t: c for t, c in t34n.items() if t35n[t] < c and t not in RENUMBER_TOKENS}
    assert not lost_t, f"{paper}: frozen v34 tex numeric tokens lost/reduced: {lost_t}"
    new_t = {t for t in t35n if t not in t34n} - RENUMBER_TOKENS
    assert not new_t, f"{paper}: new tex-level numeric token values: {sorted(new_t)[:10]}"

    rc = subprocess.run(
        ["tectonic", "--keep-logs", str(texfile)],
        cwd=str(LATEX), capture_output=True, text=True,
    )
    runlog = rc.stdout + rc.stderr
    assert rc.returncode == 0, f"{paper}: tectonic failed:\n{runlog[-2000:]}"
    logfile = LATEX / f"{paper}.log"
    assert logfile.exists(), f"{paper}: tectonic log not written"
    logtext = logfile.read_text(errors="replace")
    assert "Missing character" not in logtext, f"{paper}: missing glyphs in PDF"
    errs = [l for l in logtext.splitlines() if l.startswith("! ")]
    assert not errs, f"{paper}: TeX errors: {errs[:5]}"
    overfull = sum(1 for l in logtext.splitlines() if "Overfull \\hbox" in l)
    shutil.move(str(logfile), str(LOGS / f"{paper}.log"))

    pdffile = LATEX / f"{paper}.pdf"
    assert pdffile.exists() and pdffile.stat().st_size > 10_000, f"{paper}: PDF missing/empty"

    pages = 0
    for line in logtext.splitlines():
        if line.startswith("Output written on"):
            pages = int(re.search(r"\((\d+) pages", line).group(1))
    md5 = hashlib.md5(texfile.read_bytes()).hexdigest()
    decls = [t for t, _ in moved]
    return {
        "paper": paper, "md5": md5, "figures": n_merged,
        "overfull": overfull, "pdf_kb": pdffile.stat().st_size // 1024,
        "pages": pages, "decls": decls,
    }


def main() -> int:
    results = []
    for paper in PAPERS:
        info = build_paper(paper)
        results.append(info)
        print(
            f"  {info['paper']}: OK  md5={info['md5'][:10]}  pages={info['pages']}  "
            f"figures={info['figures']}  overfull={info['overfull']}  "
            f"pdf={info['pdf_kb']} KB  decls={info['decls']}"
        )
    print(f"\n{len(results)}/{len(PAPERS)} papers compiled. LaTeX+PDF in: {LATEX}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
