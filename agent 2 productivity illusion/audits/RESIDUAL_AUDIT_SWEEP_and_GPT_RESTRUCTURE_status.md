# Residual audit sweep + GPT restructuring status

**Date:** 2026-09-07 (turn-19). Against the final two-land (scope-A) `manuscript_ECOMOD_v33.tex`.

---

## Q1 — Anything from any audits still to be implemented?

**Result: one genuine residual found and fixed; everything else is already implemented or deliberately scoped.**

### The one live residual (fixed this turn)
The `supplementary/SUPPLEMENTARY_information.md` was still a **v32 one-stock companion**: it carried the
one-stock model (S1–S4) and one-stock spectral values (`+0.62`/`+0.625` eigenvalue, `5.4 yr` masking window,
`τ_g≈18–20 yr` recovery cliff) **without labelling them as comparator results**. The manuscript is now the
**two-land** model, and its data-availability statement pointed to the SI as the "full model specification."

**Fix applied (all three locations reconciled):**
1. SI preamble rewritten — now the companion to `manuscript_ECOMOD_v33.tex`, with a new **"Structure and scope"**
   block that states S1–S4 and the first block of §S5 are the **one-stock comparator** (retained as a limit)
   and that the two-land spec lives in the manuscript's "Model formulation" + SI §S5.1–§S5.3.
2. SI §S5 opening block given a **Scope note** attributing `+0.62`/`+0.625`/`5.4 yr`/`18–20 yr` to the
   one-stock comparator.
3. Manuscript data-availability bullet rewritten to point to the correct sections and label the one-stock
   values as comparator (not two-land).

This resolves the v32 F21/F22 data-integrity concern in its last remaining location (the SI).

### Audit-by-audit sweep (verified against the final manuscript)
| Audit | Status |
|---|---|
| **v33 four-audit joint eval** (§4 Priority fix, Tiers 0–2) | All implemented in prior turns (verified turn-17/18): conversion operator with explicit `τ_conv`, `G_c` split into quality `q`, sustainable `A_f*>0` via `μA_r`, `R_A=R_B/ψ_f`, share-weighted proxy, corrected annualized rates, in-domain demo, corrected units, fixed basin sentence, no-CSD, no "bistable", corrected predictions register, softened positioning. |
| **v32 joint eval** (Part 10/11 remaining points) | Superseded by scope-A corrected model. Only live item was the SI one-stock labelling → **fixed**. |
| **qwen decomposition** | Implemented (proxy spec, observation-operator framing, unit/calibration/residual caveats, citation set). |
| **grok/gemini upgrade** | Implemented (recover-fraction reconciliation is tied to the corrected model; the SI is now scoped). |
| **turnover-regime audits** | Implemented. |

No new residual found beyond the SI one-stock labelling.

---

## Q2 — GPT's restructuring suggestions vs the final version

**Source:** `audits/JOINT_EVALUATION_of_gpt_consolidation_plan.md` §5 "Reconciliation — the corrected v33 spec"
(items 1–11). GPT's plan was technically *more* correct than the then-current V33 on stability/equilibrium
inheritance; most of it has since been folded into the corrected model.

### Implemented and verified
| GPT item | Status in final manuscript |
|---|---|
| 1. Ontology: `A_r` state/balance, regeneration as a **growth flow** (not area transfer), dynamic `A_f+A_c+A_r=A_tot` | ✅ "Land area conserved 1:1; capacity a separate book"; "Regeneration is a growth flow of capacity, not a land-area transition"; `A_r` = balance. |
| 2. Equilibria isolated/boundary; **no `P=B/e` continuum, no `det J≡0`** | ✅ "one-parameter family in the *land allocation*, not a free `P`; no identically singular Jacobian." |
| 3. Static geometry / `A_c*`/`ψ_c*` | ✅ Superseded by the quality formulation (no interior area-based capacity maximum; `ψ_c*` corrected, turn-17). |
| 4. Per-active-set 4×4 delayed Jacobian; **no inherited eigenvalue** | ✅ "No entry, no determinant sign, and no eigenvalue value inherited." |
| 5. Ratios `R_B`, `R_A=R_B/ψ_f`; stock-decline condition | ✅ `R_A=R_B/ψ_f` (verified); `Δb_conv` as the honest replacement for a universal index. |
| 6. One-stock = **comparator / aggregation artefact** | ✅ (now also labelled in the SI, this turn). |
| 7. Typed floors via complementarity; `K(t)=max{K_min,B/e}`; forward invariance | ✅ "(10) Typed floors and complementarity"; "Conservation and forward invariance" bullet. |
| 10. Program links (paper1 Prop 1 / paper3 / paper4-v18) | ✅ "Division of labour" bullet. |
| 11. Keep verified positives (`R_B=1`, `R_A` signal, conversion loop, NFA reading) | ✅ Retained. |

### Not carried — deliberate scope choices (no correctness gap)
| GPT item | Why not carried |
|---|---|
| 8. Formal recovery metric `R_c(T)` plus `ΔA_c/ΔA_f/ΔA_r/ΔD/ΔP` reporting | The manuscript reports the *qualitative* asymmetry (recovery-needs-restoration, gate-sign) and the composition window; a scalar `R_c(T)` recovery metric is an illustrative addition not required by any verified result. |
| 9. Explicit `τ_p ≳ 250 yr` delay scan | The paper's delay conclusions are at the baseline `τ_g=20`, `τ_p=25`; extending the scan is a sensitivity-programme add-on, not a correctness item. |
| 9'. Full branch-continuation / tipping taxonomy (fold vs Hopf vs border-collision vs rate-induced) | The manuscript reports the *outcomes* as negative results (no fold, no Hopf, no CSD) rather than running a formal branch-continuation classification. Consistent with the "minimal-edit, honest-negative-results" scope. |

**Bottom line:** GPT's restructuring is essentially fully realized in the final version; the only outstanding
GPT items are optional *bifurcation-programme / recovery-metric* additions rather than corrections. If you want,
I can add the `R_c(T)` metric and an explicit `τ_p`-extended delay scan as a supplementary section, but neither
is required for correctness or for any claim currently in the manuscript.
