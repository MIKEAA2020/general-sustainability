# TRANSFER_AUDIT_RESPONSE — Three Findings on the Transferred Session Work

**Scope:** response to the external audit of the transferred files (`general-sustainability-session-work.zip` / `full-session-work.patch`, as applied to `main` in commits 18bfccc…f07674b). Each finding is verified against the actual files, accepted or qualified with evidence, and repaired. All repairs are committed with this document.

---

## Finding 1 — The theorem files (E1–E7, A4, B10, C-a) are short "cards" (0.6–1.7 KB), not full 17-field proofs

**Verdict: ACCEPTED in full. Verified.**

Evidence (file sizes in the applied tree):

| File | Size |
|---|---|
| `C_TIER_COMPLETIONS.md` | 569 B |
| `E6_EXTERNAL_MATCHING_MATRIX.md` | 599 B |
| `E5_MODULE_ADMISSION_NUMERICAL.md` | 614 B |
| `E4_INTERGENERATIONAL_PRODUCTION.md` | 725 B |
| `CA_EXECUTION.md` | 743 B |
| `A3_VARIABLE_EVENT_KERNEL.md` | 745 B |
| `E7_CONSERVATION_VIABILITY_COUPLING.md` | 785 B |
| `A4_NONLINEAR_SMALL_GAIN.md` | 822 B |
| `A2_COUPLING_CLASS.md` | 848 B |
| `A1_CONTINUUM_LIFT_STATUS.md` | 979 B |
| `TCS_1_1_FREEZE.md` | 988 B |
| `E1_LANGUAGE_COMPLETENESS.md` | 1,043 B |
| `E2_SELECTORS_AND_CERTIFICATES.md` | 1,083 B |
| `E3_CLASSIFICATION_THEOREMS.md` | 1,258 B |
| `B_TIER_BRIDGES.md` | 1,662 B |

**Root cause (recorded honestly):** the long-form originals were lost to two filesystem resets of the working environment (worklog Task 10, Task 13). The Task-13 rebuild recreated *all* lost documents "from the worklog documentation (abbreviated where the originals were longer)". The result is exactly what the audit found: statement-plus-sketch cards, not self-contained proofs.

**Why this mattered beyond brevity:** `PROOF_MANIFEST.md`'s own vocabulary defines `PROVEN` as "formal proof, **self-contained in the cited file**". Roughly 30 manifest rows cited card files under that label. Under the manifest's own definition those statuses were inflated — the proofs existed in the session record (chat worklog), not in the repository.

**Repair (this commit):**
1. Every theorem-bearing card is **expanded to a full self-contained proof document**: exact statement with all hypotheses, phase space, complete proof, necessity/scope counterexamples, honest status, provenance, and dependency edges (the load-bearing subset of the 17-field record schema — Fields 3, 4, 6, 8, 9, 16, 17; the remaining fields are record-format items specific to batch-2 docket records and are marked N/A for internal theorems).
   - Expanded: E1, E2, E3, E4, E5, E6, E7, A3, A4, B_TIER_BRIDGES, C_TIER_COMPLETIONS, CA_EXECUTION, plus the TCS-1.1 freeze card (Finding 3) and the A1/A2 status documents (provenance headers added).
2. Two stale cross-references inside the cards are reconciled: E3.C2 described the nonlinear substitution classification as a "conjectural bridge" although the later B-tier wave **proved** it (B6); E3.C5 described the bifurcation transversality classification as "stated, not proved" although B7 **proved** it. The expanded E3 states both at their proved scope with cross-references.
3. `PROOF_MANIFEST.md` is corrected: every session-theorem row now carries the honest per-file status `PROVEN (full proof in file — reconstructed and expanded this commit)` or the specific weaker label where a component remains conditional/partial.
4. **Provenance discipline:** each expanded file carries a header stating that the proof is a reconstruction from the session record (worklog Tasks 3–8) after the filesystem loss, so downstream readers can trace provenance rather than trusting a bare "PROVEN".

**Residual (not fixable here):** the reconstruction is by the same agent that produced the originals; it is *not* an independent re-derivation. The independent-rerun obligation (HONEST_DISCLOSURE.md) extends to the proofs: before any Wave E submission, a second party must re-verify the expanded proofs line-by-line. No status was upgraded by the expansion — the labels reflect the same mathematical content, now with the proof actually in the file.

---

## Finding 2 — E5 is a linear (S,K)×(S,K) toy model, not the scored 2J3KL or J-17 series; it cannot support any claim about the real system without a valid transfer (R04 forbids transfer)

**Verdict: ACCEPTED in full. Verified.**

Evidence:
- `E5_NUMBERS.json` records `"module.source": "A001 topdown source, Section 6 (lines 740-960), Theorems 6.1/6.2/6.3"`, `"phase_map": "identity on (S,K)"`, and the verdict string `"ADMITTED WITH NUMBERS (linear resource-sink, declared scope)"`. The admitted object is the **linear** resource–sink: closed-form kernel `[2,∞)×[0,2]`, constant policy `H ≡ H_min`.
- The real systems named by the audit are of a different class entirely: the northern-cod program (NAFO **2J3KL**; A014 revised article, A016 crosswalk population) and the scored delay-model series of the A021 joint docket (the **J-series**, including J17 — the BLZ exact-theorem citation item), whose C4 gated DDE is the object of the validated computations (C1/C2/C3 dockets).
- **R04.Thm1's converse** (batch-2 record, Field 8) proves that no judgment transfers without the five-map admission certificate (type/unit, phase-space, dynamics, safe-set, policy/information correspondence); `ANALOGY_ONLY` is *excluded from transfer by the theorem*. No five-map certificate exists from the linear (S,K) toy to 2J3KL or to any A021 J-series model. Therefore **no statement proved about the E5 module supports any claim about the real system.**

Where the transferred documents under-scoped this (now repaired):
- `PUBLICATION_STRATEGY.md` listed "E5's interval-verified numerical admission as the worked example" (Paper 3) and "the E5 admission template for case screening" (Paper 5) without the toy-scope qualifier.
- `D_TIER_EMPIRICAL_AGENDA.md` stated "fisheries resource–sink as the primary G1 case … all mathematics is in place" — true only **for the linear module**; it did not state that the G1 empirical case (real 2J3KL data against a scored model) additionally requires an R04 admission of that scored model (or a Cor2 approximate admission with erosion), neither of which exists.
- The E5 card itself carried no scope-and-transfer-prohibition section.

**Repair (this commit):**
1. `E5_MODULE_ADMISSION_NUMERICAL.md` is expanded to the full admission record **with a mandatory "Scope and transfer prohibition" section**: the numbers are the linear A001 §§6–10 toy's; the module admitted into the architecture is the toy (per R04.Tab3, the only complete five-map certificate in the programme); transfer to 2J3KL/J-17-class models requires the R04 certificate, which does not exist; Cor2 approximate admission is the only other route and is likewise not constructed.
2. `PUBLICATION_STRATEGY.md` (Paper 3/5 rows, consolidation decision, G1 row) now carries the explicit qualifier: E5 is a **method demonstration on the linear module**, not evidence about any real fishery.
3. `D_TIER_EMPIRICAL_AGENDA.md` readiness matrix and decision section now state the two-track reality: the E5 track (linear module, numbers committed) and the real-system track (2J3KL/J-17 scored models), with the R04/Cor2 transfer requirement named as a **gating item for G1**, and the corrected claim of what "all mathematics is in place" covers.
4. `PROOF_MANIFEST.md` Part IV citation form for E5 corrected to: "The **linear A001 §§6–10 resource–sink module** is admitted with interval-verified numerical constants (method demonstration; no transfer to 2J3KL/J-17-class systems without the R04 certificate)".

**What E5 legitimately remains:** the programme's first complete worked example of the admission method (five maps exact, interval-verified constants, displayed (REG) family) and the template for case screening — exactly what Paper 5 needs as a *method* exhibit. Nothing more.

---

## Finding 3 — TCS-1.1 is only a freeze card; the controlling schema is still TCS-1.0

**Verdict: ACCEPTED in full. Verified.**

Evidence:
- `TCS_1_1_FREEZE.md` (988 B) is a **diff specification**: five new types, seven mandatory fields, registry layering, a five-entry composition gate, status vocabulary, migration checklist. It freezes the *diff*; it does not migrate any record.
- `control/01_canonical_system_schema_TCS_1_0.md` §10: "TCS-1.0 is frozen. A change … creates TCS-1.1 … and **requires migration entries** in the concordance." No migration entries exist; every batch-2 record and every packet theorem is a TCS-1.0 record.
- The transferred documents nonetheless read as if TCS-1.1 were operative: `PUBLICATION_STRATEGY.md` G6 status "**FROZEN**" and the Wave-0 row "G6 (**done**)"; `OPEN_PROBLEMS_REGISTER.md` "C-h: TCS-1.1 FROZEN"; `WAVE_E_UPDATE.md` "G6 … is FROZEN". Frozen ≠ controlling: the diff being frozen does not make TCS-1.1 the schema of any existing record.

**Impact (as the audit states):** any formalisation or compatibility claim must be checked against **TCS-1.0**, not TCS-1.1. In particular:
- E1's language completeness is relative to the **TCS-1.0 §4** eight judgment families (the frozen judgment inventory the theorems actually quantify over).
- C-a's decidability is decidability of the **TCS-1.0** judgment language at fixed data.
- No compatibility claim "valid under TCS-1.1" is available to any theorem, record, or artifact in the programme. (The one prior claim of that form — the master review's "valid under both TCS-1.0/1.1" — was already withdrawn in the session's Wave-4 repairs; nothing reintroduced it, but the strategic documents' "G6 done" phrasing invited exactly this audit's finding.)

**Repair (this commit):**
1. `TCS_1_1_FREEZE.md` is expanded with a mandatory **controlling-schema header**: TCS-1.0 controls; TCS-1.1 is a frozen, **unapplied** diff; zero records conform to TCS-1.1; the migration checklist is an open obligation whose completion is a precondition for *any* TCS-1.1-scoped claim; the E1/C-a formalisation scope is TCS-1.0.
2. `PUBLICATION_STRATEGY.md`: G6 status corrected to "FROZEN (diff only — **not controlling**; TCS-1.0 controls; migration open)"; the Wave-0 row corrected from "G6 (done)" to "G6 diff frozen; migration NOT done".
3. `OPEN_PROBLEMS_REGISTER.md` and `WAVE_E_UPDATE.md`: C-h/G6 entries annotated with the non-controlling status.
4. `PROOF_MANIFEST.md`: a controlling-schema statement is added; the E1 and C-a rows are explicitly scoped to the TCS-1.0 judgment language.

**Residual:** the TCS-1.1 migration itself is deliberately **not** executed in this repair — running the migration would change the schema under ~40 records and requires the concordance machinery; it is registered as an open Wave-0 obligation with its checklist. This is a scoping decision recorded here, not an omission.

---

## Repair summary

| # | Finding | Verdict | Repaired in this commit |
|---|---|---|---|
| 1 | Cards, not proofs | ACCEPTED | 13 theorem documents expanded to full self-contained proofs with provenance headers; manifest statuses corrected to per-file honesty; E3's two stale cross-references reconciled |
| 2 | E5 toy-scope / R04 transfer prohibition | ACCEPTED | E5 expanded with mandatory scope-and-transfer-prohibition section; strategy + D-tier + manifest claims re-scoped; G1 gating item added |
| 3 | TCS-1.1 freeze-only | ACCEPTED | Freeze card expanded with controlling-schema header; G6/C-h statuses corrected everywhere; manifest carries the controlling-schema statement |

**Not changed by this repair (honest boundaries):** no theorem's mathematical status was upgraded; the independent-rerun obligation is unchanged (NONE for all artifacts); the A1 piecewise-Chebyshev campaign, A3 residue, B4 continuum transfer, and external audit execution remain open exactly as HONEST_DISCLOSURE.md records them.

---

## Postscript (follow-up audit): the "J-17" identification — three objects, not one track

A follow-up audit finding, **verified and accepted**: Finding 2's evidence section *misidentified* "J-17". It wrote that the audit's "J-17 series" is "the scored delay-model series of the A021 joint docket (the J-series, including J17 — the BLZ exact-theorem citation item)". That identification is wrong in two ways, and the shorthand "2J3KL/J-17-class systems" / "the real-system track (2J3KL/J-17)" that propagated from it into E5, the strategy, the D-tier agenda, the register, A2, and the manifest collapsed **three distinct objects**:

1. **NAFO 2J3KL** — the northern-cod fishery (A014/A016): a real system (the G1a fisheries case).
2. **Edwards well J-17** — the Edwards Aquifer index well (San Antonio): a real system on the groundwater side (the G1b referent). The Edwards Aquifer critical-period management system was examined as a case candidate in the manuscript's case search and **rejected on the confound gate**; A005 is a generic typed template, not Edwards-calibrated. For an Edwards-type system, **Cor2 approximate admission is forecast-map only** (a screening/forecast map with eroded kernels — not a certified admission licensing transfer).
3. **The A021 C4 J-series** — the joint-decision-docket items J01–J25 (J17 = the BLZ citation-matching disposition): **audit bookkeeping, not a real system**. The C4 gated DDE is a programme model equation; no "scored (J-17-series) model" exists, and the validated C4 computations support no claim about any fishery or aquifer.

**Repairs applied (this commit):** three-object tables added to `PUBLICATION_STRATEGY.md` and `D_TIER_EMPIRICAL_AGENDA.md`; the collapsed phrasing retired in `E5_MODULE_ADMISSION_NUMERICAL.md` (scope section, Field 16), `PROOF_MANIFEST.md` (header, Part II row, Part IV citation form, closing note), `OPEN_PROBLEMS_REGISTER.md` (G1), and `A2_COUPLING_CLASS.md`; independent-rerun status remains **NONE** everywhere; the Paper 6/7 folds restated as **proposals, not gates** (the Paper 4 capstone they fold into is itself NOT CONFIRMED; the A025 fold pipeline is NOT REBUILT); `WAVE_E_UPDATE.md`'s "add B10/A4/E7" instruction qualified — reconstructed ≠ closed atlas content, **Wave E is not closed**.

**Honest residual:** this postscript corrects the *referent* of the transfer prohibition; it does not weaken the prohibition itself — R04.Thm1's converse applies to each of the three objects separately, and no five-map certificate exists from the linear (S,K) toy to any of them.
