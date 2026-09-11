# Author-blocked decision plan v2 (improved)

v1 = `paper5_authorblocked_audit_verification_v2.md` §4R. Verdict on v1: direction
sound, verdicts stand — but not yet build-ready. v2 makes no reversals; it adds
decision rules, a dependency order, scope boundaries, acceptance bars, and merge
points. Nine upgrades, marked [U1]–[U9]. Next build v30, single version.

## Decision rules (read first) [U1]

- R1 (fork rule): A6 is decided FIRST and as a fork: rebuild ⟺ screen stays a
  result; reframe ⟺ screen becomes illustrative. No third status.
- R2 (title rule): title follows the fork — rebuild keeps the title; reframe
  retitles (screen out of the title) + rewrites the abstract null sentence.
  Retitle is not a free-floating A10 item.
- R3 (evidence rule): printed numbers must diff against code at build time
  (acceptance bar, not aspiration).
- R4 (tier-hygiene rule): "provisional" only on archive-derived values;
  materials-pending screen values are "illustrative" (reframe) or results
  (rebuild). Never mix the two tier words.

## Dependency order (decision sequence; single v30 build)

Wave 1 (ungated, proceed now): A3, A5-restructure, A11-sentence/placement,
A8/A9 (settled), §3.7-inventory write-up (below). Wave 2 (A6 fork, then):
retitle (R2), §§3.5–3.6 status, §4.2 revision, Box-1 rows, A11-sensitivity
(rebuild only), A5-rebanding-concern (rebuild only). A10 compression executes in
Wave 2 (its content depends on the fork); notation table in Wave 1 (cheap,
fork-independent).

## A3 — print the vector (Wave 1)

Table-3 delta: DELETE the grouped "not listed" row; ADD value rows r = 0.02,
K = 100, Emax = 30, Zref = 1, δ0 = 0.01, Δref = 1, τm = 5 (code-verified);
UPDATE the fixed-point row to (N*, Z*, E*) = (89.55188, δ, 2.08962) + interiority
note. Precision policy: exact closed forms where they exist (δ = ln2/10),
code-printed decimals otherwise (6dp to match repo prints). Interiority line
(§2.1 or §3.4, one sentence): "Φ(0) = δ gives s* = 0 uniquely with sp_k′(0) =
1/2 exactly, and E* ∈ (0, Emax), so the fixed point is interior to the
nonsmooth regions of Φ_k and Π." Gains already printed (v29 §2.1) — no action.
Solver/scan/code/seeds stay archived per R's list. Dangling pointer dies with
the grouped row (no repoint needed). ACCEPTANCE: build script diffs every
printed value against campaign constants; zero mismatches.

## A5 — restructure §3.3 around the decomposition (Wave 1)

§3.3 becomes: windows paragraph + decomposition paragraph + supplement pointer
(R's restructure, adopted). Supplement tables [U2]: core cells only
(g ∈ {1,2,5,10,20} × η ∈ {0.914,3.0}: raw window, institutional-only window,
fish-r crossings raw/institutional) transcribed from
`stage_scan_recovered/rerun_outputs_2026_09_01/{rwin_out,tau0_out}.txt` +
`stage_decomp_results.md` §2, with generating-script paths pinned path@commit
(`stage_{r_window,tau0_decomposition,decomp2}.py`); full outputs by repo pointer,
not transcription. Reading: two-level (within-operator mechanism separation
evidencing §4.1's cross-operator confound-claim); tier stays provisional.
Non-dependency stated [U3]: bands (§2.4/§3.5) are unchanged by this restructure.
Qwen's band-concern is logged in the REPO decision record (these audit files),
not the manuscript (no change-log rule) [U4]; archive-independent
re-prespecification stays available post-rebuild (needs a screen re-run).

## A6 — the fork (Wave 2; decided first within it)

Cost-split first [U5]: §3.7's missing inventory (case table + query log) is a
WRITE-UP, not code — discharge it directly in Wave 1 (author-authored table,
repo-deposited) regardless of fork. The fork covers §§3.5–3.6 only.
- Rebuild: exact-recovery (scripts/notes → same 42) or re-derivation
  (criterion + public v4.66 + new code → defensible 42, exact match not
  guaranteed). Deposit: repo (versioned code + CSVs) + Zenodo DOI at submission
  (never "on request"). Contents: 42 IDs, eligibility rule (executable),
  detrending code, spectral routines, AR(1)/null code + seeds, power code +
  seeds, periodogram CSV. ACCEPTANCE: deposited materials reproduce the reported
  zero-count exactly and power values within fixed-seed MC noise [U6].
- Reframe (recommended if no scripts/notes): "illustrative application" status;
  Russell takes the §4.2 load (citation verified: McManus, Licandro & Coombs
  2016, ICES JMS 73(2):227 — declines to confirm a true cycle, attributes
  patterns to climate trends; supports "apparent cycles ≠ demonstrated
  mechanism" as precedent). Scope, explicit [U7]: §§3.5–3.6 + title (R2) +
  abstract + §4.2 (precedent-first) + Box-1 screen/power rows + first-use note;
  §3.7 status unchanged (already explicit); §3.8 + theory untouched. Reversible
  later (rebuild upgrades status) at rewrite cost — stated, not hidden.
- Fork trigger [U8]: decide before v30; if deferred past v30, default to
  reframe (the honest status of missing materials is illustrative, not pending).

## A10 — compress without renumbering (Wave 2 content, Wave 1 table)

No renumber (spectra already lead at §3.4). Compression rule [U9]: one
finding-sentence + one method-limit sentence per demonstration (§§3.5–3.8) in
Results; Discussion keeps only operator-relevant morals (§4.1; condensed
§4.2–§4.4; §4.5 intact). Retitle per R2 (not free-floating). Notation table:
UPGRADED to recommended (~15 symbol rows; cheap; resolves A8-adjacent lookup
friction). Appendix B keep; split rejected (§3.7-write-up + fork resolve what a
split would move, not cure). §3 split/figures: no action without author motive.

## A11 — merged first-use note (Wave 1 note; Wave 2 sensitivity)

Merge R's sentence with the A6 five-gap list into ONE "screen status" note at
§2.4 (non-archival + illustrative + no confirmatory weight) with a one-line
pointer at §3.5 [U6b: no duplication]. Keep §4.7(iv) as the Discussion anchor;
§4.2 revision is a flagged dependency of "no confirmatory weight." Under
rebuild: (iv) updates to report the 5.3 sensitivity outcomes (ARMA(1,1),
trend-stationary, block-bootstrap, regime-surrogate, detrending) instead of
merely listing the limitation.

## A8/A9 — settled (keep/leave, v1 §1.4 reasons). No action.

## v30 build-time checks (assertions, not review comments)

B1 Table-3↔code value diff (zero mismatches). B2 No dangling "computational
record" pointer. B3 Tier-hygiene grep ("provisional" only archive-derived).
B4 Title↔status consistency (screen in title ⟺ screen is result). B5 First-use
note present (§2.4) + §3.5 pointer. B6 §4R-retired: Qwen-clause absent,
"superseded"-language absent, "on request" absent. B7 Russell citation verified
(done: supports the transfer). B8 Single-version rule: all Wave 1+2 decisions
in one v30 build; no content/line-number split.

## What did not change (v1 verdicts standing)

Full-disclosure A3; keep+cite A5; the fork itself; R-reframe recommended;
appendix-B keep; split rejected; Qwen-clause rejected; comparator-AR(1)
rejected; FD/solver-fear corrections; "two unreproduced"/"superseded"/
"circularity"/"collapses" corrections; D1–D17.
