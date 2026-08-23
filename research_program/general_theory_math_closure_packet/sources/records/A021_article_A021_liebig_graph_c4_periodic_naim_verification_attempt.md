# C4 Periodic-NAIM Verification Attempt — Option C

## Status

A new internal numerical verification project was initiated after authorization to pursue the positive-dimensional periodic-NAIM route. No manuscript theorem is promoted by this report. The computations are reproducible local evidence, not a rigorous enclosure of the infinite-dimensional RFDE spectrum.

## Selected minimal instantiation

- Binding block: gated Candidate-A C4 working core.
- Binding delay: `tau=4.5 yr`.
- Binding invariant object: the stable large-amplitude C4 periodic orbit in the lower bistable window, selected away from the lower Hopf (`3.78487`) and lower continuation event (`about 5.63`).
- Provisional slack test block: a second identical gated Candidate-A C4 copy at its equilibrium with the same delay `tau=4.5`.
- Coupling: not instantiated. The calculations verify only the uncoupled product candidate. A generic small `C1` perturbation class can later be considered, but the actual A021 vector-Liebig residuals `f,g` remain missing.

Thus the provisional unperturbed product is

\[
\mathcal M_0=\Gamma_x\times\{\widehat y_*\},
\]

where `Gamma_x` is the selected C4 cycle and `hat y_*` is the identical C4 equilibrium history.

## Binding periodic orbit reproduced

A fixed-step method-of-steps RK4 integration with `dt=0.05 yr`, horizon `50000 yr`, and initial state `(25,300,0.5,10)` converged to a period-one orbit with:

- period `370.95 yr`;
- `N in [45.69208,94.87305]`;
- `A in [834.58311,943.05308]`;
- `Z in [0.001534,0.678093]`;
- `E in [0.354363,20.082770]`.

The memory-floor argument remained positive with minimum margin about `0.00147554`, so this orbit lies in a smooth local region of the C4 vector field.

Time-step convergence:

| `dt` | period |
|---:|---:|
| 0.25 | 370.75 |
| 0.10 | 370.90 |
| 0.05 | 370.95 |

This independently reproduces A018's source-stated C4 period near `371 yr` at `tau=4.5`.

## Discrete monodromy/Floquet convergence

The variational DDE was integrated over one period on the full RK4 discretized history state. Matrix dimensions and results were:

| `dt` | history dimension | phase multiplier | dominant nontrivial multiplier | inferred normal exponent (`yr^-1`) |
|---:|---:|---:|---:|---:|
| 0.25 | 76 | 0.986879 | 0.687748 | 0.00100966 |
| 0.10 | 184 | 0.997749 | 0.687703 | 0.00100943 |
| 0.05 | 364 | 1.001361 | 0.687687 | 0.00100936 |

At all three levels, no nontrivial discretized multiplier had modulus at least one. The leading nontrivial multiplier and derived normal exponent are strongly converged. The next nontrivial multiplier at `dt=0.05` was approximately `0.30237`; the remaining computed multipliers were near zero, consistent with eventual compactness and the rank structure of the delayed coupling.

This establishes strong numerical evidence that the selected C4 orbit is hyperbolic and attracting. It does **not** constitute a rigorous enclosure of every RFDE Floquet multiplier.

## Tangent and projection estimates

From the fine orbit, the supremum-history norm of the phase tangent varied from approximately `0.33317` to `1.51709`, giving the bound

\[
M_c\approx 4.55356
\]

for tangent/inverse-tangent norm ratios over phase.

The finite-discrete phase projection norm was about `547.10`, indicating strong nonnormality. Therefore the Floquet spectral radius alone is not an acceptable bunching proof; transient prefactors matter.

After removing the discrete phase projection, the stable-complement power norms at `dt=0.05` were approximately:

| periods `n` | `||S^n||` | `M_c ||S^n||` |
|---:|---:|---:|
| 20 | 2.6569 | 12.0983 |
| 25 | 0.40863 | 1.86070 |
| 30 | 0.06285 | 0.28617 |
| 35 | 0.00967 | 0.04401 |
| 40 | 0.00149 | 0.00677 |

Thus the finite-discrete `C1` inverse-tangent product drops below one by 30 periods. This is numerical bunching evidence at a very large time map, not a continuum theorem.

## Provisional slack equilibrium spectrum

For an identical C4 equilibrium at `tau=4.5`, an upwind method-of-lines generator converged as follows for its rightmost characteristic pair:

| history intervals | rightmost real part | imaginary part |
|---:|---:|---:|
| 50 | `-6.9797e-5` | `0.02468133` |
| 100 | `-6.8406e-5` | `0.02468110` |
| 200 | `-6.7710e-5` | `0.02468098` |
| 400 | `-6.7362e-5` | `0.02468093` |

A real root near `-0.00103152` was also stable. The provisional slack decay rate is therefore approximately

\[
\beta_y\approx 6.7\times10^{-5}\ {\rm yr}^{-1},
\]

much slower than the binding cycle's principal normal exponent (`about 0.001009 yr^-1`). The slack block controls the product asymptotic rate.

No rigorous semigroup prefactor has yet been extracted for the slack equilibrium.

## Current NAIM disposition

### Newly closed numerically

1. A named gated C4 periodic orbit is selected (`tau=4.5`).
2. Its state profile, period, smooth-floor margin, and branch location are specified.
3. Three-level discretization convergence supports one simple phase multiplier and a strictly stable nontrivial spectrum.
4. A binding normal exponent and tangent norm ratio are estimated.
5. A concrete identical C4 slack equilibrium and its rightmost characteristic pair are estimated.

### Still open

1. Rigorous enclosure of the infinite-dimensional Floquet spectrum and simplicity of the phase multiplier.
2. Continuum invariant history-space projections and their norms.
3. Rigorous binding and slack evolution-family prefactors.
4. A continuum prefactor-aware domination inequality.
5. Concrete multi-block A021 coupling functionals `f,g` and physical coupling.
6. Uniform `C1` perturbation bounds on a tube.
7. Exact BLZ theorem statement and hypothesis match.
8. A stable-foliation/asymptotic-phase theorem match, if claimed.

## Controlling conclusion

Option C has advanced from “no named C4 periodic object” to a **specific, numerically well-supported attracting C4 periodic-NAIM candidate**. It has not reached a rigorous concrete A021 theorem because the continuum enclosures, coupling, and theorem match remain open.

## Reproducible artifacts

Directory: `research_program/article_A021_liebig_graph/computations/`

- `c4_cycle_naim.py`
- `c4_floquet_discrete.py`
- `c4_equilibrium_spectrum.py`
- `summarize_c4_naim.py`
- `c4_naim_numerical_summary.json`
- `c4_bunching_discrete.json`
- time-step-specific orbit and Floquet `.json`/`.npz` files.
