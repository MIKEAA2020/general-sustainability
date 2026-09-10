# Master findings register & corrections — ECOMOD-26-1191
## Complete consolidated record of every finding, suggestion, and correction from the whole review

This register pulls together **all** findings and proposals made across the entire conversation
into a single auditable index. It is intended as the authoritative "did we miss anything?" list.
It flags, for each item, whether it has already been written into a deliverable file, and it
records **two corrections to my own earlier statements** plus **two finding that this final
verification pass surfaced and that were not previously documented**.

Three prior deliverables exist (not modified by this document):

1. `ECOMOD-26-1191_review.md` — the flaws / internal-inconsistency critique.
2. `ECOMOD-26-1191_proposed_upgrades.md` — the constructive revision strategy with
   pre-verified fixes.
3. `response_to_human_reviewer.md` — adjudication of the external reviewer's comments (b)–(g).

---

## PART A — New items from this final verification pass

These were **not** in any prior file. They come from re-running the technology scenario and the
collapse endpoint after auditing my own earlier claims.

### A1. CORRECTION — my earlier `review.md` §2 over-stated the condition for the "illusion"

**What `review.md` §2 said:** *"With the paper's Scenario-E wave (Δb=0.3, t_wave=150) it is
**not** [reachable]: b never exceeds ~0.5 (b₀)… Only with a far **stronger/earlier** wave
(Δb ≥ 2, t_wave ≈ 50) does B rise above its initial value — and then M still ends at 0."*

**What the re-run shows (corrected):**

- In the paper's **own** Scenario E (Δb=0.3, t_wave=150), **B does reach 0.5588** — *above* its
  initial value of 0.5. But it does so at t≈50 where **M = 1.084 is RISING** (logistic overshoot
  from the low starting P=0.1), *not* falling. So it is **not** the productivity illusion.
- The genuine illusion (B rising **while M falls**, B > 0.51, M < 1.0) **does not** occur in the
  paper's Scenario E — that part of the original claim is correct.
- **But the threshold is wrong.** With the **same Δb = 0.3** (the paper's own amplitude) and a
  **moved-forward t_wave = 100 yr**, the genuine illusion **does** occur: B peaks at **0.618**
  while M has fallen to **0.847**. So the paper's parameter amplitude is sufficient; only the
  *timing* (t_wave) is what separates "no illusion" from "illusion."

**So the corrected statement is:** the productivity illusion **is reachable at the paper's own
Δb = 0.3**; it requires only that the technology wave **arrive earlier** (t_wave ≈ 100 yr rather
than 150 yr). My earlier "Δb ≥ 2" figure was wrong; the budget needed is smaller, which in fact
**strengthens** the recommendation to demonstrate the illusion. (The `proposed_upgrades.md` §2
representative case used α=0.2, Δb=0.8 — that still works, but a simpler, more persuasive case is
**α = 0.5 (baseline), Δb = 0.3 (paper's amplitude), t_wave = 100 yr**.)

### A2. CORRECTION / REFINEMENT — the technology-increases-debt finding is real but method-dependent

**What `review.md` §7.2 and `proposed_upgrades.md` §4 said:** technology scenario E ends with more
cumulative debt than D (paper's 5.240 vs 4.826), and I framed it as a "technology ⇒ more debt"
rebound.

**Refinement (still holds in direction, but must be qualified):** For Scenario D the debt is
**robust** (~4.83–4.86 across treatments). For Scenario E the reported final debt is **highly
sensitive to the numerical treatment of the singular collapse endpoint** (see A3): I reproduced
5.26, 6.74, and 18.70 depending on whether the population is `frozen`, `crashed`, or left
un-clamped once K→0. **The qualitative conclusion (D_E > D_D) is robust; the specific figure
(5.240) is not.** This must be stated, otherwise the .240-place value reads as more precise than
the model warrants.

### A3. NEW FLAW — the population equation is singular at the collapse endpoint (ill-posed)

This is a genuine flaw I did not previously document (I had only flagged the M ≥ 0 clamp in
`review.md` §7.4).

- Eq. (4): dP/dt = r·P(t)·(1 − P(t−τ_p)/K(t)), with **K = b·M/r_opt**.
- As M → 0, **K → 0**, so the ratio **P/K → ∞** and dP/dt → **−∞**. The right-hand side is
  **unbounded / non-Lipschitz** at the collapse point.
- Verbatim asymptotics I computed (P = 0.01, bottom of the ramp):

  | M (gha) | K | dP/dt |
  |--------:|:--|------:|
  | 0.05 | 2.5e-2 | +1.2e-4 |
  | 0.01 | 5.0e-3 | −2.0e-4 |
  | 1e-3 | 5.0e-4 | −3.8e-3 |
  | 1e-4 | 5.0e-5 | −4.0e-2 |
  | 1e-6 | 5.0e-7 | **−4.0** |

- Consequently **"total collapse to P = 0" is not a smooth approach to an attractor; it is a
  singular blow-up**, and the exact point at which P reaches 0 (and hence how much further debt
  accumulates) depends on the ad-hoc clamping in the discretisation. This is the *underlying* cause
  of the A2 sensitivity, and it is a real modelling defect worth stating as a limitation and
  correcting (e.g. with a minimum-viable-K, a carrying-capacity floor, or a rescaling).
- The gradient blow-up also implies the reported **"max Ω"** divergence (B → 0) and the choices
  about when to stop integrating are likewise method-dependent.

### A4. NEW (supporting) — the mechanism of why earlier technology enables the illusion

The reason t_wave matters: with Δb = 0.3 a wave at t_wave = 150 arrives **after** debt has
already eroded b₀e^{−αD} below b₀, so T(t) just props up a falling b and cannot lift B above its
declining path. With t_wave = 100 the wave lands **while M is still near its (M_max-overshoot)
high point and while D is still small**, so b₀e^{−αD} + T(t) rises above b₀ and B rises while M
begins to fall. This is a clean, mechanistic statement of "illusion requires the technology wave
to outpace the debt build-up," and it directly supports the paper's central thesis.

---

## PART B — Complete findings register (everything from the whole conversation)

Legend — **Status:** `✔ verified` (I reproduced it) · **Doc:** the file that contains it
(R = review.md, P = proposed_upgrades.md, H = response_to_human_reviewer.md, NEW = this register).

### B1. What is CORRECT in the manuscript (verified — do not criticise)

| # | Finding | Status | Doc |
|--:|---------|:------:|:---:|
| 1 | All six scenario-table entries reproduce exactly to 3 decimals | ✔ | P §0, R §0 |
| 2 | Characteristic equation (13) and the Appendix A linearisation are correct | ✔ | R §0 |
| 3 | Both single-delay polynomials are correct (harmless scalar factor) | ✔ | R §0 |
| 4 | No single delay destabilises the baseline (verified up to large τ) | ✔ | R §0 |
| 5 | Scenario-B one-delay Hopf at τ_M≈83 yr, ω≈0.026, crossings ~242 yr | ✔ | R §0 |
| 6 | The two-mechanism division (debt-driven vs delay-transient-driven collapse) | ✔ | R §0, P §0 |
| 7 | Non-delayed 2×2 Jacobian is stable whenever M*>M_max/2 (a₁₁<0) | ✔ | R §9 (fair-credit note) |
| 8 | Dimensions are internally consistent (γ dimensionless; Eq 11/12/13 consistent) | ✔ | R §0, H (b) |
| 9 | Units claim rebuttal: D is gha (not gha·years); α is gha⁻¹ — reviewer (b) is wrong | ✔ | H (b) |

### B2. The substantive flaws (documented in `review.md`)

| # | Finding | Doc |
|--:|---------|:---:|
| 10 | "≈80 yr" threshold governs no shown scenario (sustainable α=0 subsystem; Scenario A has no lags; Scenario D is linearly stable) | R §1a |
| 11 | In Figure 6 the (30,25) diamond sits in the stable region yet Scenario D collapses → two disconnected results | R §1b |
| 12 | Instability is marginal: max Re λ ≈ +0.007 yr⁻¹ over the whole plane (~150-yr e-folding) | R §1c |
| 13 | The boundary is ratio-dependent, NOT a constant-(τ_M+τ_P) contour (e.g. sum=110 gives unstable and stable) | R §1d |
| 14 | Productivity illusion is asserted, never demonstrated; B(t) never plotted; all six scenarios collapse | R §2, P §2 |
| 15 | Half-Earth (Eq 9) caps population, not footprint ⇒ Ω_HE = 0.575, not 0.5 | R §3, P §3 |
| 16 | "No single delay can destabilise" proof sits on an exact knife-edge equality r²a₁₁² = (γ e a₂₁)² = 1.0e-4 | R §4 |
| 17 | "Basin of attraction shrinks" asserted, no basin computation | R §5, P §7 |
| 18 | Scenario B/C outcome is "environment recovers, humans collapse" (opposite of orchard framing) | R §5 |
| 19 | "max Ω not reported" footnote arbitrary (Ω peaks ~5.0 for D, ~4.1 for E; Fig 4 plots them) | R §5 |
| 20 | Unsupported empirical claim "global data 1961–2022…" with no data/figure/reference | R §6, P §8, H (d) |
| 21 | Technology scenario accrues MORE debt than no-tech (paper: 5.240 vs 4.826) | R §7.2, P §4 [see A2] |
| 22 | Environmental delay applied asymmetrically (τ_M lags stock channel; debt channel instantaneous) | R §7.3 |
| 23 | "Total collapse" M=0 reached only by clamping (no M≥0 floor in Eq 1) | R §7.4, P §6 |
| 24 | "Persistent oscillation for η ≥ 0.02" is not generic (narrow band ~0.02–0.05 only) | R §7.5 |
| 25 | Single-delay polynomials contain a spurious ω=0 root (λ=0 is not an eigenvalue) | R §7.6 |

### B3. Goodness / scope issues (documented across R, P, H)

| # | Finding | Doc |
|--:|---------|:---:|
| 26 | γ and ρ asserted without justification; parameters chosen at the knife-edge | P §10, H (e) |
| 27 | "Self-referential" concern — model builds in the debt feedback then "reproduces" collapse; a sufficiency, not an empirical, claim | H (e) |
| 28 | r_opt and e are static and never varied, yet paper promises emergent r_opt(t) | H (c) — partly fair |
| 29 | GFN methodology **is** cited (Borucke et al. 2013); reviewer (d) "no literature cited" is factually wrong | H (d) |
| 30 | Reviewer (d) data-limitation point is correct and corroborated by GFN's own caveats (biocapacity overestimated, overshoot understated) | H (d) |
| 31 | Reviewer (b) units claim "D should be gha·years" is wrong; the legitimate part is that flow-vs-stock convention is never stated | H (b) |

### B4. Proposed upgrades (documented in `proposed_upgrades.md`)

| # | Upgrade | Doc |
|--:|---------|:---:|
| 32 | Replace "≈80 yr" with the ratio-dependent, near-neutral boundary statement | P §1 |
| 33 | Add a "technology-masking" scenario + plot B(t) and M(t) [see A1 for the simpler parameter set] | P §2 |
| 34 | Fix Half-Earth to K = 0.5·B/e (verified: Ω→0.500, M=1.000, P=0.217; vs 0.575/0.970/0.243) | P §3 |
| 35 | Reframe technology→more-debt as a Jevons-type rebound | P §4 [see A2] |
| 36 | Add a debt lag OR justify the asymmetric delay | P §5 |
| 37 | Analyse trivial equilibrium; add a floor; switch to a stiff DDE solver + dt-convergence table | P §6 |
| 38 | Replace "basin shrinks" assertion with a measured stable-fraction (0.506 → 0.042; IC flips) + basin figure | P §7 |
| 39 | Revised internally-consistent abstract | P §9 |
| 40 | Prioritised author checklist | P §10 |

### B5. Numeric anchors produced along the way (verified, reusable)

| Quantity | Value | Source file |
|----------|-------|:-----------:|
| Scenario A steady state (M*,P*) | (0.800, 0.400) | sim.py |
| Scenario B / C final | (1.193–1.194, 0.007–0.009) | sim.py |
| Scenario D / E final M | → 0 (collapse) | sim.py |
| Scenario F (Half-Earth) | (0.970, 0.243, Ω=0.575) | sim.py, halfearth_fix.py |
| Corrected Half-Earth | (1.000, 0.217, Ω=0.500) | halfearth_fix.py |
| Basin stable-fraction (0,0)→(30,25) | 0.506 → 0.042 | basin.py, fig_basin.py |
| Max Re λ over plane | ≈ +0.007 yr⁻¹ | map2.py |
| First unstable points | sum ≈ 77–78 | scan75.py |
| Knife-edge | r²a₁₁² = (γ e a₂₁)² = 1.0e-4 | derived |
| Scenario-B Hopf | τ_M ≈ 83 yr, ω ≈ 0.026 | stab.py |
| dt-convergence of Scenario A M* | 0.8022 (dt=0.5) → 0.8021 (dt=0.05) | converge.py |
| Illusion case (α=0.5, Δb=0.3, t_wave=100) | B 0.5→0.618 while M→0.847 | db_threshold.py / e_trace.py |

---

## PART C — Corrections to the prior deliverable files

I have **not** edited the three prior files (so as not to disturb them). Recommended manual edits:

1. **`review.md` §2** — replace the sentence *"Only with a far stronger/earlier wave (Δb≥2,
   t_wave≈50) does B rise above its initial value — and then M still ends at 0."* with the
   corrected statement from **A1**: the illusion is reachable at the paper's own **Δb = 0.3**,
   requiring only an earlier **t_wave ≈ 100 yr** (verified: B→0.618 while M→0.847); note also that
   in the paper's own Scenario E, B reaches 0.5588 but via **M rising**, not the masking mechanism,
   so the "no shown scenario exhibits the illusion" conclusion stands.
2. **`review.md` §7.2 and `proposed_upgrades.md` §4** — add the A2 qualification: the direction
   (D_E > D_D) is robust, but the specific figure is method-dependent because of the A3 singularity.
3. **`review.md` §7.4 and `proposed_upgrades.md` §6** — extend with **A3**: the population
   equation is itself singular (non-Lipschitz) at K→0, which is the deeper cause of the
   collapse-endpoint method-dependence; and note the "max Ω" divergence is likewise method-dependent.

---

## PART D — Should-answer author checkpoints that are now complete

The following reviewer / self-posed questions all have verified answers in hand:

- *Is the productivity illusion demonstrable?* **Yes** — A1 gives a one-line change (move
  t_wave earlier) that produces it.
- *Does chasing the illusion require implausible parameters?* **No** — the paper's own Δb = 0.3
  suffices with earlier timing.
- *Is the reported debt figure trustworthy?* **Direction yes, magnitude no** — A2/A3.
- *Is the Half-Earth result self-consistent?* **No as written; fixed by K = 0.5·B/e** — P §3.
- *Is the "≈80 yr" number a result?* **It is a marginal, ratio-dependent boundary of an
  unscenariosed subsystem** — R §1.
- *Are the units wrong (per reviewer b)?* **No** — D is gha, α is gha⁻¹; only the flow/stock
  convention needs stating — H §(b).

---

## PART F — Adjudication of two independent model-audits (added after cross-checking Claude & Grok audits)

Two line-level audits of the manuscript were later supplied. I verified every substantive claim.
Full detail is in `evaluation_of_model_audits.md`; below are the additions/changes to THIS
register.

### F1. CORRECTION to my own earlier claim (in `review.md` §0/§9) — the zero-delay stability condition is `a11 < r`, NOT `a11 < 0`.
**Both audits are right; I was wrong.** For the coupled non-delayed system `A+B+C`, Routh–Hurwitz
gives `tr = a11 − r < 0` ⇒ **`a11 < r`**, and `det = γe·a21 − r·a11 = r·ρ·M*/M_max > 0
identically` (using `ρ(1−M*/M_max) = γeb0/r_opt`). So `a11<0` is *sufficient but not necessary*;
the exact condition is `a11<r`, and the paper's condition (12) is over-restrictive. (Numerics for
the paper's chosen parameters are unaffected since `a11=−0.5 < r=0.02`.)

### F2. NEW FLAW (missed by me and the paper) — the "M_max/2 threshold from which recovery is impossible" is FALSE.
Logistic recovery `ρM(1−M/M_max) > 0` for **every** 0 < M < M_max (verified numerically). M_max/2 is
the *maximal-regeneration* point, not a separatrix; there is no bistability or irreversibility in a
plain logistic. The only absorbing state is M=0 exactly (and only via the numerical clamp — see
A3). The manuscript **contradicts itself**: §5 *Limitations* says it "neglects hysteresis and
irreversible thresholds," yet §4/§5 claim an irreversible threshold at M_max/2. The real collapse
mechanism is *sustained delayed depletion* (`γE(t−τ_M)` does not scale with M), NOT the logistic
hump. This is more central than the "≈80 yr" over-claim.

### F3. SHARPER VERSION of my earlier "knife-edge" finding — the correct classification is by a sign of `Λ`.
`Λ ≡ r²a11² − (γea21)²`. The two single-delay quartics have opposite-sign constant terms, so:
- `Λ < 0` ⇒ environmental lag `τ_M` alone Hopfs (Scenario B; paper's ≈83 yr is this case),
- `Λ > 0` ⇒ **demographic lag `τ_P` alone Hopfs**, and
- `Λ = 0` ⇒ neither (measure-zero curve; the baseline sits exactly here because `ρ=3γeb0/r_opt=1.5`
  forces `M*/M_max=2/3` and `r²a11²=(γea21)²=10⁻⁴`).

**Verified:** for `ρ=1.6` (`Λ=+4.4×10⁻⁵>0`, a11=−0.6), the demographic delay alone Hopfs with
`ω≈0.0114 yr⁻¹` at `τ_P≈224.6 yr` (subsequent at ≈777, ≈1329 yr). **This refutes the paper's
stated sufficient condition** `r²a11² ≥ (γea21)²`; strict `>` actually *guarantees* a τ_P-only Hopf.
The correct statement is: *generically exactly one lag is individually destabilizing, selected by
the sign of `Λ`.*

### F4. NEW methodological point (why this was easy to miss) — the demographic-delay Hopf lives at `τ_P≈225 yr`.
My earlier single-delay scans stopped at τ_P≈150 and found no Hopf. The competing τ_P-only Hopf
appears **only at a large τ_P (≈225 yr) and slow ω (≈0.011 yr⁻¹)** off the knife-edge. So the
paper's 41×41 grid over τ∈[0,80] **cannot** rule out a single-delay Hopf. Any "no single delay
destabilizes" conclusion must be stated as a function of `Λ` and any scan must extend to τ_P≳250 yr.

### F5. The `τ_M=0` polynomial degree. — Claude is right (Grok's main text is wrong).
The correct `τ_M=0` elimination (via the clean modulus `|Q(iω)|=|P(iω)|`) is **degree 4**:
`ω²(1250ω²+287) = ω²(ω² + a11² − r² − 2γea21)·(ω² + a11²)`. The paper's degree-6 form
`ω²(2500ω⁴+1199ω²+143.5)` contains a **spurious `(ω²+a11²)`** factor. Conclusion (no positive root)
survives, but the "analytic proof" was not performed cleanly.

### F6. Other audit-flagged items (valid, add to record)
- **ρ=1.5 yr⁻¹ is implausibly fast**: `1/ρ≈0.67 yr` vs `τ_M=30`, `τ_P=25`; `ρ/r=75`. So `τ_M` acts
  as a *pure sink delay* while regeneration is effectively instantaneous — the "slow environment,
  lags matter" story is not realised (Grok).
- "Verified to machine precision" is **circular** (at τ=0 the equation is det(λI−(A+B+C))=0,
  satisfied by construction) and the `<10⁻¹⁶` residual is at double-precision ε (Claude).
- §5 lists **"antibiotic resistance"** as an overshoot symptom — non sequitur; and the
  elevator/"sudden break" metaphor contradicts Scenarios B/C's *asymptotic* decay (Claude).
- Truncated sentence `"when *ted near the notional equilibrium"` in §4 (literal typo).
- Claude's reference list and GFN data-limitation treatment are strong and should be adopted.

### F7. Where an audit is NOT right
- Grok's "corrected τ_M=0 polynomial is degree-6" is refuted (see F5); his own appendix says
  degree-4 — internally inconsistent.
- Grok's "no change needed" for Half-Earth (just mention Ω=0.575) does not fix the internal
  inconsistency the manuscript itself creates (text says "caps at half"; realized is 57.5%).
- Claude's proposed *redesign* (Allee term, multiplicative debt `b=(b₀+T_b)e^{−αD}`, `θ`-switch,
  `K_true/K_perc`, adaptation law, yield-vs-efficiency split) is excellent but is **a new model,
  not a repair**; present minimal corrections as primary, redesign as an option.

---

## PART G — Audit completeness statement (updated)

Every finding generated in the conversation is now documented. Prior findings are in `review.md`,
`proposed_upgrades.md`, `response_to_human_reviewer.md`, the earlier Part A of this register, and
the audit adjudication in `evaluation_of_model_audits.md`. This pass added: **two corrections to my
own prior statements** (F1 zero-delay condition; F5 polynomial degree), **two newly-surfaced flaws I
had missed** (F2 false M_max/2 threshold; F4 scan-truncation artifact / F3 Λ-classification), and
**one supporting methodological insight** (the τ_P≈225 yr Hopf). No findings remain floating
outside the five files (`review.md`, `proposed_upgrades.md`, `response_to_human_reviewer.md`, this
register, and `evaluation_of_model_audits.md`).
