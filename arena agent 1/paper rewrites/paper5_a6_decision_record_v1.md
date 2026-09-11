# A6 fork decision record v1 (2026-09-11)

Fork from `paper5_decision_plan_v2.md` (A6, rules R1/R2): rebuild (screens stay
results) vs reframe (screens become illustrative). Decided on evidence after the
§3.6-power and §3.7-battery closeouts, per user direction 2026-09-11 (affirmative
decision required; passive reframe-default overridden).

## Decision: REBUILD

The acceptance bar (`decision_plan_v2` §A6/U6) is met: deposited materials
reproduce the reported zero-count exactly and the power values within fixed-seed
Monte Carlo noise. The reframe premise ("missing materials") is false for the
executed screens: the materials exist, are deposited, and reproduce. Title keeps
the screen (R2); abstract null sentence keeps; §§3.5–3.6 stay results.

## Evidence

**§3.5 42-stock screen — bit-exact.** `ram_crosssection.py` + `ram_target_stocks.csv`
re-executed locally: output identical byte-for-byte to the committed
`ram_crosssection.log` (42 stocks, all band powers, CVs, the single nominal flag
PANCHNCHSP band-B 0.425 vs 95% 0.407). Zero-count: `verify_bh.py` (deposited BH-FDR
reconstruction over the 84 target-band cells, empirical p from the same seed-7
nulls) gives 0 rejections (smallest p = 0.0448) — the BH-adjusted zero is
deterministic from deposited machinery.

**§3.5 root-cause finding — text/code divergence (repaired in v30).** v29 §2.4
described bands 4–8 yr (biomass) + 12–60 yr (effort) with a BY fallback and
detrending/endpoint sensitivity; no deposited code executes that screen. The
executed screen uses bands A/B/C/D (2.5–5/5–9/9–14/14–30) with a nominal 95% AR(1)
comparison; the BH step exists only as the post-hoc `verify_bh.py`; the effort
half (12–60 yr on F) was never executed though F is in the CSV. v30 §2.4 now
describes the executed screen; the never-executed effort bands, BY fallback, and
unexecuted sensitivity claims are dropped (methods describe executed analyses only).

**§3.6 power — within noise (closeout).** Canonical config white/burn-0 reproduces
the report: sprat 1.00/0.24(exact)/1.00/0.70∼(35/50 vs 29/50, p=0.21)/1.00;
anchovy [0.00,0.10] vs [0.02,0.14]; cod marginal (report-only FP). AR(1) record
noise refuted under both burns. v30 §2.5 corrects "AR(1)-type noise" to white
(the AR(1) is the test null, not the injection: `power_demo.py` L135 injects iid
normal) and cites the filed driver; numbers unchanged.

**Discriminator (cod/sprat) — not re-executed, justified.** Its model grids feed no
printed number (v29 §3.7's cod paragraph uses the four-state comparison, not the
stage-model verdicts; CVs 0.387/0.143 come from the ICES series, sprat 0.40 from
the RAM log). Case-level interpretation outside the screen bar; committed log stands.

**§3.7** is outside the fork (status unchanged per plan) but its SOI block is
repaired in v30 (below) because the battery closeout proved artifact contamination.

## Battery open items (closed)

**§9.1 chile_reported_only — VERIFIED but artifact-inflated; input recovered.**
Root-cause chain: (1) the deposited "Chile" series is the GLOBAL taxon-600004
aggregate (Peru+Chile+Ecuador+…), proven against today's public SAU API
(`taxa/tonnage/reporting-status`, region 600004) to max rel. diff 5.1e-08;
(2) the author's "Chile" file is the taxon-page download, the author's Peru file
the EEZ-604 download (different pages, codings, vintages — consistent with the
supp's "entity 604 taxon 87" vs "Taxa 600004" labels); the public API cannot
serve per-country reporting splits (filter params ignored; website CSV = same API),
but the global split suffices because the file is global; (3) global-reported
early-half × raw-SOI lag 1 = r=+0.3870, p=0.0237 — the printed (0.387, 0.0237)
exactly; (4) with artifact-free SOI the same cell is r=+0.2519, p=0.157 (n.s.).
v30 drops the sensitivity with the SOI block (its premise is gone) and relabels
"Chile/Chilean series/both stocks" to global-taxon/both series (numbers unchanged,
incl. the clean NINO1-Granger p=0.00016). Uploads forensics: the author's raw
`SAU Taxa 600004 v50-1.csv` is byte-identical to the deposited Chile file (totals
only — the reported-only input was never archived, confirming the recovery's
necessity); `shortened.txt` (entity 604/taxon 87 TSV, 1950–2024) matches deposited
Peru 0/75 with all rows tagged "Reported" (provenance quirk, battery numbers
unaffected). Evidence: `s91_verify.py` + log + `sau_taxa600004_reporting.json`.

**§9.2 |r|≈0.31 provenance — IDENTIFIED.** Exhaustive scan ({Sep,Aug} ×
{logged,unlogged,detrended} × 4 NINOs × lags 1–12): the unique standard-pipeline
match is September-vintage detrended-log Peru × NINO1 lag 1 (r=−0.3119, p=0.0091);
August gives −0.2917 under the same pipeline; only implausible lag-10 cells
otherwise. The supp's "series behind that figure" clause pins the September
vintage, so the figure is the detrended computation. v30 documents the pipeline in
§3.7+S4. Observations (not printed — post-hoc): first-difference NINO1 lag1 =
−0.48 (p≈0); detrended spectrum keeps 3.71 yr but moves 7.96→6.67 yr (the 7.96-yr
"co-dominant" peak is trend leakage). Evidence: `fig031_provenance.py` + log.

## Power open items (closed)

**§8.1 power_demo.py md5 — doc-side mislabel; bytes VALIDATED.** Deposit-commit
bytes = HEAD bytes (single-commit history); the deposit doc's "md5" column is
truncated SHA-256 mislabeled (5/5 files match `sha256[:12]`, sizes exact) — the
hashes confirm, not impeach, the repo bytes. The column-label fix belongs to the
owning agent (file outside this work's paths); recorded here, not applied.

**§8.2 H400 vs §3.6 scope — intentional, no dependence.** v29 §3.6 prints 100–200 yr
only; H400 exists solely in the report + committed tables as supplementary. No action.

## v30 changes (mechanical list)

Main (12 subs in `build_paper5_v30.py`): header; §2.4 executed-screen rewrite + file
citations; §2.5 white-noise + driver citation; §3.5 target-bands wording; §3.6
void-registration cut (era-split/SOI-pathway/SOI-lags premises all artifact);
§3.7 anchoveta rewrite (detrended-NINO1 figure doc; clean-SOI null 0/90 with Peru
+0.07/+0.16/+0.01; global-taxon labels; Granger/CCM/mechanistic tails kept; era,
splits, collapse-exclusion, reported-only, focal-test sentences cut); Box-1
anchoveta + bands rows; Appendix-A two discharge flips; Data-availability screen/
power discharge; stale supp pointer v5→v8. Supp (9 subs in `build_paper5_supp_v8.py`):
S4 figure doc, series labels, clean SOI (Peru +0.073/+0.158/+0.014 — note the
battery record's "+0.015" is a transcription rounding slip of 0.014452, corrected
here from code output; global +0.052/−0.047/+0.007), BH 0/90, family wording,
Granger relabel, era/collapse/reported cuts, registration cut; S8 discharge list +
tier upgrades (screen = re-execution-verified; power = independently re-executed)
+ "other ... remain unreproduced" scoping.

## R3 number audit (v30 printed ↔ code)

−0.31/0.009 ↔ fig031 log (−0.3119/0.0091); clean SOI +0.073/+0.158/+0.014,
+0.052/−0.047/+0.007, 0/90 ↔ xcell pipeline (== `forensics.py` L59–65) full-precision
rerun (0.072713/0.157743/0.014452/0.052195/−0.046965/0.007087, all p≥0.19);
Granger 0.00009/0.00016/≥0.19 ↔ battery 12/12 rerun (NINO1-based, clean, unchanged);
3.70/7.96/3.63 ↔ battery peaks 4/4 (unchanged); sprat CV 0.40 ↔ RAM log (unchanged);
power 1.0/0.24–0.58/0.02–0.14 ↔ closeout grids (unchanged); BH zero ↔ verify_bh run
(0 rejections); 42 stocks/bands/powers ↔ bit-exact RAM rerun. Build checks: B3
"provisional" only stage/archive (8 sites); B4 title unchanged; B6 retired-language
absent (Qwen only in acknowledgments); B8 single version (tex+supp+pdf one build).

## Residuals (not in v30)

Effort-half screen never executed (F available; future re-derivation, not a repair);
BH step is post-hoc reconstruction (committed, deterministic, cited as such);
deposit-doc hash-column label (owning agent's file); full A3/A5/A8–A11 program still
author-blocked and out of this scope; v30 PDF built with tectonic 0.15.0 from the
committed tex + fig1 (single figure, unchanged).
