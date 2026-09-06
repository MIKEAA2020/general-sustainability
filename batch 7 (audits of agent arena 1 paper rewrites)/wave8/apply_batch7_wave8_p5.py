#!/usr/bin/env python3
"""P5 v24 (wave-8 owner-directed presentation pass).

Changes:
  1. The version-log paragraph before the abstract is removed.
  2. The abstract is tightened from 354 to under 315 words. Every
     claim, value, and scoping statement is preserved (forward
     invariance; the rapid-review-limit scope; the 6.5-yr Neimark-
     Sacker-type crossing; the command-step-artefact reading; the
     archived-regions provisionality and the q = 0.1 catchability
     flip; the operator-distinctness thesis; the screen's null
     result; the cod descriptive split; the closing design-parameter
     reading). The cuts are phrasal (compressed clauses, dropped
     restatements).
  3. Keywords 6 -> 7 and reselected for contribution emphasis:
     "stability" (too generic alone) is replaced by "sampled-data
     control" and "Neimark–Sacker bifurcation" (the paper's named
     crossing signature).
  4. Figure 1 points at the regenerated figure
     figs_p5/fig1_crossing_record_v24.png (compact centred title and
     legend replacing the full-width clipped title; row labels use
     the paper's own channel vocabulary "Extractive/Protective",
     matching the caption; built by make_fig_p5_v24.py).
  5. Section 3.3: "the unit-circle crossing record ... is now
     complete" -> "is complete"; the scan note "(seed-free; the
     record reproduces the registered numbers before extension)" ->
     "(seed-free; it reproduces the registered numbers on the range
     they cover)".
  6. Appendix A's "previously carried in the main flow" -> present
     tense.
  7. The Supplementary-material statement names the accompanying
     file paper5_supplementary_v5.md.
Fail-loud; byte-reproducible; writes paper5_sampled_governance_v24.md.
"""
from __future__ import annotations
import hashlib
import re
from pathlib import Path

SRC = Path(__file__).resolve().parents[2] / "arena agent 1/paper rewrites"
OLD = SRC / "paper5_sampled_governance_v23.md"
NEW = SRC / "paper5_sampled_governance_v24.md"

text = OLD.read_text()
orig = text


def rep(old: str, new: str, n: int = 1):
    global text
    assert text.count(old) == n, f"needle x{text.count(old)} (want {n}): {old[:90]!r}"
    text = text.replace(old, new)


# --- 1. remove the version-log paragraph ------------------------------------
m = re.search(r"\*Version log \(v23\)\.\*[^\n]*\n\n", text)
assert m, "version log paragraph not found"
text = text[:m.start()] + text[m.end():]
assert "*Version log" not in text

# --- 2. the abstract: four paragraphs, replaced wholesale ---------------------
lines = text.split("\n")
a = next(i for i, l in enumerate(lines) if l.strip() == "## Abstract")
k = next(i for i in range(a + 1, len(lines))
         if lines[i].startswith("**Keywords") or lines[i].startswith("**Box 1"))
ABSTRACT_OLD = "\n".join(lines[a + 1:k]).strip()
assert ABSTRACT_OLD.startswith("Fisheries governance is periodic"), ABSTRACT_OLD[:60]

ABSTRACT_NEW = """Fisheries governance is periodic: assessments are compiled at fixed cadences, decisions taken at review points, and controls held until the next review. Real institutions therefore operate a sampled-control loop — observation and update occur at discrete review times — an architecture we call *sample-and-hold governance*. The formal literature instead represents institutional response as a continuous-time delay or an annual discrete step on a surplus-production model; neither matches the operating object, and substituting either can move or delete stability boundaries.

We analyse a logistic stock under held effort between reviews, with a filtered deficit signal carrying institutional memory and a projected Euler update resetting effort at each review. The sampled state space is forward invariant by induction; the rapid-review limit is a finite-horizon consistency statement, not a stability claim. The logistic hold map's equilibrium multipliers cross the unit circle at a review interval near 6.5 yr (a Neimark–Sacker-type crossing); thresholds reported by first-order discretisation are command-step artefacts. The archived stage-structured response regions are provisional (their generating computation was never attached) and not robust to the catchability scale the stage record never declares: at $q = 0.1$ every class's annual-review verdict flips, making that comparison uninformative rather than a non-reproduction. The sample-and-hold map and the continuous-delay equation are distinct operators; stability does not transfer in general between them.

A multiplicity-controlled Lomb–Scargle screen of 42 annually assessed stocks finds no target-band discoveries; a structured search across more than thirty systems returns zero eligible cases. The northern cod case yields a descriptive split: the crash interpretation is formulation-dependent, post-collapse dynamics expose an identification problem the mortality-allocation comparison does not resolve, and a phase-line obstruction shows why no fixed scalar autonomous model reproduces the observed reversals.

The cadence and form of periodic review, not ecological lag alone, determine whether governance stabilises or destabilises a harvested stock; the review interval is a local spectral design parameter."""

rep(ABSTRACT_OLD, ABSTRACT_NEW)
nwords = len(re.findall(r"\S+", ABSTRACT_NEW))
assert nwords < 315, nwords

# --- 3. keywords 6 -> 7 (reselected) -------------------------------------------
rep("**Keywords:** periodic review; sample-and-hold governance; review "
    "interval; institutional delay; fisheries management; stability",
    "**Keywords:** periodic review; sample-and-hold governance; review "
    "interval; institutional delay; sampled-data control; "
    "Neimark–Sacker bifurcation; fisheries management")

# --- 4. Figure 1 path ------------------------------------------------------------
rep("![Figure 1](figs_p5/fig1_crossing_record.png)",
    "![Figure 1](figs_p5/fig1_crossing_record_v24.png)")

# --- 5. Section 3.3 recasts -------------------------------------------------------
rep("the unit-circle crossing record over $[0.2, 200]$ yr is now complete "
    "(Figure 1)",
    "the unit-circle crossing record over $[0.2, 200]$ yr is complete "
    "(Figure 1)")
rep("(seed-free; the record reproduces the registered numbers before extension)",
    "(seed-free; it reproduces the registered numbers on the range they cover)")

# --- 6. Appendix A recast -----------------------------------------------------------
rep("This appendix consolidates the registration meta-text that Sections 2.2, "
    "2.4, and 2.5 previously carried in the main flow, so that the Methods keep "
    "only load-bearing status statements;",
    "This appendix consolidates the registration meta-text out of the Methods — "
    "Sections 2.2, 2.4, and 2.5 — so that the Methods keep only load-bearing "
    "status statements;")

# --- 7. the supplementary-file citation -------------------------------------------------
rep("**Supplementary material** is deposited with this article: the statement "
    "inventory with the status of every main-text statement (S1),",
    "**Supplementary material** is deposited with this article (the accompanying "
    "file `paper5_supplementary_v5.md`): the statement inventory with the status "
    "of every main-text statement (S1),")

NEW.write_text(text)

# --- verification ------------------------------------------------------------------------
def abstract_words(t):
    lines = t.split("\n")
    a = next(i for i, l in enumerate(lines) if l.strip() == "## Abstract")
    body = []
    for l in lines[a + 1:]:
        s = l.strip()
        if s.startswith("**Keywords") or s.startswith("**Box 1") or s.startswith("## "):
            break
        if s:
            body.append(l)
    return sum(len(re.findall(r"\S+", l)) for l in body)

assert abstract_words(text) == nwords < 315, (abstract_words(text), nwords)
kw = next(l for l in text.split("\n") if l.startswith("**Keywords"))
assert len(kw.split(";")) == 7, kw
assert "figs_p5/fig1_crossing_record_v24.png" in text
assert "paper5_supplementary_v5.md" in text
for needle in ["$T_r = 47.536$", "79.143", "6.501", "2.306", "$\\rho = 1.00035$",
               "42", "0.9967"]:
    assert needle in text, needle
for banned in ["*Version log", "is now complete", "previously carried",
               "before extension"]:
    assert banned not in text, banned


def table_lines(t):
    return [l for l in t.split("\n") if l.lstrip().startswith("|")]


assert table_lines(text) == table_lines(orig), "table rows changed"

print("P5 v24 written;", len(orig), "->", len(text), "chars")
print("abstract words:", nwords)
print("MD5:", hashlib.md5(text.encode()).hexdigest())
