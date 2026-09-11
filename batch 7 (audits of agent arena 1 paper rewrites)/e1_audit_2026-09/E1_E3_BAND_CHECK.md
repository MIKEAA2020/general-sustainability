# Band check: can E1's retention rule and E3's be unified?

**Run before any merge prose, as the gate on the E1–E3 merge.**
**Date:** 10 Sep 2026 · **Inputs:** `wave_e_edwards/results/rolling_summary.csv` (archived,
16 rows) · **No model was refit.** The check applies a decision threshold to already-computed
RMSE values.

---

## 1. The question

E1's rule requires a module to beat both persistence and its declared comparator by more
than a **5% tie band**, at **both horizons**. E3's rule requires it to beat both, with
**no band**. A merged paper claiming "one rule, two systems" is false unless the two
reconcile. The check: apply E1's rule to E3's archived scores and count verdict changes.

## 2. Result: **no verdict flips. The gate passes.**

Retention outcome on Edwards, both rules:

| rule | retained set |
|---|---|
| E3 as published (no band) | **empty** |
| E1's rule (5% band) applied to the same scores | **empty** |

E3's frozen verdict stands unchanged, and the merged paper can state one rule.

## 3. What the band does change — the route, not the outcome

This is the part that must be reported rather than buried. Two modules change status at
individual horizons, and one changes the *reason* it is excluded.

| module | h | RMSE | comparator | H2 margin vs persistence | H1 margin vs comparator | E3 | E1+band |
|---|---|---|---|---|---|---|---|
| M1 | 1 | 12.84 | — | **+0.0296** | n/a | pass | **fail** |
| M1 | 5 | 21.25 | — | −0.0069 | n/a | fail | fail |
| M2m | 1 | 12.28 | M1 | +0.0716 | **+0.0433** | pass | **fail** |
| M2m | 5 | 17.44 | M1 | +0.1734 | +0.1791 | pass | pass |
| M3 | 1 | 14.46 | M2 | −0.0928 | **+0.0163** | fail | fail |
| M4 | 1 | 14.30 | M3 | −0.0805 | **+0.0113** | fail | fail |
| M3 | 5 | 33.46 | M2 | −0.5853 | **+0.0008** | fail | fail |
| M4 | 5 | 33.39 | M3 | −0.5820 | **+0.0021** | fail | fail |

**Six margins fall inside the 5% band.** Bolded above.

- **M1 at h=1** beats persistence by 2.96% — inside the band. Under E3's rule it passes at
  that horizon; under E1's it does not. It fails at h=5 under both, so the both-horizons
  requirement excludes it either way and the overall verdict is unaffected.
- **M2m** is the substantive case. E3 reports it as beating persistence at both horizons
  and **declines it on class grounds** — it collapses to an AR(1) when fluxes are held
  constant, so it is not extra structure. Under E1's rule it fails H1 at h=1 on a 4.33%
  margin, inside the band. **The same module is excluded by both rules for entirely
  different reasons**: a substantive judgement about model class in E3, an automatic
  threshold in E1.

That coincidence is worth reporting in the merged paper rather than smoothing over. It is
evidence that the tie band and the class-grounds judgement are doing related work — the
band catches, mechanically, a case that E3 had to catch by argument.

## 4. Disclosure required in the merged paper

E3's analysis was pre-registered without a tie band. Applying one is a post-hoc change to
a pre-registered decision rule, and must be stated as such:

> The companion groundwater analysis applied the retention rule without a tie band. The
> present unification adds the band. No retention verdict changes on either system; six
> Edwards margins fall inside the band, and the module they affect was already excluded on
> class grounds. The check is reported in Supplement S-6.

## 5. What this does **not** license

The gate passing permits the merge. It does not complete the methods case:

- **Condition 3 remains unmet.** Operating characteristics are established at one series
  length (T = 33) against correctly specified truths only. The merge adds a second
  application, not a second series length in the power study, and adds no
  misspecified-truth DGP. A reviewer asking "how do you know the rule is not failing
  because of misspecification?" still has no answer.
- The band's behaviour here is **domain-specific evidence of one kind**: on Edwards it
  binds six times without changing an outcome. That is not a demonstration that it is
  domain-neutral.

## 6. Recommendation

Proceed to the merge on the rule question. Sequence unchanged: fix condition 3 before
retitling, since the merge satisfies condition 2 but leaves condition 3 as the binding
constraint on any reusability claim.
