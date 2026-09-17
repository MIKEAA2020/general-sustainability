#!/usr/bin/env python3
"""Wave-15 / Task 87, part 2: build paper4_delay_dynamics_v32.tex/.pdf from
paper4_delay_dynamics_v32.md (created by wave15/make_v32.py).

The wave-14 pipeline with every fail-loud check inherited (pure-ASCII body,
emphasis-mis-parse symptom, figure counts, numeric-token multiset EXACTLY
equal between markdown and LaTeX body, no markdown word lost, declaration
relocation with the AI declaration as the final subsection, clickable
ORCID/email front matter, pinned date, tectonic compile with log scan,
idempotent rebuild).  The wave-14 v31-content needles are replaced by the
v32 content needles (the documented-timelines strengthening), and the
tex-level numeric discipline is taken against the v31 tex: every frozen
scientific token of the v31 LaTeX survives verbatim in v32 (section
renumber 11.4->11.8 exempted, exactly as verified at md level); the new
tokens are the md-level empirical-record whitelist (documented dates, SSB
values, reference volume/page/DOIs), verified equal between md and tex by
the inherited multiset check.

Outputs: arena agent 1/paper rewrites/latex/paper4_delay_dynamics_v32.tex
and .pdf.  v31 tex/pdf remain untouched (version discipline).  Run twice
to pin byte-reproducibility.
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

PAPERS = ["paper4_delay_dynamics_v32"]

# --- front matter (identical to wave-13/14) ------------------------------------
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

# --- back matter (identical to wave-13/14) -------------------------------------
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

# --- v32 content needles (the documented-timelines strengthening) -------------
V32_NEEDLES = {
    "paper4_delay_dynamics_v32": [
        "Documented governance timelines occupy the same scales",   # abstract
        "the northern cod record runs from annual assessment",      # abstract
        "The management record supplies the field-scale counterpart",  # intro
        "the documented institutional timelines that ground the two timing coordinates",  # organization
        "11.4 Documented institutional timelines",
        "the northern cod (NAFO 2J3KL) record is the canonical instance",
        "fell from about 735 kt in the 1991 assessment to about 31 kt in the 1994 assessment",
        "a stock falling by a factor of more than twenty between annual assessments",
        "less frequent assessment reduced relative yield",          # Li et al.
        "the empirical counterpart of this paper's reading of",     # T_r reading
        "are the subject of the companion sampled-governance paper",
        "not the coefficients of any theorem",                      # scope guard
        "(Section 11.5's first stated open task",                  # re-pointed xref
        "11.5 Certification levels",                                # renumber
        "they are not a calibration, and no institutional coefficient is identified from them",
        "What can be learned from the collapse of a renewable resource",   # ref
        "The influence of stock assessment frequency",              # ref (Li)
        "Effects of altered stock assessment frequency",            # ref (Peterson)
        "Lessons for stock assessment from the northern cod collapse",  # ref (Walters)
        "Stock Assessment of Northern Cod (NAFO Divs. 2J3KL) in 2016",   # ref (DFO)
    ],
}

RENUMBER_TOKENS = {"11.4", "11.5", "11.6", "11.7", "11.8"}

# the '\maketitle' body separator (raw string: single backslash in the file)
MAKETITLE_SEP = "\n" + r"\maketitle" + "\n\n"


def header_comment(paper: str) -> str:
    return (
        f"% LaTeX source generated from {paper}.md by wave15/build_latex_v15.py "
        f"(batch 7 (audits of agent arena 1 paper rewrites)/wave15).\n"
        f"% Wave-14 pipeline with the wave-15 documented-timelines edits:\n"
        f"% abstract timelines sentence, introduction management-record\n"
        f"% grounding, new Discussion 11.4 'Documented institutional\n"
        f"% timelines: scale grounding for the two timing coordinates'\n"
        f"% (northern cod record, DFO 2016/2024; Hutchings and Myers 1994;\n"
        f"% Walters and Maguire 1996; Li, Bence and Brenden 2016; Peterson\n"
        f"% et al. 2022), old 11.4-11.7 renumbered 11.5-11.8, the not-a-\n"
        f"% calibration clause in Limitations (i), and the six references.\n"
        f"% Front matter: Amin Abaee, Independent Researcher, clickable ORCID\n"
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
    for needle in V32_NEEDLES[paper]:
        assert needle in final_flat, (
            f"{paper}: v32 content needle missing: {needle!r}"
        )
    assert final.count("\\section*{Declarations}") == 1, f"{paper}: Declarations section not unique"
    assert "\\thanks" not in final, f"{paper}: thanks footnote present"
    tail_parts = final.rsplit("\n\n\\end{document}", 1)[0].rsplit("\n", 2)
    assert tail_parts[-2] == "\\subsection*{AI declaration}" and tail_parts[-1] == AI_TEXT, (
        f"{paper}: AI declaration is not the final subsection"
    )

    texfile = LATEX / f"{paper}.tex"
    if texfile.exists():
        old = texfile.read_text(encoding="utf-8")
        if "by wave15/build_latex_v15.py" in old:
            assert final == old, f"{paper}: non-idempotent rebuild (output changed)"
        else:
            raise AssertionError(f"{paper}: unrecognised existing tex header")
    texfile.write_text(final, encoding="utf-8")

    # 6. tex-level numeric discipline vs the v31 tex (frozen values survive);
    #    run after the write so failures are debuggable on disk. The v31
    #    header comment's own version/wave tokens are excluded with the v31
    #    header stripped first.
    v31tex = (LATEX / "paper4_delay_dynamics_v31.tex").read_text(encoding="utf-8")
    v31body = v31tex.split(MAKETITLE_SEP, 1)[1]
    v32body = final.split(MAKETITLE_SEP, 1)[1]
    t31 = tokens_numeric(strip_cmds(v31body))
    t32 = tokens_numeric(strip_cmds(v32body))
    lost_t = {t: c for t, c in t31.items() if t32[t] < c and t not in RENUMBER_TOKENS}
    assert not lost_t, f"{paper}: frozen tex numeric tokens lost/reduced: {lost_t}"

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
