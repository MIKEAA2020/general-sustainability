#!/usr/bin/env python3
"""E3 v15 (wave-8 owner-directed presentation pass).

Changes:
  1. The four version-log paragraphs before the abstract (v11-v14) are
     removed; the journal article carries no change log.
  2. The abstract is tightened from 322 to under 315 words (phrasal
     trims only; every value, verdict, and caveat is preserved).
  3. Keywords 5 -> 7: "J-17 index well" and "water balance" added.
  4. The climate-rung comparator deviation loses its version-history
     narration ("corrected in this version", "Earlier versions of this
     paper declared...", "This version corrects..."): the deviation
     record now states the comparator declaration, why the alternative
     (M2m as gate) would be circular, and that the choice changes no
     frozen verdict - the protocol-disclosure content, without the
     manuscript-version references.
  5. "the owner-archived script" (two sites) reads "the archived
     script" / "(archived)".
Fail-loud; byte-reproducible; writes paperE3_edwards_forecast_ladder_v15.md.
"""
from __future__ import annotations
import hashlib
import re
from pathlib import Path

SRC = Path(__file__).resolve().parents[2] / "arena agent 1/paper rewrites"
OLD = SRC / "paperE3_edwards_forecast_ladder_v14.md"
NEW = SRC / "paperE3_edwards_forecast_ladder_v15.md"

text = OLD.read_text()
orig = text


def rep(old: str, new: str, n: int = 1):
    global text
    assert text.count(old) == n, f"needle x{text.count(old)} (want {n}): {old[:90]!r}"
    text = text.replace(old, new)


# --- 1. remove the four version-log paragraphs ------------------------
for tag in ("v11", "v12", "v13", "v14"):
    m = re.search(r"\*Version log \(" + tag + r"\)\.\*[^\n]*\n\n", text)
    assert m, f"version log {tag} not found"
    text = text[:m.start()] + text[m.end():]
assert "*Version log" not in text

# --- 2. abstract trims -------------------------------------------------
rep("— a margin whose bootstrap interval covers zero, so the retention is a "
    "coin-flip recorded by a point-RMSE rule, not a skill claim.",
    "— a margin whose bootstrap interval covers zero: a coin-flip retention "
    "recorded by a point-RMSE rule, not a skill claim.")
rep("it is listed and then declined by a protocol class clause recorded "
    "outside the frozen retention rule.",
    "it is listed and then declined by a protocol class clause outside the "
    "frozen retention rule.")
rep("no signal available at the annual forecast origin recovers that gap.",
    "no signal at the annual forecast origin recovers that gap.")
rep("the one-pool balance, given the year's fluxes, nowcasts the current "
    "year rather than forecasting the next. Multi-year planning should "
    "prefer climatological baselines over persisted recharge.",
    "the one-pool balance, given the year's fluxes, nowcasts rather than "
    "forecasts. Multi-year planning should prefer climatological baselines "
    "to persisted recharge.")

# --- 3. keywords 5 -> 7 ------------------------------------------------
rep("**Keywords:** Edwards Aquifer; groundwater level forecasting; forecast "
    "evaluation; persistence benchmark; prediction skill",
    "**Keywords:** Edwards Aquifer; J-17 index well; groundwater level "
    "forecasting; water balance; forecast evaluation; persistence benchmark; "
    "prediction skill")

# --- 4. the comparator deviation recast --------------------------------
rep('2. **The climate-rung comparator (corrected in this version).** The frozen '
    'Pass-2 protocol document states the climate question as whether a causal '
    'recharge forecast reduces primary RMSE on J-17 "relative to persistence and '
    'relative to M1" — the retained M1. Earlier versions of this paper declared '
    'the climate rung\'s (H2) comparator to be the declined M2m instead and '
    'disclosed the declaration as a protocol kink; that declaration was '
    'inconsistent with the frozen document and circular in the way the external '
    'audit identified: the gate was a model the protocol had itself declined. '
    'This version corrects the comparator to the frozen document\'s M1 (with '
    'persistence); Section 5.4 reports the climate verdict on that gate, and '
    'the M2m margins are retained as a nested-baseline reading rather than as '
    'the gate. The correction changes no frozen verdict — no climate module is '
    'retained under either statement — but it corrects the stated mechanism.',
    '2. **The climate-rung comparator.** The frozen Pass-2 protocol document '
    'states the climate question as whether a causal recharge forecast reduces '
    'primary RMSE on J-17 "relative to persistence and relative to M1" — the '
    'retained M1. The comparator is read accordingly: persistence and M1. '
    'Declaring the declined M2m as the rung\'s (H2) comparator instead would be '
    'inconsistent with the frozen document and circular — the gate would be a '
    'model the protocol had itself declined. Section 5.4 reports the climate '
    'verdict on the declared gate, and the M2m margins are retained as a '
    'nested-baseline reading rather than as the gate. The choice changes no '
    'frozen verdict — no climate module is retained under either statement — '
    'but it fixes the stated mechanism.')

# --- 5. owner-archived -> archived --------------------------------------
rep("the owner-archived script `campaign_e3_dm_uncertainty.py` (in the "
    "batch-7 audit directory)",
    "the archived script `campaign_e3_dm_uncertainty.py` (in the batch-7 "
    "audit directory)")
rep("(owner-archived)", "(archived)")

NEW.write_text(text)

# --- verification -------------------------------------------------------
def abstract_words(t):
    lines = t.split("\n")
    a = next(i for i, l in enumerate(lines) if l.strip() == "## Abstract")
    b = next(i for i in range(a + 1, len(lines)) if lines[i].startswith("## "))
    body = [l for l in lines[a + 1:b] if l.strip() and not l.startswith("**Keywords") and not l.startswith("**Article Impact")]
    return sum(len(re.findall(r"\S+", l)) for l in body)

aw = abstract_words(text)
assert aw < 315, aw
kw = next(l for l in text.split("\n") if l.startswith("**Keywords"))
assert len(kw.split(";")) == 7, kw
for needle in ["14.70 versus 13.23 ft", "12.84 ft", "12.28 ft", "7.55 ft",
               "16.80 ft", "21.11 ft", "0.39 ft", "0.13 ft",
               "campaign_e3_dm_uncertainty.py", "rolling_modern_2007.csv"]:
    assert needle in text, needle
for banned in ["*Version log", "corrected in this version", "Earlier versions",
               "This version corrects", "owner-archived", "external audit"]:
    assert banned not in text, banned


def table_lines(t):
    return [l for l in t.split("\n") if l.lstrip().startswith("|")]


assert table_lines(text) == table_lines(orig), "table rows changed"

print("E3 v15 written;", len(orig), "->", len(text), "chars")
print("abstract words:", aw)
print("MD5:", hashlib.md5(text.encode()).hexdigest())
