#!/usr/bin/env python3
"""Wave-7 build: paperE1_cod_forecast_ladder v12 -> v13.

Quality-scan fixes (owner directive, wave 7, Task 77): presentation-layer only.
1. §2.1: drop the dangling 'critical-zone vocabulary used below' clause (no such vocabulary
   exists below in this manuscript; the DFO 2009 citation is retained).
2. §1 roadmap extended to name §3.5 and §3.6 (the post-freeze layers).
3. §3.2 + Table 10: 'SSE 128.35/127.84' relabelled MSE (the printed training-RMSE pair
   11.29–12.24 kt squares exactly to 127.4–149.9, so the objective is the per-transition MSE;
   the same E2-v18 label class; values untouched).
4. §4: duplicate '(694 of 713 kt)' clause trimmed; duplicate crash clause trimmed.
5. §4: the 600-word paragraph split at two topic boundaries (predictand; log-RMSE).
6. References: DFO 2024a/2024b disambiguation (in-text site updated); DFO 2010 entry dropped
   (never cited, no attribution site); NAFC 2025 entry cited at its two Zenodo sites;
   Cadigan 2016 cited in Table 1's caption (the NCAM model paper).
Non-destructive: no frozen verdict, score, kernel, or table VALUE changes; abstract untouched.
"""
import hashlib, re, sys

SRC = "../../arena agent 1/paper rewrites/paperE1_cod_forecast_ladder_v12.md"
DST = "../../arena agent 1/paper rewrites/paperE1_cod_forecast_ladder_v13.md"

src = open(SRC, encoding="utf-8").read()
text = src
edits = []

def sub_once(old, new, tag):
    global text
    assert text.count(old) == 1, f"FAIL [{tag}]: anchor count {text.count(old)} (expected 1): {old[:90]!r}"
    text = text.replace(old, new, 1)
    edits.append(tag)

# --- 1. critical-zone dangling clause (keep the DFO 2009 citation) ---
sub_once(
 "(the precautionary-approach framework of DFO, 2009, governs the critical-zone vocabulary used below)",
 "(the precautionary-approach framework of DFO, 2009)",
 "critical-zone clause")

# --- 2. §1 roadmap names §3.5/§3.6 ---
sub_once(
 "the alternative assessment specification (3.3), and prey-informed productivity (3.4).",
 "the alternative assessment specification (3.3), prey-informed productivity (3.4), the post-freeze Diebold–Mariano and block-bootstrap uncertainty layer (3.5), and the fitted parameters as printed (3.6).",
 "roadmap 3.5/3.6")

# --- 3. SSE->MSE relabels (labels only; values untouched) ---
sub_once(
 "nearly flat at their minima (SSE 128.35 versus 127.84 kt²)",
 "nearly flat at their minima (MSE 128.35 versus 127.84 kt²)",
 "3.2 SSE->MSE")
sub_once(
 "training SSE $128.35$ kt²",
 "training MSE $128.35$ kt²",
 "Table10 row1 SSE->MSE")
sub_once(
 "training SSE $127.84$ kt²",
 "training MSE $127.84$ kt²",
 "Table10 row2 SSE->MSE")

# --- 4. §4 duplicate clauses ---
sub_once(
 "the delay, not the structure, separates M4 from persistence — while at $h = 5$ on Specification B the model's own cost dominates (694 of 713 kt).",
 "the delay, not the structure, separates M4 from persistence.",
 "694-duplicate trim")
sub_once(
 "A more accurate $C_t$ cannot produce the crash in a constant-$r$ surplus model, because the observed $\\Delta S$ is far larger than $C_t$.",
 "A more accurate $C_t$ cannot produce the crash in a constant-$r$ surplus model.",
 "crash-clause trim")

# --- 5. §4 paragraph split (blank-line inserts only) ---
sub_once(
 "while beating only the delay-carrying M4 ($195.6$ kt). The predictand is an assessment smoother",
 "while beating only the delay-carrying M4 ($195.6$ kt).\n\nThe predictand is an assessment smoother",
 "para split 1")
sub_once(
 "Recreational catch remains incompletely measured. The log-RMSE scores of Table 4",
 "Recreational catch remains incompletely measured.\n\nThe log-RMSE scores of Table 4",
 "para split 2")

# --- 6a. DFO 2024a/2024b disambiguation ---
sub_once(
 "the Rose and Walters (2019) model and the DFO (2024) assessment model",
 "the Rose and Walters (2019) model and the DFO (2024a) assessment model",
 "2024a in-text")
sub_once(
 "DFO, 2024. NAFO Divisions 2J3KL Northern Cod stock assessment to 2024. DFO Can. Sci. Advis. Sec. Sci. Advis. Rep. 2024/049.",
 "DFO, 2024a. NAFO Divisions 2J3KL Northern Cod stock assessment to 2024. DFO Can. Sci. Advis. Sec. Sci. Advis. Rep. 2024/049.",
 "2024a entry")
sub_once(
 "DFO, 2024. Assessment of capelin in NAFO Divisions 2J3KL. DFO Can. Sci. Advis. Sec. Sci. Advis. Rep. 2024/050.",
 "DFO, 2024b. Assessment of capelin in NAFO Divisions 2J3KL. DFO Can. Sci. Advis. Sec. Sci. Advis. Rep. 2024/050.",
 "2024b entry")

# --- 6b. drop the uncited DFO 2010 entry (with its following blank line) ---
sub_once(
 "DFO, 2010. Proceedings of the Newfoundland and Labrador Regional Atlantic cod Framework Meeting. DFO Can. Sci. Advis. Sec. Proceed. Ser. 2010/053.\n\n",
 "",
 "drop DFO 2010 entry")

# --- 6c. cite the NAFC dataset entry at its two Zenodo sites ---
sub_once(
 "The year-by-year 3L spring acoustic biomass is tabulated in Zenodo 10.5281/zenodo.17515115, with 2023 = 331.3 kt from Murphy et al. (2025).",
 "The year-by-year 3L spring acoustic biomass is tabulated in the Northwest Atlantic Fisheries Centre's Zenodo record (2025), 10.5281/zenodo.17515115, with 2023 = 331.3 kt from Murphy et al. (2025).",
 "NAFC cite body")
sub_once(
 "Capelin acoustic index: Murphy et al. (2025), Zenodo repository 10.5281/zenodo.17515115.",
 "Capelin acoustic index: Murphy et al. (2025), on the Northwest Atlantic Fisheries Centre (2025) Zenodo record 10.5281/zenodo.17515115.",
 "NAFC cite data-avail")

# --- 6d. cite Cadigan 2016 (the NCAM model paper) in Table 1's caption ---
sub_once(
 "**Table 1.** Primary specification — Specification A (the 1983–2015 NCAM M-shift SSB series of DFO, 2016, Table A2).",
 "**Table 1.** Primary specification — Specification A (the 1983–2015 NCAM M-shift SSB series of DFO, 2016, Table A2; the state-space assessment model of Cadigan, 2016).",
 "Cadigan cite")

# --- version log replacement ---
OLD_LOG_PREFIX = "*Version log (v12).*"
assert text.count(OLD_LOG_PREFIX) == 1
i = text.index(OLD_LOG_PREFIX)
j = text.index("\n\n", i)
NEW_LOG = (
"*Version log (v13).* Wave-7 quality scan (owner directive: conceptual clarity and flow, remnants and redundancy, "
"terminology and style). Presentation-layer fixes only; no frozen verdict, score, kernel, or table value changes; "
"the abstract is untouched at 300 words. (1) Section 2.1's parenthetical claiming the DFO (2009) precautionary-approach "
"framework 'governs the critical-zone vocabulary used below' is trimmed to the citation alone — no critical-zone "
"vocabulary occurs below in this manuscript (a shared-text remnant). (2) The Section 1 roadmap is extended to name "
"Sections 3.5 and 3.6, which the post-freeze waves added. (3) The recovery-window training objective printed as "
"'SSE 128.35 versus 127.84 kt²' (Section 3.2) and as 'training SSE' (two Table 10 rows) is relabelled MSE: the printed "
"training-RMSE pair 11.29–12.24 kt squares exactly to 127.4–149.9 kt², so the objective is the per-transition mean — "
"the same label class E2 fixed at v18; the values are untouched. (4) Section 4's decomposition paragraph loses its "
"duplicated clause (the Spec-B '(694 of 713 kt)' reading was stated in consecutive sentences) and its duplicated "
"crash-explanation clause, and is split at two topic boundaries (the predictand paragraph; the log-RMSE paragraph). "
"(5) References: the two same-year DFO 2024 entries are disambiguated 2024a/2024b with the in-text site updated; the "
"never-cited DFO (2010) framework-meeting entry is dropped (no attribution site exists in the text); the Northwest "
"Atlantic Fisheries Centre (2025) dataset entry is cited at its two Zenodo sites; and Cadigan (2016) — the NCAM "
"state-space model paper — is cited in Table 1's caption. Tables 1–9 are byte-identical; Table 10's two label cells "
"change SSE→MSE with values byte-identical."
)
text = text[:i] + NEW_LOG + text[j:]

# --- mechanical checks ---
# body-only comparison (logs stripped from both sides)
body_old = src.replace(src[i:src.index("\n\n", i)], "", 1)
assert body_old.count("*Version log") == 0
body_new = text.replace(text[text.index(NEW_LOG):text.index("\n\n", text.index(NEW_LOG))], "", 1)
assert body_new.count("*Version log") == 0
needles = ["184.4", "195.6", "86.4", "11.1", "127.4", "149.9", "11.29", "12.24",
           "128.35", "127.84", "884.6", "p = 0.005", "694 of 713", "615.72", "1031"]
for n in needles:
    co, cn = body_old.count(n), body_new.count(n)
    if n in ("694 of 713",):
        assert cn == co - 1, f"FAIL needle {n!r}: {co} -> {cn}"
    else:
        assert cn == co, f"FAIL needle {n!r}: {co} -> {cn}"
# SSE must now appear only where true SSE objects (none in E1 body) or zero times
assert "training SSE" not in body_new
assert "(SSE 128.35" not in body_new
assert "(MSE 128.35" in body_new
# abstract untouched
a_old = src[src.index("## Abstract"):src.index("## 1.")]
a_new = text[text.index("## Abstract"):text.index("## 1.")]
assert a_old == a_new, "FAIL: abstract changed"
# table rows byte-identical except the two relabelled Table 10 cells
def table_lines(s):
    return [l for l in s.split("\n") if l.startswith("|") and "Version log" not in l]
tl_old, tl_new = table_lines(src), table_lines(text)
assert len(tl_old) == len(tl_new), f"FAIL table-line count {len(tl_old)} -> {len(tl_new)}"
diff = [(o, n) for o, n in zip(tl_old, tl_new) if o != n]
assert all("SSE" in o and "MSE" in n and o.replace("SSE", "MSE") == n for o, n in diff), \
    f"FAIL unexpected table diffs: {diff[:3]}"
assert len(diff) == 2, f"FAIL: {len(diff)} table diffs"
# no version-log narration in body (the freeze-disclosure 'recorded at this revision' site is intentional)
assert "v12)" not in text

open(DST, "w", encoding="utf-8").write(text)
md5 = hashlib.md5(text.encode()).hexdigest()
print(f"OK  E1 v13 written ({len(text.splitlines())} lines; {len(edits)} edits + log)")
print(f"    MD5 {md5}")
print(f"    table diffs: exactly the 2 relabelled Table-10 cells")
