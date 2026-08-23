# ER033 Point Inventory and Mathematical Assessment

## Overall disposition

Retain ER033's continuum-error and no-promotion cautions. Reject its time-scale, discretization, period, branch, floor, and prefactor-consistency analysis because it misreads the implemented computation.

## Valid points

1. Finite-discrete pointwise operator norms are not a continuum RFDE domination proof.
2. Discretization-to-continuum operator errors remain missing.
3. Continuum Floquet projections and full spectral enclosure remain missing.
4. Source-derived `G,f,g` and exact theorem matching remain open.
5. No invariant-manifold theorem promotion is justified.

## Critical errors

1. **Time variable misread.** The labels 30, 35, and 40 are explicitly numbers of binding periods, not years. The actual times are `n P_x`, with `P_x approximately 370.93 yr`.
2. **Period is not missing.** The period is independently phase-corrected to `370.9311778464 yr`, with endpoint mismatch below `4.9e-7` and spectral residual below `6.8e-6`.
3. **Wrong operator identification.** The extrapolated norms `0.209,0.074,0.026` are slack semigroup norms at 30/35/40 binding periods, not binding Floquet factors.
4. **Invalid `M_s(T)` check.** ER033 multiplies those slack norms by `exp(beta_x T)` using the binding exponent and treats `T` as 30/35/40 years. The product rate is controlled by the slack exponent and the actual times are roughly 11,128/12,983/14,837 years. The resulting factor-of-eight claim is meaningless.
5. **Grid conflation.** Binding monodromy grids use `dt=0.25,0.10,0.05`, corresponding to 18,45,90 delay intervals. Slack semigroup extrapolation uses 100,200,400 history intervals. ER033's `h_min=0.05/4.5` paired with 400 intervals mixes the two discretizations.
6. **Branch status resolved.** The selected orbit is independently reproduced as the C4 large-cycle candidate in the lower bistable window `(3.78487,about 5.63)`. The monostable interval is a different regime.
7. **Floor clearance resolved.** The full floor argument has minimum about `0.00147554` on the selected C4 orbit.
8. **Passport resolved.** State ranges and direct period are recorded.
9. **Publication remark obsolete.** Corrected A021 already reports periods as binding-period multiples and labels finite-discrete operator norms caveatedly.
10. **Uniform exponential pair nuance.** Point samples alone do not prove a uniform pair, but variation among `||T(nP)||exp(beta nP)` is not a contradiction; semigroup transients and using a nonsharp beta naturally produce variation. A uniform `M` is a supremum bound, not an equality or constant fitted at each time.

## Controlling status

- finite-discrete product bunching: numerically verified at 35–40 binding periods;
- orbit passport/floor/branch: complete numerically;
- validated continuum operator enclosure/projections: open;
- source-derived coupling and exact theorem: open;
- no new manuscript change.