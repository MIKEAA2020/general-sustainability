# Article 004 Formal-Content Inventory

**Source:** `uploads/Paper_IV_Phosphorus_Agriculture_Module.txt`

## Scale modules

1. Extraction and processing layer
2. Regional fertilizer/agriculture/consumption/recovery layer
3. Catchment soil/erosion/receiving-water/ecological-function layer

## Material state

\[
r_P=(P_{\rm reserve},P_{\rm process},P_{\rm fertilizer},P_{\rm soil,labile},P_{\rm soil,stable},P_{\rm crop},P_{\rm livestock},P_{\rm food/product},P_{\rm waste},P_{\rm recovery},P_{\rm river/lake},\ldots)^\top.
\]

## Continuous material equation

\[
\dot r_P
=
\mathsf S_P\nu_P(X_t,U,\omega,\vartheta)
+b_P(X_t,U,\omega,t),
\qquad
\ell_P^\top\mathsf S_P=0.
\]

## Functional states

\[
f_P=(f_{\rm soil},f_{\rm aquatic},f_{\rm habitat},\chi).
\]

The component \(\chi\) is undefined in the source and requires correction.

## Service map

\[
s=\mathcal F_P(r_P,f_P,U,\omega,\vartheta).
\]

## Safety set

\[
\mathcal C_P(\lambda)
=
\{(r_P,f_P):
P_{\rm soil,labile}\ge P_{\rm soil}^{\min},
\ f_{\rm soil}\ge f_{\rm soil}^{\min},
\ f_{\rm aquatic}\ge f_{\rm aquatic}^{\min},
\ P_{\rm river/lake}\le P_{\rm water}^{\max},\ldots\}.
\]

## Admissible action relation

\[
\mathcal A_P(X,\omega;\lambda)
=
\{U:s(X,U,\omega)\ge s^{\min}(\lambda),
\ R(X,U)\in\mathcal R_{\rm adm}(\lambda)\}.
\]

The symbol \(R\) is overloaded and should be replaced by a rights/burden operator.

## Observation model

\[
Y_k
=
\mathcal O_P(X_{[t_{k-1},t_k]})
+
\varepsilon_k.
\]

## Compatible-state set

\[
B_k
\subseteq
C([t_{k-1}-\tau,t_k],\mathcal X_P)
\times\Theta.
\]

## Competing model set

- H0: aggregate regional phosphorus balance
- H1: multi-compartment regional/catchment model
- H2: spatial trade-network/catchment model

## Unverified components

No explicit constitutive flux laws, parameter values, trade matrices, erosion functions, observation likelihoods, thresholds, institutional transition laws, data, numerical results, theorems, or empirical tests are supplied in the source.
