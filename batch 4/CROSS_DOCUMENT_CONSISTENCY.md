# CROSS_DOCUMENT_CONSISTENCY — Claims vs. the Honest-Status Register

**Scope.** Item 3 of the agreed plan: find claims in the strategy, manuscript, and record documents that outrun the statuses in `PROOF_MANIFEST.md` and the audit findings.

**Corpus.** `PROOF_MANIFEST.md`, `TRANSFER_AUDIT_RESPONSE.md`, `JOINT_AUDIT_ASSESSMENT.md`, `batch 2/03_publication_strategy/PUBLICATION_STRATEGY.md`, `batch 2/04_open_problems/*` (13 files), the three top-level manuscripts (`.md` + `.docx`), both traceability reports, `revised_articles/` (24 files), both Wave E manuscripts, and `research_program/article_A021_liebig_graph/`.

**Reproducible check:** `reaudit/verify_consistency.py` (exit 0; output `reaudit/consistency_output.txt`).

---

## Headline

**The status discipline holds where it was deliberately installed and breaks where it wasn't.** All five Part-V-forbidden claims are absent from every manuscript and strategy document. The E5 transfer prohibition, the TCS-1.1 freeze, and the three-object real-system table are enforced consistently and correctly across the post-audit documents. The `.docx` artifacts are in sync with their `.md` sources. The four theorems refuted in item 1 are not cited downstream as proved.

Eight defects found. The pattern is uniform: **every one sits in a document that predates the audits or was left off a repair list.** The manifest, `PUBLICATION_STRATEGY.md`, `D_TIER_EMPIRICAL_AGENDA.md`, and both Wave E manuscripts were repaired and are clean. `WAVE_E_UPDATE.md` was not repaired. The manuscripts and traceability reports predate the audits entirely.

| Document | Last commit | Clean? |
|---|---|---|
| `PROOF_MANIFEST.md` | `fe4efc0` 08-25 | yes (authoritative) |
| `PUBLICATION_STRATEGY.md` | `4af53e4` 08-25 | yes — except C2 |
| `TRANSFER_AUDIT_RESPONSE.md` | `4af53e4` 08-25 | yes |
| Wave E manuscripts (both) | `4af53e4` 08-25 | yes |
| `D_TIER_EMPIRICAL_AGENDA.md` | — | yes |
| **`WAVE_E_UPDATE.md`** | — | **no — C3, C4, C5** |
| **Manuscripts (3) + traceability (2)** | `6ef8299` 08-23 | **pre-audit — C7, C8** |

---

## What passes

**Part-V forbidden claims: none appear.** I searched every `.md` and `.tex` in the repository for all five claims `PROOF_MANIFEST.md` Part V lists as not-yet-citable. Each pattern matches **only** the manifest row that forbids it:

| Forbidden claim | Assertions outside the manifest |
|---|---|
| "The continuum orbit exists within a declared ball" | 0 |
| "The bunching inequality closes in the continuum" | 0 |
| "The NAIM persistence theorem's hypotheses are verified" | 0 |
| "Every governance claim is decidable against the calibrated model" | 0 assertions — 1 mention, in `CA_EXECUTION.md`, quoting it as a **prohibition** ("never … without the two extra verifications") |
| "The fold is certified for the continuous DDE" | 0 |

(The bunching pattern does occur in `product_prefactor_bunching_assessment.md`, correctly scoped to a *numerical C1 product* result — see C6.)

**TCS-1.1: no document asserts it is controlling.** Zero assertions across the tree. Every reference outside `TCS_1_1_FREEZE.md` is a migration obligation, a proposal, or an explicit denial ("zero records conform to TCS-1.1"; "No compatibility claim 'valid under TCS-1.1' is available").

**E5 transfer prohibition: enforced everywhere it matters.** `PUBLICATION_STRATEGY.md` Papers 3 and 5 both carry the toy-scope qualifier; `D_TIER_EMPIRICAL_AGENDA.md` states "These numbers are the linear toy's — they support no claim about the real fishery"; the Edwards Wave E manuscript states "It does not confirm E5 interval-verified admission, E7 sandwiches, Stackelberg, or a frozen TCS-1.1 … E5 is not this Ω"; the cod manuscript lists "E5, E7, B10, interval Hopf, TCS-1.1-as-frozen" among *unmatched* session IDs. The three-object table separating NAFO 2J3KL / Edwards well J-17 / A021 C4 J-series is explicit and correct.

**TCS-1.1: no document presents it as controlling.** Every reference outside `TCS_1_1_FREEZE.md` is either a migration obligation, a proposal, or a denial.

**`.docx`/`.md` sync: no stale Word artifacts.** All three manuscript pairs match — character-count ratios 0.997 and opening text identical after markup stripping.

**Item-1 refutations are contained.** `A3.Thm1`, `B6.Thm1`, `E4.Thm2`, and `E4.Lem1` are not cited as proved anywhere downstream. The only external reference is `E6_EXTERNAL_MATCHING_MATRIX.md`, which lists A3's compactness as a candidate novelty to check against the literature — the correct treatment.

---

# Findings

## C1 — `A3_KERNEL_CERTIFICATE.json` is a dangling artifact reference

The file is named twice as an existing artifact and exists nowhere in the repository (`find` over the full tree returns nothing). Both mentions are in `A3_VARIABLE_EVENT_KERNEL.md`:

- provenance header: "The kernel *computation* artifact (A3_KERNEL_CERTIFICATE.json) is a **toy instance** … COMPUTED_PARTIAL"
- status section: "**A3 kernel computation (A3_KERNEL_CERTIFICATE.json): COMPUTED_PARTIAL** — a 1-D toy instance verifying the class conditions"

`PROOF_MANIFEST.md` line 138 registers the same object under a description rather than a filename — "| A3 toy kernel | 1D system on the declared class | **COMPUTED_PARTIAL** | Toy instance; no Wave E relevance |" — so nothing in the register points at the missing file either.

Worth noting for accuracy: the manifest's "Partial computations (COMPUTED_PARTIAL)" table has columns *Artifact | Description | Status | What is missing* and carries **no file path and no SHA-256 for any of its five rows**, unlike Part II's computation tables which carry both. So the A3 row is not anomalous within its table — but that means all five `COMPUTED_PARTIAL` statuses in that table are untraceable to an artifact by construction, and in this one case the named artifact does not exist at all.

**Fix.** Either commit the artifact, or change the row to `SPECIFIED` / `NOT IN TREE` and strike the two citations in the A3 file. Separately, adding a path column to the COMPUTED_PARTIAL table would make all five rows traceable.

## C2 — the published reproduction command fails, and step 1 corrupts the pinned panel

`PUBLICATION_STRATEGY.md` §Real-system referents gives:

```
wave_e_edwards/ — python3 src/build_panel.py && python3 src/build_climate.py \
                  && python3 src/run_ladder.py && python3 src/run_recharge.py
```

I ran it. Two failures in sequence:

1. `build_panel.py` overwrites `data/annual_panel.csv`, emitting 15 columns instead of 20 and dropping all five climate columns. The hash moves off the pinned `d6d725db…` (item 2, finding F4).
2. `build_climate.py` raises `FileNotFoundError: .../climdiv-pcpndv-v1.0.0-20260806` and **exits 1**. The `&&` chain aborts; neither ladder ever runs.

The parenthetical immediately following the command already contains the answer — "nClimDiv raw file omitted … `annual_panel.csv` already carries the derived columns" — which is precisely why `build_panel.py` must not be run. `PROOF_MANIFEST.md` Part VI gets this right ("uses committed `data/annual_panel.csv`"); the strategy document does not.

**Fix.** Replace with `python3 src/run_ladder.py && python3 src/run_recharge.py`, and move the panel/climate rebuild into a separate note flagged as requiring the uncommitted nClimDiv file.

## C3 — `WAVE_E_UPDATE.md` §2 labels computations as proofs

Five rows in the §2 table read "Committed and **PROVEN**", "Committed and **VALIDATED**", or "Committed and **INTERVAL-CERTIFIED**":

| Row | Label used | Manifest's actual classification |
|---|---|---|
| E5 module admission | "Committed and PROVEN" | Part II, *Discrete-level validated computations* — a computation, `E5_NUMBERS.json` |
| C4 orbit Krawczyk | "Committed and PROVEN at K=80" | Part II computation; Part IV citation form is "certified with local uniqueness at the K=80 level (discrete)" |
| A025 Hopf certificates | "Committed and PROVEN" | Part II computation |
| C4 monodromy/Floquet | "Committed and VALIDATED" | not a manifest vocabulary term |
| C4 off-grid residual | "Committed and INTERVAL-CERTIFIED" | not a manifest vocabulary term |

The manifest's vocabulary is declared "mandatory, no exceptions" and reserves `PROVEN` for "formal proof, **self-contained in the cited file**". None of these five is a proof. Notably the same document's §1 handles the *theorems* correctly ("all statuses are `PROVEN (reconstructed)` … reconstructed ≠ closed atlas content"), so the defect is local to §2.

## C4 — three-way disagreement on whether B1 closes R02.Cor6

| Document | Statement |
|---|---|
| `PROOF_MANIFEST.md` line 46 | "R02.Cor6 \| Eroded closed-loop safety \| … \| **PROVEN_CONDITIONAL (sampled-data erosion bridge open)** \| Demoted from 'proved'" |
| `B_TIER_BRIDGES.md` | "B1 — Sampled-Data Erosion Theorem — **PROVED (closes R02.Cor6's bridge)**" |
| `WAVE_E_UPDATE.md` §1 | "R02.Cor6's bridge is **now a theorem, not a conditional**. Paper 5's governance-design section can cite it directly." |
| `PUBLICATION_STRATEGY.md` Paper 5 | "sampled-data erosion theorem (B1) **closes R02.Cor6's bridge**" |

Three documents assert closure; the authoritative register still records the bridge as open. Item 1's finding #8 found B1.Thm1's *conclusion* over-scoped relative to its hypotheses (the "verbatim `K_{−r}`" step needs a successor certificate at depth `3r/2` that hypothesis 3 doesn't supply) — which suggests the manifest is the correct one and the other three are premature.

**Fix.** Reconcile on the manifest's side: B1 closes the bridge *at the depth its hypotheses deliver*, not at the stated `r`. Update the three asserting documents, or strengthen B1's hypothesis 3 and then update the manifest.

## C5 — `WAVE_E_UPDATE.md` retains the pre-audit E5 framing that Finding 2 repaired elsewhere

"What does NOT need updating" table: *"Fisheries as the G1 case \| Unchanged — **E5's admission makes it stronger, not different**."*

`TRANSFER_AUDIT_RESPONSE.md` Finding 2 identified exactly this under-scoping — documents treating the E5 linear-toy admission as strengthening a real-system claim. Its numbered repair list (items 1–4) covers `E5_MODULE_ADMISSION_NUMERICAL.md`, `PUBLICATION_STRATEGY.md`, `D_TIER_EMPIRICAL_AGENDA.md`, and `PROOF_MANIFEST.md`. `WAVE_E_UPDATE.md` is absent from that list.

The omission is sharper than a simple miss, though: the same commit **did** edit `WAVE_E_UPDATE.md` — line 87 records "`OPEN_PROBLEMS_REGISTER.md` and `WAVE_E_UPDATE.md`: C-h/G6 entries annotated with the non-controlling status" under Finding 3, and line 114 records "`WAVE_E_UPDATE.md`'s 'add B10/A4/E7' instruction qualified — reconstructed ≠ closed atlas content" under the repair summary. The file was in hand and two of its claims were corrected; the E5 row in "What does NOT need updating" was left standing.

Given R04.Thm1's converse forbids transfer without a five-map certificate that doesn't exist, "E5's admission makes it stronger" is not supportable for 2J3KL.

The same file's §2 row — "E5 module admission \| Paper 3's worked example + Paper 5's template \| Committed and PROVEN" — likewise lacks the toy-scope and transfer-prohibition qualifier that every other document now carries.

## C6 — the register carries a superseded, more optimistic bunching figure

`PROOF_MANIFEST.md` line 137: "B4 bunching (**n=15 periods**) \| Discrete stable-complement powers + slack decay \| COMPUTED_PARTIAL". `B_TIER_BRIDGES.md` B4: "close at `n = 15` periods (value 0.649) … **Unchanged from STATUS_CORRECTION.md**. Not re-labeled."

But `research_program/article_A021_liebig_graph/product_prefactor_bunching_assessment.md` — whose four reproducibility artifacts I confirmed all exist — concludes:

> "The numerical `C1` product bunching inequality closes only marginally at 30 periods but robustly by **35 periods** … This directly confirms the audits' warning that **the stable multiplier alone cannot establish bunching**."

with the correct status `NUMERICALLY_VERIFIED_DISCRETE_PRODUCT_BUNCHING_AT_35_PERIODS` and the explicit caveat "It is not a continuum operator bound."

Neither `PROOF_MANIFEST.md` nor `B_TIER_BRIDGES.md` cites that assessment. So the register's headline number is the stable-multiplier-only figure that the later prefactor-aware assessment supersedes — the register is **more optimistic than the committed evidence**, in the direction that matters, for the artifact Paper 4's NAIM capstone rests on (Part III row: "B4 discrete bunching + A2 coupling declaration … NOT CONFIRMED").

**Fix.** Update the B4 row to the 35-period prefactor-aware figure, cite the assessment, and keep `COMPUTED_PARTIAL` (the assessment's own status agrees).

## C7 — two disjoint status vocabularies, no crosswalk

`PROOF_MANIFEST.md` declares six terms "mandatory, no exceptions": `PROVEN`, `PROVEN_CONDITIONAL`, `PROVEN (reconstructed)`, `COMPUTED_PARTIAL`, `SPECIFIED`, `OPEN`.

The manuscripts use an entirely different system: a nine-category epistemic taxonomy (*Definition/architectural postulate, Identity, Theorem, Conditional theorem/lemma, Conjecture, Numerical proposition, Empirical hypothesis, Normative postulate, Research programme*), plus `[P]/[E]/[N]/[L]` claim-type tags, plus seven box types. I searched for a mapping between the two systems and found none.

Consequence: a reviewer holding `revised_sustainability_manuscript.md` cannot check any of its "Theorem" boxes against the register's status for the same result. The manuscripts are the publication artifacts; the manifest is the register; nothing connects them.

**Fix.** A one-page crosswalk (manuscript category → manifest term) appended to the manifest, or a status column added to the manuscripts' box inventory.

## C8 — the traceability documents don't trace status, and predate the audits

`general_theory_of_sustainability_traceability.md` (dated 14 August) and `revised_manuscript_traceability.md` (17 August) map *source concepts → manuscript locations* with treatments like "Retained" / "Expanded" / "Restored" / "Retained with claim-type qualification". Neither references `PROOF_MANIFEST.md` or carries a single status label.

Timeline: traceability reports 14–17 Aug → manuscripts 23 Aug → audits and manifest 25 Aug. So no document anywhere in the repository maps the post-audit statuses onto the manuscripts. Combined with C7, the publication artifacts are currently unreachable from the register.

---

# Root cause

One cause explains C3 through C8. The audits of 25 August produced a repair list, and the repair list was executed — thoroughly, in `PUBLICATION_STRATEGY.md`, `D_TIER_EMPIRICAL_AGENDA.md`, `PROOF_MANIFEST.md`, `E5_MODULE_ADMISSION_NUMERICAL.md`, `OPEN_PROBLEMS_REGISTER.md`, `A2_COUPLING_CLASS.md`, and both Wave E manuscripts. But it was a **claim-by-claim** repair, not a sweep. `WAVE_E_UPDATE.md` shows this most clearly: it was opened and edited in that commit — two of its claims were corrected — yet three others survived (C3's computation labels, C4's bridge claim, C5's E5 row), because the repairs were driven by the specific findings enumerated in each audit rather than by a pass over the document. The 23 August manuscripts and the 14–17 August traceability reports were never in scope at all (C7, C8). C1 and C2 are independent of the audits: a dangling artifact reference, and a reproduction command that was never executed end-to-end.

A grep for the manifest's own vocabulary across the tree would have caught C3 in one pass. That check does not currently exist as a committed tool; `reaudit/verify_consistency.py` implements it.

---

# What I did not check

- **`revised_articles/` A001–A025 in depth.** I searched all 24 for the Part-V patterns and the E5/TCS-1.1 disciplines and found no hits, but I did not read them against the register claim-by-claim. A018 alone is 183 KB.
- **`uploads/` and `research_program/external_reviews/`.** These are inputs and captured audits, not programme claims, so I treated them as out of scope.
- **Whether the manuscripts' internal "Theorem" boxes are actually proved.** That is a much larger job and belongs with the item-1 method, applied to the manuscript theorem inventory rather than the session files.
- **The `.docx` build scripts.** I verified the `.docx` files match their `.md` sources; I did not re-run `build_*_docx.py` to confirm the generators still produce them.
