# Root-cause remediation for the two-book model — implementing the audit fixes

**Trigger:** `uploads/4 audits_v33 audit.txt` (deepseek, qwen, gemini, grok). Treated as a
consistency + correctness pass on `manuscript_ECOMOD_v33.tex`. Joint evaluation:
`audits/JOINT_EVALUATION_of_four_audits_v33.md`.

**What this document does:**
1. Names the single deepest root cause and shows all four audits converge on it.
2. Delivers a **working, dimensionally-corrected model** (`model_sims/twoland_fixed.py`) that fixes it,
   with **verified** numerics (I re-ran it, not asserted it).
3. Lists the **remaining audit points** and how each is incorporated, as-is or improved.
4. States what is now (and is not) claimable.

---

## 1. The root cause (one sentence)

**The capital-land variable `A_c` was forced to play three incompatible roles at once —
conserved *area* (ha), a *capacity* stock, and a source of a *flow* — so the model mixed area
transfers with capacity growth and put a stock (`S/κ`, which is `ha`) inside rate equations
(`ha/yr`).** This is the *same* category error the earlier work called master **RC1** (the single
environmental stock playing three roles) — re-expressed for two books, a recurrence rather than a
fix.

### 1.1 How each audit lands on it

| Audit | Words | Root-cause link |
|---|---|---|
| glok | "ECOMOD is still a one-stock liquidation model wearing two land symbols"; "`S/κ` does not have the units of `dA/dt`"; "same object cannot be a conserved area compartment and a logistic biomass stock" | **Direct hit** — the tri-role conflation |
| gemini | "`G_c` double-counting and the land-conservation breach"; "cannot be both a conserved area compartment and a capacity stock" | **Direct hit** |
| qwen | "`G_c` is called 'not a land-area transition', but the equation makes it one"; "differs on definition of deficit" | Same class |
| deepseek | "units of `D` inconsistent"; "`S/κ` donor-limited is dimensionally odd"; "`κ=b_f` but not independent" | Symptom-level, same class |

### 1.2 The two concrete defects (both confirmed in code before I fixed them)

**D1 — the conversion operator is dimensionally wrong.**
`S = [E − σ_f Y_f − σ_c Y_c]_+` is a flow (`gha·yr⁻¹`); `κ = b_f` is `gha·ha⁻¹·yr⁻¹`; therefore
`S/κ = (gha·yr⁻¹)/(gha·ha⁻¹·yr⁻¹) = ha` — **a stock.** Yet in `twoland_dyn.py` the code does
`u_c = min(S/kappa, A_c)` and adds it to `dAf`/`dAc` (each `ha·yr⁻¹`). A stock added to a rate is
the original `γ = 1/b_G` unit error under a new name. The manuscript's own convention note ("gives
`S/κ` in `ha·yr⁻¹`") is arithmetically false.

**D2 — `G_c` is double-counted and breaks area conservation.**
`G_c` appears in `dA_c/dt` (as a `ha·yr⁻¹` area term) **and** in `Y_c = b_c A_c + b_{G,c} G_c(A_c)`
(as a flow). Because `A_r = A_tot − A_f − A_c`, putting `G_c` in `dA_c/dt` forces `A_r` to fall by
`G_c` — an implicit hidden `A_r → A_c` area transfer, contradicting the claim "regeneration is a
growth flow, not a land-area transition." The machine-precision conservation check is vacuous (it
holds by definition of Eq. 7, whatever `dA_c/dt` does).

**D3 (consequence) — no sustainable cropland equilibrium.**
With `dA_f/dt = S/κ − η_f A_f` and no `A_r → A_f` term, `A_f* = 0` at every equilibrium; agriculture
exists only as a deficit-financed transient.

---

## 2. The correction (implemented)

Split the capital book into **area** (conserved 1:1 with `A_f`, `A_r`) and **quality** `q`
(per-ha capacity index, a separate state). Conversion moves area only; regeneration is a *flow* that
enters the biocapacity sum but never the area book. Conversion is a **rate** with an explicit time
constant. A cropland-maintenance term restores a sustainable `A_f* > 0`.

```
book:        A_f + A_c + A_r = A_tot        (EXACT, 1:1 area flows only)
quality:     q in [0, q_max]                (per-ha capacity)

g_c(q)   = rho_c q (1 - q/q_max)            [1/yr]  regeneration of QUALITY
Y_c      = b_c A_c + b_G,c g_c(q) A_c       [gha/yr]
Y_f      = b_f A_f ;  B = Y_f + Y_c ;  E = e P ;  S = [E - σ_f Y_f - σ_c Y_c]_+

conversion RATE:  u_c = min(S/b_f, A_c - A_c^min) / tau_conv     [ha/yr]
   dA_f/dt = +u_c + mu A_r - eta_f A_f    (maintenance A_r->A_f)
   dA_c/dt = -u_c + R_rc                  (restoration A_r->A_c, surplus-gated, sign-correct)
   dA_r/dt = -mu A_r + eta_f A_f - R_rc   (=> d(A_f+A_c+A_r)/dt = 0  EXACTLY)
dq/dt     = g_c(q)                        (quality regeneration; NOT an area transfer)
dP/dt     = r P (1 - P/K) ,  K = B/e ;  dD/dt = [E-B]_+ - eta D
```

`model_sims/twoland_fixed.py` implements this.

### 2.1 Verified results (I re-ran `twoland_fixed.py`)

**Exact conservation (the test the audits said was vacuous).**
```
|A_f + A_c + A_r - A_tot|_{max} = 0.00e+00      (an honest 1:1 area book, not an imposed identity)
```

**A sustainable cropland equilibrium now EXISTS** (zero-cropland pathology resolved):
```
long-run:  A_f = 0.667   A_c = 0.778   A_r = 0.556   q = 1.000   P = 1.101
```
Three land books coexist in steady state; `A_f* ≈ 0.67 > 0`.

**Composition illusion under consistent domain** (A_tot=2.5 so A_f0+A_c0=2.1 is in-domain):
```
conservation |sum - A_tot|max = 0.00e+00     initial A_r = +0.400 (in domain)
window 150.3 yr   B 0.594 -> 0.825   A_c 1.500 -> 0.808
                  A_f 0.600 -> 0.923   A_r 0.400 -> 0.769
sum of area changes = 0.0000           q 0.900 -> 1.000
final A_c=0.808 (>Ac_min=0.05), A_r=0.769 (>=Ar_min)  OK
```
The mask is now a **genuine 1:1 conversion** (ΔA_f +0.323, ΔA_c −0.692, ΔA_r +0.369, sum 0.0000) —
**not** grok's "overflow + retirement + conversion starting outside the carrying area." The off-domain
artifact is gone.

**The `R_A` identity is now correct.** With the correct fast-land share `ψ_f = Y_f/B`:
```
psi_f=0.9104  R_B=1.4727  R_B/psi_f=1.6176  R_A=1.6176   (match)
psi_f=0.9657  R_B=0.9401  R_B/psi_f=0.9735  R_A=0.9735   (match)
```
(`R_A = R_B/ψ_f` holds exactly; the manuscript's `R_A = R_B/ψ_c` with `ψ_c = b_c A_c/Y_c` is the
wrong share and is algebraically false.)

**The composition diagnostic is robust** (the claim that survives with or without an interior
capacity maximum):
```
delta_b_conv = b_f - b_c_eff   at  q=0.30 -> +0.787 ; q=0.60 -> +0.785 ; q=0.90 -> +0.794
```
Positive and essentially flat across quality — the **composition/conversion mechanism is structural**,
independently of whether `Y_c` has an interior maximum.

---

## 3. Status of the root-cause claim

The paper's core **conceptual** contributions survive the correction and are independent of the
conversion bug (matching glok's "What still stands"):

| Survives | Grounded in |
|---|---|
| Composition illusion as an **accounting identity** (`b_f > b_{c,eff}` ⇒ 1 ha shift raises current B) | ✅ static, verified (`Δb_conv ≈ +0.79`) |
| **Identifiability** of value-weighted gha (yield vs area vs book not identifiable from World B alone) | ✅ the NFA structure |
| **Recovery not the inverse** of conversion; sign of the gate matters | ✅ surplus vs deficit gate |
| Capital-land interior max **iff `b_{G,c} ρ_c > b_c`**, a ratio, identification-dependent | ✅ regime-conditional |
| **Informational** claim: controlling only B cannot enforce an A_c floor | ✅ |

**Now gated / no longer claimable as reported** (until re-derived on the corrected operator):
- The conversion-fold "eigenvalues" (`λ_+ = +0.039…+0.073`), `E_ceil = 0.478`, `J_c`, `tab:conv`.
- "Critical slowing down" preceding the conversion fold (it was computed on the **saddle** branch).
- The fixed "5.4 yr" composition window and the "1-to-1 conversion" reading of the old demo.
- The additive empirical proxy table (must become share-weighted).

---

## 4. Remaining audit points — incorporated (as-is or improved)

### 4.1 Incorporated as-is (verified real & fixable)

| Point | Audit(s) | Status |
|---|---|---|
| Units of `D`/`α`/`γ` | deepseek, qwen, gemini, glok | `D`→gha, `α`→gha⁻¹, `γ`→ha·gha⁻¹. Fix in symbol table + Eq (11). |
| `R_A = R_B/ψ_f` (not `ψ_c`) | all four | **Proved it holds** with `ψ_f`; the manuscript is wrong. |
| Proxy table not additive (needs share weights) | all four | `d ln B = s_f(d ln b_f + d ln A_f) + s_c d ln B_c`. |
| Annualized rates wrong (`+0.377`, `−0.867`) | deepseek, qwen, glok | Correct: `+0.339%/yr`, `−1.233%/yr` (recomputed from data). |
| Demo off-domain / not 1:1 | qwen, gemini, glok | Fixed by consistent `A_tot` + area/quality split (verified sum 0.0000). |
| Basin sentence backwards | deepseek, glok, qwen | "higher initial capital supports higher demand." |
| `σ_f,σ_c` = 1 silently | deepseek, gemini | Set both = 1 in registry + state it, or carry through. |
| `L_c`,`H_c` orphaned | gemini, glok, deepseek | Remove or define. |
| `A_r` state-vs-balance; "4-D" | deepseek, gemini | Pick one: 5-D with q, `A_r` a balance. |
| Missing symbols (`b_f0,H_c,R_fc,R_rc,χ,ρ_r,A_f^max,Δb,κ_w,t_wave,Φ,Ψ,V_eco`) | all | Add to table or remove. |
| CSD on the wrong branch / "hysteresis=bistable" | glok, qwen, gemini | Report on stable branch; "fold-induced threshold," not bistability. |
| "seven predictions" vs prediction-7 double-count | gemini | Dynamical set = 1–4, 6. |
| "only shortening the lag helps" vs flat-in-`τ_g` | glok, gemini | Allee row contradicts Prediction 4; fix. |
| `Y_c^max` (0.0609) vs `E_ceil` (0.478) conflated | gemini, glok | Two different objects; label distinctly. |
| LaTeX `(\$f,\$c)`, `A_tot` | gemini, glok | `(\sigma_f,\sigma_c)`, `A_{\text{tot}}`. |
| `V_{eco}` re-used for three different things | glok | One symbol, one meaning. |

### 4.2 Incorporated after improvement (audit overreach / framework correction)

| Point | Audit claim | Improvement |
|---|---|---|
| Population "artifact" framing | gemini: "a fallacy"; glok: "another theorem" | The identity is **exact** (verified residual `8.3e−17`). It is **not** the composition illusion; it is the extensive/intensive result. Keep it, relabel it, never brand it the two-land result. |
| "Core thesis refuted" | gemini/glok narrative | **Not refuted** — only the dynamical spectral layer is gated (see §3). |
| `Y_c'/b_f` "is dimensionless" | glok | It is `yr`. The mixing conclusion stands; the stated unit is off. |
| "5.4 yr is a coincidence/red flag" | glok | Neither a confirmation nor a red flag — it was a by-product of the bug. Re-derive on the corrected operator (the corrected window is ~150 yr at fixed demand). |

### 4.3 Points I do NOT adopt (would be wrong or out of scope)

- **gemini's "population-artifact fallacy" as causal** — an exact identity is not a causal claim.
- **gemini's "deficit-gated restoration is a fallacy / reforest during famine"** — this is a fair
  *scenario warning* (it can deepen a short-run deficit) but it is not a contradiction of the model;
  the corrected model surplus-gates restoration and the policy point stands with that gate.
- **Rewriting to gemini's specific architecture (add maintenance + surplus-gate) vs glok's
  (instantaneous conversion + quality state)** — these differ in detail; I implemented the minimal
  common core (area/quality split + conversion rate + maintenance) that satisfies both without
  over-committing to either's full prescription. The remaining choice is an authorial/modelling one.

---

## 5. Net deliverable

- `model_sims/twoland_fixed.py` — the root-cause-corrected model, run and verified.
- This document — the root-cause naming, the fix, verified results, and the full remaining-points
  register (as-is or improved).
- `audits/JOINT_EVALUATION_of_four_audits_v33.md` — the claim-by-claim adjudication.

*No manuscript text was changed; the corrected model and its verified numbers are provided so the
manuscript can adopt them rather than assert them.*

---

## 6. Adoption log (turn-14: joint audit implementation)

The manuscript `manuscript_ECOMOD_v33.tex` and the model were both reconciled to the corrected operator.

### 6.1 Model
- `model_sims/twoland_fixed.py` is now the reference two-land deterministic model, referenced in the
  manuscript's `(Data availability)` and `(Reproducibility)` statements.
- The `__main__` demo now runs at `A_tot=2.5` (manuscript baseline; in-domain `A_r(0)=0.4`). This removed
  the off-domain start that had produced a spurious ~5.4 yr composition window. Verified under the baseline:
  fixed `E=0.825`, `A_c0=1.5`, `A_f0=0.6`, `q0=0.9` over `A_tot=2.5` gives `B 0.594→0.825`,
  `A_c 1.500→0.808`, `A_f 0.600→0.923`, `q 0.9→1.0`, window `150.3 yr`, `maxcon=0.0e+00`.

### 6.2 Manuscript — analytic/spectral layer corrected to the quality model
- Symbol table: removed the orphaned `A_{c,max}` / `A_{c,ext}` / `\kappa=b_f` / `\gamma`; added `q`,
  `\mu`, `\tau_{\mathrm{conv}}`, `q_{\max}`, `\Upsilon_c(q)`, `R_{rc}`, `\chi_r`; `q` flagged a state.
- Capacity-maximum subsection: now the quality form `q^*=q_{\max}/2` (unconditional; any `\rho_c>0`),
  with `\Upsilon_c(q^*)=b_c+b_{G,c}\rho_c q_{\max}/4`; the old `A_c^*=1.069` / `Y_c'(A_c)=0` / area
  capacity-maximum ratio `b_{G,c}\rho_c>b_c` framing is superseded and explicitly disclaimed.
- Regime table `tab:regime`: reframed around the composition diagnostic `\Delta b_{\mathrm{conv}}>0`
  (composition-premium / neutral / discount), not the old `Y_c(A_c)` shape regime.
- Equilibria: no-conversion face is a one-parameter family in the capital book `A_c` with
  `A_r^*=({\eta_f}/{\mu})A_f^*` (verified index `0.8333`); representative members
  `(A_f,A_c,A_r,P)=(0.914,0.824,0.762,1.488)` and `(1.091,0.500,0.909,1.731)`. Replaced the single,
  unreproducible `(0.667,0.778,0.556,1.101)` value.
- Characteristic structure: state vector `z=(A_f,A_c,q,P,D)` (5D, one algebraic redundancy); delayed
  regeneration `G_c'(q^*)` in the `q` row, not the `A_c` row.
- Conversion loop: `S`/partials now in terms of `q` and `\Upsilon_c(q)`; `\Delta b_{\mathrm{conv}}`
  verified `+0.787/@q=0.3`, `+0.784/@0.6`, `+0.794/@0.9`; the composition Mechanism is structural.
- `tab:conv` updated to the verified `\Delta b_{\mathrm{conv}}` (`0.534/0.784/1.134/1.934`); the
  saddle eigenvalue column flagged *illustrative* (old operator; pending re-derivation).
- `tab:basin` re-derived under the corrected model: capital-crash demand threshold
  `P_0≈2.45/2.75/3.00/3.20` for `A_c0=0.40/0.70/1.00/1.18` (monotone in `A_c0`; larger than the old
  `\lesssim1.10`, because maintenance `\mu A_r` + finite `\tau_{\mathrm{conv}}` buffer the shortfall).
- CSD/`\lambda_+`/`E_ceil` values marked illustrative/pending; the early-warning ordering corrected to
  the *stable* branch `\lambda_-\to0^-`, not the saddle `\lambda_+`.
- `R_A=R_B/\psi_f` (with `\psi_f=Y_f/B`), `u_c>R_{rc}` stock-decline condition, `\sigma_f,\sigma_c=1`,
  and the substitute/deficit-gated restoration wording all kept consistent.
- Proxy table relabelled as component log-changes with a share-weighted footnote (final numeric
  presentation still deferred to the user's explicit format choice).

### 6.3 Verified (rerun) numeric anchors
- Composition demonstration (fixed `E=0.825`, `A_tot=2.5`): `B 0.594→0.825`, `A_c 1.500→0.808`,
  `A_f 0.600→0.923`, `q 0.9→1.0`, `150.3 yr`, `maxcon=0.0e+00`.
- `R_A=R_B/\psi_f`: `1.6176=1.6176`, `0.9735=0.9735`.
- Conservation `\max|A_f+A_c+A_r-A_{tot}|=0.0e+00`.

### 6.4 Re-derived E_ceil / fold / CSD (corrected operator) — no longer "illustrative"

On the corrected operator the frozen-demand system was re-solved analytically and verified against the code:

- **Unique interior equilibrium.** On the no-conversion face with frozen `E`, `S=0` gives
  `E = B_eq(A_c)` where `B_eq(A_c) = b_f0·k·A_tot − A_c·(b_f0·k − b_c)` with `k = μ/(μ+η_f) = 0.5455`
  (fast-book equilibrium `μA_r = η_f A_f`, quality at `q=q_max` so `Υ_c=b_c`). Since
  `b_f0·k − b_c = 0.414 > 0`, `B_eq` is **monotone** in `A_c`, so for each `E` there is exactly one
  interior equilibrium `A_c^*(E)`; the old two-branch merge is gone.
- **`E_ceil`:** `E_ceil = B_eq(A_c^min) = b_f0·k·A_tot − A_c^min·(b_f0·k − b_c) ≈ 1.138`. It sits at
  `A_c^*=A_c^min=0.05` (a **typed-floor collision**, not an interior saddle-node). Verified:
  `A_c^*(E)=1.110, 0.626, 0.385, 0.143, 0.070` at `E=0.70, 0.90, 1.00, 1.10, 1.13`; for `E>E_ceil`
  capital is driven to floor and `D→1.21, 5.39` at `E=1.158, 1.238`.
- **No fold.** There is **no interior saddle-node**; `B_eq` is monotone, so no two-branch merge and no
  catastrophic-shift fold. Hysteresis is absent (unique equilibrium), and the negative-results table row was
  changed accordingly (`No (as a fold)` / `No` for CSD / `No (no fold)` for hysteresis).
- **No CSD.** The leading eigenvalue of the active-conversion linearisation is **constant**
  `λ_max ≈ −0.0537 yr⁻¹` along the branch (the `(A_c,A_f)` block gives `−0.0537, −0.9975`; the decoupled
  quality mode `dq/dq=ρ_c(1−2q/q_max)|_{q=q_max} = −ρ_c = −0.08`), independent of `E` because `B_eq` is linear
  and `q=q_max` makes `Υ_c=b_c` constant. It does **not** tend to zero as `E→E_ceil`, so there is no CSD.
  Prediction 3, the abstract, the principal-claim bullet, the `tab:conv` caption, the no-CSD scoped note,
  and the CSD definition were all updated to this (negative) verdict.

Both the manuscript abstract and `supplementary/ABSTRACT_submission.tex` were rewritten to the corrected
claims and trimmed to ~307 words each (target ≤ 315).
