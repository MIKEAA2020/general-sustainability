# Joint evaluation of the four audits of `manuscript_ECOMOD_v33.tex`

**Input:** `uploads/4 audits_v33 audit.txt` (2710 lines). Four independent audits:
**deepseek** (lines 1–495), **qwen** (497–2093), **gemini** (2231–2445), **grok** (2451–2710).
Each was produced against the live `manuscript_ECOMOD_v33.tex` (609 lines, 7 tables).

**Method.** I did not take any audit at face value. I re-derived the disputed results
from the manuscript source, checked units, and recomputed the empirical numbers from the real
GFN World series (`data/nfa/...1961_2022.csv`). This note records what I verified, the verdict on
each audit as a whole, and the claim-by-claim adjudication.

---

## 0. Headline verdict

**The audits are, jointly, substantially correct, and they escalate in severity. The lowest two are
"consistency-pass" audits; the top two identify real, possibly load-bearing defects.** There is no
audit that is wrong in its *load-bearing* diagnosis. The disagreements between them are (a) severity
and (b) the shape of the repair, not whether the defect exists.

I confirm one genuinely **load-bearing dimensional error** (the conversion operator `S/κ`), two
**structural/architectural** problems (`G_c` double-use and the zero-cropland equilibrium), and a
long tail of **real but fixable** unit / notation / internal-contradiction errors. I also confirm
several claims the audits raised are **audit-overreach**, and I flag where the audits themselves are
imprecise.

**Crucially, the paper's core thesis survives.** grok states it most cleanly in "What still stands":
the **composition-illusion-as-accounting-identity** (`b_f > b_{c,eff}` ⇒ shifting a hectare raises
current `B`), the **identifiability** of gha (yield vs area vs book not identifiable from World `B`
alone), **recovery-not-inverse**, the **regime-conditional fold** (`b_{G,c}ρ_c > b_c`), and the
**informational controller** result are all independent of the conversion-rate bug. What the bug (and
the structural issues) undermine are the *dynamical* "spectral" results — the conversion-fold
eigenvalues, `E_ceil`, "critical slowing down", the "1-to-1 conversion" reading of the 5.4 yr window,
and the additive empirical proxy table.

---

## 1. Per-audit verdicts

| Audit | Locus | Independent verdict | Severity it claims | My severity |
|---|---|---|---|---|
| **deepseek** | Units, notation, Eq-level, numerics | "Clear ideas, not yet internally consistent enough for rigorous use" | high but cosmetic | **Real, mostly fixable**; 2 of its items are load-bearing (units of `D`/`α`; `R_A` identity) |
| **qwen** | Must-fix contradictions + line-level | "Coherent and important ... needs a consistency pass before claims are safe" | must-fix | **Widest and cleanest audit**; nearly every item verified. Very high hit-rate |
| **gemini** | Structural/fatal + architecture | "Critical structural defect ... requires three targeted corrections" | fatal conceptual | **Confirms two genuine structural flaws** (G_c double-use; zero-cropland equilibrium) + a real `R_A` error |
| **grok** | Load-bearing algebra/units | "ODEs are not dimensionally homogeneous; several results are properties of that inhomogeneity, or one-stock leftovers" | **fatal** | **Correct on the key point.** `S/κ` unit inconsistency is genuine and load-bearing |

**No audit requires a "wrong" verdict on its central diagnostic.** The escalation is real: grok and
gemini are not merely thorough — they have found the weakest link, and it is the conversion operator.

---

## 2. Verified claims — adjudication table

Legend: ✅ = **confirmed real** (I verified in the source / by computation); 🟡 = **real but partially
handled already** (scoped in text); ❌ = **audit overreach or imprecise**; ⚠️ = **audit itself imprecise**.

### 2.1 Dimensional / unit — the "fatal-to-serious" tier

| # | Claim | My computation / source | Verdict |
|---|---|---|---|
| **S/κ units** (grok #1, qwen, gemini §2.x, deepseek 3.3) | `S=[E−σ_f Y_f−σ_c Y_c]_+` is `gha·yr⁻¹`; `κ=b_f` is `gha·ha⁻¹·yr⁻¹`; so `S/κ = ha`, **a stock, not `ha·yr⁻¹`** | `S/κ = (gha/yr)/(gha/(ha·yr)) = ha`. ✳ **Confirmed.** Pages 5–6 put `S/κ` into `dA_c/dt` and `dA_f/dt`, which are `ha·yr⁻¹`. The manuscript's own convention note claims "gives `S/κ` in `ha·yr⁻¹`" — **arithmetically wrong**. This is what grok calls "the original `γ=1/b_G` error under a new name." | ✅ **LOAD-BEARING** |
| **`J_c` mixes `1/time` with dimensionless `1`** (grok #1, deepseek 3.2) | `J_c=[[G_c'+Y_c'/b_f, 1],[-Y_c'/b_f, -(1+η_f)]]`; `G_c'` is `yr⁻¹`, `Y_c'/b_f` is `yr`, the `1` is dimensionless | Y_c'/b_f = (gha·ha⁻¹)/(gha·ha⁻¹·yr⁻¹) = **yr**. Adding `yr⁻¹` and `yr` and `1` in one matrix. | ✅ inherited from the `κ` bug |
| **Donor-limited `S/κ ≤ A_c`** (grok #1, deepseek 3.3, gemini) | A rate compared to a stock | `S/κ=ha` (stock) vs `A_c` (stock) — only consistent if `S/κ` is a stock (ΔA one-shot). So it can't be a rate as used in the ODE. | ✅ |
| **Units of `D` and `α`** (all four) | Symbol table: `D` `gha·yr`, `α` `(gha·yr)⁻¹`; baseline: `α=0.03 yr⁻¹` | Eq (11) `dD/dt=[E−B]_+−ηD`. If `D` is `gha·yr`, LHS is `gha` but `[E−B]_+` is `gha·yr⁻¹` → inconsistent. The integral of a `gha·yr⁻¹` flow over `dt` (`yr`) is **`gha`, not `gha·yr`**. To fix: `D` in `gha`, `α` in `gha⁻¹`. | ✅ |
| **Units of `γ`** (deepseek 2.3, grok #7) | Table: `γ=1/b_{G,c}` `ha·gha⁻¹·yr⁻¹` | `b_{G,c}` is `gha·ha⁻¹`, so `1/b_{G,c}` is `ha·gha⁻¹` — **no `yr⁻¹`**. | ✅ |
| **`R_A=R_B/ψ_c` is algebraically false** (all four) | Defines `R_A=E/Y_f`, `R_B=E/B`, `ψ_c=b_c A_c/Y_c`, then writes `R_A=R_B/ψ_c` | `R_B/ψ_c=(E/B)/(b_cA_c/Y_c)=E·Y_c/(B·b_cA_c) ≠ E/Y_f`. The correct share is the **fast-land share** `ψ_f=Y_f/B` (or `b_fA_f/B`), giving `R_A=R_B/ψ_f`. `ψ_c` is the *direct-yield share inside capital*, not the fast share of `B`. | ✅ — genuine algebra error |

### 2.2 Structural / architectural — genuine

| # | Claim | Verification | Verdict |
|---|---|---|---|
| **`G_c` double-use + land-conservation breach** (grok #2, gemini 1.1, qwen 1.2) | `G_c` appears in `dA_c/dt` (Eq 5, as `ha·yr⁻¹`) AND in `Y_c` (Eq 2b, as a flow). If `A_c,A_f,A_r` are conserved 1:1 area summing to `A_tot`, then `dA_r/dt=−dA_f/dt−dA_c/dt` forces `A_r` to fall by `G_c` — an implicit `A_r→A_c` area transfer, contradicting "regeneration is a growth flow, not a land-area transition." | Confirmed in source Eq (5), Eq (7), and convention note. The same object cannot be (i) a conserved area compartment and (ii) a logistic biomass stock. `max|A_f+A_c+A_r−A_tot|=2.2e−16` is vacuous — it holds by definition of Eq (7). | ✅ **structural** |
| **No sustainable cropland equilibrium** (grok #3, gemini 1.2, qwen) | No-conversion face `S=0, η_f>0 ⇒ A_f*=0`; active-conversion face endogenous `P` gives `S=0`. So `A_f*=0` at every equilibrium — agriculture exists only as a transient financed by converting `A_c`. | Confirmed in §Analytic results. Presented as a *virtue* ("no family, no `det J≡0`"), but it is a **defect** of linear `η_f A_f` decay with no maintenance/`A_r→A_f` term. The "balance point `R_B=1`" is not an agricultural steady state. | ✅ **structural** |

### 2.3 Numerical / empirical — real

| # | Claim | My computation from real data | Verdict |
|---|---|---|---|
| **Annualized rates don't match the log changes** (deepseek 4.1, qwen, grok) | Manuscript: `+23.0% (+0.377% yr⁻¹; ln B=+0.207)`; `−52.9% (−0.867% yr⁻¹)` | `ln B=+0.2069` ✓; `/61 → **+0.339%/yr**`, not `+0.377`. `ln(B/P)=−0.7520`; `/61 → **−1.233%/yr**`, not `−0.867`. The manuscript's annualized figures are wrong (they look like arithmetic averages, not continuous rates). | ✅ real |
| **Proxy decomposition not additive** (all four) | Table lists `B +0.207`; `A_f +0.160`; `b_f +1.128`; `B_c^res −0.404` | `0.160+1.128−0.404 = +0.884 ≠ +0.207`. `d ln B` does not equal the unweighted sum of component log changes; it needs share weights `s_f=b_fA_f/B, s_c=B_c/B`. The residual `B_c^res` is not the "composition" term. | ✅ real |
| **Residual is not an independent ecological-capital proxy** (qwen 1.8, grok #9, gemini) | `B_c^res=B_NFA−b_fA_f` | Inherits every calibration error in `b_f(t₀)`, every NFA land type not in `A_f` (grazing, forest products, fishing, carbon), equivalence shifts, and measurement error. It is an **accounting residual**, not a measured capital book. | ✅ (text already partially caveats this) |
| **Demo initial condition off-domain** (all four) | `A_{c0}=1.5 > A_{c,max}=1.2`; `A_{f0}+A_{c0}=2.1`, `A_tot` never given | `G_c(1.5)=0.08·1.5·(1−1.5/1.2)=−0.03 ha/yr` — **negative regeneration at t=0**. The "conversion raises B" reading is overflow+retirement+conversion, not pure conversion. | ✅ real |
| **Basin table text contradicts the table** (deepseek 4.3, grok #8, qwen) | Text: "Lower initial A_c0 has more headroom; higher A_c0 collapses at lower demand." Table: `A_c0=0.40→P₀≲0.9`; `A_c0=1.00→P₀≲1.10` | **Backwards.** Higher initial capital supports *higher* demand. The sentence is directly contradicted by its own table. | ✅ real |
| **`ψ_c*` and `A_c*` correct** (grok #10 note) | `ψ_c*=2b_c/(b_c+b_{G,c}ρ_c)`, `A_c*=1.069` at baseline | Verified earlier; these two displayed formulas survive a unit check. | ✅ holds |

### 2.4 Methodological / epistemic

| # | Claim | Judgment | Verdict |
|---|---|---|---|
| **CSD on the wrong branch** (grok #5, qwen 1.10, gemini 4.2) | `λ_+` (`+0.058→+0.0003`) is the **saddle-positive** eigenvalue. Early-warning CSD is the **stable** branch `λ_−→0⁻` (return time). On a saddle, perturbations diverge; there is no recovery time. | The manuscript's own CSD-definition note concedes "`T_ret` is not defined on the saddle" but still calls it "critical slowing down" and builds Prediction 3 on it. | ✅ real (terminological + substantive) |
| **Hysteresis "bistable equilibria"** (qwen 1.10, grok) | Table: "Hysteresis ... a property of the fold (bistable equilibria)". But the branches are one stable + one saddle = a **threshold/fold**, not bistability (which needs two *stable* equilibria). | The word "bistable" is wrong; "fold-induced threshold / saddle-node transition" is right. | ✅ real (minor wording) |
| **`d ln B` population "artifact" framing** (gemini 4.1, grok #9) | The identity `d ln B = d ln(B/P)+d ln P` is exact; population `+464%`, per-capita `−364%`. But calling the rise a "population-scale artifact" over-claims: an identity is not a causal mechanism, `B` is computed independently of `P`, and this is the *extensive vs intensive* theorem, **not** the composition illusion (`B` up, `A_c` down). | "Keep it; do not brand it as the two-land result" (grok). Adjust wording; keep the per-capita halving as a separate (intensive) result. | 🟡 / partially an **over-claim** — fix framing |
| **"What these share is a single stock" overstates the literature hole** (grok #10) | World3 already contains arable land, soil fertility, non-renewables; Erb/Krausmann/Haberl *are* composition papers. | The positioning sentence is too strong. | 🟡 real (positioning) |

### 2.5 Notation / internal-contradiction tail — real but mostly cosmetic

- **Missing symbols** (`b_{f0}, H_c, R_{fc}, R_{rc}, χ, ρ_r, A_f^max, Δb, κ_w, t_{wave}, Φ, Ψ, V_{eco}`) — ✅ real.
- **`σ_f, σ_c` introduced but set to unity silently** — Eq (4) and symbol table retain them; baseline gives no values; analytics set them to 1. `[E−σY]` vs `[E−B]` (debt) use different deficit definitions → `S>0` possible while `[E−B]_+=0`. ✅ real.
- **`A_r` listed as state but called a balance; system "4-dimensional"**(deepseek 2.6, gemini 3.4, grok #10) — ✅ real, pick one.
- **`A_{c,ext}` never used** (deepseek 2.4, gemini) — ✅ real.
- **`κ` not independent (`κ=b_f` while `b_f` is a derived state via Eq 10)** (deepseek 2.5, grok #7) — ✅ real; must decide `κ=b_{f0}` (freeze) vs `κ=b_f(t)`.
- **`L_c`/`H_c` orphaned** (gemini 3.3, grok #2, deepseek 2.1) — `L_c` appears in Eq (5), `H_c` appears nowhere else; `L_c=0` in all analysis and numerics. ✅ real.
- **LaTeX: `(\\$f,\\$c)` should be `$(\sigma_f,\sigma_c)$`; `$A_tot$` → `$A_{\text{tot}}$`** (gemini 5.1-2, grok #7) — ✅ real.
- **"seven predictions" vs "prediction 7 is both dynamical and observational"** (gemini 5.4) — Prediction 7 is double-listed; dynamical set should be "1–4, 6". ✅ real (minor).
- **"**only shortening the lag helps**" (Allee row) vs Prediction 4 "recover fraction flat in `τ_g`"** (grok #8, gemini 3.1) — direct contradiction: if the boundary is flat in `τ_g`, then shortening the lag is *not* the sole remedy. ✅ real.
- **Fold thresholds conflated: `Y_c^max = 0.0609` vs `E_ceil = 0.478`** (gemini 2.4, grok #5) — Table `tab:regime` says "interior fold at `E=Y_c^max`"; §Analytic results uses `E_ceil=0.478`. These are different objects (`Y_c^max` is capital-land MSY; `E_ceil` is the conversion-capacity ceiling). ✅ real.
- **"no dimensionless parameter is left without its stated unit" is false** (deepseek 5.2) — `Δb, κ_w, χ, A_f^max, σ_f, σ_c, V_{eco}` lack units/baseline. ✅ real.

---

## 3. Independent verification of the key numbers (my own, not the audits')

From `data/nfa/...1961_2022.csv` (World, 2025 edition):

| Quantity | Value (this eval) | Manuscript | Status |
|---|---|---|---|
| `ln B` change | `+0.2069` | `+0.207` | ✅ |
| Annualized `ln B` | `+0.339%/yr` | `+0.377%/yr` | ❌ wrong |
| `ln(B/P)` change | `−0.7520` | `−0.752` | ✅ |
| Annualized `ln(B/P)` | `−1.233%/yr` | `−0.867%/yr` | ❌ wrong |
| `B/P` total | `−52.9%` | `−52.9%` | ✅ |
| Population share of `d ln B` | `+463.5%` | `+464%` | ✅ |
| Per-capita share | `−363.5%` | `−364%` | ✅ |
| Identity residual | `8.3e−17` | "exact" | ✅ |
| `R_B` overshoot onset | `1971` (`E/B=1.006`) | `1971` | ✅ |

---

## 4. Priority fix list (mine, after adjudication)

**Tier 0 — load-bearing (must fix before the manuscript is rigorous; the "dynamical/spectral" results are gated on it):**
1. **The conversion operator.** Either (a) treat conversion as an **instantaneous one-shot area adjustment** `ΔA = b_f^{-1}[E−σ_fY_f−σ_cY_c]_+` (a DAE/algebraic, or a `1/τ_conv` rate with an explicit time constant), or (b) declare `κ` to carry a time constant. **Until then** the conversion-fold eigenvalues, `E_ceil`, "critical slowing", the "1-to-1 conversion" window, and `tab:conv` are *not well defined as reported*. grok's and gemini's diagnosis is correct here.
2. **`G_c` split.** Either keep `G_c` purely in `Y_c` (quality/capacity on area `A_c`; requires an extra quality state `Q_c` and `Y_c=Y_c(A_c,Q_c)`), or accept `G_c` as an `A_r→A_c` area transfer and drop the "not a land-area transition" claim. Do **not** have it be both.
3. **Cropland equilibrium.** Add an explicit maintenance / `A_r→A_f` (pioneer) term, or set `η_f=0` except when the flow is unprofitable, so that a sustainable `A_f^*>0` exists.

**Tier 1 — must fix (correctness/presentation of the empirical and identifiability block):**
4. **`R_A=R_B/ψ_f`** (use the fast-land share `ψ_f=Y_f/B`, not `ψ_c=b_cA_c/Y_c`), or drop the identity.
5. **Additive proxy decomposition** → replace the non-adding table with share-weighted contributions `d ln B = s_f(d ln b_f + d ln A_f) + s_c d ln B_c`, or relabel the rows as *component log changes* (not contributions). Label `B_c^res` a **residual**, not an independent proxy.
6. **Correct annualized rates** to `+0.339%/yr` and `−1.233%/yr` (or state they are total-per-year, and give the continuous rates separately).
7. **Re-run/fix the Demonstration** so `A_{c0} ≤ A_{c,max}` (and state `A_tot`), and stop presenting negative-regeneration startup as pure conversion.
8. **Units of `D`/`α`/`γ`** → `D` in `gha`, `α` in `gha⁻¹`, `γ` in `ha·gha⁻¹` (no `yr⁻¹`).
9. **Basin sentence** → "higher initial capital supports higher demand" (fix the reversed text).

**Tier 2 — should fix (consistency, notation, framing):**
10. `σ_f,σ_c`: set both `=1` in the baseline registry and state it, or carry them through all analytics (the `S=0⇒E=B` step, and `J_c`, assume unity).
11. Define/remove missing symbols (`b_{f0}, H_c, L_c, R_{fc}, R_{rc}, χ, ρ_r, A_f^max, Δb, κ_w, t_{wave}, Φ, Ψ, V_{eco}`); decide `κ=b_{f0}` vs `κ=b_f(t)`.
12. `A_r` state-vs-balance; `A_{c,ext}` remove or use; `L_c/H_c` define or remove.
13. CSD: report it on the stable branch or drop the "CSD precursor" claim; change "hysteresis/bistable" → "fold-induced threshold".
14. "Prediction 7 double-counted"; "only shortening the lag helps" vs flat-in-`τ_g`; fix `Y_c^max` vs `E_ceil` labelling; LaTeX `(\sigma_f,\sigma_c)`, `A_{\text{tot}}`.
15. Soften the "population-scale artifact" and "single-stock shared by all literature" positioning.

---

## 5. What the audits got right / wrong / imprecise (fairness box)

- **No audit's load-bearing diagnosis is false.** The strongest (grok, gemini) are correct about the conversion unit and structural issues; the weakest (deepseek, qwen) are correct about a large tail of real unit/notation errors.
- **Escalation, not error:** deepseek treats the unit errors as "not rigorous"; grok correctly shows the *conversion* unit error is fatal to the spectral results. Neither is wrong; grok is simply the one who followed the `κ` chain to its consequences.
- **Audit-overreach (do not accept):** (i) gemini's claim that the population result is *causally* a "fallacy" — it is an exact identity; the defect is *framing* (don't call it the composition illusion), not arithmetic. (ii) gemini/grok's suggestion that the core **thesis** is refuted — it is not; only the dynamical spectral layer is gated. (iii) Some audits' "5.4 yr is a coincidence/red flag" — it is *not* an independent confirmation either; it should simply be re-derived honestly once the operator is fixed.
- **Audit-imprecision:** grok's "`Y_c'/b_f` is dimensionless" — it is actually `yr`; the point (mixing `yr⁻¹` and `yr` in `J_c`) stands but the stated unit is off. deepseek's "`R_A` defined twice" — it is defined once; the added *identity* is wrong. These do not change the conclusion.

---

## 6. Bottom line

The four audits converge on a real cluster of defects, with grok and gemini correctly identifying
the **structural weakest link** (the conversion operator's units, `G_c` double-use, and the missing
cropland equilibrium). The paper's central **conceptual** contributions — the composition illusion as
an accounting identity, the identifiability of value-weighted gha, recovery-not-inverse, and the
regime-conditional fold — **are not refuted** and are independent of the bugs. What the audits
correctly force is a decision: **repair the conversion operator** (grok's/gemini's architecture, which
differ in whether they add a maintenance term and a quality state) or **re-scope** the dynamical
spectral results as illustrative pending that repair.

*No manuscript text was modified during this evaluation.*

---

## 7. Root cause — named and remediated (verified, not asserted)

The four audits converge on a **single deepest root cause**, which is the same category error the
earlier work called **master RC1** (the environmental stock playing three roles), re-expressed for
two books: **`A_c` is simultaneously conserved area, a capacity stock, and a source of a flow.**
I confirmed both concrete defects **in the code** (`twoland_dyn.py`):

- **D1** — `S/κ = (gha·yr⁻¹)/(gha·ha⁻¹·yr⁻¹) = ha` (a **stock**), yet it is added to `dA_f/dt` and
  `dA_c/dt` (each `ha·yr⁻¹`). A stock added to a rate. The manuscript's convention note ("gives
  `S/κ` in `ha·yr⁻¹`") is arithmetically false.
- **D2** — `G_c` sits in `dA_c/dt` **and** in `Y_c`; via the `A_r = A_tot − A_f − A_c` balance this
  forces a hidden `A_r → A_c` area transfer, contradicting "regeneration is a growth flow, not a
  land-area transition." The `|2.2e−16|` conservation check is vacuous.
- **D3** — with `dA_f/dt = S/κ − η_f A_f` and no `A_r → A_f` term, `A_f* = 0` at every equilibrium.

### 7.1 I built and ran a corrected model (`model_sims/twoland_fixed.py`)

Split the capital book into **area** (conserved 1:1) and **quality** `q` (per-ha capacity, separate
state). Conversion moves area; regeneration is a flow that enters `Y_c` but never the area book.
Conversion is a **rate** with an explicit `τ_conv`; a maintenance term restores a sustainable `A_f*`.

**Verified (re-ran, not asserted):**
```
|A_f + A_c + A_r - A_tot|max = 0.00e+00          (honest 1:1 area book, not an imposed identity)
sustainable equilibrium:  A_f=0.667  A_c=0.778  A_r=0.556  q=1.000  P=1.101   (A_f* > 0, pathology resolved)
composition window (consistent A_tot=2.5, in-domain):  sum of area changes = 0.0000
     B 0.594->0.825  A_c 1.500->0.808  A_f 0.600->0.923  A_r 0.400->0.769   q 0.900->1.000
     final A_c=0.808 (>Ac_min), A_r=0.769 (>=Ar_min)  OK
R_A = R_B/psi_f  (psi_f = Y_f/B)  ->  1.6176 = 1.6176 ; 0.9735 = 0.9735   (identity HOLDS)
delta_b_conv = b_f - b_c_eff  ->  +0.787 (q=.3), +0.785 (q=.6), +0.794 (q=.9)   (robust, structural)
```

**Nothing about the core thesis is refuted.** The composition-illusion-as-accounting-identity, the
identifiability of gha, recovery-not-inverse, and the regime-conditional fold all survive and are
independent of the conversion bug. What is gated (until re-derived on the corrected operator) is the
dynamical "spectral" layer: the conversion-fold eigenvalues, `E_ceil`, "critical slowing down" (it
was computed on the saddle branch), the fixed "5.4 yr" window, the "1-to-1 conversion" reading, and
the additive empirical proxy table.

### 7.2 Remaining audit points — incorporated (as-is or improved)

**As-is (verified real & fixable):** units of `D`/`α`/`γ`; `R_A = R_B/ψ_f`; share-weighted proxy
decomposition; annualized rates (`+0.339`, `−1.233`); demo off-domain / not-1:1 (fixed by consistent
`A_tot` + area/quality split); basin sentence backwards; `σ_f,σ_c = 1`; orphaned `L_c,H_c`; `A_r`
state-vs-balance; missing symbols; CSD on wrong branch; "hysteresis ≠ bistable"; prediction-7
double-count; Allee-row vs Prediction-4 contradiction; `Y_c^max` vs `E_ceil`; LaTeX `(\$f,\$c)`/
`A_tot`; `V_{eco}`.

**After improvement (audit overreach / framework):** the population "artifact" is an **exact identity**,
not a causal fallacy — keep it but as the extensive/intensive result, never as the two-land
composition illusion; the "core thesis refuted" narrative is not supported (only the spectral layer is
gated); glok's "`Y_c'/b_f` is dimensionless" is off (it is `yr`); "5.4 yr is a red flag" is neither —
it was a by-product of the bug.

**Not adopted:** gemini's causal reading of the population identity (an identity is not a causal
claim); the specific architectural prescription (gemini's maintain+surplus-gate vs glok's
instantaneous+quality) — both are satisfied by the minimal common core I implemented; the remaining
choice is the author's.

---

## Addendum (turn-17): status of §4 Priority Fix List against the current manuscript

I re-checked every item of the §4 Priority Fix List (Tiers 0–2) against the *current*
`manuscript_ECOMOD_v33.tex` (which has been re-derived on the corrected operator in the intervening
turns). Nearly all are already implemented. The one genuine residual inconsistency found and fixed:

**Fixed now:**

1. **Assumption (2) `ψ_c*` formula — stale/wrong.** It read `ψ_c^*=2b_c/(b_c+b_{G,c}\rho_c)`, a leftover from
   the superseded *capacity-maximum* ratio framing. Under the corrected quality formulation, capital value is
   `Υ_c(q)=b_c+b_{G,c}G_c(q)` and there is **no interior area-based capacity maximum**, so that ratio is not a
   structural quantity. The direct-yield share of capital value at the regeneration maximum `q^*=q_max/2` is
   `b_c/(b_c+b_{G,c}G_c(q_max/2)) = b_c/(b_c+b_{G,c}\rho_c q_max/4) ≈ 0.758` (the old formula gave 0.877).
   Replaced with the composition diagnostic `Δb_conv = b_f − Υ_c(q)` and the corrected direct-yield share.
2. **Symbols `L_c`, `H_c` (timber channel) were used but undefined.** Added both to the symbol table as
   "extension (off in the base model)".

**Verified already-implemented (no action needed) — the Tier 0–2 list, item by item:**

- **Tier 0-1 Conversion operator:** `u_c=min(S/b_f,\,A_c-A_c^min)/\tau_conv` with explicit time constant; the
  old `S/κ` stock-in-a-rate incoherence is explicitly removed. ✅
- **Tier 0-2 `G_c` split:** quality state `q`; `G_c(q)` is a *flow of capacity*, never an area transfer; area
  book conserved 1:1 (`max|A_f+A_c+A_r-A_tot|=0.00e+00`); regeneration-vs-area book-mixing eliminated. ✅
- **Tier 0-3 Cropland equilibrium:** maintenance term `\mu A_r` ⇒ sustainable `A_f^*>0`
  (family members `(0.914,0.824,0.762,1.488)` and `(1.091,0.500,0.909,1.731)`), not `A_f^*=0`. ✅
- **Tier 1-4 `R_A=R_B/ψ_f`:** corrected; uses fast-land share `ψ_f=Y_f/B` (verified `1.6176=1.6176`). ✅
- **Tier 1-5 Proxy decomposition:** share-weighted (log-mean Divisia), not additive rows. ✅
- **Tier 1-6 Annualized rates:** `+0.339%/yr` and `−1.23%/yr` (not `+0.377`/`−0.867`). ✅
- **Tier 1-7 Demo off-domain:** consistent `A_tot=2.5`, `A_r(0)=0.4≥A_r^min` in-domain; 1:1 area changes. ✅
- **Tier 1-8 Units of `D`/`α`/`γ`:** `D` in gha (accumulation), `α` in gha⁻¹, `γ=1/b_{G,c}` in ha·gha⁻¹
  (no yr⁻¹), `σ_f,σ_c=1`. ✅
- **Tier 1-9 Basin sentence:** "Higher initial `A_c0` supports *higher* demand ... monotone increasing", and
  table thresholds now increase in `A_c0`. ✅
- **Tier 2-10/11/12 Notational tail:** `σ_f,σ_c` set to 1 and stated; missing symbols largely removed or
  defined (`Δb,κ_w,t_wave` are used in Eq. 13; `A_c,ext`, `V_eco`, `ρ_r`, `χ` removed); `A_r` declared a
  constrained balance (5D state); `A_c,ext` removed; `L_c/H_c` now defined (this addendum). ✅
- **Tier 2-13 CSD/bistable:** No CSD (leading eigenvalue constant `−0.0537`, no `λ→0`); no fold; "Hysteresis /
  path dependence No (no fold)"; "bistable" no longer used. ✅
- **Tier 2-14 Register/labelling:** predictions register now "1–4,6 dynamical; 5 regime-conditional; 7
  observational"; "only shortening the lag" vs flat-in-`τ_g` contradiction resolved (remedy is demand/
  restoration change); `Y_c^max` vs `E_ceil` tagging removed (superseded by composition diagnostic). ✅
- **Tier 2-15 Positioning:** population identity reframed as the *extensive/intensive* split, explicitly *not*
  the two-land composition illusion and *not* a causal claim; "single stock" literature sentence softened to
  "treatment of the environment as a single stock or single aggregate balance ... either absent or not
  identifiable." ✅
