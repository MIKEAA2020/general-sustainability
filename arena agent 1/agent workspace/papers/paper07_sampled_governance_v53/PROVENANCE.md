# Provenance and verification — Paper07 v53

**Edition:** Paper07 v53, standalone  
**Base edition:** Paper07 v52  
**Date:** 2026-10-16  
**Parallel edition preserved:** Paper08 v48, the combined manuscript; this work does not overwrite or merge it.  
**Repository destination:** `MIKEAA2020/general-sustainability`, branch `e2-v3-source-year`, at `arena agent 1/agent workspace/papers/paper07_sampled_governance_v53/` (selected by the 2026-10-16 all-refs audit). The branch history is the publication record; Paper08 v48 and all prior Paper07 editions remain preserved.

## Lineage and scope

Paper07 v53 is a standalone continuation of v52. The main source is assembled from `parts/`; the recovered/reconstructed supplementary document is assembled from `si_parts/`. Earlier editions and the parallel Paper08 v48 are preserved. The repository release is added beside the latest confirmed Paper07 lineage location, not by replacing an earlier edition. The all-ref audit is recorded in `VERSION_AUDIT_2026-10-16.md`; no Paper07-specific tag or release exists, and no earlier version is to be rewritten.

## Material changes in v53

1. **Review-interval interpretation.** The stock screen contains 42 stocks: seven with the proxy review interval \(T_r=0.5\) years and 35 with \(T_r=1\) year. Both proxy values are below the modeled crossing window, so the screen identifies no window-approach gradient. The reproduced band associations run in opposite directions (band A \(\rho=-0.408, p=0.007\); band B \(\rho=-0.340, p=0.028\)); they are explicitly described as proxy-based, confounded, and non-causal. Baseline target-band tests have zero Benjamini–Hochberg discoveries across 84 tests.
2. **Sensitivity provenance.** SI S11 distinguishes the locally rerun ±2% one-at-a-time analysis from the archived ±5%/±10% battery in `src/p7_empirical/recovered/sens_table.csv`. The archived values are labeled as archived and not as a fresh v53 rerun. Main-text Table 2 now allocates more width to its interpretation column.
3. **Supplement reconstruction.** The SI has S-prefixed section, subsection, equation, table, figure, and theorem numbering, a formal finite-horizon Lemma S2.2 with proof, a regenerated case inventory, and a reproducibility register. The widened TOC number fields and the sensitivity table additions are included in the final build.
4. **Numerical verification.** A separate finite-difference audit compares the full nonlinear plant/controller-flow Jacobian with the monodromy calculation. At \(T_r=1\), the relative-step \(3\times10^{-5}\) Jacobian discrepancy is at most \(6.93\times10^{-11}\), and the finite-difference and monodromy radii agree to about \(2.3\times10^{-11}\). At the crossing, the same-step error is about \(1.67\times10^{-9}\). These checks support the local calculation only; they do not establish an invariant circle or nonlinear bifurcation theorem.
5. **Reproducible outputs and limitations.** The 20,001-point joint-box analysis, archived cohort checks, baseline multiplier plot, and generated supplementary tables are retained. The complete screen-battery rerun timed out; its restored log is archived output, not a new completed run. The complete power-grid driver and the archived comparator lack complete rerun/metadata and remain explicitly qualified in the paper.

## Final build record

- Main: `paper07_sampled_governance_v53.pdf`, 14 A4 pages.
- Supplement: `paper07_sampled_governance_v53_SI.pdf`, 29 A4 pages.
- Main was compiled twice after the final source edits; SI was compiled three times to settle cross-references and the S-prefixed TOC.
- The final `.log` files show no overfull boxes, undefined references, label-change warnings, or hyperref warnings.
- Sampled final pages were visually inspected, including main Table 2/Results pages and SI S11 sensitivity/joint-box pages. The archived and rerun sensitivity records are now separately identified, and the generated S11.4 table agrees with the archived CSV.

## Credential handling

The user-supplied GitHub PAT remains in its designated workspace location and is excluded from the bundle and repository publication. It must never be committed or pushed. Do not copy credential files into the paper tree, source bundle, or a Git worktree.
