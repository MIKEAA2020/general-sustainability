# RISK REGISTER — unresolved / partially-closed master & revision items

Each row: the item, status, what remains to be done, and owner/priority. This is the "what is still
open" list that makes the scan actionable for the next revision.

| # | Item | Status | What remains | Priority |
|---|---|---|---|---|
| R1 | **Corrected-model basin** (12G.2 analogue) | OPEN — flagged | The `0.506→0.042` fraction and scenario endpoints are **original-model** results. The corrected `(1‴)` S0 has a **one-sided boundary** (no unique interior attractor), so the paper must **recompute the corrected basin** as a recover(`A→A_max`)/collapse(`A→A_ext`) boundary with the one-sided/boundary caveat, and report it separately. | High |
| R2 | **Corrected-model characteristic equation / table / figures** | OPEN | Master Part 7 Step 4/7 require recomputing the char. eq., numerical table, and all figures for `(1‴)` — the revision lists the items and discrepancies but does not itself produce the full recomputed table/figure set. | High |
| R3 | **Masking demonstration is parameter-scoped** | PARTIAL | A genuine mask is reproduced but **only** for deficit ≲0.075 (≈15 % of `b₀A₀`). Decide whether to (a) publish only the narrow, deficit-bounded demonstration (current), or (b) also reproduce the master's original-model sets on the original model as a separate legacy illustration. | Medium |
| R4 | **`ρ` realism / fast–slow χ reduction validity** | PARTIAL | `χ` reduction is valid only while `a₁₁ ≤ 0`; at realistic `ρ≈0.02–0.1 yr⁻¹` use the full 2-D transcendental equation. Stated in §4.3/§13; the corrected-model transcendental crossing curves (Hale & Huang 1993; Gu/Niculescu/Chen 2005) are not yet computed. | Medium |
| R5 | **η primary vs robustness dial; `η→0` singular** | COVERED (policy) | `η` is treated as primary; `η→0` flagged. Keep an explicit `η=0` irreversible benchmark in the paper. | Low |
| R6 | **Non-smoothness / one-sided stability at `E=B`** | COVERED (choice) | The revision uses a stated-width softplus ramp; paper must still state the one-sided/boundary stability (or the ramp width) for the sustainable point. | Low |
| R7 | **Priority / literature (Hutchinson)** | PARTIAL | The master says the "Hutchinson early-result" claim is *unsupported*, not *disproven*. Do not claim priority without evidence; GFN caveats bound the 1961–2022 claim (already reflected in §11/§13). | Low |
| R8 | **Version control** | OPEN — infra | No git repo in the workspace (yes/no). Recommendation below. | Low |
| R9 | **External/2nd-model peer review** | OPEN | A second, independent reviewer of the cross-check is recommended (esp. for the S0 one-sided-boundary finding R1 and the original/provenance labelling). | Low |
| R10 | **`θ` dimensionless group** | PARTIAL | `§4.4` carries the full set including `θ`, but `θ` is not explicitly defined in the master text (it is implied by the non-dimensionalization). Confirm its definition before submission. | Low |

## Net state

Every master item is now either **fully implemented** or **explicitly flagged** (provenance,
recompute-needed, or deferred). There are **no silent gaps**: the only genuinely "new work" remaining is
(a) the corrected-model basin recomputation (R1) and (b) the corrected characteristic-equation/table/
figures (R2), both of which are *computation*, not *decision*, and both are already written down as
required actions in the revision.
