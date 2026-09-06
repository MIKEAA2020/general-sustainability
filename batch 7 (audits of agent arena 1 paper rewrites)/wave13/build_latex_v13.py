#!/usr/bin/env python3
"""Wave-13 build: journal-style front/back matter + DOI-carrying references
for the nine papers' LaTeX/PDF.

Owner directive (2026-09-06), four items:
  1. date = September 6, 2026.
  2. ORCID and email in clickable format, all beneath the author name.
  3. AI declaration at the end with the other declarations; each declaration
     a separate title and subsection.
  4. substitute the owner's nine Zenodo DOIs for the placeholder companion
     references (md-level: the eight new versions v15/v22/v16/v14/v23/v13/
     v32/v26 created by wave13/apply_md_doi.py; P4 unchanged at v30).

This is the wave-9/11 pipeline with the front-matter author block replaced
(\\thanks footnote removed; clickable \\href ORCID + email beneath the byline),
the date pinned, and a typesetting-layer relocation: the papers' own
declaration subsections (Data availability / Data Availability Statement /
CRediT / Funding / Author contributions / Declaration of competing interest /
Conflicts of interest; P2's bold-label Declarations paragraph split into
subsections) are moved to a trailing "Declarations" section AFTER the
references and supplementary material, each as its own titled subsection,
with the AI declaration appended as the final subsection. Journal
convention (Elsevier): declarations close the article.

Fail-loud guarantees (all wave-9/11 checks inherited):
  1. Pure-ASCII body, emphasis-mis-parse symptom, figure counts,
     numeric-token multiset EXACTLY equal between markdown and LaTeX body,
     no markdown word lost - the moved declaration text stays inside the
     checked corpus (a pure relocation), so any drift fails the multiset.
  2. The relocated content is byte-identical to the pandoc output (the
     regex extraction is verified by the token checks).
  3. Front-matter needles asserted (name, affiliation, href ORCID, href
     mailto, date); back-matter needles asserted (Declarations section,
     AI-declaration subsection, verbatim AI text).
  4. P4 (md unchanged): the fresh body is asserted identical to the wave-11
     tex body, and the new file equals the old after ONLY the header,
     \\author, \\date, and declaration-relocation substitutions.
  5. Idempotence: a rebuild over wave-13 output is byte-identical.
  6. tectonic compile: exit 0, no 'Missing character', no TeX error lines;
     log archived to wave13/logs/.

Outputs: arena agent 1/paper rewrites/latex/<paper>.tex and .pdf for the
current md versions (new canonical names for the eight bumped papers; the
old-version tex/pdf remain in place - version discipline; P4 regenerates
in place, wave-11 original recoverable at dc1d501). Run twice to pin
reproducibility.
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

PAPERS = [
    "paperE1_cod_forecast_ladder_v15",
    "paperE2_cod_intervention_v22",
    "paperE3_edwards_forecast_ladder_v16",
    "paperE4_edwards_intervention_v14",
    "paper1_assessment_separation_v23",
    "paper2_obstruction_calculus_v13",
    "paper3_material_ledgers_v32",
    "paper4_delay_dynamics_v30",
    "paper5_sampled_governance_v26",
]

# --- front matter (owner-supplied content; directive items 1-2) ---------------
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

# --- back matter (directive item 3) --------------------------------------------
AI_TEXT = (
    "GLM (Z.ai), Qwen (Alibaba Cloud) and DeepSeek AI assisted with "
    "drafting and iterative review."
)
BACK_NEEDLES = (
    "\\section*{Declarations}",
    "\\subsection*{AI declaration}",
    AI_TEXT,
)

# declaration subsection headings (normalized, case-insensitive exact match)
DECL_EXACT = {
    "data availability",
    "data availability statement",
    "credit authorship contribution statement",
    "author contributions",
    "funding",
    "declaration of competing interest",
    "conflicts of interest",
}
P2_DECL_LABELS = ["Funding", "Competing interests",
                  "Data availability", "Code availability"]

# wave-11 author line (for the P4 body-identity substitution check)
W11_AUTHOR = (
    "\\author{Amin Abaee\\thanks{amin\\_abaee@ut.ac.ir; "
    "ORCID: 0000-0002-0019-1842.\\newline "
    "AI declaration: GLM (Z.ai), Qwen (Alibaba Cloud) and DeepSeek AI "
    "assisted with drafting and iterative review.} \\\\ Independent Researcher}"
)


def header_comment(paper: str, wave: int) -> str:
    if wave == 11:
        return (
            f"% LaTeX source generated from {paper}.md by wave11/build_latex_author.py "
            f"(batch 7 (audits of agent arena 1 paper rewrites)/wave11).\n"
            f"% Body byte-identical to the wave9/build_latex.py output (asserted at build time).\n"
            f"% Adds the author front matter: Amin Abaee, Independent Researcher,\n"
            f"% amin_abaee@ut.ac.ir, ORCID 0000-0002-0019-1842, and the AI declaration\n"
            f"% (GLM (Z.ai), Qwen (Alibaba Cloud) and DeepSeek AI assisted with drafting\n"
            f"% and iterative review).\n"
            f"% Edit the markdown source and re-run the build script to regenerate.\n"
            f"% Compiles error-free with tectonic (also compatible with pdflatex/xelatex).\n"
        )
    return (
        f"% LaTeX source generated from {paper}.md by wave13/build_latex_v13.py "
        f"(batch 7 (audits of agent arena 1 paper rewrites)/wave13).\n"
        f"% Pandoc body identical to the wave-9/11 output (asserted at build time), "
        f"with the\n"
        f"% declaration subsections relocated to a trailing Declarations section.\n"
        f"% Front matter: Amin Abaee, Independent Researcher, clickable ORCID\n"
        f"%(https://orcid.org/0000-0002-0019-1842) and email (amin_abaee@ut.ac.ir)\n"
        f"% beneath the name; date September 6, 2026.\n"
        f"% Back matter: the paper's own declarations, each a titled subsection, plus\n"
        f"% the AI declaration (GLM (Z.ai), Qwen (Alibaba Cloud) and DeepSeek AI\n"
        f"% assisted with drafting and iterative review).\n"
        f"% References carry the owner's Zenodo DOIs (see wave13/apply_md_doi.py).\n"
        f"% Edit the markdown source and re-run the build script to regenerate.\n"
        f"% Compiles error-free with tectonic (also compatible with pdflatex/xelatex).\n"
    )


# --- 1. markdown-level fixes (literal-star notation; applied in memory) -----
MD_FIXES: dict[str, list[tuple[str, str, int]]] = {
    "paperE1_cod_forecast_ladder_v15": [
        # the three-part state-equation display is 122pt too wide at 11pt;
        # break before the a(S_t)=cases part (content unchanged)
        (r"""$$
S_{t+1}=\bigl[S_t+g(S_t)-C_t+\varepsilon_t\bigr]_+,
\qquad
g(S_t)=rS_t\bigl(1-S_t/K\bigr)\,a(S_t),
\qquad
a(S_t)=""",
         r"""$$
\begin{gathered}
S_{t+1}=\bigl[S_t+g(S_t)-C_t+\varepsilon_t\bigr]_+,
\qquad
g(S_t)=rS_t\bigl(1-S_t/K\bigr)\,a(S_t),
\\
a(S_t)=""", 1),
        (r"""\end{cases}
$$""",
         r"""\end{cases}
\end{gathered}
$$""", 1),
    ],
    "paperE4_edwards_intervention_v14": [
        ("K*_phys", "$K^{\\ast}_{\\mathrm{phys}}$", 1),
        ("K*_inst", "$K^{\\ast}_{\\mathrm{inst}}$", 1),
        ("B(T) = H* + (618 − H*)/a^T",
         "$B(T) = H^{\\ast} + (618 - H^{\\ast})/a^{T}$", 1),
        ("T_empty(C) = ln((C − H*)/(K* − H*))/ln(1/a)",
         "$T_{\\mathrm{empty}}(C) = \\mathrm{ln}\\bigl((C - H^{\\ast})/(K^{\\ast} - H^{\\ast})\\bigr)/\\mathrm{ln}(1/a)$", 1),
        ("K*", "$K^{\\ast}$", 7),   # remaining sites: L57 x3, L77 x1, L79 x3
        ("H*", "$H^{\\ast}$", 0),   # safety net: all H* consumed by formulas
    ],
    "paperE2_cod_intervention_v22": [
        ("0.5K* (442.3)", "$0.5K^{\\ast}$ (442.3)", 1),
    ],
}

# --- 3b. Unicode -> LaTeX macros --------------------------------------------

SUBMAP = {c: str(i) for i, c in enumerate("₀₁₂₃₄₅₆₇₈₉")}
SUBMAP.update({"₊": "+", "₋": "-"})
SUPMAP = {c: str(i) for i, c in enumerate("⁰¹²³⁴⁵⁶⁷⁸⁹")}
SUPMAP.update({"⁺": "+", "⁻": "-"})

CHARMAP = {
    "§": r"\S{}",
    "−": r"\ensuremath{-}",
    "□": r"\ensuremath{\square}",
    "±": r"\ensuremath{\pm}",
    "×": r"\ensuremath{\times}",
    "·": r"\ensuremath{\cdot}",
    "≈": r"\ensuremath{\approx}",
    "→": r"\ensuremath{\rightarrow}",
    "≤": r"\ensuremath{\leq}",
    "≥": r"\ensuremath{\geq}",
    "≡": r"\ensuremath{\equiv}",
    "∈": r"\ensuremath{\in}",
    "∞": r"\ensuremath{\infty}",
    "γ": r"\ensuremath{\gamma}",
    "ε": r"\ensuremath{\varepsilon}",
    "π": r"\ensuremath{\pi}",
    "β": r"\ensuremath{\beta}",
    "δ": r"\ensuremath{\delta}",
    "ρ": r"\ensuremath{\rho}",
    "α": r"\ensuremath{\alpha}",
    "Δ": r"\ensuremath{\Delta}",
    "†": r"\dag{}",
    "…": r"\ldots{}",
    "“": "``",
    "”": "''",
    "’": "'",
    "é": r"\'e",
    "á": r"\'a",
    "í": r"\'i",
    "ć": r"\'c",
    "ä": r'\"a',
    "ö": r'\"o',
    "ü": r'\"u',
    "ô": r"\^o",
    "ã": r"\~a",
    "ñ": r"\~n",
    "Å": r"\AA{}",
    "ø": r"\o{}",
    "Ø": r"\O{}",
    "š": r"\v{s}",
}

# Combining accents and the script capital, applied before CHARMAP so the
# base glyph is consumed together with its accent.
PHRASES = [
    ("β\u0302", r"\(\hat{\beta}\)"),
    ("γ\u0302", r"\(\hat{\gamma}\)"),
    ("P\u0304", r"\(\bar{P}\)"),
    ("\U0001D49F", r"\(\mathcal{D}\)"),
]


def unicode_fixes(t: str) -> str:
    # sub/superscript runs first (so "10³" and "yr⁻¹" become single groups)
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


# --- integrity-check helpers ------------------------------------------------


def strip_cmds(s: str) -> str:
    s = re.sub(r"\\[a-zA-Z]+", " ", s)
    s = re.sub(r"\\[^a-zA-Z]", " ", s)
    s = re.sub(r"[{}]", " ", s)
    return s


def tokens_numeric(s: str) -> Counter:
    return Counter(re.findall(r"\d+(?:\.\d+)?", s))


def tokens_words(s: str) -> Counter:
    return Counter(w.lower() for w in re.findall(r"[A-Za-z]+", s))


# Words the LaTeX body gains purely from environment/infrastructure names
# (after command stripping, \begin{X} leaves the word "X").
INFRA_WORDS = {
    "figure", "minipage", "verbatim", "longtable", "abstract", "itemize",
    "tabular", "array", "document", "table", "center", "quote",
    "enumerate",  # from \begin{enumerate}
    "b", "htbp", "width",  # from [b], [htbp], width= injected by this build
    "declarations",  # the injected \section*{Declarations} heading (back matter)
}
# Per-paper expected extra words from deliberate math-notation conversions.
ALLOWED_EXTRA_WORDS = {
    "paperE4_edwards_intervention_v14": Counter({"d": 3}),  # \mathcal{D} x3
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


# --- declaration relocation (directive item 3, typesetting layer) -------------

SUBSEC_RE = re.compile(r"\\subsection\{([^}]+)\}(\\label\{[^}]*\})?", re.S)


def split_bold_labels(content: str, paper: str) -> list[tuple[str, str]]:
    """P2's Declarations form: one paragraph of bold-labelled declarations."""
    parts = re.split(r"\\textbf\{([^}]+)\}", content)
    assert parts and parts[0].strip() == "", (
        f"{paper}: Declarations paragraph has text before the first bold label"
    )
    assert len(parts) % 2 == 1, f"{paper}: odd textbf split"
    pairs: list[tuple[str, str]] = []
    for i in range(1, len(parts) - 1, 2):
        label = parts[i].strip()
        body = re.sub(r"\s+", " ", parts[i + 1]).strip()
        assert label.endswith("."), f"{paper}: bold label {label!r} lacks a period"
        pairs.append((label[:-1], body))
    assert [t for t, _ in pairs] == P2_DECL_LABELS, (
        f"{paper}: unexpected bold-label declarations: {[t for t, _ in pairs]}"
    )
    return pairs


def relocate_declarations(tex: str, paper: str) -> tuple[str, list[tuple[str, str]]]:
    """Move the declaration subsections to a trailing Declarations section.

    Pure relocation: the captured content is re-emitted verbatim (P2's
    bold-label paragraph is the one structured re-form, per the owner's
    'separate title and subsection' directive); the token-level checks that
    run afterwards prove nothing was lost or added inside the corpus.
    """
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
            moved.extend(split_bold_labels(content, paper))
        else:
            c = content.strip()
            assert "\\subsection{" not in c and "\\section{" not in c, (
                f"{paper}: nested heading inside declaration {title_raw!r}"
            )
            moved.append((title_raw, c))

    # remove the declaration spans (reverse order keeps indices valid)
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

    # 1. in-memory markdown fixes
    for old, new, expected in MD_FIXES.get(paper, []):
        n = md.count(old)
        assert n == expected, f"{paper}: md fix {old!r}: expected {expected}, found {n}"
        md = md.replace(old, new)

    # 2. pandoc
    r = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "latex"],
        input=md, capture_output=True, text=True, check=True,
    )
    tex = r.stdout

    # 3a. title extraction (pandoc emits \section{Title}\label{slug}; the
    # label is infrastructure and is dropped with the heading)
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

    # 3e. pandoc escapes a literal '*' inside math as '\*'; after '^' or '_'
    # that is invalid TeX ("Missing { inserted") - normalise to \ast
    tex = tex.replace("^\\*", "^{\\ast}").replace("_\\*", "_{\\ast}")

    # 3f. Unicode -> macros; must end pure ASCII
    tex = unicode_fixes(tex)
    bad = sorted({c for c in tex if ord(c) > 127})
    assert not bad, f"{paper}: unmapped non-ASCII: {[hex(ord(c)) for c in bad]}"

    # 3g. emphasis mis-parse symptom (literal-star class of bugs): pandoc
    # disables intraword '*' emphasis, so a legitimate \emph never directly
    # follows a word character; if it does AND opens with punctuation, a
    # literal star was eaten (E4's K* sites). Reference titles legitimately
    # start with digits, so a bare digit opening is not flagged.
    assert not re.search(r"[A-Za-z0-9]\\emph\{[,.:;)]", tex), (
        f"{paper}: emphasis-span mis-parse symptom present"
    )

    # 3h. declaration relocation: the papers' own declaration subsections
    # move to a trailing Declarations section (content verbatim; the moved
    # text stays inside the checked corpus below).
    body_pre = tex  # pre-relocation pandoc body (for the P4 identity check)
    tex, moved = relocate_declarations(tex, paper)

    # 4. integrity checks: numeric multiset exact; no md word lost
    corpus = title + "\n" + tex
    corpus = re.sub(r"\\begin\{longtable\}\[\]\{@{}.*?@\{\}\}", " ", corpus, flags=re.S)
    corpus = re.sub(r"\\rule\{[^}]*\}\{[^}]*\}", " ", corpus)  # md horizontal rules
    corpus = re.sub(r"\\label\{[^}]*\}", " ", corpus)  # auto-id anchors (may carry digits)
    corpus = re.sub(r"\\def\\labelenumi[^{]*\{[^}]*\}", " ", corpus)  # enumerate label defs
    corpus = re.sub(r"\\setcounter\{enumi\}\{\d+\}", " ", corpus)  # enumerate start offsets
    md_check = unicode_fixes(md)

    # Numbers absorbed by LaTeX auto-numbering (rendered identically by
    # pandoc's enumerate/\caption machinery, but absent from the .tex
    # source tokens):
    #  - each figure: the md's alt text "Figure N" and bold caption prefix
    #    "Figure N." disappear into \caption's automatic "Figure N:" label
    #    (and the word "figure" twice for the word check);
    #  - each ordered-list marker (decimal "N."/"N)"/"(N)", roman "(i)",
    #    alpha "(a)"/"(b)"): enumerate prints the label itself; pandoc
    #    preserves the marker style and any non-1 start (\setcounter), so
    #    the rendered numbering is identical to the markdown's.
    fig_nums = [int(n) for n in re.findall(r"!\[Figure (\d+)\]", md_check)]
    marker_re = re.compile(r"^(\s*)\(?([0-9]+|[ivxl]+|[a-z])[.)] +")
    marker_digits: list[int] = []
    marker_words: list[str] = []
    # Pandoc list semantics: a marker line is a list item only when it
    # starts a block (after a blank line, a heading, a fence) or continues
    # an open list; a marker line inside a running paragraph is lazy
    # continuation text and stays literal in the output.
    state = "blank"  # blank | text | in_list
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
            state = "text"  # literal marker inside a paragraph
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
    unexpected = extras - ALLOWED_EXTRA_WORDS.get(paper, Counter())
    assert not unexpected, (
        f"{paper}: unexpected extra LaTeX words: {dict(unexpected.most_common(10))}"
    )

    # 5. assemble: front matter (items 1-2) + body + back matter (item 3,
    # AI declaration appended as the final Declarations subsection, outside
    # the checked corpus exactly like the front matter).
    final = (
        header_comment(paper, 13)
        + PREAMBLE
        + f"\\title{{{title}}}\n" + AUTHOR + "\n" + DATE + "\n\\maketitle\n\n"
        + tex.strip()
        + "\n\n\\subsection*{AI declaration}\n" + AI_TEXT + "\n\n\\end{document}\n"
    )
    for needle in AUTHOR_NEEDLES:
        assert needle in final, f"{paper}: author block missing {needle!r}"
    for needle in BACK_NEEDLES:
        assert needle in final, f"{paper}: back matter missing {needle!r}"
    assert final.count("\\section*{Declarations}") == 1, f"{paper}: Declarations section not unique"
    assert "\\thanks" not in final, f"{paper}: wave-11 thanks footnote still present"
    # the AI declaration is the LAST thing before \end{document}
    tail_parts = final.rsplit("\n\n\\end{document}", 1)[0].rsplit("\n", 2)
    assert tail_parts[-2] == "\\subsection*{AI declaration}" and tail_parts[-1] == AI_TEXT, (
        f"{paper}: AI declaration is not the final subsection"
    )

    texfile = LATEX / f"{paper}.tex"
    if texfile.exists():
        old = texfile.read_text(encoding="utf-8")
        if "by wave13/build_latex_v13.py" in old:
            assert final == old, f"{paper}: non-idempotent rebuild (body changed)"
        elif "by wave11/build_latex_author.py" in old:
            # P4 (md unchanged): BODY IDENTITY - the fresh pandoc body equals
            # the wave-11 body, and the new file equals the old after ONLY the
            # header, \author, \date, and declaration-relocation changes.
            old_body = old.split("\n\\maketitle\n\n", 1)[1].rsplit(
                "\n\n\\end{document}\n", 1
            )[0]
            assert body_pre.strip() == old_body.strip(), (
                f"{paper}: pandoc body drifted from the wave-11 output"
            )
            old_front = old.split("\n\\maketitle\n\n", 1)[0]
            expected_front = (
                old_front
                .replace(header_comment(paper, 11), header_comment(paper, 13), 1)
                .replace(W11_AUTHOR, AUTHOR, 1)
                .replace("\n\\date{}", "\n" + DATE, 1)
                # xcolor: the link-color mix (blue!45!black) is instantiated
                # by the clickable ORCID/email links (wave-9/11 never typeset
                # a link, so the option was inert)
                .replace(
                    "\\usepackage[colorlinks=true,allcolors=blue!45!black]{hyperref}",
                    "\\usepackage{xcolor}\n"
                    "\\usepackage[colorlinks=true,allcolors=blue!45!black]{hyperref}",
                    1,
                )
            )
            actual_front = final.split("\n\\maketitle\n\n", 1)[0]
            assert actual_front == expected_front, (
                f"{paper}: front matter changed beyond header/author/date"
            )
            new_body = final.split("\n\\maketitle\n\n", 1)[1].rsplit(
                "\n\n\\end{document}\n", 1
            )[0]
            relocated_old, _moved = relocate_declarations(old_body, paper)
            expected_body = (
                relocated_old.strip()
                + "\n\n\\subsection*{AI declaration}\n" + AI_TEXT
            )
            assert new_body == expected_body, (
                f"{paper}: body changed beyond the declaration relocation"
            )
        else:
            raise AssertionError(f"{paper}: unrecognised existing tex header")

    texfile.write_text(final, encoding="utf-8")

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
    print(f"\n{len(results)}/9 papers compiled. LaTeX+PDF in: {LATEX}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
