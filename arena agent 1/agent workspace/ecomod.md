# ECOMOD Alignment Audit — weak/strong sustainability, the inspired mathematical framework, and cross-strengthening

**Task 117 / owner-directed audit (2026-09-22).** Directive: check `agent 2 productivity illusion/manuscript_ECOMOD_v36.tex` (the ECOMOD/"productivity illusion" family member) for (i) weak/strong sustainability alignment with the five-manuscript corpus audited in Task 116, (ii) cross-strengthening opportunities in both directions, and (iii) alignment of the inspired mathematical framework with the companions' actual results. This document extends `CROSS_MANUSCRIPT_ALIGNMENT_AUDIT.md` (Task 116, which covered P1 v59 / P2 v44+supp / P3 v32 + live JIE v3 / P4 v41 / P5 v47) to the sixth family member. English-only rule standing; no unilateral manuscript changes made.

**Audited version:** `agent 2 productivity illusion/manuscript_ECOMOD_v36.tex` (775 lines; dated September 7, 2026; title "How Aggregation Can Conceal Composition: Aggregate Biocapacity and the Identifiability of Modelled Ecological-Capital Drawdown"; ECOMOD = the Ecological Modelling target).

**Method.** Full read of the manuscript; every companion claim traced to its source text (P1 v59 `latex/paper1_assessment_separation_v59.tex`; P3 v32 `latex/paper3_material_ledgers_v32.tex`; P4 v41 `latex/paper4_delay_dynamics_v41.tex`; P2 v44 and P5 v47 for the vocabulary mappings); a 10-gram and 15-gram verbatim-overlap scan (comments stripped, LaTeX commands normalized) of ECOMOD against all five corpus manuscripts; Theorem-numbering stability checked across the P1 chain (v35/v44/v47/v53/v59); the σ-notation objects compared across the family.

---

## 1. The companion mapping (who ECOMOD cites, and how)

ECOMOD cites exactly three of the five corpus papers, all three correctly identified by DOI:

| ECOMOD entry | Corpus paper | Title used | Status |
|---|---|---|---|
| Abaee, 2026a (DOI 22554217) | Paper 4 delay dynamics v41 | P4's **current** title ("Governance delay and the stability of harvested stocks: mobilising and protective feedback rules, and the review interval as a design parameter") | ✓ resolves; the *deposit* still carries the old title ("Delay-Induced Regime Change in Harvested Stocks…") — the standing owner-side deposit-refresh item (Task-116 flag 2) applies unchanged |
| Abaee, 2026b (DOI 22545740) | Paper 1 assessment separation v59 | P1's **current** title ("Aggregate Indices and Transition Safety: A Quantifier-Order Separation Between Scalarized and Coordinate-Wise Feasibility") | ✓ the same best-practice as P2's citation of P1 |
| Abaee, 2026c (DOI 22554177) | Paper 3 material ledgers v32 | The v32-chain/deposit title ("Typed Flux Ledgers and Depletion Arithmetic…") | ✓ resolves to the deposit; **note** the live JIE v3 submission variant is retitled "Typed material-flow ledgers for componentwise sustainability diagnostics" — if it publishes under that title, this entry (like P1's) needs the refresh |

Papers 2 and 5 are not cited (ECOMOD uses their *vocabulary* in two places — see §4 items 4-5 — but no results); that is a legitimate division-of-labor choice, with optional soft pointers recommended below.

## 2. Weak/strong sustainability alignment — VERDICT: ALIGNED

ECOMOD's doctrine paragraph (line 437) adopts **P3's material-cycle reading with correct attribution** ("By weak sustainability, in the material-cycle reading adopted here (Abaee, 2026c)…"): weak = the idealised regime in which substitution and regeneration jointly redistribute matter as it arises (substitution admissible only through an identified physical pathway); strong = the regime in which that closure fails, so a separately-binding floor on a critical stock binds. This corresponds clause-for-clause to P3 v32's own definition (lines 246-262): "Strong sustainability is the regime in which that closure fails --- either because no identified physical pathway re-routes the extracted matter, or because depletion outruns the rate at which such a pathway could be deployed", with weak as the idealized closure and waste a relational status. The reading is harmonious with the family's one-doctrine story exactly as recorded in Task 116: the dichotomy dissolved into one formal object; weak = the idealized/permissive regime; strong = the binding end.

- **The scalarized/coordinate-wise mapping is exact.** ECOMOD: "The weighted composite B is the weak-sustainability index: it satisfies its aggregate floor while the *typed* floor on ecological capital A_c is violated" (line 437) — the same separation as its R_B/R_A gap, and formally the scalarized-vs-coordinate-wise feasibility separation of P1 (2026b), which ECOMOD anchors via the aggregation theorem in its division-of-labor statement (line 342).
- **No stale claims.** ECOMOD makes no claim about P1's σ-extension results state (the spectrum is never referenced), so the v53→v59 waves supersede nothing in ECOMOD. Its one P1 pointer — "the aggregation theorem (Proposition 1 of the deposited version of that work; Theorem 5 of its current version)" — remains valid against v59: Theorem 5 is stable across the chain (28 mentions in v35, 29 in v44, 30 in v47, 34 in v53, present throughout v59 as the acceptance-gap/licensing-thresholds theorem).
- **The delay doctrine is cleanly divided.** "ECOMOD's delays are *ecological* (regeneration τ_g, demography τ_p), whereas the companion's lie in the *institutional* feedback loop" (line 342) — consistent with P4's territory, and ECOMOD explicitly does **not** claim the one-stock comparator's Hopf classification (χ = q/(ρ−2q), τ_m ≈ 85.4, τ_p ≈ 231 yr, the +0.62 eigenvalue) for the two-land system (lines 471-478): the one-stock results are quarantined in SI §§S1-S4. ✓

## 3. The inspired mathematical framework — every import verified at its source

| Framework element ECOMOD imports | Source (verified) | Attribution in ECOMOD | Status |
|---|---|---|---|
| Compensatory-aggregation gap; scalarized-vs-typed-floor separation; the aggregation theorem | P1 v59 Theorem 5 (the acceptance gap / per-weight licensing thresholds); P3 §10.1 | line 342 (division of labour); line 437 | ✓ correct |
| Static typed-flux ledger; conservation/donor-limitation rules; depletion arithmetic; the no-nonnegative-weighting aggregation obstruction | P3 v32 (obstruction = §10.1 "Compensatory aggregation is rejected…"; "No nonnegative weighting certifies componentwise…" lines 66/219) | lines 342, 486-488 | ✓ correct |
| "Productivity illusion" (the term and its two senses) | P3 v32 line 124 (definition), lines 131-153 (the yield-inflation second sense) | lines 69, 71, 496 | ✓ the yield-inflation sense is named exactly at line 496; see flag 1 for one loose gloss |
| P3's registered two-pool dynamical open gap, which ECOMOD fills | P3 v32 lines 158-161 ("The groundwater two-pool model is a registered open gap whose admitted applied object is the one-pool affine approximation") | lines 491-494 ("ECOMOD supplies exactly that missing dynamical realisation --- a minimal two-book, delay-coupled model --- for the global-hectare biocapacity case") | ✓ exact, both sides |
| P3's non-transfer clause | P3 v32 lines 2615-2618 ("The companion's global periodic results are properties of its reduced systems and do not transfer to the closed primitive ledger") | line 491 (quoted) | ✓ verbatim-faithful |
| Mobilising/protective feedback distinction | P4 v41 (title vocabulary; 60 occurrences) | line 427 uses the taxonomy **without an inline citation** | flag 2 |
| Exact-tube semantics | P1's vocabulary (the exact tubes of the common-shock extension) | line 439(b) uses it un-attributed | flag 3 (minor) |
| Robust-viability / preregistered-retention caveat | P5's framework vocabulary | line 429 mirrors it un-cited | §4 item 5 (optional) |
| Controller-observability point | P2's incomplete-observation territory | line 428 un-cited | §4 item 4 (optional) |

**Theorem-numbering and σ-notation checks.** The "current version" Theorem-5 pointer is stable (above). On notation: ECOMOD's σ_f, σ_c (human-available flow shares, land-subscripted) join the family's σ-objects (P1's σ-spectrum — which v59's notation subsection already disambiguates against the companions' σ-notations — and P2's σ*(B₀)). The subscripted shares are formally distinct and collide with nothing inside ECOMOD; a one-line family-notation note is optional for the next round (mirroring P1 v59's existing practice).

## 4. Cross-strengthening — the actionable inventory

**Direction 1: ECOMOD ← the corpus's post-v36 results.** P1's Lemma A, Lemma B, and Theorem S2 did not exist in any P1 version when ECOMOD v36 was finalized (zero occurrences in v44 and v47; they first appear in the v53→v59 chain, after September 7). ECOMOD's next round can therefore anchor three of its claims to strictly stronger results that were unavailable at its writing:

1. **Line 437, "The weighted composite B is the weak-sustainability index"** can now be made literal: by P1 v59's **Lemma A**, the linear member is the aggregator family's *attained* weak extreme — B (a fixed-weight linear composite) *is* the perfectly-substitutable member. One clause suffices: "the linear, perfectly-substitutable member of the companion's aggregator family --- its attained weak extreme (Lemma A of Abaee, 2026b)". This also tightens the weak/strong alignment by linking ECOMOD's material-cycle reading (2026c) to P1's aggregator-family reading in one sentence — the two formalizations of the one doctrine, currently cited separately.
2. **Line 439(a), "The mask is a structural failure of any aggregate that compensates a falling capital book with a rising yield, not an accident of one parameter set"** can now cite P1 v59's **Theorem S2(ii)** (no positive-elasticity aggregator is uniformly safe; the only uniformly safe aggregator is σ = 0, the typed/Leontief end). This upgrades the claim from "this aggregate can mask" to "no compensating aggregate of the family can be uniformly safe" — the exact family-level theorem behind ECOMOD's structural thesis.
3. **Optional pointer:** P1 v59's continuum slice closure (§5.8: the four-regime tolerance structure, the flip-total ladder) is the certified exact-arithmetic companion of ECOMOD's substitution-buffer formula ("violated by exactly the amount that the fast-land yield gains against the capital loss", line 437).
4. **Line 427 (mobilising/protective):** add "(Abaee, 2026a)" — the taxonomy is the delay companion's title vocabulary.
5. **Lines 428-429 (controller observability; robust-viability/preregistered retention):** optional soft pointers to P2 and P5 in P4's established "companion analyses (under review)" style.

**Direction 2: the corpus ← ECOMOD (owner-side, next-round).**

6. **P3's registered two-pool open gap is now filled** by ECOMOD's minimal dynamical two-book realization (ECOMOD lines 491-494 self-position exactly there, verified against P3's own registration). P3's next chain round can convert "registered open gap" to "supplied in the companion biocapacity study" with a forward citation to ECOMOD's deposit (Zenodo 22554480) — the single highest-value family synchronization available.
7. **P1's measured instance:** ECOMOD supplies the measured NFA demonstration of the aggregation face (population +464% / per-capita −364%; R_B crossing 1 in 1971; cropland 2.85× vs. flat non-cropland; the recursive identifiability of the non-cropland book). A forward pointer in P1's limitations/empirical-context would note the measured instance exists.
8. **P4's ecological-delay complement:** ECOMOD's ecological delays (τ_g, τ_p) complete the delay taxonomy beside P4's institutional ones; P4's next round could cite the ecological-delay companion.

## 5. Self-plagiarism / verbatim duplication — verdict: CLEAN outside one flagged P3 doctrine echo

The 10/15-gram scan (comments stripped, LaTeX normalized) of ECOMOD against all five corpus manuscripts:

- **vs P1:** 7 shared 15-grams — all shared *reference entries* (Becker et al. 2017; Fischer et al. 2022; Schaefer 1954). Benign.
- **vs P2, P4, P5:** zero shared 15-grams (the 10-gram hits are normalization artifacts). Clean.
- **vs P3:** 9 shared 15-grams, **all from one ~25-word doctrine passage**: "because no identified physical pathway re-routes the extracted matter, or because depletion outruns the rate at which such a pathway could be deployed" — ECOMOD line 437 quotes P3 v32 lines 255-258 nearly verbatim (dropping "either"). Two further shared phrasings sit in the same paragraph just below the 15-gram threshold ("are returned to use in time and are therefore not waste"; "waste is a relational status, not an intrinsic property of any material"). The passage *is* attributed ("in the material-cycle reading adopted here (Abaee, 2026c)"), but not marked as quotation. Recommendation (mirroring Task-116's P2-P3 echo flag): in the next ECOMOD round, quotation-mark the definition sentence, paraphrase it, or make the borrowing explicit ("in the ledger study's words").
- **A shared image, below the n-gram radar:** the elevator analogy (rated for ten, carrying fourteen, the cable failing invisibly) appears in **both** ECOMOD line 69 and P3 v32 lines 162-165 with different wordings. It is the family's most distinctive shared illustration and is unattributed in ECOMOD. Recommendation: attribute ("in the ledger study's image…") or replace one instance in a future round.

## 6. Flags (recorded; no unilateral changes)

1. **Line 71's gloss of the productivity illusion** — "the aggregate rises not merely because technology outpaces degradation (the productivity illusion as Abaee, 2026c, defines it)" — is looser than P3's actual definition ("the appearance that a system is delivering adequately while the base that sustains the delivery is being reduced"; the yield-inflation sense = drawdown-maintained measured yield, which requires no technology channel at all). ECOMOD's line 69 and line 496 characterize it correctly; only line 71's parenthetical is loose. Next-round precision fix.
2. **Line 427's mobilising/protective bullet lacks the inline citation** to Abaee (2026a) — the taxonomy is P4's title vocabulary (§4 item 4).
3. **Line 439(b)'s exact-tube semantics** used without attribution (P1's vocabulary) — minor; one clause would do.
4. **The author block** reads "Amin Abaee / Independent Researcher" without the Tehran affiliation that P4 v41 gained this round (Task 116 item 2) and P3's JIE v3 carries ("Independent Researcher, Tehran, Iran"). If family-consistent affiliations are wanted, ECOMOD's next round should match.
5. **The deposit-title network item** (Task-116 flag 2) extends to ECOMOD: 2026a cited under the current P4 title against the old deposit title; 2026c cited under the deposit/v32 title against the live JIE v3's new title; ECOMOD's own deposit (22554480) joins the network the corpus can cite once the owner-side Zenodo refresh happens.

## 7. Conclusion

ECOMOD v36 joins the family **aligned**: it reads the weak/strong doctrine through P3's material-cycle lens with correct attribution, anchors the arithmetic face to P1's separation (Theorem 5, numbering verified stable), fills P3's registered two-pool dynamical open gap by explicit self-positioning, keeps its delays ecological against P4's institutional ones, and quarantines its one-stock comparator honestly. Every companion claim traced in this audit resolved at its source. The duplication scan is clean outside one attributed-but-unmarked ~25-word doctrine echo with P3 and the shared elevator image (both next-round fixes). The cross-strengthening inventory (§4) is concrete in both directions: ECOMOD's next round can anchor its structural claims to P1's post-v36 Lemma A / Theorem S2(ii) (which did not exist when v36 was finalized), and the corpus's next rounds gain a filled two-pool gap (P3), a measured instance (P1), and an ecological-delay companion (P4).
