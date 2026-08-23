# Article 005 Formal-Content Inventory

**Source:** `uploads/Paper_III_Groundwater_Module.txt`

## Continuous state

\[
Z=(H_f,H_s,M_q,\sigma_{\rm sal},\chi).
\]

The component \(\chi\) is undefined in the source.

## Constitutive storage

\[
A_i=\mathcal A_i(H_i),
\qquad
C_i(H_i)=\frac{d\mathcal A_i}{dH_i}>0,
\quad i\in\{f,s\}.
\]

## Prescribed and implemented controls

\[
a_k\in\Gamma(B_k,h_k),
\]

\[
U_k=(q_{p,f,k},q_{p,s,k},q_{r,k},q_{{\rm rel},k})
\in\mathcal E(B_k,h_k,a_k).
\]

The release control \(q_{\rm rel}\) is not routed in the displayed balances.

## Cross-formational leakage

\[
\ell_{fs}=\kappa_{fs}(H_f-H_s),
\]

\[
\ell_{f\to s}=[\ell_{fs}]_+\psi_f(A_f),
\qquad
\ell_{s\to f}=[-\ell_{fs}]_+\psi_s(A_s),
\]

\[
\ell^{\rm net}_{fs}=\ell_{f\to s}-\ell_{s\to f}.
\]

## Head-based water balances

\[
C_f(H_f)\dot H_f
=R_{\rm nat}+q_r-q_{p,f}-\ell^{\rm net}_{fs}-L_f+J_f,
\]

\[
C_s(H_s)\dot H_s
=\ell^{\rm net}_{fs}-q_{p,s}-L_s+J_s.
\]

## Derived total storage balance

Not displayed in the source but implied:

\[
\frac{d}{dt}(A_f+A_s)
=R_{\rm nat}+q_r-q_{p,f}-q_{p,s}-L_f-L_s+J_f+J_s.
\]

## Generic solute balance

\[
\dot M_q
=I_q-O_q(X,U,\omega)+\mathcal R_q(X,U,\omega).
\]

A two-formation concentration model may require separate masses \(M_{q,f}\) and \(M_{q,s}\).

## Safety set

\[
\mathcal C_Z(\lambda)
=\{Z:
H_f\ge H_f^{\min},
H_s\ge H_s^{\min},
M_q\le M_q^{\max},
\sigma_{\rm sal}\le\sigma_{\max},
\chi\in\mathcal X_\chi\}.
\]

## Ecological-flow action relation

\[
\mathcal A(Z,\omega;\lambda)
=\{U:Q_{\rm eco}(Z,U,\omega)
\ge Q_{\rm eco}^{\min}(\lambda)\}.
\]

The symbol \(\mathcal A\) conflicts with the storage function and master architecture notation.

## Observation and compatible state

\[
Y_k=\mathcal O(Z_{[t_{k-1},t_k]})+\varepsilon_k,
\]

\[
B_k\subseteq C([t_{k-1}-\tau,t_k],\mathcal Z)\times\Theta.
\]

## Structural discrepancy

\[
\dot Z
=F_{\rm gw}(Z,U,\omega,\vartheta)+\delta_t,
\qquad
\delta_t\in\mathcal D_t.
\]

## Competing hypotheses

Physical:

- H0: one-pool storage;
- H1: fast/slow two-pool storage with bidirectional leakage;
- H2: distributed or higher-dimensional groundwater model.

Institutional:

- scarcity-amplifying extraction;
- protective restraint/restoration;
- inertia/capture/state-dependent action.

## Unverified components

No named basin, data, parameter values, thresholds, constitutive recharge/leakage/solute functions, observation likelihood, policy class, model comparison, kernel, numerical result, or empirical result is supplied.
