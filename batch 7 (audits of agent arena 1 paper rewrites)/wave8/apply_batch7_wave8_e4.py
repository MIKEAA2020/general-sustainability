#!/usr/bin/env python3
"""E4 v13 (wave-8 owner-directed presentation pass).

Changes:
  1. The version-log paragraph before the abstract is removed.
  2. The abstract is tightened from 374 to under 315 words. Every
     verdict, value, and caveat is preserved (the 615.72-ft attractor,
     the 13-year kernel emptiness, the 7.2%/31.5% securing cut, the
     nominal +3.3%/+0.4% margins and their hybrid-quantity status, the
     0.4% trigger lag, the T = 3-year certified bound and its
     optimistic-defect qualifier, the 660-ft nothing-retained verdict,
     and the three-year certified-claims limit). The cuts are phrasal:
     the duplicated "This paper provides such a score" frame, the
     1934-1990 window gloss, the flat-cap enumeration (carried in the
     body), and connective redundancy.
  3. Keywords 5 -> 7: "viability kernel" and "groundwater governance"
     added.
Fail-loud; byte-reproducible; writes paperE4_edwards_intervention_v13.md.
"""
from __future__ import annotations
import hashlib
import re
from pathlib import Path

SRC = Path(__file__).resolve().parents[2] / "arena agent 1/paper rewrites"
OLD = SRC / "paperE4_edwards_intervention_v12.md"
NEW = SRC / "paperE4_edwards_intervention_v13.md"

text = OLD.read_text()
orig = text


def rep(old: str, new: str, n: int = 1):
    global text
    assert text.count(old) == n, f"needle x{text.count(old)} (want {n}): {old[:90]!r}"
    text = text.replace(old, new)


# --- 1. remove the version-log paragraph -------------------------------
m = re.search(r"\*Version log \(v12\)\.\*[^\n]*\n\n", text)
assert m, "version log paragraph not found"
text = text[:m.start()] + text[m.end():]
assert "*Version log" not in text

# --- 2. the abstract: four paragraphs, replaced wholesale ---------------
ABSTRACT_OLD = text.split("## Abstract\n\n", 1)[1].split("\n\n**Keywords:**", 1)[0]
assert ABSTRACT_OLD.startswith("**Problem.**"), ABSTRACT_OLD[:60]

ABSTRACT_NEW = """**Problem.** Drought management in permitted groundwater systems relies on triggers and pumping reductions; the protection competing rules deliver under adverse recharge is rarely scored against a fixed criterion.

**Approach.** We compute robust viability kernels of the J-17 annual-mean head for a declared policy family — training-mean pumping (282.16 × 10³ acre-ft yr⁻¹, not current use), flat caps of 0–90%, a Stage-I reactive rule, and the critical-period-management (CPM) cascade — under persistent drought-floor recharge. A non-BAU policy is retained only if at least as protective as training-mean pumping and more permissive than the smallest securing flat cap, under a protocol frozen before any score was computed.

**Results.** At the 618-ft physical threshold under the drought-of-record floor, training-mean pumping's worst-case attractor (615.72 ft) lies below the threshold, its kernel emptying beyond 13 years; every flat cut of 10% or deeper and both reactive rules make the safe set invariant; the smallest securing cut is interpolated 7.2% of training mean pumping (31.5% of current). The reactive rules are retained **nominally** at 618 ft under the mildest floor class only: their supply margins (+3.3% Stage I, +0.4% cascade, against the kernel-matched flat-90% cap) are hybrid — worst-case protection against wet-year replay entitlement the robust class excludes — and under the floor classes a 0.4% trigger lag. Retention is **not** certified (certified positive-pumping kernels empty beyond T = 3 years, a bound the out-of-sample defect makes optimistic), and **nothing is retained at 660 ft**, where the reactive rules are invisible to the kernel of their own trigger — a geometric property of trigger design (the cascade's purpose is springflow protection near 618 ft, not head invariance).

**Implications.** Reactive rules match flat-cap protection at the physical threshold and seem generous only if wet-year pumping counts; the 660-ft threshold is protected by wet years, not the pumping family; certified claims are limited to three years by the fitted defect."""

rep(ABSTRACT_OLD, ABSTRACT_NEW)
nwords = len(re.findall(r"\S+", ABSTRACT_NEW))
assert nwords < 315, nwords

# --- 3. keywords 5 -> 7 -------------------------------------------------
rep("**Keywords:** Edwards Aquifer; critical period management; J-17 index "
    "well; pumping policies; robust viability",
    "**Keywords:** Edwards Aquifer; critical period management; J-17 index "
    "well; pumping policies; robust viability; viability kernel; "
    "groundwater governance")

NEW.write_text(text)

# --- verification ---------------------------------------------------------
def abstract_words(t):
    lines = t.split("\n")
    a = next(i for i, l in enumerate(lines) if l.strip() == "## Abstract")
    b = next(i for i in range(a + 1, len(lines)) if lines[i].startswith("## "))
    body = [l for l in lines[a + 1:b] if l.strip() and not l.startswith("**Keywords")
            and not l.startswith("**Article Impact")]
    return sum(len(re.findall(r"\S+", l)) for l in body)

assert abstract_words(text) == nwords < 315, (abstract_words(text), nwords)
kw = next(l for l in text.split("\n") if l.startswith("**Keywords"))
assert len(kw.split(";")) == 7, kw
for needle in ["615.72 ft", "13 years", "7.2%", "31.5%", "+3.3%", "+0.4%",
               "T = 3 years", "660 ft", "618-ft", "282.16"]:
    assert needle in text, needle
for banned in ["*Version log", "at this revision", "of earlier version"]:
    assert banned not in text, banned


def table_lines(t):
    return [l for l in t.split("\n") if l.lstrip().startswith("|")]


assert table_lines(text) == table_lines(orig), "table rows changed"

print("E4 v13 written;", len(orig), "->", len(text), "chars")
print("abstract words:", nwords)
print("MD5:", hashlib.md5(text.encode()).hexdigest())
