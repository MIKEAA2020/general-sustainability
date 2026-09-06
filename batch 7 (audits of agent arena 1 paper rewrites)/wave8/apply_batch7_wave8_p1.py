#!/usr/bin/env python3
"""P1 v22 (wave-8 owner-directed presentation pass).

Changes:
  1. The version-log paragraph before the abstract is removed.
  2. Keywords 6 -> 7: "capital substitution" added (the core
     weak/strong-sustainability debate term).
  3. Figure 1 points at the regenerated figure
     figs_p1/fig1_witness_v22.png (the "intermediate weights" /
     "license both" annotation and the s_2 = 2 leg label repositioned
     into clear space; built by make_fig_p1_v22.py). The caption is
     unchanged - the figure's contract is the same.
  4. The supplementary-material pointer names the new supplementary
     file paper1_supplementary_v3.md.
The abstract is untouched (299 words, under 315).
Fail-loud; byte-reproducible; writes paper1_assessment_separation_v22.md.
"""
from __future__ import annotations
import hashlib
import re
from pathlib import Path

SRC = Path(__file__).resolve().parents[2] / "arena agent 1/paper rewrites"
OLD = SRC / "paper1_assessment_separation_v21.md"
NEW = SRC / "paper1_assessment_separation_v22.md"

text = OLD.read_text()
orig = text


def rep(old: str, new: str, n: int = 1):
    global text
    assert text.count(old) == n, f"needle x{text.count(old)} (want {n}): {old[:90]!r}"
    text = text.replace(old, new)


# --- 1. remove the version-log paragraph --------------------------------
m = re.search(r"\*Version log \(v21\)\.\*[^\n]*\n\n", text)
assert m, "version log paragraph not found"
text = text[:m.start()] + text[m.end():]
assert "*Version log" not in text

# --- 2. keywords 6 -> 7 ---------------------------------------------------
rep("**Keywords:** sustainability assessment; weak and strong sustainability; "
    "compensatory aggregation; scalarization; viability theory; composite indicators",
    "**Keywords:** sustainability assessment; weak and strong sustainability; "
    "compensatory aggregation; scalarization; viability theory; composite "
    "indicators; capital substitution")

# --- 3. Figure 1 path -----------------------------------------------------
rep("![Figure 1](figs_p1/fig1_witness.png)",
    "![Figure 1](figs_p1/fig1_witness_v22.png)")

# --- 4. supplementary filename --------------------------------------------
rep("are provided in the accompanying supplementary file `paper1_supplementary_v2.md`",
    "are provided in the accompanying supplementary file `paper1_supplementary_v3.md`")

NEW.write_text(text)

# --- verification -----------------------------------------------------------
def abstract_words(t):
    lines = t.split("\n")
    a = next(i for i, l in enumerate(lines) if l.strip() == "## Abstract")
    b = next(i for i in range(a + 1, len(lines)) if lines[i].startswith("## "))
    body = [l for l in lines[a + 1:b] if l.strip() and not l.startswith("**Keywords")
            and not l.startswith("**Mathematics")]
    return sum(len(re.findall(r"\S+", l)) for l in body)

aw = abstract_words(text)
assert aw == 299, aw
kw = next(l for l in text.split("\n") if l.startswith("**Keywords"))
assert len(kw.split(";")) == 7, kw
assert "figs_p1/fig1_witness_v22.png" in text
assert "paper1_supplementary_v3.md" in text
for needle in ["$\\mathfrak{S}$", "relative interior", "witness menu", "Theorem 5"]:
    assert needle in text, needle


def table_lines(t):
    return [l for l in t.split("\n") if l.lstrip().startswith("|")]


assert table_lines(text) == table_lines(orig), "table rows changed"

print("P1 v22 written;", len(orig), "->", len(text), "chars")
print("abstract words:", aw)
print("MD5:", hashlib.md5(text.encode()).hexdigest())
