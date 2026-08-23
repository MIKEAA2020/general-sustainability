# Shared model registry for the capital-liquidation research program

This registry is the authoritative naming convention for model variants used across Papers I–VIII.

## Core model variants

| ID | Name | State vector | Donor/target closure | Institutional topology | Main role | Status |
|---|---|---|---|---|---|---|
| I-3S | Frozen-A gated inner three-state core | `(N,Z,E)` | Active pool frozen/saturated; logistic `S(N)` | Local or lumped depending on paper | Closed-form equilibrium, Hopf cubic, inner continuation | Local Hopfs certified; global folds numerical/model-specific |
| I-4W | Working four-state core | `(N,Aact,Z,E)` | Large-reservoir/dynamic derived target; `Ageo` frozen or omitted | Usually lumped institutional variables | Quantitative four-state Hopf and working-core thresholds | Hopf numerical; global fold classification open |
| I-4Q | Fixed-target/QSS four-state core | `(N,Aact,Z,E)` | Fixed intrinsic target; detritus slaved | Institutional-failure specialization | Alternative singular limit | Valid singular limit; not the working high-A equilibrium |
| II-FD | Finite-donor primitive natural block | `(N,Aact,Ageo,U)` plus `(Z,E)` when included | Primitive donor-limited fluxes; `Ageo` dynamic; no derived target | As specified in Paper II | Closed finite-donor ledger and rest-point obstruction | No positive-effort interior rest; extraction integrable |
| IV-VEC | Vector Liebig product | Multiple specialized blocks, typically `(Ni,Ai,Zi,Ei)` | Smooth soft minimum; yield-gap reduction when applicable | Mean-field result only unless local hypotheses added | Binding-constraint/vector reduction | Conditional finite-time/modal result; yield parity unreduced |
| V-STAGE | Stage-structured Erlang fishery | `(XA,XJ,Z,E)` | Ricker recruitment; one-box Erlang parameter `g` | Mean-field stage result or separate local extension | Adult/juvenile harvest comparison | Mean-field modal theorem; local delayed Hopf open |
| V-STAGE-DELAY | True maturation-delay/stage extension | Adult/juvenile fields with explicit maturation delay | Delayed/distributed maturation operator | Continuous or sampled governance depending on model | Pelagic windows and cohort dynamics | Separate operator; not the one-box Erlang model |
| VI-SP | Frozen-A spatial three-state field | Spatial `(N,Z,E)` | Frozen active pool | Local-effort or mean-field | Spatial Jensen/modal analysis | Mean-field nonzero-mode theorem; local spatial Hopf open |
| VIII-COLL | Inner three-state collocation problem | Fourier orbit `(Y,T)` for `(N,Z,E)` | Same as I-3S | Continuous delay | Hopf interval data and small-branch fold study | Hopf certificate conditional on interval pipeline; fold not certified |

## Closure rules

### Working four-state versus finite donor

The working four-state closure uses a derived target such as

```text
Aeq,W = Aeq,intrinsic + kappaA*K/omegaA
```

and can sustain the high-`Aact` working equilibrium as a frozen-donor or large-reservoir object.

The finite-donor primitive closure instead uses donor-limited primitive transfers and a dynamic `Ageo`. It is a different system. Results from `I-4W` must not be described as results for `II-FD`.

### Inner three-state versus working four-state

`I-3S` is the frozen-active-pool inner problem. Its local Hopfs and global continuation events are not identical to the `I-4W` thresholds.

Typical Candidate-A values:

```text
I-3S gated Hopfs:  tau- ~ 3.666, tau+ ~ 150.358 yr
I-4W gated Hopfs:  tau- ~ 3.78,  tau+ ~ 150.1 yr
```

The inner small-branch event near `tau ~ 5.587` is not automatically the working four-state fold near `tau ~ 5.63`, and neither is automatically the large-cycle termination of the other model.

### Stage notation

- `g` in the one-box Erlang model is a rate parameter.
- A true maturation delay is a separate delay/distributed-delay operator.
- `Tr` denotes periodic-review interval.
- `tau` denotes continuous institutional delay only when the model explicitly uses a DDE.

### Spatial notation

- `j`: spatial mode index.
- `mu_j`: Neumann Laplacian eigenvalue.
- `k_soft`: softplus sharpness.
- `D*mu_j`: modal diffusion rate.

## Result-status vocabulary

Use these labels consistently:

- **Theorem:** proved under explicitly stated hypotheses.
- **Conditional theorem:** proved only after a modal-Hurwitz, yield-gap, or closure hypothesis.
- **Numerical result:** computed for named parameters/operator; not a general theorem.
- **Interval certificate:** requires interval/exact coefficient propagation and validated inclusion.
- **Conjecture/open:** no proof or validated numerical enclosure yet.

## Spatial-result registry

| Object | Spatial statement currently supported |
|---|---|
| I-3S mean-field | Every nonzero mode decays; field stability iff homogeneous DDE stability |
| I-3S local | Exact modal cubic and gain ratio; local delayed spatial Hopf remains open |
| I-4W well-mixed `A` | Nonzero stock modes decay at rate at least `r*N*s/K`; mean-field equivalence |
| I-4W local nondiffusing `A` | Nonzero `(N,A)` block Hurwitz under stated `BN >= 0` condition |
| II-FD | No positive-extraction steady state; no interior exploited rest to spatially destabilize |
| IV-VEC mean-field | Nonzero modes remain Hurwitz under yield gap plus explicit modal-slack hypothesis |
| V-STAGE mean-field | Adult/juvenile nonzero two-stage blocks Hurwitz for stated models |
| Local higher-dimensional fields | No universal negative-diagonal Turing theorem; separate modal analysis required |
| Local delayed spatial Hopf | Open except for named finite grid checks |

## Prohibited cross-paper substitutions

Do not substitute:

- `I-4W` for `II-FD`;
- `I-3S` for `I-4W` without saying frozen-A inner approximation;
- one-box Erlang `g` for a true maturation delay;
- continuous delay `tau` for review interval `Tr`;
- homogeneous Hopf `H` for spatial modal cubic `Hj`;
- empirical Paper VII proxies for model-generated `Tdep`;
- mean-field modal stability for local-institution spatial stability.
