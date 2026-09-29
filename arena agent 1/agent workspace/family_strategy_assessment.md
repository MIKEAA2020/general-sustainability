# Do the family papers meet the top-journal bar?

**Basis.** Abstracts of the seven current lead manuscripts (fetched from `lean-audit-v4`),
the file inventory (341 `.tex` files), a literature probe on the two novelty claims, and the
audit work already done on E2, P4 and P5. I have not read the 190 KB P1/P4 bodies in full —
this is an assessment of framing, contribution and submission risk, not a line-by-line review.

---

## Short answer

**Not as currently constituted — but the raw material is better than the packaging.**

There are two genuinely publishable ideas in the family, and roughly ten manuscripts
wrapped around them. No single paper currently has one unmistakable headline, and top
journals reject on "what, exactly, is the contribution?" before they read a line of the math.

The two real ideas:

1. **Obstruction certificates** (P2) — certifying that *no* observation-based policy is
   viable, the necessity direction that complements the viability kernel.
2. **The decision clock** (P4 + P5) — that what determines stability in a managed
   renewable resource is not the biology but the *timing and form of policy revision*.

Everything else is supporting material that is currently dressed as standalone papers.

---

## The two novelty claims, tested

**P2 — obstruction / non-viability certificates.** This gap is real. The literature I
probed is overwhelmingly about *computing* the kernel — Hamilton–Jacobi reachability and
viscosity characterisations [1](https://arxiv.org/html/2510.11396), Pontryagin-style
backward procedures and contingent-cone conditions [2](https://dx.doi.org/10.3390/math2020068),
differential-inclusion capture basins [3](https://www.researchgate.net/publication/224740078_Viability_kernels_and_capture_basins_of_sets_under_differential_inclusions).
Sufficiency has a canonical answer (Veliov's output-feedback regulation condition).
The systematic *necessity* direction is comparatively thin. **Genuine methodological
development.**

**P4/P5 — review cadence as a stability variable.** The theory literature does not treat
assessment cadence as a stability-determining design variable. The practitioner literature
treats it as administration: NOAA runs management-track assessments twice a year
[1](https://www.fisheries.noaa.gov/new-england-mid-atlantic/population-assessments/management-track-stock-assessments),
MMPA stock assessment reports are reviewed annually for strategic stocks and at least every
three years otherwise [5](https://www.fisheries.noaa.gov/s3/2023-05/02-204-01-Final-GAMMS-IV-Revisions-clean-1-kdr.pdf),
and the IWC's Revised Management Procedure sets catch levels over five-year periods with an
explicit rule on *timing of reviews*
[2](https://www.fao.org/4/v8400e/V8400E09.htm). Cadence is a live, varying institutional
choice that nobody has modelled as a stability parameter. **Genuine applied contribution
of broad practical interest.**

---

## What is below the bar

| Paper | Assessment |
|---|---|
| **P3** material ledgers | Careful, correct, and reads as accounting hygiene. "Three diagnostics are widely misread" is a valuable clarification, but as a top-journal contribution it is a typology, not a novel result. |
| **E3** Edwards forecast ladder | A clean benchmarking study with an honest negative result (persistence and AR(1) are hard to beat; the one-pool balance nowcasts rather than forecasts). Useful; but single-system benchmarking rarely clears a top-journal novelty bar on its own. |
| **E1 / E2 / E4** | Single-system case studies carrying a large theoretical load. Strong as *evidence for* Papers A–C; weak as standalone submissions. |
| **P1** assessment separation | The acceptance-gap geometry is elegant. Risk: "common-plan acceptance and per-weight acceptance do not commute" sits close to known robust-optimisation and MCDM separation results. Needs an explicit, aggressive prior-art section or it reads as a rediscovery. |

## The structural problems — these matter more than any single paper

**1. Fragmentation.** 341 `.tex` files; ~15 distinct manuscripts; version numbers reaching
v63 (P1), v56 (P2), v47 (P5), v60 (E1). A referee handed this family cannot answer "what is
the contribution?". This is the single biggest obstacle.

**2. The best findings are buried as caveats.** Two results are the most generalisable and
most citable things in the whole family, and both are framed as limitations:
- P5: a multiplicity-controlled screen of **42 stocks finds no robust institutional cycles**,
  and a 32-system cross-sector search finds no unconfounded oscillator.
- E3: simple benchmarks beat deliberately simple process-based models.

Well-framed null results are publishable in top journals. Buried ones are not.

**3. The verification apparatus is inward-facing.** The batteries, sabotage tests and
"reproduced to nine significant figures" claims certify that the manuscript matches *its own
archive*. That is reproducibility engineering, and it is genuinely good. It is not scientific
validation, and a referee does not care about it. **Demote it to a reproducibility
statement.** Evidence it is not validation: E2's battery is green at 83/83 while Table 1
disagrees with the deposited result file on 24 of 30 cells.

**4. Live correctness risk.** E2 as pushed (`c2fe8fc`) has a bifurcated numeric layer: the
prose uses the Schaefer disturbance classes, while Table 1, Table 3 and four of seven
figures use superseded Fox/`results_srcyear` values; the vacuity claims in nine places are
now false; and Table 1 is generated by a different runner from the one that produced the
deposited result file, while its three Family A/B rows are printed by a script that writes no
archive. A referee who checks one table against the deposited data and finds it contradicts
will distrust all of them. A family is judged by its weakest link.

> **Correction.** I first reported the Family A/B rows as unreproducible. That was wrong —
> I had grepped a subdirectory, not the repository. They are generated by
> `wave_e_cod/src/run_v15b_existing.py` and reproduce exactly. The real defect is that the
> script archives nothing, and that it runs on the superseded source-year basis. See
> `family_audit_v53_e2_class_bifurcation.md`.

---

## Concrete plan: consolidate fifteen manuscripts into three

### Paper A — theory
**"Obstruction certificates for viability under incomplete observation"**
→ *Automatica*, *SIAM J. Control & Optimization*, or *Math. Control Signals Systems*

Core: P2. Fold in P1's gap geometry, `finite_horizon_completeness`, `minimax_dual_certificates`,
`certificate_duality`. One question: *when can you certify that no observation-based policy works?*
Must include: a hard prior-art section against HJ reachability and contingent-cone methods,
and at least one worked case where a certificate bites on a system where the kernel cannot
be computed.

### Paper B — mechanism + evidence
**"The decision clock: how review timing and response delay determine resource stability"**
→ *Nature Sustainability*, *PNAS*, or *Nature Communications*

Core: P5 (sample-and-hold) **+** P4 (governance delay) **+** `applied_regime_viability` (the
cod certification). These are two halves of one idea and should not be separate papers.
Headline — stated positively, not as a caveat:
> What decides whether management stabilises or destabilises a renewable resource is not
> biology but the decision clock. Across 42 stocks and 32 cross-sector systems, periodicity
> alone cannot diagnose governance feedback.

For a NatSustain-calibre venue: cut the math density hard, put the mechanism in two or three
figures, and make the policy variable explicit and actionable. The practitioner literature
shows assessment cadence is a real, varying institutional choice — annual, biennial,
three-year, five-year. That is your hook.

### Paper C — measurement
**"What depletion numbers can and cannot certify"**
→ *Ecological Economics*, *Environmental Research Letters*, or *PNAS Nexus*

Core: P3 (typed ledgers) **+** E1–E4. Headline: three public-data diagnostics in wide use
are read as depletion forecasts but measure different things; on locked protocols, simple
benchmarks beat simple process models; assessment records support certification only under
explicitly stated conventions. Lead with E3's null result.

---

## Sequenced actions

1. **Fix E2 first.** It is the weakest link and the one I can verify today: vacuity rewrite
   (9 sites), Table 1, Table 3, four figures, the "seven years" slip, and the false
   Data-availability claim.
2. **Freeze and prune.** One clean manuscript plus one supplement per paper. Archive the
   other ~330 `.tex` files out of the submission tree.
3. **Promote the null results** to the headline in Papers B and C.
4. **Demote verification** to a reproducibility statement — keep the machinery, drop the
   implication that it validates the science.
5. **Write the prior-art section for Paper A** before anything else in that paper; it
   determines whether the novelty claim survives.

I can start on (1) now, or draft the consolidation outline for any of Papers A–C.
