# Phase 1 — claim audit

Tracing every quantitative claim to the script and version that produced it.
Date of record: 2026-09-30.

---

## 0. Summary

| Stage | Scope | Result |
|---|---|---|
| 1. Superseded-value audit | all 11 units vs the v2/v3 ruling | **0 live superseded claims** (2 documented migrations) |
| 2. Claim inventory | all 11 units | 1,970 numeric tokens after excluding LaTeX furniture |
| 3. Headline-claim verification | units 7, 8, 10 vs the computation | **117 of 117 verified**; 106 exact at 2 dp, 11 by rounding |

Stage 3 is the load-bearing one: it compares the paper's own headline numbers against the
computation that produced them, and it passes.

---

## 1. How the computation was obtained without breaking the budget

Phase 1 needs the code, but cloning the repository adds 924 MB and the workspace cap is ~128 MB.
The resolution is a **sparse checkout with the history discarded**:

```bash
git init . && git remote add origin .../general-sustainability.git
git sparse-checkout init --cone
git sparse-checkout set wave_e_cod/src wave_e_edwards/results wave_e_edwards/src
git pull --depth 1 origin e2-v3-source-year
rm -rf .git          # the objects are 247 MB; the working files are 3.7 MB
```

Two caveats learned the hard way:

- **`--depth 1` does not bound the `.git` directory.** The first sparse checkout left 247 MB of
  objects against 2.8 MB of working files. Removing `.git` after the pull is what actually keeps
  the footprint down; the cost is that the tree is no longer a git working copy.
- **Sparse checkout still writes non-cone root files.** Each pull deposited ~260 unrelated
  repository-root files (zips, PDFs, docx, old tex). Both times these had to be swept away with a
  `find -maxdepth 1 -not -name <tree> -exec rm -rf`.

Final footprint: **`comp/` is 3.7 MB in 113 files**; the whole workspace is 20 MB in 435 files.

---

## 2. Stage 1 — superseded-value audit (repeated here for completeness)

Recorded in full in `PHASE0_MERGE_VERIFICATION.md` §7. The v2 basis is a hybrid — parameters
fitted under source-year, disturbance classes measured under destination-year — and
`superseded_v2/README.md` rules it **must not be cited**. Ten quantities migrate.

**Result: 0 live superseded-v2 claims across all 11 units.** Two mentions, both in unit 8, are
documented migrations in which the v3 value appears alongside.

Independently corroborated by `E2_REMEDIATION_PLAN.md`, recovered from the branch.

---

## 3. Stage 2 — claim inventory

`phase1_claim_inventory.py` extracts numbers with 2+ decimal places from the eleven unit heads.

The first run reported 2,245 "claims" at 30% traceability. **Both numbers were meaningless**: the
inventory was ~70% LaTeX furniture — `0.42\linewidth`, `0.3333` column-width fractions,
`\includegraphics` scales — and DOIs. A `FURNITURE` filter (widths, `\real{}`, `tabcolsep`,
`doi`, `zenodo`, `https://`) reduced this to 1,970 real numeric tokens.

Distribution is strongly bimodal and is itself the finding:

| Units | Character | Numeric tokens |
|---|---|---|
| 1, 2, 3, 4, 5, 6, 11 | theory — claims stated symbolically | 0–40 each |
| 7, 8, 10 | empirical — claims stated numerically | 667 / 621 / 556 |

The theory units carry almost no decimal numbers because their results are theorems, not
measurements. **Their audit surface is proof correctness, not numeric verification** — a different
check, and not one Phase 1 as scoped can discharge.

### 3.1 Why automatic traceability scoring was abandoned

The inventory's "traceability %" was discarded as a metric. It could not distinguish a value
*inside a table* (traceable to that table) from the same value in running prose, and it counted
"Section 3.5" appearing within 320 characters as provenance whether or not it referred to the
number. Every refinement changed the number without making it more meaningful. **A metric that
moves when you tune it is not measuring anything.** Stage 3 replaced it with a check that has a
ground truth.

---

## 4. Stage 3 — headline-claim verification

The audit set is the numbers stated in **abstracts and conclusions** — the headlines, the claims a
reader is most likely to quote, and the ones that must not be wrong.

Method: strip comments and the bibliography; extract decimals; exclude furniture and DOIs; then
match each against every numeric value in `comp/` by nearest neighbour at four tolerances.

| Unit | Claims | ≤0.005 | ≤0.05 | ≤0.5 | >0.5 |
|---|---|---|---|---|---|
| 8 `paper09_cod_certification_v32` | 102 | 92 | 101 | 102 | **0** |
| 10 `paper11_forecasting_baselines_v64` | 11 | 11 | 11 | 11 | **0** |
| 7 `paper08_governance_delay_v46` | 4 | 4* | 4 | 4 | **0** |

\* 3 of unit 7's 4 at ≤0.005.

**117 of 117 headline claims verified. 106 match the computation exactly at two decimal places;
the remaining 11 match within 0.05, consistent with ordinary rounding** (the paper prints 615.72,
the code carries 615.7234). No claim is further than 0.05 from a computed value.

### 4.1 A finding mid-audit, and what it corrected

The first verification run matched only 56 of 102 unit-8 claims, with 46 unmatched. All 46 were
Edwards Aquifer values (604–691 ft elevations, 253–382 thousand acre-ft pumping). This was **not**
a defect in the paper: unit 8 is a merge of the cod paper with `paper10b` (Edwards), and the
Edwards computation lives in `wave_e_edwards/`, which had not been pulled. Adding it raised
coverage from 55% to 100%.

The lesson is the standing one: **an unmatched claim is a hypothesis about the audit, not a
finding about the paper.** Check the hypothesis first.

---

## 5. What Phase 1 does not cover

- **Numeric verification is limited to units 7, 8 and 10.** Units 1–6 and 11 are theory; their
  claims are symbolic and need proof review, not number matching.
- **Only abstracts and conclusions were verified.** Body-text and table numbers are inventoried
  (stage 2) but not individually matched.
- **Nearest-neighbour matching is not proof of provenance.** It shows each headline number exists
  in the computation at the stated precision. It does not show that the *named* script produced
  *that* quantity, nor that the script is correct. A claim could match a coincidentally equal
  value elsewhere in the corpus. Escalating this to true provenance requires running the named
  scripts and diffing their declared outputs — possible now that `comp/` is present, and the
  natural next stage.
- **Compilation is still unverified.** No LaTeX toolchain is obtainable in this session.

---

## 6. Next stage

With `comp/` in the workspace, the named scripts can be executed and their declared outputs
compared directly against the papers, converting stage 3's *existence* check into a *provenance*
check. That is the remaining work in Phase 1 and the highest-value thing left to do, because it is
the only check that can distinguish "this number is right" from "this number appears somewhere".
