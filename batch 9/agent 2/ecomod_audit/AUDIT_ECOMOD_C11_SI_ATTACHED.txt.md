# Audit of ECOMOD continued 11 — Supplementary Information

**Audited file:** `ecomod_continued_11_revision_draft_20261028_SI.txt` (576 lines; LaTeX source).  
**Companion main paper:** `ecomod_continued_11_revision_draft_20261028 (1).pdf`, audited separately in [`AUDIT_ECOMOD_C11_ATTACHED_PDF.md`](AUDIT_ECOMOD_C11_ATTACHED_PDF.md).  
**Audit date:** 2026-10-28.  
**Scope:** SI equations and proofs, internal consistency with the companion PDF, reported tables/text, empirical-method transparency, and submission reproducibility. No SI figures, the referenced `si_drawdown_depth.csv`, source package, or simulator were attached with this SI text. I did not compile the SI or independently rerun the numerical experiments.

## Overall assessment

**The SI resolves several important C10-era mathematical problems, but still needs a focused correction and a complete reproducibility package.** It now gives a precise projected delayed-quality law, explicitly disavows transfer of the raw unconstrained DDE's characteristic roots, corrects the debt row of the Jacobian, scopes the population-delay statement to the actual equation, distinguishes the equality locus from surplus equilibria, and supplies the previously inconsistent recovery endpoint. Those are substantial improvements.

Three substantive issues remain in the SI itself:

1. the finite-time debt bound drops the initial debt when translating it into a bound on the yield-loss channel;
2. the additive-degradation aside reuses a coefficient with the wrong units, both in the SI and the companion main paper; and
3. the claim that a control using only total biocapacity cannot guarantee the capital-area floor is too strong without restrictions on the controller (a blanket no-conversion rule is a counterexample).

The SI also repeats the S8 experiment-opening paragraph verbatim, and its empirical “regeneration anchors” remain insufficiently reproducible from the material supplied. These issues do not negate the valid account identities or the main conditional masking example.

**Recommendation:** correct the mathematical statements, narrow the control claim, provide the selected run/data/fit artefacts and figure assets, and then re-check the source against the main-paper PDF.

## 1. Findings requiring correction

### 1.1 Finite-time debt bound omits initial debt — Medium

**Location:** SI §S2.5, “Boundedness asymmetry and the crossover shortfall”; compare main-paper Proposition 3(ii).

From \(\dot D=S-\eta D\), with \(0\le S(t)\le\bar S\) over the interval and \(D(0)\ge0\), the standard comparison bound is

\[
D(t)\le \max\{D(0),\bar S/\eta\}.
\]

The SI states this bound, but then says the debt channel in \(\ln b_f=\ln(b_{f0}+T_b)-\alpha D\) “contributes no less than \(-\alpha\bar S/\eta\).” That conclusion does not follow when \(D(0)>\bar S/\eta\); in that case the bound is \(-\alpha D(0)\). The manuscript's displayed threshold \(\bar S=S^\dagger\) also equates the technology ceiling to the bound obtained from a running shortfall supremum, not necessarily to the realised debt loss at a finite time. Even for \(D(0)=0\), the comparison inequality is generally an upper bound on debt, not an equality throughout the run.

**Repair:** carry \(D(0)\) into the finite-time loss bound:

\[
-\alpha D(t)\ge-\alpha\max\{D(0),\bar S/\eta\}.
\]

Call \(S^\dagger\) a *sufficient worst-case bound crossover* under the stated initial-debt condition (or include the initial-debt term in the threshold). Reserve equality of realised channels for the separate limiting case where a constant shortfall \(S^*\) is sustained and \(D\to S^*/\eta\).

### 1.2 Additive degradation remains dimensionally inconsistent — Medium

**Location:** SI §S2.5; also main-paper PDF p. 19.

For the selected multiplicative law, \(\alpha\) has units (gha·yr)\(^{-1}\), and \(D\) has units gha·yr, so \(\alpha D\) is dimensionless. In the aside, the SI writes

\[
b_f=b_{f0}+T_b-\alpha D
\]

and compares \(\Delta b\) with \(\alpha D^*\). But \(b_{f0},T_b,\Delta b\) have units gha·ha\(^{-1}\), whereas \(\alpha D\) is dimensionless. The same coefficient cannot be subtracted from yield or compared with a yield increment. This is not repaired by describing the quantities as “bounded increments.”

**Repair:** remove the aside, or define a different additive coefficient (with units of yield divided by debt units) and derive the comparison for that alternative law from scratch. Make the same change in the main manuscript so the two documents agree.

### 1.3 Output-only control impossibility claim is not established — Medium

**Location:** SI §S6, “Typed floors and conversion stop.”

The SI says: “A control based only on total \(B\) cannot guarantee this typed floor because \(B\) does not identify \(A_c\).” Non-identification is established, but it does not imply that every output-only controller fails to preserve the floor. A controller that sets \(u_c\equiv0\) (a constant function of any observation, including \(B\)) guarantees \(\dot A_c=R_{rc}\ge0\) from an initially admissible state. The specified conversion law itself also slows as \(A_c\) approaches \(A_c^{\min}\), preserving that floor under the stated nonnegative restoration rule.

**Repair:** state the defensible conclusion: \(B\) alone cannot reconstruct \(A_c\) or implement a desired \(A_c\)-dependent intervention. Any stronger impossibility claim must define the permitted controller class, initial-information set, and a nontrivial performance requirement that excludes blanket conversion shutdown.

### 1.4 Regeneration-anchor statistics remain difficult to reproduce — Medium

**Location:** SI §S5.5, “Regeneration anchors.”

The SI reports 2ndFOR results from 1,334 plots/41 chronosequences/35 “good fits” (median \(t_{50}\approx30\) yr and \(\tau_r\approx38\) yr under a “lagged saturating recovery model”), and a separate summary for 33 collapsed fish stocks (\(t_{50}\approx5.6\) yr and \(\tau_r\approx3.4\) yr). It appropriately says these heterogeneous records are not pooled, do not calibrate \(\rho_c\) or \(\tau_g\), and do not validate the model. But it does not give the recovery-fit equation, inclusion/exclusion criteria for “good fits,” exact records or data files, fitting method, censoring/failed-recovery treatment, uncertainty, or analysis code. The cited papers alone do not reproduce the new fitted medians.

**Repair:** include the fit definitions, record-selection rules, underlying data or durable identifiers, code, uncertainty/sensitivity analysis, and treatment of unrecovered trajectories. If this analysis is only intended as context and cannot be documented, remove the novel fitted summaries and retain directly sourced published results with careful wording. Keep the existing non-calibration caveat.

## 2. Editorial and package issues

### 2.1 Exact duplicate paragraph in the technology-wave section — Minor

**Location:** SI §S8, opening paragraph.

The paragraph beginning “The matched experiment compares endogenous-demand runs with the technology increment \(T_b\) switched on or off…” is duplicated verbatim immediately afterward. Delete one copy.

### 2.2 Figure and data artefacts are not included with the supplied SI source

The SI uses `\includegraphics` for comparator and technology-wave figures, and refers to `si_drawdown_depth.csv` for the full initial-population grid. These assets were not among the supplied files, so I could not compile or visually inspect the SI, check the plots against their captions, or reproduce the full grid. The main-paper audit likewise noted the prospective data/code statement (“will be deposited”).

**Action:** provide the exact figure files, CSV, simulator and data-processing code, and a version identifier that pairs this SI with the main PDF. Replace the future-tense deposit statement with a working archive/repository release before submission.

## 3. Checks that pass / improvements since the prior audit

- **Bounded delayed-quality model:** the SI defines the projected law and admissible continuous history; proves monotonicity and convergence to \(q_{\max}\) for \(q(0)>0\); identifies the all-zero history as an exception; and correctly declines to apply raw-DDE characteristic roots at the projected boundary.
- **Population delay:** it correctly observes that \(\tau_p\) delays carrying capacity, not the population's own crowding term. The constant-capacity mode is the ordinary logistic mode, and the former Hutchinson-style \(r\tau_p\) criterion is explicitly rejected.
- **Debt Jacobian:** the deficit-face row includes \(\partial\dot D/\partial D=\alpha b_fA_f-\eta\), and is clearly limited to the smooth interior of that active face.
- **Reduced land branch:** the affine matrix, trace/determinant and eigenvalue scope are stated for the deficit-active fixed-quality/frozen-debt branch. The text now notes the distinct full endogenous-population equality equilibria and surplus family rather than treating the equality point as the sole equilibrium.
- **Recovery values:** the SI table gives \(A_c(T)=0.677\) ha and \(\mathcal R_c=0.46\) for the \(P_0=2\) run at \(T=400\) yr, matching the paired main-paper summary and resolving the large C10 main/SI discrepancy at the level of the reported figures.
- **Technology-wave protocol:** it discloses the nonzero logistic tail at \(t=0\), distinct current \(B(0)\) and common no-wave prehistory, and the difference between all-time and post-midpoint debt maxima. Step-halving results are reported, and the interpretation remains conditional.
- **Empirical account analysis:** the SI states source vintage, endpoint handling, population conversion, proxy construction, and the account/physical-stock distinction in enough detail to make the accounting logic inspectable. The reported NFA values agree with the prior independent check of the same edition recorded in `AUDIT_ECOMOD_C10.md`. The proxy residual is explicitly not identified with modelled capital contribution or physical capital.
- **Cross-paper pointers:** this SI includes versioned GitHub links for the cited governance v41 and assessment v71 manuscripts. The cited theorem numbering is consistent with the v71 companion found in the repository: Theorem 2 (witnessed separation) and Theorem 4(iii) (substitutability ladder).

## 4. Bottom line

This SI is substantially more coherent than the earlier C10 supplement: several central mathematical corrections are now explicit, and the recovery result matches the revised main text. The remaining finite-time debt-bound omission, dimensionally invalid additive-law aside, and overbroad controller-impossibility sentence are concrete and readily fixable. The empirical regeneration fits and simulation figures still need a versioned evidence package. Correct those points and remove the duplicate paragraph before treating the SI as independently reproducible or submission-ready.
