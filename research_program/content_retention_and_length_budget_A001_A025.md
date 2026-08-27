# Content Retention and Length Budget — A001–A025 Programme (Programme-Wide)

**Status:** Planning register (measured; no theorem status created or promoted).
**Date:** 2026-08-27
**Purpose:** Answer, with the programme's own measured numbers, the governance question: *the repo holds 20+ articles including one 72,580-word manuscript — how can all valid content be retained across "about five papers" without exceeding journal length limits?*
**Companions:** `revised_optimal_publication_architecture_A001_A025.md` (the architecture), `paper2_theorem_atlas_content_budget.md` (the Paper 2 precedent), `paper2_retained_row_budget_report.md`, `canonical_concordance_A001_A025_coverage.md` (the routing).

---

## 1. The short answer

**It cannot, and it was never designed to.** "Five papers" is not the retention vehicle; it is the **assured minimum of journal articles** in a multi-layer architecture:

| Layer | Vehicle | Length constraint | Retention role |
|---|---|---|---|
| 0 | **The repository itself** (public, versioned, hash-pinned) | none | Every source article, corrected article, proof artifact, and register is retained **in full, permanently, citable** |
| 1 | **Journal articles** — 5 assured + 2 conditional (Papers 6–7) + Wave E scored-forecast papers (2, drafted) + domain papers (up to 3, gated) | venue main-text limits | Carry only **load-bearing content**: theorem statements, proofs of record, certified results, decisive counterexamples |
| 2 | **Electronic supplementary material / preprint versions** | effectively none (venue-dependent) | Full proofs, extended tables, artifact crosswalks |
| 3 | **The definitive monograph** (Wave 3) | none (university-press monographs routinely run 80–120k words) | The **uncompressed canonical narrative** — where the full architecture is reintegrated after module closure |
| 4 | **The versioned reproducibility compendium** | none | Proof/data/code/version artifacts and retained conditional material |

The non-loss rule (architecture, final section) is the binding constraint, and it is a **routing** rule, not a compression rule:

> Every valid source proposition must map to: (1) a specific paper section; (2) a proof/technical appendix or companion; (3) a conditional future-paper docket; or (4) an explicit negative/counterexample record. **No valid result may disappear merely because its source manuscript does not retain a standalone identity.**

The 409-row canonical concordance is the executed form of that rule: **every row already carries a destination**. Retention is enforced at the row level, not guessed at the article level.

---

## 2. The measured intake — what the ~200k words actually are

Registered sources: 26, totalling **200,507 words**. This number is intake pressure, not manuscript material:

| Class | Sources | Words | Notes |
|---|---|---:|---|
| **Non-additive supplemental version** | SRC-A018-V18 | 72,580 | `manuscript_v18_dehedged.txt` — a *version* of A018, registered "supplemental_version_received; not canonical pending version audit". It is not additive content; it is a version-audit obligation. |
| **Canonical A001–A025** | 25 | 127,927 | The true intake |
| — of which the three flagships | A018 (27,523), A002 (23,977), A001 (23,174) | 74,674 | 58% of the canonical intake; the two architecture articles (A001+A002) share the typed framework and overlap heavily |
| — of which superseded/rejected branches | A006, A007, A010 (partially superseded); A008, A009, A015, A017 (rejected branches) | ~16,900 | Their **valid** content is negative/counterexample/redesign material routed to the registers — a few lines each, not article length |
| — of which bridged supplements | A019, A020, A022, A024, A025 (+A021) | ~11,000 | "Integrate into unified applied article; no separate paper" per the source registry |

The corrected publication-bound articles (`revised_articles/`, 23 files) total **97,758 words**, of which the top three (A018 20.5k, A001 20.2k, A002 19.5k) are 60,171 words — again concentrated in the flagships.

**Key fact:** the load-bearing formal content of the entire intake is inventoried as **409 concordance rows** (definitions, theorems, propositions, corollaries, lemmas, examples, counterexamples, conjectures, programmes). Everything else in the 128k canonical words is connective prose, motivation, discussion, and duplicated framing — which papers rewrite, not retain.

---

## 3. The routing map — where the 409 rows go

Measured from `canonical_concordance_A001_A025.csv` (destination routing closed 2026-08-26; scientific row-closure in progress, 152/409 `row_verified`):

| Destination | Rows | Share | Retention consequence |
|---|---:|---:|---|
| Paper 2 (theorem atlas) | 128 | 31% | The one genuinely long paper; split trigger pre-authorized (below) |
| Paper 5 (sampled governance/empirical) | 56 | 14% | Standard article; many rows are empirical-status rows needing statements, not proofs |
| Paper 4 (delay dynamics) + appendix/compendium | 54 + 13 | 16% | Main paper + the compendium appendix absorbs the overflow |
| Paper 3 (ledgers/diagnostics) | 54 | 13% | Standard article |
| **Negative/counterexample register** | 43 | 11% | **Retained as register entries** (statement + one-line reason + source pointer), not as article content |
| Paper 7 conditional (stage/spatial) | 20 | 5% | Published **only if** its independent gate closes; until then it is Paper 4 supplement material + docket |
| Paper 1 or monograph introduction | 18 | 4% | Architecture-level statements; most land in the monograph where length is free |
| **Conditional docket (open problems)** | 12 | 3% | Cited as open problems; not reproduced |
| Paper 6 conditional (NAIM/RFDE) | 8 | 2% | Gated on the B4 continuum transfer |
| Paper 1 if independent-result gate; else Paper 2 | 3 | 1% | Pending the novelty audit |

**Reading:** 55 rows (13%) are conditional-paper material that costs current-paper length **nothing** unless its gate closes (in which case it becomes its own paper's content — the architecture's honest fallback rule); 55 rows (13%) are register/docket entries costing a few lines each; 18 rows head to the monograph where there is no limit. The load on the five assured papers' main texts is roughly 313 rows plus connective material — and even that is not uniformly main-text: Paper 4's 13 appendix rows are already routed to the compendium appendix.

---

## 4. The per-paper length budgets

### Paper 2 — the measured precedent

The repo has already done this exercise exactly (`paper2_theorem_atlas_content_budget.md`, `paper2_retained_row_budget_report.md`):

- Gross A001+A002 intake: 40,582 words / 152 rows.
- After substantive routing (delegation, not deletion): **63 main rows + 7 bounded-appendix rows**; located formal source words 20,146; with a 35% connective/reproducibility allowance, preliminary manuscript equivalent **≈ 27,197 words** before bibliography and figures.
- 63 rows **delegated** to other papers or the monograph (retained elsewhere — not lost); 19 rows to the docket.
- **Pre-authorized split trigger:** if the verified venue budget fails, Paper 2 splits coherently by question into **2A (typed viability under observation and implementation)** and **2B (projectability, noncompensation, substitution, and composition limits)** — each with its own question, assumptions, complete proofs, examples, and referee audience. Not "results versus proofs."

The split logic generalizes: **the architecture's default response to a length failure is a coherent split, never destructive condensation.**

### The other assured papers — estimated loads

Using the same per-row retention economics (a retained row costs ≈ statement + classification + citation; a main-proof row costs its proof block; a delegated row costs a forward pointer):

| Paper | Routed rows | Expected shape | Length risk |
|---|---:|---|---|
| Paper 1 (general theory/architecture) | 18–21 | Architecture + axioms + the Operator II finite theorem + negative lessons | Low — most rows are statements; the deep content is delegated |
| Paper 3 (ledgers/diagnostics) | 54 | Primitive-flux ledger + conservation proofs + verified domain examples at exact status | Moderate — proof-heavy but the family is coherent |
| Paper 4 (delay dynamics) | 54 + 13 appendix | Named C3/C4 systems, Hopf analysis, Floquet/fold certification hierarchy, **the A1 4d true-periodic existence certificate** | Moderate — the certification narrative is self-contained; the appendix rows go to the compendium |
| Paper 5 (sampled governance/empirical) | 56 | Sample-and-hold theory + empirical designs + case statuses | Low–moderate — many rows are empirical-status statements |
| Wave E forecast papers (outside the A001–A025 numbering) | — | Already drafted: 3,427 + 3,523 words with full artifact trees as cited supplementary | **Closed** — submission-consistent per Tasks 42–43 |

If any paper's verified budget fails its venue, the response is the pre-authorized pattern: split by coherent question (e.g., Paper 3 → ledger theory / domain applications; Paper 4 → Hopf-dynamics / certification methods), with each fragment meeting the independence standard. **The architecture explicitly refuses to disguise extra papers as unlimited supplements** — which is the honest alternative to the failure mode the question worries about.

### Journal length mechanics (planning defaults; venue policies to be recorded at submission time)

- Ordinary mathematics / applied-mathematics articles: ≈ 25–40 pages ≈ 8–15k words main text; proofs routinely move to electronic supplementary material.
- Applied ecology / forecasting venues: ≈ 6–10k words; the Wave E papers (3.4–3.5k) sit comfortably inside.
- Supplementary material: effectively unlimited at most venues; the repo's hash-pinned artifact trees (the established Wave E pattern) are exactly this.
- Preprints: no length limit; full-length versions can live there permanently.
- The monograph: no limit — this is where A001/A002's full narrative and the v18-scale material are reintegrated.

Venue-specific policies are recorded per the Paper 2 budget's quantitative gate (`L_total ≤ L_target` with ≥10% revision buffer) when each paper reaches venue selection.

---

## 5. Where the 72,580-word manuscript fits

`SRC-A018-V18` (`uploads/manuscript_v18_dehedged.txt`) is the single largest document in the repo and the likely referent of "over 70 thousand words". Its registered status: **supplemental version received; not canonical pending version audit** (a registered open obligation). The retention facts:

1. It is a **version** of A018 (canonical 27,523 words), not additive content — the programme's non-merger/version discipline applies.
2. It is **retained in full** in the repository (layer 0) regardless of any publication decision.
3. Its disposition runs through the version audit: whatever it uniquely contains relative to canonical A018 either (a) enters the A018-destined papers (Papers 3/4 seam per the `A018_ledger_to_dynamics_interface_contract.md`), (b) enters the monograph, or (c) is recorded as superseded. It cannot silently inflate any paper, and it cannot be lost.
4. The v18-coupling assessment (`article_A021_liebig_graph/manuscript_v18_coupling_assessment.md`) is the standing partial audit.

The same discipline governs every other superseded or bridged source: **"no separate paper" never means deletion** — it means the destination is a paper section, a companion, the docket, or the negative register, with the source itself permanently archived.

---

## 6. What "about five papers" actually claims

The architecture's own final count:

- **Assured minimum:** 5 papers (General theory/architecture; Theorem atlas; Ledgers/diagnostics; Delay dynamics; Sampled governance).
- **Near-ready conditional:** Paper 6 (A021 NAIM persistence) — gated on the B4 continuum transfer.
- **Conditional methods extension:** Paper 7 (stage/spatial) — gated on its own independent result.
- **Domain papers conditional on empirical closure:** up to 3 (phosphorus A004, groundwater A005, distributive/adaptive A016).
- **Already drafted (outside this numbering):** the two Wave E scored-forecast papers (cod 2J3KL negative certificate; Edwards Ω_SA first positive selection) with their intervention companions.
- **Synthesis products:** the monograph (uncompressed) + the versioned reproducibility compendium.

So the honest expected count is **5 assured + 2 Wave E + likely 6, potentially 7+ as gates close, plus up to 3 domain papers, plus the monograph** — a series of 8–13 citable objects, with the monograph and compendium as the unlimited-length retention backstops and the repository as the permanent archive.

**The five-paper number is a floor, not a container.** What makes it honest is precisely the discipline the programme already runs: every one of the 409 inventoried rows has a destination; every destination failure triggers a coherent split rather than condensation; every rejected or superseded source survives as a negative record or archived version; and the definitive reintegration is a monograph, not a journal article.

---

## 7. Current obligations this budget keeps open

1. **Paper 2 venue gate:** after exact proof verification, compute `L_total` against the selected venue; split 2A/2B if the gate fails (pre-authorized).
2. **SRC-A018-V18 version audit:** pending; nothing in this budget pre-empts it.
3. **Scientific row-closure campaign:** 152/409 rows `row_verified` (A001, A002 complete); 214 + 15 remain across 20 sources — the row-level verification that the budgets above assume.
4. **Paper 1 independent-result gate:** the Operator II novelty/nonduplication audit decides journal-article vs monograph-introduction status for its 18+3 rows.
5. **Part III paper-support rows:** close against finalized papers (NOT CONFIRMED by design until the papers exist).
6. **B4 continuum transfer:** unlocks Paper 6's gate (8 conditional rows + the A1 campaign's certified orbit as Paper 4's capstone content).

---

## Interpretation

The length problem is real but it is **solved by architecture, not by compression**: three-tier retention (repo → papers → monograph), row-level destination routing (409/409 routed), pre-authorized coherent splits (Paper 2A/2B; Paper 7's supplement-to-paper fallback), conditional papers that cost nothing until their gates close, register/docket destinations for negative and open content, and unlimited-length backstops (monograph + compendium + supplementary + preprints + the repository itself). The gross word counts (200,507 registered; 127,927 canonical; 97,758 corrected-article words) measure intake pressure; the publication-bound load is the 409-row inventory distributed as above, and the single genuinely tight case (Paper 2, ≈27.2k preliminary) already carries its split trigger. No valid result is lost at any point in this pipeline — the non-loss rule is checkable row by row, and 100% of rows are routed.
