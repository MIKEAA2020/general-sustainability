#!/usr/bin/env python3
"""Wave-7 build: paperE4_edwards_intervention v11 -> v12. Quality-scan fixes, presentation-layer only.

1. Intro: the mirror-verdict clause un-swapped — the cod companion retains nothing (its own
   no-dominance outcome; stated correctly later at the Discussion), the aquifer retains the
   reactive rules (nominally): 'none retained there, reactive rules retained here'.
2. §2.4: the perpetual floors are declared in Section 2.2 (Uncertainty classes and safe sets),
   not 2.3 (Governance family) — pointer corrected.
3. §3.2: 'the observed maximum annual mean (692.7 ft)' corrected to the record value 691.96 ft
   (the 1992 mean — the record's maximum, verified against the committed annual panel; the
   12.0-yr ceiling arithmetic is unchanged at that value: 11.98 yr).
4. §3.7: the resolvability sentence's parenthetical coordinated with its '2.3-ft gap'
   (615.72 ft to the 618-ft threshold; the marginal flat-90% attractor at 618.88 ft).
5. Tables renumbered into order of appearance (captions and in-text tokens; the EAA's own
   external 'Table 1' references untouched): Table 3->2, Table 2->3, Table 6->4, Table 4->5,
   Table 5->6; Tables 1 and 7 unchanged.
6. The BAU alias declaration extended to running prose (the v11 rename left mixed usage).
7. 'about 31%' harmonised to 'about 31.5%' (4 sites); 'demand-management' harmonised to the
   abstract/conclusions' 'positive-pumping' (2 sites); 'preregistration record' -> the
   family's 'frozen-protocol record'; the Critical-Period EAA entry and Puente (1978) cited.
Non-destructive: no frozen verdict, kernel, score, or table VALUE changes.
"""
import hashlib

SRC = "../../arena agent 1/paper rewrites/paperE4_edwards_intervention_v11.md"
DST = "../../arena agent 1/paper rewrites/paperE4_edwards_intervention_v12.md"

src = open(SRC, encoding="utf-8").read()
text = src
edits = []

def sub_once(old, new, tag):
    global text
    assert text.count(old) == 1, f"FAIL [{tag}]: count {text.count(old)}: {old[:80]!r}"
    text = text.replace(old, new, 1)
    edits.append(tag)

def sub_count(old, new, n, tag):
    global text
    c = text.count(old)
    assert c == n, f"FAIL [{tag}]: count {c} != {n}"
    text = text.replace(old, new)
    edits.append(tag)

# --- 1. mirror-verdict swap ---
sub_once(
 "reaches the mirror verdict — reactive rules retained there, none retained here",
 "reaches the mirror verdict — none retained there, reactive rules retained here (nominally, under the mildest floor class)",
 "mirror verdict swap")

# --- 2. perpetual floors pointer ---
sub_once(
 "the perpetual floors of Section 2.3",
 "the perpetual floors of Section 2.2",
 "floors 2.3->2.2")

# --- 3. record max value (verified: 1992 = 691.96 = max; 12.0 yr unchanged) ---
sub_once(
 "the observed maximum annual mean (692.7 ft) gives 12.0 years",
 "the observed maximum annual mean (691.96 ft, the 1992 mean) gives 12.0 years",
 "692.7 -> 691.96")

# --- 4. gap coordination ---
sub_once(
 "rests on a 2.3-ft gap (615.72 to 618.88)",
 "rests on a 2.3-ft gap (615.72 ft to the 618-ft threshold; the marginal flat-90% attractor sits at 618.88 ft)",
 "gap coordination")

# --- 5. table renumbering (order of appearance; unique anchors; EAA external Table 1 untouched) ---
sub_once("**Table 3.** Nominal kernel lower boundary", "**Table 2.** Nominal kernel lower boundary", "T3->T2 cap")
sub_once("**Table 2.** Mean prescribed pumping", "**Table 3.** Mean prescribed pumping", "T2->T3 cap")
sub_once("**Table 6.** The retention margins", "**Table 4.** The retention margins", "T6->T4 cap")
sub_once("**Table 4.** Finite-duration floors", "**Table 5.** Finite-duration floors", "T4->T5 cap")
sub_once("**Table 5.** Floor-class supply", "**Table 6.** Floor-class supply", "T5->T6 cap")
sub_once("reported in Section 3.4 (Table 6)", "reported in Section 3.4 (Table 4)", "T6->T4 in-text (2.4)")
sub_once("the hybrid margins of Table 6: S1's", "the hybrid margins of Table 4: S1's", "T6->T4 in-text (3.5)")

# --- 6. BAU alias declaration extended to prose ---
sub_once(
 "Training-mean pumping (called BAU in the frozen protocol; the label is retained in tables)",
 "Training-mean pumping (called BAU in the frozen protocol; the label is retained in tables and, under this declaration, in running prose as the family's baseline label)",
 "BAU alias fence")

# --- 7a. about 31% -> 31.5% ---
sub_count("about 31%", "about 31.5%", 4, "31->31.5 x4")

# --- 7b. demand-management -> positive-pumping ---
sub_count("demand-management policy", "positive-pumping policy", 2, "demand-mgmt->positive-pumping x2")

# --- 7c. preregistration record -> frozen-protocol record ---
sub_once(
 "It is archived with the analysis code as the preregistration record, alongside the companion forecast-evaluation protocols dated 2026-08-25.",
 "It is archived with the analysis code as the frozen-protocol record, alongside the companion forecast-evaluation protocols dated 2026-08-25.",
 "preregistration->frozen-protocol")

# --- 7d. Critical-Period EAA entry cited ---
sub_once(
 "a 20%-at-660 sketch of the Authority's published Stage I (the actual rule keys on 10-day J-17 or Comal flow)",
 "a 20%-at-660 sketch of the Authority's published Stage I (Edwards Aquifer Authority, Critical Period / Drought Management; the actual rule keys on 10-day J-17 or Comal flow)",
 "EAA CP entry cited")

# --- 7e. Puente 1978 ---
sub_once(
 "(USGS-estimated, Puente method; Umphres and Choi 2025)",
 "(USGS-estimated, Puente 1978 method; Umphres and Choi 2025)",
 "Puente year")

# --- version log ---
OLD_LOG_PREFIX = "*Version log (v11).*"
assert text.count(OLD_LOG_PREFIX) == 1
i = text.index(OLD_LOG_PREFIX)
j = text.index("\n\n", i)
NEW_LOG = (
"*Version log (v12).* Wave-7 quality scan (owner directive: conceptual clarity and flow, remnants and redundancy, "
"terminology and style). Presentation-layer fixes only; no frozen verdict, kernel, score, or table value changes. "
"(1) The Introduction's mirror-verdict clause was swapped relative to both papers' records and is corrected: the cod "
"companion retains nothing (its no-dominance outcome, stated correctly later in the Discussion), while this aquifer "
"retains the reactive rules (nominally, under the mildest floor class). (2) Section 2.4's disturbance-class pointer is "
"corrected to Section 2.2, where the perpetual floors are declared. (3) The ceiling arithmetic sentence's 'observed "
"maximum annual mean (692.7 ft)' is corrected to the record value 691.96 ft — the 1992 mean, the record's maximum, "
"verified against the committed annual panel; the horizon value is unchanged at that ceiling (11.98 ≈ 12.0 years). "
"(4) The bootstrap section's resolvability sentence coordinates its numbers: the 2.3-ft gap is training-mean pumping's "
"attractor (615.72 ft) against the 618-ft threshold, with the marginal flat-90% attractor at 618.88 ft. (5) The tables "
"are renumbered into order of appearance — captions and in-text tokens; Table 3→2, Table 2→3, Table 6→4, Table 4→5, "
"Table 5→6, Tables 1 and 7 unchanged; the Edwards Aquifer Authority's own external 'Table 1' references are untouched; "
"every table body is byte-identical. (6) The BAU alias declaration is extended to running prose (the v11 rename left "
"mixed usage now covered by the declared alias). (7) 'about 31%' harmonised to 'about 31.5%' (four sites); "
"'demand-management policy' harmonised to the abstract and conclusions' 'positive-pumping policy' (two sites); 'the "
"preregistration record' renamed to the family's 'frozen-protocol record'; the Critical Period / Drought Management "
"entry and Puente (1978) are cited in text. The abstract's three-verdict lead, all kernels, boundaries, supplies, and "
"bootstrap records are untouched."
)
text = text[:i] + NEW_LOG + text[j:]

# --- checks ---
body_old = src.replace(src[i:src.index("\n\n", i)], "", 1)
body_new = text.replace(text[text.index(NEW_LOG):text.index("\n\n", text.index(NEW_LOG))], "", 1)
for n in ["615.72", "618.88", "0.88", "5.6", "8.1", "3.16", "3.2", "2.3", "625.6", "658.4",
          "282.16", "321", "382.16", "6.50", "692.7", "691.96"]:
    co, cn = body_old.count(n), body_new.count(n)
    if n == "692.7":
        assert cn == co - 1, f"FAIL {n}: {co}->{cn}"
    elif n == "691.96":
        assert cn == co + 1, f"FAIL {n}: {co}->{cn}"
    elif n == "2.3":
        assert cn == co - 1, f"FAIL {n}: {co}->{cn}"
    else:
        assert cn == co, f"FAIL {n}: {co}->{cn}"
# table token counts after renumber
import re
toks_new = re.findall(r"Table \d", body_new)
assert toks_new.count("Table 1") == 6, toks_new.count("Table 1")
assert toks_new.count("Table 2") == 1 and toks_new.count("Table 3") == 1
assert toks_new.count("Table 4") == 3 and toks_new.count("Table 5") == 1
assert toks_new.count("Table 6") == 1 and toks_new.count("Table 7") == 1
# table bodies byte-identical (strip caption lines)
def table_bodies(s):
    return [l for l in s.split("\n") if l.startswith("|")]
assert table_bodies(src) == table_bodies(text), "FAIL table body changed"
a_old = src[src.index("## Abstract"):src.index("## 1.")]
a_new = text[text.index("## Abstract"):text.index("## 1.")]
assert a_old.replace("demand-management policy", "positive-pumping policy").replace("about 31%", "about 31.5%") == a_new, "FAIL abstract changed beyond the harmonised term"

open(DST, "w", encoding="utf-8").write(text)
print(f"OK  E4 v12 written ({len(text.splitlines())} lines; {len(edits)} edits + log)")
print(f"    MD5 {hashlib.md5(text.encode()).hexdigest()}")
