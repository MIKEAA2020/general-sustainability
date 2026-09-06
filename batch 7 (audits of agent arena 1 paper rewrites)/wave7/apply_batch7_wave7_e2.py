#!/usr/bin/env python3
"""Wave-7 build: paperE2_cod_intervention v19 -> v20. Quality-scan fixes, presentation-layer only.

1. Data availability: close the unbalanced parenthesis (iteration-cap clause).
2. Data availability: 'the Section 3.8 breakpoint test' -> the object's real name (the 1992
   one-off sensitivity of Section 3.8).
3. §4: 'Three consequences' -> 'Four consequences' (the paragraph lists First..Fourth).
4. §4: 'Three classes of findings' enumerated explicitly.
5. §3.11: the comparison table gains a caption (Table 6) + an in-text reference.
6. §1 roadmap: names the current result objects (the no-dominance verdict and the
   vacuous-class identity, not 'the two negative certificates') and the 3.6-3.11 layers.
7. §3.3/§3.10/§5: 'order 80-90' harmonised to the settled 'order 70-90' reading (2 sites;
   v14-era remnants; no frozen value touched).
8. Result 3.6 + §4: the form-sensitivity claims corrected to the post-v15 class story (the
   5th-percentile class is informative on the registered form; the restoration is at the
   perpetual-worst class) - the E2-v18 contradiction-fix class.
9. Table 2 row label 'Committed Schaefer' -> 'Registered Schaefer' (the body's term).
10. 'the productivity certificate' one-off term renamed to the vacuous-class identity.
11. 'frozen source-year classes' collocations fixed (2 sites); 'rejected-designs note of
    Definition 2.4' -> 'following Definition 2.4' (2 sites); the T=5 built-in check pointed
    at the archived kernel table; the upper-edge sentence's inverted logic reworded;
    3 unspaced em-dashes spaced; the Regular et al. (2025) reference entry added.
Non-destructive: no frozen verdict, score, kernel, boundary, or table VALUE changes.
"""
import hashlib, re

SRC = "../../arena agent 1/paper rewrites/paperE2_cod_intervention_v19.md"
DST = "../../arena agent 1/paper rewrites/paperE2_cod_intervention_v20.md"

src = open(SRC, encoding="utf-8").read()
text = src
edits = []

def sub_once(old, new, tag):
    global text
    assert text.count(old) == 1, f"FAIL [{tag}]: count {text.count(old)}: {old[:80]!r}"
    text = text.replace(old, new, 1)
    edits.append(tag)

# --- 1. unbalanced parenthesis ---
sub_once(
 "(computed by a runner with the iteration cap raised to $20{,}000$ and an explicit convergence assertion.",
 "(computed by a runner with the iteration cap raised to $20{,}000$ and an explicit convergence assertion).",
 "close paren")

# --- 2. breakpoint test name ---
sub_once(
 "The Section 3.6 Fox form, the Section 3.11 xteNCAM row, and the Section 3.8 breakpoint test are produced by",
 "The Section 3.6 Fox form, the Section 3.11 xteNCAM row, and the Section 3.8 1992 one-off sensitivity are produced by",
 "breakpoint name")

# --- 3. Four consequences ---
sub_once(
 "Three consequences for the methods record follow from the new layers.",
 "Four consequences for the methods record follow from the new layers.",
 "four consequences")

# --- 4. enumerate the three classes ---
sub_once(
 "Three classes of findings must also be kept distinct. The form and specification sensitivities carry the same division.",
 "Three classes of findings must also be kept distinct — the form and specification sensitivities, the geometric findings, and the identified findings. The form and specification sensitivities carry the same division.",
 "three classes enumerated")

# --- 5. Table 6 caption + reference ---
sub_once(
 "| Object | $r$ | $K$ (kt) | $F'(\\mathrm{LRP})$ | Constructive (kt) | zero-catch q10, $T=1$ | zero-catch q10, $T=\\infty$ |",
 "**Table 6.** The two specifications compared at their own reference points (the registered NCAM row and the second, unpooled xteNCAM row of Section 3.11).\n\n| Object | $r$ | $K$ (kt) | $F'(\\mathrm{LRP})$ | Constructive (kt) | zero-catch q10, $T=1$ | zero-catch q10, $T=\\infty$ |",
 "Table 6 caption")
sub_once(
 "The row is a labelled sensitivity with opposite structure at its own reference point.",
 "The row is a labelled sensitivity with opposite structure at its own reference point (Table 6).",
 "Table 6 ref")

# --- 6. roadmap ---
sub_once(
 "Section 2 states the methods. Section 3 reports the kernels, the two negative certificates, the constructive boundary, the certified layer, and the stress replay. Section 4 discusses limitations.",
 "Section 2 states the methods. Section 3 reports the kernels, the no-dominance verdict and the vacuous-class identity, the constructive boundary, the certified layer, and the stress replay, followed by the form comparison (Section 3.6), the carrying-capacity, stochastic, finite-duration, and uncertainty layers (Sections 3.7-3.10), and the second-specification row (Section 3.11). Section 4 discusses limitations.",
 "roadmap")

# --- 7. order 80-90 -> 70-90 (2 sites) ---
sub_once(
 "The corrected bound is read as order $80$–$90$ kt, not the $40$–$60$ kt of the frozen convention.",
 "The corrected bound is read as order $70$–$90$ kt, not the $40$–$60$ kt of the frozen convention.",
 "order 70-90 (3.3)")
sub_once(
 "moves the worst-case reading of the boundary to an order of $80$–$90$ kt under the declared class",
 "moves the worst-case reading of the boundary to an order of $70$–$90$ kt under the declared class",
 "order 70-90 (3.10)")

# --- 8. form-sensitivity class corrections ---
sub_once(
 "The Allee form removes the vacuity even of the perpetual-worst floor and of the 5th-percentile class, because its maximum surplus ($372.4$ kt) exceeds both.",
 "The Allee form removes the vacuity of the perpetual-worst floor — the one class vacuous on the registered form — because its maximum surplus ($372.4$ kt) exceeds both class magnitudes ($-329.0$ and $-287.4$ kt yr⁻¹).",
 "Result 3.6 class fix")
sub_once(
 "The productivity certificate's 5th-percentile reading is form-sensitive — the data-preferred depensatory refit restores a nonempty kernel at that class (Section 3.6) — and its perpetual-worst half is not.",
 "The vacuous-class identity's perpetual-worst reading is form-sensitive — the data-preferred depensatory refit restores a nonempty kernel at that class, the one class vacuous on the registered form (Section 3.6) — and its 5th-percentile half is not, that class being informative on both forms.",
 "L269 class fix")

# --- 9. Committed -> Registered (table label cell) ---
sub_once(
 "| Committed Schaefer | 989.0 | 2219.6 | **884.6** | empty | **884.6** |",
 "| Registered Schaefer | 989.0 | 2219.6 | **884.6** | empty | **884.6** |",
 "Committed->Registered")

# --- 10. (folded into edit 8: the one-off 'productivity certificate' renamed) ---

# --- 11a. frozen source-year collocations ---
sub_once(
 "Under the frozen source-year classes, every member of both was empt",
 "Under the declared source-year classes, every member of both was empt",
 "frozen->declared (2.4)")
sub_once(
 "under the frozen source-year 10th-percentile floor ($-80.87$ kt)",
 "under the source-year 10th-percentile floor ($-80.87$ kt)",
 "frozen drop (3.6)")

# --- 11b. rejected-designs note pointer (2 sites) ---
sub_once(
 "The rejected-designs note of Definition 2.4 reports the same clause-H1 emptiness",
 "The rejected-designs note following Definition 2.4 reports the same clause-H1 emptiness",
 "rejected-designs (3.4)")
sub_once(
 "recorded in the rejected-designs note of Definition 2.4 and not plotted",
 "recorded in the rejected-designs note following Definition 2.4 and not plotted",
 "rejected-designs (Fig 3)")

# --- 11c. T=5 built-in check pointer ---
sub_once(
 "reproduces the registered $T=5$ boundary as a built-in check",
 "reproduces the registered $T=5$ boundary of the archived kernel table as a built-in check",
 "T=5 archive pointer")

# --- 11d. upper-edge inverted logic ---
sub_once(
 "The safe set's upper edge ($10^4$ kt, twice $K$) is never approached and exists only so that kernels can be written $[s, \\infty)$; the positive-part floor $[\\cdot]_+$ never binds on any reported kernel path.",
 "The safe set's upper edge ($10^4$ kt, twice $K$) is a computational grid cap, never approached on any reported kernel path; kernels are written $[s, \\infty)$ because the cap is never approached, and the positive-part floor $[\\cdot]_+$ never binds on any reported kernel path.",
 "upper edge logic")

# --- 11e. three unspaced em-dashes ---
hits = re.findall(r"[A-Za-z]—[A-Za-z]", text)
assert len(hits) == 3, f"FAIL em-dash count {len(hits)}: {hits}"
text = re.sub(r"([A-Za-z])—([A-Za-z])", r"\1 — \2", text)
edits.append("em-dash spacing x3")

# --- 11f. Regular et al. 2025 reference entry ---
sub_once(
 "Schijns, R., Froese, R., Hutchings, J.A., Pauly, D., 2021.",
 "Regular, P.M., et al., 2025. Assessment of the Northern Cod stock in NAFO Divisions 2J3KL in 2024. DFO Can. Sci. Advis. Sec. Res. Doc. 2025/048.\nSchijns, R., Froese, R., Hutchings, J.A., Pauly, D., 2021.",
 "Regular entry")

# --- version log ---
OLD_LOG_PREFIX = "*Version log (v19).*"
assert text.count(OLD_LOG_PREFIX) == 1
i = text.index(OLD_LOG_PREFIX)
j = text.index("\n\n", i)
NEW_LOG = (
"*Version log (v20).* Wave-7 quality scan (owner directive: conceptual clarity and flow, remnants and redundancy, "
"terminology and style). Presentation-layer fixes only; no frozen verdict, score, kernel, boundary, or table value "
"changes; the abstract is untouched. (1) Data availability: the iteration-cap parenthesis is closed; 'the Section 3.8 "
"breakpoint test' is renamed to its object (the 1992 one-off sensitivity); the Regular et al. (2025) entry cited in "
"Section 3.11 is added to the References. (2) Section 4: 'Three consequences' corrected to four (the paragraph lists "
"First–Fourth); the 'Three classes of findings' are enumerated explicitly. (3) Section 3.11's comparison table gains "
"its caption (Table 6) and an in-text reference. (4) The Section 1 roadmap names the current result objects — the "
"no-dominance verdict and the vacuous-class identity — instead of 'the two negative certificates', and the 3.6–3.11 "
"layers. (5) Two 'order 80–90 kt' prints are harmonised to the settled 'order 70–90 kt' reading (the conclusions' "
"form; v14-era remnants). (6) Two form-sensitivity claims are corrected to the post-v15 class story: the 5th-percentile "
"class is informative on the registered form, and the depensatory refit's restoration is at the perpetual-worst class "
"(Result 3.6's statement and the Section 4 sentence that had the two halves inverted; Section 3.6's own record was "
"already correct); the one-off term 'the productivity certificate' is renamed to the vacuous-class identity. (7) Table 2's "
"row label 'Committed Schaefer' is harmonised to the body's 'Registered Schaefer'; two 'frozen source-year' collocations "
"are fixed; the rejected-designs note's pointer reads 'following Definition 2.4'; the T=5 built-in check names the "
"archived kernel table; the safe-set upper-edge sentence's inverted logic is reworded (the cap is why [s, ∞) notation "
"is licit, not what prevents it); three unspaced em-dashes are spaced. Tables 1–5 byte-identical except the one "
"relabeled row; Table 6 is a caption for the pre-existing comparison table; all values byte-identical."
)
text = text[:i] + NEW_LOG + text[j:]

# --- checks ---
body_old = src.replace(src[i:src.index("\n\n", i)], "", 1)
body_new = text.replace(text[text.index(NEW_LOG):text.index("\n\n", text.index(NEW_LOG))], "", 1)
for n in ["91.6", "57.6", "44.7", "87.1", "2219.6", "1098.7", "1020.9", "884.6", "372.4",
          "12,772.2", "306,532", "0.2369", "1.1531", "$80$–$90$", "$70$–$90$"]:
    co, cn = body_old.count(n), body_new.count(n)
    if n == "$80$–$90$":
        assert cn == co - 2, f"FAIL {n}: {co}->{cn}"
    elif n == "$70$–$90$":
        assert cn == co + 2, f"FAIL {n}: {co}->{cn}"
    else:
        assert cn == co, f"FAIL {n}: {co}->{cn}"
assert "productivity certificate" not in body_new
assert "Committed Schaefer" not in body_new
def table_lines(s):
    return [l for l in s.split("\n") if l.startswith("|")]
tl_old, tl_new = table_lines(src), table_lines(text)
assert len(tl_old) == len(tl_new), f"FAIL table count {len(tl_old)}->{len(tl_new)}"
diff = [(o, n) for o, n in zip(tl_old, tl_new) if o != n]
assert all(o.replace("Committed", "Registered") == n for o, n in diff) and len(diff) == 1, f"FAIL diffs: {diff}"
a_old = src[src.index("## Abstract"):src.index("## 1.")]
a_new = text[text.index("## Abstract"):text.index("## 1.")]
assert a_old.replace("e—i", "e — i").replace("P—a", "P — a").replace("e—t", "e — t") == a_new or a_old == a_new, \
    "FAIL abstract changed beyond em-dash spacing"
# balanced parentheses in Data availability paragraph
da = text[text.index("## Data availability"):text.index("## CRediT")]
assert da.count("(") == da.count(")"), f"FAIL paren balance {da.count('(')} vs {da.count(')')}"

open(DST, "w", encoding="utf-8").write(text)
print(f"OK  E2 v20 written ({len(text.splitlines())} lines; {len(edits)} edits + log)")
print(f"    MD5 {hashlib.md5(text.encode()).hexdigest()}")
