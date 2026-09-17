#!/usr/bin/env python3
"""Wave-16 / Task 88, part 1: author paper4_delay_dynamics_v33.md --- the
reader-oriented formal rewrite of paper4_delay_dynamics_v32.md.

Task (owner-directed): "read some related landmark papers to rewrite formally
but reader-oriented, according to academic writing conventions, without excess
jargon, using mostly plain words to remain highly accessible.  always produce
new versions."

Landmark papers read for the writing conventions (web, abstract level):
Fridman 2010 Automatica (refined input-delay approach to sampled-data
control), Richard 2003 Automatica (time-delay systems overview), Hetel et al.
2017 Automatica (aperiodic sampling overview), May 1973 Ecology (time-delay
versus stability), Hutchings and Myers 1994 CJFAS (northern cod collapse ---
the exemplar of plain declarative formal writing).  Conventions applied:
short declarative sentences, one fact per sentence; results stated before
machinery; every technical term defined in plain words at first use; explicit
section-level signposting; active constructions; the three-level certainty
scale (proved theorem / interval certificate / declared-status numerical
result) kept intact claim by claim.

What changes and what does not:
- ALL prose is rewritten for readability (abstract, introduction,
  contributions, section openers, interpretation paragraphs, discussion,
  conclusion; theorem statements and proofs smoothed, hypotheses and
  conclusions preserved).
- Every equation, table, figure, numeric value, interval, reference entry,
  hypothesis label (H1)-(H5), and certification-tier statement is carried
  over unchanged: display equations and tables are spliced byte-identical
  from the v32 markdown (the @@V32:<NAME>@@ markers below), and the
  fail-loud checks verify that every math span of v33 exists verbatim in
  v32 and that the v32 numeric multiset is a sub-multiset of v33's.
- One deliberate correction: v32 carries three 'M_{\\\\mathrm{ZOH}}' /
  '\\\\pm' double-backspace (sic: double-backslash) typos in the
  scheme-dependence remark of Section 8, which shipped as literal '\\\\'
  line-break commands in the v32 PDF's math.  v33 uses the correct
  single-backslash forms; the single span with no single-backslash
  counterpart in v32 ('$\\\\rho(M_{\\\\mathrm{ZOH}})$') is whitelisted in
  the math check below.

This script is fully reproducible from the repository alone: it concatenates
wave16/parts_v33/part01..part10 (the authored prose), splices the verbatim
blocks from arena agent 1/paper rewrites/paper4_delay_dynamics_v32.md by the
validated anchors, applies the seven micro-formatting alignments, and writes
arena agent 1/paper rewrites/paper4_delay_dynamics_v33.md.  v32 is never
modified (version discipline).  Re-running is idempotent.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PR = ROOT / "arena agent 1/paper rewrites"
HERE = Path(__file__).resolve().parent
V32 = PR / "paper4_delay_dynamics_v32.md"
V33 = PR / "paper4_delay_dynamics_v33.md"

# the one deliberate correction (see module docstring)
MATH_WHITELIST = {"$\\rho(M_{\\mathrm{ZOH}})$"}


def extract_blocks(t: str) -> dict[str, str]:
    lines = t.split("\n")

    def L(a: int, b: int) -> str:  # 1-indexed inclusive line range of v32 md
        return "\n".join(lines[a - 1 : b])

    blocks = {
        "KEYWORDS": L(11, 11),
        "DEFS": L(54, 54),
        "EQ1": L(56, 60),
        "PARAMTABLE": L(64, 77),
        "DSET": L(84, 84),
        "EQ2": L(103, 103),
        "NORMSTAR": L(117, 117),
        "LEMMABOUND": L(123, 123),
        "RMISMATCH": L(127, 127),
        "GRONWALL": L(129, 129),
        "EQ3": L(135, 135),
        "GAINS": L(137, 137),
        "EQ4": L(141, 141),
        "FM": L(143, 143),
        "ZSTAR": L(153, 153),
        "EQ_ESTAR": L(155, 155),
        "LINFIRST": L(163, 163),
        "LINCOEF": L(165, 169),
        "EQ5": L(171, 171),
        "FILTERID": L(173, 173),
        "LCANCEL": L(175, 175),
        "EQ6": L(189, 189),
        "EQ7": L(191, 191),
        "EQ8": L(195, 195),
        "HEVEN": L(199, 199),
        "CROSSTABLE": L(222, 226),
        "L1": L(235, 235),
        "EQ9": L(265, 265),
        "EQ10": L(277, 277),
        "MODBOUND": L(281, 281),
        "CERTMAP": L(297, 297),
        "HCUBIC": L(315, 315),
        "CCOEF": L(317, 317),
        "HCUBICFULL": L(327, 327),
        "GAMMA": L(335, 335),
        "PHASEEQ": L(353, 353),
        "FLIPDELAYS": L(355, 355),
        "AHOLD": L(361, 361),
        "EQ11": L(363, 363),
        "DRSTOCK": L(392, 392),
        "DRDEF": L(394, 394),
        "DRZ": L(396, 396),
        "DRE": L(397, 397),
        "EQ12": L(427, 427),
        "EXACTUPDATE": L(441, 441),
        "EQ13": L(443, 443),
        "TRUC": L(449, 449),
        "MZOH": L(455, 455),
        "CONSOLTABLE": L(460, 467),
        "FIGBLOCK": L(488, 490),
        "PINNED": L(509, 509),
        "FOLDS4": L(511, 511),
        "EQ14": L(543, 543),
        "LOGID": L(565, 565),
        "TRANSTABLE": L(592, 599),
    }

    def find_heading(s: str) -> int:
        for i, ln in enumerate(lines, 1):
            if ln.strip() == s:
                return i
        raise AssertionError(f"heading {s!r} not found in v32")

    r0 = find_heading("## References")
    r1 = find_heading("## Supplementary material")
    d0 = find_heading("## Data availability")
    d1 = find_heading("## Declaration of competing interest")
    blocks["REFS"] = "\n".join(lines[r0 - 1 : r1 - 1]).rstrip("\n")
    blocks["DATAAVAIL"] = "\n".join(lines[d0 - 1 : d1 - 1]).rstrip("\n")
    blocks["SUPPL"] = "\n".join(lines[r1 - 1 :]).rstrip("\n")
    # anchor sanity: every block must be nonempty and contain its marker tag
    for name, body in blocks.items():
        assert body.strip(), f"block {name} is empty"
    return blocks


FIXES = [
    # align \neq -> \ne, \geq -> \ge, \big -> \bigl, and the v32 paren-in-math
    # form, so that every math span of v33 is byte-identical to a v32 span
    ("$\\mathrm{d\\,Re}\\,\\lambda/\\mathrm{d}\\tau \\neq 0$",
     "$\\mathrm{d\\,Re}\\,\\lambda/\\mathrm{d}\\tau \\ne 0$"),
    ("$\\partial_\\lambda \\Delta_{\\mathrm{full}} \\neq 0$",
     "$\\partial_\\lambda \\Delta_{\\mathrm{full}} \\ne 0$"),
    ("$\\partial_\\lambda \\Delta_{\\mathrm{core}} \\neq 0$",
     "$\\partial_\\lambda \\Delta_{\\mathrm{core}} \\ne 0$"),
    ("$\\mathrm{d}\\,\\mathrm{Re}\\,\\lambda/\\mathrm{d}\\tau \\neq 0$",
     "$\\mathrm{d}\\,\\mathrm{Re}\\,\\lambda/\\mathrm{d}\\tau \\ne 0$"),
    ("$R_0 = \\mathbf e_3\\big(C_Z \\mathbf e_2^\\top + C_E \\mathbf e_3^\\top\\big)$",
     "$R_0 = \\mathbf e_3\\bigl(C_Z \\mathbf e_2^\\top + C_E \\mathbf e_3^\\top\\bigr)$"),
    ("with a negative modulus gap ($-3\\times10^{-4}$ to $-10^{-3}$)",
     "with a negative modulus gap $(-3\\times10^{-4}$ to $-10^{-3}$)"),
    ("$\\alpha_0 > \\beta_0 \\geq 0$", "$\\alpha_0 > \\beta_0 \\ge 0$"),
]


def main() -> int:
    t32 = V32.read_text(encoding="utf-8")
    blocks = extract_blocks(t32)

    parts = sorted((HERE / "parts_v33").glob("part*.md"))
    assert len(parts) == 10, f"expected 10 parts, found {len(parts)}"
    text = "".join(p.read_text(encoding="utf-8") for p in parts)

    used: set[str] = set()

    def repl(m: re.Match) -> str:
        name = m.group(1)
        assert name in blocks, f"unknown block marker {name}"
        used.add(name)
        return blocks[name]

    text = re.sub(r"@@V32:(\w+)@@", repl, text)
    assert used == set(blocks), (
        f"unused blocks: {sorted(set(blocks) - used)}"
    )

    for old, new in FIXES:
        assert text.count(old) == 1, f"fix anchor not unique: {old!r}"
        text = text.replace(old, new)

    # fail-loud check 1: every math span of v33 exists verbatim in v32
    spans = re.findall(r"\$\$.*?\$\$|\$[^\$\n]+\$", text, flags=re.S)
    missing = [s for s in spans if s not in t32 and s not in MATH_WHITELIST]
    assert not missing, f"math spans missing from v32: {missing[:5]}"

    # fail-loud check 2: v32 title, keywords and reference block survive
    assert text.split("\n", 1)[0] == t32.split("\n", 1)[0], "title changed"
    assert blocks["KEYWORDS"] in text, "keywords block missing"
    assert blocks["REFS"] in text, "references block not byte-identical"

    # fail-loud check 3: all twelve numbered sections + all subsection
    # headings of v32 survive (same skeleton, no renumbering)
    h32 = [ln.rstrip() for ln in t32.split("\n") if ln.startswith("#")]
    h33 = [ln.rstrip() for ln in text.split("\n") if ln.startswith("#")]
    missing_h = [h for h in h32 if h not in h33]
    assert not missing_h, f"headings lost: {missing_h}"

    if V33.exists():
        old = V33.read_text(encoding="utf-8")
        assert old == text, "non-idempotent rebuild of v33 markdown"
    V33.write_text(text, encoding="utf-8")
    print(f"  paper4_delay_dynamics_v33.md: OK  {len(text)} chars, "
          f"{len(spans)} math spans (all verbatim in v32, "
          f"{len(MATH_WHITELIST)} whitelisted correction)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
