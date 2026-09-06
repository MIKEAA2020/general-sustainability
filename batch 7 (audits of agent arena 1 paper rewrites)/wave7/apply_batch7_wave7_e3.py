#!/usr/bin/env python3
"""Wave-7 build: paperE3_edwards_forecast_ladder v13 -> v14. Quality-scan fixes, presentation-layer only.

1. Table 7 row label: 'M2m (the declined gate)' -> 'M2m (the declined nested baseline)' (the
   comparator correction's own vocabulary; the caption already carries it).
2. §2.3: 'Tables 4 and 6' -> 'Tables 4 and 7' (stale pre-v12 table renumbering).
3. §5.2: drop the false 'Table 3 footnote' pointer (Table 3 carries no footnote).
4. §5.3: the restored post-2007 RMSE ranking attributes its fourth value (M2 13.31, verified
   against the committed rolling_modern_2007.csv).
5. §1: the duplicated companion citation deduplicated.
6. References: the never-cited, internally mismatched Author-B entry dropped (its descriptor
   names the groundwater intervention while its label names the cod study; the text cites only
   the forecast companion).
7. §2.1: the duplicated 'The predictand is a measured well series.' sentence dropped (the
   table-note instance is kept); the field-types note gains the TWDB/NSE glosses.
8. §4.1: 'its independent replication (Section 5.3.1)' deduplicated pointer.
9. §6: '321 kaf' -> the paper's unit convention (321 x 10^3 acre-ft).
Non-destructive: no frozen verdict, score, or table VALUE changes; abstract untouched.
"""
import hashlib

SRC = "../../arena agent 1/paper rewrites/paperE3_edwards_forecast_ladder_v13.md"
DST = "../../arena agent 1/paper rewrites/paperE3_edwards_forecast_ladder_v14.md"

src = open(SRC, encoding="utf-8").read()
text = src
edits = []

def sub_once(old, new, tag):
    global text
    assert text.count(old) == 1, f"FAIL [{tag}]: count {text.count(old)}: {old[:80]!r}"
    text = text.replace(old, new, 1)
    edits.append(tag)

# --- 1. Table 7 row label ---
sub_once(
 "| M2m (the declined gate) | 12.28 | −0.56 | 17.44 | — |",
 "| M2m (the declined nested baseline) | 12.28 | −0.56 | 17.44 | — |",
 "M2m row label")

# --- 2. stale table number ---
sub_once(
 "(every model in Tables 4 and 6 is scored on the identical origin sets",
 "(every model in Tables 4 and 7 is scored on the identical origin sets",
 "Tables 4 and 7")

# --- 3. false footnote pointer ---
sub_once(
 "has the wrong sign on pumpage (γ = +0.021; Table 3 footnote)",
 "has the wrong sign on pumpage (γ = +0.021)",
 "Table 3 footnote drop")

# --- 4. attribute the fourth RMSE value (M2 = 13.31, CSV-verified) ---
sub_once(
 "with the one-year RMSE ranking unchanged ($13.09$, $12.16$, $13.31$, and $8.03$ ft)",
 "with the one-year RMSE ranking unchanged (persistence $13.09$, M1 $12.16$, M2 $13.31$, and the oracle $8.03$ ft)",
 "RMSE owners")

# --- 5. duplicated citation ---
sub_once(
 "(Author et al., in review; Author et al., in review)",
 "(Author et al., in review)",
 "citation dedupe")

# --- 6. drop the mismatched uncited Author-B entry ---
sub_once(
 "Author, B., et al. In review. Surplus-production intervention selection under a persistent recharge floor. Companion intervention study (Northern cod, NAFO 2J3KL).\n\n",
 "",
 "drop Author-B entry")

# --- 7a. duplicated predictand sentence (§2.1 opening instance dropped) ---
sub_once(
 "The predictand is a measured well series. The specification separates data fields from empirical constructs, models, and normative thresholds,",
 "The specification separates data fields from empirical constructs, models, and normative thresholds,",
 "predictand dedupe")

# --- 7b. TWDB/NSE glosses in the field-types note ---
sub_once(
 "Field types: D = data, E = empirical construct, M = model, N = normative threshold. The predictand is a measured well series.",
 "Field types: D = data, E = empirical construct, M = model, N = normative threshold; TWDB = Texas Water Development Board; NSE = Nash–Sutcliffe efficiency. The predictand is a measured well series.",
 "TWDB/NSE glosses")

# --- 8. deduplicated replication pointer ---
sub_once(
 "the uncertainty layer of Section 5.3.1 together with its independent replication (Section 5.3.1)",
 "the uncertainty layer of Section 5.3.1 together with its independent replication",
 "replication pointer")

# --- 9. unit harmonisation ---
sub_once(
 "as in 1956 (321 kaf from wells)",
 "as in 1956 ($321 \\times 10^3$ acre-ft from wells)",
 "kaf -> acre-ft")

# --- version log: E3 stacks; append v14 after v13 ---
V13 = "*Version log (v13).*"
assert text.count(V13) == 1
i = text.index(V13)
j = text.index("\n\n", i)
NEW_LOG = (
"\n\n*Version log (v14).* Wave-7 quality scan (owner directive: conceptual clarity and flow, remnants and redundancy, "
"terminology and style). Presentation-layer fixes only; no frozen verdict, score, or table value changes; the abstract "
"is untouched. (1) Table 7's M2m row label 'the declined gate' is corrected to 'the declined nested baseline' — the "
"comparator correction's own vocabulary (the caption already reads 'the nested M2m baseline'); a v12 renumbering "
"casualty. (2) Section 2.3's origin-set pointer reads 'Tables 4 and 7' (it still named the pre-v12 Table 6, which is "
"now the DM-uncertainty table). (3) The drawdown-window sentence drops its 'Table 3 footnote' pointer (Table 3 carries "
"no footnote). (4) The restored post-2007 record attributes its one-year RMSE ranking (persistence 13.09, M1 12.16, "
"M2 13.31, oracle 8.03 ft — M2's 13.31 verified against the committed rolling_modern_2007.csv). (5) The Introduction's "
"duplicated companion citation is deduplicated. (6) The never-cited Author-B reference entry is dropped: its descriptor "
"('a persistent recharge floor') names the groundwater intervention study while its label names the cod study, and the "
"text cites only the forecast companion. (7) The duplicated 'The predictand is a measured well series.' sentence is "
"dropped (the table-note instance is kept), and the field-types note gains the TWDB and NSE glosses. (8) The "
"independent-replication pointer no longer names Section 5.3.1 twice in one sentence. (9) '321 kaf' is written in the "
"paper's unit convention ($321 \\times 10^3$ acre-ft). Tables 1–8 byte-identical except the one relabelled Table-7 row "
"label; all values byte-identical."
)
text = text[:j] + NEW_LOG + text[j:]

# --- checks ---
body_old = src.replace(src[i:j], "", 1)
body_new = text.replace(src[i:j], "", 1).replace(NEW_LOG, "", 1)
for n in ["13.09", "12.16", "13.31", "8.03", "17.16", "25.10", "0.31", "0.25", "0.19",
          "12.28", "−0.56", "17.44", "6.50", "−0.858", "0.384"]:
    assert body_old.count(n) == body_new.count(n), f"FAIL {n}: {body_old.count(n)}->{body_new.count(n)}"
assert "kaf" not in body_new
assert "Author, B." not in body_new
def table_lines(s):
    return [l for l in s.split("\n") if l.startswith("|")]
tl_old, tl_new = table_lines(src), table_lines(text)
assert len(tl_old) == len(tl_new) + 1 or len(tl_old) == len(tl_new), f"table count {len(tl_old)}->{len(tl_new)}"
diff = [(o, n) for o, n in zip(tl_old, tl_new) if o != n]
assert all(o.replace("(the declined gate)", "(the declined nested baseline)") == n for o, n in diff), f"FAIL {diff}"
assert len(diff) == 1, f"FAIL {len(diff)} diffs"
a_old = src[src.index("## Abstract"):src.index("## 1.")]
a_new = text[text.index("## Abstract"):text.index("## 1.")]
assert a_old == a_new, "FAIL abstract changed"

open(DST, "w", encoding="utf-8").write(text)
print(f"OK  E3 v14 written ({len(text.splitlines())} lines; {len(edits)} edits + log)")
print(f"    MD5 {hashlib.md5(text.encode()).hexdigest()}")
