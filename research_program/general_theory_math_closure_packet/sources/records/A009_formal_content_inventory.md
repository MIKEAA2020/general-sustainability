# Article 009 Formal-Content and Data Inventory

**Source:** `uploads/paper3_rev2.md`

## Adaptive-capacity vector

\[
a_i=(a_{i,1},a_{i,2},a_{i,3},a_{i,4}).
\]

Only the income/consumption coordinate has a named data source. Other coordinates and floors are not operationalized.

## Exact safe set

\[
K=\{a:a_k\ge a_{floor,k}\ \forall k\}.
\]

## Proposed KS function

\[
h_{dist}(a)
=-\frac1\rho
\log\sum_k
\exp(\rho(a_{floor,k}-a_k)).
\]

Status: dimensionally invalid with heterogeneous units; finite-\(\rho\) nonnegative condition is sufficient but not necessary after normalization.

## Correct normalized soft minimum

\[
m_k=(a_k-a_{floor,k})/s_k,
\]

\[
h_\rho(m)
=-\frac1\rho\log\sum_ke^{-\rho m_k},
\]

\[
\min_km_k-\frac{\log n}{\rho}
\le h_\rho
\le\min_km_k.
\]

## Proposed regional criterion

\[
H_{region}(t)
=
\inf_{i\in D1(t)}h_{dist}(a_i(t)).
\]

Status: not smooth after population infimum; complete individual data unavailable.

## Proposed pooled-decile formula

\[
P_{global}^{D1}
=
\sum_r(P_r/P_{total})F_r^{D1}.
\]

Status: incorrect for the global bottom decile.

## Correct mixture construction

\[
F_{global}(y)=\sum_rw_rF_r(y),
\qquad
q_{0.1}=F_{global}^{-1}(0.1).
\]

## Proposed cohort tensor

\[
T_{t,t+1}(j,j')
=\Pr(a_{t+1,j'}\mid a_{t,j}).
\]

The displayed non-decline inequality in the source has inconsistent indices.

## Current poverty line issue

The source uses \$2.15/day in 2017 PPP. The World Bank replaced this in June 2025 with \$3.00/day in 2021 PPP. A historical 2017-PPP analysis may retain \$2.15 only with consistent PPP vintage and explicit labeling.

## Missing reproducibility objects

- PIP query and extraction code;
- country/region coverage and survey years;
- welfare concept and PPP vintage;
- population weights;
- bottom-decile estimator;
- data for biophysical, infrastructure, and agency axes;
- floor provenance;
- uncertainty propagation;
- dynamics and policy model for a true CBF result;
- cohort definition and transition estimator.
