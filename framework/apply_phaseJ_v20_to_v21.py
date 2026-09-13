#!/usr/bin/env python3
"""Phase J — journal-fit structural pass. v20 -> v21_restructured + supplement.

Owner decision (NEW-2): restructure after the text passes; distinguishing
filename marking the restructure; continuous version count. V9-A/H/C applied:
(1) worked examples (Sections 4-5) precede the simulation (Section 6);
(2) standard / demonstration / simulation layers separated (Section 2-3 / 4-5 /
6); (3) peripheral detail moved to Supplement S1 (uncertainty variants, open
problem, verification appendix) with the main text carrying summaries.
No verdict, number, or frozen element is changed; content moved to the
supplement is preserved verbatim.
"""
import re, sys

SRC = "framework/paperF1_retention_framework_v20.md"
MAIN = "framework/paperF1_retention_framework_v21_restructured.md"
SUPP = "framework/paperF1_retention_framework_v21_supplement.md"

t = open(SRC).read()

def cut(start_marker, end_marker):
    """Extract the block between two header lines; verify uniqueness."""
    if t.count(start_marker) != 1 or t.count(end_marker) != 1:
        print(f"FAIL cut: {start_marker!r} ({t.count(start_marker)}) / {end_marker!r} ({t.count(end_marker)})")
        sys.exit(1)
    i = t.index(start_marker)
    j = t.index(end_marker, i)
    return t[i:j]

# --- extract v20 blocks -------------------------------------------------
head      = cut("# When a model is not retained", "## 1. Introduction")
s1        = cut("## 1. Introduction", "## 2. The retention rule")
s2        = cut("## 2. The retention rule", "## 3. The information-set audit")
s3        = cut("## 3. The information-set audit", "## 4. Operating characteristics")
s4        = cut("## 4. Operating characteristics", "## 5. Applications")
s5        = cut("## 5. Applications", "## 6. Cross-application comparison")
s5_1      = cut("### 5.1 Marine stock", "### 5.2 Groundwater")
s5_2      = cut("### 5.2 Groundwater", "## 6. Cross-application comparison")
s6        = cut("## 6. Cross-application comparison", "## 7. What the standard extracts")
s7        = cut("## 7. What the standard extracts", "## 8. Conclusions")
s8        = cut("## 8. Conclusions", "## Data availability")
da_refs   = cut("## Data availability", "## Appendix — Verification")
appendix  = t[t.index("## Appendix — Verification"):]

s4_1      = cut("### 4.1 Why, and the pre-registration", "### 4.2 Data-generating processes")
s4_2      = cut("### 4.2 Data-generating processes", "### 4.3 Results")
s4_3      = cut("### 4.3 Results", "### 4.4 Reading")
s4_4      = cut("### 4.4 Reading", "### 4.5 Comparison with alternative decision rules")
s4_5      = cut("### 4.5 Comparison with alternative decision rules", "### 4.6 Open problem")
s4_6      = cut("### 4.6 Open problem", "### 4.7 Prospective registration")
s4_7      = cut("### 4.7 Prospective registration", "## 5. Applications")

# --- moved-to-supplement pieces (extracted from their blocks) -----------
unc_start = "**Uncertainty-robust variants (sensitivity analyses, run after the pre-registered campaign).**"
unc_end   = "The pre-registered rule is unchanged; these variants are reported as sensitivity analyses."
assert s4_5.count(unc_start) == 1 and s4_5.count(unc_end) == 1
i = s4_5.index(unc_start); j = s4_5.index(unc_end) + len(unc_end)
unc_full  = s4_5[i:j]

open_full = s4_6[len("### 4.6 Open problem — pre-check diagnostic\n\n"):].rstrip() + "\n"

appendix_body = appendix[len("## Appendix — Verification\n\n"):].rstrip() + "\n"

# --- assemble main ------------------------------------------------------
# Section 6: old 4.1-4.5 with new numbering; uncertainty summary; IC block kept
s6_new = ("## 6. Operating characteristics\n\n"
          + s4_1.replace("### 4.1 Why, and the pre-registration", "### 6.1 Why, and the pre-registration")
          + s4_2.replace("### 4.2 Data-generating processes — fixed before scoring", "### 6.2 Data-generating processes — fixed before scoring")
          + s4_3.replace("### 4.3 Results (core + Amendment 1)", "### 6.3 Results (core + Amendment 1)")
          + s4_4.replace("### 4.4 Reading — identification versus gates", "### 6.4 Reading — identification versus gates"))
s6_new += s4_5.replace("### 4.5 Comparison with alternative decision rules", "### 6.5 Comparison with alternative decision rules")
# replace the full uncertainty paragraph by the summary (before the IC block)
unc_summary = ("**Uncertainty-robust variants.** Re-scoring the same replicates with an "
               "uncertainty gate (each margin’s 95% block-bootstrap interval entirely below "
               "zero) strengthens specificity but empties the retained set everywhere, and a "
               "model confidence set never eliminates persistence in any replicate — "
               "persistence lies inside the 90% set in every replicate, so the non-retention "
               "verdicts are not artefacts of the fixed band; the reported verdicts are "
               "unchanged in direction. Full variant detail in Supplement S1.\n\n")
assert s6_new.count(unc_full) == 1
s6_new = s6_new.replace(unc_full, unc_summary)
# open-problem pointer at the end of Section 6
s6_new += ("A pre-check diagnostic identifying in advance where the rule has power remains "
           "open; the examined candidates and the D3 counterexample are documented in "
           "Supplement S1.\n\n")

s9_new = ("## 9. Scope and conclusions\n\n"
          + s7[len("## 7. What the standard extracts from the two applications\n\n"):]
          + "\n**Conclusions.**\n\n"
          + s8[len("## 8. Conclusions\n\n"):])

main = (head
        + s1
        + s2
        + s3
        + s5_2.replace("### 5.2 Groundwater: Edwards Aquifer index well J-17",
                       "## 4. Worked example — Edwards Aquifer index well J-17\n\nFull detail in companions. Reported here: scored verdicts, margins, route. Every number verified against source CSVs. No pooling, no verdict transfer.")
        + s5_1.replace("### 5.1 Marine stock: Northern cod, NAFO 2J3KL",
                       "## 5. Worked example — Northern cod, NAFO 2J3KL")
        + s6_new
        + s6.replace("## 6. Cross-application comparison — two domains, same rule, different failure modes",
                     "## 7. Two domains, one rule — cross-application comparison")
        + s4_7.replace("### 4.7 Prospective registration", "## 8. Prospective registration")
        + s9_new
        + da_refs)

# --- cross-reference map (applied to main) ------------------------------
refmap = [
    ("Section 4.7", "Section 8", 3),
    ("Section 4.6", "Supplement S1", 1),
    ("Section 4.5", "Section 6.5", 5),
    ("Section 4.3", "Section 6.3", 3),
    ("Section 4.2", "Section 6.2", 5),
    ("Section 5.2", "Section 4", 3),
    ("(Section 6)", "(Section 7)", 1),
    ("Section 7 states what the standard extracts from the pair, and what it does not license.",
     "Section 9 states what the standard extracts from the pair, and what it does not license.", 1),
    ("**Operating-characteristic study** (Section 4) — applies rule to synthetic data from known processes, measuring how often retains module genuinely present and how often not. Design, including thresholds separating adequate from inadequate instrument (power ≥80%, specificity ≥90%), registered before any synthetic series generated. Sections 5 and 6 apply the rule to three scored objects and compare.",
     "**Operating-characteristic study** (Section 6) — applies the rule to synthetic data from known processes, measuring how often it retains a module genuinely present and how often not. The design, including the thresholds separating an adequate from an inadequate instrument (power ≥80%, specificity ≥90%), was registered before any synthetic series was generated. Sections 4 and 5 apply the rule to the three scored objects and Section 7 compares the two domains.", 1),
]
for old, new, want in refmap:
    n = main.count(old)
    if n != want:
        print(f"FAIL refmap {old!r}: found {n}, want {want}")
        sys.exit(1)
    main = main.replace(old, new)
    print(f"ref ok: {old!r} x{want}")

open(MAIN, "w").write(main)

# --- supplement ---------------------------------------------------------
supp = ("# Supplement S1 — moved verification and sensitivity detail\n\n"
        "*Companion to paperF1_retention_framework_v21_restructured.md. Content moved "
        "verbatim from the pre-restructure manuscript (v20); numbering below follows v20 — "
        "“Section 4.5” reads as Section 6.5 of the restructured main text, and “Section 4.6” "
        "as its open-problem summary.*\n\n"
        "## S1.1 Uncertainty-robust variants (from Section 6.5 of the main text)\n\n"
        + unc_full + "\n"
        "## S1.2 Open problem — pre-check diagnostic (from Section 6 of the main text)\n\n"
        + open_full + "\n"
        "## S1.3 Verification appendix (from the pre-restructure manuscript)\n\n"
        + appendix_body)
open(SUPP, "w").write(supp)

wc = len(main.split())
print(f"main: {len(main)} chars, {wc} words")
print(f"supplement: {len(supp)} chars, {len(supp.split())} words")
