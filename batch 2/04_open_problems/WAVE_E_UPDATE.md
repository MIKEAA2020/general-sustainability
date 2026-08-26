# Wave E Design Update — Findings from This Session

**Question:** Does the Wave E design described in the repository require updating to meet findings from this session?

**Answer: Yes — in three specific ways.** The core architecture (five papers, fisheries as the G1 case, the publication waves) is unchanged. But the session produced new theorems, new computational artifacts, and status corrections that the Wave E documents do not yet reflect.

---

## What changed and what it means for Wave E

### 1. New theorems strengthen Papers 1–3 (not yet reflected) — **all statuses are `PROVEN (reconstructed)`**

The following results are recorded in the session theorem files, but **every one of them is a same-agent reconstruction after the filesystem loss** (TRANSFER_AUDIT_RESPONSE Finding 1; PROOF_MANIFEST.md vocabulary): reconstructed ≠ closed atlas content. They may be added to the paper descriptions **only with that qualifier**, and Wave E does not close on them until the independent line-by-line re-verification (the Wave-0 gate) is done:

| Theorem | Paper it strengthens | How |
|---|---|---|
| **A4** Nonlinear assume–guarantee (monotone-operator theorem) | Paper 2 (atlas) + Paper 1 (composition lesson) | The composition gate now has FOUR theorems (not two): the restricted proximal-normal, the tubular A–G, the eroded generation transfer, and the nonlinear monotone-operator version. Paper 2's composition section is substantially richer. |
| **B1** Sampled-data erosion theorem | Paper 5 (governance design) | R02.Cor6's bridge is closed **at the two-depth form** (B1.Thm1 repaired: a sample-time certificate at depth `R` converts to continuous-time safety at depth `r` at the cost `V_max T_s ≤ R − r`; the invariance reading of the original headline is refuted and withdrawn). Paper 5's governance-design section can cite it with that depth bookkeeping. |
| **B9** Stochastic viability (chance-kernel, filter soundness, quantile erosion) | Paper 2 (atlas) + Paper 5 | The stochastic layer — previously a docket item (D3) — now has proved restricted results. |
| **B10** Stackelberg equilibrium existence | Paper 1 (architecture) | The strategic-implementation docket (D5) has its foundational record. Paper 1's institutional section can acknowledge the reduction. |
| **C-a** Decidability at fixed data | Paper 1 (scope) + Paper 5 (computability) | Every governance claim is decidable on the finite class. Paper 5's empirical falsification design is backed by a computability theorem. |
| **E7** Conservation–viability coupling | Paper 3 (the "so what") | Moiety barriers produce kernel bounds from flux data alone. This is Paper 3's missing bridge between conservation and viability. |

### 2. New computational artifacts upgrade Paper 4 (partially reflected)

| Artifact | What it upgrades | Status |
|---|---|---|
| C4 orbit Krawczyk (margin 1186) | Paper 4's certified-computation section | Committed; **interval computation certified with local uniqueness at the K=80 level (discrete)** — Part II validated computation, not a proof |
| C4 off-grid residual (interval-certified v2) | Paper 4's continuum-lift evidence | Committed; interval-verified residual bounds (Part II computation; manifest vocabulary: COMPUTED_PARTIAL-adjacent, no `INTERVAL-CERTIFIED` status exists) |
| C4 monodromy/Floquet (dt=0.25) | Paper 4's cycle stability | Committed; validated computation (not a manifest vocabulary term — Part II row) |
| A025 Hopf certificates (interval) | Paper 4's Hopf section reproducibility | Committed; interval computation with outward-rounded coefficients (Part II) |
| E5 module admission | Paper 3's worked example + Paper 5's template | Committed; **interval-verified admission of the linear A001 §§6–10 toy** (Part II computation; toy scope, R04 transfer prohibition applies) |
| **A025 fold Moore–Spence Krawczyk** | Paper 4's fold certification | **NOT REBUILT** — the fold pipeline script is committed but the computation stalls |

### 3. Status corrections the Wave E documents must respect

The audit imposed a mandatory vocabulary and the rule "no gate is closed for Wave E." The Wave E documents (D_TIER_EMPIRICAL_AGENDA.md, PUBLICATION_STRATEGY.md) still use the original optimistic phrasing in places.

| Document | What needs updating |
|---|---|
| `D_TIER_EMPIRICAL_AGENDA.md` | The readiness matrix should note that the E5 admission is committed and reproducible (with SHA-256 hash), not just "complete." The three preregistered protocols should reference the E6 matching matrix for their external-literature obligations. |
| `PUBLICATION_STRATEGY.md` | The G-item statuses are stale: G2 (coupling) is now DECLARED, not just open; G4 (selectors) has a proved measurable half; G6 (TCS-1.1) is FROZEN. The Paper 2 content description should include the new theorems (A4, B1, B9, B10). The Paper 3 description should include E7. **[Post-transfer-audit correction: G6 FROZEN means the DIFF is frozen — TCS-1.0 remains the controlling schema; migration open; see TRANSFER_AUDIT_RESPONSE.md Finding 3.]** |
| `OPEN_PROBLEMS_REGISTER.md` | Already updated with the post-addressment statuses — but the rebuilt version (from the filesystem reset) is abbreviated and may have lost some detail. |

---

## Concrete updates needed

### PUBLICATION_STRATEGY.md additions

1. **Paper 2 content**: add "nonlinear assume–guarantee composition (A4), sampled-data erosion (B1), stochastic viability layer (B9), Stackelberg equilibrium (B10), decidability (C-a)" — **each cited as `PROVEN (reconstructed)` pending independent re-verification, not as closed atlas content**
2. **Paper 3 content**: add "conservation–viability coupling (E7) as the paper's bridge theorem" — **same reconstruction qualifier**
3. **G-item statuses**: G2 → DECLARED; G4 → measurable selection proved; G6 → FROZEN (**diff only — NOT controlling; TCS-1.0 controls; migration open**)
4. **Wave 0 readiness**: add "independent rerun of all committed computational artifacts" as a prerequisite (it is the gating item per PROOF_MANIFEST.md “Reproducibility status” (the consolidated disclosure content))

### D_TIER_EMPIRICAL_AGENDA.md additions

1. **E5 cross-reference**: note the committed artifact with hash
2. **Protocol external obligations**: reference E6's matching matrix
3. **G1 readiness note**: the fisheries resource–sink template is not just designed but committed with interval-verified numbers (E5_NUMBERS.json)

### OPEN_PROBLEMS_REGISTER.md

Already has the post-addressment update. The rebuilt version is faithful.

---

## What does NOT need updating

| Item | Why |
|---|---|
| Five-paper architecture | Unchanged — the session's theorems strengthen existing papers, they don't create new ones |
| Fisheries as the G1 case | Unchanged as the **empirical** G1 case; E5's admission is the linear toy's — it strengthens the worked example, **not** any real-system claim (R04.Thm1's converse forbids transfer to 2J3KL without the five-map certificate, not constructed; repaired per `batch 4/CROSS_DOCUMENT_CONSISTENCY.md` C5) |
| Consolidation decisions (Paper 6/7 folds) | Unchanged **as proposals** — the folds are editorial defaults, not gates; final decisions wait for Wave-0 close (the Paper 4 capstone content they fold into is itself NOT CONFIRMED; see PUBLICATION_STRATEGY.md "Proposed consolidations") |
| Release wave structure | Unchanged (Wave 0 still gates on G5/G6-migration/manifests — G6's *migration*, not merely the freeze, is the gate) |
| The monograph and compendium roles | Unchanged |

---

## Bottom line

**Scored trees now live on this repository:** `wave_e_cod/` and `wave_e_edwards/`. Strategy documents must cite those paths, not a “local-only” tree. Independent rerun of those scores is **done** (`batch 4/WAVE_E_RERUN.md`: 30/30 result files byte-identical) — `INDEPENDENT_RERUN_NONE` is false for the scored trees. Wave E is not closed.

**The Wave E design is structurally sound but needs three specific content updates:**

1. **Add the new theorems to the paper descriptions** (A4, B1, B9, B10, C-a, E7)
2. **Update the G-item statuses** (G2 DECLARED, G4 half-proved, G6 FROZEN-diff-only — TCS-1.0 controls until migration)
3. **Add the independent-rerun prerequisite to Wave 0** (it is the single gating item)

None of these changes the architecture or the sequencing. They make the existing design reflect what was actually proved and computed this session. **Wave E is not closed:** the theorem files are reconstructions pending independent line-by-line re-verification, no Wave E specification has been matched (every Part III row NOT CONFIRMED), and the Paper 6/7 folds remain proposals. The scored-tree artifacts and the five Part II discrete certificates now have independent reruns (`WAVE_E_RERUN.md`, `VALIDATED_COMPUTATIONS_RERUN.md`); that is a citation-gate discharge, not a Wave E close.
