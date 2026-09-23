# Supplementary Material — SafeTransition: exact rational certification of transition safety for sustainability assessment

*Accompanies:* A. Abaee (2026). *SafeTransition: exact rational
certification of transition safety for sustainability assessment*
(manuscript v7, Environmental Modelling & Software submission).
Verification deposit: <https://doi.org/10.6084/m9.figshare.33764023>.

*Section references of the form "Section n" refer to the accompanying
manuscript; references S1–S11 are internal to this supplement. Package
version 1.3.0; all quantities are exact rationals unless stated as
rendering floats. Changes from the v3 supplement: S1–S3 aligned with the
v7 semantics (tube statuses, endpoint reset, operator scope, belief
quotient semantics, feasibility-honesty, minimum-cardinality
subfamilies); S5 updated to the 1.3.0 tree (58 tests); S9 extended
(belief\_failure checker type, one-sided verdict semantics, property
battery); S10 rewritten for the 1.3.0 study (six families, separated
numerator/denominator bit metrics, dense stress family with recorded
practical envelope, platform metadata); S11 added (pooled-kernel
regression anchor).*

---

## S1. The five assessment operators, as implemented

A typed transition datum consists of a phase state `z = (q, x, s1, ..., sn)`
(phase flag, fund coordinates, typed floors normalized to zero), a finite
action set, a finite disturbance set, a tube `Tube(a, d)` for each action
and disturbance (the set of states visited over the review period), a
transition-safe set `S`, and a destination set `G` reached under an
endpoint reset with gain vector `e`. Actions declare breakpoint offsets;
each tube carries a status: `EXACT` (the exact visited set of its
declared piecewise-linear paths) or `CONSERVATIVE` (a certified outer
enclosure of an underlying nonlinear realization). The status fixes the
verdict direction: constraints passed on an exact tube certify the
represented trajectory safe (violation: unsafe); on a conservative
enclosure, passing certifies the realization safe, while a violation is
inconclusive unless the violating point is known reachable (Section 2.1;
one-sided semantics also documented on `TubeStatus`).

All five operators share the same finite disturbance set per action, the
same reset, and the same destination condition; weights are strictly
positive; endpoint tests evaluate at the terminal pre-reset state
`y⁻`, destination tests at the post-reset successor `z⁺ = R(y⁻)`.

| Operator | Condition on each `(a, d)` | Destination test |
| --- | --- | --- |
| Typed, noncompensatory `E_typ` | `Tube(a,d) ⊆ S_typ = {x ≥ 0, s_i ≥ 0 ∀i, Phys}` | `z⁺` in `G` |
| Scalarized aggregate `E_w` | `Tube(a,d) ⊆ {x ≥ 0, w·s ≥ 0, Phys}` | `z⁺` in `G`, `w·s ≥ 0` |
| Exact-tube physical `E_tube,phys` | `Tube(a,d) ⊆ {x ≥ 0}` | `z⁺` in `G_phys` |
| Endpoint-only physical `E_end` | `y⁻` in `{x ≥ 0}` | `z⁺` in `G_phys` |
| Typed-endpoint `E_end,typ` | `y⁻` in `S_typ` | `z⁺` in `G` |

Each inclusion in the chain
`E_typ(z) ⊆ E_w(z) ⊆ E_tube,phys(z) ⊆ E_end(z)` holds at every state and
positive weight, possibly strictly: floors with the physical constraint
included imply their weighted shadow under `w > 0`; deleting floors
weakens the condition; a tube constraint implies the same constraint at
the contained pre-reset endpoint; typed sets include the physical
constraint by definition. `check_chain` verifies each inclusion exactly
on request (Section 3.3). The accepted-state set `V[E] = {z : E(z) ≠ ∅}`
and the compensatory accepted set `V_weak = ⋂_w V_w` follow. `V_weak` is
the `∀w ∃a` condition (the licensed action may depend on the weight) and
is in general strictly larger than the `∃a ∀w` uniform-action condition;
the witnessed separation `V_typ ⊆ V_weak`, strict in general, is the
formal statement of what a composite index cannot see (Section 2.1).

## S2. The recursions

**Typed recursion.** On an explicit state–action graph, `W_0` is the safe
set and `W_{k+1} = {z : some action keeps every visited state safe under
all of the action's disturbances and its successor lies in W_k}`.
Under a unit-cost predicate model the recursion is polynomial in the
numbers of states, state–action pairs, and horizon; bit complexity
depends on rational coefficient growth and is reported by the scaling
study (S10) (Section 2.2).

**Belief-space recursion.** States carry observation labels `γ`; beliefs
are elements of the quotient of the state space by `γ` — sets of labels
whose state fibres are re-expanded at every step. An action is
admissible for a belief `B` when no state in any of `B`'s labels' fibres
enters a violation under any of the action's disturbances; the belief
updates to the labels reachable under the action. `W_0` is the safe
label set; `W_k` denotes the k-step viable beliefs.

*Soundness (all finite systems).* `B ∈ W_k` certifies a belief-based
(observation-history) policy viable for k steps.

*Completeness (conditional).* A belief outside `W_N` admits no such
policy only when `γ` is a safety-and-action quotient: safe-set
membership and action admissibility constant on fibres, successors
label-determined. Label injectivity on reachable states is the simplest
sufficient condition. Absent the quotient condition, non-membership is
an abstraction artifact, not a certificate of policy nonexistence
(Section 2.2).

Beliefs in `W_1 \ W_2` exhibit post-observation recourse failure — the
demonstration instance of Section 4.3 (manuscript Table 5) has the
three-state system with root belief `{y12}`, which is one-step viable
and exits at the second step under every observation-based policy. The
failure explainer's output serializes as a `belief_failure` certificate
(system, horizon, per-action reason codes) that the independent checker
re-derives from the serialized system alone (S9).

## S3. The certificate family, with a worked derivation

For a stacked rational system `Au ≤ b`, Fourier–Motzkin elimination with
provenance tracking derives each row together with its multiplier vector
over the original rows. A derived contradiction `0 ≤ c, c < 0` yields,
after normalization, `λ ≥ 0` with `λᵀA = 0` and `λᵀb < 0`; the library
re-verifies both identities exactly before returning the certificate
with its normalized certificate contradiction value `−λᵀb > 0`:
invariant to positive rescaling of `λ` (fixed by normalizing
`Σλ = 1`) but not invariant under rescaling of the input rows, and
therefore a property of the normalized certificate rather than an
intrinsic distance to feasibility (Section 2.3). Feasible systems
return a bare verdict: feasibility is decided, not witnessed.

**Worked derivation (the stacked menu window of Section 4.3).** System:
`u ≤ 2/5` (row 1) and `−u ≤ −3/5` (row 2). Eliminating `u` combines the
rows with nonnegative multipliers: `1·(row 1) + 1·(row 2)` gives
`0 ≤ 2/5 − 3/5 = −1/5 < 0`, provenance `(1, 1)`. Normalizing the
provenance to a convex combination gives `λ = (1/2, 1/2)`; then
`λᵀA = (1/2)·1 + (1/2)·(−1) = 0` and `λᵢb = (1/2)(2/5) + (1/2)(−3/5) =
−1/10 < 0`. The certificate is returned with margin exactly `1/10`,
matching the infeasibility margin quoted in Section 4.3 and manuscript Table 4.

**Common-action obstruction.** Fires when the safe-action sets of a
family of mutually possible states (co-possible under the assessed
observation) intersect emptily while each is nonempty; with recursively
viable action sets the obstruction rules out a viable observation-based
policy at that horizon. A minimum-cardinality conflicting subfamily is
reported (exhaustive search in nondecreasing size), so every strictly
smaller subfamily is certified to intersect (Section 2.3).

**Observation-only safety-classification criterion.** Current safe-set
membership is exactly classifiable from the current observation alone
iff it is constant on observation fibres; a violating fibre is reported
otherwise. The criterion concerns this classification only — it does
not rule out observation-history policies, belief-based control,
conservative certifiers, or three-valued procedures (Sections 2.3 and
4.3).

## S4. Complete enumeration of the twenty-four benchmark checks

The `benchmark` module re-derives every deposited value of the
resource-transition benchmark (Section 4.1; Schaefer realization with
`r = 4`, `K = 10`, `B_lim = 2`, `H_max = 13`, `δ0 = 1/2`). All twenty-four
pass; runtime under one second (Xeon @ 2.60 GHz; manuscript Table 4):

1. witness datum `(x, s1, s2) = (1/2, 6/5, 6/5)`; gain `e = (1/4, 1/4)`; cost `c = 1`;
2. FAST tubes `(6/5, −3/10, 6/5)` benign and `(6/5, −4/5, 6/5)` adverse; `s2` flat;
3. STAGED at the rescue witness: fund `3/2 → 1/2`, `s1: 6/5 → 29/20`;
4. parameters exact;
5. stock levels `16/5`, `17/10`, `6/5`, all below `K/2` (surplus increasing);
6. certified leg slopes `3/yr`, `4/yr`;
7. quota range `[3 + σ(17/10), 3 + σ(16/5)]`;
8. quota admissibility, peak `1463/125 ≤ 13`;
9. closed season on `(1/2, 1)`;
10. benign branch tracks its line exactly (`σ(L) − H* = −3`);
11. strike drops the stock by `δ0 = 1/2` (`17/10 → 6/5`);
12. conservatism: `σ ≥ 528/125 ≥ 4` on the adverse recovery leg;
13. benign recovery: `3 ≤ σ(17/10) = 1411/250`;
14. tubes conservative for the nonlinear realization;
15. index `s1 + s2` at `w = (1,1)`: `(12/5, 2/5, 12/5)`, min `2/5 > 0`;
16. floor breached on both branches (`−4/5` adverse, `−3/10` benign);
17. typed reading: FAST and SLOW both typed-infeasible at the witness;
18. licensing thresholds `ρ1 = (2 − s1)/s2 = 2/3`, `ρ2 = s1/(2 − s2) = 3/2`;
19. no weight ratio licenses a typed-safe plan (`ρ1 < 1 < ρ2`);
20. rescue threshold `κ* = 1 − x`; witness shortfall `1/2`; rescue witness `3/2 ≥ c`;
21. sustained-yield quota `σ(16/5) = 1088/125`, admissible;
22. STAGED rebuild: stock `16/5 → 69/20`, both margins improve by `e = 1/4`;
23. STAGED quota `[2051/250, 8539/1000]`, admissible;
24. schedule values assembled from verified exact quantities.

## S5. Package artifact tree and reproduction

Package 1.3.0 (Section 6; MIT; Python ≥ 3.9; no runtime dependencies):

```
safetransition/
├── pyproject.toml, LICENSE (MIT), CITATION.cff, README.md, CHANGELOG.md
├── check_safe_transition_cert.py   # independent stdlib-only certificate checker (S9)
├── run_all.sh                      # one-command fresh reproduction (7 steps)
├── SHA256SUMS                      # integrity manifest (regenerated for 1.3.0)
├── benchmarks/                     # scaling study + committed full results (S10)
├── requirements-figures.txt        # pinned figure environment (optional)
├── dashboard.html                  # rendered single-file dashboard
├── docs/                           # submission plan; style notes
├── examples/                       # northern_cod_dashboard.py; partial_observation.py;
│                                   # certificates_demo.py (produce -> check -> tamper)
├── figure_code/                    # figure pipeline (readings, benchmark, certificate
│                                   # chain); graphical-abstract TIFF export
├── novelty_searches/               # related-software search records (S6)
├── src/safetransition/             # 9 modules, 1,698 lines
└── tests/                          # 59 tests, 966 lines (9 files)
```

`sh run_all.sh` executes, in order: the test suite (59/59, including the
certificate-protocol, scaling closed-form, provenance-determinism, and
property-based/degenerate batteries), the exact benchmark checks (24/24),
certificate emission plus the
independent checker over the emitted certificates, the three worked
examples (the certificates demo ends in tamper rejection), the quick
scaling sweep (writing a disposable results file; the committed full run
is never clobbered by a reproduction), and — when matplotlib/Pillow are
installed at the versions pinned in `requirements-figures.txt` (3.10.9
and 12.3.0) — figure regeneration (the readings, benchmark, and
certificate-chain figures via `make_safetransition_figs.py` and
`make_certificate_chain.py`, from the library's verified schedule
values), including the graphical-abstract TIFF. A SHA256SUMS
manifest covers all package files; hashes reproduce byte-for-byte on a
fresh extract apart from any rendered dashboard output, which `run_all.sh`
writes to a disposable filename.

## S6. Related-software search records

Section 5's positioning is backed by preserved search records, deposited in
the package directory `novelty_searches/` (six queries; verbatim result
records: title, URL, snippet excerpt, host, rank; method and mapping
README). Summary of the protocol:

| Query file | Target of the query | Records kept |
| --- | --- | --- |
| `q1_viability_kernel_software.json` | viability-kernel computation software (pyviability GPU work; kernel-method libraries) | 3 |
| `q2_farkas_exact_rational.json` | exact rational Farkas-certificate practice (certificate-based proofs; independent verifiers; an LP bug report on unvalidated certificates) | 3 |
| `q3_composite_indicator_software.json` | composite-indicator and dashboard software (LCA/industrial-ecology indexes; dashboard tooling) | 3 |
| `q4_exact_verification_companions.json` | exact-verification companions and arbitrary-precision libraries (SHA-256-manifested verifiers; mpmath; Coq-certificate tooling) | 3 |
| `q5_fourier_motzkin_libraries.json` | Fourier–Motzkin implementations (Maxima `fourier_elim`; cddlib; pyfme with Imbert accelerations) | 3 |
| `q6_mcda_compensation_tools.json` | MCDA index software and compensation levels (MCDA Index Tool; food-sector MCDA software review) | 3 |

Searches executed 2026-09-20 via agent-mediated web search; records are
verbatim snapshots trimmed for length, with no additions, reordering, or
edits beyond excerpting. Two observations from the records inform
Section 5 directly: (i) the nearest elimination neighbour, pyfme, is
symbolic and general-purpose and does not track Farkas provenance for
certificate return; (ii) among MCDA index tools, full-compensation
aggregation is the default and only variable-compensation option reported
in the surveyed tools is the MCDA Index Tool — the compensation axis the
accompanying framework formalizes. The Section 5 positioning is made
against these records.

The verification deposit additionally carries the manuscript-level search
set of twelve queries (`pkg/novelty_searches/`, q1–q12; schema per record:
`url`, `name`, `snippet`, `host_name`, `rank`, `date`), covering — beyond
the six package queries above — noncompensatory aggregation tools,
viability-kernel aggregation practice, safe-transition software,
price-dependent viability, quantifier-order separation, and false-positive
instances for typed floors. Section 5's named comparison set (z3, PRISM
4.0, pyfme) is cited with DOIs in the manuscript and the gap statement is
scoped accordingly: the environmental families return no certificates and
compute in floating point; general-purpose provers certify in their own
domains but ship no assessment semantics (floors, weight-licensed plan
menus, reachability tubes, epistemic viability sets).

## S7. Notation

| Symbol | Meaning |
| --- | --- |
| `z = (q, x, s1, ..., sn)` | phase state (flag, funds, typed floors) |
| `E_typ, E_w, E_tube,phys, E_end, E_end,typ` | the five operators (Section 2.1) |
| `V[E], V_weak` | accepted-state set; compensatory accepted set |
| `W_k` | k-step viable states (typed) or beliefs (belief recursion) |
| `ρ1, ρ2` | per-weight licensing thresholds at the witness: `2/3`, `3/2` |
| `κ*` | rescue threshold `max(0, 1 − x)` on the non-typed-viable region |
| `σ(B)` | Schaefer surplus `rB(1 − B/K)` |
| `λ` | Farkas multiplier vector; margin `−λᵀb > 0` |
| `γ` | observation map (state → label) |
| `Tube(a, d)` | visited set for action `a` under disturbance `d`; status `EXACT` or `CONSERVATIVE` |
| `S_typ, S_phys` | typed / physical safe sets (`S` without subscript denotes the typed set) |
| `y⁻, z⁺ = R(y⁻)` | terminal pre-reset state; post-reset successor under reset `R` |

## S8. Citation

- Abaee, A. (2026). *SafeTransition: exact rational certification of
  transition safety for sustainability assessment* (software description;
  venue-agnostic master v1; Environmental Modelling & Software submission
  v7).
- Abaee, A. (2026). *Verification code and figure pipeline for Aggregate
  Indices and Transition Safety* [data set]. figshare.
  <https://doi.org/10.6084/m9.figshare.33764023>
- Abaee, A. (2026). *Aggregate Indices and Transition Safety: A
  Quantifier-Order Separation Between Scalarized and Coordinate-Wise
  Feasibility* (companion manuscript).
- Abaee, A. (2026). *An Obstruction Calculus for Viability under Incomplete
  Observation* (companion manuscript).

## S9. Certificate protocol: serialization, independent checking, negative tests

Every infeasibility verdict ships as a checkable object with a defined
serialization and an independent verification path.

**Schema (Farkas certificate, JSON).** `type = "farkas"`; `A` (constraint
matrix), `b` (bounds), `lam` (multiplier vector), all exact rationals as
strings (`"num/den"`); `margin = −lamᵀb > 0`; `status = "infeasible"`.
`from_dict` reconstructs the object and re-verifies the defining
identities before use.

**Independent checker.** The repository-root script
`check_safe_transition_cert.py` imports only the Python standard library
and shares no code with the package. For each certificate type it
re-derives the verdict from the certificate's own contents:

| Type | What the checker re-derives |
| --- | --- |
| `farkas` | `lam ≥ 0`; `lamᵀA = 0` column-wise; `lamᵀb < 0`; reports the exact margin |
| `weight_partition` | thresholds from the floors and dip; region tiling, ordering and inclusivity for all three regimes; licensed sets at a sampled ratio per region; the binding witness constraint at each boundary |
| `benchmark` | all eleven derived values from the parameters alone (surplus values, quota bounds, thresholds, rescue value, index/floor minima); tube-enclosure inequalities (monotone interval inside (0, K/2), min σ ≥ required slope) |
| `belief_failure` | re-runs the belief recursion on the certificate's serialized system through a stdlib-only reimplementation independent of the library; validates the reported non-viability verdict and every per-action failure reason (fibre states, post-beliefs) |

The checker validates certificates against the supplied system data —
algebraic validity and, for the partition/benchmark/belief-failure
schemas, re-derivation from the certificate's own contents. The
manuscript's Table 6 summarizes emission and checking per class,
including the findings deliberately left unserialized (minimum-
cardinality subfamily, violating fibre) and the witness-free feasibility
verdict. It does not
certify that a supplied system matches an external intention, nor the
scientific validity of any datum (Section 4.2, Fig. 2).

Exit codes: 0 every certificate verified, 1 at least one rejected, 2
usage error.

**Negative tests.** The suite asserts rejection of (i) an altered bound
`b`, (ii) an altered multiplier vector `lam`, (iii) an altered system
matrix `A`, for Farkas certificates; the weight-partition checker is
exercised against an inconsistent licensed set; the benchmark checker
against a perturbed derived value (`1089/125` in place of `1088/125`);
the belief-failure checker against tampered per-action reasons and
post-beliefs. A 30-case mutation fuzz (altered `lam` entries and `A`
entries) confirms rejection of every mutation. The suite also encodes
the checker's algebra-versus-semantics boundary as a passing test: a
bound change that leaves the stacked system infeasible with the same
multipliers yields a certificate that verifies for the tampered system
— the checker validates certificates against supplied systems, not
systems against intended data.

**Property-based and degenerate battery (1.3.0).** Seeded randomized
chain inclusion (60 instances), Farkas validity cross-checked against an
independent exact vertex-enumeration oracle (60 instances, full-rank
gated), belief-recursion monotonicity, partition coverage sampling
including the STAGED-licensed-when-financed degenerate regime,
coincident thresholds (`ρ₁ = ρ₂`), zero and duplicate rows, empty
action menus, uneven action menus across an observation fibre (the
belief recursion screens an action only against the fibre states that
offer it), and cross-process canonical-JSON hash stability under three
`PYTHONHASHSEED` values.

**Tube-status semantics (one-sided).** `TubeStatus ∈ {EXACT,
CONSERVATIVE}`: declared piecewise-linear plan tubes are EXACT (each
equals the visited set of its paths); the Schaefer realization's tubes
are CONSERVATIVE outer enclosures, certified by monotonicity of σ on
the visited biomass interval [6/5, 16/5] ⊂ (0, K/2) = (0, 5)
(σ′(B) = 4 − 4B/5 > 0 there), giving σ ≥ σ(6/5) = 528/125 ≥ 4 on the
recovery legs. The verdict semantics are one-sided and conservative:
pass on a conservative enclosure certifies the realization safe;
violation inside the enclosure is inconclusive unless the violating
point is known reachable; on EXACT tubes both directions are
conclusive.

**Adversarial exactness instance.** The trough condition
49·(1/49) − 1 = 0 holds exactly (floor exactly met; the plan is licensed
in mode `w`), while direct IEEE-754 binary64 evaluation in the tested
expression order with an exact-zero threshold evaluates it to
−1.1102230246251565 × 10⁻¹⁶ (falsely unlicensed). This is a regression
case for one direct evaluation path, not a claim that floating-point
tooling generally errs (7·(1/7), by contrast, rounds to exactly 1.0
and is not an instance). The library rejects floating-point input
structurally, so this failure mode is excluded by construction.

**Belief failure witnesses.** `explain_belief_failure` returns, for a
non-viable root belief, the horizon of first failure and, per action,
either the fibre states entering a violation en route or the post-belief
that is not viable at the previous level; each action is admissible in
isolation in the state-wise, one-step, full-information sense. On the
recourse-failure system both actions fail with post-belief {y12, y4}
not one-step viable. The object serializes (`failure_certificate`) as a
`belief_failure` certificate checked as in the table above. Where the
audit's reference design nests the post-belief's failure certificate
recursively inside the parent object, this implementation achieves the
same machine-checkability by checker re-derivation (the recursion is
re-run from the serialized system), so the serialized object stays
flat; the checker verdict is honest about scope — it confirms the
failure object is re-derived from the serialized system, not that the
system matches any external intention. The belief-enumeration bound is a parameter
(default 4,096); exhaustion raises with no partial results —
exploration completeness is affected, never the soundness of returned
memberships.

## S10. Scaling study (package 1.3.0)

`benchmarks/scaling_study.py` sweeps six parameterized instance families
whose answers are known by construction and asserted at every size. The
committed full run (`benchmarks/scaling_results.json`; 73.6 s total,
single run per instance, no warm-up, wall-clock; Intel Xeon @ 2.60 GHz,
Linux x86-64, CPython 3.13) reports, per instance: wall-clock runtime,
peak traced memory (`tracemalloc`, which adds overhead to traced
phases), eliminator rows generated and peak working rows, certificate
JSON size, maximal numerator and denominator bit lengths **reported
separately**, reachable-belief counts, and the independent checker's
runtime (including subprocess startup). Platform, CPU, OS, Python
version, and the full methodology are recorded in the results metadata.
`--quick` runs a CI-sized sweep to a disposable file; the committed full
results are never clobbered by a reproduction.

| Family | Known answer (asserted) | Measurement at the stated instance |
| --- | --- | --- |
| FM chain, largest run k = 256 (rows 257) | infeasible; margin (1/5 − 255/4096)/257 | 1.59 s; 256 rows generated; certificate 335 kB, 13-bit coefficients; checker 0.29 s |
| Dyadic growth, largest run t = 320 (L = 5 links) | margin 2⁻³²⁰/7 exactly | certified exactly; margin numerator 1 bit, denominator 323 bits (7·2³²⁰) |
| Dense stress, 4 variables (12 rows), infeasible | Farkas certificate verified | 7,505 intermediate rows generated; 2.2 s |
| Dense stress, 4 variables (12 rows), feasible | feasible | impractical: 60 s budget exceeded (recorded as the envelope) |
| Typed recursion, 21,000 states (horizon 20) | all states viable | 2.1 s; linear in states |
| Action menu, 512 actions | all admissible in all five modes | 2.5 s |
| Beliefs, largest completed m = 12 | exactly 2^m reachable beliefs | 4,096 enumerated; overflow test m = 13 raises, no partial results |

Growth reading: within these structured planted-answer families, exact
rational certification remains stable as coefficient size and instance
dimension grow — elimination terminates at the planted contradiction;
the typed recursion is linear in the state count; menu cost is linear in
menu size; belief enumeration is exponential in m, as the reachable set
itself is. Within the tested range, coefficient growth had a larger
observed effect on certificate size than on wall-clock time. Closed
forms (margin (1/5 − (k−1)/4096)/(k+1) for the chain; 2⁻ᵗ/7 for the
dyadic family with L = 5) are asserted at every swept size and
re-asserted on small instances in the unit suite (59 tests).

The planted families measure correctness and exact-arithmetic stability
under controlled growth. The dense stress family complements them by
reporting the classical Fourier–Motzkin row growth without
deduplication on random dense systems (entries in [−5, 5]/[1, 3]; 3t
rows, t variables; each case under a 60 s wall-clock budget via
`SIGALRM`, seeds 20260920): 24 rows generated at t = 2, 975 rows at
t = 3 (feasible case), 7,505 rows at t = 4 (infeasible, 2.2 s), and
budget exceeded at t = 4 (feasible). The dense-system envelope of the
eliminator is narrow — consistent with the exponential worst-case
generation of intermediate inequalities stated in Section 3.3 — and
the recorded impracticality point is itself part of the study's output.

## S11. Pooled-kernel regression anchor (deposited double-integrator instance)

Section 4.3 checks, exactly, the pooled-kernel identity of the deposited
double-integrator instance: three constraint normals with a strictly
positive pooling that vanishes in the aggregate.

Normals and weights:

| j | nⱼ | λⱼ |
| --- | --- | --- |
| 1 | (1, 0) | 3/8 |
| 2 | (−3/5, 4/5) | 5/16 |
| 3 | (−3/5, −4/5) | 5/16 |

Identities (verified exactly by
`tests/test_certificates.py::test_3d_pooled_kernel_instance` and printed
by `examples/partial_observation.py`):

- `Σⱼ λⱼ = 3/8 + 5/16 + 5/16 = 1` (convex pooling);
- `\Sigma_j \lambda_j n_j = (3/8 − 3/16 − 3/16,  (5/16)(4/5) − (5/16)(4/5)) = (0, 0)` exactly.

Each normal is a unit vector (1² + 0² = 1; (−3/5)² + (±4/5)² = 1), so
the weights `λⱼ` are barycentric coordinates of the origin in the
triangle spanned by the normals: a strictly positive dependence
`Σλⱼ nⱼ = 0` with `Σλⱼ = 1` — the algebraic content of the
pooled-kernel identity. The instance serves as a cross-paper regression
anchor: the identity is quoted in the companion obstruction-calculus
manuscript and re-verified in this package's suite, so a regression in
either artifact's arithmetic surfaces in both.

## S12. The assessment paper's grid verifier: the 25 exact checks

*New in supplementary v5.* The companion manuscript *Aggregate Indices
and Transition Safety* (S8, third entry) ships its own machine artifact
— the **grid verifier**
`verification/typed_false_positive_instantiation.py` in the deposit
(S8, second entry) — checking the finite rational instance of its
Proposition 3, Proposition 4, Theorem 5, and Remark 7. This section
enumerates its 25 checks, which the manuscript cites; the software's
separate 24-check benchmark suite is enumerated in S4, and the two
counts index different check lists (25 ≠ 24 is not a disagreement).

**Execution record.** Run 2026-08-28; deterministic; exact integer
arithmetic throughout (scale 40: dip 3/2 → 60, worst-case dip 2 → 80,
floor threshold 2 → 80, reset gain 1/4 → 10, rescue cost 1 → 40, grid
step 0.1 → 4); no floats, no tolerances, no randomness, no outer tube
approximation. Grid `[0,3]³` at step 0.1 in `(x, s₁, s₂)` = 29,791
states; runtime ≈ 36 s; **25/25 checks pass**, exit 0; results committed
as `typed_false_positive_instantiation.json`. The false-positive set
occupies 1,900 grid states.

**The checks** (labels `[T1]`–`[T10]` are the verifier's internal
theorem-file groups, mapped to the manuscript's results in the first
row of each group):

- **[T1] exact-tube machinery** (underlies Propositions 3–4):
  1. FAST breakpoint table exact (dip at t = 1/2, recovery at t = 1);
  2. STAGED breakpoint table exact (linear spend/growth);
  3. per-coordinate exact ranges = breakpoint extremes (piecewise
     monotonicity asserted);
  4. worst-case dip constants: benign 3/2, adverse 2, floor
     threshold 2.
- **[T2–T4] the three assessment regions** (Theorem 5(1)–(3)):
  5. machine typed-feasibility = {x ≥ 1} ∪ {s₁ ≥ 2} ∪ {s₂ ≥ 2} on
     every grid state;
  6. machine all-weights admissibility = {x ≥ 1} ∪ {s₁ + s₂ ≥ 2} on
     every grid state (per-weight search over the dense critical set
     r = k/20, k = 0..40, r = ∞, the exact boundary weights ρ₁, ρ₂,
     and the adversarial midpoint — all exact integer pairs);
  7. FAST/SLOW per-weight safety biconditionals (r ≥ ρ₁ / r ≤ ρ₂) on
     every grid state over the dense weight grid;
  8. boundary weights exact: FAST safe at r = ρ₁, SLOW safe at r = ρ₂;
  9. machine endpoint-only feasibility = all of X₀ on every grid state.
- **[T5] hierarchy** (Theorem 5(4)):
  10. typed ⇒ all-weights-aggregate ⇒ endpoint-only, no violations on
      the grid.
- **[T6–T7] the false-positive set** (Proposition 3 instance):
  11. false-positive set nonempty on the grid;
  12. interior witness (1/2, 6/5, 6/5): aggregate-feasible for every
      critical weight;
  13. the witness is interior (all ±0.1 neighbours remain in FP);
  14. endpoint-only witness (1/2, 1/10, 1/10): endpoint-feasible,
      aggregate-infeasible at w = (1, 1);
  15. aggregate-vs-typed strictness witness confirmed.
- **[T8] per-weight licensing at the witness** (Proposition 4
  instance):
  16. r = 1/2: SLOW-only (FAST unsafe, SLOW safe);
  17. r = 1: both plans safe;
  18. r = 2: FAST-only (SLOW unsafe, FAST safe);
  19. E_typ = ∩_w E_w = ∅ machine-verified over the full critical
      weight set.
- **[T9] the rescue split** (Remark 7 instance):
  20. R witness (3/2, 6/5, 6/5): typed-transformable via STAGED;
  21. I witness (1/2, 6/5, 6/5): all four actions rejected, each with
      its exhibited violated constraint (the negative-certificate
      form);
  22. rescue split verified on the whole grid.
- **[T10] multi-stage propagation** (Remark 7, stages):
  23. stage-0 hierarchy holds and regions are preserved through two
      hold intervals;
  24. the FP strictness witness survives the holds at stage 0;
  25. the endpoint-only strictness witness survives the holds at
      stage 0.

**Status discipline.** A machine pass confirms the manuscript's
closed-form proofs at the exact-integer level stated per check; the
proofs themselves live in the manuscript. Re-run:
`python3 verification/typed_false_positive_instantiation.py` from the
deposit root (stdlib only; ≈ 36 s; exit 0 iff all 25 pass).
