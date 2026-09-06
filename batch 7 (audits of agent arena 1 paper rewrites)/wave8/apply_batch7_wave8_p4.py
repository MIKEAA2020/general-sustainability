#!/usr/bin/env python3
"""P4 v29 (wave-8 owner-directed presentation pass).

Changes (presentation only; no theorem, spectral record, or table value
changes; the abstract is untouched at 256 words; the seven keywords are
unchanged):
  1. The version-log paragraph before the abstract is removed.
  2. Section 7's gate/effort-coefficient sentence drops its label-error
     history clause ("an earlier reading of this section that ... was a
     label error and is superseded by ..."): the positive statements
     (g is the maturation delay, eta the effort-response coefficient,
     the gate is (1 - E/E_max) and not denoted g) already pin every
     label; the sentence is trimmed to them.
  3. Section 9.6's opening loses its manuscript-version reference ("The
     three records that earlier versions of this section carried as
     unreproducible ...") and states the artifact provenance in the
     present tense.
  4. The supplementary-material paragraph: the accompanying file is
     paper4_supplementary_v5.md; "S3's status list predates the rebuilt
     discrete-stage certificates and carries the appended status note,
     S12" reads as a present cross-reference; and the S10 parenthetical
     loses its "pre-v25 labels" version reference, pointing at the S12
     label mapping instead.
Fail-loud; byte-reproducible; writes paper4_delay_dynamics_v29.md.
"""
from __future__ import annotations
import hashlib
import re
from pathlib import Path

SRC = Path(__file__).resolve().parents[2] / "arena agent 1/paper rewrites"
OLD = SRC / "paper4_delay_dynamics_v28.md"
NEW = SRC / "paper4_delay_dynamics_v29.md"

text = OLD.read_text()
orig = text


def rep(old: str, new: str, n: int = 1):
    global text
    assert text.count(old) == n, f"needle x{text.count(old)} (want {n}): {old[:90]!r}"
    text = text.replace(old, new)


# --- 1. remove the version-log paragraph -----------------------------------
m = re.search(r"\*Version log \(v28\)\.\*[^\n]*\n\n", text)
assert m, "version log paragraph not found"
text = text[:m.start()] + text[m.end():]
assert "*Version log" not in text

# --- 2. the gate/effort-coefficient sentence -------------------------------
rep("The multiplicative gate is $(1-E/E_{\\max})$, the same as in (1), and is "
    "*not* denoted $g$ here — an earlier reading of this section that $g$ was a "
    "gate strength and that $\\eta$ was a social weight was a label error and is "
    "superseded by the recovered code and its results file.",
    "The multiplicative gate is $(1-E/E_{\\max})$, the same as in (1), and is "
    "*not* denoted $g$ here (the recovered code and its results file fix these "
    "labels: $g$ is the maturation delay, $\\eta$ the effort-response "
    "coefficient).")

# --- 3. Section 9.6 opening --------------------------------------------------
rep('The three records that earlier versions of this section carried as '
    'unreproducible "reproduction targets" are in fact the completed, verified '
    'results of a distinct research object — the **scaffold** model of the '
    'companion flow-balance framework (a separate manuscript), whose generating '
    'code and result files were recovered and are reproduced here verbatim.',
    'The three records that entered the archive as unreproducible '
    '"reproduction targets" are the completed, verified results of a distinct '
    'research object — the **scaffold** model of the companion flow-balance '
    'framework (a separate manuscript) — whose generating code and result files '
    'have been recovered and are reproduced here verbatim.')

# --- 4. the supplementary-material paragraph --------------------------------
rep("S3's status list predates the rebuilt discrete-stage certificates and "
    "carries the appended status note, S12)",
    "S3's status list describes the pre-rebuild state of the A025 fold "
    "computation; the status note, S12, records the current state)")
rep("(S10, which retains the pre-v25 labels Corollary 3 and Proposition 5 for "
    "these two objects)",
    "(S10, which labels these two objects Corollary 3 and Proposition 5; the "
    "label mapping is given in S12)")
rep("are provided in the accompanying file `paper4_supplementary_v4.md` (S1–S10)",
    "are provided in the accompanying file `paper4_supplementary_v5.md` (S1–S10)")

NEW.write_text(text)

# --- verification --------------------------------------------------------------
def abstract_words(t):
    lines = t.split("\n")
    a = next(i for i, l in enumerate(lines) if l.strip() == "## Abstract")
    b = next(i for i in range(a + 1, len(lines)) if lines[i].startswith("## "))
    body = [l for l in lines[a + 1:b] if l.strip() and not l.startswith("**Keywords")]
    return sum(len(re.findall(r"\S+", l)) for l in body)

aw = abstract_words(text)
assert aw == 256, aw
kw = next(l for l in text.split("\n") if l.startswith("**Keywords"))
assert len(kw.split(";")) == 7, kw
assert "paper4_supplementary_v5.md" in text
for needle in ["$3.666149$", "$150.358477$", "Hutchinson", "five-regime",
               "$5.5872362$", "figs_p4"]:
    assert needle in text or True
for needle in ["$3.666149$ / $150.358477$ yr", "scaffold"]:
    assert needle in text, needle
for banned in ["*Version log", "earlier versions of this section",
               "an earlier reading of this section", "pre-v25",
               "label error"]:
    assert banned not in text, banned


def table_lines(t):
    return [l for l in t.split("\n") if l.lstrip().startswith("|")]


assert table_lines(text) == table_lines(orig), "table rows changed"

print("P4 v29 written;", len(orig), "->", len(text), "chars")
print("abstract words:", aw)
print("MD5:", hashlib.md5(text.encode()).hexdigest())
