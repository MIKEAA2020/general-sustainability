#!/usr/bin/env python3
"""E1 v14 (wave-8 owner-directed presentation pass).

Changes (presentation only; no frozen verdict, score, kernel, or table
value changes; the abstract is untouched at 300 words):
  1. The version-log paragraph before the abstract is removed (the
     journal article carries no change log; the record lives in the
     repository).
  2. A seventh keyword is added: "negative certificate" (the paper's
     named contribution).
  3. The retention-rule disclosure's "completions recorded at this
     revision" loses the version reference: the completions are
     recorded after the scores were computed - the load-bearing
     protocol disclosure, without the manuscript-version pointer.
  4. The DM-layer echo "as the completion records" reads "as the
     protocol disclosure records".
Fail-loud; byte-reproducible; writes paperE1_cod_forecast_ladder_v14.md.
"""
from __future__ import annotations
import hashlib
import re
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parents[2] / "arena agent 1/paper rewrites"
OLD = SRC / "paperE1_cod_forecast_ladder_v13.md"
NEW = SRC / "paperE1_cod_forecast_ladder_v14.md"

text = OLD.read_text()
orig = text


def rep(old: str, new: str, n: int = 1):
    global text
    assert text.count(old) == n, f"needle x{text.count(old)} (want {n}): {old[:90]!r}"
    text = text.replace(old, new)


# --- 1. remove the version-log paragraph (one paragraph, line 5) -----
m = re.search(r"\*Version log \(v13\)\.\*[^\n]*\n\n", text)
assert m, "version log paragraph not found"
text = text[:m.start()] + text[m.end():]
assert "*Version log" not in text

# --- 2. keywords: 6 -> 7 --------------------------------------------
rep("**Keywords:** northern cod; biomass forecasting; surplus production; "
    "forecast evaluation; stock assessment; prediction skill",
    "**Keywords:** northern cod; biomass forecasting; surplus production; "
    "forecast evaluation; stock assessment; prediction skill; negative certificate")

# --- 3. the completion disclosure loses the version reference -------
rep("are completions recorded at this revision, after the scores of Section 3 were computed",
    "are completions recorded after the scores of Section 3 were computed")

# --- 4. the DM-layer echo -------------------------------------------
rep("is immaterial to every recorded verdict, as the completion records.",
    "is immaterial to every recorded verdict, as the protocol disclosure records.")

NEW.write_text(text)

# --- verification ----------------------------------------------------
def abstract_words(t):
    lines = t.split("\n")
    a = next(i for i, l in enumerate(lines) if l.strip() == "## Abstract")
    b = next(i for i in range(a + 1, len(lines)) if lines[i].startswith("## "))
    body = [l for l in lines[a + 1:b] if l.strip() and not l.startswith("**Keywords")]
    return sum(len(re.findall(r"\S+", l)) for l in body)

assert abstract_words(text) == 300, abstract_words(text)
kw = next(l for l in text.split("\n") if l.startswith("**Keywords"))
assert len(kw.split(";")) == 7, kw


def table_lines(t):
    return [l for l in t.split("\n") if l.lstrip().startswith("|")]


assert table_lines(text) == table_lines(orig), "table rows changed"
# E1 frozen-print needles
for needle in ["98 kt for persistence versus 115–206 kt", "265 kt versus 289–488 kt",
               "694–819 kt", "1898 kt", "Table 10"]:
    assert needle in text, needle

print("E1 v14 written;", len(orig), "->", len(text), "chars")
print("MD5:", hashlib.md5(text.encode()).hexdigest())
