#!/usr/bin/env python3
r"""make_v62_p1.py — build paper1_assessment_separation_v62.tex from v61.

Task 120 (alignment-completion wave) / batch 8 / paper 1.
Source of the adopted set: the post-v61 audit of the six owner questions —
(1) remaining points of batch 8/p1 journal alignment.txt worth implementing
after adapting to the JMCDA target; (3) abstract/keywords/sections/
supplementary alignment with the latest version; (5) genuine pedagogical,
expository or ecological completions; (6) the conceptual-clarity and flow
scan. Every operation is prose-level; the mathematics is untouched.

Operations:

  OP 1  provenance: the v62 header line (the v61 line stands unchanged);
  OP 2  the List of abbreviations completed — DFO, LPI, LRP, NCAM are all
        used in the body (DFO from Section 5.8's relevance chain and the
        benchmark's data anchor; LPI eleven times from the sigma-extension
        on; LRP eighteen times, first in Section 5.8 long before the
        benchmark's expansion; NCAM twice at the data anchor) but carried
        no entry in the three-item list (CES, MSY, PROMETHEE);
  OP 3  Section 5.2: the Supplementary-Material pointer gains the
        acceptance-semantics reading ("the protocols as decision-aiding
        sorting rules (Roy, 1996; Vincke, 1992)") — announcing the fourth
        S10 positioning note added to the supplementary in this same wave
        (paper1_supplementary_v12.md), which expands the v61 §5.2 paragraph
        the supplementary previously lagged by one item;
  OP 4  Section 6.3: the decision-aiding-context paragraph gains the
        conflicting-objectives/stakeholder sentence — the one remaining
        residue of the owner's uploaded inventory (its JMCDA plan item 2:
        "conflicting objectives (ecological floor vs. income floor)" and
        "multiple stakeholders"), completing the special-issue vocabulary
        ("real-world decision problems involving multiple stakeholders and
        conflicting objectives") in the paragraph that satisfies the
        venue's "explicit decision making contexts" requirement.

Evaluated in the audit and NOT implemented (with reasons, recorded in the
wave's IMPLEMENTATION_RECORD.md): delegation of any main-text material to
the supplementary (no venue word limit; the labelled extensions carry the
relevance chains that serve the venue's decision-context requirement); the
extension check-list enumerations in the supplementary (the main text's
inline verification paragraphs carry the counts and scope; the deposited
run logs carry the enumerations; duplication); a decision table for the
licensing thresholds (rejected in Task 119 as redundant — stands); the
JORS-side items (recorded for rerouting only — stands).

Standing rules honored: new version only (v62; never overwrite v61);
fail-loud anchored edits with the inverse-reconstruction gate; math-span
multiset UNCHANGED (every operation is prose-level); marker accounting;
structure pins (environments unchanged; the \item count grows by exactly
the four new abbreviation entries); register sweep (the v60/v61 banned
list plus the venue register); idempotence by destination-exists gate.
Exit 0 on success.
"""
import sys
from pathlib import Path
from collections import Counter
import re

HERE = Path(__file__).resolve().parent
LATEX = HERE.parents[1] / "arena agent 1" / "paper rewrites" / "latex"
SRC = LATEX / "paper1_assessment_separation_v61.tex"
DST = LATEX / "paper1_assessment_separation_v62.tex"


def die(msg: str):
    print(f"FAIL: {msg}")
    sys.exit(1)


if DST.exists():
    die(f"destination exists (idempotence gate): {DST.name}")

text = SRC.read_text(encoding="utf-8")
orig = text
PAIRS = []   # (name, anchor, repl, count) for every operation


def edit(name: str, anchor: str, repl: str, count: int = 1):
    global text
    n = text.count(anchor)
    if n != count:
        die(f"anchor [{name}] found {n}x (expected {count}):\n---\n{anchor[:240]}\n---")
    text = text.replace(anchor, repl)
    PAIRS.append((name, anchor, repl, count))
    print(f"  ok  {name}")


# =====================================================================
# OP 1 — provenance: the v62 header line
# =====================================================================
edit(
    "provenance-v62",
    "% v61 (JMCDA alignment wave, 2026-09-22): venue-target alignment for the Journal of Multi-Criteria Decision Analysis (special issue: Better Decisions for a Better Tomorrow) — MCDA-forward abstract, keywords, and first highlight; the MCDA compensability canon anchored (Keeney-Raiffa, Roy, Munda, Vincke); the acceptance-semantics, weight-sensitivity, and adjustable-robustness readings promoted; the JEL apparatus retired; venue declared (batch 8/v61_jmcda_wave/; batch 8/p1 journal alignment.txt).",
    "% v61 (JMCDA alignment wave, 2026-09-22): venue-target alignment for the Journal of Multi-Criteria Decision Analysis (special issue: Better Decisions for a Better Tomorrow) — MCDA-forward abstract, keywords, and first highlight; the MCDA compensability canon anchored (Keeney-Raiffa, Roy, Munda, Vincke); the acceptance-semantics, weight-sensitivity, and adjustable-robustness readings promoted; the JEL apparatus retired; venue declared (batch 8/v61_jmcda_wave/; batch 8/p1 journal alignment.txt).\n"
    "% v62 (alignment-completion wave, 2026-09-22): the abbreviations list completed (DFO, LPI, LRP, NCAM — all used in the body without an entry); the conflicting-objectives/stakeholder sentence added to the Section 6.3 decision-aiding context; the acceptance-semantics clause added to the Section 5.2 supplementary pointer, with the matching positioning note in the supplementary's S10 (batch 8/v62_alignment_completion_wave/).",
)

# =====================================================================
# OP 2 — the List of abbreviations completed (alphabetical)
# =====================================================================
edit(
    "abbreviations-completed",
    "\\item \\textbf{CES} --- constant elasticity of substitution\n"
    "\\item \\textbf{MSY} --- maximum sustainable yield\n"
    "\\item \\textbf{PROMETHEE} --- Preference Ranking Organisation Method for Enrichment Evaluation",
    "\\item \\textbf{CES} --- constant elasticity of substitution\n"
    "\\item \\textbf{DFO} --- Fisheries and Oceans Canada\n"
    "\\item \\textbf{LPI} --- Living Planet Index\n"
    "\\item \\textbf{LRP} --- limit reference point\n"
    "\\item \\textbf{MSY} --- maximum sustainable yield\n"
    "\\item \\textbf{NCAM} --- Northern Cod Assessment Model\n"
    "\\item \\textbf{PROMETHEE} --- Preference Ranking Organisation Method for Enrichment Evaluation",
)

# =====================================================================
# OP 3 — Section 5.2: the acceptance-semantics clause on the S10 pointer
# =====================================================================
edit(
    "s10-pointer-acceptance-semantics",
    "(Cinelli, Coles, and Kirwan, 2014; Sch\\\"ar, Pohl, and Geldermann, 2025) --- are collected in the\n"
    "Supplementary Material (S10).",
    "(Cinelli, Coles, and Kirwan, 2014; Sch\\\"ar, Pohl, and Geldermann, 2025) --- and the\n"
    "acceptance-semantics reading of the protocols as decision-aiding\n"
    "sorting rules (Roy, 1996; Vincke, 1992) --- are collected in the\n"
    "Supplementary Material (S10).",
)

# =====================================================================
# OP 4 — Section 6.3: the conflicting-objectives/stakeholder sentence
# =====================================================================
edit(
    "decision-context-stakeholders",
    "orderings of the assessment doctrine under which the composite index\n"
    "is read. The acceptance gap is then a robustness failure of the",
    "orderings of the assessment doctrine under which the composite index\n"
    "is read. The two criteria are conflicting objectives --- each of the\n"
    "two principal schedules protects one at the expense of the other ---\n"
    "and each is defended by a distinct constituency, so the weight space\n"
    "reads both as an assessor's calibration and as the preference profile\n"
    "of the stakeholder dispute. The acceptance gap is then a robustness\n"
    "failure of the",
)

# =====================================================================
# GATE 1 — inverse reconstruction: revert every operation in reverse
# order and require byte-identity with v61.
# =====================================================================
recon = text
for name, anchor, repl, count in reversed(PAIRS):
    if recon.count(repl) < count:
        die(f"inverse gate: replacement of [{name}] found {recon.count(repl)}x, expected {count}")
    recon = recon.replace(repl, anchor, count)
if recon != orig:
    k = next((i for i, (a, b) in enumerate(zip(recon, orig)) if a != b), min(len(recon), len(orig)))
    die(f"inverse reconstruction gate: reverted text != v61 (first divergence at offset {k}:\nRECON: ...{recon[max(0,k-80):k+80]!r}\nV61:    ...{orig[max(0,k-80):k+80]!r})")
print("  ok  inverse reconstruction: byte-exact revert to v61")

# =====================================================================
# GATE 2 — math-span multiset accounting: UNCHANGED (every operation
# is prose-level; zero spans added, zero removed, zero altered).
# =====================================================================
SPAN = re.compile(r"\\\((?:[^\\]|\\.)*?\\\)|\\\[.*?\\\]", re.S)


def spans(s):
    return Counter(SPAN.findall(s))


s61, s62 = spans(orig), spans(text)
if s62 != s61:
    only61 = s61 - s62
    only62 = s62 - s61
    die(f"math-span multiset mismatch (expected zero delta).\nspans lost: {dict(only61)}\nspans gained: {dict(only62)}")
print(f"  ok  math-span multiset: {sum(s61.values())} -> {sum(s62.values())} (unchanged, as designed)")

# =====================================================================
# GATE 3 — marker accounting: every new marker present, every retired
# marker absent.
# =====================================================================
NEW_MARKERS = [
    "% v62 (alignment-completion wave, 2026-09-22)",
    "\\item \\textbf{DFO} --- Fisheries and Oceans Canada",
    "\\item \\textbf{LPI} --- Living Planet Index",
    "\\item \\textbf{LRP} --- limit reference point",
    "\\item \\textbf{NCAM} --- Northern Cod Assessment Model",
    "and the\nacceptance-semantics reading of the protocols as decision-aiding\nsorting rules (Roy, 1996; Vincke, 1992)",
    "The two criteria are conflicting objectives --- each of the",
    "each is defended by a distinct constituency, so the weight space",
    "both as an assessor's calibration and as the preference profile",
    "of the stakeholder dispute.",
]
OLD_MARKERS = [
    "Geldermann, 2025) --- are collected in the",
]
for m in NEW_MARKERS:
    if m not in text:
        die(f"marker accounting: new marker missing: {m[:90]!r}")
for m in OLD_MARKERS:
    if m in text:
        die(f"marker accounting: retired marker still present: {m[:90]!r}")
print(f"  ok  marker accounting: {len(NEW_MARKERS)} new present, {len(OLD_MARKERS)} retired absent")

# =====================================================================
# GATE 4 — structure pins: environments and headings unchanged; the
# \item count grows by exactly the four new abbreviation entries.
# =====================================================================
for env in ("enumerate", "itemize", "figure", "table", "longtable", "abstract", "keyword", "highlights", "frontmatter"):
    b, e = text.count(f"\\begin{{{env}}}"), text.count(f"\\end{{{env}}}")
    ob, oe = orig.count(f"\\begin{{{env}}}"), orig.count(f"\\end{{{env}}}")
    if b != e:
        die(f"structure pin: unbalanced {env} ({b} begin / {e} end)")
    if (b, e) != (ob, oe):
        die(f"structure pin: {env} count changed {ob}->{b}")
delta_items = text.count("\\item") - orig.count("\\item")
if delta_items != 4:
    die(f"structure pin: \\item delta is {delta_items}, expected exactly +4 (the new abbreviation entries)")
for heading in ("\\section{Introduction}", "\\section{Interpretation}", "\\section{Conclusions}",
                "\\subsection{Positioning against established", "\\section*{References}",
                "\\section*{List of abbreviations}", "\\section*{Declarations}"):
    if text.count(heading) != orig.count(heading):
        die(f"structure pin: heading count changed: {heading}")
print("  ok  structure pins: environments, headings unchanged; \\item count +4 (the abbreviation entries)")

# =====================================================================
# GATE 5 — register sweep: the banned list plus the venue register
# (no journal name / abbreviation / special-issue mention in the body).
# =====================================================================
BANNED = ["honest", "punchline", "no longer open", "was never triggered",
          "has since closed", "in passing", "addendum", "domesticat",
          "in place:", "stated in place", "upgraded to a"]
for w in BANNED:
    if w.lower() in text.lower():
        i = text.lower().index(w.lower())
        die(f"register sweep: banned residue {w!r} at offset {i}: ...{text[max(0,i-80):i+80]}...")
body = text[text.index("\\begin{document}"):text.index("\\section*{References}")]
for w in ("Journal of Multi-Criteria", "JMCDA", "JORS", "special issue", "Wiley"):
    if w.lower() in body.lower():
        i = body.lower().index(w.lower())
        die(f"venue register: {w!r} leaked into the document body: ...{body[max(0,i-80):i+80]}...")
# The References section may legitimately name the venue (the Sch\"ar et al.
# 2025 entry is a JMCDA paper); confirm exactly that one occurrence there.
refs = text[text.index("\\section*{References}"):]
n_jmcda_refs = refs.count("Journal of Multi-Criteria Decision Analysis")
if n_jmcda_refs != 1:
    die(f"venue register: expected exactly one JMCDA mention in References (the Sch\\\"ar et al. entry), found {n_jmcda_refs}")
print(f"  ok  register sweep: {len(BANNED)} banned residues + 5 venue-leak checks absent (body; the single References mention is the Sch\\\"ar et al. JMCDA entry)")

# =====================================================================
# Write and report.
# =====================================================================
DST.write_text(text, encoding="utf-8")
nlines = text.count("\n") + 1
print(f"\nWROTE {DST.name}: {nlines} lines (v61: {orig.count(chr(10)) + 1})")
print("ALL GATES GREEN")
