# Paper 3 — GPT audit completion report v2 (2026-09-20)

Status of the GPT EMS novelty-audit items after the v6/1.2.1 round.
Companion to `paper3_gpt_audit_verification_v1.md` (v5/1.2.0 round:
1 claim refuted, certificate protocol + weight partition + tube status +
adversarial instance + §5 comparison implemented). All v1 verdicts stand;
this report covers what remained.

## Implemented in this round (v6 paper / 1.2.1 package)

| Audit item | Status | Where |
| --- | --- | --- |
| **Item 10 — "benchmark too small; add parameterized family with independent generation rules and known answers; report runtime, peak memory, FM rows, certificate size, bit lengths, checker runtime"** | **Implemented in full.** `benchmarks/scaling_study.py`: five families (FM chain, dyadic bit growth, typed recursion, action menus, belief spaces) with answers known by construction and asserted at every size; all requested metrics recorded; committed full run (11 s, `scaling_results.json`). Varying floor *count* is out of scope for the 2-floor interface and is stated as such (below). | Paper §3.5 + Table 2; package `benchmarks/`; tests assert the closed forms on small instances |
| Adversarial near-degenerate instance | Implemented in the v5 round (n = 49); the dyadic family (t = 320) extends it with continuous coefficient growth | §3.2, §3.5 |
| **§4.2 — dashboard should embed certificate hashes, library version, datum identifier, exact input serialization, checker version, verification status, re-run command; treat dashboard as audit-delivery mechanism** | **Implemented in full.** `default_provenance()` + provenance table in the dashboard; deterministic rendering (no timestamps → byte-identical re-render, checkable hashes). | Paper §4.2; package `dashboard.py`; determinism tested |
| **§4.3 — formal mapping between the common-action obstruction, the stacked system, rows of A/b, and the states/actions each row represents** | **Implemented.** Row-explicit mapping paragraph (rows = per-state menu restrictions; equal multipliers; obstruction verdict = certified infeasibility); row-mapping test in the suite. | Paper §4.3; tests |
| Conclusion — "closes a practical gap" only after independent checking + broader benchmarks + comparison | **Restored with justification.** All three prerequisites now exist; v6 §6: "closes this practical gap within its stated scope". | Paper §6 |
| Certificate language coverage (strongest option: action admissibility, tube extrema, licensing, Farkas, obstruction, belief viability, fibre violations) | **Substantially implemented across the two rounds.** Certificate types now serialized and independently checked: Farkas (v5), weight partition/licensing (v5), benchmark + tube enclosure (v5); dashboard binds hashes + re-run command (this round). Not serialized: obstruction conflicts and fibre violations (reported as data structures, not checker-verified objects) — listed below as remaining. | — |
| Second strongest option (exact weight-cone partition, completeness) | **Implemented in the v5 round**, including the three-regime generic partition; completeness argument rests on closed trough conditions | §4.3; S9 |
| gemini 1C follow-up (fund axis ambiguity, previously "noted") | **Fixed.** `make_benchmark_v45.py`: fund legend entry, coloured right-axis label, STAGED entry names the plotted quota; figure regenerated from library values with equality tested — the figure provenance is now a test invariant. | Fig. 1 caption; package `figure_code/` |

## Deliberately out of scope (documented, not silently dropped)

- **Floor-count variation in the scaling study.** The operator interface
  is two-floor by design (the scalarizing aggregate and the witnessed
  separation are two-floor constructions); the paper's scope statement
  says so. Generalizing to n floors is an interface change, not a
  benchmark variant, and is listed under future work.
- **Obstruction and fibre certificates as serialized, checker-verified
  objects.** These two verdicts remain rich data structures (minimal
  conflict, violating fibre) rather than `"type": ...` documents. The
  certificate language of the strongest option therefore covers four of
  six verdict families; extension hooks (schema versioning,
  `CHECKER_VERSION`) are in place.
- **Third strongest option (policy trees / counterexample trees).**
  Partially covered: `explain_belief_failure` returns per-action failure
  witnesses with post-beliefs (v5), but full policy trees are not
  emitted. Future work.

## Post-round QA

Paper v6: 11 pp, exit 0, 0 `??`, abstract exactly 150 words, overfull
baseline only, scaling table verified visually. Package 1.2.1: 46/46
tests; run_all.sh 7/7; SHA256SUMS 51; committed full scaling run
regenerated and committed.
