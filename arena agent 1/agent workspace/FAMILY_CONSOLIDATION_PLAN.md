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

### 1.1 Disposition of the eight venue-assigned papers — 2026-09-29

The family was originally presented as eight papers each carrying its own venue:
`obstr` (Automatica, Regular), `comp` (SIAM J. Optimization), `ws` (Systems & Control
Letters), `minimax` (Mathematics of OR), `ebc` (Automatica, Technical Communiqué), `arv`
(CJFAS), `e1` (Int. J. Forecasting), `psuff` (IEEE TAC). The inventory above did not
account for three of them. They are identified here by stem from the full repo tree
(135 distinct stems searched).

| given as | identified file | venue | → paper |
|---|---|---|---|
| `obstr` | `fam/obstr_v55.tex` | Automatica, Regular | **A** (core) |
| `minimax` | `fam/minimax_v11.tex` | Math. OR | **A** (fold in) |
| `comp` | `paper2_computational_certification_v9.tex` | SIAM J. Optimization | **A** (companion) |
| `ebc` | `paper2_exact_belief_computation_v9.tex` | Automatica, Tech. Communiqué | **A** (companion) |
| `psuff` | `paper2_probabilistic_sufficiency_v9.tex` | IEEE TAC | **A** (companion) |
| `arv` | `fam/arv_v9.tex` | CJFAS | **B** (evidence) |
| `e1` | `fam/e1_v60.tex` | Int. J. Forecasting | **C** (evidence) |
| `ws` | `fam/ws_v17.tex` | Systems & Control Letters | **C** (evidence) |

**Consequence.** **Five of the eight venue-assigned papers are the P2 obstruction
programme**, split across five venues: the core plus four companions (minimax duals,
computational certification, exact belief computation, probabilistic sufficiency). The
3-paper architecture folds all five into Paper A. That is the largest single consolidation
move in the plan, and it is the one that most needs a decision the plan does not record:
whether those four companions submit separately to their named venues, or are absorbed
into Paper A and their venues surrendered.

**Confidence.** `comp` and `psuff` are high confidence — the stems match the given names.
`ebc` is **moderate**: no file is named `ebc*`, and `paper2_exact_belief_computation` is
the only stem whose initials fit an Automatica Technical Communiqué slot. Confirm before
acting on it.

**Root cause of the omission.** The inventory was built from the `fam/` directory plus a
few known paths. The four P2 companions live in `paper rewrites/latex/` under
`paper2_*` names and were never enumerated, so they were invisible to a plan built by
listing `fam/`. Any future inventory must enumerate the whole tree, not one directory.

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

### 2.4 The decisive experiment — RUN 2026-09-29, and it answers no

P5's crossing scan was transcribed from
`arena agent 1/other documents/rerun_campaigns/campaign_p5_crossing_scan.py`
into `p5_cod_transport.py`, re-run on P5's baseline, then re-run on cod biology
with the institutional parameters (`eta`, `Emax`, `dref`, `d0`, `tm`, `Zref`,
`delta`) **held fixed**, so only the biology moves.

**Validation gate passed first** — the transcription reproduces P5's committed
record before any new number was allowed to count:

| committed | reproduced |
|---|---|
| mobilising exact, single crossing ≈ 6.5 | **6.5013** |
| mobilising Euler, crossings 47.536 / 79.143 | **47.5360 / 79.1427** |
| protective Euler, crossing 2.306 | **2.3064** |
| protective exact, stable throughout | **no crossing on [0.05, 200]** |

**Then cod** (`r = 0.2369 /yr`, `K = 5000 kt`; `q` recalibrated to place the
equilibrium):

| transport | exploitation `N*/K` | mobilising-exact crossing | `rho(1)` |
|---|---|---|---|
| P5 baseline (`r = 0.02`) | 0.8955 | **6.50 yr** | 1.0004 |
| cod, equilibrium at the LRP (884.6 kt) | 0.1769 | **175.51 yr** | 14.36 |
| cod, P5's exploitation ratio held | 0.8955 | **42.44 yr** | 8.98 |
| cod, `q` left at P5's value | 0.9912 | **26.62 yr** | 1.92 |
| cod at P5's own biomass scale (`K = 100`), ratio held | 0.8955 | **17.50 yr** | 1.179 |
| cod at P5's own biomass scale, at the LRP | 0.1769 | **82.00 yr** | 1.469 |

**Every transport puts the crossing at 17.5 yr or beyond** — 2.7× to 27× away
from 6.5. The crossing is `unstable -> stable` in every one of them, so it is a
*lower* bound throughout: on cod biology P5's loop is unstable for all review
intervals below ~17.5 yr, while E2's certificate expires at 6–7 yr.

**The near-agreement is therefore an artefact of comparing a cod certification
horizon to an illustrative baseline's stability boundary.** On one system the two
constraints do not merely fail to coincide — they are **incompatible**: no review
interval on cod is both stable and certifiable. The feasible window is not the
half-year of §2.3; it is **empty, by a factor of at least 2.5**.

**Caveat, stated plainly: the transport is not unique.** P5's institutional
parameters carry implicit scale — `Zref`, `delta`, `Emax` are absolute, not
scaled to biomass — so "run P5 on cod" admits several defensible calibrations
and the crossing is only pinned within 17.5–175 yr. The *conclusion* (no
coincidence; constraints incompatible) holds in all six; the *number* does not.

**A second finding, and a risk to Paper B.** The 6.501 yr is ill-conditioned:

| `N*/K` | crossing |
|---|---|
| 0.89552 | 6.50 yr |
| 0.89343 | 10.10 yr |
| 0.88507 | 18.38 yr |
| 0.87462 | 25.31 yr |

A **0.2%** change in the exploitation ratio moves the crossing by 55%. P5's
headline number is a property of one knife-edge calibration, not a robust time
scale of the mechanism. Paper B should not lead with it without a sensitivity
band, and this is worth raising with P5 before the merge.

### 2.5 What Paper B's headline becomes

The near-match is dead — computed, not argued. What survives is the family's own
claim, carried by P5 and E2 separately:

> What decides whether management stabilises or destabilises a renewable
> resource is not biology alone but the decision clock.

And the two results are now known to **conflict** rather than agree — certification
expires at 6–7 yr while the sampled loop is unstable below ~17.5 yr on the same
stock. That conflict is the interesting result, and it is stronger than the
agreement would have been. It is also the one claim that most needs the
calibration caveat of §2.4 carried beside it.

## 3. Paper A — theory

**Working title.** *Obstruction certificates for viability under incomplete observation*
**Venues.** *Automatica*, *SIAM J. Control & Optimization*, *Math. Control Signals Systems*
**Core.** P2; fold in P1's gap geometry, `finite_horizon_completeness`, minimax dual
certificates, certificate duality. One question: *when can you certify that no
observation-based policy works?*

Gaps, in order:

1. **Prior art first, before any other writing.** **DONE 2026-09-29.** Drafted in
   `PAPER_A_PRIOR_ART.md`. The first verdict ("the claim as stated does not survive
   unqualified") was **withdrawn**: it had been drafted from the plan summary plus an
   external search, without first probing `obstr_v55`'s own citations --- the Veliov gap it
   rested on was already closed in the manuscript. Doyen (2000), *Set-Valued Analysis*
   **8**, 149--162, has since been read **in full** and the claim **survives**: his
   Definition 1.1 quantifies over Lipschitz selections with a memoryless closed loop
   `u(h(x,w))`, and his property is exact invariance of a closed set, so his necessity does
   not reach observation-based policies generally. Paper A's residual gap is therefore
   exactly: an **exactly checkable non-existence certificate valid against every
   observation-based policy (not merely Lipschitz ones), for properties beyond exact
   maintenance of a closed domain**. **Both prior-art paragraphs are integrated into the
   manuscript** (`diffs/obstr_v57.tex`): the Doyen distinction in §1.3 *Related work*,
   placed between the sufficiency direction and the "On the failure side" sentence, and the
   Hamilton--Jacobi reachability / viscosity contrast after the barrier-certificate
   sentence, with six bibliography entries added and the narrowed residual claim stated.
   **No longer blocking.** Remaining on Paper A: item 2 below, and a compile check.
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

---

## 8. Settled 2026-09-29 — the decidable items

The same treatment applied to the other open items: go to the source, then
believe the result. Some close; some turn out to be drafting work, and are
labelled as such rather than dressed up as settled.

### 8.1 The prune blocker is cleared (§6)

The three one-version gaps that were stopping the prune:

| lead | family latest | delta | new sections |
|---|---|---|---|
| `e3_v16` | `paperE3_edwards_forecast_ladder_v17` | **+85 words** | Funding, Competing interests, Code availability |
| `e4_v15` | `paperE4_edwards_intervention_v16` | **+88 words** | Funding, Competing interests, Code availability |
| `minimax_v11` | `minimax_dual_certificates_v12` | **+0 words** | none — identical section set |

**No scientific content is lost** by building from the leads; the deltas are
front and back matter. Minimax v11 and v12 are the same paper. The prune is
unblocked for these three. (P3 remains the real gap: `p3_v32` at 26,027 words
against `paper3_material_ledgers_v50` at 36,387.)

### 8.2 E2 and ARV reconciled (§4.5) — they are complementary, not competing

ARV (`arv_v9` ≡ `applied_regime_viability_v9`, one file under two names) and E2
read the same cod record and answer **opposite** questions:

| | **ARV** | **E2** |
|---|---|---|
| direction | **obstruction / necessity** | **construction / sufficiency** |
| arithmetic | exact rational, no fitted model | floating point, Schaefer fitted 1983–2007 |
| certified object | a harvest-free multiplier bracket `[rho, max{rho+r, rho/(1-r)}]` | `C* = 91.59 kt`, `C_vac = 215.2 kt`, `T* = 6/6/7` |
| finding | both collapse steps are harvest-free contractions (upper bounds 0.754, 0.372); the reference window's worst step does **not** certify — "a typology, not a blanket verdict" | the reference point is expansive (`F' = 1.1531`) and 91.59 kt is certifiably viable, for 6–7 years |

They do not conflict: ARV certifies that **specific historical steps** were
contractions regardless of removals; E2 constructs a **management bound** from a
fit over a stated window. Different slices, opposite directions.

The real link runs the other way and is worth using: ARV's harvest-free collapse
certificates are *evidence for* E2's regime-dependence conclusion (171 kt on the
post-moratorium window, 0 ± 8 kt on the modern series). A record whose collapse
steps were harvest-free contractions is not one stationary production regime,
which is exactly why E2's bound is regime-dependent. Paper B should say that.

**Action for Paper B:** one paragraph, both directions named, no reconciliation
of numbers — there is nothing to reconcile.

### 8.3 What remains, honestly triaged

| item | kind | what it actually needs |
|---|---|---|
| §3.1 Paper A prior art | **research** | literature work: HJ reachability, viscosity characterisations, contingent cones, differential-inclusion capture basins, Veliov. Nothing can be written until this is read |
| §3.2 worked case where a certificate bites | **research** | a new computation, not a rewrite |
| §3.3 what of P1 survives | **decidable after §3.1** | the separation result is 194 KiB / 42 sections; whether it survives is a prior-art verdict, and my recommendation stands: Supplement S1 in full |
| §4.2 promote the null result | **writing** | the 42-stock and 32-system screens exist; they need promoting in the abstract, not re-deriving |
| §4.3 mechanism figures | **writing** | one figure now exists (E2's graphical abstract); two more to draw |
| §4.4 table of real cadences | **research** | needs an actual survey of institutional review cycles |
| §5.1–5.3 Paper C | **writing** | E3's null result is written; leading with it is an editorial act |
| §6 demote the verification apparatus | **writing** | move to a reproducibility statement |
| §6 one headline per paper | **partly blocked** | B's headline is at §2.5; A's waits on §3.1, C's on §5.1 |

**Root cause of the pattern across all of them:** the plan ordered the family by
what was *most finished* rather than by what was *most decidable*. The items that
closed in this session — §2, §8.1, §8.2 — closed because each had an archived
artefact that could be read and checked. The items that remain are open because
each needs something produced, not something adjudicated. That is a scheduling
fact, not a failure, and the build order should reflect it: **do the decidable
ones first** (they are cheap and they de-risk the rest), and do not let a drafting
task queue behind a research task it does not depend on.

### 8.4 A011 / A012 / A020 against P5 and P4 — supplement gains content

Asked: does Paper B's supplement gain anything from the `revised_articles/`
modules that sit on top of P5 and P4, or are they redundant? Screen used
(`diffs/compare.py`): extract every number of three or more significant digits
from each document and ask how many of the module's numbers appear nowhere in
the paper.

| module | words | vs | numbers shared | verdict |
|---|---|---|---|---|
| A011 periodic review | 5,692 | P5 (`p5_v47`, 19,765 w) | 17 of 22 (**77%**) | **keep as supplement** — moderate confidence |
| A012 delay dynamics | 8,006 | P4 (`p4_v41`, 29,662 w) | 57 of 76 (**75%**) | **keep as supplement** — high confidence |
| A020 two channels | 2,295 | P4 | 21 of 23 (**91%**) | **probably subsumed** — weak confidence |

**A012 — the clear case.** Its absent numbers are unambiguously registry data
with no counterpart in P4: a persistence bisection at the upper boundary
(`tau` in `[148.125, 148.438]` yr), crossings at `17.568` and `18.362` yr at the
out-of-range `eta = 10`, periodic-orbit folds near `5.574–5.575` and `5.587` yr,
a second branch with crossings at `3.7849` and `150.12` yr, a real Floquet
multiplier running `1.0514` at `tau = 5.584` to `0.998983` at `tau = 5.587`,
supercritical amplitude onset with fitted exponent `0.59`, and sustained cycles
of `360–380` yr in the lower regime. The module is titled *"A Registered Family
of Renewable-Resource Models"* — it is a family registry, which is what a
supplement is for. Fold it in.

**A011 — keep, with a caveat.** Three named case studies appear nowhere in P5:
Bangkok pumping (declines after 1999), Peruvian anchoveta (1950–2019 input),
and Icelandic cod with an author-calculated coefficient of variation falling
from `0.387` to `0.143` post-implementation. Four methodology sections have no
counterpart heading: the cross-sectional RAM spectral screen, power and
detectability, prospective identification designs, and governance-event panels.
**Caveat:** P5 is an IMRaD paper (14 headings) and A011 is a structured module
(23 headings); they share only "conclusion", so the section test cannot
establish redundancy. A human read is needed to confirm the spectral screen is
not already reported in P5's Methods.

**A020 — probably subsumed.** 91% numeric overlap; the only two absent numbers
are a SHA-256 fragment and one frequency (`0.0583`). Its framing sections (two
delays, sampled protection, pacing) may still be distinct, and at 2,295 words it
is cheap to keep rather than judge.

**Limits of this screen, stated so the verdict is not over-read.** A shared
number means shared content; an absent number does not prove absence, because a
result can be reported at different rounding or in different units. The section
test failed outright as a redundancy test because the two genres differ. So
these are screening verdicts: A012 is safe to fold in on this evidence, A011
needs one human read, A020 is a judgement call.

**Consequence for §6:** none of the three is *redundant enough to archive*.
The prune should treat `revised_articles/` as supplement feedstock, not as
prunable duplicates.

### 8.5 The P3 version gap — build Paper C from `v50`, and it supplies §5.2

| | `p3_v32` | `paper3_material_ledgers_v50` |
|---|---|---|
| words | 26,027 | **36,387** (+40%) |
| headings | 65 | 71 |
| distinct numbers | 91 | 136 (**38% of v50's are new**) |

Six substantive new sections in v50, four of them applied cases:

* *Composition of ledgers and the calculus of certificates*
* *Groundwater anomaly-persistence indices*
* *The applied depletion-horizon tables*
* *The phosphate reserve-life ratio*
* *The fisheries removals-only pressure time* (the `547 / 346 / 251 / 173` d series)
* *What an aggregate record fixes*

plus Abstract, Funding and Code availability. **Nothing was lost**: the one
heading that disappears, *First-Passage Semantics on Declared Surrogates*, was
absorbed rather than dropped — "first passage" occurs 22 times in v50 against 20
in v32.

**Why this is not housekeeping.** Plan §5.2 says P3's contribution is "a
typology — 'three diagnostics are widely misread'" and that "as a top-journal
contribution that is a clarification unless it is tied to a measurable
consequence." The four applied sections in v50 **are** that consequence: the
applied depletion-horizon tables, the phosphate reserve-life ratio proved to be
a static arithmetic quotient of an economic classification, the groundwater
persistence indices, and the fisheries removals-only pressure time. Building
Paper C from `p3_v32` would forfeit the ingredient §5.2 says the paper needs.

**Decision: build Paper C from `paper3_material_ledgers_v50`.**

### 8.6 Paper A prior art — drafted, and it does not clear the claim

`PAPER_A_PRIOR_ART.md` (2026-09-29) covers the four areas the plan named plus two more.
Findings:

* **Viability theory (Aubin)** and **HJ reachability** both give exact obstruction
  statements — the complement of the viability kernel, the BRT as the zero sublevel set of
  a viscosity solution — but both assume **full state observation**. Their gap is
  observation, not existence.
* **Veliov (1993)** is *sufficient only*, exactly as the plan said, and alone would leave
  Paper A's necessity claim intact.
* **The 2000 *Set-Valued Analysis* paper is the problem**: necessary *and* sufficient,
  output feedback, disturbance on dynamics **and** output, geometric and HJ–Isaacs
  characterisations, plus an algorithm. On the abstract, that is the claimed gap, closed.
* **The 2026 partial-observability line** (CBVF with conformal prediction; streaming
  contraction certificates) gives sufficiency with probabilistic, finite-horizon
  guarantees — not impossibility.

**REVISED after checking the manuscript (§5–§6 of `PAPER_A_PRIOR_ART.md`).** The first
verdict overstated the risk: `obstr_v55` already closes the Veliov gap in the recommended
way — *"Veliov's condition tells us when output feedback can work; the obstruction calculus
tells us when it cannot"* — cites the whole French viability lineage including Aubin (2001)
on the failure side, and has a dedicated §5 *Sufficiency Landscape*. Two real gaps remain,
and the priority between them flips:

1. **HJ reachability / viscosity is entirely absent** — "viscosity" occurs **zero times** in
   22,615 words, despite being the plan's first-named prior-art area and the dominant
   computational tradition in safety verification. **This is now the more urgent gap**: add a
   paragraph contrasting the obstruction certificate with the BRT-as-viscosity-sublevel-set
   construction. No paywalled source needed.
2. **The 2000 *Set-Valued Analysis* 8, 149–162 paper** is uncited. It gives necessary *and*
   sufficient conditions, but only for a **Lipschitz closed-loop** maintaining the state
   **exactly** — narrower than P2's "every policy" framing, and likely from the same school
   P2 already engages. A citation-and-distinguish job, still required.

**BLOCKING ITEM RESOLVED 2026-09-29.** Doyen (2000) was read in full (§7 of
`PAPER_A_PRIOR_ART.md`). **The claim survives.** Its Definition 1.1 requires a **Lipschitz
selection** and a **memoryless** closed loop `u(h(x,w))`; its property is **exact
invariance** of a closed set; and its thrust is synthesis (Corollary 1.3 constructs a
feedback by Steiner selection), with Doyen himself disclaiming the harder case — "no
general viability result is available in this differential game context with imperfect
and/or partial information". So it is nearest neighbour, not anticipation.
**Citation finding:** `obstr_v55` mentions "Doyen" 12 times, but every occurrence is the
sustainability-application cluster (Béné–Doyen–Gabay 2001; De Lara–Doyen 2008; Doyen et
al. 2012; Doyen–Gajardo 2020). The 2000 paper's machinery occurs **zero** times —
"Lipschitz kernel" 0, "Steiner" 0, "tangent cone" 0, "invariance" 0. The paper cites
Doyen the applied author and misses Doyen the output-feedback theorist.
**Two small writing jobs remain**: (1) cite Doyen (2000) and distinguish on policy class,
property and direction, quoting his own disclaimer; (2) add the HJ reachability / viscosity
paragraph (0 occurrences in 22,615 words), using Doyen's §2 HJ–Isaacs conditions as the
bridge. **Neither blocks drafting.**

**Also:** do not fold P1's 194 KiB separation result into Paper A until this is settled.
It carries its own prior-art question (quantifier-order separation against
robust-optimisation and MCDM separation results), and folding it in first would compound
two unresolved novelty risks.
