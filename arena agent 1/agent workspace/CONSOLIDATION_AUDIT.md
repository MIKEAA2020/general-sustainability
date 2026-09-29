# Consolidation audit — is anything being lost?

Audited 2026-09-29 against the branch `e2-v3-source-year`. Every size and word count
below comes from the repository tree and file contents, not from the plan's prose.

**Short answer: no, the consolidation is not complete, and the plan as written would lose
content.** One mapping error (a wrong file in the P1 slot), five leads that lag their
families, and 618 KiB of modules the plan never mentions. Details and recommendations
below.

---

## 1. Status of every item in the plan

| # | item | status | evidence |
|---|---|---|---|
| §0 | fix E2 first | **done** | E2 frozen at v29; battery 421 checks / 0 failed; sabotage 136 mutations / 0 holes; basis audit 187/187; 28 pp, 10 figs, 8 tables; graphical abstract added |
| §1 | inventory of manuscripts | **done, but defective** | 12 leads named; see §2 — one lead is the wrong file |
| §2 | settle the P5/E2 relation | **SETTLED BY COMPUTATION 2026-09-29 — the answer is no** | P5's crossing scan was transcribed, validated against its committed gate (6.5013 / 47.5360 / 79.1427 / 2.3064, protective-exact stable) and re-run on cod biology: the crossing moves to **17.5 yr or beyond** in all six transports. The constraints are not merely unproven to coincide — they are incompatible. See plan §2.4 |
| §3.1 | Paper A: prior-art section first | **open** | nothing written |
| §3.2 | Paper A: worked case where a certificate bites | **open** | |
| §3.3 | Paper A: decide what of P1 survives | **open — and the input file is wrong** | see §2.1 |
| §4.1 | Paper B: settle P5/E2 | **settled — no link** | = §2, now rewritten |
| §4.2 | Paper B: promote the null result | **open** | |
| §4.3 | Paper B: 2–3 mechanism figures | **open** | no figure budget now applies |
| §4.4 | Paper B: table of real institutional cadences | **open** | |
| §4.5 | Paper B: reconcile E2 and ARV | **settled — complementary** | ARV is the obstruction/necessity direction (harvest-free multiplier brackets, exact rational); E2 is the construction/sufficiency direction. Opposite questions, no numbers to reconcile. Plan §8.2 |
| §5.1 | Paper C: lead with E3's null result | **open** | |
| §5.2 | Paper C: tie P3's typology to a consequence | **open** | |
| §5.3 | Paper C: demote E1 and E4 to sections | **open** | |
| §6 | freeze and prune ~330 `.tex` files | **unblocked for 3 of 4 blockers** | E3 +85 and E4 +88 words are front matter only; minimax v11 == v12. P3 remains the real gap (26,027 vs 36,387 words). Plan §8.1 |
| §6 | demote the verification apparatus | **open** | belongs in a reproducibility statement |
| §6 | one headline per paper | **partial** | B's headline drafted; A and C have none |
| §7 | build order | **on track** | E2 done; B is next, and it starts with §2 not with drafting |

**Closed: 1 of 16.** E2 only.

---

## 2. Defects in the plan itself

### 2.1 The P1 slot names the wrong file (high severity)

The plan maps *"P1 separation → `fam/arv_v9.tex`, acceptance-gap geometry → Paper A"*, and
separately *"ARV applied regime → `applied_regime_viability_v9.tex` → Paper B"*.

Both files are **the same manuscript**:

| file | size | words | title |
|---|---|---|---|
| `fam/arv_v9.tex` | 45 KiB | 7,256 | *Regime Viability on the Northern Cod Stock: An Exact Certification of Obstruction Structure on Public Assessment Data* |
| `applied_regime_viability_v9.tex` | 45 KiB | 7,256 | *identical* |

So the P1 slot is a duplicate of the ARV slot, and the actual separation paper is nowhere
in the inventory:

| file | size | words | sections | title |
|---|---|---|---|---|
| `paper1_assessment_separation_v63.tex` | 194 KiB | 30,634 | 42 | *Aggregate Indices and Transition Safety: A Quantifier-Order Separation Between Scalarized and Coordinate-Wise Feasibility* |

Consequence if uncorrected: Paper A gets a 45 KiB cod case study folded in as "P1's gap
geometry", while 194 KiB of the real separation result is classified as one of the ~330
files to archive. That is exactly the loss the audit was asked to look for.

One useful side effect: §4.5 ("reconcile E2 and ARV") is smaller than the plan implies —
both slots point at the same cod manuscript, so there is one reconciliation, not two.

### 2.2 Five leads lag their families

| lead named in the plan | family's latest | words | assessment |
|---|---|---|---|
| `p3_v32` (P3) | `paper3_material_ledgers_v50` | 26,027 → **36,387** | **+40% — real content**; same title, so a genuine expansion |
| `obstr_v55` (P2) | `paper2_obstruction_calculus_v56_Automatica_routes` | 22,615 → 22,680 | benign: same title, same 12 sections, same 23 formal statements; a 65-word delta |
| `e3_v16` (E3) | `paperE3_edwards_forecast_ladder_v17` | — | 1 version; **unverified** |
| `e4_v15` (E4) | `paperE4_edwards_intervention_v16` | — | 1 version; **unverified** |
| `minimax_v11` | `minimax_dual_certificates_v12` | — | 1 version; **unverified** |

`e1_v60`, `p4_v41`, `p5_v47`, `ws_v17`, `applied_regime_viability_v9`, E2 v29 are current.
The three "unverified" one-version gaps must be diffed before any pruning; they are most
likely cosmetic, but that is an assumption, not a result.

### 2.3 Content mapped to no paper at all

* **17 `revised_articles/A0xx_*_corrected.tex` modules — 618 KiB.** Not mentioned in the
  plan. Several are topically adjacent to a mapped paper, which is what makes them easy to
  lose silently:

  | module | size | words | topic | adjacent to |
  |---|---|---|---|---|
  | A002 general theory | 156 KiB | 25,245 | typed flux–observation–governance theory | Paper A |
  | A018 capital liquidation | 179 KiB | 29,703 | scarcity-driven liquidation, delay amplification | Paper B |
  | A012 delay dynamics | 49 KiB | 8,006 | delay-amplified extractive mobilisation | **P4** |
  | A011 periodic review | 38 KiB | 5,692 | sampled-data periodic review | **P5** |
  | A013 component accounting | 33 KiB | 5,180 | componentwise sustainability accounting | **P3** |
  | A006 robust epistemic | 17 KiB | 2,435 | hybrid material–institutional viability | Paper A |
  | A020 two channels | 14 KiB | 2,295 | protective delay is a different loop | **P4** |
  | A021 Liebig graph | 27 KiB | 4,094 | yield-gap reduction in vector Liebig RFDEs | Paper A |
  | A019, A022–A025 | ~46 KiB | ~7,600 | closed ledgers, stage harvest, spatial, first passage, interval Hopf | Paper A |
  | A003–A005, A007 | ~53 KiB | ~7,300 | phosphorus, groundwater, institutional feedback, hybrid architecture | applied |

* **`arena agent 1/other documents/analysis/aug08_theory_original/…` — 582 KiB**, the
  largest unmapped item in the tree.
* **49 unmapped families ≥ 20 KiB**, including a second theory line
  (`paper2_worked_systems` 73 KiB, `paper2_probabilistic_sufficiency` 85 KiB,
  `paper2_computational_certification` 79 KiB) and a SafeTransition line
  (`paper1_safetransition_ems` 58 KiB, `…_master` 58 KiB).
* 79 families in total are unmapped; the plan's "other ~330 files" is really ~430.

The standing constraint still applies: **archive, never delete.**

---

## 3. What merits delegation to a supplement

Test applied: a referee needs the *result* to judge the paper, and the *detail* to check it.
Anything needed to follow the argument stays; anything needed to verify it moves.

### Paper A — theory

| destination | content | why |
|---|---|---|
| **main text** | obstruction calculus (`obstr_v55` ≡ v56), the necessity direction, one worked case where a certificate bites on a system whose kernel cannot be computed | the argument |
| **Supplement S1** | P1 separation (`paper1_assessment_separation_v63`, 194 KiB) **in full** | it is a complete second result with 42 sections, not a fold-in. Folding 30k words into A would bury it; as S1 it is citable and reviewable |
| **Supplement S2** | `minimax_dual_certificates_v12` (41 KiB), `finite_horizon_completeness`, `certificate_duality` | supporting theory a referee checks, not follows |
| **archive** | A002 (156 KiB, 25k words) | a monograph, not a supplement. Either its own deposit or archived — but do not fold it silently into A |
| **prior art** | written **before** the results section, per §3.1 | decides whether the paper exists |

### Paper B — mechanism + evidence

| destination | content | why |
|---|---|---|
| **main text** | P5 (`p5_v47`), P4 (`p4_v41`), E2 (v29), ARV (`applied_regime_viability_v9` ≡ `arv_v9`); the 6/6/7 plateau; the null result promoted into the abstract | the argument and the headline |
| **supplement** | the 42-stock screen and 32-system cross-sector search in full; the table of real institutional cadences; E2's campaign numerics; A011 and A012 **if** they contain results absent from `p5_v47` / `p4_v41` (diff first — they are topically the same papers) | verification and practitioner detail |
| **reproducibility statement** | the battery, the sabotage harness, the basis audit, the campaign code | per §6: this certifies that the manuscript matches its own archive. It is not part of the argument |
| **open** | §2, the P5/E2 relation — decides the headline | |

### Paper C — measurement

| destination | content | why |
|---|---|---|
| **main text** | E3's null result as the opening; P3's typology tied to one measurable consequence | the argument |
| **supplement** | `paper3_supplementary_v18` (72 KiB, 11,357 words, *"Checkability records and the detail behind the applied sections"*) — already written and already in this shape; E1 and E4 as sections; A013 component accounting | verification |
| **note** | build C from `paper3_material_ledgers_v50` (36,387 words), not `p3_v32` (26,027) | 40% more content, same title |

### Cross-cutting

* **Journal-route and blinded variants** (`*_Automatica_routes`, `*_NatSustain`,
  `*_blinded_NatSustain`, `*_JIE_submission`, `*_EE_submission`) — archive. These are
  venue-specific packagings of the same science.
* **Supplements the family already has**, worth reusing rather than rebuilding:
  `paper3_supplementary_v18` (72 KiB), `paper2_obstruction_calculus_v29_supplementary`
  (48 KiB, 13 formal statements), `paper3_JIE_supplement_v3` (37 KiB),
  `companionA_certification_procedure_v10` (38 KiB),
  `companionB_standards_horizon_v10` (30 KiB).

---

## 4. Corrections made and next actions

Changed in `FAMILY_CONSOLIDATION_PLAN.md`:
* §1 inventory: the P1 row now names `paper1_assessment_separation_v63` (194 KiB) as the
  separation paper, and the duplicate ARV row is marked as the same file as `arv_v9`.
* §1 inventory: leads flagged where the family has moved on (P3, E3, E4, minimax).
* §6: the prune count corrected from ~330 to ~430 files / 79 families, with the standing
  "archive, never delete" constraint restated next to it.

Next, in order:
1. Diff the three unverified one-version gaps (E3, E4, minimax) — cheap, and it closes the
   last unknown before any pruning.
2. ~~Diff A011/A012 against `p5_v47`/`p4_v41`~~ **done 2026-09-29**: A012 gains real
   content (a model-family registry: bisection intervals, orbit folds, Floquet multipliers);
   A011 keeps three case studies and four methodology sections with no counterpart in P5;
   A020 is 91% subsumed. None is redundant enough to archive. Plan section 8.4.
3. ~~Then §2 — settle the P5/E2 relation~~ **done 2026-09-29**: they are not the same
   quantity. The remaining task is the same-system experiment of §2.4 — calibrate P5's
   effort/hold model to the cod record (`q`, `E_max`) and re-run the crossing scan on cod
   parameters. That is the only thing that could turn the coincidence into a result.
