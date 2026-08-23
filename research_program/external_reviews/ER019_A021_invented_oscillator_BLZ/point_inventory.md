# ER019 Point Inventory — Joint Assessment with ER018

## Overall disposition

Reject ER019’s concrete-model and theorem-promotion claims. ER018 correctly says the actual A021 equations are absent and must not be fabricated. ER019 then invents a new two-dimensional oscillator unrelated to the recorded four-state A021 companion blocks, and even that invented oscillator does not possess the periodic orbit claimed under its stated parameters. It cannot close any concrete A021 verification action.

## Fatal model-identity defect

The A021 record describes binding blocks inherited from companion dynamics, with possible states `(N,A,Z,E)`. ER019 supplies a new two-state radial normal-form oscillator with arbitrary parameters. No derivation, reduction, parameter map, or user authorization identifies this oscillator with an actual A021 block. Calling it “the concrete A021 binding block” is fabrication. At most it could be a separate illustrative example after explicit authorization and relabeling.

## Fatal algebraic defect in the claimed periodic orbit

With `a=0`, ER019’s equations give, in polar coordinates,

\[
\dot r=r\bigl(r_0^2-d-r^2\bigr),\qquad \dot\theta=\omega_0.
\]

Because ER019 assumes `d>0`, the circle `r=r_0` is not invariant:

\[
\dot r\big|_{r=r_0}=-d r_0\ne0.
\]

A positive nonzero cycle exists only if `r_0^2>d`, at radius

\[
R=\sqrt{r_0^2-d},
\]

and its radial variational exponent is `-2R^2=-2(r_0^2-d)`, not `-2r_0^2`. Thus the displayed solution, history manifold, Floquet multiplier, `beta_x`, and every downstream domination calculation are wrong as stated.

## History-space splitting defects

1. The proposed pointwise/L2 orthogonality description of `N_{gamma_theta}A_x` is not shown to be a closed invariant complement in the supremum-norm history space.
2. For `a=0`, the equation is an ODE represented on an RFDE history space. Initial-history directions away from the value at zero are shifted out and eventually forgotten, but “the infinite-dimensional delay tail contracts completely to zero for `t>=tau`” is not a proof of a `C^{k-1}` invariant normal bundle or a uniform exponential estimate with the stated rate.
3. A valid complement and projections would need the exact variational solution operator/Floquet spectral projection in `X`, including the finite-time shift component and transient prefactor.

## Missing concrete data despite checked boxes

1. The slack functional `G`, equilibrium, characteristic matrix, `beta_y`, and semigroup prefactor remain unspecified and merely assumed.
2. Couplings `f,g`, their `Ck` norms, the localized tube, and common trajectory enclosure remain unspecified.
3. `M_x`, `M_y`, and hence `M_s` are not computed.
4. No concrete perturbation threshold `epsilon_0` or localization is derived.
5. `Ck O(epsilon)` closeness of time maps and persistent embeddings is asserted without higher variational estimates or an exact theorem conclusion.

## Citation and theorem-match defects

1. The BLZ citation again conflicts with the verified bibliography. The title used belongs to the 1998 Memoirs AMS monograph, not the asserted 1999 TAMS entry.
2. Theorems 2.1 and 3.1 were not checked from a source in this audit.
3. The exact smoothness, perturbation topology, uniqueness, boundary, local-invariance, attraction, stable-foliation, and asymptotic-phase conclusions are not reproduced.
4. A theorem giving a nearby invariant embedding does not automatically give the claimed global basin or unique asymptotic phase in the stated form.

## Joint comparison with ER018

- **Accepted from ER018:** missing model data block concrete verification; equilibrium and periodic orbit are only templates; exact prefactor inequalities and full spectra are required; no fabrication.
- **Rejected from ER018:** universal nonsingleton history-cube noncompactness, blanket mapping-space obstruction, mixed-dimension finite-union wording, and unverified BLZ citation.
- **Rejected from ER019:** invented A021 identity, incorrect periodic orbit and rates, unsupported normal splitting, assumed slack/coupling data, false checked-box completion, and theorem promotion.

## Effect on implemented manuscript and open actions

The implemented A021 manuscript already states the correct outcome: the concrete compact NAIM, domination data, and exact theorem match remain open. No manuscript change follows from ER018–ER019. The three open verification actions remain blocked pending actual A021 equations and source data.