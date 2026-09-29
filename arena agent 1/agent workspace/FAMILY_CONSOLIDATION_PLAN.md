# Family consolidation: fifteen manuscripts → three papers

**Status.** Working plan, drafted from the branch inventory and the abstracts of the
lead manuscripts. The 3-paper architecture is the recommendation already on record in
`arena agent 1/agent workspace/family_strategy_assessment.md`; this document turns it
into a build order with the state of every component checked against the branch today.

---

## 0. What changed since that recommendation

Item 1 of its sequenced actions was **"fix E2 first"**. That is done:

| E2 verification | state |
|---|---|
| battery (`paperE2_cod_intervention_v29_verification.py`) | **380 checks, 0 failed** |
| mutation harness (`..._sabotage.py`) | **124 mutations, 0 holes** |
| basis audit (`..._basis_audit.py`) | **187 declared numbers, 0 on the v2 basis, 0 unprinted** |
| compile | real tectonic, **28 pages, 10 figures, 8 tables** |

And E2 has since grown the result that most matters to Paper B: the certified horizon is
6/6/7 years for every admissible catch and every declared rule, and **no policy lengthens
it** — Table 2, Figure 10, and the Discussion consequence against two real institutional
cadences. E2 is no longer the weakest link; it is the strongest asset in the family.

---

## 1. Inventory: what exists, at what version, where it goes

Sizes are the branch copies, fetched today. "Lead" = the version to build from.

| manuscript | file | size | role | → paper |
|---|---|---|---|---|
| **P2 obstruction** | `fam/obstr_v55.tex` | 143 KiB | obstruction certificates; the necessity direction | **A** (core) |
| minimax duals | `fam/minimax_v11.tex` | 41 KiB | `minimax_dual_certificates`, `certificate_duality` | **A** (fold in) — `minimax_dual_certificates_v12` is one version on; diff before use |
| **P1 separation** | `paper rewrites/latex/paper1_assessment_separation_v63.tex` | **194 KiB** | quantifier-order separation, scalarized vs coordinate-wise (42 sections, 30.6k words) | **A** (Supplement S1 in full) |
| **P5 sample-and-hold** | `fam/p5_v47.tex` | 131 KiB | review interval as a stability variable | **B** (core) |
| **P4 governance delay** | `fam/p4_v41.tex` | 190 KiB | delay from observed decline to response | **B** (core) |
| **E2 cod intervention** | `.../paperE2_cod_intervention_v29.tex` | 110 KiB | viability kernels + certified horizon on a real record | **B** (core, applied half) |
| ARV applied regime | `.../applied_regime_viability_v9.tex` | 45 KiB | the same cod record, exact rational arithmetic | **B** (evidence) — **this file is byte-identical in content to `fam/arv_v9.tex`** (same title, 7,256 words). The old "P1 = arv_v9" mapping was a duplicate of this slot |
| **P3 typed ledgers** | `fam/p3_v32.tex` | 163 KiB | what depletion diagnostics can certify | **C** (core) — **build from `paper3_material_ledgers_v50` (229 KiB, 36,387 words): same title, 40% more content** |
| **E3 Edwards forecast** | `fam/e3_v16.tex` | 65 KiB | null result: benchmarks beat process models | **C** (lead with it) — `paperE3_edwards_forecast_ladder_v17` is one version on; diff before use |
| E1 baselines | `fam/e1_v60.tex` | 137 KiB | case study | **C** (evidence) |
| E4 elevation | `fam/e4_v15.tex` | 61 KiB | case study | **C** (evidence) — `paperE4_edwards_intervention_v16` is one version on; diff before use |
| welfare/support | `fam/ws_v17.tex` | 73 KiB | supporting | **C** (evidence) |

Two further `.tex` lines (`e2_v23`, `e2/paperE2..._v28`) are superseded and E2 v28 is
explicitly **never a base** — its verification scripts pin the hybrid convention.

---

## 2. The P5/E2 relation — settled 2026-09-29, and the answer is no

**The two are not the same quantity, and the numerical proximity is a coincidence.
Paper B must not imply a link. The firm reason, as opposed to mere caution, is that the
two results point in *opposite directions*: a conflated claim would be contradicted by
one of the two papers it rests on.**

### 2.1 What each object actually is

| | **P5** (`p5_v47`, sampled governance) | **E2** (Northern cod, frozen protocol) |
|---|---|---|
| system | illustrative logistic hold map: `r = 0.02 /yr`, `K = 100`, `q = 0.001`, measurement averaging `t_m = 5 yr` | Northern cod 2J3KL, Schaefer; committed fit `r = 0.2369 /yr`, `K = 5000 kt` (pinned), `K* = 884.6 kt` |
| object | closed-loop **stability boundary**: the review interval at which the sampled map's monodromy leaves the unit circle | open-loop **certification horizon**: the last horizon at which a worst-case certificate holds |
| event | a complex pair crosses the unit circle — a Neimark–Sacker bifurcation (nonlinear nondegeneracy *not* verified) | the inequality `F^T(S_hi) ≥ K* + r_T` becomes false |
| mechanism | the **institutional loop** — effort response and measurement averaging. The resource is nearly static: `A_N = −0.0179` | the **resource's expansion** — `a_max = F'(K*) = 1 + r(1 − 2K*/K) = 1.1531`, with defect `ε = 328.97 kt` accumulating as `r_T = ε(a^T−1)/(a−1)` |
| scale | set by `t_m = 5 yr` and the effort gains | set by `1/ln(a_max) = 7.0 yr` |
| direction | **lower bound**: unstable for `T_r < 6.501`, stable on `[6.501, 200]` yr | **upper bound**: certifiable only for `T ≤ 6` (worst class) / `T ≤ 7` (informative) |
| longer is | **stabilising** | **certificate-failing** |

(`r = 0.2369 /yr` is recovered two ways from the committed fit — from `F'(K*)` and from
`g(K*) = 172.46` — agreeing to four decimals.)

Two mechanisms, two systems, and two inequalities running opposite ways. Longer review
intervals stabilise P5's loop and destroy E2's certificate.

### 2.2 Why the near-agreement looked like a result — root cause

1. **The headline was written before the check.** This plan said: *"If those are two
   faces of one quantity, Paper B has a headline no reviewer can miss."* That is a
   conclusion stated as an aspiration, attached to a comparison nobody had performed. The
   incentive to confirm it was structural, and it survived an entire drafting cycle
   unchallenged.
2. **It is a selection from a four-entry record.** P5's crossing record is `2.306`
   (protective, Euler), `6.501` (mobilising, exact), `47.536` and `79.143` (mobilising,
   Euler). Two of the four are explicitly **artefacts of the forward-Euler command
   step**, and the protective-exact channel has **no crossing at all**. The "agreement"
   is with one of four crossings, chosen after the fact.
3. **The systems are not comparable.** Cod `r = 0.2369 /yr` against P5's `r = 0.02 /yr`
   — a factor of **11.8** — and cod `K = 5000 kt` against P5's `K = 100` dimensionless.
   No shared parameter could make the two numbers track each other.
4. **The dominant term is different.** E2's clock is the resource expanding; P5's clock
   is an institutional measurement window against a resource whose own linearisation is
   already stable.
5. **The directions are opposite.** This is the disproof, not a caveat.

### 2.3 The claim the conflation would make, and why it is not available

Were both computed on one system, the two constraints would intersect in `[6.501, 7]` yr
— a **half-year window** — and be **empty** under E2's worst residual class
(`T* = 6 < 6.501`). That is a striking thing to be able to say, which is precisely why it
must not be said on this evidence: it is a cross-system inference between systems whose
growth rates differ by 11.8×. Any reviewer who checks the parameters finds the window is
an artefact of comparing a cod stock to an illustrative baseline.

### 2.4 The decisive experiment — what actually settles it

The question cannot be settled by comparing published numbers across two different
systems. It requires both objects on **one** system, and both sides have archived,
runnable code:

* **P5:** `arena agent 1/other documents/rerun_campaigns/campaign_p5_crossing_scan.py`.
  Committed validation gate: protective Euler `ρ(1) = 0.9838`, crossing `2.306`;
  mobilising Euler `ρ(1) = 1.00055`, crossings `47.536` / `79.143`; mobilising exact
  `ρ(1) = 1.00035`, single crossing ≈ `6.5`; protective exact stable throughout
  (max `ρ = 0.9967` on `[0.2, 120]`).
* **E2:** `wave_e_cod/src/campaign_e2_cadence_v3.py`.

**Do this.** Calibrate P5's effort/hold model to the cod record and re-run the crossing
scan on cod parameters, then compare the resulting `T_r^UC` with E2's `T* = 6/6/7` on the
same stock. The work is the mapping: E2 is a surplus-production model in catch, P5 is an
effort model with `C = qEN`, so `q` and `E_max` must be fitted to the cod catch and
biomass series before the scan means anything.

* If the cod-calibrated crossing **also** lands near 6–7 yr, there is something real to
  explain — and the opposite directions then make it a genuine, publishable **tension**:
  a feasible window of about half a year, or none.
* If it lands elsewhere, which the 11.8× rate difference makes likely, the matter is
  closed and the two results are reported separately with no link claimed.

Until that run exists, Paper B carries **no** claim linking them.

### 2.5 What Paper B's headline becomes

The near-match is not available as a headline. What survives is the family's own claim,
carried by P5 alone and by E2's cadence consequence, without the coincidence:

> What decides whether management stabilises or destabilises a renewable resource is not
> biology alone but the decision clock.

Whether a second clause — that certification cannot see past ~6–7 years while a
sampled-and-held loop is unstable when reviewed more often than ~6.5 — belongs in the
headline is exactly what §2.4 decides.

---

## 3. Paper A — theory

**Working title.** *Obstruction certificates for viability under incomplete observation*
**Venues.** *Automatica*, *SIAM J. Control & Optimization*, *Math. Control Signals Systems*
**Core.** P2; fold in P1's gap geometry, `finite_horizon_completeness`, minimax dual
certificates, certificate duality. One question: *when can you certify that no
observation-based policy works?*

Gaps, in order:

1. **Prior art first, before any other writing.** The assessment is explicit that this
   decides whether the novelty claim survives: HJ reachability and viscosity
   characterisations, Pontryagin-style backward procedures and contingent-cone
   conditions, differential-inclusion capture basins, and Veliov's output-feedback
   regulation condition for the sufficiency direction. Write this section before the
   results section.
2. **At least one worked case where a certificate bites on a system whose kernel cannot
   be computed.** Without it the instrument is unfalsified in the regime that motivates
   it.
3. Decide what of P1 survives the fold. "Common-plan acceptance and per-weight acceptance
   do not commute" sits close to known robust-optimisation and MCDM separation results;
   it either carries an aggressive prior-art paragraph or it does not go in.

---

## 4. Paper B — mechanism + evidence

**Working title.** *The decision clock: how review timing and response delay determine
resource stability*
**Venue.** **preprints.org first**, journal submission derived from it afterwards.
**Length is not a constraint** — do not compress for a word budget. This retires the
`cut the math density hard` instruction from the original assessment: it was advice for a
NatSustain word limit that no longer applies. Keep the figures and the mechanism clear
because clarity is worth having, not because space is short.
**Core.** P5 (sample-and-hold) + P4 (governance delay) + E2 and ARV (the cod
certification). The assessment's reasoning for merging: these are two halves of one idea.

Headline, stated positively and not as a caveat:

> What decides whether management stabilises or destabilises a renewable resource is not
> biology but the decision clock. Across 42 stocks and 32 cross-sector systems,
> periodicity alone cannot diagnose governance feedback.

Gaps, in order:

1. **Settle the P5/E2 question** (§2 above). This is the headline, not a detail.
2. **Promote the null result.** P5's multiplicity-controlled screen of 42 stocks finds no
   robust institutional cycles, and the 32-system cross-sector search finds no
   unconfounded oscillator. Currently framed as a limitation. Well-framed null results
   are publishable at this level; buried ones are not. It belongs in the abstract.
3. **Put the mechanism in two or three figures.** E2's Figure 10 is the model: one glance,
   no notation. Figure plan: (i) review interval → stability, from P5; (ii) governance
   delay → the stabilising window, from P4; (iii) the certified horizon against catch,
   from E2. No figure budget to respect.
4. **Make the policy variable actionable.** The practitioner literature shows cadence is a
   live, varying institutional choice — annual, biennial, three-year, five-year, six-year.
   E2's Discussion already names two real ones: the IWC's six-year implementation reviews
   and aboriginal subsistence strike limits set in six-year blocks, and NOAA's
   management-track assessments. That is the hook, and it needs a table of real cadences
   against the horizon each one has to sit inside.
5. **Reconcile E2 and ARV.** Both read the same cod record; E2 in floating point with a
   declared catch-timing convention, ARV in exact rational arithmetic with a
   harvest-free multiplier bracket. Paper B must say why there are two treatments of one
   record and what each certifies — or absorb one into the other.

---

## 5. Paper C — measurement

**Working title.** *What depletion numbers can and cannot certify*
**Venues.** *Ecological Economics*, *Environmental Research Letters*, *PNAS Nexus*
**Core.** P3 (typed ledgers) + E1, E3, E4.

Gaps, in order:

1. **Lead with E3's null result.** On a locked retention rule, simple benchmarks beat
   deliberately simple process-based models (persistence 13.23 ft vs. the one-pool
   stock-flow map at 14.70 ft at one year). E3 currently reports this honestly and
   quietly; Paper C should open with it.
2. P3's contribution is a typology — "three diagnostics are widely misread". As a
   top-journal contribution that is a clarification unless it is tied to a measurable
   consequence. Tie it to one.
3. E1 and E4 are evidence for the claim, not claims. Demote them to a section each.

---

## 6. Cross-cutting, from the assessment

* **Freeze and prune.** One clean manuscript plus one supplement per paper; archive the
  other `.tex` files out of the submission tree. **The count is ~430 files in 79 families,
  not ~330** (audited 2026-09-29). Note the standing constraint from earlier in this
  session: **archive, do not delete** — the working set is needed until all three papers
  are built. Pruning is currently unsafe: see `CONSOLIDATION_AUDIT.md`, which lists 618 KiB
  of `revised_articles/A0xx` modules and a 582 KiB theory manuscript that no paper is
  mapped to.
* **Demote the verification apparatus.** The batteries, sabotage harnesses and
  "reproduced to nine significant figures" claims certify that a manuscript matches its
  own archive. That is reproducibility engineering and it belongs in a reproducibility
  statement, not in the argument. The assessment's evidence for demoting it is the same
  lesson E2 learned the hard way: a battery can be green while the table it guards is
  wrong.
* **Each paper needs one unmistakable headline** answerable in a sentence before a
  referee reads any mathematics.

---

## 7. Build order

1. **E2** — done. Frozen at v29, on `e2-v3-source-year`.
2. **Paper B next.** It is where the strongest asset already sits, its headline is the
   most citable thing in the family, and its two halves (P5, E2) are already in the same
   numerical neighbourhood. Start by settling §2, not by drafting.
3. **Paper C.** Cheapest to assemble: the null result is written and the evidence is
   frozen.
4. **Paper A last.** It carries the prior-art risk, and the prior-art section determines
   whether the paper exists at all. Writing it first, before any other part of A, is the
   assessment's instruction and it is the right one.

**Audited 2026-09-29:** see `CONSOLIDATION_AUDIT.md`. Of the 16 concrete items in this
plan, one is closed (E2). The audit found a mapping error (the P1 slot named a file that
is a duplicate of the ARV slot, leaving the real 194 KiB separation paper unmapped),
five leads that lag their families, and 618 KiB of modules mapped to no paper.

**Resolved 2026-09-29:** all three papers go to **preprints.org**, and length is not a
constraint. The consequence for Paper B is that it can be assembled at full length rather
than compressed, and the supplement can carry the derivations rather than being a
compressed remnant of them. The one thing that still has to be *decided* rather than
*fitted* is the headline (§2 above).

## Resolved 2026-09-29 (v29o): profile vs bootstrap intervals in the abstract

The abstract carried the profile range [67.9, 95.2] (width 27.3, excludes zero)
and the bootstrap interval [-89.4, 125.7] (width 215.0, includes zero) for the
same quantity without saying why they disagree by ~8x or which one the paper's
claim rests on. Resolved by (i) presenting the profile range as an
identification result and explicitly not a precision one, and (ii) a paragraph
in 3.10 explaining the disagreement. The gap is NOT the 7.4% of replicates
whose refit puts K below the reference point: the bootstrap is wider at both
ends (35 kt above the profile ceiling, 74 kt below its floor) even after
restricting to the expansive regime.

Guard: R26 in v29_battery.py registers every numeric token in the abstract (19
quantities recomputed from the archive, 10 structural). A number added to the
abstract without provenance now fails the battery. R25i/R25j pin the body's own
bootstrap sentences, which were previously unpinned.
