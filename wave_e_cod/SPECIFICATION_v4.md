# Specification sheet v4 — Retention-rule operating characteristics, Ω_sim

**Sheet status: PRE-REGISTRATION — LOCKED, NO SIMULATION RUN.**

**Issued 10 Sep 2026, before any synthetic series has been generated, fitted, or scored.**
Nothing in this sheet has been executed. If any element below changes after a result
exists, the change must be recorded as a dated amendment and the affected result reported
as exploratory.

---

## 0. Why this object exists

Six audit rounds have accepted E1's empirical result and pressed one objection that the
manuscript cannot answer from its own data:

> the negative result may be a power problem rather than a real failure of the added
> structure.

The manuscript currently answers this with scope language — non-retention is a statement
about these implementations on these series. That is honest but not informative: it does
not tell a reader whether the retention rule *could* have detected a real improvement had
one been present.

Ω_sim answers exactly that question and nothing else. It measures the **operating
characteristics of the retention rule** on synthetic data where the truth is known.

### What this sheet does not do

**v4 does not amend, relax, supersede, or reopen `SPECIFICATION_v2.md`.** Every v2 verdict
stands untouched and is not re-derived here. Ω_sim scores **synthetic** series; it cannot
retain a module on Northern cod, cannot promote one, and cannot alter a v2 verdict. No
number in Tables 3–10 changes as a result of this sheet.

It is also distinct from `SPECIFICATION_v3.md` (Ω_lag, Ω_lag-C, Ω_pit), which proposes new
*modules* on the real series. v4 adds no module. It re-uses the existing five-rung ladder
unchanged and varies only the data.

---

## 1. The claim under test

**H_sim.** On synthetic series generated from a known member of the ladder's own model
class, with sample sizes and noise levels matched to the real specifications, the
retention rule of Definition 2.4 retains the true generating module at a rate materially
above its false-retention rate.

Two outcomes are interesting and both are declared in advance:

- **If power is adequate** — the rule retains a true module often on synthetic data of the
  same size and noise as the real series — then Northern cod non-retention is evidence
  that these data do not support these modules, not that the rule is blind.
- **If power is poor** — the rule rarely retains even a true module at this sample size —
  then the manuscript's negative result must be reported as **substantially
  power-limited**, and the scope language strengthened accordingly. This outcome would
  weaken the paper's headline and must be reported with equal prominence if it occurs.

**Neither outcome is preferred.** Recording both here removes the option of presenting
whichever result is more flattering.

---

## 2. Data-generating processes — fixed before scoring

All DGPs are members of the ladder's own class, using `run_ladder.step` and
`run_ladder.surplus` **imported unmodified**, so the simulation cannot differ from the
estimator by reimplementation. (This is the rule adopted after round 5, where a hand-rolled
refit disagreed with the registered estimator.)

| DGP | Truth | Parameters, anchored to archived fits |
|---|---|---|
| **D1** | M1, autonomous Schaefer | `r = 1.935`, `K = 1032.7`, constant `C = 240` (collapse-window fit) |
| **D2** | M1, low-productivity regime | `r = 0.458`, `K = 500.0`, constant `C = 5` (recovery-window coarse fit) |
| **D3** | M2, stock-flow | `r = 1.935`, `K = 1032.7`, prescribed `C_t` = the coarse regime path 240/120/5 |
| **D4** | M1b, genuine depensation | `r = 0.458`, `K = 500.0`, `𝔰 = 15` kt — a **positive, identifiable** threshold, unlike the real fits |
| **D5** | Persistence-true null | `S_{t+1} = S_t + η_t`, no surplus term, `C ≡ 0` |

**Process noise.** `σ ∈ {11.8, 33.8}` kt, the archived recovery- and collapse-window
residual standard deviations. Innovations are Gaussian, applied inside `step` exactly as
`ε_t` enters the registered map.

**Series length.** `T = 33`, matching Specification A (1983–2015). Specification B's
`T = 71` is **not** simulated in the core design; see §2b.

**Replicates.** **200 per cell**, seeded (`seed = 0`, incremented deterministically per
replicate). Cells = 5 DGPs × 2 noise levels = 10; total 2,000 rolling-ladder passes.

**Why 200 and not 1,000.** A rolling-ladder pass on `T = 33` costs ≈7 s, measured. The
1,000-replicate design in the first draft of this sheet implied ≈70 h and was not
executable. At 200 replicates the 95% interval on a proportion near 0.80 is ±5.5 pp, which
resolves the 0.80 and 0.90 thresholds of §5 without ambiguity, at a cost of ≈4 h. The
count is fixed now and will not be raised after seeing results.

### 2b. Declared extensions, not part of the core claim

`T = 71`, `σ = 0`, and `𝔰 ∈ {5, 30}` are **declared but deferred**. If run later they are
reported as extensions with their own replicate counts, and they cannot revise the core
thresholds of §5. Recording them here prevents a later run being presented as if it had
been part of the original design.

## 3. What is applied to each synthetic series

**The retention rule of Definition 2.4, unchanged**: H1 (beat the declared comparator), H2
(beat persistence), H3 (both horizons, 5% tie band). The same five-rung ladder, the same
`fit_params` estimator, the same rolling-origin construction with the same minimum training
lengths, the same `h ∈ {1, 5}`.

**Nothing is tuned to the synthetic data.** If the rule performs badly, that is the result.

---

## 4. Declared outcome measures

For each cell:

1. **True-module retention rate** — proportion of replicates in which the generating module
   is retained. This is the power of the rule.
2. **False-retention rate** — proportion in which a non-generating structural module is
   retained. Under D6 (persistence-like null), any structural retention is a false positive.
3. **Persistence-wins rate** — proportion in which no module is retained, directly
   comparable to the real result.
4. **Tie-band sensitivity** — items 1–3 recomputed at bands of 0%, 5%, 10%.
5. **Horizon sensitivity** — items 1–3 under h=1 only, h=5 only, and both (the rule as
   written).

Reported as a table per DGP, plus an operating-characteristic curve of true-module
retention against σ at each T.

---

## 5. Declared interpretation, written before the result

Two thresholds, fixed now, following the reviewer's formulation:

- **Power.** For a module that is true and identifiable, the rule should retain it in
  **≥ 80%** of replicates under the baseline DGP.
- **Specificity.** Under the persistence-true DGP (D5), the rule should retain **no**
  structural module in **≥ 90%** of replicates.

| Observed | Reported conclusion |
|---|---|
| Both thresholds met | The rule is an adequate decision instrument at this sample size. Northern cod non-retention is then a data and identification result, not an artefact of the rule. |
| Power < 80%, specificity met | The rule is conservative: it under-retains true structure. The cod negative result must be reported as **partly power-limited**, with the measured rate stated in the Discussion. |
| Power < 30% | The rule is **substantially underpowered** at this sample size, and the manuscript's negative result must say so **in the abstract**. |
| Specificity < 90% | The rule over-retains under a null. The 5% tie band is too permissive, and this must be disclosed as a defect of the instrument. |

**These thresholds may not be adjusted after seeing the curves.** Either outcome is
reportable; only misreporting is not.

## 6. Known limitations, disclosed in advance

- **The DGPs are members of the ladder's own class.** This measures power against
  correctly-specified alternatives, which is the *easiest* case. Real power against
  misspecified truth is lower, so an adequate-power result here is an upper bound.
- Synthetic series are noise-free in the predictand: they do not reproduce the assessment
  smoothing that makes the real target autocorrelated. Persistence is therefore likely to
  be a **weaker** baseline in simulation than in reality, which again flatters the rule.
- No catch-reconstruction error, no assessment revision, no observation error on the state.
- Consequently: **a good power result does not license the claim that the real result is
  fully explained.** It licenses only the narrower claim that the rule detects real
  improvements in the class it was designed for.

---

## 7. Verification gate

Before any Ω_sim result may be reported:

1. `manuscript_style_scan.py` — 0 blockers.
2. `tier3_guard.py BASE.tex NEW.tex --si E1_SUPPLEMENTARY.md` — 0 blockers.
3. Compile from `paper rewrites/`.
4. `tier3_guard_selftest.sh` — 5/5.
5. **v2 invariance:** every v2 verdict, score and table value byte-identical to the v37
   record. Any change is a blocker, not a finding.
6. **Import check:** the simulation must call `run_ladder.step`, `run_ladder.surplus` and
   `run_ladder.fit_params` directly. A reimplementation of any of the three fails the gate.
7. **Determinism:** two consecutive runs produce byte-identical output.

---

## 8. Reporting rule

Ω_sim results are reported as a **methods validation of the retention rule**, in their own
section, explicitly outside the scored ladder — the pattern used for the capelin ablation
(`E1_SUPPLEMENTARY.md` SI-1) and carried into v3. The synthetic retention rates are never
placed in Tables 3–10 and never compared row-for-row with the real scores.

---

## 9. Authorisation status

**Written and locked. Execution authorised immediately after locking, per the
round-8 decision; results reported in `E1_SIMULATION_RESULTS.md` and in the manuscript's
"Rule operating characteristics" section.**

The manuscript as it stands (v37) makes no claim this sheet would contradict. Executing
Ω_sim is what would justify the methods reframing proposed in the round-8 review — and,
with it, the retitling that is currently held under the standing title lock. Until it is
run, the paper remains a case study with a stated protocol, which is what its title says.
