# Supplementary Material — SafeTransition: exact rational certification of transition safety for sustainability assessment

*Accompanies:* A. Abaee (2026). *SafeTransition: exact rational
certification of transition safety for sustainability assessment*
(manuscript v6, Environmental Modelling & Software submission).
Verification deposit: <https://doi.org/10.6084/m9.figshare.33764023>.

*Section references of the form "Section n" refer to the accompanying
manuscript; references S1–S9 are internal to this supplement. Package
version 1.2.1; all quantities are exact rationals unless stated as
rendering floats. Changes from the v1 supplement: S5 updated to the 1.2.0
artifact tree; S6 extended with the deposit's twelve-query record and
aligned with the manuscript's §5 comparison set; S9 added (certificate
protocol: serialization schema, independent checker, negative tests);
S10 added (scaling study, v1.2.1) and S5 updated to the 1.2.1 tree.*

---

## S1. The five assessment operators, as implemented

A typed transition datum consists of a phase state `z = (q, x, s1, ..., sn)`
(phase flag, fund coordinates, typed floors normalized to zero), a finite
action set, a disturbance set, an exact tube `Tube(a, d)` for each action
and disturbance (the set of states visited over the review period), a
transition-safe set `S`, and a destination set `G` reached under an
endpoint reset with gain vector `e`. Actions declare breakpoint offsets
together with an action-indexed worst-case disturbance; each tube is the
exact visited set (Section 2.1).

| Operator | Condition on each `(a, d)` | Destination test |
| --- | --- | --- |
| Typed, noncompensatory `E_typ` | `Tube(a,d) ⊆ {x ≥ 0, s_i ≥ 0 ∀i}` | successor in `G` |
| Scalarized aggregate `E_w` | `Tube(a,d) ⊆ {x ≥ 0, w·s ≥ 0}` | successor in `G`, `w·s ≥ 0` |
| Exact-tube physical `E_tube,phys` | `Tube(a,d) ⊆ {x ≥ 0}` | successor in `G_phys` |
| Endpoint-only physical `E_end` | endpoints in `{x ≥ 0}` | successor in `G_phys` |
| Typed-endpoint `E_end,typ` | endpoints in `S` | successor in `G` |

Because `End(a,d) ⊆ Tube(a,d)` and `S ⊆ S^w ⊆ S^phys`, the chain
`E_typ(z) ⊆ E_w(z) ⊆ E_tube,phys(z) ⊆ E_end(z)` holds at every state and
positive weight; `check_chain` verifies it exactly on request
(Section 3.3). The accepted-state set `V[E] = {z : E(z) ≠ ∅}` and the
compensatory accepted set `V_weak = ⋂_w V_w` follow; the witnessed
separation `V_typ ⊆ V_weak`, strict in general, is the formal statement of
what a composite index cannot see (Section 2.1).

## S2. The recursions

**Typed recursion.** On an explicit state–action graph, `W_1 = {z :
E_typ(z) ≠ ∅}` and `W_{k+1} = {z : some action keeps every visited state
safe and its successor lies in `W_k`}`. Polynomial in graph size and
horizon for constant-time predicates (Section 2.2).

**Belief-space recursion.** States carry observation labels `γ`; an
action is admissible for a belief `B` when no state in the fibre of `B`
enters a violation under it; the belief updates to the labels reachable
under the action. `W_k` denotes the k-step viable beliefs; the recursion
is sound and complete in finite systems. Beliefs in `W_1 \ W_2` exhibit
post-observation recourse failure — the demonstration instance of
Section 4.3 has the three-state system with root belief `{y12}`, which is
one-step viable and exits at the second step under every observation-based
policy.

## S3. The certificate family, with a worked derivation

For a stacked rational system `Au ≤ b`, Fourier–Motzkin elimination with
provenance tracking derives each row together with its multiplier vector
over the original rows. A derived contradiction `0 ≤ c, c < 0` yields,
after normalization, `λ ≥ 0` with `λᵀA = 0` and `λᵀb < 0`; the library
re-verifies both identities exactly before returning the certificate with
its infeasibility margin `−λᵀb > 0` (Section 2.3).

**Worked derivation (the stacked menu window of Section 4.3).** System:
`u ≤ 2/5` (row 1) and `−u ≤ −3/5` (row 2). Eliminating `u` combines the
rows with nonnegative multipliers: `1·(row 1) + 1·(row 2)` gives
`0 ≤ 2/5 − 3/5 = −1/5 < 0`, provenance `(1, 1)`. Normalizing the
provenance to a convex combination gives `λ = (1/2, 1/2)`; then
`λᵀA = (1/2)·1 + (1/2)·(−1) = 0` and `λᵢb = (1/2)(2/5) + (1/2)(−3/5) =
−1/10 < 0`. The certificate is returned with margin exactly `1/10`,
matching the infeasibility margin quoted in Section 4.3 and Table 2.

**Common-action obstruction.** Fires when the safe-action sets of
pairwise-compatible states intersect emptily while each is nonempty; a
minimal conflicting subfamily is reported (Section 2.3).

**Observation-fibre criterion.** An exact observation-only certifier
exists iff safe-set membership is constant on observation fibres; a
violating fibre is reported otherwise (Sections 2.3 and 4.3).

## S4. Complete enumeration of the twenty-four benchmark checks

The `benchmark` module re-derives every deposited value of the
resource-transition benchmark (Section 4.1; Schaefer realization with
`r = 4`, `K = 10`, `B_lim = 2`, `H_max = 13`, `δ0 = 1/2`). All twenty-four
pass; runtime under one second on a laptop CPU (Table 2):

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

Package 1.1.1 (Section 6; MIT; Python ≥ 3.9; no runtime dependencies):

```
safetransition/
├── pyproject.toml, LICENSE (MIT), CITATION.cff, README.md, CHANGELOG.md
├── check_safe_transition_cert.py   # independent stdlib-only certificate checker (S9)
├── run_all.sh                      # one-command fresh reproduction (7 steps)
├── SHA256SUMS                      # integrity manifest (51 entries)
├── benchmarks/                     # scaling study + committed full results (S10)
├── requirements-figures.txt        # pinned figure environment (optional)
├── dashboard.html                  # rendered single-file dashboard
├── docs/                           # submission plan; style notes
├── examples/                       # northern_cod_dashboard.py; partial_observation.py;
│                                   # certificates_demo.py (produce -> check -> tamper)
├── figure_code/                    # figure pipeline; graphical-abstract TIFF export
├── novelty_searches/               # related-software search records (S6)
├── src/safetransition/             # 9 modules, 1,633 lines
└── tests/                          # 46 tests, 621 lines
```

`sh run_all.sh` executes, in order: the test suite (46/46, including the
certificate-protocol, scaling closed-form, and provenance-determinism
tests), the exact benchmark checks (24/24), certificate emission plus the
independent checker over the emitted certificates, the three worked
examples (the certificates demo ends in tamper rejection), the quick
scaling sweep (writing a disposable results file; the committed full run
is never clobbered by a reproduction), and — when matplotlib/Pillow are
installed at the versions pinned in `requirements-figures.txt` (3.10.9
and 12.3.0) — figure regeneration (the benchmark figure via
`make_benchmark_v45.py`, from the library's verified schedule values),
including the graphical-abstract TIFF. A SHA256SUMS
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

## S8. Citation

- Abaee, A. (2026). *SafeTransition: exact rational certification of
  transition safety for sustainability assessment* (software description,
  EMS submission, v3).
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

Exit codes: 0 every certificate verified, 1 at least one rejected, 2
usage error.

**Negative tests.** The suite asserts rejection of (i) an altered bound
`b`, (ii) an altered multiplier vector `lam`, (iii) an altered system
matrix `A`, for Farkas certificates; the weight-partition checker is
exercised against an inconsistent licensed set; the benchmark checker
against a perturbed derived value (`1089/125` in place of `1088/125`).

**Tube-status semantics.** `TubeStatus ∈ {EXACT, CONSERVATIVE}`:
declared piecewise-linear plan tubes are EXACT (each equals the visited
set of its paths); the Schaefer realization's tubes are CONSERVATIVE
outer enclosures, certified by monotonicity of σ on the visited biomass
interval [6/5, 16/5] ⊂ (0, K/2) = (0, 5), giving σ ≥ σ(6/5) = 528/125 ≥ 4
on the recovery legs.

**Adversarial exactness instance.** The trough condition
49·(1/49) − 1 = 0 holds exactly (floor exactly met; the plan is licensed
in mode `w`), while binary floating point evaluates it to
−1.1102230246251565 × 10⁻¹⁶ (falsely unlicensed). 7·(1/7) is not an
instance: IEEE rounding yields exactly 1.0. The library rejects
floating-point input structurally, so the exact verdict is the only one
it can return.

**Belief failure witnesses.** `explain_belief_failure` returns, for a
non-viable root belief, the horizon of first failure and, per action,
either the fibre states entering a violation en route or the post-belief
that is not viable at the previous level; on the recourse-failure system
both actions fail with post-belief {y12, y4} not one-step viable. The
belief-enumeration bound is a parameter (default 4,096); exhaustion
raises with no partial results — exploration completeness is affected,
never the soundness of returned memberships.

## S10. Scaling study (package 1.2.1)

`benchmarks/scaling_study.py` sweeps five parameterized instance families
whose answers are known by construction and asserted at every size. The
committed full run (`benchmarks/scaling_results.json`; single core,
11.0 s total) reports, per instance: wall-clock runtime, peak traced
memory, eliminator rows generated and peak working rows, certificate JSON
size, maximal numerator/denominator bit lengths, reachable-belief counts,
and the independent checker's runtime. `--quick` runs a CI-sized sweep to
a disposable file; the committed full results are never clobbered by a
reproduction.

| Family (largest instance) | Known answer (asserted) | Largest-instance measurement |
| --- | --- | --- |
| FM chain, k = 256 (rows 257) | infeasible; margin (1/5 − 255/4096)/257 | 1.59 s; 256 rows generated; certificate 335 kB, 13-bit coefficients; checker 0.29 s |
| Dyadic growth, t = 320 | margin 2⁻³²⁰/(L+2) exactly | certified exactly; 321 certificate bits |
| Typed recursion, 21,000 states (horizon 20) | all states viable | 2.1 s; linear in states |
| Action menu, 512 actions | all admissible in all five modes | 2.5 s |
| Beliefs, m = 10 labels | exactly 2^m reachable beliefs | 1,024 enumerated; 0.59 s; default bound (4,096) reached at m = 12, exceeded at m = 13 → raises, no partial results |

Growth reading: elimination is quadratic in the planted instances and
terminates at the planted contradiction; the typed recursion is linear in
the state count; menu cost is linear in menu size; belief enumeration is
exponential in m, as the reachable set itself is. Coefficient growth
inflates certificate size (bit length grows linearly in t), not verdict
times. Closed forms (margin (1/5 − (k−1)/4096)/(k+1) for the chain;
2⁻ᵗ/(L+2) for the dyadic family) are asserted at every swept size, and
re-asserted on small instances in the unit suite (46 tests).
