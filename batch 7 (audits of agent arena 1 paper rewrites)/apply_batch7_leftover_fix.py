"""
apply_batch7_leftover_fix.py
----------------------------
Builds, non-destructively (fail-loud exact-match replacements only):

  arena agent 1/paper rewrites/paperE2_cod_intervention_v18.md  (from v17)

E2 v18 fixes the registered residual of the Task-70 verification record
(E2_V17_E3_V12_VERIFICATION.md, "Registered residual" block): the three
"SSE" labels of Section 3.6 are one-word mislabels of the fit statistic.
The committed fit objective (wave_e_cod/src/run_ladder.py, fit_params) is
the mean squared error per transition (np.mean((pred - dS)**2), n = 24
transitions), so 12,772.2 = 306,532.1/24 (Schaefer), 7,690.1 (Allee refit),
and 9,330.0 (declared-strength alternative) are MSEs, not SSEs. All three
were re-verified computationally against wave_e_cod/data/ before this fix
(r = 0.2369, K = 5000 pinned, Schaefer SSE 306,532.1, MSE 12,772.2; Allee
r = 2.0, K = 1671.7, s0 = 642.3, MSE 7,690.1; s0 = 442.3 refit r = 2.0,
K = 3223.7, MSE 9,330.0, SSE 223,920.8).

Owner acceptance of the registered one-word fix is recorded in the version
log. No value, kernel, boundary, verdict, or any other text changes: the
Fox paragraph of the same section already labels its 13,873.1 correctly as
an MSE, and Section 3.7 uses the (correct) generic "fit cost".
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
PAPERS = os.path.join(REPO, "arena agent 1", "paper rewrites")

SRC = os.path.join(PAPERS, "paperE2_cod_intervention_v17.md")
DST = os.path.join(PAPERS, "paperE2_cod_intervention_v18.md")


def replace_once(text: str, old: str, new: str, tag: str) -> str:
    n = text.count(old)
    if n != 1:
        sys.exit(f"FAIL [{tag}]: expected exactly 1 occurrence, found {n}.\n--- target start ---\n{old[:200]}\n--- target end ---")
    return text.replace(old, new, 1)


with open(SRC, encoding="utf-8") as f:
    e2 = f.read()

# --- (1) version log: replace v17's log with v18's (each version's file carries
# only its own log; the v17 file remains the preserved baseline) ---
V18_LOG = """*Version log (v18).* Fixes the registered residual of the external-audit verification record, at the owner's accepted direction: non-destructive and label-level only — no value, kernel, boundary, verdict, or other text changes anywhere. The three "SSE" labels of Section 3.6 are corrected to "MSE": the committed fit objective is the mean squared error per transition ($n = 24$ transitions), so $12{,}772.2$ kt$^2$ (= $306{,}532.1/24$, Schaefer), $7690.1$ kt$^2$ (depensatory refit), and $9330.0$ kt$^2$ (declared-strength alternative) are MSEs; the Fox paragraph of the same section already labelled its $13{,}873.1$ kt$^2$ as an MSE, and Section 3.7's "fit cost" wording is convention-neutral and unchanged. All four numbers were re-verified against the committed data and objective before the relabelling. The v17 narrative remains available as the baseline.
"""

_v17_log_start = "*Version log (v17).*"
_v17_log_end = "The v16 narrative remains available as the baseline."
_i = e2.find(_v17_log_start)
if _i < 0:
    sys.exit("FAIL [E2 v18 version log]: v17 log start marker not found.")
_j = e2.find(_v17_log_end, _i)
if _j < 0:
    sys.exit("FAIL [E2 v18 version log]: v17 log end marker not found.")
_j += len(_v17_log_end)
e2 = e2[:_i] + V18_LOG.strip() + e2[_j:]


# --- (2) first SSE mislabel: the depensatory refit paragraph ---
e2 = replace_once(
    e2,
    "with residual SSE $7690.1$ kt$^2$ against $12{,}772.2$ kt$^2$ for the registered Schaefer form",
    "with residual MSE $7690.1$ kt$^2$ against $12{,}772.2$ kt$^2$ for the registered Schaefer form",
    "E2 §3.6 first label (refit vs registered)",
)

# --- (3) same paragraph, the convention-independence sentence ---
e2 = replace_once(
    e2,
    "The bare fit parameters and the SSE are convention-independent",
    "The bare fit parameters and the MSE are convention-independent",
    "E2 §3.6 second label (convention sentence)",
)

# --- (4) the Reason paragraph's declared-strength alternative ---
e2 = replace_once(
    e2,
    "(SSE $9330.0$ kt$^2$)",
    "(MSE $9330.0$ kt$^2$)",
    "E2 §3.6 third label (declared-strength alternative)",
)

# --- sanity: no "SSE" token remains anywhere in the body (the version log
# itself legitimately mentions the retired label when describing the fix) ---
_body = e2.replace(V18_LOG.strip(), "")
if "SSE" in _body:
    sys.exit("FAIL [final sweep]: an 'SSE' token still remains in the built v18 body.")

with open(DST, "w", encoding="utf-8") as f:
    f.write(e2)

print("wrote:", DST)
print("SSE tokens in v18 body (outside the version log):", _body.count("SSE"), "(expected 0)")
print("MSE tokens in v18:", e2.count("MSE"))
