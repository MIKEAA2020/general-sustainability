# Joint verification (round 2): deepseek and qwen audits of the S5.4/S5.5 verification, checked against code + manuscript

**Scope.** After my round-1 joint verdict, two further audits were returned in one file
(`uploads/joint.txt`). deepseek pushes back on several "resolved" markers and raises new
items; qwen broadly concedes the correction and asks for targeted wording/presentation
improvements. Each claim is below re-checked against the **actual code**
(`model_sims/twoland_fixed.py`, `model_sims/recovery_metric_and_tau_p_scan.py`) and the
**manuscript** (`manuscript_ECOMOD_v33.tex`) and **SI** (`supplementary/SUPPLEMENTARY_information.md`),
not against the audits' wording. Verdict key: **CONFIRMED** (real, actionable),
**ALREADY RESOLVED** (correct in v33; audit stale or scoped), **NOT CONFIRMED** (audit
misstates v33), **PARTLY** (real but minor/scope).

---

## 0. The one thing neither audit fully pins down: v33 split its model in two

Both audits are reading a *hybrid* document — the two-book model in the main text and the
**retained one-stock comparator** in the SI (`§S1–§S4`). This division is deliberate and stated
(SI "Structure and scope", lines 26–30: *"§S1–§S4 and the first block of §S5 describe the
one-stock base model, retained explicitly as a one-stock comparator ... Do not read the one-stock
§S1–§S4 values as the two-land result."*; manuscript line 668 repeats it; manuscript line 452
labels the `+0.62` eigenvalue and `0.608–0.625` range as comparator, "not a two-land, forest, or
Earth property"). Almost every "unresolved" item below is that same one-stock/`A_max` vocabulary
bleeding through — **it belongs to the comparator, not to the two-book model.**

The two-book manuscript is consistently on the quality form: `G_c(q)=ρ_c q(1−q/q_max)` (Eq. 1,
line 154); `q* = q_max/2` interior max (line 212); "Under the corrected quality formulation there
is **no** interior area-based capacity maximum" (line 230); old `2b_c/(b_c+b_G,cρ_c)`
capacity-maximum ratio "superseded" (line 190); "no interior saddle-node (fold)", "no critical
slowing down", `E_ceil≈1.138` (lines 244–246); the composition regime is `Δb_conv=b_f−b_c,eff>0`
(lines 223, 266–268). **deepseek's §1.3 "the manuscript has a serious internal contradiction" is
NOT CONFIRMED for the two-book model** — the analytic results *were* re-derived onto the quality
form. What is real is a **scoping clarity** gap (see §2.8 / item below).

---

## 1. deepseek's Audit-1 items (six equations)

| # | deepseek claim | Verdict | Evidence |
|---|---|---|---|
| 1.1 | Debt unit resolved only if `α` is updated; verification doesn't state α's new unit | **ALREADY RESOLVED (two-book)** | Symbol table `D` = **gha** (line 82); `α` = **gha⁻¹** (line 101), baseline `α=0.03 gha⁻¹` (line 130); `b_f=(b_f0+T_b)e^{−αD}` (line 166). `η` yr⁻¹ × `D` gha = gha·yr⁻¹, Eq. (12) consistent. Residual: the **one-stock comparator** uses `D` in gha·yr and `α` in (gha·yr)⁻¹ — internally consistent *for that model*; scope it (see §2.8). |
| 1.2 | σ_f,σ_c resolved only after a consistency pass in the analytics | **ALREADY RESOLVED** | `σ_f=σ_c=1.0` stated (line 137, 193); analytics written generally (∂S/∂A_f = −σ_f b_f etc., lines 258–262) and evaluated at baseline; no residual σ in a matrix evaluated at any value other than the stated default. |
| 1.3 | `A_c,max` removal is "the largest unresolved problem"; analytics based on `G_c(A_c)` no longer valid unless re-derived | **NOT CONFIRMED (two-book)** | Re-derived: `q*` (212), no area max (230), no fold / no CSD (244–246), regime = `Δb_conv` (266–268), `tab:regime` rewritten (223, 229–233). The old `A_max`-based MSY/fold in the SI is the **labelled one-stock comparator**, not the model. |
| 1.4 | `R_A=R_B/ψ_f` needs `ψ_f` defined | **ALREADY RESOLVED** | `ψ_f=Y_f/B` defined (190, 274–276); `R_A=R_B/ψ_f` (274); `ψ_c` flagged "algebraically false" (276). |
| 1.5 | Proxy decomposition table should not look additive | **ALREADY RESOLVED** | It is share-weighted (Divisia `w_X,w_C`, `Σ=+0.207=dlnB`), and the footnote states the raw Δln "are not additive contributions ... they cannot be summed directly" (lines 515–539). This matches qwen's "preferred" option. |
| 1.6 | Restoration-sign equations must be unambiguous | **ALREADY RESOLVED** | Manuscript 457: `R_rc=ρ_rA_rΨ` surplus base, `R_fc=χA_fΦ` variant, both gates explicit; SI S5.4 defines `(B−E)_+` surplus vs `(E−B)_+` deficit. |

## 2. deepseek's §2 "not covered" items

| # | deepseek claim | Verdict | Evidence |
|---|---|---|---|
| 2.1 | `γ=1/b_G,c` unit `ha·gha⁻¹·yr⁻¹` wrong (extra yr⁻¹) | **NOT CONFIRMED** | Manuscript 177 states `γ` applies only to the timber channel `L_c=[H_c−σ_cY_c]_+/b_G,c`, "in **ha·gha⁻¹**" — correct, no stray yr⁻¹, and it is off in the base model. |
| 2.2 | `κ` appears as a parameter but is not independent (`κ=b_f`) | **ALREADY RESOLVED (two-book)** | The two-book model has no `κ`; conversion is `u_c=min(S/b_f, A_c−A_c,min)/τ_conv` (explicit time constant), and `S/κ` was removed (code comment, manuscript 177). Only `κ_w` (wave steepness, line 143) remains, and it is genuinely independent. |
| 2.3 | Missing symbols: `b_f0, H_c, R_fc, R_rc, χ, ρ_r, A_f^max, Δb, κ_w, t_wave, Φ, Ψ, V_eco` | **PARTLY — legitimate** | Present in symbol table/baseline: `b_f0` (138), `H_c` (90), `R_rc` (82), `χ_r` (84), `A_f^max` (106), `Δb,κ_w,t_wave` (143). **Absent from the symbol table though used in main text line 457:** `R_fc`, `χ`, `ρ_r`, `Φ`, `Ψ`. `V_eco` is not in v33 at all (grep empty) — so it is not missing but removed. **Actionable — DONE: added `R_fc, χ, ρ_r, Φ, Ψ` to the symbol table.** |
| 2.4 | `A_c,ext` listed but never used | **NOT CONFIRMED** | No `A_c,ext`/`A_{c,ext}` in the manuscript. Only the SI comparator keeps `A_ext` (extinction floor, one-stock). |

## 3. qwen's items

| # | qwen claim | Verdict | Evidence |
|---|---|---|---|
| 2.1 | "B stays O(1) (0.70–0.91)" too broad — table has B=1.138 (none), 1.136 (deficit) | **CONFIRMED — wording** | Joint-verdict doc line 23 and SI 377 say "B stays O(1) (0.70–0.91)" / "B stays O(1)"; the no-restoration and deficit rows sit at B≈1.13–1.14. Fix to "surplus-restoration runs **B≈0.70–0.91**; no-restoration/deficit stay near the degraded high-B equilibrium, B≈1.13–1.14." |
| 2.2 | "substantially lower population" should be softened | **CONFIRMED — wording** | SI 412: "re-equilibrates at a **substantially** lower population." But `P/P^init=0.90–0.97` (surplus) — a modest reduction. Change to "**modestly** lower supported population." |
| 2.3 | State `A_c^deg` and `A_c^ref` explicitly | **PARTLY** | Prose + table footnote state `A_c^init=0.8225`, `A_c^deg=0.0513`. Add an explicit table-caption line so it is reproducible without inference. |
| 2.4 | Add `E(T)` and `R_B(T)` columns | **CONFIRMED — verified, good** | Measured every row: `R_B(T)=1.0000`, `E=B` exactly. Adding these makes "re-equilibrates to R_B=1" directly visible and confirms it is an end-state equilibrium. |
| 2.5 | Include deficit + conversion-freeze row | **ALREADY RESOLVED** | The SI table already has "deficit, `χ_r=0.10` *conversion frozen*" (R_c=0.05). No action. |
| 2.6 | Explain why conversion-freeze **raises** `D_peak` (0.152→0.546) | **CONFIRMED — real; mechanism measured** | Freeze sets `u=0`, so conversion cannot close the deficit; `frac(E>B)` more than doubles (0.102→0.229) and mean positive `dD/dt` rises (0.00086→0.00134). Supplementary-gated restoration oversupplies `A_c` (lower B) while population re-equilibrates slowly (`τ_p`), so `E>B` persists longer → more debt. |
| 2.7 | Clarify how `A_f` falls under conversion-freeze (0.915→0.765) | **CONFIRMED — real; mechanism measured** | With `u=0`, `A_f` is replenished only by reserve→fast maintenance `μA_r` and drained by retirement `η_f A_f`. Restoration drains `A_r→A_c`, so `A_r` shrinks and `μA_r` cannot sustain the reference `A_f`; `A_f` settles lower (balances exactly at `μA_r=η_fA_f`). |
| 2.8 | Reconcile "no interior `A_c,max`" with any older text | **CONFIRMED (scope)** | The manuscript has **no** `A_c,max`; only the SI's one-stock comparator uses `A_max=1.2`, `b₀=0.5`, `A_ext`, `ρ=0.05`, and the old area-based MSY/saddle-node (`§S3`, `§S4.1`). Add one scoping sentence that these are comparator-only symbols and parameter values. |
| 2.9 | Check `D` and `α` units after debt change | **ALREADY RESOLVED (two-book)** | `D`=gha, `α`=gha⁻¹, `η`=yr⁻¹ ⇒ gha·yr⁻¹. Satisfied for the two-book model, with the comparator caveat in §2.8. |
| 2.10 | Proxy table still share-weighted | **ALREADY RESOLVED** | Yes — Divisia weights (see §1.5). |
| 3 | S5.4 wording (opening/interpretation/main-text pointer) | **ASYMPTOTIC** | The existing SI text already reads essentially as qwen suggests; only the explicit `A_c^deg/A_c^init` table note + the "modestly lower" fix are additive. |
| 4.1 | Define recovery-fraction denominator | **ALREADY RESOLVED** | SI S5.5 states the grid (`A_c0∈{0.40,0.70,1.00,1.18}`, `P_0∈{0.5…3.0}`), `crash = min A_c ≤ A_c^min`, and "24-cell grid stays 20/24=0.833." |
| 4.2 | Define how oscillation was measured | **ALREADY RESOLVED** | "measured as the peak-to-peak `P` amplitude in each quarter of the run." |
| 4.3 | State numerical robustness (dt refinement) | **CONFIRMED — verified, add** | At `τ_p=2000`: Q3 amplitude = 0.565 (dt=0.1), 0.514 (dt=0.05), 0.484 (dt=0.02) — **bounded and shrinking**, no Hopf, not a step-size artefact. Add a one-line robustness note. |
| 5 | Code checklist | **MOSTLY PASS** | `T_b=0` (recovery integrator uses `p.Y_f(...,Tb=0)`; `simulate(...,T_b_on=False)` default); conservation `|max|=0.0e+00` printed; `A_r` floor tracked (`minAr`); target-cap implemented; conversion-freeze sets `u=0` **only** (`η_f` retirement and `R_rc` restoration still run); both `τ_g`,`τ_p` delay histories populated. |

---

## 4. Confirmed, minimal edits (all verified; no domain change, no re-run needed beyond what is done)

The v33/SI content and the model are **correct**. The only genuine defects found are
**presentation/scoping and two small symbol-table omissions**:

1. **SI S5.4 table + caption:** add `E(T)` and `R_B(T)` columns (all `=1.00`, `E=B`); add an
   explicit caption line "`R_c=1` corresponds to exact return to `A_c^init`; `R_B(T)=1` at the
   end state (E=B)". *(qwen 2.3, 2.4)*
2. **SI S5.4 prose:** "substantially lower population" → "modestly lower supported population".
   *(qwen 2.2)*
3. **SI S5.4:** add one mechanism sentence for the conversion-freeze `D_peak` rise (deficit
   fraction more than doubles because conversion is frozen). *(qwen 2.6)*
4. **SI S5.4:** add one mechanism sentence for `A_f` falling under conversion-freeze
   (restoration drains `A_r→A_c`, so `μA_r` cannot sustain the reference `A_f`). *(qwen 2.7)*
5. **SI S5.5:** add a dt-refinement robustness sentence (bounded, shrinking with dt). *(qwen 4.3)*
6. **Joint-verdict doc / SI §0:** scope the "B≈0.70–0.91" range to the surplus rows. *(qwen 2.1)*
7. **Manuscript symbol table:** add `R_fc`, `χ`, `ρ_r`, `Φ`, `Ψ`. *(deepseek 2.3)*
8. **SI scope note (best placed in the S1 header / S4.1):** one sentence that `A_max=1.2`, `b₀`,
   `A_ext`, `ρ=0.05`, and the area-based MSY/saddle-node in `§S1–§S4` are **one-stock-comparator
   only**, and that the two-book model's relevant units are `D`=gha, `α`=gha⁻¹. *(qwen 2.8, deepseek 1.1/2.4)*

**deepseek's §4 "required before final acceptance" items 1,2,3,4,5,8** are already satisfied in
v33; **item 6** (missing symbols) and **item 7** (proxy-table presentation) are the genuine ones,
and both are addressed above (7 = already correct; 6 = symbol-table additions). The SI's mixed
one-stock/two-book vocabulary is the real remaining risk and is handled by item 8.

---

## 5. Bottom line

The wave-on/T_b correction stands as the essential fix, and the corrected S5.4 numbers are
internally consistent and bounded. deepseek's `§1.3` contradiction claim **does not hold** for the
two-book model (it is re-derived); the real issue it is gesturing at is the SI retaining a labelled
one-stock comparator. qwen's items are almost all warranted and **small**: two wording fixes, a
verifiable table/column addition, two mechanism sentences, a dt-robustness note, and the symbol
table/scope cleanups. No model, parameter, or numerical result needs to change.
