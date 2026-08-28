# B4 Continuum Transfer — The Execution Record (Stages T2, T4, T5)

## Status

**EXECUTED (2026-08-28).** The product bunching inequality of the two-block
periodic-NAIM scaffold closes at both transfer horizons:

\[
q_{35} = M_c \max\{\|S_x^{35}\|,\ \|T_y(35P)\|\} \le 0.4127 < 1,
\qquad
q_{40} \le 0.1555 < \tfrac14 ,
\]

with each channel certified at its stated level: the slack channel at the
**continuum level in outward-rounded interval arithmetic** (Stage T3, its own
record `b4_t3_slack_semigroup_certificate.md`), the binding channel at the
**collocation level in the Stage-4b affine noise-symbol arithmetic** (Stage
T2, below), and the prefactor at a certified 0.80% excess over the committed
discrete value (Stage T4). The \(q_{40} < 1/4\) target is the generic
two-block persistence theorem's own quantitative application requirement.

Runners (all deterministic, all checks pass):
`validated_computations/a021_c4/b4_t2_binding_product_certificate.py`,
`.../b4_t4_prefactor_certificate.py`, `.../b4_t5_assembly_certificate.py`;
artifacts `b4_t2_binding_product_certificate.json`,
`b4_t4_prefactor_certificate.json`, `b4_t5_assembly_certificate.json`.

## Stage T2 — the binding-block stable-complement product certificate

**The object.** The deflated n-period evolution of the collocation system's
monodromy: \(S_x^n = (\mathrm{Mon}\,D)^n\) with \(D = I - tt^{\mathsf T}\)
the deflation onto the orthogonal complement of the certified tangent
(\(\|\mathrm{Mon}\,t - t\|/\|t\| = 3.35\times10^{-8}\), the committed 4a/4b
tangent). The input deflation is applied at every period boundary — the
graph-transform reading of the stable-complement evolution (each period: the
phase component of the input is removed, then the one-period map acts). This
realizes, in the tangent-orthogonal chart, the same object the committed
discrete evidence realizes through the spectral projector
(\(S = M - \lambda P\); its committed powers are reproduced to 5 digits as
the cross-reference table in the artifact).

**The certificate.** In the 4b affine noise-symbol arithmetic at point-tight
stage-matrix widths (the eval-pass semantics — the operator at the fixed
point, no tube): the march of the deflated columns for 40 periods, with the
block-wrapped magnitude accumulation (the committed 500-step blocks; the
\(1.00264^{500}\) in-block pessimism paid once per block), the signed
propagation of all columns within each period, and — at each period boundary —
the signed deflation of the accumulated noise zonotope followed by the
collapse into per-coordinate extents (the 4b block-wrap pattern at period
granularity). The certificate at period \(p\):

\[
\|S_x^p\|_{\mathrm{int}} \;\le\; \max_r\Bigl(\sum_k |(\mathrm{Mon}D)^p_{rk}|
+ \mathrm{ext}_p[r]\Bigr),
\]

the float center's row sums plus the noise extents for unit-ball inputs.

**The certified numbers.**

| \(p\) | center \(\max_r\sum_k|(\mathrm{Mon}D)^p_{rk}|\) | noise ext sup | certified \(\|S_x^p\|_{\mathrm{int}}\) |
|---:|---:|---:|---:|
| 1 | 2.5505e+02 | 4.820e-03 | 2.5506e+02 |
| 10 | 7.7993e+00 | 3.198e-02 | 7.8313e+00 |
| 20 | 1.8471e-01 | 1.615e-02 | 2.0085e-01 |
| 35 | 6.7205e-04 | 5.220e-03 | **5.8923e-03** |
| 40 | 1.0337e-04 | 3.579e-03 | **3.6820e-03** |

Verification: the float part matches the direct matrix products
\((\mathrm{Mon}D)^p\) to \(10^{-11}\) at every checkpoint period; the
one-period noise extent \(4.820\times10^{-3}\) reproduces the committed
Stage-4b eval-march value \(T_{\mathrm{unc},0} = 4.8200\times10^{-3}\)
exactly; the monodromy reproduces the committed 4b top eigenvalues; the
tangent residual is the committed \(3.35\times10^{-8}\).

**Honesty.** The certificate covers the collocation system's stable-complement
product with its interval evaluation uncertainty. This closes, in interval
arithmetic, the first unsoundness channel of the committed discrete evidence
(the discretized binding projections). The **operator-level continuum lift**
— the true DDE's variational monodromy along the certified orbit vs the
collocation monodromy — is *not* enclosed: the committed Stage-4d certificate
lifts the *solution* (\(3\times10^{-7}\)), not the variational operator. The
specification's T1 (the one-period continuum variational certificate) is
therefore discharged at the collocation level only, and the assembly's
binding channel carries exactly that level.

An executed negative diagnostic is recorded for transparency: a first
implementation collapsed the noise zonotope at every *block* boundary; the
per-block \(|\cdot|\) pessimism compounded at a measured \(610\times\) per
period (the block-level \(|\mathrm{Mon}_{\mathrm{block}}|\) radius
\(1.49\) per 500-step block, 16 blocks per period). The committed design —
signed propagation within the period, collapse at period boundaries only —
was verified against the measured rates \(\rho(|\mathrm{Mon}|) = 1.036\),
\(\rho(|D\,\mathrm{Mon}|) = 0.923\) (the 364-dimensional committed Floquet
discretization; the collapse rate governs the carried noise and is
contracting), and the observed noise extents decay from \(3.4\times10^{-2}\)
(period 5) to \(3.6\times10^{-3}\) (period 40).

## Stage T4 — the prefactor certificate

**The object.** \(M_c\), the phase-tangent history ratio: for each orbit
phase \(t_i\), \(h_i = \sup_{s\in[t_i-4.5,\,t_i]}\|F(y^*(s), Z^*(s-4.5))\|\)
(the sup-norm of the tangent history), and \(M_c = \max_i h_i/\min_i h_i\).

**The certificate.** The committed K=80 Fourier substrate (the same source
all A1 stages consume) evaluated on a 65536-point grid; the delayed reads
evaluated exactly through the phase-shifted coefficients (no interpolation);
the tangent speeds enclosed by the additive budget
\(\rho = 3\times10^{-7}\) (the 4d tube) \(+\ 3\times10^{-7}v_{\max}\) (the
phase drift) \(+\ 10^{-11}\) (evaluation noise), propagated through the
right-hand side's measured Lipschitz constants (\(\|J\|_\infty \le 7.17\),
\(|D_{43}| \le 1.785\)), plus the between-sample variation bound
\(|ds/dt|\,\Delta t/2\) with \(\|ds/dt\| \le \|J\|v_{\max} + |D_{43}|v^Z_{\max}\).

**The certified number.** \(M_c \le 4.590009620\) — 0.80% above the committed
discrete value 4.553557132612546, far inside the specification's 10% budget.
Only the upper bound enters the assembly.

## Stage T5 — the assembly

\[
\begin{aligned}
q_{35} &= 4.590009620 \times \max\{5.8923\times10^{-3},\ 8.9916\times10^{-2}\}
= 0.41272 < 1 \quad(\text{2.42}\times\ \text{margin}),\\
q_{40} &= 4.590009620 \times \max\{3.6820\times10^{-3},\ 3.3885\times10^{-2}\}
= 0.15553 < \tfrac14 \quad(\text{1.61}\times\ \text{margin}).
\end{aligned}
\]

The slack channel dominates at both horizons (factors 15.3 and 9.2 over the
binding channel) — the transfer's risk concentrator, as the specification
identified, is now its most strongly certified channel.

**The theorem's remaining hypotheses, at their exact status:**

- **H1** (regularity/localization): the certified orbit's solution-level
  smoothness is the Stage-4d certificate; the perturbation class is the
  declared generic one (\(\|R_\varepsilon\|_{C^1}\le C|\varepsilon|\)); the
  concrete A021 coupling \(G, f, g\) awaits the author decision (register
  A2).
- **H2** (split tubular coordinates): not separately certified; the T2
  deflation realizes the normal evolution in the tangent-orthogonal
  complement of the certified tangent; the \(C^1\) stable bundle and the
  tubular chart at the certified radius remain a construction route.
- **The binding channel's operator-level continuum lift**: open (see T2's
  honesty statement).

## Register consequences

- **B4 (product bunching)**: the two-block scaffold's inequality CLOSES at
  both horizons with the channel levels as stated. The full
  COMPUTED (continuum) promotion additionally requires the binding channel's
  operator-level continuum lift; until then the row's honest status is the
  executed partial: slack continuum-level certified, binding
  collocation-level certified, assembly closed under the stated levels.
- **Paper 4 capstone** (Part III, NAIM persistence support): NOT promoted —
  the paper-claim-level match, the H2 chart, and the coupling declaration
  remain.
- **Paper 6 gate** (A021 continuum periodic-NAIM): substantially advanced,
  not passed — the persistence statement additionally requires H2 and the
  coupling.

## What this record does not claim

No theorem status is promoted; no registered obligation is discharged; the
certified object is the two-block scaffold's bunching inputs, not the coupled
system's persistence; the A2 coupling class remains declared, awaiting the
author decision.
