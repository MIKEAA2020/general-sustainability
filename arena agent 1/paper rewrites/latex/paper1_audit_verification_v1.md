# Paper 3 — joint audit verification report (grok + gemini audit, 2026-09-20)

Every claim in the two external audits was re-verified against the actual
artifacts (v3 source, rendered PDFs, figure PNGs at full resolution, and the
package source) before any change was made. Verdicts below. Fixes shipped as
**v4** (new files; v1–v3 preserved) and package **1.1.2**.

## Claims REFUTED (no defect; no change made)

| Claim | Verdict | Evidence |
| --- | --- | --- |
| **grok G1 / headline:** §4.1 assigns x = 3/2 to the *false-positive* witness ("shortfall 1/2 at the false-positive witness x = 3/2"), contradicting §4.2/Fig. 2(b) | **Refuted — misparse of a line break.** The source reads "…shortfall $1/2$ at the false-positive witness and full financing at the rescue witness $x = 3/2$": x = 3/2 belongs to the *rescue* witness. Text, §4.2, Fig. 2(b) and the 24 checks agree; the signed reading (witness, shortfall) = (1/2, 1/2) is consistent everywhere. | v3.tex l.290–292; benchmark checks V6 |
| **gemini 1A:** Fig. 1(a)'s green curve is mislabelled — it "is plotting the composite index under benign conditions", legend error, benign breach absent | **Refuted — colour misread.** The green line's legend is "composite index s1+s2 (weight w=(1,1))"; the *benign* branch is the **red dashed** line (starts 6/5 = 1.2, dips to −3/10), exactly as the caption states. Both red curves sit at 1.2 at t = 0; the green at 12/5 = 2.4 is the index. Legend, geometry and caption are mutually consistent. | deposited fig_benchmark_v44.png, legend crop verified |

## Claims VERIFIED and FIXED (v4 / package 1.1.2)

| Claim | Verdict | Fix |
| --- | --- | --- |
| **grok G2 / gemini 1B:** Fig. 2(a) region labels read as definitions ("SLOW licensed (r ≤ ρ₂)" placed at r < ρ₁) — conflating exclusive regions with licensing conditions | **Verified** (the drawn regions are right; the unqualified labels misread as interval definitions) | Relabelled: "only SLOW licensed (r < ρ₁)" | "both licensed for ρ₁ ≤ r ≤ ρ₂" | "only FAST licensed (r > ρ₂)"; package pipeline synced, **1.1.2** |
| **gemini 2A:** five operators announced, four in the chain; role of the typed-endpoint operator unstated; E_end ambiguous | **Verified** | v4 §2.1 adds: "The fifth operator continues the pattern on the typed side: E_typ ⊆ E_end,typ ⊆ E_end…" (E_end is thereby pinned as the physical endpoint operator) |
| **gemini 2B:** κ* = 1 − x stated without the truncation; at x = 3/2 the linear form gives −1/2 | **Verified** (the paper's own Fig. 2 and Table 2 carry max(0, 1−x); abstract/§4.1 did not) | v4 §4.1: "truncated at zero (κ* = max(0, 1−x)) once the fund covers the buy-back" |
| **gemini 2D:** Farkas normalization unspecified; margin is scaling-dependent | **Verified** (unnormalized (1,1) gives margin 1/5; quoted 1/10 assumes Σλ = 1) | v4 §2.3: "normalized to sum to one (the certificate itself is invariant to positive scaling; the infeasibility margin … is defined by this normalization)" |
| **gemini 2E:** datum defined grammatically *as* a phase state | **Verified** | v4 §2.1: "A typed transition datum **comprises** a phase state …" |
| **gemini 2C:** belief/fibre terminology conflates labels with beliefs | **Verified as wording risk** (implementation is label-set beliefs; library docstring is precise) | v4 §2.2: belief glossed as "a set of states consistent with the observations so far"; update target "the set of labels reachable under the action" |
| **gemini 3A:** "nine modules" but prose lists eight, omitting `rational` | **Verified** | v4 §3.1 names `rational` first ("the exact rational helpers on which every other module rests") |
| **gemini 3B:** abstract's unconditional "no runtime dependencies" vs matplotlib/Pillow in the pipeline | **Verified** | v4 abstract: "no **third-party** runtime dependencies" (133 words, still ≤ 150) |
| **gemini 1D:** "(1/2, 1/2)" in §4.2/Fig. 2(b) collides with phase-state coordinate reading | **Verified** | v4 §4.2 note: pairs denote (x, κ*(x)) — fund level and shortfall — not the phase-state coordinates |
| **grok G3:** AI-declaration heading says "writing process" while the statement covers code development | **Verified** | v4 heading: "Declaration of generative AI in the **research process**" |
| **grok G4 / gemini 4-1:** refs [1] and [6] share the figshare DOI (duplicate citation) | **Verified** | v4 ref 2026a: trailing deposit sentence removed; the deposit is cited once (Deposit2026). DOI now appears exactly once in the source |

## Claims NOTED, no change (judgement calls)

- **grok/gemini "future-dating" (2026 dates):** today is 2026-09-20; all dates
  are current, not future. No change.
- **grok on V_weak's relation to dashboard use:** the interpretive link is
  delegated to the companion manuscript by design; the software paper states
  the mathematical fact. No change.
- **gemini 1C (Fig. 1(b) fund axis):** the orange dotted curve *is* the fund
  schedule x(t) ∈ {3/2, 1, 1/2} on the right axis; the "rebuild to 69/20"
  label belongs to the STAGED biomass/quota reading of the deposited
  benchmark figure. The dual-axis presentation is compressed but not
  conflated; noted for the next full figure revision rather than patched
  now (the deposited figure is byte-frozen by the reproduction manifest).

## Post-fix QA

v4: compile exit 0; 9 pp; 2 images; 0 `??`; overfull baseline (2.43 pt) only;
abstract 133 words (≤ 150); figshare DOI occurs once; all cross-references
resolve; all eleven v4 insertions verified present in the rendered PDF.
Package 1.1.2: `run_all.sh` all steps pass; SHA256SUMS regenerated (40).
