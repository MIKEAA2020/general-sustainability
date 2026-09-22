#!/usr/bin/env python3
"""make_v61_p1.py — build paper1_assessment_separation_v61.tex from v60.

Task 119 (JMCDA venue alignment) / batch 8 / paper 1.
Source of the adopted set: batch 8/p1 journal alignment.txt (the evaluated,
strengthened, completed suggestion inventory for JMCDA target / JORS
comparator). Every operation is prose-level; the mathematics is untouched.

Operations (JMCDA = Journal of Multi-Criteria Decision Analysis; the SI is
"Better Decisions for a Better Tomorrow: MCDM Approaches for Sustainability,
Risk, and Complex Systems", deadline 31 January 2027):

  OP 1  provenance: v60 header date corrected (2025->2026, the wave's own
        record says 2026-09-22) + the v61 header line;
  OP 2  \\journal{Journal of Multi-Criteria Decision Analysis} (family
        precedent: the EMS variant declares its venue);
  OP 3  the JEL apparatus retired (the providecommand definition and the
        classification block) — an economics-venue artefact;
  OP 4  abstract opening re-cast compensatory/noncompensatory-first, with
        the weak/strong sustainability readings as the two instances (S1);
  OP 5  keywords re-ordered MCDA-first; "compensatory and noncompensatory
        aggregation", "composite indicators", "robustness", "sustainability
        assessment" added (S1);
  OP 6  first highlight bullet re-cast to match (S1);
  OP 7  Section 1.1: the MCDA compensability canon anchored (Keeney and
        Raiffa 1976 substitution rates; Roy 1996 concordance/veto; Munda
        2005 incommensurability) and "orthogonal to both" widened to
        "orthogonal to all of these" (S2);
  OP 8  Section 1.2: the here-and-now vs wait-and-see (adjustable
        robustness, Ben-Tal et al. 2004) reading promoted to the protocol
        introduction, with the weight in the role of the uncertain
        parameter (S4);
  OP 9  Section 5.2: the acceptance-semantics positioning paragraph — the
        sorting problematic (Roy; Vincke), the weight-adaptive reading made
        precise, the licensing thresholds as the verdict's exact
        weight-sensitivity intervals (the acceptance-side analogue of the
        Nardo et al. 2008 sensitivity analyses), and the static-vs-protocol
        compensability delimitation against Cinelli et al. 2014 and
        Schar et al. 2025 (S3 + S5, absorbing S11);
  OP 10 Conclusions: the three-constituency closing paragraph (S6);
  OP 12 References: + Keeney & Raiffa (1976); Munda (2005); Roy (1996);
        Vincke (1992) — canonical, verified;
  OP 13 is the cover letter (a separate file, not a tex operation).

Adopted later from the owner's uploaded inventory
(batch 8/p1 journal alignment.txt, received mid-wave; the evaluation is
batch 8/v61_jmcda_wave/JOURNAL_ALIGNMENT_EVALUATION.md, Part B):

  OP 14 keywords trimmed to seven (the venue's limit; Part A's list had
        nine) (B6);
  OP 15 the decision-aiding-context paragraph at the benchmark's opening
        (Section 6.3) — decision maker, decision alternatives, criteria,
        preference reading of the weights, the acceptance gap as a
        robustness failure of the decision-aiding process, the
        analyst-communicable deliverables, operational decision relevance
        (B1, the editorial-policy requirement "well-motivated by explicit
        decision making contexts"; absorbing the decision vocabulary of
        B2 and the deliverable reading of B3);
  OP 16 the Section 5.2 threshold sentence gains "the preference ranges
        over which each plan is certified" (B3).

Standing rules honored: new version only (v61; never overwrite v60);
fail-loud anchored edits with the inverse-reconstruction gate; math-span
multiset UNCHANGED (1,470 -> 1,470; zero added, zero removed — every
operation is prose-level); marker accounting; structure pins (environments
and items unchanged); register sweep (the v60 banned list plus the venue
register: no journal name, journal abbreviation, or special-issue mention
anywhere in the document body); idempotence by destination-exists gate.
Exit 0 on success.
"""
import sys
from pathlib import Path
from collections import Counter
import re

HERE = Path(__file__).resolve().parent
LATEX = HERE.parents[1] / "arena agent 1" / "paper rewrites" / "latex"
SRC = LATEX / "paper1_assessment_separation_v60.tex"
DST = LATEX / "paper1_assessment_separation_v61.tex"


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
# OP 1 — provenance: v60 date fix + v61 header line
# =====================================================================
edit(
    "provenance-v61",
    "% v60 (editorial wave, 2025-09-22): Tehran, Iran affiliation; closure blocks and the Limitations registry restated findings-first; informal terms replaced; mathematics unchanged except the recorded span accounting (batch 8/v60_editorial_wave/).",
    "% v60 (editorial wave, 2026-09-22): Tehran, Iran affiliation; closure blocks and the Limitations registry restated findings-first; informal terms replaced; mathematics unchanged except the recorded span accounting (batch 8/v60_editorial_wave/).\n"
    "% v61 (JMCDA alignment wave, 2026-09-22): venue-target alignment for the Journal of Multi-Criteria Decision Analysis (special issue: Better Decisions for a Better Tomorrow) — MCDA-forward abstract, keywords, and first highlight; the MCDA compensability canon anchored (Keeney-Raiffa, Roy, Munda, Vincke); the acceptance-semantics, weight-sensitivity, and adjustable-robustness readings promoted; the JEL apparatus retired; venue declared (batch 8/v61_jmcda_wave/; batch 8/p1 journal alignment.txt).",
)

# =====================================================================
# OP 2 — venue declaration
# =====================================================================
edit(
    "journal-declaration",
    "\\emergencystretch=3em\n% figures live in the figs_p1/ subfolder next to this file (self-contained package)",
    "\\emergencystretch=3em\n\\journal{Journal of Multi-Criteria Decision Analysis}\n% figures live in the figs_p1/ subfolder next to this file (self-contained package)",
)

# =====================================================================
# OP 3a — JEL apparatus: the definition line retired
# =====================================================================
edit(
    "jel-definition-retired",
    "\\usepackage[colorlinks=true,allcolors=blue!45!black]{hyperref}\n\\providecommand{\\jel}[1]{\\par\\noindent\\textbf{JEL classification:} #1\\par}\n\\usepackage{etoolbox}",
    "\\usepackage[colorlinks=true,allcolors=blue!45!black]{hyperref}\n\\usepackage{etoolbox}",
)

# =====================================================================
# OP 3b — JEL apparatus: the classification block retired
# =====================================================================
edit(
    "jel-block-retired",
    "\\end{keyword}\n\n\\jel{C61; C62; D81; Q01; Q56}\n\n\\begin{highlights}",
    "\\end{keyword}\n\n\\begin{highlights}",
)

# =====================================================================
# OP 4 — abstract opening re-cast (compensatory/noncompensatory first)
# =====================================================================
edit(
    "abstract-opening",
    "Sustainability criteria divide into scalarized criteria, which permit\n"
    "substitution through a weighted aggregate (weak sustainability), and\n"
    "coordinate-wise criteria, which impose separately-binding floors (strong\n"
    "sustainability). This paper compares the two as\n"
    "robust transition-safety problems on a common finite-horizon datum with\n"
    "path-wise constraints. At any fixed path the aggregate is lossless; the\n"
    "two criteria nevertheless separate, because common-plan acceptance and\n"
    "per-weight acceptance do not commute.",
    "In multi-criteria assessment, compensatory and noncompensatory\n"
    "aggregation give two readings of the same constraint set: the scalarized\n"
    "reading, which permits substitution through a weighted aggregate (weak\n"
    "sustainability), and the coordinate-wise reading, which imposes\n"
    "separately-binding floors (strong sustainability). This paper compares\n"
    "the two readings as robust transition-safety problems on a common\n"
    "finite-horizon datum with path-wise constraints. At any fixed path the\n"
    "aggregate is lossless; the two readings nevertheless separate, because\n"
    "common-plan acceptance and per-weight acceptance do not commute.",
)

# =====================================================================
# OP 5 — keywords re-ordered MCDA-first
# =====================================================================
edit(
    "keywords",
    "sustainability \\sep viability theory \\sep robust control \\sep scalarization \\sep multi-criteria decision analysis \\sep quantifier order \\sep transition safety",
    "multi-criteria decision analysis \\sep compensatory and noncompensatory aggregation \\sep composite indicators \\sep scalarization \\sep robustness \\sep sustainability assessment \\sep viability theory \\sep transition safety \\sep quantifier order",
)

# =====================================================================
# OP 6 — first highlight bullet re-cast
# =====================================================================
edit(
    "highlight-one",
    "\\item Scalarized and coordinate-wise sustainability criteria are compared as robust transition-safety problems on a common datum.",
    "\\item Compensatory and noncompensatory (weak- and strong-sustainability) criteria are compared as robust transition-safety problems on a common datum.",
)

# =====================================================================
# OP 7 — Section 1.1: the MCDA compensability canon
# =====================================================================
edit(
    "intro-mcda-canon",
    "weights-versus-importance distinction it has produced is part of good\n"
    "composite-indicator practice (Becker et al., 2017). What is established\n"
    "below is orthogonal to both: even if weights perfectly reflect importance,\n"
    "the quantifier order can still produce the gap.",
    "weights-versus-importance distinction it has produced is part of good\n"
    "composite-indicator practice (Becker et al., 2017). The compensability\n"
    "question itself is foundational in multi-criteria decision analysis:\n"
    "multi-attribute value theory builds substitution rates between criteria\n"
    "into its tradeoff structure (Keeney and Raiffa, 1976); the outranking\n"
    "tradition constrains compensation through concordance and veto (Roy,\n"
    "1996); and the decision-aiding treatment of sustainable development\n"
    "centres on incommensurable criteria (Munda, 2005). What is established\n"
    "below is orthogonal to all of these: even if weights perfectly reflect\n"
    "importance and substitution rates are elicited faithfully, the\n"
    "quantifier order can still produce the gap.",
)

# =====================================================================
# OP 8 — Section 1.2: here-and-now vs wait-and-see at the protocols
# =====================================================================
edit(
    "intro-adjustable-robustness",
    "collapses into Protocol 4 by the full-cone identity of\n"
    "Proposition 3(ii)).",
    "collapses into Protocol 4 by the full-cone identity of\n"
    "Proposition 3(ii)). In the vocabulary of decision making under\n"
    "uncertainty, the two protocols differ in when the plan is fixed relative\n"
    "to the assessment weight: Protocol 4 commits to one plan before the\n"
    "weight is known, while Protocol 2 lets the plan adapt once the weight is\n"
    "observed --- the here-and-now versus wait-and-see distinction of\n"
    "adjustable robust optimization (Ben-Tal et al., 2004), with the weight\n"
    "in the role of the uncertain parameter.",
)

# =====================================================================
# OP 9 — Section 5.2: the acceptance-semantics positioning paragraph
# =====================================================================
edit(
    "positioning-acceptance-semantics",
    "Supplementary Material (S10).\n\n"
    "Against this background, the finite-menu characterization of",
    "Supplementary Material (S10).\n\n"
    "For multi-criteria decision analysis, the protocols of\n"
    "Table~\\ref{tab:protocols} are acceptance semantics: they specify the rule\n"
    "by which a composite reading sorts a transition into the accepted or\n"
    "rejected category --- the sorting problematic of decision aiding (Roy,\n"
    "1996; Vincke, 1992). The separation is then a statement about which\n"
    "semantics a composite index can support: under weight-adaptive acceptance\n"
    "a transition is accepted when every weighting licenses some plan,\n"
    "possibly a different plan for each weighting, and Theorem 5 exhibits\n"
    "transitions that this rule accepts and the coordinate-wise rule rejects\n"
    "on an open region. The licensing thresholds of Theorem 5(6) give the\n"
    "verdict's exact weight-sensitivity intervals --- the acceptance-side\n"
    "analogue of the sensitivity analyses applied to composite-indicator\n"
    "rankings (Nardo et al., 2008). Static compensability analyses --- the\n"
    "compensatory potentials of multi-criteria methods for sustainability\n"
    "assessment (Cinelli, Coles, and Kirwan, 2014) and the partial\n"
    "compensability of the outranking approach (Sch\\\"ar, Pohl, and\n"
    "Geldermann, 2025) --- classify aggregation behaviour at a fixed profile;\n"
    "the separation established here acts one level up, in the acceptance\n"
    "protocol over a transition, and arises even where every static level of\n"
    "the index is reported correctly (Remark 2).\n\n"
    "Against this background, the finite-menu characterization of",
)

# =====================================================================
# OP 10 — Conclusions: the three-constituency paragraph
# =====================================================================
edit(
    "conclusions-three-constituencies",
    "temporal alternation alone does not provide it.\n\n\\section*{List of abbreviations}",
    "temporal alternation alone does not provide it.\n\n"
    "Read from each of the three literatures this paper connects, the results\n"
    "take one specific form. For multi-criteria assessment, they locate the\n"
    "certification failure of compensatory aggregates in the acceptance\n"
    "protocol --- not in weight choice, and not in compensability at fixed\n"
    "profiles. For decision making under uncertainty, the acceptance gap\n"
    "measures the value of information about the assessment weight, and\n"
    "Theorem 9 with Proposition 10 identifies menu convexification, not\n"
    "temporal sharing, as what removes it. For transition management, where\n"
    "separately-binding floors govern a transition, per-floor reporting along\n"
    "the path is the detection requirement the separation makes exact.\n\n"
    "\\section*{List of abbreviations}",
)

# =====================================================================
# OP 14 — keywords trimmed to seven (the venue's limit)
# =====================================================================
edit(
    "keywords-seven",
    "multi-criteria decision analysis \\sep compensatory and noncompensatory aggregation \\sep composite indicators \\sep scalarization \\sep robustness \\sep sustainability assessment \\sep viability theory \\sep transition safety \\sep quantifier order",
    "multi-criteria decision analysis \\sep compensatory and noncompensatory aggregation \\sep composite indicators \\sep scalarization \\sep robustness \\sep sustainability assessment \\sep transition safety",
)

# =====================================================================
# OP 15 — Section 6.3: the decision-aiding-context paragraph
# =====================================================================
edit(
    "benchmark-decision-context",
    "is not a fitted case study, and no empirical claim is made.\n\n\\textbf{The system.}",
    "is not a fitted case study, and no empirical claim is made.\n\n"
    "Read as a decision problem, the benchmark has the structure of a\n"
    "certification study in multi-criteria decision aiding. The decision\n"
    "maker is the resource authority; the decision alternatives are the\n"
    "menu's management schedules (NO-SWITCH, FAST, SLOW, and the\n"
    "reserve-financed STAGED); the criteria are the two typed floors ---\n"
    "the biomass margin above the limit reference point and the fleet\n"
    "income margin --- evaluated along the whole transition under the\n"
    "declared disturbance; and the scalarization weights are the preference\n"
    "orderings of the assessment doctrine under which the composite index\n"
    "is read. The acceptance gap is then a robustness failure of the\n"
    "decision-aiding process in the precise sense of Theorem 5: at every\n"
    "preference weighting the index licenses some alternative --- possibly\n"
    "a different one at different weightings --- while no single\n"
    "alternative satisfies the criteria path-wise. The deliverables are\n"
    "ones a decision analyst can communicate: the licensing thresholds ---\n"
    "the preference ranges over which each alternative is certified --- and\n"
    "the rescue threshold --- the adjustment funding that converts an\n"
    "unlicensable state into a staged transition. At the asymmetric\n"
    "allocations of the substitutability extension\n"
    "(Section~\\ref{substitutability-spectrum}), the same total margin\n"
    "draws opposite verdicts and opposite management responses, so the\n"
    "certification boundary is operationally decision-relevant.\n\n"
    "\\textbf{The system.}",
)

# =====================================================================
# OP 16 — Section 5.2: the preference-range reading of the thresholds
# =====================================================================
edit(
    "threshold-preference-ranges",
    "The licensing thresholds of Theorem 5(6) give the\n"
    "verdict's exact weight-sensitivity intervals --- the acceptance-side\n"
    "analogue of the sensitivity analyses applied to composite-indicator\n"
    "rankings (Nardo et al., 2008).",
    "The licensing thresholds of Theorem 5(6) give the\n"
    "verdict's exact weight-sensitivity intervals --- the preference ranges\n"
    "over which each plan is certified --- the acceptance-side analogue of\n"
    "the sensitivity analyses applied to composite-indicator rankings\n"
    "(Nardo et al., 2008).",
)

# =====================================================================
# OP 12 — References: four canonical MCDA entries (alphabetical)
# =====================================================================
edit(
    "ref-keeney",
    "\\emph{Ecological Economics}, 167, 106331.\n\nLade, S. J.,",
    "\\emph{Ecological Economics}, 167, 106331.\n\n"
    "Keeney, R. L., and Raiffa, H. (1976). \\emph{Decisions with Multiple\n"
    "Objectives: Preferences and Value Tradeoffs}. Wiley, New York.\n\n"
    "Lade, S. J.,",
)
edit(
    "ref-munda",
    "61(2), 183--197.\n\nNardo, M., Saisana, M.,",
    "61(2), 183--197.\n\n"
    "Munda, G. (2005). Multiple criteria decision analysis and sustainable\n"
    "development. In: Figueira, J., Greco, S., and Ehrgott, M. (eds.),\n"
    "\\emph{Multiple Criteria Decision Analysis: State of the Art Surveys}.\n"
    "Springer, New York, 953--986.\n\n"
    "Nardo, M., Saisana, M.,",
)
edit(
    "ref-roy",
    "\\emph{Nature}, 461, 472--475.\n\nSaint-Pierre, P. (1994).",
    "\\emph{Nature}, 461, 472--475.\n\n"
    "Roy, B. (1996). \\emph{Multicriteria Methodology for Decision Aiding}.\n"
    "Kluwer Academic Publishers, Dordrecht.\n\n"
    "Saint-Pierre, P. (1994).",
)
edit(
    "ref-vincke",
    "\\emph{One Ecosystem}, 10, e141086.\n\nvon Neumann, J. (1928).",
    "\\emph{One Ecosystem}, 10, e141086.\n\n"
    "Vincke, P. (1992). \\emph{Multicriteria Decision-Aid}. Wiley, Chichester.\n\n"
    "von Neumann, J. (1928).",
)

# =====================================================================
# GATE 1 — inverse reconstruction: revert every operation in reverse
# order and require byte-identity with v60.
# =====================================================================
recon = text
for name, anchor, repl, count in reversed(PAIRS):
    if recon.count(repl) < count:
        die(f"inverse gate: replacement of [{name}] found {recon.count(repl)}x, expected {count}")
    recon = recon.replace(repl, anchor, count)
if recon != orig:
    k = next((i for i, (a, b) in enumerate(zip(recon, orig)) if a != b), min(len(recon), len(orig)))
    die(f"inverse reconstruction gate: reverted text != v60 (first divergence at offset {k}:\nRECON: ...{recon[max(0,k-80):k+80]!r}\nV60:    ...{orig[max(0,k-80):k+80]!r})")
print("  ok  inverse reconstruction: byte-exact revert to v60")

# =====================================================================
# GATE 2 — math-span multiset accounting: UNCHANGED (every operation
# is prose-level; zero spans added, zero removed, zero altered).
# =====================================================================
SPAN = re.compile(r"\\\((?:[^\\]|\\.)*?\\\)|\\\[.*?\\\]", re.S)


def spans(s):
    return Counter(SPAN.findall(s))


s60, s61 = spans(orig), spans(text)
if s61 != s60:
    only60 = s60 - s61
    only61 = s61 - s60
    die(f"math-span multiset mismatch (expected zero delta).\nspans lost: {dict(only60)}\nspans gained: {dict(only61)}")
print(f"  ok  math-span multiset: {sum(s60.values())} -> {sum(s61.values())} (unchanged, as designed)")

# =====================================================================
# GATE 3 — marker accounting: every new marker present, every retired
# marker absent.
# =====================================================================
NEW_MARKERS = [
    "\\journal{Journal of Multi-Criteria Decision Analysis}",
    "% v61 (JMCDA alignment wave, 2026-09-22)",
    "% v60 (editorial wave, 2026-09-22)",
    "In multi-criteria assessment, compensatory and noncompensatory",
    "aggregation give two readings of the same constraint set",
    "the two readings as robust transition-safety problems",
    "multi-criteria decision analysis \\sep compensatory and noncompensatory aggregation \\sep composite indicators \\sep scalarization \\sep robustness \\sep sustainability assessment \\sep transition safety",
    "Compensatory and noncompensatory (weak- and strong-sustainability) criteria are compared",
    "The compensability\nquestion itself is foundational in multi-criteria decision analysis:",
    "orthogonal to all of these: even if weights perfectly reflect\nimportance and substitution rates are elicited faithfully",
    "In the vocabulary of decision making under\nuncertainty, the two protocols differ in when the plan is fixed relative",
    "the here-and-now versus wait-and-see distinction of\nadjustable robust optimization (Ben-Tal et al., 2004), with the weight\nin the role of the uncertain parameter.",
    "are acceptance semantics",
    "the sorting problematic of decision aiding (Roy,\n1996; Vincke, 1992)",
    "a transition is accepted when every weighting licenses some plan,\npossibly a different plan for each weighting",
    "give the\nverdict's exact weight-sensitivity intervals",
    "the acceptance-side analogue of\nthe sensitivity analyses applied to composite-indicator rankings\n(Nardo et al., 2008)",
    "acts one level up, in the acceptance\nprotocol over a transition",
    "Read from each of the three literatures this paper connects",
    "identifies menu convexification, not\ntemporal sharing, as what removes it",
    "per-floor reporting along\nthe path is the detection requirement the separation makes exact.",
    "Read as a decision problem, the benchmark has the structure of a",
    "a robustness failure of the\ndecision-aiding process in the precise sense of Theorem 5",
    "the preference ranges over which each alternative is certified",
    "certification boundary is operationally decision-relevant.",
    "the preference ranges\nover which each plan is certified",
    "Keeney, R. L., and Raiffa, H. (1976)",
    "Munda, G. (2005). Multiple criteria decision analysis and sustainable",
    "Roy, B. (1996). \\emph{Multicriteria Methodology for Decision Aiding}.",
    "Vincke, P. (1992). \\emph{Multicriteria Decision-Aid}.",
]
OLD_MARKERS = [
    "\\jel{C61; C62; D81; Q01; Q56}",
    "\\providecommand{\\jel}",
    "JEL classification",
    "Sustainability criteria divide into scalarized criteria",
    "sustainability \\sep viability theory \\sep robust control \\sep scalarization",
    "Scalarized and coordinate-wise sustainability criteria are compared",
    "is orthogonal to both: even if weights perfectly reflect importance,",
    "viability theory \\sep transition safety \\sep quantifier order",
    "This paper compares the two as\nrobust transition-safety problems",
]
for m in NEW_MARKERS:
    if m not in text:
        die(f"marker accounting: new marker missing: {m[:90]!r}")
for m in OLD_MARKERS:
    if m in text:
        die(f"marker accounting: retired marker still present: {m[:90]!r}")
print(f"  ok  marker accounting: {len(NEW_MARKERS)} new present, {len(OLD_MARKERS)} retired absent")

# =====================================================================
# GATE 4 — structure pins: environments, items, and headings unchanged.
# =====================================================================
for env in ("enumerate", "itemize", "figure", "table", "longtable", "abstract", "keyword", "highlights", "frontmatter"):
    b, e = text.count(f"\\begin{{{env}}}"), text.count(f"\\end{{{env}}}")
    ob, oe = orig.count(f"\\begin{{{env}}}"), orig.count(f"\\end{{{env}}}")
    if b != e:
        die(f"structure pin: unbalanced {env} ({b} begin / {e} end)")
    if (b, e) != (ob, oe):
        die(f"structure pin: {env} count changed {ob}->{b}")
if text.count("\\item") != orig.count("\\item"):
    die(f"structure pin: \\item count changed {orig.count(chr(92)+'item')}->{text.count(chr(92)+'item')}")
for heading in ("\\section{Introduction}", "\\section{Interpretation}", "\\section{Conclusions}",
                "\\subsection{Positioning against established", "\\section*{References}",
                "\\section*{List of abbreviations}", "\\section*{Declarations}"):
    if text.count(heading) != orig.count(heading):
        die(f"structure pin: heading count changed: {heading}")
print("  ok  structure pins: environments, items, and headings unchanged")

# =====================================================================
# GATE 5 — register sweep: the v60 banned list plus the venue register
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
print(f"\nWROTE {DST.name}: {nlines} lines (v60: {orig.count(chr(10)) + 1})")
print("ALL GATES GREEN")
