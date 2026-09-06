# v20 exploration — Top‑down macro‑ratio & bookkeeping analysis (Lens 1 + Lens 4)

**Status:** *exploration only — no mint, no push.* This is a findings + recommendation report for
your approval before any v20 is built. Verified on the baseline corrected S0
(`ρ=0.05`, `A_max=1.2`, `b=0.5`, `b_G=0.8`, `e=0.55`, `A_ext=0.02`; `b_Gρ=0.04 < b=0.5`, i.e. the
flow‑dominated regime).

**Headline outcome — the proposed headline is *refuted*, and the corrected result is more useful than
the one it replaces.** The idea "`E > bA` (footprint > flow‑yield) is the true irreversible‑decline
trigger, and this can happen while `E/B < 1`" does **not** survive the model. The verified truth:

1. **The operative decline/collapse trigger is `R_B = 1` (footprint = total biocapacity), exactly.**
2. **`R_A = 1` (footprint = flow‑yield) is a *necessary, earlier* signal but never by itself causes
   decline; in fact a *sustainable* steady state runs at `R_B = 1` with `R_A = 1/ψ > 1`.**
3. **In the long‑regeneration‑lag regime the overshoot ratio (either form) gives *no* forecast** of
   collapse — the decoupling is a genuine, policy‑relevant negative result.

---

## 1. Lens 4 — exact bookkeeping identities (the rigorous foundation)

From `(1‴)`, `dA/dt = G(A(t−τ_g)) − [E − bA]₊/b_G`. Define the **lag‑adjusted biocapacity**
`B̃(t) = b·A(t) + b_G·G(A(t−τ_g))`. In the deficit region (`E > bA`):

```
          E − bA = b_G·G(A(t−τ_g)) − b_G·(dA/dt)                    [exact, no ramp]
   ⇒      dA/dt  = ( B̃ − E ) / b_G                                  [exact]
```

**Corollaries (parameter‑free):**
- `dA/dt < 0  ⟺  E > B̃` — the stock declines **exactly** when the footprint exceeds the
  (lag‑adjusted) biocapacity. With `τ_g = 0`, `B̃ = B`, recovering the manuscript's identity
  `dA/dt = (B−E)/b_G`.
- `dA/dt ≥ 0` whenever `E ≤ bA` (the liquidation term is zero and `G ≥ 0` on `[0, A_max]`), so
  **`E > bA` (`R_A > 1`) is a necessary but not sufficient condition** for decline.
- At any equilibrium (`dA/dt = 0`): `E = B̃`, i.e. **the balance point is `R_B = 1`** — not `R_A = 1`.

> These identities **justify** the macro ratios rather than defining them ad‑hoc (the user's Option‑4
> motivation). They also expose a minor bookkeeping note: the manuscript's `dA/dt = (B−E)/b_G` is exact
> only if `B` uses the *delayed* regeneration `G(A(t−τ_g))`; strictly it is `(B̃−E)/b_G`.

## 2. Lens 1 — the two macro ratios and their roles

Define `R_B = E/B` (standard GFN footprint/biocapacity overshoot) and `R_A = E/(bA)` (footprint ÷
flow‑yield). Since `B = bA + b_G G(A) ≥ bA`:

```
   R_A = R_B · (B/(bA)) = R_B / ψ ,      ψ = bA/B  (the flow share)
```

**Verified onset (baseline, τ_g=10, toe of collapse):** bisecting the recover→collapse boundary for
`A₀ ∈ {0.30,…,1.05}` gives **`R_B = 1.000`** at the boundary in every case, with `R_A = 1.01–1.06 (>1)`
there (table below). So the boundary sits on `R_B = 1`, and `R_A` is already above 1 by the factor `1/ψ`:

| `A₀` | `ψ` | boundary `P₀` | `R_B` | `R_A` |
|---|---|---|---|---|
| 0.30 | 0.943 | 0.289 | **1.000** | 1.060 |
| 0.45 | 0.952 | 0.430 | **1.000** | 1.050 |
| 0.60 | 0.962 | 0.567 | **1.000** | 1.040 |
| 0.90 | 0.980 | 0.835 | **1.000** | 1.020 |
| 1.05 | 0.990 | 0.964 | **1.000** | 1.010 |

## 3. Regime‑scoping closed form (flow share separates the two ratios)

At the *sustainable equilibrium* the two ratios are related in closed form. Where an **interior MSY**
exists (`b_Gρ > b`): `A* = A_max(b+b_Gρ)/(2b_Gρ)`, and

```
   ψ*  = 2b / (b + b_Gρ) = 2 / (1 + b_Gρ/b)
   R_A^eq = 1/ψ* = (1 + b_Gρ/b)/2          (R_B^eq = 1 always)
```

- **Flow‑dominated (`b_Gρ < b`, incl. baseline `b_Gρ/b = 0.08`):** no interior MSY
  (closed‑form `A*` lies outside `[0, A_max]`); the sustainable point is the boundary `A_max`, where
  `ψ = 1` and **`R_A = R_B = 1`** — the two ratios coincide.
- **Increment‑dominated (`b_Gρ > b`):** `R_A^eq = (1 + b_Gρ/b)/2 > 1`, rising with `b_Gρ/b`.
  E.g. `b_Gρ/b = 6 → R_A^eq = 3.5, ψ*=0.286`; `b_Gρ/b = 12 → R_A^eq = 6.5, ψ*=0.154`.

**Consequence (the corrected counter‑intuitive point):** in an *increment‑dominated* system a healthy,
sustainable steady state runs with **footprint > flow‑yield (`R_A > 1`)** — it relies on the
regeneration buffer. So `R_A > 1` is **not** a warning sign; it is the normal operating point there.
Conversely, `R_B = 1` (footprint = biocapacity) is the operative balance point in every regime.

## 4. The genuinely novel negative (ties to §13(9))

Projecting the full 208‑cell baseline basin onto the macro‑ratio plane (fig. 1) shows the overshoot
ratio is a **good selector only in the short/moderate‑lag recovery regime, and fails in the long‑lag
basin‑crisis regime**:

| regime | collapse cells | "silent" collapse — began with `R_B<1` AND `R_A<1` | share |
|---|---|---|---|
| `τ_g = 10` (recovery) | 125 | 2 | **1.6 %** |
| `τ_g = 30` (collapse) | 197 | 72 | **37 %** |

At `τ_g=10` the recover/collapse split runs cleanly along `R_B = 1`; at `τ_g=30` **37 % of collapses
begin from a state where *both* the standard and the flow‑yield overshoot ratios are below 1** — i.e.
neither macro ratio warns, because the regeneration **lag** (not the demand/stock ratio) is the
controlling variable. This is the observable‑level statement of the §13(9) basin‑boundary‑crisis /
no‑CSD result: **monitoring a footprint/biocapacity ratio (in either form) cannot forecast a long‑lag
collapse; only shortening the lag helps.** The figure annotates it.

## 5. Honest rebuttal to the proposed headline

| Proposed (Option‑1 headline) | Verified |
|---|---|
| "`E > bA` is the true irreversible‑decline trigger" | **No** — `dA/dt<0 ⟺ E > B̃ ≈ B` (`R_B=1`); `E>bA` is necessary but not sufficient |
| "this can happen while `E/B < 1`" | **False as a collapse claim** — between `R_A=1` and `R_B=1` the stock still regenerates (`dA/dt>0`); the silent‑collapse cells do NOT satisfy `R_A>1,R_B<1` but rather `R_A<1,R_B<1` (lag‑driven, not ratio‑driven) |
| "monitor `E/(bA)`, because `E/B` is lenient/lagging" | **Partly right for timing, wrong for cause** — `R_A` does cross `1` *earlier* (by the factor `1/ψ`), but it is a *leading indicator*, not the trigger, and its lead is ≈0 in flow‑dominated systems and grows only with increment‑dominance |

## 6. Recommendation for v20

Fold in **§4 (top‑down macro‑ratio identity)** + the **two‑ratio roles** + the **regime‑scoping closed
form** + the **silent‑collapse decoupling** as a short, rigorous addition (a new §4 subsection or a
compact §13(1)‑style lemma). Frame it as:

- **"The balance point is `R_B = 1` (footprint = biocapacity); `R_A = 1` (footprint = flow‑yield) is
  a necessary, earlier *leading* signal but not the collapse trigger; the gap is the flow share `ψ`,
  with the closed form `R_A^eq = (1 + b_Gρ/b)/2` at a sustainable interior MSY."**
- **"In the long‑lag regime *neither* overshoot ratio forecasts collapse (37 % silent) — a warning that
  ratio‑based monitoring cannot replace the lag."** (This is the honest, useful negative.)

This *prevents* a plausible over‑claim and delivers a real caveat. It is **regime‑scoped**, so it does
not assert the (false) baseline `E>bA`-trigger reading.

**Not developed (as you directed):** Option 2 (growth‑accounting) and Option 3 (coarse‑grain 1‑D
reduction) — deferred.

## Files
- Figures: `scans/topdown_macro_ratios.png` (basin in the macro‑ratio plane, τ_g=10 vs 30),
  `scans/topdown_ratio_separation.png` (flow‑share separation closed form).
- This report: `reports/v20_topdown_macro_ratios.md`.
