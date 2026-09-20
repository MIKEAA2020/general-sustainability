# SafeTransition

**Exact rational certification of transition safety** — typed assessment
operators, backward recursions, Farkas obstruction certificates, and
dashboard readings for sustainability transitions.

- Version 1.0.0 · Python ≥ 3.9 · **zero runtime dependencies** (standard library only) · MIT
- Verification deposit: <https://doi.org/10.6084/m9.figshare.33764023>

## Purpose

Composite (scalarized) indicators can certify a transition that breaches a
typed floor mid-way: a weighted index can stay positive along a plan while
an ecological or social floor is driven below zero. SafeTransition turns the
mathematical resolution of this failure mode — developed in the companion
manuscripts *Aggregate Indices and Transition Safety: A Quantifier-Order
Separation Between Scalarized and Coordinate-Wise Feasibility* and *An
Obstruction Calculus for Viability under Incomplete Observation* (A. Abaee)
— into auditable software:

1. **Typed assessment operators.** The noncompensatory typed operator, the
   scalarized aggregate operator at any positive weight, the exact-tube
   physical operator, and the endpoint-only operators, with the operator
   chain checked exactly at each state.
2. **Backward recursions.** The finite-graph typed recursion (polynomial in
   graph size and horizon) and the belief-space robust epistemic recursion
   for partially observed systems (sound and complete in finite systems).
3. **Obstruction certificates.** Exact rational Fourier–Motzkin elimination
   with provenance tracking returns Farkas certificates `lam ≥ 0`,
   `lam·A = 0`, `lam·b < 0` with the infeasibility margin; the common-action
   obstruction reports a minimal conflicting subfamily of states; the
   observation-fibre criterion decides when an exact observation-only
   certifier can exist.
4. **Dashboard readings.** Per-weight licensing thresholds (the witness
   values are rho1 = 2/3 and rho2 = 3/2), the rescue threshold
   kappa\* = 1 − x on the non-typed-viable region, per-plan floor minima,
   the composite-index minimum, and the index-blindness alarm — rendered as
   a single self-contained HTML file (inline SVG/CSS, no external resources).

Every assessment, recursion, and certificate runs in **exact rational
arithmetic** (`fractions.Fraction`). Floats appear only in rendered SVG
geometry, never in checks. This complements floating-point viability and
control toolboxes: outputs here are *verifiable*, not merely computed.

## Installation

```bash
pip install .            # from this directory; no dependencies will be pulled
```

## Quickstart

```bash
safetransition verify                 # 24/24 exact benchmark checks
safetransition demo --out dash.html   # checks + certificate demos + dashboard
safetransition report --out dash.html # dashboard only
python -m unittest discover -s tests  # test suite
```

Library use (the witnessed separation: the aggregate operator licenses a
plan at w = (1, 1) while the typed operator admits none):

```python
from fractions import Fraction as Q
from safetransition import WitnessDatum, witness_state, E, compute

datum  = WitnessDatum()
z      = witness_state(Q(1, 2), Q(6, 5), Q(6, 5))   # (fund, floors) = (1/2, 6/5, 6/5)

E(datum, z, mode="typ")                 # -> frozenset()          (typed: empty)
E(datum, z, mode="w", w=(Q(1), Q(1)))   # -> {'FAST'}             (aggregate: licensed)

r = compute()                           # exact dashboard readings
(r.rho1, r.rho2, r.kappa_star)          # -> (2/3, 3/2, 1/2)
r.blind_alarm                           # -> True: index min 2/5 > 0, floor -4/5 < 0
```

Partial observation and certificates:

```python
from safetransition import belief_backward, certify_polyhedron, fibre_criterion

# u <= 2/5 and -u <= -3/5 cannot hold: exact Farkas certificate
res = certify_polyhedron([[1], [-1]], [(2, 5), (-3, 5)])
res.certificate.lam, res.certificate.margin   # -> ((1/2, 1/2), 1/10)
```

## Certificate protocol

Every infeasibility verdict ships as a checkable object. Farkas
certificates serialize to JSON (exact rationals as strings) and are
re-verified by the repository-root script `check_safe_transition_cert.py`,
which shares **no code** with the package and re-derives each verdict from
the certificate's own contents. The `weight_partition` certificate carries
the complete licensed-set arrangement along the weight ratio (including
the regime dip > s1 + s2, where the thresholds swap and an unlicensed gap
opens around r = 1), and `benchmark_certificate` emits the benchmark
parameters plus eleven derived quantities that the checker re-derives
independently. Tampered certificates are rejected by design — try it:

```sh
PYTHONPATH=src python3 -m safetransition.cli certify --outdir certificates
python3 check_safe_transition_cert.py certificates/*.json
# then flip any entry in a JSON file and re-run: the checker rejects it
```

## The built-in benchmark

`run_benchmark()` re-derives, in exact arithmetic, the twenty-four verified
quantities of the resource-transition benchmark (a Schaefer realization of
the witness datum): witness and tube tables, quota admissibility on both
disturbance branches, conservatism of the certified tubes for the nonlinear
(logistic surplus) realization, index blindness at w = (1, 1), the licensing
thresholds 2/3 and 3/2, the rescue threshold, and the sustained-yield
(σ(16/5) = 1088/125) and staged-rebuild schedules. The same checks are
archived, with the figure pipeline, in the verification deposit
(DOI 10.6084/m9.figshare.33764023).

## Architecture

| Module | Contents |
| --- | --- |
| `rational` | exact rational helpers (`frac`, `fmt`) |
| `datum` | typed transition data; the fully specified `WitnessDatum` |
| `operators` | the five operators, accepted-state sets, `V_weak`, chain check |
| `recursion` | typed finite-graph recursion; belief-space recursion |
| `certificates` | Fourier–Motzkin + Farkas (serializable); common-action obstruction; fibre criterion |
| `check_safe_transition_cert.py` | independent stdlib-only verifier for serialized certificates (repository root) |
| `indicators` | licensing thresholds, rescue threshold, blindness alarm |
| `dashboard` | single-file HTML rendering (inline SVG/CSS) |
| `benchmark` | the twenty-four exact checks and verified schedule values |
| `cli` | `verify` / `report` / `demo` / `certify` |

## Citation

If you use SafeTransition, please cite the verification deposit and the
companion manuscripts:

> Abaee, A. (2026). *Verification code and figure pipeline for Aggregate
> Indices and Transition Safety* [dataset]. figshare.
> <https://doi.org/10.6084/m9.figshare.33764023>

> Abaee, A. (2026). *Aggregate Indices and Transition Safety: A
> Quantifier-Order Separation Between Scalarized and Coordinate-Wise
> Feasibility* (manuscript; verified by the deposit above).

> Abaee, A. (2026). *An Obstruction Calculus for Viability under Incomplete
> Observation* (manuscript; certificate family implemented in
> `safetransition.certificates`).

## License

MIT. The verification deposit is distributed under CC-BY-4.0.
