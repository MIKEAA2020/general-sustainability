# Joint verification: the two S5.4 / S5.5 audits, checked against code and manuscript

**Scope.** Audit 1 (the "mechanism-with-cost" reviewer) and Audit 2 (the "re-frame as phase-dependent"
reviewer) were jointly evaluated against the actual model code (`model_sims/twoland_fixed.py`,
`model_sims/recovery_metric_and_tau_p_scan.py`) and the manuscript (`manuscript_ECOMOD_v33.tex`) rather than
on the audit claims alone. Each claim below is marked **CONFIRMED**, **PARTLY CONFIRMED**, or **NOT
CONFIRMED / not what is actually wrong** together with the evidence.

---

## 0. The one finding that actually changes the result (and neither audit pinpointed the mechanism)

Both audits demanded that the `R_c>1` / "over-restoration" result be **verified against the ceilings, the
reserve floor and donor limits** before being trusted. That request was correct — and the verification
surfaced a **real defect in my own S5.4 computation, not a model ceiling.**

- **What I had wrong.** The committed `recovery()` integrator applied the bounded technology step `T_b`
  unconditionally. The base model runs with `T_b` **off** (`simulate(..., T_b_on=False)`), and that is the
  configuration used for every reference state and every reported result. With the wave spuriously *on*, the
  surplus-gated run drove `A_c → 2.39` (96% of `A_tot`), pushed `A_r` to `0.049` **below its stated floor
  `A_r^min=0.10`**, collapsed `B → 0.17`, and produced the alarming `R_c(900)=2.07`, `P_end/P_init=0.26`.
- **Corrected (base model, `T_b=0`).** The capital book stays bounded (`max A_c=1.09`, well inside `A_tot=2.5`),
  `A_r` **never** goes below its floor (min `0.602`), `B` stays `O(1)` (`0.70–0.91`), and the over-restoration
  is a *modest* move along the one-parameter equilibrium family (`R_c≈1.07–1.27`), with the population
  re-equilibrating to `P/P^init≈0.90–0.97` (not `0.26`).

> **Verdict on audit 2 §3 ("check `R_c>1` against `A_c,max`/`A_r`/donor"):** CONFIRMED that this check was
> necessary and it caught a genuine flaw — but the flaw was **my wave-on manifold/artefact**, not an
> `A_c,max` ceiling (the model has no interior `A_c,max`; the manuscript's §Model explicitly superseded it).
> The honest state is: **no `A_r`-below-floor and no `A_c`-exceeds-`A_tot` artefact** after the correction.

---

## 1. Audit 1, six "unresolved inconsistencies" — verified against the current manuscript

| # | Audit-1 claim | Verdict | Evidence |
|---|---|---|---|
| 1 | Debt unit: `D` cannot be in `gha·yr` (Eq. 12, symbol table) | **NOT CONFIRMED (already resolved)** | Symbol table now reads `$D$ … accumulated ecological debt & gha` (a stock), and `η D` with `η` in `yr^-1` gives `gha·yr^-1`; `[E−B]_+` is also `gha·yr^-1`, so `dD/dt = [E−B]_+ − η D` is dimensionally homogeneous with `D` in `gha`. Eq. (12) is correct. |
| 2 | `σ_f,σ_c` undefined / implicitly 1 | **NOT CONFIRMED (already resolved)** | Symbol table (dimensionless, param) and parameter table (`1.0, 1.0`), and §Model bullet (2b) states "in the baseline they are set to $1$ … and are stated as such, so that `S=[E−Y_f−Y_c]_+`". |
| 3 | `A_c0=1.5` but `A_c,max=1.2` → `G_c(A_c)<0` | **NOT CONFIRMED (already resolved)** | The corrected **quality** formulation has no interior area-based `A_c,max`; §Model (2) states the old `A_c`-capacity `G_c(A_c)` is superseded. The composition demonstration uses `A_tot=2.5`, so `A_r(0)=0.4≥A_r^min` is **in-domain**; capacity is now the per-ha quality index `q∈[0,q_max]`. |
| 4 | Algebraic error `R_A=R_B/ψ_c` | **NOT CONFIRMED (already resolved)** | §Analytic results gives `R_A=R_B/ψ_f`, and explicitly marks `R_A=R_B/ψ_c` as "algebraically false" (`ψ_c=b_cA_c/Y_c` is the direct-yield share inside the capital book, not the fast share). |
| 5 | Proxy decomposition non-additive; main text sums raw log changes | **PARTLY CONFIRMED / already flagged** | The manuscript explicitly states the raw `Δln` components are "not additive contributions to `dln B`; they cannot be summed directly" and gives the exact share-weighted identity (`w_X… + w_C…`). The empirical series uses the *exact* identity `dln B = dln(B/P)+dln P` (residual `<10^-16`), which is genuinely additive. The additivity caveat is already written. |
| 6 | Restoration sign: `R_fc=χA_fΦ(B−E)` surplus-gated but text calls surplus-gated "inert during shortfall" | **PARTLY CONFIRMED (wording, not an equation error)** | The manuscript's base model treats **`R_rc`** (reserve→capital) as the restoration and relegates `R_fc` (fast→capital) to "a stated variant." The base `R_rc` is indeed surplus-gated (`B>E`). "Inert during a shortfall" is *not* mutually exclusive with being surplus-gated — the gate `(B−E)_+` is zero when `E>B`, so surplus-gating is *by construction* inert during a deficit. The apparent tension is resolved by the phase-dependent wording now added to the main text and S5.4. |

**Summary of audit-1 items 1–6:** five are already resolved in v33 (they were addressed in the
root-cause-corrected build); item 6 is a wording/phrasing issue that is now reconciled rather than a
defect in the equations. None of them is the defect that actually corrupted the S5.4 numbers.

---

## 2. Audit 2 — interpretive advice: all sound and adopted

Audit 2's framing was directly usable and is now **implemented**:

1. **Phase-dependent, not "surplus works."** Confirmed and now measured. From the degraded
   *non-equilibrium* post-crash state, surplus-gating restores `A_c`; at `χ_r≥0.05` it restores it *beyond*
   the reference (`R_c>1`) and the supported population re-equilibrates downward. Crucially, **from the
   degraded *equilibrium* itself (`R_B=1`, so `B=E`) both gates are exactly inert** — the sharpest form of
   "surplus-gating cannot initiate recovery during an active deficit." A new "from degraded EQUILIBRIUM"
   row documents this: `R_c=0` for every gate.
2. **Don't present deficit-gating as false.** Adopted: it is the *only* gate active during the shortfall, and
   at the tested rates it is **swamped by conversion** (`R_c≈0`) — necessary-but-insufficient, not wrong.
3. **Rename `R_c>1` as "over-restoration relative to reference," not "overshoot."** Adopted throughout S5.4
   and the main-text pointer; "over-restoration" is used, and the caveat that it is *the reference*, not an
   ecological optimum, is made explicit.
4. **Report the full end state, not only `R_c` and `P_end/P_init`.** Adopted: the S5.4 table now lists
   `A_c, A_f, A_r, B, P/P^init, min A_r, max A_c, D_peak`, plus conservation (identically `0`).
5. **Neutral population wording.** Adopted: "the surplus-gated restoration path re-equilibrates at a
   substantially lower population (`P/P^init≈0.90–0.97`)" rather than "the population pays"; the
   policy-relevance wording ("matters if maintaining current population is a policy objective") is kept.
6. **Reconcile with the deficit-gating claim; add a main-text summary.** Adopted: the phase-dependent
   sentence added to the main-text recovery paragraph (SI §S5.4) prevents a contradict-the-supplement reading.
7. **Target cap / conversion ceiling policy rows.** Adopted and **computed** (not merely mentioned):
   - surplus + **target cap at `A_c^*`**: `R_c=1.00` exactly, `P/P^init=1.00`, no overshoot — the clean
     target-level stopping rule.
   - surplus + **conversion freeze**: *worse* for debt (`D_peak 0.152→0.546`) and still over-restores — a
     freeze helps the capital book but the debt accrues, so freeze is not a clean fix.
   - deficit + conversion freeze: `R_c=0.05` — still no net recovery, confirming conversion is not the only
     obstacle (the restorative flow is itself weak against the shortfall).
8. **Prediction-6-style revision.** The manuscript's recovery prediction is now stated as phase-dependent
   (surplus-gating inert during the shortfall; deficit-gating acts during it but is swamped unless sized or
   capped; restoration is correctly gated, sized and bounded by floors or a target) — matching the audit.

---

## 3. Audit 2 §3, quantitative re-check (the ceiling / donor / `A_r` question)

Definitive numbers (base model, corrected):

| Policy | `R_c(900)` | `A_c` | `A_f` | `A_r` | `B` | `P/P^init` | `min A_r` | `max A_c` | `D_peak` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| none | −0.00 | 0.051 | 1.336 | 1.113 | 1.138 | 1.39 | 1.113 | 0.057 | 0.152 |
| surplus `χ_r=0.02` | 0.73 | 0.612 | 1.030 | 0.858 | 0.906 | 1.11 | 0.858 | 0.612 | 0.152 |
| surplus `χ_r=0.05` | 1.07 | 0.875 | 0.886 | 0.738 | 0.797 | 0.97 | 0.724 | 0.885 | 0.152 |
| surplus `χ_r=0.10` | 1.27 | 1.030 | 0.802 | 0.668 | 0.733 | 0.90 | 0.602 | 1.092 | 0.152 |
| surplus `χ_r=0.10` **target-cap** | **1.00** | **0.822** | 0.915 | 0.763 | 0.819 | **1.00** | 0.664 | 0.822 | 0.152 |
| surplus `χ_r=0.10` conv-freeze | 1.36 | 1.098 | 0.765 | 0.637 | 0.705 | 0.86 | 0.602 | 1.098 | 0.546 |
| deficit `χ_r=0.05` | 0.00 | 0.055 | 1.334 | 1.112 | 1.136 | 1.39 | 1.112 | 0.060 | 0.145 |
| deficit `χ_r=0.10` | 0.01 | 0.059 | 1.331 | 1.110 | 1.135 | 1.39 | 1.110 | 0.065 | 0.139 |
| **from degraded equilibrium (any gate)** | **0.00** | 0.051 | 1.336 | 1.113 | 1.138 | 1.39 | 1.113 | 0.051 | 0.000 |

**Ceiling / floor / donor answer.** `A_r` is never below `A_r^min=0.10` (min `0.602`); `A_c` never exceeds
`A_tot=2.5` (max `1.098`); `A_f+A_c+A_r=A_tot` to machine precision in every row. The "over-restoration" is
**bounded and in-domain** — it is a real, modest shift along the equilibrium family, *not* a domain violation.
This is the corrected, trustworthy version of the earlier `R_c(900)=2.07` result, which was a wave artefact.

---

## 4. Bottom line

- **Keep S5.4 and S5.5** (both audits recommend; the sections are genuinely useful).
- **Audit 1's six "unresolved inconsistencies" are not, on inspection, open defects in v33** — five are
  already addressed and one (restoration-sign) is a wording tension now reconciled. Audit 1's *instinct* that
  the numbers needed scrutiny was correct, but its specific list was largely stale.
- **Audit 2's diagnostic (verify `R_c>1` against the ceilings/floors/donor) was the productive one:** it
  caught my wave-on computation artefact. Its framing guidance (phase-dependent; deficit not false; rename
  over-restoration; full end state; neutral population wording; target-cap/conversion-freeze rows; main-text
  pointer) is all correct and now implemented.
- **Action taken:** (1) rewrote `recovery_metric_and_tau_p_scan.py` on the base model (`T_b=0`) and from the
  correct non-equilibrium start; (2) replaced the S5.4 table with the corrected base-model numbers + full end
  state + the target-cap and conversion-freeze policy rows + a "from degraded equilibrium" row; (3) replaced
  the misleading `R_c>1`/population-cost reading with the phase-dependent interpretation and "over-restoration
  relative to reference" phrasing; (4) added the main-text phase-dependent pointer and a neutral population
  statement; (5) re-verified SI heading structure, manuscript envs/braces/math, and zero unresolved refs.
- **S5.5 unchanged and confirmed** (recover fraction flat at 0.833 over `τ_p=25–500`; no sustained limit
  cycle / no Hopf up to `τ_p=2000` yr — the single overshoot pulse keeps amplitude ≈0.57 and shifts later).
