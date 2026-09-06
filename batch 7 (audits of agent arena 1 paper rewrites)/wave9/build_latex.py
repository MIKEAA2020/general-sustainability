#!/usr/bin/env python3
"""Wave-9 build: LaTeX sources + compiled PDFs for the nine papers.

Owner directive: provide LaTeX and PDF of all 9 papers (E1 v14, E2 v21,
E3 v15, E4 v13, P1 v22, P2 v12, P3 v31, P4 v30, P5 v25), compiling
error-free. (P4 enters at v30: this LaTeX pass surfaced the §9.6
setext-heading accident, fixed first in apply_batch9_p4_v30.py.)
Pipeline per paper:

  1. In-memory markdown fixes (only where literal star notation would be
     mis-parsed by pandoc as emphasis): E4's K*_phys/K*_inst/K*/H* sites
     and E2's table-cell 0.5K* -> inline math superscript-star notation.
     The markdown files on disk are NOT modified.
  2. pandoc (markdown -> LaTeX body).
  3. Post-processing: title -> \\title{}; \\subsection{Abstract} ->
     abstract environment (terminated at the Keywords paragraph or the
     next heading); each pandoc implicit figure merged with its
     following bold 'Figure N.' caption paragraph into a proper
     \\begin{figure}[htbp] with \\caption{...}; the 'Prepared in the
     format of ...' note centred in small type; all remaining Unicode
     mapped to LaTeX macros (prose Greek, relations, sub/superscript
     runs, accented reference names, QED box, script D, combining
     accents on beta/gamma/P).
  4. Fail-loud checks: output pure ASCII; no emphasis-span mis-parse
     symptom (\\emph{ starting with punctuation); figure counts match
     the markdown; numeric-token multiset EXACTLY equal between the
     (transformed) markdown and the final LaTeX body (frozen values
     cannot change); no markdown word lost in conversion.
  5. tectonic compile (exit code 0, no 'Missing character', no TeX error
     lines); log archived to wave9/logs/.

Outputs: arena agent 1/paper rewrites/latex/<paper>.tex and .pdf.
Run twice from the wave9 directory to pin reproducibility.
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
    "paperE1_cod_forecast_ladder_v14",
    "paperE2_cod_intervention_v21",
    "paperE3_edwards_forecast_ladder_v15",
    "paperE4_edwards_intervention_v13",
    "paper1_assessment_separation_v22",
    "paper2_obstruction_calculus_v12",
    "paper3_material_ledgers_v31",
    "paper4_delay_dynamics_v30",
    "paper5_sampled_governance_v25",
]

# --- 1. markdown-level fixes (literal-star notation; applied in memory) -----
# Exact-count assertions make these fail-loud: if the source changes, the
# build stops rather than silently mis-converting.
MD_FIXES: dict[str, list[tuple[str, str, int]]] = {
    "paperE1_cod_forecast_ladder_v14": [
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
    "paperE4_edwards_intervention_v13": [
        ("K*_phys", "$K^{\\ast}_{\\mathrm{phys}}$", 1),
        ("K*_inst", "$K^{\\ast}_{\\mathrm{inst}}$", 1),
        ("B(T) = H* + (618 − H*)/a^T",
         "$B(T) = H^{\\ast} + (618 - H^{\\ast})/a^{T}$", 1),
        ("T_empty(C) = ln((C − H*)/(K* − H*))/ln(1/a)",
         "$T_{\\mathrm{empty}}(C) = \\mathrm{ln}\\bigl((C - H^{\\ast})/(K^{\\ast} - H^{\\ast})\\bigr)/\\mathrm{ln}(1/a)$", 1),
        ("K*", "$K^{\\ast}$", 7),   # remaining sites: L57 x3, L77 x1, L79 x3
        ("H*", "$H^{\\ast}$", 0),   # safety net: all H* consumed by formulas
    ],
    "paperE2_cod_intervention_v21": [
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
}
# Per-paper expected extra words from deliberate math-notation conversions.
ALLOWED_EXTRA_WORDS = {
    "paperE4_edwards_intervention_v13": Counter({"d": 3}),  # \mathcal{D} x3
}

PREAMBLE = r"""\documentclass[11pt]{article}
\usepackage[a4paper,margin=1in]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{booktabs,longtable,array,calc}
\usepackage{colorlinks_placeholder}
\usepackage{etoolbox}
\AtBeginEnvironment{longtable}{\small}  % dense data tables
\setlength{\tabcolsep}{4pt}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\setcounter{secnumdepth}{-1}
\emergencystretch=3em
\graphicspath{{../}}
\begin{document}
""".replace(
    "\\usepackage{colorlinks_placeholder}",
    "\\usepackage[colorlinks=true,allcolors=blue!45!black]{hyperref}\n\\usepackage[font=small,labelfont=bf]{caption}",
)


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

    # 5. assemble and compile
    final = (
        f"% LaTeX source generated from {paper}.md by wave9/build_latex.py "
        f"(batch 7 (audits of agent arena 1 paper rewrites)/wave9).\n"
        f"% Edit the markdown source and re-run the build script to regenerate.\n"
        f"% Compiles error-free with tectonic (also compatible with pdflatex/xelatex).\n"
        + PREAMBLE
        + f"\\title{{{title}}}\n\\author{{}}\n\\date{{}}\n\\maketitle\n\n"
        + tex.strip()
        + "\n\n\\end{document}\n"
    )
    texfile = LATEX / f"{paper}.tex"
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

    md5 = hashlib.md5(texfile.read_bytes()).hexdigest()
    return {
        "paper": paper, "md5": md5, "figures": n_merged,
        "overfull": overfull, "pdf_kb": pdffile.stat().st_size // 1024,
    }


def main() -> int:
    results = []
    for paper in PAPERS:
        info = build_paper(paper)
        results.append(info)
        print(
            f"  {info['paper']}: OK  md5={info['md5'][:10]}  "
            f"figures={info['figures']}  overfull={info['overfull']}  "
            f"pdf={info['pdf_kb']} KB"
        )
    print(f"\n{len(results)}/9 papers compiled. LaTeX+PDF in: {LATEX}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
