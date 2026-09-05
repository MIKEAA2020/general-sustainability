#!/usr/bin/env python3
"""
apply_batch7_wave4_e1.py — fail-loud build of paperE1_cod_forecast_ladder_v11.md from v10.

Implements the wave-4 E1 items (owner-directed, "cite, don't drop"):
  R1  companion citations (Edwards forecast-evaluation; governance; interval-verified
      linear template) — in-text citations + three reference entries.  [both, consensus 7]
  R2  the freeze claim weakened at all three sites (abstract, §1, §4 lead) to
      "coded before the first scoring pass and applied unchanged", matching §4's
      no-dated-protocol disclosure.  [both, consensus 6]
  R3  Definition 2.4 completed (deciding score = the frozen RMSE pair h=1 & h=5; declared
      H1 comparators M1-for-M2 / M3-for-M4 with M1b the reported alternative; 5% tie band)
      + the post-freeze DM / Kunsch-bootstrap layer as §3.5 + Table 9 + Diebold(1995),
      Kunsch(1989) references + Data-availability registration.  [both, A8]
  R4  the 1898-kt Spec-B collapse error enters the abstract.  [grok]
  R5  the log-score floor stated (eps_log = 1e-3 kt, distinct from the Def-2.1 process
      noise) with per-origin floor-hit counts.  [claude]
  R6  "No module M2–M4 is retained" → "No structural model — M1 through M4".  [claude]
  R7  Definition 4.2 moved to Methods as Definition 2.5 with the machine layer defined;
      Funding section added (submission placeholder, mirroring the CRediT pattern);
      claude's abstract note "115–206 mixes Table 4/5" → "across both catch treatments".

Non-destructive: Tables 1–8 byte-identical; Table 9 is a new post-freeze layer; no frozen
verdict, score, kernel, or table value changes.  Every edit asserts its anchor appears
exactly once; every mechanical check fails loudly.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "arena agent 1", "paper rewrites",
                   "paperE1_cod_forecast_ladder_v10.md")
DST = os.path.join(HERE, "..", "arena agent 1", "paper rewrites",
                   "paperE1_cod_forecast_ladder_v11.md")


def sub1(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise SystemExit(f"FAIL [anchor {label}]: expected exactly 1 occurrence, found {n}")
    return text.replace(old, new)


def main():
    t = open(SRC, encoding="utf-8").read()

    # ---------------- version log ----------------
    v10_log = t.split("\n", 5)  # header lines
    old_log_start = "*Version log (v10).*"
    idx = t.find(old_log_start)
    if idx != t.find("\n*Version log") + 1 or t.count(old_log_start) != 1:
        raise SystemExit("FAIL: v10 version log anchor")
    log_end = t.find("\n\n## Highlights", idx)
    if log_end == -1:
        raise SystemExit("FAIL: version log terminator")
    new_log = (
        "*Version log (v11).* Implements the wave-4 items of the joint-audit evaluation's E1 "
        "remaining-points list (R1–R7), owner-directed as cite-not-drop. (R1) The three companion "
        "studies now carry in-text citations and reference entries: the Edwards Aquifer "
        "forecast-evaluation study, the governance study, and the interval-verified linear template "
        "(in preparation). (R2) The freeze claim 'fixed in the analysis scripts before execution' is "
        "weakened at all three sites (abstract, Section 1, Section 4's lead) to 'coded before the first "
        "scoring pass and applied unchanged', with the later passes declared rather than preregistered "
        "— matching the freeze-discipline paragraph's own disclosure. (R3, audit item A8) Definition 2.4 "
        "is completed: the deciding score is the frozen specification's rolling-origin RMSE pair at "
        "$h=1$ and $h=5$ (clause H3); the declared (H1) comparators for the non-nested rungs are M1 for "
        "M2 and M3 for M4, with M1b the reported alternative; a 5% tie band is declared; and a "
        "post-freeze Diebold–Mariano + Kunsch moving-block-bootstrap layer (new Section 3.5, Table 9; "
        "registered script campaign_e1_dm_uncertainty.py, seed 0, 20,000 replications) attaches "
        "uncertainty to every load-bearing margin — on Specification A all non-retention margins are "
        "within noise, on Specification B every margin against persistence separates. (R4) The 1898-kt "
        "Specification-B collapse error enters the abstract. (R5) The log-score floor is stated "
        "($\\varepsilon_{\\mathrm{log}} = 10^{-3}$ kt, distinct from the Definition-2.1 process noise) "
        "with the per-origin floor-hit counts. (R6) 'No module M2–M4 is retained' becomes 'no structural "
        "model'. (R7) Definition 4.2 moves to Methods as Definition 2.5 with the machine layer defined, "
        "and a Funding section is added; the abstract's mixed-treatment range now says 'across both "
        "catch treatments'. No frozen verdict, score, or table value changes: Tables 1–8 are "
        "byte-identical, Table 9 is the new post-freeze layer, and the abstract is 300 words."
    )
    t = t[:idx] + new_log + t[log_end:]

    # ---------------- abstract ----------------
    t = sub1(t,
        "This evaluation follows a stated retention rule (a model is kept only if it reduces primary "
        "RMSE relative to the next-simpler model and relative to persistence), fixed in the analysis "
        "scripts before execution. Early-warning and intervention criteria are declared but not "
        "invoked. The test is applied",
        "This evaluation follows a stated retention rule (a model is kept only if it reduces primary "
        "RMSE relative to the next-simpler model and relative to persistence), coded before the first "
        "scoring pass and applied unchanged; later passes were declared, not preregistered (Section 4). "
        "The test is applied",
        "abstract-p1")

    t = sub1(t,
        "The one-year rolling RMSE is 98 kt for persistence versus 115–206 kt for the structural "
        "ladder, and the five-year rolling RMSE is 265 kt versus 289–488 kt. The collapse window is "
        "missed by every model (694–819 kt structural; 670 and 688 kt naive). A constant-productivity "
        "surplus model with a 1992 catch drop cannot produce the crash. Neither an AR residual nor a "
        "one-year delay reduces that error (819 kt in each case), and on rolling origins the delay "
        "raises one-year RMSE (196 versus 135 kt).",
        "The one-year rolling RMSE is 98 kt for persistence versus 115–206 kt for the structural "
        "ladder across both catch treatments, and the five-year rolling RMSE is 265 kt versus 289–488 "
        "kt. The collapse window is missed by every model (694–819 kt structural; 670 and 688 kt "
        "naive), and on the extended 1954–2024 specification official landings drive the stock-flow "
        "module's collapse-window error to 1898 kt. A constant-productivity model with a 1992 catch "
        "drop cannot produce the crash. Neither an AR residual nor a one-year delay reduces that "
        "error (819 kt each), and on rolling origins the delay raises one-year RMSE (196 versus "
        "135 kt).",
        "abstract-p2")

    t = sub1(t,
        "does not beat persistence on the primary score, and modules not identified on the training "
        "window increase error. The same rule applied to a second, unpooled specification "
        "(xteNCAM, 1954–2024, LRP 276 kt) gives the same non-retention outcome (origin-matched "
        "persistence 84 kt versus M1's 120 kt at $h=1$; the mixed-origin reading is 88 kt). The "
        "machine layer verifies the recorded arithmetic and its byte-level reproducibility, not the "
        "class-level incompatibility. The two series are not mixed.",
        "does not beat persistence on the primary score, and unidentified modules increase error. "
        "The same rule applied to a second, unpooled specification (xteNCAM, 1954–2024, LRP 276 kt) "
        "gives the same non-retention outcome (origin-matched persistence 84 kt versus M1's 120 kt "
        "at $h=1$). The machine layer verifies the recorded arithmetic and its byte-level "
        "reproducibility, not the class-level incompatibility.",
        "abstract-p3")

    # ---------------- §1: R2 + R1 (Edwards companion) ----------------
    t = sub1(t,
        "This evaluation follows a stated retention rule, fixed in the analysis scripts before "
        "execution: additional model structure is retained only when",
        "This evaluation follows a stated retention rule, coded before the first scoring pass and "
        "applied unchanged (the pass-level freeze record is Section 4): additional model structure "
        "is retained only when",
        "s1-freeze")

    t = sub1(t,
        "applies the same scored design to a groundwater system (the Edwards Aquifer, Texas). The "
        "two systems' series are never pooled",
        "applies the same scored design to a groundwater system (the Edwards Aquifer, Texas; Author "
        "et al., in review). The two systems' series are never pooled",
        "s1-edwards")

    t = sub1(t,
        "in which the factor is replaced by $1$ (a companion governance study under separate review "
        "makes the same point).",
        "in which the factor is replaced by $1$ (a companion governance study under separate review "
        "makes the same point; Author et al., in review).",
        "lemma22-governance")

    # ---------------- Definition 2.4 completion (R3) ----------------
    t = sub1(t,
        "**Definition 2.4 (Retention rule).** *A module $M$ on the ladder of Definition 2.3 is "
        "retained only if both of the following hold on the rolling-origin primary RMSE score:*\n\n"
        "- *(H1) $M$ reduces primary RMSE relative to the next-simpler model on the ladder;*\n"
        "- *(H2) $M$ reduces primary RMSE relative to last-value persistence.*\n\n"
        "*Retention is decided separately on each specification. A module failing either (H1) or "
        "(H2) is not retained.*",
        "**Definition 2.4 (Retention rule).** *A module $M$ on the ladder of Definition 2.3 is "
        "retained only if all of the following hold on the rolling-origin primary RMSE score:*\n\n"
        "- *(H1) $M$ reduces primary RMSE relative to its declared comparator — the next-simpler "
        "rung for the nested steps (M1b against M1, M3 against M2); for the two rungs that are not "
        "strict nestings, M1 for M2 (the autonomous constant-catch map whose catch treatment M2 "
        "changes) and M3 for M4 (the module the delay acts on). M1b is reported as the alternative "
        "comparator for M2 and never decides retention;*\n"
        "- *(H2) $M$ reduces primary RMSE relative to last-value persistence;*\n"
        "- *(H3) each required reduction holds at both horizons $h=1$ and $h=5$ — the frozen "
        "specification's primary score is the rolling-origin RMSE pair — and exceeds a tie band of "
        "5% of the comparator's score; improvements inside the band are ties and do not retain.*\n\n"
        "*Retention is decided separately on each specification. A module failing any of "
        "(H1)–(H3) is not retained. Two disclosures complete the rule. First, it is a point-rule "
        "ranking under a pre-set score, not a test of equal predictive ability; the post-freeze "
        "uncertainty layer of Section 3.5 attaches Diebold–Mariano and moving-block-bootstrap "
        "intervals to its margins and changes no verdict. Second, the tie band and the comparator "
        "declarations are completions recorded at this revision, after the scores of Section 3 were "
        "computed: no recorded verdict depends on them — the smallest structural deficit against "
        "persistence (M1b's on Specification A at $h=1$) is 17%, and no (H1) comparison in Tables "
        "3–8 reverses under either comparator reading.*\n\n"
        "**Definition 2.5 (Negative certificate).** *A negative certificate is a machine-verified "
        "finding of non-retention of a model class under the stated retention rule (Definition 2.4): "
        "the scored one-step least-squares implementation of the class does not satisfy (H1)–(H3) on "
        "the rolling-origin primary RMSE score on the declared series. A negative certificate is "
        "weaker than a statistical null result; it is scoped to the estimator, the ladder, and the "
        "series on which it is issued.*\n\n"
        "The machine layer that the certificate refers to is the deterministic scoring stack — the "
        "scripts registered in the Data availability record together with their pinned output "
        "checksums. What that layer verifies is the recorded arithmetic and its byte-level "
        "reproducibility. The class-level incompatibility (Proposition 4.1) is a mathematical "
        "statement proved in Section 4, not an object the machine layer verifies.",
        "def2.4")

    # ---------------- §3.2: R6 ----------------
    t = sub1(t,
        "No module M2–M4 is retained on Specification A. Persistence is the lowest-RMSE forecast.",
        "No structural model — M1 through M4 — is retained on Specification A. Persistence is the "
        "lowest-RMSE forecast.",
        "r6")

    # ---------------- §3.5 (new; R3) ----------------
    table9 = """### 3.5 Uncertainty on the retention margins (post-freeze layer)

A post-freeze uncertainty layer attaches Diebold–Mariano tests (Diebold and Mariano, 1995; unweighted HAC truncation at lag $h-1$) and moving-block bootstrap intervals (Künsch, 1989; block length $\\max(h,3)$, 20,000 replications, seeded) to the retention margins of Definition 2.4. It is computed from the archived per-origin forecast files: on Specification B the xteNCAM rolling file; on Specification A the archived per-origin file is the annual-landings pass of Section 3.2 (the coarse-regime pass's per-origin rows are not archived — its summary is — and the verdicts coincide under both treatments). The persistence baseline is not archived per-origin; it is recomputed on the identical origin sets from the registered series, and the recomputation reproduces the recorded origin-matched baselines (98 and 265 kt on Specification A; 84 and 300 kt on the matched Specification B origins) — the script fails loudly otherwise. The layer attaches uncertainty to margins the point rule has already ranked; it changes no frozen verdict, score, or table value.

**Table 9.** Uncertainty on the retention margins (post-freeze layer; Diebold–Mariano with HAC lag $h-1$; Künsch moving-block bootstrap, block length $\\max(h,3)$, 20,000 replications, seeded). Gaps are module minus comparator, in kt; positive gaps mean the module is worse.

| Spec | $h$ | Module | Comparator | $n$ | RMSE module | RMSE comp. | Gap (kt) | DM $z$ | 95% CI (kt) | $p$ |
|---|---:|---|---|---:|---:|---:|---:|---:|---|---:|
| A | 1 | M1 | persist | 25 | 120.5 | 98.0 | +22.5 | 1.15 | [−13.3, +50.5] | 0.192 |
| A | 1 | M1b | persist | 25 | 114.8 | 98.0 | +16.7 | 0.98 | [−19.3, +59.2] | 0.376 |
| A | 1 | M2 | persist | 25 | 160.4 | 98.0 | +62.4 | 1.30 | [−11.9, +107.0] | 0.445 |
| A | 1 | M3 | persist | 25 | 153.6 | 98.0 | +55.6 | 1.02 | [−18.0, +91.6] | 0.927 |
| A | 1 | M4 | persist | 25 | 206.3 | 98.0 | +108.2 | 1.51 | [−8.2, +192.7] | 0.338 |
| A | 1 | M2 | M1 | 25 | 160.4 | 120.5 | +39.9 | 1.13 | [−59.1, +88.5] | 0.687 |
| A | 1 | M4 | M3 | 25 | 206.3 | 153.6 | +52.7 | 0.99 | [+4.7, +144.7] | <0.001 |
| A | 5 | M1 | persist | 21 | 288.7 | 264.7 | +24.0 | 1.84 | [−43.1, +56.4] | 0.279 |
| A | 5 | M1b | persist | 21 | 288.6 | 264.7 | +23.9 | 1.84 | [−43.1, +56.4] | 0.284 |
| A | 5 | M2 | persist | 21 | 393.8 | 264.7 | +129.1 | 1.10 | [−25.0, +215.9] | 0.576 |
| A | 5 | M3 | persist | 21 | 351.5 | 264.7 | +86.8 | 1.10 | [−7.3, +131.9] | 0.266 |
| A | 5 | M4 | persist | 21 | 486.4 | 264.7 | +221.7 | 1.14 | [−27.0, +412.8] | 0.759 |
| A | 5 | M2 | M1 | 21 | 393.8 | 288.7 | +105.1 | 0.97 | [−78.8, +230.1] | 0.807 |
| A | 5 | M4 | M3 | 21 | 486.4 | 351.5 | +134.9 | 1.15 | [−28.4, +292.4] | 0.902 |
| B | 1 | M1 | persist | 59 | 119.5 | 84.4 | +35.0 | 2.81 | [+2.7, +70.8] | 0.032 |
| B | 1 | M1b | persist | 59 | 151.6 | 84.4 | +67.2 | 3.60 | [+18.3, +117.7] | 0.009 |
| B | 1 | M2 | persist | 59 | 166.0 | 84.4 | +81.6 | 3.22 | [+36.4, +122.8] | <0.001 |
| B | 1 | M3 | persist | 59 | 126.7 | 84.4 | +42.3 | 1.85 | [+1.0, +92.5] | 0.042 |
| B | 1 | M4 | persist | 59 | 205.7 | 84.4 | +121.3 | 3.20 | [+53.7, +193.0] | <0.001 |
| B | 1 | M2 | M1 | 59 | 166.0 | 119.5 | +46.6 | 1.78 | [−20.5, +104.5] | 0.170 |
| B | 1 | M4 | M3 | 59 | 205.7 | 126.7 | +79.0 | 3.07 | [+35.6, +116.4] | <0.001 |
| B | 5 | M1 | persist | 55 | 431.9 | 300.0 | +131.9 | 2.06 | [+33.2, +218.6] | 0.008 |
| B | 5 | M1b | persist | 55 | 445.5 | 300.0 | +145.5 | 1.80 | [+18.2, +250.9] | 0.023 |
| B | 5 | M2 | persist | 55 | 1058.9 | 300.0 | +758.9 | 2.15 | [+363.6, +1038.5] | <0.001 |
| B | 5 | M3 | persist | 55 | 930.1 | 300.0 | +630.2 | 2.39 | [+352.8, +845.6] | <0.001 |
| B | 5 | M4 | persist | 55 | 1030.7 | 300.0 | +730.8 | 2.35 | [+407.3, +978.3] | <0.001 |
| B | 5 | M2 | M1 | 55 | 1058.9 | 431.9 | +627.0 | 1.97 | [+195.7, +929.7] | 0.004 |
| B | 5 | M4 | M3 | 55 | 1030.7 | 930.1 | +100.6 | 1.88 | [+20.2, +177.4] | 0.007 |

Readings. On Specification A no non-retention margin separates from zero: at $h=1$ the deficits against persistence (16.7–108.2 kt on $n=25$) carry DM $z$ from 0.98 to 1.51 with bootstrap $p$ from 0.19 to 0.93, and at $h=5$ (23.9–221.7 kt on $n=21$) $z$ from 1.10 to 1.84 with $p$ from 0.27 to 0.76 — the heavy-tailed collapse-window losses dominate the bootstrap variance at this sample size, and the negative certificate on Specification A is a point-rule ranking whose margins are within noise, the reading Section 4 already records ("they suffice to rank models and do not suffice to certify a small skill difference"). On Specification B the non-retention separates: every module's deficit against persistence is decisive at $h=1$ ($p$ from 0.042 to below 0.001 on $n=59$) and at $h=5$ ($p$ at most 0.023 on $n=55$). The declared (H1) comparators behave asymmetrically: M2's deficit against M1 is within noise at $h=1$ on both specifications and at $h=5$ on Specification A, separating only on Specification B at $h=5$ ($p=0.004$), while M4's delay cost against M3 separates at $h=1$ on both specifications ($p$ below 0.001) and at $h=5$ on Specification B ($p=0.007$) but not on Specification A ($p=0.90$). The alternative comparator reading (M2 against M1b) is within noise at $h=1$ on both specifications and at $h=5$ on Specification A, separating on Specification B at $h=5$ ($p=0.005$): the comparator declaration of Definition 2.4 is immaterial to every recorded verdict, as the completion records. The layer is produced by the registered script `campaign_e1_dm_uncertainty.py` (batch-7 audit directory of the repository), deterministic under seed 0, with its output archived alongside it (`results/e1_dm_uncertainty.csv`).

## 4. Discussion"""

    t = sub1(t, "## 4. Discussion", table9, "s35-insert")
    # undo: the marker above replaced the heading; restore heading context check below

    # ---------------- §4: R5 floor + R2 §4 lead + companion cites ----------------
    t = sub1(t,
        "The log-RMSE scores of Table 4 carry an undeclared-floor caveat: structural trajectories "
        "that absorb at zero make $\\log 0$ undefined, the reported values use "
        "$\\log\\max(\\hat S, \\varepsilon)$ with the $\\varepsilon$-floor part of the registered "
        "scoring configuration, and the raw-RMSE column is the retention score.",
        "The log-RMSE scores of Table 4 carry a floor caveat: structural trajectories absorb at the "
        "numerical floor $\\varepsilon_{\\mathrm{log}} = 10^{-3}$ kt rather than at zero (the "
        "trajectory code clips the state to $[\\varepsilon_{\\mathrm{log}}, 10^{6}]$ kt), and the "
        "reported values use $\\log\\max(\\hat S, \\varepsilon_{\\mathrm{log}})$; "
        "$\\varepsilon_{\\mathrm{log}}$ is part of the registered scoring configuration and is "
        "distinct from the process noise $\\varepsilon_t$ of Definition 2.1. The floor binds often: "
        "on the archived per-origin records (the annual-landings rolling pass of Section 3.2) 15 of "
        "25 M1 and 17 of 25 M1b one-year origins and 19 of 21 five-year origins for both modules "
        "absorb at the floor (M3 at 3; M2 and M4 at most once per horizon); on Specification B, 22 "
        "of 59 and 24 of 59 at $h=1$ and 36 of 55 and 46 of 55 at $h=5$ (M2, M3, and M4 between 0 "
        "and 11). The raw-RMSE column is the retention score.",
        "r5-floor")

    t = sub1(t,
        "**Freeze discipline.** The evaluation windows and scoring rules were fixed in the analysis "
        "scripts before execution; the design is a fixed computational protocol rather than a "
        "prospective clinical-style registration.",
        "**Freeze discipline.** The evaluation windows and scoring rules were coded before the first "
        "scoring pass and applied unchanged; the design is a fixed computational protocol rather "
        "than a prospective clinical-style registration.",
        "s4-freeze")

    t = sub1(t,
        "Unlike the companion evaluation on the Edwards Aquifer (under separate review), whose "
        "protocol files are dated and locked before scoring",
        "Unlike the companion evaluation on the Edwards Aquifer (Author et al., in review), whose "
        "protocol files are dated and locked before scoring",
        "s4-edwards")

    t = sub1(t,
        "The scores do not transfer to an interval-verified linear template (a companion "
        "methodological study, under review; that template is a linear $(S,K)$ construction, not "
        "this SSB series),",
        "The scores do not transfer to an interval-verified linear template (a companion "
        "methodological study, Author et al., in preparation; that template is a linear $(S,K)$ "
        "construction, not this SSB series),",
        "s4-template")

    # ---------------- remove Definition 4.2 (moved to Methods as 2.5) ----------------
    t = sub1(t,
        "\n\n**Definition 4.2 (Negative certificate).** *A negative certificate is a machine-verified "
        "finding of non-retention of a model class under the stated retention rule (Definition 2.4): "
        "the scored one-step least-squares implementation of the class does not satisfy (H1) or (H2) "
        "on the rolling-origin primary RMSE score on the declared series. A negative certificate is "
        "weaker than a statistical null result; it is scoped to the estimator, the ladder, and the "
        "series on which it is issued.*\n",
        "\n",
        "def4.2-remove")

    # ---------------- Funding (R7) ----------------
    t = sub1(t,
        "## CRediT authorship contribution statement\n\n[To be completed at submission.]",
        "## CRediT authorship contribution statement\n\n[To be completed at submission.]\n\n"
        "## Funding\n\n[To be completed at submission.]",
        "funding")

    # ---------------- Data availability registration ----------------
    t = sub1(t,
        "The two assessment specifications (NCAM and xteNCAM) were analysed throughout as separate, "
        "unpooled series.",
        "The two assessment specifications (NCAM and xteNCAM) were analysed throughout as separate, "
        "unpooled series. The post-freeze uncertainty layer (Section 3.5) is produced by "
        "`batch 7 (audits of agent arena 1 paper rewrites)/campaign_e1_dm_uncertainty.py` — seeded "
        "and deterministic, with Diebold–Mariano (HAC) and Kunsch moving-block bootstrap on the "
        "archived per-origin forecast files — and its output is archived alongside it as "
        "`batch 7 (audits of agent arena 1 paper rewrites)/results/e1_dm_uncertainty.csv`; the "
        "persistence baseline is recomputed there on the identical origin sets from the registered "
        "series and asserted against the recorded origin-matched values.",
        "data-avail")

    # ---------------- References ----------------
    t = sub1(t,
        "Cadigan, N.G., 2016. A state-space stock assessment model for northern cod, including "
        "under-reported catches and variable natural mortality rates. Can. J. Fish. Aquat. Sci. 73, "
        "296–308.",
        "Author, A., et al., in review. Does a one-pool water-balance model improve forecasts of "
        "Edwards Aquifer head? A scored test at J-17. Companion forecast-evaluation study (Edwards "
        "Aquifer, Texas).\n\nAuthor, B., et al., in review. Periodic review as sampled governance: "
        "sample-and-hold dynamics of assessment-driven effort control. Companion governance "
        "study.\n\nAuthor, C., et al., in preparation. Interval-verified bounds in linear "
        "management templates. Companion methodological study.\n\nCadigan, N.G., 2016. A "
        "state-space stock assessment model for northern cod, including under-reported catches and "
        "variable natural mortality rates. Can. J. Fish. Aquat. Sci. 73, 296–308.\n\nDiebold, "
        "F.X., Mariano, R.S., 1995. Comparing predictive accuracy. J. Bus. Econ. Stat. 13, 253–263. "
        "https://doi.org/10.1080/07350015.1995.10524599",
        "refs-1")

    t = sub1(t,
        "Murphy, H.M., Adamack, A.T., Lewis, R.S., Bourne, C.M., 2025. Assessment of capelin in "
        "NAFO Divisions 2J+3KL to 2023.",
        "Künsch, H.R., 1989. The jackknife and the bootstrap for general stationary observations. "
        "Ann. Stat. 17, 1217–1241. https://doi.org/10.1214/aos/1176347265\n\nMurphy, H.M., "
        "Adamack, A.T., Lewis, R.S., Bourne, C.M., 2025. Assessment of capelin in NAFO Divisions "
        "2J+3KL to 2023.",
        "refs-2")

    # ---------------- mechanical checks ----------------
    v11 = t
    m = re.search(r"## Abstract\n(.*?)\n\n\*\*Keywords", v11, re.S)
    if not m:
        raise SystemExit("FAIL: abstract not found in v11")
    wc = len(m.group(1).split())
    if not (290 <= wc <= 300):
        raise SystemExit(f"FAIL: abstract word count {wc} outside [290, 300]")
    if "1898 kt" not in m.group(1):
        raise SystemExit("FAIL: R4 1898-kt sentence missing from abstract")
    # R2: the old claim may survive only as a quotation inside the version log line
    body_lines = [l for l in v11.splitlines() if not l.startswith("*Version log (v11).*")]
    body = "\n".join(body_lines)
    if "fixed in the analysis scripts before execution" in body:
        raise SystemExit("FAIL: R2 old freeze claim still present outside the version log")
    if "Definition 4.2" in body:
        raise SystemExit("FAIL: Definition 4.2 still referenced outside the version log")
    if "No module M2–M4 is retained" in body:
        raise SystemExit("FAIL: R6 old phrase still present outside the version log")
    for needle, label in [
        ("coded before the first scoring pass", "R2 wording"),
        ("Author, A., et al., in review", "R1 ref A"),
        ("Author, B., et al., in review", "R1 ref B"),
        ("Author, C., et al., in preparation", "R1 ref C"),
        ("Author et al., in review", "R1 in-text"),
        ("Diebold, F.X., Mariano, R.S., 1995", "DM ref"),
        ("Künsch, H.R., 1989", "Kunsch ref"),
        ("### 3.5 Uncertainty on the retention margins (post-freeze layer)", "S3.5"),
        ("**Table 9.**", "Table 9 caption"),
        ("campaign_e1_dm_uncertainty.py", "DM script registered"),
        ("**Definition 2.5 (Negative certificate).**", "Def 2.5"),
        ("(H3)", "H3 clause"),
        ("No structural model — M1 through M4 — is retained", "R6 phrase"),
        ("\\varepsilon_{\\mathrm{log}} = 10^{-3}", "R5 floor value"),
        ("15 of 25 M1 and 17 of 25 M1b", "R5 counts A"),
        ("## Funding", "R7 funding"),
        ("across both catch treatments", "abstract catch-treatments"),
    ]:
        if needle not in v11:
            raise SystemExit(f"FAIL: expected string missing [{label}]: {needle!r}")
    # Table 9 rows
    t9 = [l for l in v11.splitlines() if l.startswith("| A |") or l.startswith("| B |")]
    t0 = [l for l in open(SRC, encoding="utf-8").read().splitlines()
          if l.startswith("| A |") or l.startswith("| B |")]
    if len(t9) != len(t0) + 28:
        raise SystemExit(f"FAIL: Table 9 adds {len(t9) - len(t0)} data rows, expected 28")
    # Tables 1-8 byte-identical
    old_tables = [l for l in open(SRC, encoding="utf-8").read().splitlines()
                  if l.startswith("|")]
    new_tables = [l for l in v11.splitlines() if l.startswith("|")]
    if len(new_tables) != len(old_tables) + 30:
        raise SystemExit(f"FAIL: table-line counts {len(old_tables)} -> {len(new_tables)} "
                         f"(expected +30)")
    # splice out the 30 new Table-9 lines (header + separator + 28 rows)
    hdr = "| Spec | $h$ | Module | Comparator | $n$ | RMSE module | RMSE comp. | Gap (kt) | DM $z$ | 95% CI (kt) | $p$ |"
    i = new_tables.index(hdr)
    spliced = new_tables[:i] + new_tables[i + 30:]
    if spliced != old_tables:
        raise SystemExit("FAIL: Tables 1-8 are not byte-identical after the build")
    # Highlights unchanged and <= 85 chars
    hl = re.search(r"## Highlights\n(.*?)\n\n## Abstract", v11, re.S).group(1)
    for line in hl.strip().splitlines():
        if len(line.lstrip("- ")) > 85:
            raise SystemExit(f"FAIL: Highlights line over 85 chars: {line!r}")

    open(DST, "w", encoding="utf-8").write(v11)
    print(f"OK: wrote {DST}")
    print(f"    abstract words: {wc}; table rows: {len(old_tables)} -> {len(new_tables)}; "
          f"lines: {len(v11.splitlines())}")


if __name__ == "__main__":
    main()
