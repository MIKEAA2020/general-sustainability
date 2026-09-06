#!/usr/bin/env python3
"""P3 v31 (wave-8 owner-directed presentation pass).

Changes (presentation only; no statement, proof, table row, recorded
value, or verdict changes; the abstract is untouched at 281 words; the
seven keywords are unchanged):
  1. The version-log paragraph before the abstract is removed.
  2. The three "re-lettered from ..." notation parentheticals lose
     their rename history (the disambiguation rationale is kept,
     stated as a present-tense letter-choice):
     - the rho_P table row's "(re-lettered from $\\rho$)" dropped;
     - the chi/eta table row's "(re-lettered from $r$, $\\nu$)" dropped;
     - the Conditional Theorem 15 preamble's "re-lettered from $r$ and
       $\\nu$ so that ..." -> "chosen so that ...".
  3. The Section 3.1 numbering note loses the "audited demotions" /
     "demoted Theorems" narration: the note declares the two-counter
     convention and that Propositions 4, 6, 17, 18, 20 are main-counter
     statements, not layering-counter members.
  4. Two fisheries-paragraph recasts: "neither a demotion of the
     number" -> "(both recorded)"; "now supplied and re-verified" ->
     "supplied and re-verified".
  5. The supplementary pointer names paper3_supplementary_v8.md and
     loses the "pre-v28 status words ... demotion relabels" wording
     ("maps the supplementary's status words to the main text's
     current labels").
Fail-loud; byte-reproducible; writes paper3_material_ledgers_v31.md.
"""
from __future__ import annotations
import hashlib
import re
from pathlib import Path

SRC = Path(__file__).resolve().parents[2] / "arena agent 1/paper rewrites"
OLD = SRC / "paper3_material_ledgers_v30.md"
NEW = SRC / "paper3_material_ledgers_v31.md"

text = OLD.read_text()
orig = text


def rep(old: str, new: str, n: int = 1):
    global text
    assert text.count(old) == n, f"needle x{text.count(old)} (want {n}): {old[:90]!r}"
    text = text.replace(old, new)


# --- 1. remove the version-log paragraph ----------------------------------
m = re.search(r"\*Version log \(v30\)\.\*[^\n]*\n\n", text)
assert m, "version log paragraph not found"
text = text[:m.start()] + text[m.end():]
assert "*Version log" not in text

# --- 2. the re-lettering parentheticals ------------------------------------
rep("| $\\rho_P$ | product-retirement fraction routing $r_P$ to $U$ versus $W$ "
    "(re-lettered from $\\rho$) | §2.3; §4.3; §4.4; §8.1 |",
    "| $\\rho_P$ | product-retirement fraction routing $r_P$ to $U$ versus $W$ | "
    "§2.3; §4.3; §4.4; §8.1 |")
rep("| $\\chi, \\eta$ | hybrid state and primitive-flux vector of Conditional "
    "Theorem 15 (re-lettered from $r$, $\\nu$) | §4.8 |",
    "| $\\chi, \\eta$ | hybrid state and primitive-flux vector of Conditional "
    "Theorem 15 | §4.8 |")
rep("letters local to this statement, re-lettered from $r$ and $\\nu$ so that "
    "$r$ stays the growth rate of Section 2.2 and $\\nu$ a macro parameter of "
    "Section 5.4",
    "letters local to this statement, chosen so that $r$ stays the growth rate "
    "of Section 2.2 and $\\nu$ a macro parameter of Section 5.4")

# --- 3. the Section 3.1 numbering note --------------------------------------
rep(
    '(Numbering note: the two layering propositions of this section carry their own counter, Propositions 1–2; every other numbered statement of this article runs on the single 1–20 sequence counter, whose status words reflect the audited demotions — "Proposition 4", "Proposition 6", "Proposition 17", "Proposition 18", and "Proposition 20" are the demoted Theorems 4, 6, 17, 18, and 20, not further members of the layering counter — so every label is unique and resolves directly; the supplementary’s statement inventory and this offset are reconciled in its S6.)',
    '(Numbering note: the two layering propositions of this section carry their own counter, Propositions 1–2; every other numbered statement of this article runs on the single 1–20 sequence counter, so "Proposition 4", "Proposition 6", "Proposition 17", "Proposition 18", and "Proposition 20" are main-counter statements, not further members of the layering counter — so every label is unique and resolves directly; the supplementary’s statement inventory and this status-word offset are reconciled in its S6.)')

# --- 4. the fisheries-paragraph recasts --------------------------------------
rep("Two disclosures ride the headline site (both recorded, neither a demotion "
    "of the number):",
    "Two disclosures accompany the headline value (both recorded):")
rep("the archived pull's 43-stock list and extract-time series state, now "
    "supplied and re-verified, differ from both public releases",
    "the archived pull's 43-stock list and extract-time series state — supplied "
    "and re-verified — differ from both public releases")

# --- 5. the supplementary pointer ---------------------------------------------
rep("The accompanying file `paper3_supplementary_v7.md` carries:",
    "The accompanying file `paper3_supplementary_v8.md` carries:")
rep("read with the S6 statement-status naming offset, which maps the "
    "supplementary’s pre-v28 status words to the main text’s demotion relabels;",
    "read with the S6 statement-status naming offset, which maps the "
    "supplementary’s status words to the main text’s current labels;")

NEW.write_text(text)

# --- verification ---------------------------------------------------------------
def abstract_words(t):
    lines = t.split("\n")
    a = next(i for i, l in enumerate(lines) if l.strip() == "## Abstract")
    b = next(i for i in range(a + 1, len(lines)) if lines[i].startswith("## "))
    body = [l for l in lines[a + 1:b] if l.strip() and not l.startswith("**Keywords")]
    return sum(len(re.findall(r"\S+", l)) for l in body)

aw = abstract_words(text)
assert aw == 281, aw
kw = next(l for l in text.split("\n") if l.startswith("**Keywords"))
assert len(kw.split(";")) == 7, kw
assert "paper3_supplementary_v8.md" in text
for needle in ["G3P v1.12", "median $3.39$ yr", "$1.79$ yr", "Ricard et al. (2012)",
               "Daly (1990)"]:
    assert needle in text, needle
for banned in ["*Version log", "re-lettered", "audited demotions", "demoted Theorems",
               "neither a demotion", "now supplied"]:
    assert banned not in text, banned


def table_lines(t):
    return [l for l in t.split("\n") if l.lstrip().startswith("|")]


# two notation-table rows lose their "(re-lettered ...)" cells - the only
# table-line changes; everything else must be byte-identical.
tl_new, tl_old = table_lines(text), table_lines(orig)
diff = [l for l in tl_old if l not in tl_new] + [l for l in tl_new if l not in tl_old]
assert len(diff) == 4, diff  # 2 removed + 2 added notation-table rows

print("P3 v31 written;", len(orig), "->", len(text), "chars")
print("abstract words:", aw)
print("MD5:", hashlib.md5(text.encode()).hexdigest())
