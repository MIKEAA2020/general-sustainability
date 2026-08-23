# A014 Evaluation — Northern Cod Strong-Depensation Test

## Source identity

- Source: `uploads/paper1_final.md`
- SHA-256: `dbb9145aca0765652737f953ff7ea03162d643a33a336db6893eb6cfb3698795`
- Submitted title: *Northern Cod (NAFO 2J3KL): A Present-Tense Test of Strong Depensation*
- Status on receipt: author-labelled final; independently evaluated here as a candidate source, not accepted as final.

## Overall verdict

**Promising bounded empirical/model-discrimination note, but not integration-ready.** Its strongest result is narrower than claimed: an exact nonconstant trajectory of a one-dimensional autonomous ODE cannot reverse direction without encountering an equilibrium, and uniqueness prevents crossing an equilibrium. Therefore a visibly rising-and-falling series cannot be an exact trajectory of one fixed autonomous scalar surplus model. This does not by itself identify the biological mechanism, establish a literal Allee threshold, or reject a noisy state-space/forced/time-varying model.

The two-window distinction—collapse versus delayed recovery—is useful and should be retained. The paper must remove causal overclaims and supply the calculations behind the constrained-M and institutional-margin tables.

## Verified items

1. DFO SAR 2016/026 Table A2 reports the rounded SSB and M values used for 1991–2015. In particular, 1992–1994 values are SSB 381.95, 101.05, 30.55 kt and M 2.214, 2.575, 2.331 yr⁻¹.
2. The displayed survival percentages for 1991–1995 agree with `exp(-M)` after rounding.
3. DFO announced a commercial 2J3KL fishery with Canadian TAC 18,000 t on 26 June 2024.
4. The appendix Python script executes successfully and verifies its four selected toy simulations.
5. The scalar autonomous phase-line obstruction is mathematically sound after restatement as an exact-trajectory result with fixed forcing/removal parameters and uniqueness.

## Live defects and required corrections

### A014-L1 — Autonomous/nonautonomous mismatch

The displayed model contains `C(t)`. It is not autonomous when removals vary with time. State the theorem for constant/removal-free forcing or augment the state and analyze that enlarged autonomous system. A time-varying `C(t)` can generate reversals.

### A014-L2 — Trichotomy overstates finite-time behavior

If the structural threshold lies below the observed low, convergence toward carrying capacity can be arbitrarily slow as parameters approach degeneracy. “Should have climbed far” requires lower bounds on growth and distance from equilibrium. The reliable contradiction is repeated direction reversal in an exact scalar autonomous trajectory, not failure to reach an unspecified biomass by an unspecified deadline.

### A014-L3 — Threshold-shift lemma requires existence conditions

For the displayed cubic, a constant removal or proportional extra mortality shifts the lower positive equilibrium upward only when the modified positive equilibria exist and the loss lies below the relevant production maximum. Larger losses can eliminate the positive basin entirely. State these conditions and distinguish a structural Allee parameter from an effective unstable equilibrium.

### A014-L4 — Assessment parameter is not identified biological cause

NCAM `M` is an estimated unobserved-death component conditional on model structure. DFO framework proceedings explicitly caution that unreported fishing deaths may enter de-facto M. Replace “M-pulse dominates/explains the crash” with “the NCAM M-shift formulation allocates most estimated mortality to M.” The alternative formulation and literature demonstrate structural uncertainty.

### A014-L5 — Moratorium timing cannot be inferred from annual SSB alone

The 2 July 1992 moratorium date is verified, but an annual 1992 SSB estimate does not establish that intervention occurred before a within-year crossing of 300 kt. Remove `Δτ_gov=-1` unless a dated observation/decision series and threshold-crossing convention are supplied.

### A014-L6 — “Fast” does not imply adequate

Response speed, action magnitude, compliance, catch history, ecological lag, and causal effect are distinct. The institutional section may report a timing datum but may not infer adequacy from sign alone.

### A014-L7 — Unreproduced calculations

The following require equations, source series, code, units, windows, and uncertainty: `C/π₀`, 257.8 kt/yr unreported catch, 102.5% of mean SSB, `M_act`, `M_legit`, and the “2 of 3 perverse” classification.

### A014-L8 — Ecosystem discriminants overclaimed

The Tam–Bundy context values may be descriptive mass-balance inputs, not causal tests. “Predator pit not supported” and “no capelin correlation” require a defined estimator, interval, lag structure, and uncertainty. Keep them untested or exploratory until reproduced.

### A014-L9 — Observation and model error

The exact-trajectory rejection must be separated from rejection under measurement error, process noise, age structure, migration, time-varying mortality, and state-space observation models.

### A014-L10 — Publication style and status

Remove internal labels such as “Phase-7,” “Part X,” “Darling killed,” checkmarks, and “SETTLED.” Replace them with theorem, evidence, and limitation language.

## Integration and publication decision

- Do not integrate causal claims or numerical tables beyond verified DFO values.
- Retain the corrected scalar-autonomous counterexample and crash/non-recovery split as a bounded fisheries case.
- Preferred destination: A011 empirical/sampled-governance companion or a flagship case box.
- Reassess separate short-paper merit only after reproducible calculations, uncertainty, and model-comparison corrections. It does not presently add a fourth assured publication identity.
