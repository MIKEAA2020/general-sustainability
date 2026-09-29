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
| minimax duals | `fam/minimax_v11.tex` | 41 KiB | `minimax_dual_certificates`, `certificate_duality` | **A** (fold in) |
| P1 separation | `fam/arv_v9.tex` | 45 KiB | acceptance-gap geometry | **A** (fold in) |
| **P5 sample-and-hold** | `fam/p5_v47.tex` | 131 KiB | review interval as a stability variable | **B** (core) |
| **P4 governance delay** | `fam/p4_v41.tex` | 190 KiB | delay from observed decline to response | **B** (core) |
| **E2 cod intervention** | `.../paperE2_cod_intervention_v29.tex` | 110 KiB | viability kernels + certified horizon on a real record | **B** (core, applied half) |
| ARV applied regime | `.../applied_regime_viability_v9.tex` | 45 KiB | the same cod record, exact rational arithmetic | **B** (evidence) |
| **P3 typed ledgers** | `fam/p3_v32.tex` | 163 KiB | what depletion diagnostics can certify | **C** (core) |
| **E3 Edwards forecast** | `fam/e3_v16.tex` | 65 KiB | null result: benchmarks beat process models | **C** (lead with it) |
| E1 baselines | `fam/e1_v60.tex` | 137 KiB | case study | **C** (evidence) |
| E4 elevation | `fam/e4_v15.tex` | 61 KiB | case study | **C** (evidence) |
| welfare/support | `fam/ws_v17.tex` | 73 KiB | supporting | **C** (evidence) |

Two further `.tex` lines (`e2_v23`, `e2/paperE2..._v28`) are superseded and E2 v28 is
explicitly **never a base** — its verification scripts pin the hybrid convention.

---

## 2. The spine of Paper B (and the one thing to get right)

Two independent objects put a review-interval boundary at essentially the same place:

* **P5** (sample-and-hold governance, an illustrative baseline): the exact map crosses
  once, near a **6.5-year** review interval; one-step approximations report artefact
  crossings.
* **E2** (Northern cod, frozen protocol, committed kernel computation): the certified
  horizon is **6 years** under the two harsher floors and **7** under the informative
  one — and it is 6/6/7 for *every* admissible catch, including none at all.

Same neighbourhood, arrived at from opposite directions: P5 asks at what review interval
a managed loop loses stability; E2 asks over what horizon a robustness certificate for a
reference point remains valid. If those are two faces of one quantity, Paper B has a
headline no reviewer can miss, because the theory and the certification agree.

**They are not yet shown to be the same quantity, and the paper must not imply it until
they are.** P5's crossing is a stability boundary in review-interval space for a
sample-and-hold operator; E2's horizon is the crossing at which a geometrically growing
erosion margin overtakes the worst-case trajectory. The first job on Paper B is to settle
this: either derive the link, or state plainly that the numerical proximity is a
coincidence of two different objects and keep the two results in separate sections.

Everything else in Paper B is easier than this, and this decides the headline.

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
  other ~330 `.tex` files out of the submission tree. Note the standing constraint from
  earlier in this session: archive, do not delete — the working set is needed until all
  three papers are built.
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

**Resolved 2026-09-29:** all three papers go to **preprints.org**, and length is not a
constraint. The consequence for Paper B is that it can be assembled at full length rather
than compressed, and the supplement can carry the derivations rather than being a
compressed remnant of them. The one thing that still has to be *decided* rather than
*fitted* is the headline (§2 above).
