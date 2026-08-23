# Step 3: derivative and equilibrium audit

## Findings

### Frozen-A three-state core

The current Paper I linearisation is internally consistent:

```text
A_N = S'(N*) - qE*
A_E = -qN*
B_N = (qE* - S'(N*))/(2*tau_m) = -A_N/(2*tau_m)
B_E = qN*/(2*tau_m) = -A_E/(2*tau_m)
```

Therefore:

```text
A_E*B_N - A_N*B_E = 0
L(lambda) = B_E*lambda
```

The Paper VI modal cubic and Paper VIII Hopf cubic are consistent with this identity.

### Working four-state core

For the working four-state equations

```text
dot N = R(N,A) - q E N
dot A = -B(N,A) + omega_A*(Aeq,W - A)
B = R + kappa_A*N*s(A)
```

with `s(A)=A/(A+A0)`, the correct derivatives are:

```text
A_N = R_N - qE
A_A = R_A
B_N = R_N + kappa_A*s(A)
B_A = R_A + kappa_A*N*s_A(A)
J_AA = -B_A - omega_A
```

Equivalently, at an exploited rest:

```text
A_N = -r*N*s(A)/K
B_N = s(A)*(r*(1-2*N/K) + kappa_A)
```

The earlier universal spatial drafts used an incorrect expression equivalent to
`B_N = -A_N - kappa_A*s`, which must not be used.

### Working four-state local active-pool block

For a local nondiffusing active pool with lumped `Z,E`, the nonzero physical block is

```text
[ A_N - D*mu_j,  A_A ]
[ -B_N,          J_AA ]
```

Writing `alpha=-A_N>0`, `gamma=-J_AA>0`, and `delta=D*mu_j`, its determinant is

```text
(alpha+delta)*gamma + A_A*B_N.
```

It is Hurwitz under `B_N >= 0`. The recorded Paper I working and QSS rests satisfy this condition under the current parameters.

### Four-state characteristic factorization

The former universal four-state factorization in the spatial drafts is not accepted. The sign relations used for `B_N^(A)` and the claimed cancellation in the delayed minor were inconsistent with the governing derivatives. A full four-state modal factorization requires a fresh determinant derivation from the corrected Jacobian before publication.

### Numerical coefficient discrepancy

Older spatial drafts quoted `C_E` values near `-0.1245` for Candidate A. The current three-state `compute_core.py` gated coefficient is approximately

```text
C_E = -0.059518
```

These values belong to different derivative/variant calculations unless a specific alternative convention is documented. The stale value should not be reused across papers.

## Cross-paper status

- Paper I inner three-state derivatives: consistent.
- Paper II primitive equations: use a different closure; no transfer of working-core derivatives.
- Paper VI final: uses corrected two-state local-A derivatives and does not rely on the invalid four-state factorization.
- Paper VIII: uses the inner three-state derivatives and remains consistent with Paper I.

## Required before any four-state spatial theorem

1. Recompute the full four-state Jacobian from the working equations.
2. Derive the modal determinant directly from that Jacobian.
3. Recompute all stationary-mode signs numerically.
4. Recompute any four-state modal gain expression.
5. Keep the result parameter-specific unless a genuine general proof is supplied.
