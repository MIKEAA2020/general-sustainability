#!/usr/bin/env python3
"""Phase L — v25_restructured -> v26_restructured.

Owner-approved scope (2026-09-13): O18, O22, O24, O25, O27, O29(+NEW-19
band-invariance), O33, O37, O38, O39, plus the NEW-18 supplement move
(DM mechanics of Section 5 -> S1.4). One pass, idempotent, count-asserted.

Numeric-set policy: the only tokens leaving the main text are the
Diebold-Mariano mechanics tokens moved to Supplement S1.4 (NEW-18, owner
approved). No other numeric token is added, removed, or altered.
"""

import re
import sys

SRC = "paperF1_retention_framework_v25_restructured.md"
DST = "paperF1_retention_framework_v26_restructured.md"

RULES = []  # (name, old, new)


def R(name, old, new):
    RULES.append((name, old, new))


# ---- L1 (O38): abstract rule-version parenthetical ---------------------------
R("L1", 
  "The same standard is applied, unchanged, to three scored objects in two unrelated domains:",
  "The same standard is applied, unchanged (the one recorded rule-version difference is stated in Section 4), to three scored objects in two unrelated domains:")

# ---- L2a (O37): moderate "portable and domain-free" ---------------------------
R("L2a",
  "The standard in one page: three obligations, portable and domain-free.",
  "The standard in one page: three obligations, portable in their statement and demonstrated here on two domains.")

# ---- L2b (O18): pointer to the standalone specification (Supplement S2) ------
R("L2b",
  "The demonstration — one rule on three scored objects in two domains, an empty retained set reached by two different routes — shows the standard working.",
  "The normative core and a fillable reporting checklist are stated separately as the two-page Supplement S2, independent of any worked example. The demonstration — one rule on three scored objects in two domains, an empty retained set reached by two different routes — shows the standard working.")

# ---- L3 (O29): practical-equivalence umbrella on the tie band ----------------
R("L3",
  "The deciding score is the pre-registered specification’s rolling-origin RMSE pair at h=1 and h=5 (H3).",
  "The deciding score is the pre-registered specification’s rolling-origin RMSE pair at h=1 and h=5 (H3). The band is a practical-equivalence margin: fixed here at 5% by pre-registration, it may instead be set on a simulation-calibrated basis (Section 8) or on a decision basis — a margin judged irrelevant to the decision at hand — with the basis stated.")

# ---- L4 (O24): negative-certificate claim-strength taxonomy N0-N3 ------------
R("L4",
  "**Definition 2.2 (Negative certificate).** A machine-verified finding of non-retention under a stated rule, scoped to estimator, ladder, and series. Weaker than a statistical null. Distinct from the Brier secondary diagnostic. The 1992–1993 fishing moratorium is deliberately not evaluated.",
  "**Definition 2.2 (Negative certificate).** A machine-verified finding of non-retention under a stated rule, scoped to estimator, ladder, and series. Weaker than a statistical null. Distinct from the Brier secondary diagnostic. The 1992–1993 fishing moratorium is deliberately not evaluated.\n\n**Claim strength.** A negative certificate carries one of four levels. N0 — the rule ran and the verdict is its output. N1 — N0 plus archived margins and the gate decomposition, so the verdict is reproducible and its withholding gate is known. N2 — N1 plus the Section 3 information-set audit, so the verdict is scoped to what was available at each origin. N3 — N2 plus operating characteristics at the object’s own length and noise attaining the adequacy targets of Section 6.1, making non-retention evidential for the affected class. The verdicts reported here carry N2: the cod operating characteristics are class-conditional (power is limited by identification at every band width, Section 8), and the Edwards calibration is registered prospectively (Section 8). A certificate expires when its inputs change — a revised data vintage, a re-scored origin, an amended rule — and a combined claim carries the lowest level of its parts. N3 is the level at which non-retention may be reported as evidence rather than description.")

# ---- L5 (O27 + O29): two-axis reading guide + epistemic-consequence ----------
R("L5",
  "Specificity of 0.95–0.995 is scoped explicitly to in-class truth and does not transfer to misspecified settings.",
  "Specificity of 0.95–0.995 is scoped explicitly to in-class truth and does not transfer to misspecified settings.\n\n**Two axes for reading a verdict.** The outputs of the algorithm answer one question — what the rule decided — and this section answers the other — how strongly the decision may be read. Every verdict is best read on two axes: the predictive result (retained, not retained, or declined on class grounds) and its structural interpretation (identification-limited, gate-withheld, or structurally redundant). The same output label carries different evidential weight in different classes: non-retention is strong evidence against the module where the rule has power, and is descriptive rather than evidential for the affected classes where it does not, unless and until a calibration attains the adequacy targets (Section 8).")

# ---- L6 (O27): M2m clarifying sentence (Section 4) ---------------------------
R("L6",
  "Without the band it would pass H1 but still be declined on class grounds, so the empty set holds either way.",
  "Without the band it would pass H1 but still be declined on class grounds, so the empty set holds either way. The M2m decline is a ladder-membership verdict — the map reduces to the simpler AR(1) member under the declared conditions — not a predictive finding; its predictive margins remain reported in Table 5 (−7.16% and −17.34% versus persistence).")

# ---- L7 (O25): Edwards decision-context paragraph ----------------------------
R("L7",
  "The 15-year floor applies to rolling origins only; fixed windows use their declared training sets.",
  "The 15-year floor applies to rolling origins only; fixed windows use their declared training sets.\n\n**Decision context.** The Edwards verdicts bear on forecasting claims about J-17, not on the monitoring or permitting framework itself. Persistence remains the decision baseline — the pre-registered H2/H3 anchor — and non-retention records that no module demonstrated operational skill over it at one or five years: a statement about the evidence available at the origin, which leaves the index well and its management instruments in place. The oracle bound shows what perfect driver information would buy (−42.96% at h=1) and what the module class leaves on the table.")

# ---- L8 (O25): cod decision-context paragraph --------------------------------
R("L8",
  "**Conditional hindcast disclosure.** The predictand is retrospectively reconstructed rather than taken from vintages at each origin, and catch is supplied along the horizon. This is a conditional hindcast, not an operational forecast, and must not be reported as skill.",
  "**Conditional hindcast disclosure.** The predictand is retrospectively reconstructed rather than taken from vintages at each origin, and catch is supplied along the horizon. This is a conditional hindcast, not an operational forecast, and must not be reported as skill.\n\n**Decision context.** The cod verdicts are hindcast verdicts about assessment-module forecast utility, not verdicts about stock status or about the assessments themselves. The scored target is the assessment’s own retrospective biomass, and modules supplied the realised catch still fail to beat persistence, so the verdict licenses the negative forecasting claim and nothing about the drivers of the collapse: total landings are not SSB-equivalent removals, and the failed collapse reproduction does not test whether fishing caused it.")

# ---- L9 (O29 + NEW-19): band-invariance of reported verdicts -----------------
R("L9",
  "It never re-opens the verdicts reported here, which remain decided by the pre-registered 5% band (the calibration procedure is specified in Section 8).",
  "It never re-opens the verdicts reported here, which remain decided by the pre-registered 5% band (the calibration procedure is specified in Section 8). The reported verdicts are band-invariant — on cod no margin approaches the band (ranking alone decides, Section 5), and on Edwards the withheld module is declined on class grounds at any band (Section 4) — so the calibration governs the interpretation of future verdicts, not the verdicts reported here. A band may instead be set on a decision basis, the margin a decision-maker judges operationally irrelevant, with the basis stated.")

# ---- L10a (O29): decision-based margin admissible alternative (Section 8) ----
R("L10a",
  "If no band attains both targets, the attainable frontier is reported and the 5% band is retained.",
  "If no band attains both targets, the attainable frontier is reported and the 5% band is retained. A decision-based margin is an admissible alternative basis; whichever basis is adopted is stated with the verdict.")

# ---- L10b (O22): third-domain prospective registration -----------------------
R("L10b",
  "With these elements fixed, the reporting obligations of Sections 2 and 3",
  "**Third domain.** Before a third scored object is evaluated, the same elements are registered for it: the Section 3 information-set audit completed on its inputs; origin-matched baselines on the object’s own origins; the retention rule, its band, and the band’s stated basis fixed before scoring; an operating-characteristic study at the object’s own length and noise before any evidential claim (N3, Section 2.2); pinned-seed archival of every score, seed map, and forecast file; and every verdict reported with its certificate level. A third domain is not required by the standard — the obligations are portable — but every new application is a commitment of this form fixed before its data are seen.\n\nWith these elements fixed, the reporting obligations of Sections 2 and 3")

# ---- L11 (O33): tiered adoption guidance (Section 9) -------------------------
R("L11",
  "The formal information-set table — what is available at origin t and to which module — is the most useful single addition, proposed as a reporting template.",
  "The formal information-set table — what is available at origin t and to which module — is the most useful single addition, proposed as a reporting template.\n\n**Adoption tiers.** The standard admits graded adoption. Core: state the rule as an explicit algorithm before scoring and report the margins. Evidential: add the information-set audit and the operating-characteristic study under processes the study’s own models could generate — the minimum accompanying evidence above. Strong non-retention: the N3 level of Section 2.2, attained only when the calibration meets the adequacy targets at the object’s own length and noise, before non-retention may be reported as evidence. The tiers are an adoption ladder; the evidential tier is this article’s own practice.")

# ---- L12 (O39): three-quantity terminology (Section 6.1) ---------------------
R("L12",
  "Simulation scores synthetic series only. No empirical verdict changes.",
  "Simulation scores synthetic series only. No empirical verdict changes.\n\nThree quantities are kept distinct throughout. Model-class identification — the rule retains the generating module, the true-class retention rate this article calls power. Predictive selection — a module beats the declared baselines on a scored object (Sections 4 and 5). Mechanism attribution — a predictive gain the module’s mechanism did not cause (the D6–D7 rows).")

# ---- L13 (NEW-18): DM mechanics of Section 5 -> compressed; moved to S1.4 ----
R("L13",
  "**Uncertainty layer.** Diebold–Mariano descriptive loss-differential diagnostics and moving-block-bootstrap intervals attach to the margins. DM z tests the mean squared-loss differential. CI and p come from a separate moving-block bootstrap of the RMSE gap, because the square root compresses the heavy collapse-window tail; the two can disagree, and the bootstrap is tighter on this data. p is the bootstrap percentile-tail fraction p_perc = 2 · min{#(Δ* ≤ 0), #(Δ* ≥ 0)} / B. The CI excludes zero iff p < 0.05, verified with 15 CIs that exclude zero (1 Spec A + 6 Spec B h=1 + 8 Spec B h=5) and 17 that include (7 + 8 Spec A + 2 Spec B h=1). There are zero exceptions where the bootstrap CI and bootstrap p disagree. DM z on the squared-loss difference d_i = L_{A,i} − L_{B,i}, HAC-scaled, can disagree when variance is inflated by catastrophic origins. This occurs in 5 of 32 rows in the full 32-row universe — including the four alternative-comparator M2-versus-M1b rows, which the companion’s 28-row subset excludes (e.g., Spec A M4 versus M3 h=1 [+4.7, +144.7], z = 0.99, p < 0.001 (bootstrap percentile-tail); Spec B M3 versus persist h=1 [+1.0, +92.5], z = 1.85, p = 0.042; Spec B M4 versus M3 h=5 [+20.2, +177.4], z = 1.88, p = 0.007). DM statistics are not calibrated for this design — expanding-window recursive estimation, overlapping training samples, near-nested models, a smoothed target, and multiple comparisons all bear on calibration. The verdicts do not rest on DM statistics, which are reported as descriptive loss-differential diagnostics. Bootstrap intervals are conditional on archived forecast paths and propagate no parameter, revision, catch, or covariate uncertainty.",
  "**Uncertainty layer.** Diebold–Mariano loss-differential diagnostics and moving-block-bootstrap intervals attach to the margins, reported as descriptive; the verdicts do not rest on DM statistics, which are not calibrated for this design (expanding-window recursive estimation, overlapping training samples, near-nested models, a smoothed target, multiple comparisons). The mechanics and the full 32-row universe are in Supplement S1. Bootstrap intervals are conditional on archived forecast paths and propagate no parameter, revision, catch, or covariate uncertainty.")

# ---- L14: Data availability — supplements listed ----------------------------
R("L14",
  "Companion papers: Abaee (2026a) — the Edwards J-17 scored ladder; Abaee (2026b) — the Northern cod scored ladder.",
  "Companion papers: Abaee (2026a) — the Edwards J-17 scored ladder; Abaee (2026b) — the Northern cod scored ladder. Supplements S1 and S2 are distributed with the manuscript: S1 carries the moved verification detail (uncertainty-robust variants, the pre-check diagnostic, the verification appendix, and the Diebold–Mariano mechanics moved from Section 5); S2 is the standalone two-page specification and fillable checklist.")


def main():
    src = open(SRC, encoding="utf-8").read()
    out = src
    applied = []
    for name, old, new in RULES:
        n = out.count(old)
        assert n == 1, f"{name}: anchor count {n} != 1"
        assert new not in out, f"{name}: replacement already present (not idempotent-safe)"
        out = out.replace(old, new, 1)
        applied.append(name)
    open(DST, "w", encoding="utf-8").write(out)
    print(f"applied {len(applied)} rules: {applied}")
    print(f"{SRC}: {len(src)} chars -> {DST}: {len(out)} chars")


if __name__ == "__main__":
    main()
