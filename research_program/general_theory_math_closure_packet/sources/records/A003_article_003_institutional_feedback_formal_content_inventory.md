# Article 003 Formal-Content Inventory

**Source:** `uploads/Paper_V_Institutional_Feedback_and_Nonlinear_Transitions.txt`

## Equations

1. Standing-stock equation:
   \[
   \dot N=R(N,A,\ldots)-qEN.
   \]
2. Perceived scarcity/deficit filter:
   \[
   \dot Z=\tau_m^{-1}[D(N,E,A,\ldots)-Z].
   \]
3. Institutional/effort response:
   \[
   \dot E=\mathcal G_\gamma(E,Z(t-\tau_I),h).
   \]
4. Sampled observation and prescription:
   \[
   Y_k=\mathcal O(X_{[t_{k-1},t_k]})+\varepsilon_k,
   \qquad
   a_{k+1}=\Pi_\gamma(Y_k,h_k,\rho_k).
   \]
5. Implemented control correspondence:
   \[
   U_{k+1}\in\mathcal E(B_k,h_k,a_{k+1}).
   \]
6. Safety-distance diagnostics:
   \[
   \operatorname{dist}(\mathcal A_\mu,\mathcal C_X^c),
   \qquad
   \operatorname{dist}(\mathcal R_{[0,T]},\mathcal C_X^c).
   \]

## Policy hypotheses

- H1: scarcity-amplifying extraction;
- H2: protective restraint/restoration;
- H3: inertia, capture, or state-dependent response.

## Physical mechanism types

- standing-stock culling;
- recruitment suppression;
- weak viability coupling.

## Formal conjecture

**Structured persistence.** A nonlinear transition verified in a reduced hybrid/RFDE model may persist under small physically admissible coupling only after well-posedness, suitable contractivity where applicable, spectral separation, center-manifold reduction, transverse Poincaré-map conditions, and preservation of positivity and safety are established.

## Numerical programme objects

- ungated variant;
- gated variant;
- hybrid-effort variant;
- four-state support-pool variant;
- two-channel liquidation variant;
- stage-structured variant;
- sampled-review variant;
- thermodynamic-tether variant;
- unified-core variant.

No equations, parameter files, code, or outputs for these archived variants were included in the submitted source.
