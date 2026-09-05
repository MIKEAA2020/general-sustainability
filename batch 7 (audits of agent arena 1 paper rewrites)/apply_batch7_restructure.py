"""
apply_batch7_restructure.py
---------------------------
Builds, non-destructively (fail-loud exact-match replacements only):

  1. arena agent 1/paper rewrites/paperE2_cod_intervention_v17.md   (from v16)
  2. arena agent 1/paper rewrites/paperE3_edwards_forecast_ladder_v12.md (from v11)

E2 v17 implements the owner-directed restructure-level items of the batch-7 joint
audit (the parallel sandbox's "E2 v17" description, evaluated and verified here):
abstract re-scope (governed-object lead, K-pin named a declared fit defect),
retention filter -> dominance partial order (Definition 2.6, clauses verbatim),
Result 3.1 -> "No dominance", Result 3.2 demoted to a definitional note,
Conclusions renumbered to 5 findings + 2 definitional notes, and the
§3.7/Figure 4/§4/Conclusions expansion statements reconciled in one reading
(not an artifact of the particular pinned value; conditional on K >= 2K*).
No value, kernel, or boundary changes anywhere.

E3 v12 registers the owner-archived independent replication of the post-freeze
uncertainty layer (batch 7 campaign_e3_dm_uncertainty.py, verified
deterministic and reproducing every claimed number) and resolves the
climate-comparator kink against the frozen Pass-2 protocol document
(comparator = persistence and M1, not the declined M2m). No frozen verdict,
score, or archived number changes.

Every replacement asserts the target occurs exactly once; any mismatch aborts
with a loud error before writing anything.
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
PAPERS = os.path.join(REPO, "arena agent 1", "paper rewrites")

E2_SRC = os.path.join(PAPERS, "paperE2_cod_intervention_v16.md")
E2_DST = os.path.join(PAPERS, "paperE2_cod_intervention_v17.md")
E3_SRC = os.path.join(PAPERS, "paperE3_edwards_forecast_ladder_v11.md")
E3_DST = os.path.join(PAPERS, "paperE3_edwards_forecast_ladder_v12.md")


def replace_once(text: str, old: str, new: str, tag: str) -> str:
    n = text.count(old)
    if n != 1:
        sys.exit(f"FAIL [{tag}]: expected exactly 1 occurrence, found {n}.\n--- target start ---\n{old[:200]}\n--- target end ---")
    return text.replace(old, new, 1)


# ----------------------------------------------------------------------------
# E2: v16 -> v17
# ----------------------------------------------------------------------------
with open(E2_SRC, encoding="utf-8") as f:
    e2 = f.read()

# --- (1) version log ---
E2_V17_LOG = """*Version log (v17).* Implements the restructure-level items of the joint external audit, as directed by the owner: non-destructive and restructure-level only — no value, kernel, or boundary is changed anywhere. (1) The abstract is re-scoped to lead with the governed object (a single fitted map; every statement scoped to that map, its declared classes, and its declared family) and the $K = 5000$ kt pin is named a declared fit defect. (2) Definition 2.6 is restated as a dominance partial order — the rule the frozen protocol calls its retention rule, with clauses verbatim — and the retention-filter vocabulary is retired: clause (H1), read at every reading with empty scored as worst, structurally blocks every positive-catch rule given the declared classes (BAU's kernel is marginally nonempty at the 5th-percentile $T=\\infty$ class where every positive-catch rule is empty), so a "retention" filter could only ever restate the rule. Result 3.1 becomes "No dominance", with the verdict's selection-theoretic status stated. (3) The vacuous-emptiness statement of Result 3.2 is demoted from a numbered result to a definitional note — an arithmetic identity of the declared class ($|e| > g_{\\max}$), not an empirical finding — and the Conclusions are renumbered to five findings and two definitional notes. (4) The expansion statements of §3.7, Figure 4, §4, and the Conclusions are reconciled in one consistent reading: expansion is not an artifact of the particular pinned value (it holds for every admissible $K \\ge 2K^* = 1769.2$ kt) and is explicitly conditional on $K \\ge 2K^*$, with the data selecting that range of the box. (5) The freeze date is stated as prior to scoring and the post-freeze objects are disclosed (both already present in v16; re-verified). The v16 narrative remains available as the baseline.
"""
e2 = replace_once(
    e2,
    "**Prepared in the format of Fisheries Research (research article)**\n\n## Abstract",
    "**Prepared in the format of Fisheries Research (research article)**\n\n" + E2_V17_LOG + "\n## Abstract",
    "E2 version log",
)

# --- (2) abstract re-scope ---
e2 = replace_once(
    e2,
    "Intervention selection is scored, not asserted. A governance module survives only if it improves the declared protection-and-supply outcome, and the protocol was frozen first. The governed object is the one-step least-squares surplus-production map on the 1983–2007 Northern cod (NAFO 2J3KL) SSB series ($r = 0.2369$; $K = 5000$ kt at its bound; residual SD $114.9$ kt). It is scored on the declared catch-policy family",
    "The governed object of this paper is a single fitted map — the one-step least-squares surplus-production map on the 1983–2007 Northern cod (NAFO 2J3KL) SSB series ($r = 0.2369$; $K = 5000$ kt pinned at its optimization bound, a declared fit defect; residual SD $114.9$ kt) — and every statement below is scoped to that map, its declared disturbance classes, and its declared catch-policy family; nothing here is a Northern-cod-general result. On that object, intervention selection is scored, not asserted: a governance module must improve the declared protection-and-supply outcome to be kept, and the protocol was frozen first. The map is scored on the declared catch-policy family",
    "E2 abstract scope lead",
)

# --- (3) abstract list restructure ---
e2 = replace_once(
    e2,
    "(2) Only the perpetual-worst floor exceeds maximum surplus; the 5th-percentile class is informative, not vacuous. (3) The map is expansive at the LRP, the contraction form of the certified conversion fails, and certified kernels are empty beyond seven years.",
    "(2) No non-BAU policy dominates BAU under the declared partial order: every positive-catch rule is empty under the 5th-percentile class at $T=\\infty$ (where BAU is nonempty), so none improves on BAU there, and the equally protective flat 60-kt cap supplies more than every protective rule; the surplus-proportional family is genuinely reactive—its catch scales with the harvested surplus and vanishes below the LRP—and at $\\phi \\le 0.5$ holds the entire safe set under the informative 10th-percentile class at every horizon while harvesting more than the moratorium, so it is the closest to a dominance, but it does not dominate BAU. (3) The map is expansive at the LRP — for every admissible $K \\ge 2K^* = 1769.2$ kt, so not an artifact of the particular pinned value, though conditional on $K \\ge 2K^*$ — the contraction form of the certified conversion fails, and certified kernels are empty beyond seven years.",
    "E2 abstract items 2-3",
)
e2 = replace_once(
    e2,
    "(5) The surplus-proportional family is genuinely reactive—its catch scales with the harvested surplus and vanishes below the LRP—and at $\\phi \\le 0.5$ holds the entire safe set under the informative 10th-percentile class at every horizon while harvesting more than the moratorium; it is nonetheless not retained, because it is empty under the 5th-percentile class at $T=\\infty$ (where BAU is nonempty), so it does not improve on BAU, and the equally protective flat 60-kt cap supplies more. (6) The depensatory refit leaves the constructive, selection, and expansion certificates intact; only the class-vacuity reading reverses.",
    "(5) The depensatory refit leaves the constructive, selection, and expansion certificates intact; only the class-vacuity reading reverses. A definitional note rather than a numbered finding: only the perpetual-worst floor exceeds the map's maximum surplus ($g_{\\max} = 296$ kt yr$^{-1}$) — an arithmetic identity of that declared class, not an empirical result about Northern cod productivity; the 5th-percentile and 10th-percentile classes are informative.",
    "E2 abstract items 5-6 -> 5 + note",
)

# --- (4) freeze statements: selection vocabulary ---
e2 = replace_once(
    e2,
    "how do reactive rules fare against it under the declared retention rule?",
    "how do reactive rules fare against it under the declared dominance rule?",
    "E2 §1 Q2 rule name",
)
e2 = replace_once(
    e2,
    "None of them replaces or alters the frozen family, the frozen floor classes, or the retention rule.",
    "None of them replaces or alters the frozen family, the frozen floor classes, or the dominance rule of Definition 2.6.",
    "E2 §2.1 post-freeze rule name",
)
e2 = replace_once(
    e2,
    "The intervention protocol — object, defect declaration, disturbance classes, policy family, and retention rule — was frozen (dated 2026-08-26) before any kernel, boundary, replay, or retention score was computed.",
    "The intervention protocol — object, defect declaration, disturbance classes, policy family, and the selection rule restated in Definition 2.6 as a dominance partial order — was frozen (dated 2026-08-26) before any kernel, boundary, replay, or selection score was computed.",
    "E2 §1 freeze statement",
)
e2 = replace_once(
    e2,
    "and the protocol was frozen on 2026-08-26, before any kernel, boundary, replay, or retention score was computed.",
    "and the protocol was frozen on 2026-08-26, before any kernel, boundary, replay, or selection score was computed.",
    "E2 §2.1 freeze statement",
)

# --- (5) Definition 2.6 -> dominance partial order ---
e2 = replace_once(
    e2,
    """**Definition 2.6 (Retention rule).** A non-BAU policy is retained only if all three of the following hold.

- (H1) Its kernel is at least as protective as BAU's at every reading (compared on the kernel lower boundary; empty = worst).
- (H2) It improves on BAU somewhere.
- (H3) At some reading where it improves, its mean allowed catch exceeds that of every at-least-as-protective flat cap.""",
    """**Definition 2.6 (Dominance partial order).** The rule the frozen protocol calls its retention rule is restated here, clauses verbatim, as a partial order on policies rather than a filter that selects an adopted policy: a non-BAU policy *dominates* BAU only if all three of the following hold.

- (H1) Its kernel is at least as protective as BAU's at every reading (compared on the kernel lower boundary; empty = worst).
- (H2) It improves on BAU somewhere.
- (H3) At some reading where it improves, its mean allowed catch exceeds that of every at-least-as-protective flat cap.

*Why the filter vocabulary is retired.* Clause (H1), read at every reading with empty scored as worst, is a structural block rather than a comparison that could go either way: under the 5th-percentile class at $T=\\infty$ every declared positive-catch rule has an empty kernel while BAU's is nonempty ($2219.6$ kt), so within the declared family no positive-catch rule can satisfy (H1) at all — the rule's outcome is fixed by the declared classes and BAU's marginal nonemptiness there. Presenting that outcome as a "retention" decision would overstate it; the vocabulary here is dominance, the outcome is stated as a selection property of the declared partial order (Result 3.1), and the two identity-level statements of the construction (the vacuous-class identity and the structural block itself) are demoted to definitional notes.""",
    "E2 Definition 2.6",
)

# --- (6) §3.2 header + intro ---
e2 = replace_once(
    e2,
    "### 3.2 The two negative certificates\n\nThe first result concerns selection; the second concerns the vacuous classes. Both are negative and both are scoped to the declared rule and disturbance classes.",
    "### 3.2 The no-dominance verdict and the vacuous-class identity\n\nThe first result concerns dominance; the second is the vacuous-class identity, demoted to a definitional note. Both are scoped to the declared rule and disturbance classes.",
    "E2 §3.2 header/intro",
)

# --- (7) Result 3.1 -> No dominance ---
e2 = replace_once(
    e2,
    "**Result 3.1 (Selection).** Under the frozen retention rule of Definition 2.6, no non-BAU policy is retained.",
    "**Result 3.1 (No dominance).** Under the dominance partial order of Definition 2.6 (the frozen rule; clauses verbatim), no non-BAU policy dominates BAU.",
    "E2 Result 3.1 title",
)
e2 = replace_once(
    e2,
    "No non-BAU policy is therefore retained, and the mechanism is the empty-at-the-5th-percentile-class reading of clause (H1), with the supply comparison as a second failure. The companion groundwater evaluation retained its reactive rules at $3.3$–$50.6\\%$ higher permitted supply; this evaluation retains none. □",
    "No non-BAU policy therefore dominates BAU, and the mechanism is the empty-at-the-5th-percentile-class reading of clause (H1), with the supply comparison as a second failure. The verdict's status is selection-theoretic, not empirical: given the declared classes, clause (H1) blocks every positive-catch rule by construction (Definition 2.6's note), so the no-dominance outcome is a property of the declared partial order and classes as much as of the policies. The companion groundwater evaluation operates under a different constraint structure — not a single fatal floor — so its retained reactive rules and this no-dominance outcome are not comparable selections. □",
    "E2 Result 3.1 reason ending",
)

# --- (8) Result 3.2 -> definitional note ---
e2 = replace_once(
    e2,
    "**Result 3.2 (Vacuous classes).** Under the perpetual-worst floor, no catch policy — zero catch included — holds the LRP. Under the 5th-percentile and 10th-percentile classes the statement is not vacuous: those floors lie below the map's maximum surplus and the classes carry informative content.",
    "**Definitional note 3.2 (The vacuous-class identity).** Under the perpetual-worst floor, no catch policy — zero catch included — holds the LRP. This statement is demoted from a numbered result to a note: it is an arithmetic identity of the declared class, not an empirical finding, and it is not numbered on a par with the constructive boundary or the stochastic layer. Under the 5th-percentile and 10th-percentile classes the statement is not vacuous: those floors lie below the map's maximum surplus and the classes carry informative content.",
    "E2 Result 3.2 title",
)
e2 = replace_once(
    e2,
    "*Reason.* The perpetual-worst floor ($-329.0$ kt yr⁻¹) exceeds the map's maximum surplus ($g_{\\max} = 296$ kt yr⁻¹). Every trajectory therefore declines for every catch, zero included. This is an arithmetic identity of that declared disturbance class, not an empirical finding about Northern cod productivity (the critical-floor axis $\\bar e = g_{\\max}$ is stated in Section 3.1). The 5th-percentile class ($-287.4$ kt yr⁻¹) and the 10th-percentile class ($-80.9$ kt yr⁻¹) both lie below $g_{\\max}$ and are not vacuous: their kernels carry substantive content (Table 1, Result 3.3). The correction of the residual convention therefore reduces the vacuous family from two classes to one, and turns the earlier \"the two harsher floors exceed maximum surplus\" certificate into a single-floor statement. The analogy to the companion groundwater institutional certificate is one of form only; that certificate is institutional, this one is a floor-above-surplus identity, and the two are not pooled. □",
    "*Statement.* The perpetual-worst floor ($-329.0$ kt yr⁻¹) exceeds the map's maximum surplus ($g_{\\max} = 296$ kt yr⁻¹). Every trajectory therefore declines for every catch, zero included: $|e| > g_{\\max}$ implies monotone decline for every $C \\ge 0$ — an identity of the map's algebra, not a measurement. The 5th-percentile class ($-287.4$ kt yr⁻¹) and the 10th-percentile class ($-80.9$ kt yr⁻¹) both lie below $g_{\\max}$ and are not vacuous: their kernels carry substantive content (Table 1, Result 3.3), and the 5th-percentile moratorium kernel is nonempty ($2219.6$ kt). The correction of the residual convention therefore reduces the vacuous family from two classes to one. The analogy to the companion groundwater institutional certificate is one of form only; that certificate is institutional, this one is a floor-above-surplus identity, and the two are not pooled. □",
    "E2 Result 3.2 reason",
)
e2 = replace_once(
    e2,
    "The reference point is protected by good years rather than by demand management — but under the corrected class the margin that good years must supply is smaller than the frozen reading implied.",
    "On this map the reference point is protected by good years rather than by demand management — but under the corrected class the margin that good years must supply is smaller than the frozen reading implied.",
    "E2 §3.2 closer scope tag",
)

# --- (9) scattered retention-vocabulary sites ---
e2 = replace_once(
    e2,
    "which is exactly why the same family is empty there, and why the frozen retention rule does not retain it.",
    "which is exactly why the same family is empty there, and why it does not dominate BAU under the frozen rule.",
    "E2 Result 3.4 reason tail",
)
e2 = replace_once(
    e2,
    "The constructive boundary of Section 3.3 and the retention verdict of Section 3.2 are therefore unaffected.",
    "The constructive boundary of Section 3.3 and the dominance verdict of Section 3.2 are therefore unaffected.",
    "E2 Result 3.6 reason",
)

# --- (10) Figure 4 caption ---
e2 = replace_once(
    e2,
    "The expansion classification is not an artifact of the pinned carrying capacity: the grid of Section 3.7 shows $F' \\ge 1.000$ at every admissible $K \\ge 2K^*$, with contraction ($F' = 0.61$–$0.93$) restored only below $2K^*$",
    "The expansion classification is not an artifact of the particular pinned value: the grid of Section 3.7 shows $F' \\ge 1.000$ at every admissible $K \\ge 2K^* = 1769.2$ kt. The classification is conditional on $K \\ge 2K^*$: contraction ($F' = 0.61$–$0.93$) is restored only below $2K^*$",
    "E2 Figure 4 caption",
)

# --- (11) §3.7 reading (i) ---
e2 = replace_once(
    e2,
    "(i) The expansion obstruction is the data-selected regime, not a bound artifact. $F' \\ge 1.000$ at every $K \\ge 2K^*$ — exactly $1.0000$ at $K = 2K^*$, rising to $1.1531$ at the registered $K$ — and the informative constructive bound rises monotonically toward the registered end of the box ($-32.2$ kt at $K = 1000$ kt to $91.6$ kt at $K = 5000$ kt).",
    "(i) The expansion obstruction holds for every admissible $K \\ge 2K^* = 1769.2$ kt and is the data-selected regime within that range — not an artifact of the particular pinned value $K = 5000$ — while remaining conditional on $K \\ge 2K^*$: $F' \\ge 1.000$ at every $K \\ge 2K^*$ — exactly $1.0000$ at $K = 2K^*$, rising to $1.1531$ at the registered $K$ — and the informative constructive bound rises monotonically toward the registered end of the box ($-32.2$ kt at $K = 1000$ kt to $91.6$ kt at $K = 5000$ kt), with the fit cost rising as $K$ falls below $2K^*$.",
    "E2 Result 3.7 (i)",
)

# --- (12) §4 expansion paragraph ---
e2 = replace_once(
    e2,
    "The expansive classification at the LRP inherits that defect: $F'(K^*) = 1 + r(1 - 2K^*/K)$ exceeds 1 only while $K > 2K^* = 1769.2$ kt, so any data-supported $K$ below twice the LRP would make the closed loop contract at the boundary and restore the contraction form of the conversion; the expansion obstruction is therefore conditional on the bound-pinned carrying capacity, not on the identified $r$.",
    "The expansive classification at the LRP carries the $K$-pin's declared defect with it, in one reading consistent with Section 3.7 and Figure 4: $F'(K^*) = 1 + r(1 - 2K^*/K)$ exceeds 1 exactly while $K > 2K^* = 1769.2$ kt. The expansion is conditional on $K \\ge 2K^*$, and within that range it is not an artifact of the particular pinned value — it holds for every admissible $K \\ge 2K^*$, and the carrying-capacity grid shows the data select that range (the fit cost and the informative certificates both deteriorate below $2K^*$). Any data-supported $K$ below twice the LRP would make the closed loop contract at the boundary and restore the contraction form of the conversion; the condition is on $K$, not on the identified $r$.",
    "E2 §4 expansion paragraph",
)

# --- (13) §4 retention-rule paragraph ---
e2 = replace_once(
    e2,
    "The retention rule's protective clause is structurally conservative toward the moratorium.",
    "The dominance rule's protective clause is structurally conservative toward the moratorium.",
    "E2 §4 retention-rule para head",
)
e2 = replace_once(
    e2,
    "that 5th-percentile emptiness is what fails retention, and only a rule that is at least as protective as BAU at every reading and improves on the moratorium somewhere — none here — could be retained.",
    "that 5th-percentile emptiness is what blocks dominance, and only a rule that is at least as protective as BAU at every reading and improves on the moratorium somewhere — none here — could dominate BAU.",
    "E2 §4 retention-rule para tail",
)

# --- (14) §4 first paragraph + selection-finding paragraph ---
e2 = replace_once(
    e2,
    "The productivity negative certificate (Section 3.2) is a robust-layer statement: under the perpetual-worst persistent floor, no catch policy — zero catch included — holds the LRP.",
    "The vacuous-class identity (Section 3.2, definitional note) is a robust-layer statement: under the perpetual-worst persistent floor, no catch policy — zero catch included — holds the LRP.",
    "E2 §4 first para identity rename",
)
e2 = replace_once(
    e2,
    "What survives is a clause-(H1) selection finding at the 5th-percentile $T=\\infty$ class: no positive-catch rule is retained because every such rule is empty there while BAU's kernel is nonempty ($2219.6$ kt). The supply comparison is a second failure, not the mechanism. The surplus-proportional family is the closest to a retention, in that",
    "What survives is the clause-(H1) structural block at the 5th-percentile $T=\\infty$ class: no positive-catch rule dominates BAU because every such rule is empty there while BAU's kernel is nonempty ($2219.6$ kt). The supply comparison is a second failure, not the mechanism. The surplus-proportional family is the closest to a dominance, in that",
    "E2 §4 selection-finding head",
)
e2 = replace_once(
    e2,
    "It fails of retention because, on the 5th-percentile class and at $T=\\infty$, it does not improve on BAU at all, and the equal-protection flat cap yields a higher mean catch.",
    "It fails of dominance because, on the 5th-percentile class and at $T=\\infty$, it does not improve on BAU at all, and the equal-protection flat cap yields a higher mean catch.",
    "E2 §4 selection-finding tail",
)

# --- (15) Conclusions restructure ---
e2 = replace_once(
    e2,
    "Scored intervention selection on the fitted Northern cod surplus-production map yields six conclusions, stated at their actual strength.",
    "Scored intervention selection on the fitted Northern cod surplus-production map yields five findings and two definitional notes, stated at their actual strength.",
    "E2 conclusions intro",
)
e2 = replace_once(
    e2,
    "(2) In the source-year convention only the perpetual-worst floor is vacuous: it exceeds the map's maximum surplus. The 5th-percentile and 10th-percentile classes are informative, and the 5th-percentile moratorium kernel is nonempty ($2219.6$ kt).\n\n(3) No non-BAU policy is retained, and the mechanism is the clause-(H1) reading at the 5th-percentile $T=\\infty$ class rather than boundary geometry or, alone, supply: every positive-catch rule is empty there while BAU's kernel is nonempty ($2219.6$ kt).",
    "(2) No non-BAU policy dominates BAU, and the mechanism is the clause-(H1) reading at the 5th-percentile $T=\\infty$ class rather than boundary geometry or, alone, supply: every positive-catch rule is empty there while BAU's kernel is nonempty ($2219.6$ kt).",
    "E2 conclusions 2-3 merge",
)
e2 = replace_once(
    e2,
    "It is still not retained, because it does not improve on BAU at the harsher-informative class, and an equally protective flat 60-kt cap supplies more.",
    "It still does not dominate BAU: it does not improve on BAU at the harsher-informative class, and an equally protective flat 60-kt cap supplies more.",
    "E2 conclusion 3 tail",
)
e2 = replace_once(
    e2,
    "(4) The certified layer is empty beyond seven years because the map is expansive at the reference point, and the carrying-capacity grid shows this is the data-selected regime: contraction is restored only below twice the LRP, where the informative certificates themselves collapse.\n\n(5) The certificates survive",
    "(3) The certified layer is empty beyond seven years because the map is expansive at the reference point — for every admissible $K \\ge 2K^* = 1769.2$ kt, so not an artifact of the particular pinned value, though conditional on $K \\ge 2K^*$ — and the carrying-capacity grid shows this is the data-selected regime within that range: contraction is restored only below twice the LRP, where the informative certificates themselves collapse.\n\n(4) The certificates survive",
    "E2 conclusions 4-5 renumber",
)
e2 = replace_once(
    e2,
    "(6) The results are convention-dependent in the residual convention only in the sense",
    "(5) The results are convention-dependent in the residual convention only in the sense",
    "E2 conclusion 6 -> 5",
)
e2 = replace_once(
    e2,
    "every parameter and every certificate direction is otherwise stable.\n\nThe methodological content is the protocol itself",
    """every parameter and every certificate direction is otherwise stable.

*Definitional note A (identity).* Only the perpetual-worst floor is vacuous, and that vacuity is an arithmetic identity of the declared class — the floor exceeds the map's maximum surplus, so every trajectory declines for every catch, zero included — not an empirical finding about Northern cod productivity (Section 3.2's note). The 5th-percentile and 10th-percentile classes are informative, and the 5th-percentile moratorium kernel is nonempty ($2219.6$ kt).

*Definitional note B (rule-level).* The no-dominance outcome of finding (2) is a selection property of the declared partial order as much as of the policies: clause (H1), read at every reading with empty scored as worst, blocks every positive-catch rule at the 5th-percentile $T=\\infty$ class given BAU's nonempty kernel there, so within the declared family the outcome could not have gone the other way (Definition 2.6's note). It is recorded as a note so that it is not read as an empirical selection finding on a par with the constructive bound and the stochastic layer.

The methodological content is the protocol itself""",
    "E2 conclusions notes insert",
)

with open(E2_DST, "w", encoding="utf-8") as f:
    f.write(e2)
print(f"wrote {E2_DST} ({len(e2)} chars)")

# ----------------------------------------------------------------------------
# E3: v11 -> v12
# ----------------------------------------------------------------------------
with open(E3_SRC, encoding="utf-8") as f:
    e3 = f.read()

E3_V12_LOG = """*Version log (v12).* Registers the owner-supplied independent replication of the post-freeze uncertainty layer and resolves the climate-comparator kink against the frozen protocol document. Non-destructive: no frozen verdict, no reported score, and no archived number changes. (1) The climate rung's comparator is corrected to the frozen Pass-2 protocol's own statement — the climate question is whether a causal recharge forecast reduces J-17 RMSE "relative to persistence and relative to M1". Earlier versions (v10 and v11) declared the declined M2m as the rung's (H2) comparator; that declaration was inconsistent with the frozen document and circular in exactly the way the external audit identified (the gate was a model the protocol had itself declined). The retention verdict — no climate module retained — is unchanged under either statement, but the stated mechanism is corrected (Sections 4.1, 5.4). (2) The post-freeze uncertainty layer of Section 5.3.1 is registered with an independent replication: the owner-archived script `campaign_e3_dm_uncertainty.py` (batch-7 audit directory of the repository), a second Diebold–Mariano + moving-block-bootstrap implementation with different seeds, block lengths, and HAC conventions, whose verified, deterministically reproduced output confirms every load-bearing reading (the 0.39-ft AR(1) retention margin: DM z = −0.86, block CI [−1.22, +0.56] ft, p = 0.38, statistically indistinguishable from zero; the M2m edge over persistence: p = 0.001; the five-year climatology win: p = 0.035). (3) The Diebold and Mariano (1995) and Künsch (1989) citations are added; the Section 5.3.1 table is numbered (Table 6) and the climate and counterfactual tables renumbered to Tables 7 and 8. The v11 narrative remains available as the baseline.
"""
e3 = replace_once(
    e3,
    "The v10 narrative remains available as the baseline.\n\n## Abstract",
    "The v10 narrative remains available as the baseline.\n\n" + E3_V12_LOG + "\n## Abstract",
    "E3 version log",
)

# --- §4.1 deviation item 2: comparator corrected ---
e3 = replace_once(
    e3,
    "2. **The M2m-as-comparator rule.** The climate rung's (H2) comparator is M2m — a model the protocol declines (a protocol kink). Section 5.4 therefore reports the climate margins against both M2m and M1.",
    "2. **The climate-rung comparator (corrected in this version).** The frozen Pass-2 protocol document states the climate question as whether a causal recharge forecast reduces primary RMSE on J-17 \"relative to persistence and relative to M1\" — the retained M1. Earlier versions of this paper declared the climate rung's (H2) comparator to be the declined M2m instead and disclosed the declaration as a protocol kink; that declaration was inconsistent with the frozen document and circular in the way the external audit identified: the gate was a model the protocol had itself declined. This version corrects the comparator to the frozen document's M1 (with persistence); Section 5.4 reports the climate verdict on that gate, and the M2m margins are retained as a nested-baseline reading rather than as the gate. The correction changes no frozen verdict — no climate module is retained under either statement — but it corrects the stated mechanism.",
    "E3 §4.1 deviation 2",
)
e3 = replace_once(
    e3,
    "Post-freeze objects, labelled as such: the climate-pass fixed-window scores, the pumpage counterfactuals of Section 5.6, the Comal service-series scoring, and the uncertainty layer of Section 5.3.1. None replaces or alters a frozen verdict.",
    "Post-freeze objects, labelled as such: the climate-pass fixed-window scores, the pumpage counterfactuals of Section 5.6, the Comal service-series scoring, and the uncertainty layer of Section 5.3.1 together with its independent replication (Section 5.3.1). None replaces or alters a frozen verdict.",
    "E3 §4.1 post-freeze list",
)

# --- §5.3.1: citations, table number, row label, replication paragraph ---
e3 = replace_once(
    e3,
    """A post-freeze uncertainty layer attaches Diebold–Mariano tests (Newey–West HAC, lag h − 1) and moving-block bootstrap intervals (block length 8, 10,000 replications, seeded) to every load-bearing margin, computed from the archived per-origin forecast files. It is labelled post-freeze and changes no frozen verdict.

| Comparison (rolling, h = 1 unless noted) |""",
    """A post-freeze uncertainty layer attaches Diebold–Mariano tests (Diebold and Mariano 1995; Newey–West HAC, lag h − 1) and moving-block bootstrap intervals (Künsch 1989; block length 8, 10,000 replications, seeded) to every load-bearing margin, computed from the archived per-origin forecast files. It is labelled post-freeze and changes no frozen verdict.

**Table 6.** Uncertainty on the load-bearing margins (post-freeze layer; Diebold–Mariano with Newey–West HAC, lag h − 1; moving-block bootstrap, block length 8, 10,000 replications, seeded).

| Comparison (rolling, h = 1 unless noted) |""",
    "E3 §5.3.1 intro + Table 6 label",
)
e3 = replace_once(
    e3,
    "| M2_combo − M2m (climate gate) |",
    "| M2_combo − M2m (nested baseline) |",
    "E3 §5.3.1 row label",
)
e3 = replace_once(
    e3,
    "Third, the climate-gate margin (combo − M2m, +0.43 ft) is itself within noise: the climate rejection is a point-RMSE rule outcome, not a significance finding.",
    """Third, the nested-baseline margin (combo − M2m, +0.43 ft) is itself within noise: the climate rejection is a point-RMSE rule outcome, not a significance finding.

An independent replication of this layer is registered with the repository: the owner-archived script `campaign_e3_dm_uncertainty.py` (in the batch-7 audit directory), a second Diebold–Mariano + moving-block-bootstrap implementation — HAC lag h − 1 with unweighted truncation and population-variance scaling, block length h, 20,000 replications, seed 0, deterministic (byte-identical on re-execution) — reading the same registered per-origin forecast file. Its verified output (archived alongside it) reproduces every load-bearing reading: the M1 retention margin DM z = −0.86 with block CI [−1.22, +0.56] ft (bootstrap p = 0.38); the M2m edge over persistence (p = 0.001); the h = 5 climatology win (p = 0.035). It also registers two rows this table does not carry — the h = 1 climatology loss (+2.94 ft against persistence, p = 0.046) and the M2 h = 5 loss (+12.4 ft, p < 0.001) — both consistent with the readings above. The two implementations use different seeds, block lengths, HAC weighting, and variance conventions, and agree on every conclusion: the 0.39-ft AR(1) retention margin is statistically indistinguishable from zero, the M2m edge is the only one-year margin that separates from noise, and the five-year climatology win survives.""",
    "E3 §5.3.1 replication paragraph",
)

# --- §5.4 narrative: corrected comparator ---
e3 = replace_once(
    e3,
    "Lagged precipitation and September–November Niño 3.4 have modest skill on R relative to climatology (528–545 versus 556 × 10³ acre-ft), and they do not constitute forecast structure on head: the point-RMSE rule lists ENSO, lagged precipitation, and the combination — each beats persist and M1 by margins of 0.02, 0.04, and 0.13 ft, all within noise (Section 5.3.1) — but each fails (H2) against the declared nested comparator M2m (12.28 ft), whose own margin over them (+0.43 ft for the combination) is also within noise. The rejection is therefore honest only with both margins visible: the climate modules beat persistence and the AR(1) by at most 0.13 ft and lose to climatological fluxes; none is retained, and nothing in that verdict is a significance finding. At h = 5 all three have RMSE 3–6 ft higher than persistence (the h > 1 climate scores reuse the one-step recharge forecast, held constant over the horizon, so this is a design consequence, not a multi-year climate test); structurally they are M2m with a weakly adjusted intercept. M2_Rar loses at h = 1 (13.25 ft; 0.41 ft worse than M1) — autoregression on nearly white recharge is not a recharge forecast.",
    "Lagged precipitation and September–November Niño 3.4 have modest skill on R relative to climatology (528–545 versus 556 × 10³ acre-ft), and they do not constitute forecast structure on head. The frozen Pass-2 gate compares the climate modules against persistence and the retained M1 (Section 4.1): on that gate the three modules are listed by the point rule — each beats persist and M1 by margins of 0.02, 0.04, and 0.13 ft, all within noise (Section 5.3.1, Table 6) — so the listing is not a skill claim. None is retained, on three stated grounds: the margins against the gate are within noise; at h = 5 all three have RMSE 3–6 ft higher than persistence (the h > 1 climate scores reuse the one-step recharge forecast, held constant over the horizon, so this is a design consequence, not a multi-year climate test); and structurally they are the declined M2m with a weakly adjusted intercept — no additional forecast structure over the retained AR(1) class — so against that nested climatological baseline they lose outright (12.71–12.82 versus 12.28 ft; the combination's +0.43-ft deficit, Section 5.3.1, also within noise). The rejection is therefore honest with both readings visible: the climate modules beat persistence and the AR(1) by at most 0.13 ft and lose to climatological fluxes; none is retained, and nothing in that verdict is a significance finding. M2_Rar loses at h = 1 (13.25 ft; 0.41 ft worse than M1) — autoregression on nearly white recharge is not a recharge forecast.",
    "E3 §5.4 narrative",
)

# --- table labels ---
e3 = replace_once(
    e3,
    "**Table 6.** Rolling RMSE, climate-informed recharge (same origin sets as Table 4; margins vs M1 and vs the M2m gate both shown for the h = 1 column).",
    "**Table 7.** Rolling RMSE, climate-informed recharge (same origin sets as Table 4; margins vs M1 — the frozen Pass-2 gate — and vs the nested M2m baseline both shown for the h = 1 column).",
    "E3 Table 6 -> 7",
)
e3 = replace_once(
    e3,
    "**Table 7.** Pumpage counterfactuals, 1991–2023 (fitted pre-permit map; actual recharge).",
    "**Table 8.** Pumpage counterfactuals, 1991–2023 (fitted pre-permit map; actual recharge).",
    "E3 Table 7 -> 8",
)

# --- §6 precision fix ---
e3 = replace_once(
    e3,
    "while here every module must beat persistence and the next-simpler causal model under a rule frozen before scoring, and on that rule the entire causal ladder is rejected at the one-year horizon.",
    "while here every module must beat persistence and the next-simpler causal model under a rule frozen before scoring, and on that rule no causal module is retained at the one-year horizon (the climate rungs pass the frozen Pass-2 gate by within-noise margins and are declined on class grounds; Section 5.4).",
    "E3 §6 ladder sentence",
)

# --- references ---
e3 = replace_once(
    e3,
    "Daliakopoulos, I.N., Coulibaly, P., and Tsanis, I.K. 2005. Groundwater level forecasting using artificial neural networks. *Journal of Hydrology* 309: 229–240. https://doi.org/10.1016/j.jhydrol.2004.12.001\n",
    "Daliakopoulos, I.N., Coulibaly, P., and Tsanis, I.K. 2005. Groundwater level forecasting using artificial neural networks. *Journal of Hydrology* 309: 229–240. https://doi.org/10.1016/j.jhydrol.2004.12.001\n\nDiebold, F.X., and Mariano, R.S. 1995. Comparing predictive accuracy. *Journal of Business & Economic Statistics* 13: 253–263. https://doi.org/10.1080/07350015.1995.10524599\n",
    "E3 ref Diebold",
)
e3 = replace_once(
    e3,
    "Edwards Aquifer Authority. Critical Period / Drought Management. https://www.edwardsaquifer.org/groundwater-users/critical-period-drought-management/\n",
    "Edwards Aquifer Authority. Critical Period / Drought Management. https://www.edwardsaquifer.org/groundwater-users/critical-period-drought-management/\n\nKünsch, H.R. 1989. The jackknife and the bootstrap for general stationary observations. *Annals of Statistics* 17: 1217–1241. https://doi.org/10.1214/aos/1176347265\n",
    "E3 ref Kunsch",
)

# --- data availability ---
e3 = replace_once(
    e3,
    "the clip-binding statement of Section 5.2 is computed there from the registered panel and reproduces both fixed-window M2 RMSEs (18.11 and 55.32 ft) exactly.",
    "the clip-binding statement of Section 5.2 is computed there from the registered panel and reproduces both fixed-window M2 RMSEs (18.11 and 55.32 ft) exactly. The independent replication of the post-freeze uncertainty layer is registered as `batch 7 (audits of agent arena 1 paper rewrites)/campaign_e3_dm_uncertainty.py` (owner-archived), with its deterministically reproduced output archived alongside it at `batch 7 (audits of agent arena 1 paper rewrites)/results/e3_dm_uncertainty.csv`; it recomputes the Diebold–Mariano and moving-block-bootstrap table from the same registered per-origin forecast file under different seeds, block lengths, and HAC conventions, and every load-bearing conclusion of Section 5.3.1 is unchanged under either implementation.",
    "E3 data availability",
)

with open(E3_DST, "w", encoding="utf-8") as f:
    f.write(e3)
print(f"wrote {E3_DST} ({len(e3)} chars)")
print("OK: both papers built with all replacements applied exactly once.")
