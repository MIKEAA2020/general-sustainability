# Cod & sprat discrimination — stage-model three-way test (2026-08-08)

**Purpose.** Use the verified stage-structured (maturation-delay) model to
discriminate, for two real stocks, whether observed dynamics are consistent
with (a) the institutional-delay mechanism (τ inside a window, τ=0 stable),
(b) the biological delayed-recruitment (cohort) mechanism (τ=0 already
oscillatory), or (c) neither. Code: `cod_sprat_discriminator.py`; model
machinery `stage_r_window.py` + `stage_decomp2.py` (validated: g=0 reproduces
base windows; τ=0 classifier nonlinear; dt-converged cycles).

## Data provenance (honest)

- **Iceland cod (cod.27.5a):** the ICES series could NOT be re-pulled this
  session (SAG data endpoint 404s; stockassessment.org mirror timed out). We
  use the observed facts already verified from the full ICES 1955–2023 series
  in the manuscript's empirical section: post-1995 sustained fluctuation,
  CV = 0.387, peak-to-trough 1.25, cycle period ≈ 10–15 yr; haddock under the
  same 1995 HCR: CV = 0.143 (internal control).
- **Baltic sprat (SPRAT22-32):** RAM Legacy v4.66 (local
  `ram_target_stocks.csv`), 1974–2023, n = 50 — pulled and analyzed here.

## Method

For each (r, g, η) cell: τ=0 stability class (nonlinear, 1%-perturbation
single-delay RK4, T=8000 yr) + institutional crossing windows (two-delay
characteristic criterion) + verdict at the case's institutional lag τ_case:
INSTITUTIONAL (τ_case inside window), STABLE (below/above window), or COHORT
(τ=0 oscillatory). η ∈ {0.914 (baseline), 3.0 (max effort response)}.

## Test 1 — Iceland cod (r = 0.2–0.3, g = 5–7 yr, τ_case = 0.25 yr)

| r | g | r·g | η=0.914 | η=3.0 |
|---|---|---|---|---|
| 0.20 | 5 | 1.00 | stable, no window → STABLE | cohort P₀=40 yr → COHORT |
| 0.20 | 6 | 1.20 | window (18.5,22.7); τ_case below → STABLE | cohort P₀=47 yr → COHORT |
| 0.20 | 7 | 1.40 | window (14.9,33.2); τ_case below → STABLE | window (5.2,12.9); τ_case below → STABLE* |
| 0.25 | 5 | 1.25 | stable, no window → STABLE | cohort P₀=38 yr → COHORT |
| 0.25 | 6 | 1.50 | window (11.7,26.4); τ_case below → STABLE | window (2.9,10.8); τ_case below → STABLE* |
| 0.25 | 7 | 1.75 | cohort P₀=35 yr → COHORT | window (5.0,11.4); τ_case below → STABLE* |
| 0.30 | 5 | 1.50 | window (9.9,20.3); τ_case below → STABLE | cohort P₀=22 yr → COHORT |
| 0.30 | 6 | 1.80 | cohort P₀=30 yr → COHORT | window (3.1,9.4); τ_case below → STABLE* |
| 0.30 | 7 | 2.10 | cohort P₀=26 yr → COHORT | window (5.2,10.2); τ_case below → STABLE* |

(* = τ=0 classification "drift" — neither converged nor cleanly cycling within
T=8000; verdict for τ_case still valid since τ_case < window lower edge.)

**Verdict: the institutional mechanism is REJECTED for Iceland cod at both η.**
In every grid cell, cod's implementation lag τ = 0.25 yr lies far below the
institutional window's lower edge (9.9–33 yr across cells): the stage model
never predicts institutional oscillation for a lag of a quarter-year. The
cohort mechanism appears only at r·g ≳ 1.75 (η=0.914; P₀ = 26–35 yr) or broadly
at η=3.0 (P₀ = 22–47 yr) — 2–3× longer than the observed 10–15 yr. **Neither
channel cleanly explains cod's observed cycles** — quantitatively confirming
the manuscript's conclusion that cod is confounded (cohort resonance /
outside-model mechanism), and replacing the earlier qualitative
"15–25× period mismatch vs the four-state core" with a stage-model statement:
institutional: impossible at τ=0.25; cohort: present but 2–3× too slow.
The haddock control (CV 0.143 under the same HCR) remains unexplained by the
model class, as before.

## Test 2 — Baltic sprat (r = 0.6–1.0, g = 1.5–2.5 yr, τ_case = 1.5 yr)

Observed (this run, RAM v4.66): CV = 0.400 full series / 0.241 post-1995;
peak-to-trough 7.8; SSB mean 890 kt (min 223, max 1730). Spectral: variance
dominated by the low-frequency band — 54% of normalized power at periods
20–50 yr (≈28-yr trend-like structure); top peak 27.9 yr (power 0.0039) sits
just below both the pointwise-95% AR(1) red-noise threshold (0.0040) and the
multiple-testing-corrected threshold (0.0053). **No robust significant period
emerges** (the earlier session's "16.7 and 4.2 yr significant" is not
reproduced under a strict AR(1) null — method-dependent; 4.2 yr ≈ harmonic of
the ≈28-yr low-frequency structure).

Model grid (key cells):

| r | g | r·g | η=0.914 | η=3.0 |
|---|---|---|---|---|
| 0.8 | 2.0 | 1.60 | window (2.6,7.7) yr, P≈8 yr; τ=1.5 below → STABLE | window (3.1,7.8) yr, P≈8 yr; τ=1.5 below → STABLE |
| 0.7 | 2.5 | 1.75 | cohort P₀=10 yr → COHORT | cohort P₀=11 yr → COHORT |
| 0.9 | 2.0 | 1.80 | cohort P₀=8 yr → COHORT | cohort P₀=8 yr → COHORT |
| 1.0 | 2.0 | 2.00 | cohort P₀=8 yr → COHORT | cohort P₀=8 yr → COHORT |
| 0.6–0.7 | ≤2.0 | ≤1.4 | stable, no window → STABLE | stable, no window → STABLE |

**Verdict: null on the sharpest prediction, not a positive test.** The model's
new institutional claim for sprat-class parameters (r≈0.8, g≈2) is a ≈8-yr
sustained oscillation for implementation lags τ ∈ (2.6, 7.8) yr. Baltic
sprat's actual τ (ICES annual TAC implementation, ≈1–1.5 yr) sits **below** the
window, so the model itself predicts STABLE for this stock — and the observed
series shows no robust ≈8-yr cycle, consistent with that null. The strong
observed variance is low-frequency (non-stationary trend/regime structure,
CV 0.40), outside the model's scope (recruitment/ecosystem drivers). At higher
r (0.9–1.0, cohort region) the model predicts 8–12-yr oscillations at τ=0 —
also not robustly observed. So Baltic sprat does NOT test the pre-registered
sharp claim; a stock with τ ∈ (2.6, 7.8) yr is required for that test.

## What the two tests together establish

1. The institutional mechanism at a short lag (τ ≈ 0.2–1.5 yr) is rejected in
   both cases — consistent with the manuscript's fast-lag conclusions; cod is a
   quantitative confirmation (institutional impossible at τ=0.25; cohort
   2–3× too slow), sprat is a null (τ below window; model predicts stable).
2. The genuinely new, still-untested prediction is the decadal institutional
   window for τ ∈ (2.6, 7.8) yr at sprat-class parameters — it needs a stock
   whose real implementation lag falls inside that range (some TAC systems with
   2–3-yr cycles between decisions/actual enforcement, or reform events).
3. Neither case validates the mechanism positively; both are consistent with
   the manuscript's cautious empirical stance, now with stage-model numbers.

## Honest caveats

- cod raw series not re-pulled this session (SAG API 404); observed facts from
  the manuscript's verified analysis of the ICES series.
- r, g for cod/sprat are literature-range estimates; verdicts are robust to the
  grid within each η, but η itself is uncalibrated for real fisheries (both
  values reported).
- "drift" τ=0 cells at η=3.0 (cod) are ambiguous; reported as STABLE for the
  τ_case verdict only, with the caveat that τ=0 may be marginally unstable.
- Spectral significance is method-dependent (E2 vs this run); the honest
  statement is "no robust period," not a confident period list.
- The stage bands themselves remain not collocation-classified (open item);
  this does not affect the τ_case-below-window verdicts, which only need the
  window lower edges.
