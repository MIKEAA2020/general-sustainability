"""Build paper5 supplementary v11 from v10 (completeness + alignment). Asserted-once."""
import sys

SRC = '/home/user/paper5_v34/paper5_supplementary_v10.md'
DST = '/home/user/paper5_v35/paper5_supplementary_v11.md'

s = open(SRC, encoding='utf-8').read()
n0 = len(s)

SUBS = [
 ('P1-nine-bodies',
  "It carries eight bodies of material:",
  "It carries nine bodies of material:"),
 ('P1b-s9-listed',
  "the empirical hypotheses with their declared tests (S7); and the reproducibility register (S8). Every item carries",
  "the empirical hypotheses with their declared tests (S7); the reproducibility register (S8); and the screen-sensitivity battery and stage-scan decomposition records (S9). Every item carries"),
 ('P2-s1-s35',
  "cohort selection and processing routines are registration requirements.",
  "cohort table, screen routine, and multiplicity reconstruction deposited, zero count re-execution-verified; sensitivity battery and endpoint extension at nominal tier (S9.1)."),
 ('P3-s1-s36',
  "(conditional simulations on 100–200 yr synthetic records; simulation code and seeds are registration requirements).",
  "(conditional simulations on 100–200 yr synthetic records; code and seeds deposited, independently re-executed; H400 cells supplementary)."),
 ('P4-s1-s34mag',
  "the effort-carried signal magnitudes (80–240% effort vs 1–2% biomass; exploratory computational record)",
  "the effort-channel excursion record (effort excursions exceeding biomass excursions; nominal reconstruction record)"),
 ('P5-s1-s23',
  "two-operator discipline and $\\det(M-e^{i\\theta}I)=0$ locality (definition)",
  "two-operator discipline and $\\det(D\\mathcal P_{T_r}(X^*)-e^{i\\theta}I)=0$ locality (definition)"),
 ('P6-s1-schaefer',
  "the Schaefer degenerate-member correction (identity-level statement about the family)",
  "the Schaefer formal-limit correction (identity-level statement about the family)"),
 ('P7a-s1-s24s25',
  "- **Main text §3.1:** forward invariance (theorem; proof displayed in full in the main text).",
  "- **Main text §2.4:** the 42-stock cohort definition, band prespecification, and AR(1)-null/BH pipeline (methods; materials deposited, Appendix A).\n- **Main text §2.5:** the injected-signal power design (methods; code and seeds deposited; H400 cells supplementary).\n- **Main text §3.1:** forward invariance (theorem; proof displayed in full in the main text)."),
 ('P7b-s1-s41s43',
  "- **Main text §4.4:** the five falsification criteria (definitions of outcomes counting against the mechanism).",
  "- **Main text §4.1:** the operator-substitution moral (interpretation of the §3.4 record; no new computation).\n- **Main text §4.2:** the null's bounded refutation value (interpretation; Russell precedent as disciplinary template).\n- **Main text §4.3:** the cod case at its exact status (descriptive partition; falsification benchmark).\n- **Main text §4.4:** the five falsification criteria (definitions of outcomes counting against the mechanism)."),
 ('P7c-s1-s47',
  "- **S2–S8:** each item carries its status on the line.",
  "- **Main text §4.7:** the nine limitations (status declarations; the battery outcomes restated from S9.1).\n- **S2–S9:** each item carries its status on the line."),
 ('P8a-taum',
  "$\\tau_m$ a measurement delay",
  "$\\tau_m$ a memory/filter timescale"),
 ('P8b-eta',
  "$\\eta$ the softplus effort-shaping coefficient",
  "$\\eta$ the effort-response coefficient"),
 ('P8c-emax',
  "$E_{\\max}$ the effort scale at which the softplus term saturates",
  "$E_{\\max}$ the effort ceiling"),
 ('P8d-d0',
  "$\\delta_0$ a baseline signal feedthrough",
  "$\\delta_0$ the effort-law gain"),
 ('P8e-zref',
  "$Z_{\\rm ref}$ a reference signal level",
  "$Z_{\\rm ref}$ the reference deficit"),
 ('P8f-dref',
  "$\\Delta_{\\rm ref}$ a reference signal scale",
  "$\\Delta_{\\rm ref}$ the reference scale"),
 ('P9-s23-table3',
  "Two calibrated parameter points are two points in $(\\eta/r,\\varrho)$, not one class.",
  "Two calibrated parameter points are two points in $(\\eta/r,\\varrho)$, not one class. At the baseline calibration the closed form evaluates to the main-text Table 3 fixed point $(89.55188, \\delta, 2.08962)$."),
 ('P10-s35-ideal',
  "and it enters the main text only as the ideal limit of the sampled-governance comparison.",
  "and it is a benchmark for the sampled-governance comparison, not invoked in the main text."),
 ('P11-s37-governs',
  "No calibrated predictive distribution is claimed. This boundary-only content governs every power and detectability statement of the main text (§3.6).",
  "No calibrated predictive distribution is claimed. These boundaries govern proxy-based detectability readings; the main-text §3.6 power analysis injects synthetic signals and uses no empirical proxy."),
 ('P12-s4-region',
  "lies below the anchovy-class response region — controller nonclassification",
  "lies below the anchovy-class review-interval response region — controller nonclassification"),
 ('P13-s8-other',
  "the legacy code and machine outputs are not committed, and the other retrospective computational and data results remain unreproduced.",
  "the legacy code and machine outputs are not committed, and the other legacy retrospective results remain unreproduced."),
 ('P14-s8-typo',
  "the screen-sensitivity battery (§S9.1),",
  "the screen-sensitivity battery (S9.1),"),
 ('P15-s8-appa',
  "This section records the reproducibility status of every empirical and computational claim in the article.",
  "This section records the reproducibility status of every empirical and computational claim in the article. The consolidated requirements are stated in Appendix A; this register tracks their discharge."),
 ('P16-s91-dep',
  "`screen_battery_v31.log`) are deposited with this revision; the base variant",
  "`screen_battery_v31.log`) are deposited with the article; the base variant"),
 ('P17-s91-status',
  "**Status: nominal tier (seed-fixed,\nlogged); the bit-replication",
  "**Status: nominal tier (seed-fixed,\nlogged), battery and endpoint extension alike; the bit-replication"),
 ('P18-s21-interval',
  "can repeatedly rise and fall across a common level.",
  "can repeatedly rise and fall across a common interval."),
]

fails = []
for tag, old, new in SUBS:
    c = s.count(old)
    if c != 1:
        fails.append((tag, c))
        continue
    s = s.replace(old, new, 1)

if fails:
    print('FAILED:', fails)
    sys.exit(1)
open(DST, 'w', encoding='utf-8').write(s)
print(f'supp v11 built: {len(SUBS)}/{len(SUBS)} subs ok, {n0} -> {len(s)} chars')
