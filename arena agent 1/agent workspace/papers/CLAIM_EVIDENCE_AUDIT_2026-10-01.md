# Claim-to-evidence investigation — archived; expanded audit stopped

Date: 2026-10-01. **Scope corrected by the owner:** the attempted 15-head
claim-by-claim review is **stopped**, not a prerequisite for repairing source
preservation or reproducibility. This is an evidence record of a *partial*
paper07 reading and inherited paper08 text, **not a corpus-clearance test** and
not a queue to re-audit every paper. Earlier formal and empirical verification
remain credited. Two newly added prose claims from the AI-authored paper07 v49
sensitivity section were corrected in the live heads and their computational
source; all other notes below are historical leads, not newly introduced faults
or current blockers. Historical v49 remains unchanged to document origin. The
reviewed live heads remain the eventual reproducibility targets; grouping and
upstream regeneration are separate owner decisions, **not gated on a 15-head
scientific re-audit**.

## Correct the starting premises

- It is **not** true that numeric checks never ran. `PHASE1_CLAIM_AUDIT.md` inventoried 1,970 tokens, nearest-matched 117 abstract/conclusion numbers in units 7, 8 and 10, and subsequently re-executed some E2 source-year campaigns. **The 117 nearest-value matches are not provenance or evidence of correct scientific interpretation**; that record itself says so. No paper-by-paper review of *all* numbers and claims was thereby completed. `PROOF_AUDIT.md` checks proof-marker existence, not proof correctness.
- The claimed **“58 dead pointers” is not an established defect**. `PROOF_AUDIT.md` explicitly retracts an earlier mistaken count of 75 and a later count of one: against the old-numbered, correct supplement lineages, **75/75 sampled pointers resolve, zero dead**. A `58` elsewhere is the source RAM stock panel size and also a paper06 page count, not a validated dead-pointer backlog. Do not strip or fabricate citations on this premise. A new pointer inventory would need its own named scope and existence test.
- The source-preservation repairs in `OPEN_CONTENT_ITEMS.md` are real but do not validate scientific claims. Named structural gate and live-tail detector zeroes are not content verdicts.

## Producer root-cause diagnosis — **deferred repair, not a cosmetic bypass**

The source-preservation mismatch is not one simple “script versus paper” choice. These pre-existing producer findings are recorded for the *separate* reproducibility repair, not new manuscript correctness failures:

1. **Reference identity and boundaries:** `p5/mergelib.py::split_entries/_split_glued` can split a complete book reference at `Publisher, City (year)`, creating an author head and a detached publisher tail; `merge_refs` deduplicates by a truncated normalized prefix rather than proven work identity. The paper01 v61 Aubin 1991 entry is a concrete regression witness; the v62 merge is deliberately fail-closed. Source paragraphs are authoritative evidence for the reference, not a reason to trust that old parser.
2. **Loss of source scope at part boundaries:** generic merge/split routines remove per-source front matter or treat the bibliography/declarations/supplement as an undifferentiated global suffix. Paper05/06 lost distinct post-reference content, paper11 lost the Edwards data record, and paper08 inherited a *deliberately blinded* sampled seed. The reviewed heads repaired those losses; rerunning an old producer is not a valid reconciliation.
3. **A check was not necessarily before the write:** `p5/mergelib.py::merge` constructs `out`, **writes `BASE+OUT`**, *then* calls `phase0_scan.report_gate(phase0_scan.gate_text(...))`. Thus that routine's structural gate cannot guarantee no unsafe file was written; a failure after the write is not fail-closed. Source-specific scripts that check before calling it offer some protection, but the library itself has the order wrong. This must be tested and fixed after grouping/target decisions, before permitting unattended regeneration.
4. **No source-to-output scientific invariant:** matching LaTeX sections, braces, refs, and compilation cannot certify a numeric derivation or claim strength. The AI-authored v49 sensitivity prose escaped a new-section computation-to-prose check; a structural merge gate cannot infer the true perturbation label. The targeted check now runs at the addition boundary; do not impose a new broad fatal rule on unrelated papers without report-only false-positive tests.

The intended endpoint is a **source- and configuration-driven generator** whose scratch output reproduces each *final, reviewed* head when the owner decides the grouping. Tests should fail **before** file replacement on mismatched source provenance or numbers. A copied terminal `.tex` used as a “generator” would not resolve this root cause. These are design findings, **not completed producer repairs**.

## Scope of this archival record

The preceding expanded protocol and proposed all-15-head review were scope
creep and have been withdrawn. Only selected paper07 claims were source-tested;
paper08 repeats that sampled passage. No conclusions about the remaining 13
heads follow from this investigation. An exhaustive content/prior-art audit is
an **optional separate project**, not required to repair provenance and source
preservation. “Not inspected here” is not “unverified by earlier work.”

## Paper07 v50 — first source-specific pass (PARTIAL)

**Question tested:** Does a sampled/held decision clock have stability properties different from continuous-delay or Euler command-step models, and what do its computations and empirical screen actually license? **Sources:** `p7/campaign_scan.py` (SHA-256 `abe91da59fbb43f125998fe98d1a800df2f77294be09bad6f99645f9cddd1c2c`, byte-identical to workspace `p5_crossing_scan.py`), `p7/sensitivity.py` (SHA-256 `b0d74ed2654706fa5d2ef1102106629cc209372242a6a4394f89e2b233f802ff`), archived `paper5_aug08_originals/ram_crosssection.py`, `ram_target_stocks.csv`, `verify_bh.py`, and its curated `u5_case_table.csv`. The first two scripts had already been archived; this pass **executed** them afresh. Execution logs and exact recheck tables: `../content_audit/p7_campaign_recheck.log`, `p7_sensitivity_recheck.log`, `p7_one_axis_recheck.csv`, `p7_joint_box_recheck.csv` and `p7_bh_recheck.log`. Python used numpy 2.3.5 / scipy 1.17.1.

### Reproduced, **within the declared model and input panel**

1. Running the actual crossing campaign gives the baseline exact mobilising crossing **6.5013 yr**; Euler mobilising **47.536 / 79.1427 yr**; Euler protective **2.3064 yr**; exact protective no crossing on the scanned **[0.2, 200] yr**, maximum spectral radius about **0.9967**. Both regenerated CSV outputs (`p5_crossing_record.csv`, `p5_linear_trajectory_mse.csv`) are **byte-identical** to the branch's committed campaign results (SHA-256 `dceeb62c16d3b079b25bb62790f33993c1544951773b4ba5e98773e7cdca2f7d` and `31d90b12f3e0706a09345aa5b2d45c6b45c2fda45abfbfbc6b8a51a4b1e82662`). This validates deterministic execution for that illustrative Candidate-A model, **not** parameter calibration, a real fishery threshold, or the correctness of every claim in §3.4.
2. Recomputed all **128** corners (64 each box) at 4001 grid points plus bisection from the source model equations: assuming the six axes are `r,K,q,eta,Emax,dref`, the ±0.5% box gives **60/64 crossings, 0.87196484–10.67042538 yr**; the ±1% box gives **44/64, 4.42319231–13.65324207 yr**. At the non-crossing corners the annual spectral radii are <1. No multiple crossings were seen at this grid resolution. These figures agree with §3.5. **The six-axis names are inferred from the one-at-a-time table**; the extant sensitivity note and manuscript say only “six influential parameters.” A checkable campaign should name them in its registered input, and a sampled grid is not an interval proof.
3. Re-executed the **84 target-band tests** using the archived 58-stock RAM input, `n>=20` valid SSB filter (**42 eligible**), 200 seeded AR(1) surrogates and BH step-up: **0 discoveries**, smallest nominal p-value **0.0448**. Also executed the archived `screen_battery_v31.py` in full: all **11** named baseline/alternative variants produce **0/84 BH rejections** (`../content_audit/p7_screen_battery_recheck.log`). This supports stability of this *selected panel's* zero count to those specified analysis choices, not absence of cycles, correct cohort selection, controller-sign identification, or general statistical FDR guarantees under arbitrary dependence. The case-search CSV contains **32** curated rows and no row marked as satisfying all four criteria; this checks the **internal tally**, not the primary evidence for each classification. The original RAM input panel and labels have not been independently revalidated here.

### Lineage check — what was introduced when

Before calling anything a *new* error, compare versions. The ±1% table and the “three orders” sentence are **already in paper07 v49**, the AI-authored 2026-09-29 sensitivity addition (`push_v43.py` describes writing §3.5). Neither appears in v48 or in the unblinded sampled v46 source. Both are in the **pre-repair** v50 snapshot and were copied when paper07 v50 was merged into paper08 v46. The October 1 attribution/back-matter repairs **did not add or change either numeric claim**. This means earlier AI drafting **did introduce** these two claims into the paper07 lineage; the merge then propagated, rather than generated, them. The 0.24--0.58 power range exists already in paper07 v48 and unblinded sampled v46; its exact fixed-seed mismatch was **previously documented** in `POWER_CLOSEOUT_RECORD_v1.md`, not newly caused by this audit or the merge. The erroneous classification of Adamson–Hilker as continuous is in the **pre-repair v50** related-work section (not in v49), and is carried into paper08's sampled part; the continuous-channel v45 discusses the same work as *informational delay*, without this blanket classification.

Lean work should not be discounted or misapplied: `LEAN_AUDIT_2026-09-30.md` explicitly says paper07 and paper08 make **no Lean claim** and have no corresponding Lean modules. Its source scan also says the newer toolchain pin's build was **not rerun in that audit**. Formalized statements in other units are not tests of the sampled-paper parameter sweep, empirical screen, power simulation, or prior-art characterization.

### Two v49 sensitivity prose defects — **corrected in the current heads**

**P7-N1, CORRECTED: one-at-a-time “worst 1% swing” column used ±2% cells.** The original `p7/sensitivity.py` stored values in order `(-2%, -1%, baseline, +1%, +2%)`, then compared `v[4]` and `v[0]` against baseline while printing “worst 1% swing.” Historical v49 and the pre-correction paper07 v50/paper08 v46 texts used those values. Independently rerunning the crossings gives **actual worst ±1% relative changes**: K **54.08%** (printed 59.5%), q **47.12%** (55.4%), effort cap **47.02%** (55.3%), eta **8.88%** (18.9%), r **7.08%** (14.6%), memory timescale **0.81%** (1.6%). `dref` has an actual ±1% swing **63.81%** even though the old table column was a dash (the old `NaN` handling also suppressed its finite −2% swing). The main qualitative conclusion “K, q and effort cap move by more than half” **does not hold for q and effort cap at ±1%** (they do at ±2%). This was a source-code **labelling and non-finite-endpoint handling error**, propagated to both heads and the explanatory note, not a defect in the crossing computation. **Resolution:** retain the calculated ±2% percentages, relabel the column and qualifying sentence as 2%, state the finite-only rule in the caption, and show the finite `dref` −2% shift as **65.7%**; correct `p7/sensitivity.py` and `PAPER07_SENSITIVITY.md`. The user approved fixing the prose instead of changing the underlying model.

**P7-N2, CORRECTED: “three orders of magnitude larger” margin had no matching denominator.** Paper07 v50 ~L1525 and its copy in paper08 v46 ~L4972 state that the protective channel's margin is three orders larger than the mobilising channel's. From the very cited numbers: protective max-grid margin `1-0.9967≈0.0033`; mobilising annual instability excess `1.00035-1≈0.00035`; ratio **≈9.4**, *about one order*, not 1,000. Comparing annual values instead (`1-0.9838=0.0162`) gives ratio **≈46**, still not 1,000. Moreover a protective minimum margin over a grid and a mobilising annual excess at one point are not the same evaluation basis; choose like-for-like comparisons before asserting a robustness ratio. The stable-on-grid verdict remains supported; the claimed scale does not. **Resolution:** both live heads and the source note now state the protective minimum sampled-grid margin **0.0033** and the annual mobilising instability excess **0.00035**, explicitly noting these evaluate different interval sets, without claiming a universal ratio.

**P7-N3, PRE-EXISTING PROVENANCE NOTE (not a new block): the printed power endpoint differs from the documented fixed-seed driver.** Paper07 §3.6 quotes sprat-class power “approximately 0.24--0.58” at `sigma=0.3` on 100--200 yr records (copied into paper08). Ran archived `power_driver_v2.py --tmode record --burn 0 --noises white --cells sprat_H100_s03,sprat_H200_s03` with its `power_demo.py` dependency, 50 fixed trial seeds, 120-simulation seed-7 null; output: **0.24 (12/50) at H=100, 0.70 (35/50) at H=200**, log `../content_audit/p7_power_recheck.log`. The archived `POWER_CLOSEOUT_RECORD_v1.md` itself records this 0.70-versus-0.58 mismatch and calls it “sampling-consistent” (pooled p≈0.21). That is not the same as **reproducing a deterministic fixed-seed archived value**. The 0.58 may come from another version or sampling convention, but neither is established by this run. Do not substitute 0.70 in the manuscript or assert 0.58 false without identifying the original generating configuration; record it as unreconciled provenance. The qualitative conclusion that power depends on noise and record length remains.

**P7-L1, INHERITED v50 WORDING; outside this narrow fix:** §Related work ~L191–206 states that Shertzer–Prager, Brown et al., **and Adamson–Hilker (2020)** each concern a **continuous lag**, then contrasts the present sampled architecture with theirs. Adamson and Hilker explicitly say they use a **discrete-time resource-harvester model** with outdated stock `X_{t-τ}` in the effort update. Primary article (model description): [1](https://link.springer.com/article/10.1007/s12080-020-00462-x). It is *not* necessarily the same continuous-flow/held-command map developed here: the comparison must say precisely how the discrete seasonal update, information delay and current paper's sample-and-hold operation differ. The blanket classification is false; novelty **against this nearer comparator remains unestablished**. Other cited comparators have not all been read in primary form yet.

**P7-S1, archival interpretation note, not an active defect or blocker:** §3.5 calls a 1–11 yr box-sensitivity range “plausible” and the point “not identifiable” but supplies **no measured parameter-uncertainty distribution or identification study**. The manuscript explicitly denies that the band is a confidence interval, correctly. Nonetheless the box is a chosen perturbation, not an estimated plausible range for institutions. Review wording after testing parameter basis and comparator evidence; do not infer real-world thresholds from the model.

### Disposition and narrow next steps

- **Historical source:** paper07 v49 first added the two sensitivity overstatements.
  Its versioned file and original push message are preserved as provenance,
  not silently rewritten. Current paper07 v50 and paper08 v46 have the
  corrections in that inherited passage. `p7/sensitivity.py` and
  `PAPER07_SENSITIVITY.md` now agree. `../content_audit/check_p7_sensitivity_addition.py`
  executes the computation and checks both manuscripts against its output.
- **Not reopened:** the power discrepancy was documented before this inquiry;
  Adamson–Hilker wording entered by v50 and was inherited by the combined v46.
  They are not “fresh discoveries,” theorem failures, or additional reasons to
  expand this repair into a 15-head audit. Any related-work revision would be a
  separately scoped content decision.
- **Return to original work:** source preservation and reproducible generation
  of reviewed heads remain the open producer task. The owner will decide final
  grouping independently; do not hold that work hostage to a new corpus-wide
  content-audit checklist. No Lean theorem or verification battery changed.

**Process rule:** When a *new section* is authored, check every quantitative
sentence, table label, uncertainty qualifier and margin comparison against the
actual computation **at the point of addition, before merging**. Record the
source run and finite/non-finite conventions. For this section the targeted
script above is the executable example. This is a source-bound prose review,
not a speculative corpus-wide fatal detector.
