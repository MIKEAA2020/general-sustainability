# F1 v29 Humanized — Change Log (2026-09-18)

**Carrier of record.** `framework/paperF1_retention_framework_v29_humanized.md` → `framework/paperF1_retention_framework_v29.tex/.pdf` (typst stamp `se29-c1375ed`).

**Status.** New version only; v28 and all prior carriers untouched (provenance discipline).

## 1. Design

- Repo `gemini_F.txt` provides the register spine (the paper’s prose architecture: abstract, §1, §2.3, §3, §6.1–§6.2 headings, §7–§9, §6.5 table lead), per `HYBRID_SYNTHESIS_ASSESSMENT_E3_F1_20260918.md`.
- The numeric protocol record is re-anchored section-by-section to v28’s frozen instrumentation because the F1 paper is style *about* the numbers — a register rewrite was judged unsafe for those sections.

## 2. Section disposition (v29 = v28 body under gemini register, section annotated)

| Section | Disposition |
|---|---|
| Title / Abstract | gemini spine (hours-up register with identical frozen claims) |
| §1 Introduction | gemini spine |
| §2.1 | gemini headings + v28 ladder paragraphs (Cod ladder running numerics incl. M1–M4, K-bounds, catch-treatment pair, ±17-kt calibration; Edwards ladder) re-anchored; v28 per-origin lower-bound sentence grafted (≈ 950.8 kt; 50.8 kt; K = 5000 endpoint) |
| §2.2 | v28 Algorithm body swapped wholesale (ΔG = 2.0, b = 0.05, clone-acceptance 0.05, margin printouts 109.7 / 232.8 / 945.1 / 170.9 / 613.4, Algorithm Box preserved) |
| §2.3 | gemini spine (class-grounds, v28-faithful) |
| §3 | gemini spine (information-set / audit abstraction preserved) |
| §4 Worked Edwards | v28 body swapped under gemini heading (M2m margins 12.283 vs 13.230 ft; DM z = −2.010, CI [−2.796, 0.028], p = 0.0356; oracle 7.547/10.865 ft, −42.96%/−48.52%; Comal rated r-stream) |
| §5 Worked cod | v28 body swapped under gemini heading (verbatim window table incl. 98.05/114.80/120.51, persistence 55.32+147.05, ratio ρ = 0.899, Welch t = 10.54, bootstrap 95 % [0.894, 0.903]) |
| §6.1–§6.2 | gemini spine; DGP table kept; graft: design-time naive regime-switch rejection sentence (900 → 888 → ⋯ → 0, rejected at design time) |
| §6.3 | v28 body swapped (core + Amendment-1 rows incl. extremes 0.633/0.733/0.933/0.867, mean-gain annotations +3.1/+9.2 kt graft lead) |
| §6.4 | gemini spine + topic sentence graft ("Power is low for three of four in-class structural processes; the cause is identification, not the gates.") |
| §6.5 | gemini spine (register) + v28-identical 8-row table + band-invariance graft (band-invariant verdicts; prospective calibration ≥ 0.80 / ≥ 0.90 governs future verdicts only) |
| §7–§9 | gemini spine |
| Data availability | v28 body swapped (environment-sensitivity 151.6/153.2/445.5/462.5, ±17 kt cap, DM one-sided z = −3.284 / p = 0.0016, reproducibility tokens, rebuilt byte-for-byte statement) |
| References | v28 frozen reference set re-pinned verbatim (Adaee Zensodo ×2 incl. 22552680 / 22553609; M4 title corrected to "The M4 Competition: 100,000 time series and 61 forecasting methods", IJF 36(1), 54–74) |
| Declarations | new block (competing/funding/CRediT/AI-statement), e1-family template, register-matched |

## 3. Verification battery (executed)

- **Presence (whitespace-exact)**: abstract frozen claims 0.955 / 0.960 / 0.995 / 0.950 / 0.0055 / 0.034 / 0.633 / 0.733 / 0.933 / 0.867 / 98.05 / 114.80 / 120.51 / 120.54 / 14.70 / 12.84 / 12.283 / 13.230 / 21.106 / −42.96 / −48.52 / 0.986 / 950.8 / 50.8 / 940.8 / 40.8 / 612.5 / 18.11 / 55.32 / 14.52 / 105.8 / 129.8 / 127.4 / 149.9 / all present in `.md` and in the PDF text layer.
- **Banned-token scan**: Companion Monograph / Hydrogeological Model Elaboration / Fish and Fisheries / 105324 / 105327 / 20,000 replications → all zero.
- **Numeral diff vs v28**: 105 → 19 residual tokens after grafts, all triaged: (a) reference-page page ranges and years (269, 172, 31, 83, 96 — References bibliography entries only); (b) parenthetical decimals inside v28 §6.4-§6.5 closeout paragraphs whose table values and prose equivalents are carried; (c) hyphen-border regex fragments (−1842, −23). No payload token from §2–§6 is absent: the ladder paragraph, four worked-example tables, DGP table, core + Amendment rows, alternative-rules table, DM/archival z-CI-p triplets, and the reproducibility block all land byte-comparable.
- **New-token audit**: all 8 new numeric tokens traced to adjacent-archived arithmetic (−0.21 = 0.765 − 0.978 annotation; 7.16 % = 0.9469/13.230; 17.34 % = 3.6607/21.106; 32.5 % = 1 − 0.675; 9.3 / 9.1 = margin-annotation arithmetic; 10.87 rounding twin of 10.865 = 21.1056 × (1 − 0.4852)), each logged above as a derived annotation where inserted. No new unsupported ground value.
- **Provenance**: `10.865 ft (oracle, h = 5)` arithmetic-consistent with the archived frozen pair (21.1056 ft, −48.52 %) and is retained as a derived value, the same policy as the F1 corpus’s frozen-pair arithmetic — derivation, not sourcing.
- **Layout**: abstract on page 1, clickable ORCID/email URIs, Algorithm Box rendered as indented preformatted block (the original ```-fence converted; no stray backticks), zero `horizontalrule` / `=>` / `$$` strays in the text layer, 21 pages.

## 4. Losses closed by graft (none remaining)

## 5. Known deliberate differences from v28

- Several v28 section titles rewritten to gemini register (table above); content bodies preserved or grafted verbatim.
- v28's step-of-pass paragraphs in §6.4 (page-level prose) supplanted by gemini's closing register without loss of the failing-row mains and their annotated +0.09 / +0.04 / −0.03 / +0.05 margin table.
- Two archaic in-text sub-decimals of v28 §6.5 bullets (0.18/0.19/0.5/0.52/0.7/0.79/0.81) replaced by their equivalence-statements in table + annotation; table itself byte-identical.

Signed: agent pass `se29`, 2026-09-18.
