"""
apply_batch7_wave2.py
---------------------
Batch-7 wave 2: the six-paper implementation pass (Task 71). Builds,
non-destructively (fail-loud exact-match replacements only):

  1. arena agent 1/paper rewrites/paperE1_cod_forecast_ladder_v10.md    (from v9)
  2. arena agent 1/paper rewrites/paper1_assessment_separation_v19.md   (from v18)
  3. arena agent 1/paper rewrites/paper5_sampled_governance_v20.md      (from v19)
  4. arena agent 1/paper rewrites/paper3_material_ledgers_v27.md        (from v26)
  5. arena agent 1/paper rewrites/paper4_delay_dynamics_v26.md          (from v25)
  6. arena agent 1/paper rewrites/paper2_obstruction_calculus_v8.md     (from v7)

E1 v10 lands the factual-recheck layer that the joint-audit evaluation
describes but that was never committed (no v10 file existed). Every number
was re-verified against wave_e_cod before this build:
  A7  p0=98.05, control(S_tm1)=184.43, M4=195.57 (h=1) -> delay 86.38 /
      model 11.14; p0=264.72, control 329.84, M4=488.27 (h=5) -> delay
      65.12 / model 158.43.
  A3  code bounds r in (0.001,2], K in [max_train_S + 10, 5000]; 500 is
      the multi-start initialiser.
  A5  recovery-window K-sweep (coarse-regime catch, train 1995-2007):
      MSE 127.4 (K=5000, r=0.435) -> 149.9 (K=60, r=0.773); training
      RMSE 11.29 -> 12.24 kt (spread 0.95).
  A1/A2 collapse fit (train 1983-1990, C=240): r=1.9350, K=1032.7;
      equilibria 144.1 (repelling) / 888.6 (attracting); one-step map
      monotone below 783.2 (F' = 0 there); F'(attractor) = -0.39.
Plus the v9-claimed-but-absent presentation fixes (keyword, origin-matched
abstract, §2.3 Brier/Direction conventions, "weaker than a statistical
null", Highlights <= 85 chars, abstract <= 300 words).

P1 v19 repairs the reference fabric damaged by the v17 hybrid edit
(von Neumann 1928 / Sion 1958 / Ben-Tal et al. 2004 cited in §4.10 but
absent from the References).

P5 v20 repairs the internal contradictions left by the v19 honest-tier
correction (abstract over-claim; §3.4 and §4.1 still asserting the
archived windows as findings).

P3 v27 applies the verified micro-error cluster (Prop 2 cite, §3.3
condition name, §2.2 list title, §3.1 "first three", §5.4 double-C
disambiguation, 47.5 not 47.6, the blank-cell claim).

P4 v26 applies the verified small-error cluster (tau_M pair, Section 5.1
pointer, regime (iii) unstable-arm range).

P2 v8 applies the first safe tranche of the P2 audit (a-fortiori
direction, abstract scoping, companion reference, §6.4 drift-certificate
number). The deeper theorem-level repairs are registered as follow-ups,
not applied.

No frozen verdict, score, kernel, spectral record, or table value changes
anywhere; the E1 decomposition numbers are relabelled/decimalised versions
of values already printed in §4 of v9.
"""
from __future__ import annotations

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
PAPERS = os.path.join(REPO, "arena agent 1", "paper rewrites")


def replace_once(text: str, old: str, new: str, tag: str) -> str:
    n = text.count(old)
    if n != 1:
        sys.exit(f"FAIL [{tag}]: expected exactly 1 occurrence, found {n}.\n--- target start ---\n{old[:220]}\n--- target end ---")
    return text.replace(old, new, 1)


def rd(name):
    with open(os.path.join(PAPERS, name), encoding="utf-8") as f:
        return f.read()


def wr(name, text):
    path = os.path.join(PAPERS, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote:", name)


# ============================================================================
# 1. E1: v9 -> v10
# ============================================================================
e1 = rd("paperE1_cod_forecast_ladder_v9.md")

E1_LOG = """*Version log (v10).* Lands the factual-recheck layer recorded in the joint-audit evaluation's E1 block (the described v10 file was never committed; every number below was re-verified against the committed data and code before this build). (A7) The M4-gap decomposition of Section 4 is relabelled: the one-year gap decomposes into the information delay (the year-old start under the same persistence rule, 86.4 of 97.5 kt) and the surplus model's own cost (the remaining 11.1 kt); five-year: 65.1 versus 158.4 kt — the v9 labels had the two component names swapped — and the constructive finding is stated (at $h=1$ the model's own penalty is about 11 kt; the delay, not the structure, separates M4 from persistence). (A3) Section 2.2's declared box is corrected to the code's actual bounds ($K$ above the training-window maximum; 500 kt is the multi-start initialiser), so M1b's $K = 105.9$ kt is an interior fit. (A5) Section 3.2 gains the flat-valley ranking caveat (fixed-$K$ sweep: MSE 127.4–149.9 kt², training RMSE 11.29–12.24 kt, $r$ 0.435–0.773; the $(r,K)$ pair is not identified, valley-variant ordering not a robust ranking). (A1/A2) The Section 1 obstruction sentence and Proposition 4.1 are restated for the fitted two-equilibrium collapse map (repeller 144 kt, attractor 889 kt, one-step map monotone below 783 kt, damped approach with slope $-0.39$). (A4) One unifying sentence on the catch-dependence. Presentation fixes the v9 log claimed but the file lacked: the keyword set, the origin-matched abstract numbers, the Section 2.3 Brier and Direction conventions, "weaker than a statistical null", Highlights of at most 85 characters, abstract of at most 300 words. No score, verdict, or table value changes; the decomposition figures are relabelled and decimalised versions of values already printed in v9's Section 4.
"""
e1 = replace_once(
    e1,
    "**Prepared in the format of Fisheries Research**\n\n## Highlights",
    "**Prepared in the format of Fisheries Research**\n\n" + E1_LOG + "\n## Highlights",
    "E1 version log",
)

# --- Highlights: H1, H4, H5 over 85 chars ---
e1 = replace_once(
    e1,
    "- The scored ladder (a forward-ordered set of seven models — persistence, mean, M1, M1b, M2, M3, M4 — evaluated by a fixed retention rule, and not a strict nesting for M2 and M4) is run from the two naive baselines on two assessment specifications",
    "- A scored seven-model ladder runs against two naive baselines, two specifications",
    "E1 Highlights 1",
)
e1 = replace_once(
    e1,
    "- A negative certificate is issued for the scored Schaefer/Allee ladder on the two unpooled series, scoped to this estimator and ladder",
    "- Negative certificate for the scored Schaefer/Allee ladder, scoped to estimator",
    "E1 Highlights 4",
)
e1 = replace_once(
    e1,
    "- Post-2015 production stall reconstructions and the forecast ladder fail in the same configuration (constant-productivity surplus law), scored on different objects",
    "- Stall reconstructions and the ladder share the constant-productivity failure mode",
    "E1 Highlights 5",
)

# --- Abstract: trims + origin-matched numbers ---
e1 = replace_once(
    e1,
    "The test is applied to Northern cod (*Gadus morhua*) in NAFO divisions 2J3KL. The primary predictand is the NCAM M-shift spawning-stock biomass series (DFO, 2016, Table A2) for 1983–2015, with LRP 884.6 kt. Forward-ordered surplus-production models form a scored ladder (a forward-ordered set of models evaluated by a fixed retention rule, not a strict nesting for M2 and M4), and two naive baselines issue fixed-window and rolling-origin forecasts.",
    "The test is applied to Northern cod (*Gadus morhua*), NAFO 2J3KL. The primary predictand is the NCAM M-shift SSB series (DFO, 2016, Table A2) for 1983–2015, LRP 884.6 kt. Surplus-production modules form a scored ladder (not a strict nesting for M2 and M4), and two naive baselines issue fixed-window and rolling-origin forecasts.",
    "E1 abstract para 1",
)
e1 = replace_once(
    e1,
    "The collapse window is missed by every model (694–819 kt for the structural models; the naive baselines score 670 and 688 kt).",
    "The collapse window is missed by every model (694–819 kt structural; 670 and 688 kt naive).",
    "E1 abstract para 2",
)
e1 = replace_once(
    e1,
    "Within the scope of this estimator and ladder, the evidence here supports a negative certificate scoped to this ladder and estimator: the scored one-step least-squares Schaefer/Allee ladder on these two unpooled series does not beat persistence on the primary score, and modules not identified on the training window increase error. The same rule applied to a second, unpooled specification (xteNCAM, 1954–2024, LRP 276 kt) gives the same non-retention outcome under the same rule (persistence 88 kt versus 120 kt).",
    "Within this estimator and ladder, the evidence supports a negative certificate scoped to both: the scored one-step least-squares Schaefer/Allee ladder on these two unpooled series does not beat persistence on the primary score, and modules not identified on the training window increase error. The same rule applied to a second, unpooled specification (xteNCAM, 1954–2024, LRP 276 kt) gives the same non-retention outcome (origin-matched persistence 84 kt versus M1's 120 kt at $h=1$; the mixed-origin reading is 88 kt).",
    "E1 abstract para 3",
)

# --- Keywords ---
e1 = replace_once(
    e1,
    "**Keywords:** northern cod; recruitment forecasting; forecast evaluation; stock assessment; prediction skill",
    "**Keywords:** northern cod; biomass forecasting; surplus production; forecast evaluation; stock assessment; prediction skill",
    "E1 keywords",
)

# --- A3: §2.2 bounds ---
e1 = replace_once(
    e1,
    "Parameters are estimated by one-step least squares on the training window only. Bounds: $r\\in(0.001,2]$, $K\\in[500,5000]$ kt; the reported fits attain both endpoints of the declared box.",
    "Parameters are estimated by one-step least squares on the training window only. Bounds: $r\\in(0.001,2]$ and $K$ constrained above the training-window maximum — the estimation code optimises $K$ on $[\\max_{\\mathrm{train}} S + 10, 5000]$ kt, with $500$ kt the multi-start initialiser rather than the lower bound, consistent with the frozen specification's constraint of $K$ above the training maximum. The reported fits attain the upper endpoint ($K = 5000$ kt) where the data prefer an unbounded carrying capacity; M1b's recovery-window $K = 105.9$ kt is a valid interior fit, not a bound violation.",
    "E1 §2.2 bounds (A3)",
)

# --- §2.3: Brier + Direction conventions ---
e1 = replace_once(
    e1,
    "The primary score is RMSE of SSB (kt). Secondary scores are mean absolute error, RMSE on $\\log S$, the Brier score for $\\mathbf{1}\\{\\hat S<\\mathrm{LRP}\\}$, and the sign-hit rate of $\\Delta S$ on fixed windows.",
    "The primary score is RMSE of SSB (kt). Secondary scores are mean absolute error, RMSE on $\\log S$, the Brier score for $\\mathbf{1}\\{\\hat S<\\mathrm{LRP}\\}$, and the sign-hit rate of $\\Delta S$ on fixed windows. On Specification A the Brier indicator is near-degenerate — the $884.6$-kt LRP sits above the entire origin range, so the score separates little (Section 3.3 gives the record). The sign-hit rate is conventionally $0.00$ for persistence, whose forecast $\\Delta S = 0$ has no sign; persistence is excluded from that ranking by declaration.",
    "E1 §2.3 Brier/Direction conventions",
)

# --- A5 + A4: §3.2 additions ---
e1 = replace_once(
    e1,
    "not an inconsistency between fitting objects.",
    "not an inconsistency between fitting objects. The same flat valley caps what the ranking can resolve: refitting the recovery-window Schaefer map with $K$ fixed anywhere on $[60, 5000]$ kt and $r$ re-optimised moves the one-step training objective only from mean squared error $127.4$ to $149.9$ kt$^2$ (training RMSE $11.29$–$12.24$ kt, a spread under $0.95$ kt) while $r$ compensates from $0.435$ to $0.773$ — on this window the $(r, K)$ pair is not identified, and the ordering of valley variants is not a robust ranking. One mechanism unifies both faces of the catch-dependence: a constant catch shifts the flat valley's minimiser without moving the objective, so the rolling scores (refit at every origin) are insensitive to the catch treatment while the single fixed-window fit is not.",
    "E1 §3.2 A5/A4 additions",
)

# --- A1/A2: §1 obstruction sentence ---
e1 = replace_once(
    e1,
    "In the monotone parameter regime fitted here, such a map approaches its equilibrium monotonically and cannot reproduce a path that crashes and then recovers, so the scored test measures how severely that bar penalizes out-of-sample error rather than whether the bar exists.",
    "In the fitted collapse-window parameterisation ($r = 1.935$, $K = 1032.7$ kt, constant catch $240$ kt) such a map has two positive equilibria — a lower repelling point at $144$ kt and an upper attractor at $889$ kt, with the one-step map monotone below $783$ kt — so every trajectory either settles toward the attractor or collapses toward the absorbing state, and no path that crashes and then recovers is a trajectory of the map; the scored test measures how severely that bar penalizes out-of-sample error rather than whether the bar exists.",
    "E1 §1 obstruction (A1/A2)",
)

# --- A1/A2: Proposition 4.1 statement ---
e1 = replace_once(
    e1,
    "*Let $S_{t+1}=F(S_t)$ be an autonomous one-dimensional surplus-production map of Definition 2.1 in a monotone parameter regime. If the observed path $(S_t)$ is non-monotone (crash followed by partial recovery), then no trajectory of $F$ reproduces $(S_t)$ exactly. M1's collapse failure on Specification A is the finite-sample face of this obstruction: it is the incompatibility of the observed path with the autonomous surplus-production model class.*",
    "*Let $S_{t+1}=F(S_t)$ be an autonomous one-dimensional surplus-production map of Definition 2.1 with at most two positive equilibria — a lower repelling point and an upper attracting point — and a one-step map monotone below its maximum; the single-equilibrium monotone regime is the special case, and the fitted collapse-window map ($r = 1.935$, $K = 1032.7$ kt, constant catch $240$ kt) has exactly this form (repeller $144$ kt, attractor $889$ kt, monotone below $783$ kt). If the observed path $(S_t)$ is non-monotone (crash followed by partial recovery), then no trajectory of $F$ reproduces $(S_t)$ exactly. M1's collapse failure on Specification A is the finite-sample face of this obstruction: it is the incompatibility of the observed path with the autonomous surplus-production model class.*",
    "E1 Prop 4.1 statement (A1/A2)",
)

# --- A1/A2: Proposition 4.1 proof ---
e1 = replace_once(
    e1,
    "*Proof.* In the monotone parameter regime, $F$ is monotone on each side of its unique positive equilibrium $S^\\star$, and every trajectory approaches $S^\\star$ monotonically (overshoot is excluded by the regime). A path that crashes through $S^\\star$ and then recovers is therefore not a trajectory of $F$. □",
    "*Proof.* Below the lower equilibrium $F(S) < S$, so every trajectory that enters that region decreases toward the absorbing state and never rises — a crash followed by recovery is excluded from below. Between the two equilibria $F(S) > S$, so trajectories there move toward the attractor (in the fitted map with damped oscillations around it — the slope at the attractor is $F'(S^\\star) \\approx -0.39$ — not a monotone approach); a crash through the repeller is excluded from above. A path that crashes through the lower equilibrium and then recovers is therefore not a trajectory of $F$. □",
    "E1 Prop 4.1 proof (A1/A2)",
)

# --- "weaker than a statistical null" (two sites) ---
e1 = replace_once(
    e1,
    "— a machine-verified finding of non-retention, distinct from a statistical null result —",
    "— a machine-verified finding of non-retention, weaker than a statistical null result —",
    "E1 §3.3 null rewording",
)
e1 = replace_once(
    e1,
    "A negative certificate is distinct from a statistical null result; it is scoped to the estimator, the ladder, and the series on which it is issued.",
    "A negative certificate is weaker than a statistical null result; it is scoped to the estimator, the ladder, and the series on which it is issued.",
    "E1 Def 4.2 null rewording",
)

# --- A7: §4 decomposition relabel ---
e1 = replace_once(
    e1,
    "its one-year gap against persistence mixes the delay cost with information loss",
    "its one-year gap against persistence mixes the information delay with the model's own cost",
    "E1 §4 lead-in (A7)",
)
e1 = replace_once(
    e1,
    "on Specification A the control reads 184 kt at $h = 1$ and 330 kt at $h = 5$, against M4's 196 kt and 488 kt, so the information loss accounts for 86 of the 98 kt one-year gap and the delay itself for the remaining 12 kt, and 65 versus 158 kt of the five-year gap; on Specification B the control reads 158 kt and 337 kt against M4's 206 kt and 1031 kt, where the delay's own contribution is again modest at $h = 1$ (48 of 118 kt) and dominant at $h = 5$ (694 of 713 kt). M4's error is therefore mostly information loss at the one-year horizon on both specifications, and mostly the delay's persistence of stale information at the five-year horizon on Specification B.",
    "on Specification A the control reads 184.4 kt at $h = 1$ and 329.8 kt at $h = 5$, against M4's 195.6 kt and 488.3 kt, so the information delay — the year-old start under the same persistence rule — accounts for 86.4 of the 97.5-kt one-year gap and the surplus model's own cost for the remaining 11.1 kt, and 65.1 versus 158.4 kt of the five-year gap; on Specification B the control reads 158 kt and 337 kt against M4's 206 kt and 1031 kt, where the model's own cost is again modest at $h = 1$ (48 of 118 kt) and dominant at $h = 5$ (694 of 713 kt). M4's error is therefore mostly the information delay at the one-year horizon on both specifications, and mostly the surplus model's own structure at the five-year horizon on Specification B: at $h = 1$ the surplus model's own penalty is only about 11 kt — the delay, not the structure, separates M4 from persistence — while at $h = 5$ on Specification B the model's own cost dominates (694 of 713 kt).",
    "E1 §4 decomposition (A7)",
)

# --- sanity: abstract <= 300 words, Highlights <= 85 chars ---
_abs = re.search(r"## Abstract\n(.*?)\n\n\*\*Keywords", e1, re.S).group(1)
_wc = len(_abs.split())
if _wc > 300:
    sys.exit(f"FAIL [E1 abstract length]: {_wc} words > 300.")
print(f"E1 abstract: {_wc} words (<=300 OK)")
_high = re.findall(r"^## Highlights\n\n((?:- .*\n)+)", e1, re.M)
if not _high:
    sys.exit("FAIL [E1 highlights]: block not found.")
for line in _high[0].strip().split("\n"):
    if len(line) > 85:
        sys.exit(f"FAIL [E1 highlights]: line over 85 chars: {line[:90]}...")
print("E1 Highlights: all <= 85 chars OK")

wr("paperE1_cod_forecast_ladder_v10.md", e1)

# ============================================================================
# 2. P1: v18 -> v19 (dangling references repair)
# ============================================================================
p1 = rd("paper1_assessment_separation_v18.md")

P1_LOG = """*Version log (v19).* Repairs the reference fabric damaged by the v17 hybrid edit: von Neumann (1928), Sion (1958), and Ben-Tal et al. (2004) are cited in the Section 4.10 Remark but had no entries in the References; the three entries are added in alphabetical position. No text, theorem, proof, or number changes; the remaining follow-up edits registered for this paper (the typed-endpoint operator, the Section 1.1 companion-prose strip, the Section 2 tuple cut, the notation pass, and the further demotions) are unchanged and remain open.
"""
p1 = replace_once(
    p1,
    "# The Limits of Compensatory Aggregation: A Formal Separation of Weak and Strong Sustainability Assessment\n\n## Abstract",
    "# The Limits of Compensatory Aggregation: A Formal Separation of Weak and Strong Sustainability Assessment\n\n" + P1_LOG + "\n## Abstract",
    "P1 version log",
)

p1 = replace_once(
    p1,
    "Aubin, J.-P., Bayen, A. M., and Saint-Pierre, P. (2011). *Viability Theory: New Directions*, 2nd ed. Birkhäuser, Boston.\n\nBoos, A. (2015).",
    "Aubin, J.-P., Bayen, A. M., and Saint-Pierre, P. (2011). *Viability Theory: New Directions*, 2nd ed. Birkhäuser, Boston.\n\nBen-Tal, A., Goryashko, A., Guslitzer, E., and Nemirovski, A. (2004). Adjustable robust solutions of uncertain linear programs. *Mathematical Programming*, 99(2), 351–376.\n\nBoos, A. (2015).",
    "P1 ref: Ben-Tal et al. 2004",
)
p1 = replace_once(
    p1,
    "Schär, S., Pohl, E., and Geldermann, J. (2025). Analysing the compensatory properties of the outranking approach PROMETHEE. *Journal of Multi-Criteria Decision Analysis*, 32, e70013.\n\nSolow, R. M. (1974).",
    "Schär, S., Pohl, E., and Geldermann, J. (2025). Analysing the compensatory properties of the outranking approach PROMETHEE. *Journal of Multi-Criteria Decision Analysis*, 32, e70013.\n\nSion, M. (1958). On general minimax theorems. *Pacific Journal of Mathematics*, 8(1), 171–176.\n\nSolow, R. M. (1974).",
    "P1 ref: Sion 1958",
)
p1 = replace_once(
    p1,
    "Usubiaga-Liaño, A. (2025). Strong sustainability in the SEEA and the wider indicator debate. *One Ecosystem*, 10, e141086.\n\nWorld Bank. (2011).",
    "Usubiaga-Liaño, A. (2025). Strong sustainability in the SEEA and the wider indicator debate. *One Ecosystem*, 10, e141086.\n\nvon Neumann, J. (1928). Zur Theorie der Gesellschaftsspiele. *Mathematische Annalen*, 100, 295–320.\n\nWorld Bank. (2011).",
    "P1 ref: von Neumann 1928",
)

# sanity: the three citations now resolve
for probe in ("Ben-Tal, A., Goryashko", "Sion, M. (1958)", "von Neumann, J. (1928)"):
    if p1.count(probe) < 1:
        sys.exit(f"FAIL [P1 refs]: {probe} missing after build.")
wr("paper1_assessment_separation_v19.md", p1)

# ============================================================================
# 3. P5: v19 -> v20 (regression repairs)
# ============================================================================
p5 = rd("paper5_sampled_governance_v19.md")

P5_LOG = """*Version log (v20).* Repairs the internal contradictions left by the v19 honest-tier correction. (1) The abstract's operator sentence is softened back to the general statement — stability does not transfer in general between the sample-and-hold map and the continuous-delay equation (matching Section 3.2's narrow transfer conditions) — instead of v19's broadened "nothing transfers". (2) The Section 3.4 comparator paragraph's stage-map sentences now attribute the 3–4 yr and 6–12 yr windows to the archived, unreproduced record (consistent with Section 3.3's corrected lead and the reconstruction comparison table) instead of asserting them as findings, and the unsupported multiplier-equation gloss on the archived record is dropped. (3) Section 4.1's finding sentence attributes the near-3–4-yr crossing to the archived record rather than presenting it as a result. No spectral record, table value, or verdict changes.
"""
p5 = replace_once(
    p5,
    "*Methodology and case study — prepared in the style of the ICES Journal of Marine Science*\n\n## Abstract",
    "*Methodology and case study — prepared in the style of the ICES Journal of Marine Science*\n\n" + P5_LOG + "\n## Abstract",
    "P5 version log",
)

p5 = replace_once(
    p5,
    "The sample-and-hold map and the continuous-delay equation are distinct operators; nothing transfers between them.",
    "The sample-and-hold map and the continuous-delay equation are distinct operators; stability does not transfer in general between them.",
    "P5 abstract non-transfer softening",
)

p5 = replace_once(
    p5,
    "On the stage-structured review map, annual review is stable at every tested response value — all declared annual-review trajectories converged at every tested response value — the anchovy-class window relocates to $T_r\\approx 3$–$4$ yr, and the sprat-class window to $T_r\\approx 6$–$12$ yr, robust to 30% multiplicative assessment error. Both statements are $\\det(M-e^{i\\theta}I)=0$ on the map to which they refer; neither transfers to the other operator.",
    "On the archived stage-structured review map, annual review is stable at every tested response value — all declared annual-review trajectories converged at every tested response value — and the archived record places the anchovy-class window at $T_r\\approx 3$–$4$ yr and the sprat-class window at $T_r\\approx 6$–$12$ yr, reporting robustness to 30% multiplicative assessment error. These are archived, unreproduced statements (Section 3.3): the generating computation is not available, and the paper's own reconstruction does not reproduce the multi-year windows; they are claims about the archived map, not results of the reconstructed object, and neither transfers to the other operator.",
    "P5 §3.4 archived attribution",
)

p5 = replace_once(
    p5,
    "exhibits an instability crossing near 3–4 yr of review under the stage-structured map (a different ecological plant, Section 2.3; the plant–operator confound is kept adjacent — the operator effect is not claimed to be isolated by this comparison; the provisional status of those windows and the labelled reconstruction's comparison with them are stated in Section 3.4)",
    "carries an archived, unreproduced instability record near 3–4 yr of review under the stage-structured map (a different ecological plant, Section 2.3; the archived windows' provisional status and the reconstruction's non-reproduction of them are stated in Sections 3.3 and 3.4; the plant–operator confound is kept adjacent — the operator effect is not claimed to be isolated by this comparison)",
    "P5 §4.1 archived attribution",
)

wr("paper5_sampled_governance_v20.md", p5)

# ============================================================================
# 4. P3: v26 -> v27 (verified micro-error cluster)
# ============================================================================
p3 = rd("paper3_material_ledgers_v26.md")

P3_LOG = """*Version log (v27).* Applies the verified micro-error cluster of the joint audit (consensus item 6 plus two arithmetic facts and one cross-check): Proposition 2's proof now cites Theorem 7 (the natural-block mass identity) rather than Theorem 3; the Section 3.3 displayed condition is renamed the barrier-safety (non-depletion) condition — it is the negation of depletion, not depletion itself; Section 2.2's list is retitled "the four geo-interface and closure primitives" (the detritus-return term does not involve the donor pool); Section 3.1 names the separated predicates (the first, second, and fourth of the four) instead of "the first three"; the Section 5.4 double use of $C$ is disambiguated in prose (the composition matrix versus the coverage vector); the Section 6.5.2 global-mean groundwater horizon is 47.5 yr ($19/0.4$), not 47.6; and the MCS-2026 Australia sentence no longer claims the main table leaves the cell blank (the pre-2026 value is retained under the quarantine dagger, pending the registered re-pin). No table value, theorem statement, or classification changes.
"""
p3 = replace_once(
    p3,
    "# Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics, and the Semantics of Depletion Horizons\n\n## Abstract",
    "# Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics, and the Semantics of Depletion Horizons\n\n" + P3_LOG + "\n## Abstract",
    "P3 version log",
)

p3 = replace_once(
    p3,
    "constant extraction at a rate exceeding regeneration is exactly mass-balanced (Theorem 3 states the identity)",
    "constant extraction at a rate exceeding regeneration is exactly mass-balanced (Theorem 7 states the identity)",
    "P3 Prop 2 theorem cite",
)

p3 = replace_once(
    p3,
    "and the depletion condition is",
    "and the barrier-safety (non-depletion) condition is",
    "P3 §3.3 condition rename",
)

p3 = replace_once(
    p3,
    "and the four primitives involving the donor are",
    "and the four geo-interface and closure primitives are",
    "P3 §2.2 list retitle",
)

p3 = replace_once(
    p3,
    "This section separates the first three and proves their relationships.",
    "This section separates the first, second, and fourth of these predicates and proves their relationships (the third, thermodynamic admissibility, is out of scope here, per Proposition 2's layering).",
    "P3 §3.1 first-three fix",
)

p3 = replace_once(
    p3,
    "with $C$ the operative extraction-law readout and $\\widehat{M}$ the declared demand-coverage matrix mapping the moiety readout $S = Cx$ into the units of the coverage vector $C(t)$",
    "with $C$ the operative extraction-law readout and $\\widehat{M}$ the declared demand-coverage matrix mapping the moiety readout $S = Cx$ — the composition matrix $C$ of Theorem 3, a different object from the coverage vector $C(t)$ despite the shared letter — into the units of that coverage vector",
    "P3 §5.4 double-C disambiguation",
)

p3 = replace_once(
    p3,
    "| global mean | $-0.4$ | $-14$ | $-33.0$ | $\\approx 47.6$ |",
    "| global mean | $-0.4$ | $-14$ | $-33.0$ | $\\approx 47.5$ |",
    "P3 47.5 arithmetic fix",
)

p3 = replace_once(
    p3,
    "MCS 2026 reports Australia's reserves as $120{,}000$ kt (JORC-compliant; the main table leaves that cell blank), so the displayed pre-2026 Australian row is quarantined pending the re-pin.",
    "MCS 2026 reports Australia's reserves as $120{,}000$ kt (JORC-compliant; the main table retains the pre-2026 value of $5{,}800{,}000$ kt under the quarantine dagger rather than leaving the cell blank), so the displayed pre-2026 Australian row is quarantined pending the re-pin.",
    "P3 blank-cell claim fix",
)

wr("paper3_material_ledgers_v27.md", p3)

# ============================================================================
# 5. P4: v25 -> v26 (verified small-error cluster)
# ============================================================================
p4 = rd("paper4_delay_dynamics_v25.md")

P4_LOG = """*Version log (v26).* Applies the verified small-error cluster of the joint audit: Corollary 6.1's proof pairs the deployment delays $(\\tau_M, \\tau_p)$ — not the filter relaxation time $\\tau_m$, which never shares an equation with the deployment delays by the paper's own notation rule; Section 1.1 points to the phase-stabilised window of Section 5.1 (where that window is defined and opened), not Section 4; and the five-regime topology's regime (iii) no longer claims the second-fold branch's unstable upper arm exists "through this window" — the registered record places it on the regime-(iv) interval $64.4 < \\tau < 150.4$ yr above the second fold, matching Section 9.3's statement. No theorem, spectral record, or table value changes.
"""
p4 = replace_once(
    p4,
    "# Delay-Induced Regime Change in Harvested Stocks: The Mobilising and Protective Channels of Institutional Feedback, and the Review Interval as Control\n\n## Abstract",
    "# Delay-Induced Regime Change in Harvested Stocks: The Mobilising and Protective Channels of Institutional Feedback, and the Review Interval as Control\n\n" + P4_LOG + "\n## Abstract",
    "P4 version log",
)

p4 = replace_once(
    p4,
    "no imaginary root exists for any $(\\tau_m, \\tau_p)$",
    "no imaginary root exists for any $(\\tau_M, \\tau_p)$",
    "P4 Cor 6.1 tau_M pair",
)

p4 = replace_once(
    p4,
    "The phase-stabilised window of Section 4 is the interval of delays inside which the lag, not the feedback, holds the loop stable.",
    "The phase-stabilised window of Section 5.1 is the interval of delays inside which the lag, not the feedback, holds the loop stable.",
    "P4 §1.1 Section 5.1 pointer",
)

p4 = replace_once(
    p4,
    "the second-fold branch records show an unstable upper arm existing mathematically through this window, without generic basin",
    "the second-fold branch records show an unstable upper arm existing mathematically only above the second fold — over regime (iv)'s $64.4 < \\tau < 150.4$ yr, as Section 9.3 registers — without generic basin",
    "P4 regime (iii) unstable-arm range",
)

wr("paper4_delay_dynamics_v26.md", p4)

# ============================================================================
# 6. P2: v7 -> v8 (first safe tranche)
# ============================================================================
p2 = rd("paper2_obstruction_calculus_v7.md")

P2_LOG = """*Version log (v8).* Applies the first safe tranche of the joint audit's internal-consistency repairs (the evaluation record's P2 consensus items 4, 6, and 8, plus two line errors): the "a fortiori" direction is corrected — the emptiness theorems are about the robust epistemic notion $\\mathrm{ERViab}$ and do not transfer to the weaker non-robust one, which contains it; the abstract's blanket "finite, checkable certificates" claim is scoped to the polyhedral and finite-fibre cases with the timing bound a conditional template, "Five mechanisms are proved" is softened to "established", "The further four" is named, and the informal "the disturbance moves after the control" is made precise; the companion assessment-separation analysis now has a reference entry; and Section 6.4's timing bound cites the drift certificate (3) — Theorem 4's — rather than (1). The deeper theorem-level repairs (Theorem 4's H2 circularity, the Theorem 1/3 closed-loop existence gap, Theorem 2's admissibility reframing, Definition 1/EViab, Corollary 6, Remark 1's policy class) are registered as follow-up edits and deliberately not applied in this tranche. No theorem statement, proof, or number is changed beyond the listed scoping and labels.
"""
p2 = replace_once(
    p2,
    "# An Obstruction Calculus for Viability under Incomplete Observation\n\n## Abstract",
    "# An Obstruction Calculus for Viability under Incomplete Observation\n\n" + P2_LOG + "\n## Abstract",
    "P2 version log",
)

p2 = replace_once(
    p2,
    "We use $\\mathrm{ERViab}$ throughout, since the disturbance classes of sustainability problems are adverse by construction; the theorems hold a fortiori for the weaker (non-robust) notion.",
    "We use $\\mathrm{ERViab}$ throughout, since the disturbance classes of sustainability problems are adverse by construction. The theorems are stated for this robust notion; their emptiness conclusions do not transfer a fortiori to the weaker non-robust one — the robust epistemic kernel is contained in the non-robust one, so an observation-based policy may exist there that no robust policy survives.",
    "P2 a-fortiori direction",
)

p2 = replace_once(
    p2,
    "We develop an obstruction calculus — a set of finite, checkable certificates that no observation-based policy exists. The certificates are sound sufficient conditions for nonviability and do not exhaust the complement of the epistemic kernel (the observation-based counterpart of the viability kernel). Five mechanisms are proved, with a sixth exhibited under a policy-class restriction.",
    "We develop an obstruction calculus — a set of obstruction certificates for the nonviability of every observation-based policy, finitely checkable in the polyhedral and finite-fibre cases and closed-form but conditional elsewhere. The certificates are sound sufficient conditions for nonviability and do not exhaust the complement of the epistemic kernel (the observation-based counterpart of the viability kernel). Five mechanisms are established — four as finite objects, the timing bound as a closed-form template — with a sixth exhibited under a policy-class restriction.",
    "P2 abstract scoping",
)

p2 = replace_once(
    p2,
    "The further four cover a finite-time exit certificate under an Isaacs-type drift condition (the disturbance moves after the control and forces violation within a computable time)",
    "The further four mechanisms cover a finite-time exit certificate under an Isaacs-type drift condition (the disturbance is chosen along the realised control — with the policy's actions already fixed — and forces violation within a computable time)",
    "P2 abstract further-four + game order",
)

p2 = replace_once(
    p2,
    "the control-space analogue of the material-substitution separation certificates reported in the companion assessment-separation analysis (under review).",
    "the control-space analogue of the material-substitution separation certificates reported in the companion assessment-separation analysis (Author et al., in review).",
    "P2 companion in-text citation",
)

# companion reference entry (alphabetical: after Aubin-Frankowska, before Béné)
p2 = replace_once(
    p2,
    "Aubin, J.-P., Frankowska, H.: Set-Valued Analysis. Birkhäuser, Boston (1990)\n\nBéné, C., Doyen, L., Gabay, D.: A viability analysis for a bio-economic model. Ecol. Econ. **36**, 385–396 (2001)",
    "Aubin, J.-P., Frankowska, H.: Set-Valued Analysis. Birkhäuser, Boston (1990)\n\nAuthor, A., et al., in review. A formal separation of weak and strong sustainability assessment: the limits of compensatory aggregation. Companion assessment-separation analysis.\n\nBéné, C., Doyen, L., Gabay, D.: A viability analysis for a bio-economic model. Ecol. Econ. **36**, 385–396 (2001)",
    "P2 companion reference entry",
)

p2 = replace_once(
    p2,
    "The bound is computable from the drift certificate (1), which is the same certificate a robustness analysis computes anyway.",
    "The bound is computable from the drift certificate (3), which is the same certificate a robustness analysis computes anyway.",
    "P2 §6.4 drift certificate number",
)

wr("paper2_obstruction_calculus_v8.md", p2)

print("\nAll six wave-2 versions built.")
