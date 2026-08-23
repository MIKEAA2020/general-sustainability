# Paper VIII certification protocol (consolidated)

## Certification target

Two different objects must be distinguished:

1. **Collocation fold:** a regular zero of the 387-dimensional Moore--Spence map for the frozen `m=64` nodal collocation system.
2. **Continuous-DDE fold:** a simple saddle-node of periodic orbits of the infinite-dimensional RFDE.

A collocation certificate is not a continuous-DDE certificate.

## Frozen discrete map

Use the existing nodal formulation only:

- `m=64` nodes;
- `U in R^192` for the three state variables;
- `X=(U,T) in R^193`;
- `G(X,tau) in R^193`, including the fixed first-sine phase condition;
- Moore--Spence state `Z=(X,v,tau) in R^387`.

The phase condition and the nodal/spectral delay convention must not change during certification.

## Discrete certification sequence

### 1. Base Jacobian validation

Validate the analytic `D_X G` against central finite differences, separately checking:

- state columns;
- period column;
- delay column;
- phase row.

The current base collocation Jacobian has passed this numerical check at approximately `1e-10` after correcting the omitted spectral derivative term. This is not a proof.

### 2. Floating-point Moore--Spence candidate

Solve

```text
G(X,tau) = 0
D_X G(X,tau) v = 0
ell^T v - 1 = 0
```

using a scaled/block Newton or robust bordered solve. Do not invert `D_X G` alone. Do not accept a candidate solely because the collocation residual is small.

Record:

- `||G||`;
- `||D_X G v||`;
- `|ell^T v-1|`;
- smallest singular value of `D_X G`;
- left nullvector residual;
- floating-point transversality and curvature quantities.

If no candidate converges, stop. No interval calculation is justified.

### 3. Floating-point fold nondegeneracy

With left nullvector `w`, evaluate

```text
a = w^T G_tau
b = w^T D^2_XX G[v,v]
```

after fixing state, parameter, and nullvector scaling. Do not use universal thresholds such as `1e-4`; only a later interval exclusion `0 notin [a]` and `0 notin [b]` is a certificate.

### 4. Outward-rounded interval infrastructure

The implementation must provide validated enclosures for:

- `G`;
- `D_X G`;
- `G_tau`;
- `D^2_X G[v,v]`;
- the full 387-dimensional Moore--Spence derivative.

`mpmath.iv` may be used for prototyping, but package compliance and directed rounding must be verified. Naive interval FFT matrices are likely to suffer severe wrapping; use validated real trigonometric matrices or a rigorously controlled block representation.

Before a 387-dimensional run, validate the interval stack on the one-dimensional Hopf cubic and its known simple root.

### 5. Krawczyk inclusion

For a box `[Z]` about a converged Moore--Spence candidate and a float preconditioner `Y`, compute

```text
K([Z]) = Z0 - Y F(Z0) + (I - Y [D F]([Z]))([Z]-Z0).
```

The inclusion

```text
K([Z]) subset int([Z])
```

is the proof. Residuals, condition numbers, and singular values are diagnostics only.

If inclusion succeeds, it certifies a unique zero of the discrete Moore--Spence map and hence a unique fold of the `m=64` collocation system. It does not certify the continuous RFDE.

### 6. Interval nondegeneracy

On the same validated box, enclose the left nullvector and evaluate interval versions of `a` and `b`. Require

```text
0 notin [a],   0 notin [b].
```

## Continuous-DDE lift

Only after the discrete certificate succeeds should a continuous lift be attempted.

Use one weighted Fourier Banach space, for example `ell^1_nu`, and formulate the **full bordered infinite-dimensional Moore--Spence map**. The tail of `f(U,S U)` does not vanish merely because `U` has finite Fourier support: softplus, rational terms, and gated products generate infinitely many modes.

A continuous radii-polynomial proof must bound:

- the orbit defect;
- the infinite Fourier tail;
- the bordered nullvector equation;
- the period and delay derivatives;
- the nonlinear second derivative;
- the infinite-dimensional transversality and curvature quantities.

A periodic-orbit radii polynomial without the bordered fold equations is insufficient.

## Current status

- Pseudo-arclength locator: available.
- Base collocation Jacobian: numerically cross-validated.
- Moore--Spence zero: not obtained.
- Interval Krawczyk: not started.
- Continuous-DDE radii polynomial: not implemented.

The current scientifically valid statement is therefore:

> Pseudo-arclength continuation locates a turning region of the discrete collocation branch. No formal fold certificate has yet been obtained for either the collocation system or the continuous DDE.
