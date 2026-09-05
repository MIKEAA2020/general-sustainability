#!/usr/bin/env python3
"""
apply_batch7_wave4_p5.py — fail-loud build of paper5_sampled_governance_v21.md from v20.

Implements the wave-4 P5 items (owner-directed, "cite, don't drop" / non-destructive):
  R23 [both — consensus 3, partial] q-sensitivity surfacing:
      one sentence in the abstract + two sentences in Section 4.1 (q = 0.001 vs q = 0.1
      flips every verdict of the reconstruction), and Section 3.4's Reading reworded to
      claude's blunter framing (the archived-vs-reconstructed comparison is uninformative
      at the undeclared catchability scale rather than a non-reproduction).
  R24 [claude E10 + grok's notation notes] Notation unification:
      monodromy M -> D P_{T_r}(X*); Lemma 2.2's production maximum M -> f_max (M is
      natural mortality only); S's two scopes fixed and fenced; delta (softplus shift)
      defined at its equation and distinguished from delta_0 (k = 10 noted there); g, C_E,
      C_Z, and the "four-state prediction" defined at their use sites; tau_- defined
      inline; channel terminology unified to "extractive" (audits' preference; recorded).
  Middle-layer docket:
      Box 1  — the claims ledger (claim -> evidential status -> record pointer), 26 rows,
               placed after the keywords (grok: "a 'claims at their exact status' box
               after the abstract"; claude: consolidated claim-status).
      Appendix A — the registration meta-text consolidated (statements kept verbatim as
               bullets), with a declared/registered/pre-registered vocabulary convention
               and ONE main-text pointer (Section 2.2); carries Table 3.
      Table 3 — the parameter table (claude A6): the parameter values the manuscript
               itself prints for the logistic core and the stage reconstruction; entries
               the text never prints are marked as such; NO new computations.
      Spectral-margins paragraph (Section 3.4) — the recorded margins of the rho = 1.00035
               annual-review verdict (claude A2 / grok: "needs its computational archive
               or a short appendix"), with the sensitivity caveat; lambda and theta are
               recorded as not-printed archive items.
      Undelayed-limit reconciliation (Section 3.4) — the A1 tension across Sections 2.3,
               3.2, 3.4 stated explicitly as an open record (lambda not printed).
      A9 — the slow-stock "agreement" reclassified as a disagreement between the
               reconstruction's own records; the 30%-error cells as noise-driven variance
               at a non-noise-adjusted threshold.
      A4 — the Section 2.4 screen bands' descent from the archived stage-map peaks
               acknowledged.
      4.6 relocation — the distributive-constraints material moved out of the Discussion
               to Appendix B (verbatim; the audits say Supplementary, which the repo rule
               forbids editing, so the relocation target is this file's appendix), with a
               brief "what the case does not measure" paragraph left in Section 4.6.
      "42 vs several dozen" — the abstract now says 42 (both audits: "use 42 throughout").
      Companion citation — the delay-dynamics companion cited in text (4 sites) and in
               the References (Author, D., et al., in review; fresh letter; real title).
      Housekeeping — the never-cited DFO (2022) entry cited at Section 2.7's
               assessment-record sentence.
      Rose (2026) and the frozen 2026-09-01 plan date: resolved-by-clock, NOT edited.

Non-destructive: Table 1, Table 2, the Section 3.4 comparison table, and the Section 4.6
mismatch table are byte-identical (the last relocated verbatim); no frozen verdict, score,
spectral record, crossing, or table value changes; no new computations (the margins
paragraph restates printed values only). Every edit asserts its anchor appears exactly
once; every mechanical check fails loudly.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "arena agent 1", "paper rewrites",
                   "paper5_sampled_governance_v20.md")
DST = os.path.join(HERE, "..", "arena agent 1", "paper rewrites",
                   "paper5_sampled_governance_v21.md")


def sub1(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise SystemExit(f"FAIL [anchor {label}]: expected exactly 1 occurrence, found {n}")
    return text.replace(old, new)


def main():
    t = open(SRC, encoding="utf-8").read()
    v20 = t

    # ---------------- version log ----------------
    old_log = "*Version log (v20).*"
    if t.count(old_log) != 1:
        raise SystemExit("FAIL: v20 version log anchor")
    idx = t.find(old_log)
    log_end = t.find("\n\n## Abstract", idx)
    if log_end == -1:
        raise SystemExit("FAIL: version log terminator")
    new_log = (
        "*Version log (v21).* Implements the wave-4 items of the joint-audit evaluation's P5 "
        "remaining-points list (R23, R24, and the middle-layer docket), owner-directed and "
        "non-destructive. (R23) The stage-map catchability sensitivity now surfaces in the "
        "abstract and in Section 4.1 — at $q = 0.1$, against the imported $q = 0.001$, every "
        "annual-review verdict of the reconstruction flips — and Section 3.4's Reading is "
        "reworded to the audits' blunter framing: the archived-versus-reconstructed comparison "
        "is uninformative at that undeclared scale rather than a non-reproduction. (R24, "
        "notation) The Section 2.3 multiplier condition is written on the Jacobian "
        "$D\\mathcal P_{T_r}(X^*)$ (the monodromy sense of $M$ is retired); Lemma 2.2's "
        "production maximum is written $f_{\\max}$, leaving $M$ to natural mortality alone; "
        "the two scopes of $S$ (surplus production in the control sections, spawning stock "
        "biomass in the cod case) are fixed in the notation paragraph and never share an "
        "equation; the softplus shift $\\delta$ is defined at its equation and distinguished "
        "from the effort-law gain $\\delta_0$, with the sharpness value $k = 10$ noted there; "
        "$g$ (Section 3.3), $C_E$ and $C_Z$ (Section 3.4), and the \"four-state prediction\" "
        "(Section 3.7) are defined at their use sites; and the channel terminology is unified "
        "to \"extractive\" — the term of Sections 1–2 — with \"mobilising\" retired from this "
        "manuscript's body (the companion's title keeps its own word). (Middle layer) Box 1 is "
        "the claims ledger (claim, status, pointer) placed after the keywords; Appendix A "
        "consolidates the registration meta-text with a declared/registered/pre-registered "
        "vocabulary convention and one main-text pointer, and carries Table 3, the parameter "
        "values this manuscript itself prints for both computed cores (nothing newly computed; "
        "unprinted entries marked); a spectral-margins paragraph in Section 3.4 reports the "
        "recorded margins of the $\\rho = 1.00035$ annual-review verdict with the sensitivity "
        "caveat (the angle $\\theta$ and the continuous eigenvalue $\\lambda$ are not printed "
        "and stay with the computational archive); the undelayed-limit tension across Sections "
        "2.3, 3.2, and 3.4 is reconciled explicitly as an open record; the slow-stock trajectory "
        "cell is reclassified as a disagreement between the reconstruction's two records "
        "(bistability, a non-decayed transient, or a classification-threshold artefact) and the "
        "30%-error cells as noise-driven variance at a non-noise-adjusted threshold; the "
        "Section 2.4 screen bands' descent from the archived stage-map peaks is acknowledged; "
        "Section 4.6's distributive-constraints material is relocated to Appendix B, leaving a "
        "brief measurement-limit paragraph in the Discussion; the abstract's cohort wording is "
        "harmonised to the paper's own 42; the companion delay study is cited in text and in "
        "the References (Author, D., et al., in review); and the uncited DFO (2022) entry is "
        "cited at the assessment-record sentence in Section 2.7. Rose (2026) and the frozen "
        "2026-09-01 plan date are resolved-by-clock and untouched. No spectral record, table "
        "value, crossing, or verdict changes: Table 1, Table 2, the Section 3.4 comparison "
        "table, and the Section 4.6 mismatch table are byte-identical (the last relocated "
        "verbatim), and Box 1 and Table 3 are the new tables."
    )
    t = t[:idx] + new_log + t[log_end:]

    # ---------------- abstract: R23 q-sensitivity + 42 ----------------
    t = sub1(t,
        "a threshold reported by a first-order discretisation is a command-step artefact. "
        "The sample-and-hold map and the continuous-delay equation are distinct operators;",
        "a threshold reported by a first-order discretisation is a command-step artefact. "
        "The archived regions are also not robust to the catchability scale the stage record "
        "never declared: at $q = 0.1$, against the reconstruction's imported $q = 0.001$, every "
        "class's annual-review verdict flips, so the archived-versus-reconstructed comparison "
        "is uninformative at that undeclared scale rather than a non-reproduction. "
        "The sample-and-hold map and the continuous-delay equation are distinct operators;",
        "abstract-q")

    t = sub1(t,
        "A multiplicity-controlled Lomb–Scargle screen of several dozen annually assessed stocks",
        "A multiplicity-controlled Lomb–Scargle screen of 42 annually assessed stocks",
        "abstract-42")

    # ---------------- Box 1: the claims ledger ----------------
    BOX1 = """**Box 1. Claims at their exact evidential status.**

Each load-bearing claim, its evidential status, and its record pointer. Nothing in this box is new; the body sections carry the full statements.

| Claim | Evidential status | Record |
|---|---|---|
| Forward invariance of the sampled state space | Exact (induction) | Section 3.1, Proposition 3.1 |
| Rapid-review limit: finite-horizon consistency only | Exact, scoped | Section 3.2 |
| Small-$T_r$ multiplier transfer $\\mu_j = 1 + T_r\\lambda_j + O(T_r^2)$ | Conditional (hyperbolicity, $C^1$-consistency, projection inactive) | Section 3.2 |
| Euler hold map: complex pair at 47.536 yr; real $-1$ at 79.143 yr; stable band [47.54, 79.14] yr | Closed-form monodromy, 200,001-point scan with bisection; command-step artefacts relative to the exact map | Section 3.4 |
| Euler protective channel: real $-1$ at 2.306 yr, stable only on [0.2, 2.31] yr | Same record; artefact band | Section 3.4 |
| Exact held-assessment map: single complex crossing at 6.501 yr (unstable to stable) | Closed-form monodromy record | Section 3.4 |
| Exact protective channel: no crossing; maximum $\\rho = 0.9967$ | Same record | Section 3.4 |
| Annual review unstable: $\\rho = 1.00035$ (exact) and $1.00055$ (Euler); protective $0.9838$ | Multiplier record; near-unit-circle margins with sensitivity caveat | Section 3.4 |
| Continuous-delay Hopf pair at 3.666 and 150.358 yr on the same plant | Companion delay study (in review) | Section 3.4 |
| Relation between the three undelayed-limit statements | Recorded as an open tension; continuous eigenvalue not printed | Section 3.4 |
| Stage-map archived windows: anchovy 3–4 yr, sprat 6–12 yr, cod convergence on [1, 20] yr, slow-stock oscillation-then-convergence | Archived, unreproduced (generating computation unattached) | Section 3.3 |
| Screen bands 4–8 yr (biomass) and 12–60 yr (effort) | Descend from the archived stage peaks; inherit provisional status | Sections 2.4 and 3.3 |
| Stage reconstruction: annual stability $\\rho(1) = 0.895$ (anchovy), $0.923$ (sprat), $0.956$ (cod), $0.994$ (slow-stock); long-horizon band from 34–35 yr; slow-stock $\\rho(50) = 0.67$ | Declared, pre-registered reconstruction (plan frozen before any run) | Section 3.4 |
| Stage reconstruction at $q = 0.1$: every class unstable at annual review ($\\rho(1) \\ge 1.29$); slow-stock $\\rho(50) = 7.8$ | Declared sensitivity layer of the reconstruction | Section 3.4 |
| Archived-versus-reconstruction verdicts (MATCH/MISMATCH table) | Post-hoc consistency check; uninformative at the undeclared $q$ | Section 3.4 |
| Screen of 42 annually assessed stocks: zero robust target-band peaks | BH-adjusted selected-cohort consistency check | Section 3.5 |
| Power: sprat-class 1.0 and 0.24–0.58; anchovy-class 0.02–0.14 | Conditional simulations | Section 3.6 |
| Structured case search: zero eligible cases among more than thirty systems | Author-curated inventory | Sections 2.6 and 3.7 |
| Anchoveta–ENSO association: 3.7 yr peak, $r = +0.51$, era-split 1950–1984 | Registered-data battery; association, not an identified mechanism | Section 3.7 |
| Northern cod crash window 1991–1995 (Table 2) | Assessment record (DFO CSAS SAR 2016/026, NCAM M-shift) | Sections 2.7 and 3.8 |
| Constrained-M quantities ($M = 0.46$, $F = 1.37$, unreported catch $257.8$ kt yr$^{-1}$, …) | Unreproduced hypotheses on the open-problem docket | Section 3.8 |
| Northern cod two-window split | Descriptive partition | Sections 3.8 and 4.3 |
| Post-2015 production stall | Review record (Rose, 2026) | Section 3.8 |
| Phase-line obstruction | Exact; model-class diagnostic (its two conditions unmet by the assessment record) | Sections 2.7 and 3.8 |
| Five prospective designs | Specified, unexecuted; no registration identifier | Section 4.5 |
| Distributive constraints | Declared, not operationalised | Section 4.6 and Appendix B |"""

    t = sub1(t,
        "stability\n\n## 1 Introduction",
        "stability\n\n" + BOX1 + "\n\n## 1 Introduction",
        "box1-insert")

    # ---------------- R24: notation paragraph (Section 2.1) ----------------
    t = sub1(t,
        "*Notation.* Throughout, $N$ denotes the resource stock, $Z$ the institutional deficit "
        "signal, and $E$ the extraction effort. The review Poincaré map — the discrete-time map "
        "obtained by sampling the continuous flow at review instants — is written $\\mathcal "
        "P_{T_r}$; the projection onto the admissible effort interval $[0,E_{\\max}]$ is "
        "$\\Pi_{[0,E_{\\max}]}$. The signal map $\\Phi$ is a nonnegative functional of the "
        "deficit, with memory timescale $\\tau_m>0$; its softplus realisation is $\\Phi_k$. The "
        "effort law is $F_B$. The assessment operator is $\\mathcal A_n$ and the observation "
        "operator is $\\mathcal O$. For the northern cod case, $S$ is spawning stock biomass, "
        "$\\mathfrak s$ the unstable threshold, $K$ the unexploited carrying capacity, $C(t)$ "
        "removals, $M$ instantaneous natural mortality, and $F$ fishing mortality.",
        "*Notation.* Throughout, $N$ denotes the resource stock, $Z$ the institutional deficit "
        "signal, and $E$ the extraction effort. The review Poincaré map — the discrete-time map "
        "obtained by sampling the continuous flow at review instants — is written $\\mathcal "
        "P_{T_r}$; its Jacobian at the fixed point $X^*$, the monodromy matrix of the sampled "
        "loop, is $D\\mathcal P_{T_r}(X^*)$ (Section 2.3's multiplier condition is written on "
        "it); the projection onto the admissible effort interval $[0,E_{\\max}]$ is "
        "$\\Pi_{[0,E_{\\max}]}$. The signal map $\\Phi$ is a nonnegative functional of the "
        "deficit, with memory timescale $\\tau_m>0$; its softplus realisation is $\\Phi_k$, with "
        "shift $\\delta$ (a constant regularisation offset, distinct from and unrelated to the "
        "effort-law gain $\\delta_0$) and sharpness $k$. The effort law is $F_B$. The assessment "
        "operator is $\\mathcal A_n$ and the observation operator is $\\mathcal O$. In the "
        "control sections $S(\\cdot)$ is surplus production — $S(N)$ on the logistic plant "
        "(equation (2)) and $S(A)$ on the stage plant (Section 3.4) — while $g$ (Section 3.3), "
        "$C_E$ and $C_Z$ (Section 3.4), and the four-state loop (Section 3.7) are defined at "
        "their use sites. In the northern cod case (Sections 2.7 and 3.8, Table 2) $S$ is "
        "instead spawning stock biomass (reported as SSB in Table 2), $\\mathfrak s$ the "
        "unstable threshold, $K$ the unexploited carrying capacity, $C(t)$ removals, $M$ "
        "instantaneous natural mortality (with extra mortality $M_x$ in Lemma 2.2), and $F$ "
        "fishing mortality. The two scopes of $S$ never share an equation, and no symbol serves "
        "two sorts: the monodromy is written $D\\mathcal P_{T_r}(X^*)$ throughout, and Lemma "
        "2.2's production maximum is written $f_{\\max}$, leaving $M$ to natural mortality "
        "alone.",
        "notation-pass")

    # ---------------- R24: delta/k at the Phi_k equation ----------------
    t = sub1(t,
        "+\\delta\\right\\}.\n$$\n\nEquations (1)–(4) with $\\Phi=\\Phi_k$ constitute",
        "+\\delta\\right\\}.\n$$\n\nwith shift $\\delta$ a constant regularisation offset "
        "(distinct from and unrelated to the effort-law gain $\\delta_0$) and sharpness $k$ — "
        "the value used in the computed records, $k = 10$, is stated at its use site in "
        "Section 3.4 and collected in Table 3 of Appendix A. The multiplier records of Section "
        "3.4 presuppose a fixed point interior to the nonsmooth regions of $\\Phi_k$ and "
        "$\\Pi_{[0,E_{\\max}]}$; the equilibrium coordinates are not printed in this manuscript "
        "(Appendix A).\n\nEquations (1)–(4) with $\\Phi=\\Phi_k$ constitute",
        "phi-k-delta")

    # ---------------- companion citation, site 1 (Section 2.1) ----------------
    t = sub1(t,
        "reported in Section 3.4 with attribution to the companion delay study. The effort law is",
        "reported in Section 3.4 with attribution to the companion delay study (Author et al., "
        "in review). The effort law is",
        "companion-s1")

    # ---------------- registration-vocabulary consolidation (Section 2.2) ----------------
    t = sub1(t,
        "The solver configuration and initial histories are a declared registration "
        "requirement. Until that computational record is complete, the stage-output values "
        "carry provisional status.",
        "Until the solver configuration and initial histories are attached (Appendix A), the "
        "stage-output values carry provisional status.",
        "reg-22-remove")

    t = sub1(t,
        "The original stage record remains unattached, and its output values keep provisional "
        "status.\n\n### 2.3",
        "The original stage record remains unattached, and its output values keep provisional "
        "status. The declared and registered computational requirements of this section and of "
        "Sections 2.4, 2.5, 3.3, and 3.4 — solver configurations, initial histories, stock "
        "identifiers, the eligibility table, the null-calibration record, simulation code and "
        "seeds, and the reconstruction's plan, code, and output tables — are consolidated in "
        "Appendix A, which also fixes the vocabulary convention for 'declared', 'registered', "
        "and 'pre-registered'.\n\n### 2.3",
        "reg-pointer")

    # ---------------- R24: monodromy M -> D P (Section 2.3) ----------------
    t = sub1(t,
        "The operative condition is $\\det(M-e^{i\\theta}I)=0$ on the map to which the "
        "statement refers.",
        "The operative condition is $\\det(D\\mathcal P_{T_r}(X^*)-e^{i\\theta}I)=0$ on the map "
        "to which the statement refers, with $D\\mathcal P_{T_r}(X^*)$ the Jacobian of the "
        "review map at its fixed point (the monodromy matrix of the sampled loop).",
        "s23-monodromy")

    # ---------------- A4: screen-band lineage (Section 2.4) ----------------
    t = sub1(t,
        "integrates power in the predeclared bands (4–8 yr for biomass, 12–60 yr for effort).",
        "integrates power in the predeclared bands (4–8 yr for biomass, 12–60 yr for effort) — "
        "bands that descend from the archived, unreproduced stage-map diagnostics of Section "
        "3.3 (its observable-specific dominant peaks near 4 and 8 yr in biomass and 12 and "
        "60 yr in effort) and carry that record's provisional status into the screen's target "
        "definition.",
        "s24-lineage")

    # ---------------- registration meta-text removals (Sections 2.4, 2.5) ----------------
    t = sub1(t,
        "not a database classification of a stock as extractive or protective. The RAM stock "
        "identifiers and the eligibility table are a declared registration requirement.\n\n"
        "For each eligible",
        "not a database classification of a stock as extractive or protective.\n\n"
        "For each eligible",
        "reg-24-remove")

    t = sub1(t,
        "The reported zero count is the BH-adjusted result. The full null-calibration record "
        "— AR(1) coefficient estimation, detrending inside each null replicate, missing-data "
        "treatment, and the number of Monte Carlo replicates — is a registered requirement "
        "attached with the computational archive. One caveat is also registered:",
        "The reported zero count is the BH-adjusted result. One caveat is also registered:",
        "reg-24b-remove")

    t = sub1(t,
        "Power is estimated on 100–200 yr synthetic records across noise scales. The "
        "simulation code and seeds are a declared registration requirement.",
        "Power is estimated on 100–200 yr synthetic records across noise scales.",
        "reg-25-remove")

    # ---------------- housekeeping: DFO (2022) cited (Section 2.7) ----------------
    t = sub1(t,
        "The case evidence is the assessment record.",
        "The case evidence is the assessment record (the recovery-potential and sequential "
        "stock assessments: DFO, 2011, 2016, 2022, 2024).",
        "dfo-2022")

    # ---------------- R24: Lemma 2.2's production maximum M -> f_max ----------------
    t = sub1(t,
        "the unique maximum $S^* = S_+$ with value $M = f(S^*) > 0$",
        "the unique maximum $S^* = S_+$ with value $f_{\\max} = f(S^*) > 0$",
        "lemma-fmax-1")
    t = sub1(t,
        "For $0 < C < M$, the intermediate value theorem",
        "For $0 < C < f_{\\max}$, the intermediate value theorem",
        "lemma-fmax-2")
    t = sub1(t,
        "($f(\\mathfrak s) = 0 < C < M = f(S^*)$)",
        "($f(\\mathfrak s) = 0 < C < f_{\\max} = f(S^*)$)",
        "lemma-fmax-3")
    t = sub1(t,
        "($f(K) = 0 < C < M$)",
        "($f(K) = 0 < C < f_{\\max}$)",
        "lemma-fmax-4")
    t = sub1(t,
        "As $C \\uparrow M$ the two roots",
        "As $C \\uparrow f_{\\max}$ the two roots",
        "lemma-fmax-5")
    t = sub1(t,
        "and for $C > M$ the equation",
        "and for $C > f_{\\max}$ the equation",
        "lemma-fmax-6")

    # ---------------- R24: g defined (Section 3.3) ----------------
    t = sub1(t,
        "The corresponding continuous-delay calculations locate response regions near "
        "$rg\\approx 1.5$–$1.6$:",
        "The corresponding continuous-delay calculations on the delayed-recruitment "
        "parameterisation — $g$ is its maturation delay, and the response regions are located "
        "through the product $rg$ — locate response regions near $rg\\approx 1.5$–$1.6$:",
        "s33-g")

    # ---------------- R24: C_E, C_Z defined + companion site 2 (Section 3.4) ----------------
    t = sub1(t,
        "for $C_E \\ne 0$. Comparing its monodromy",
        "for $C_E \\ne 0$ — the exact solution, over one review interval, of the linearised "
        "effort law $\\dot e = C_E e + C_Z z$ with the assessment $z$ held, where $C_E$ and "
        "$C_Z$ are the coefficients of that linearisation (the partial derivatives of $F_B$ "
        "with respect to $E$ and $Z$ at the compared fixed point; unrelated to the removals "
        "$C$ of the cod case), and equation (4)'s increment is the forward-Euler discretisation "
        "of the same linear object. Comparing its monodromy",
        "s34-CE-CZ")

    t = sub1(t,
        "executed and verified on the companion delay study's identical hold map (same "
        "effort-law bracket,",
        "executed and verified on the companion delay study's identical hold map (Author et "
        "al., in review; same effort-law bracket,",
        "companion-s2")

    # ---------------- spectral margins paragraph (claude A2 / grok) ----------------
    MARGINS = (
        "**Spectral margins of the annual-review verdict.** The annual-review instability is a "
        "near-unit-circle record, and its margins are part of the record. The exact "
        "held-assessment update's annual spectral radius is $\\rho = 1.00035$ — a modulus "
        "exceeding unity by $3.5\\times 10^{-4}$ — with the forward-Euler update at $1.00055$ "
        "and the protective channel at $0.9838$ (maximum $0.9967$ over the tested range). The "
        "multiplier types are recorded with the crossings — a complex pair at the exact map's "
        "single 6.501 yr crossing (the Neimark–Sacker signature), real $-1$ multipliers at the "
        "Euler crossings (79.143 yr extractive, 2.306 yr protective) — while the dominant "
        "multiplier's angle $\\theta$ at the crossing and the continuous eigenvalue $\\lambda$ "
        "to which Section 3.2's transfer relation refers are not printed in this manuscript; "
        "they belong to the declared computational record (Appendix A). At a margin of this "
        "size the verdict is conditional on the monodromy's numerical construction — the "
        "printed precision record is the 200,001-point scan with bisection refinement; the "
        "linearisation construction and floating-point detail are archive items — and on the "
        "unprinted parameter vector (Table 3). What the margin does not condition is the "
        "ordering across updates and channels (exact $1.00035$ below Euler $1.00055$; "
        "protective $0.9838$ below both) or the crossing directions; the headline \"annual "
        "review is unstable\" is read at that status."
    )
    t = sub1(t,
        "the exact protective map is stable throughout.\n\n![Figure 1]",
        "the exact protective map is stable throughout.\n\n" + MARGINS + "\n\n![Figure 1]",
        "margins-insert")

    # ---------------- R24: extractive/mobilising unification (6 sites) ----------------
    t = sub1(t, "crosses twice on the mobilising channel",
                "crosses twice on the extractive channel", "chan-1")
    t = sub1(t, "crosses once on the mobilising channel",
                "crosses once on the extractive channel", "chan-2")
    t = sub1(t, "Both Euler crossings of the mobilising channel",
                "Both Euler crossings of the extractive channel", "chan-3")
    t = sub1(t, "Annual review is unstable on both mobilising updates",
                "Annual review is unstable on both extractive updates", "chan-4")
    t = sub1(t, "The same mobilising loop under continuous delay",
                "The same extractive loop under continuous delay", "chan-5")
    t = sub1(t, "exactly one crossing (mobilising, 6.50 yr)",
                "exactly one crossing (extractive, 6.50 yr)", "chan-6")

    # ---------------- one-plant contrast: tau_- defined + companion site 3 ----------------
    t = sub1(t,
        "but stable under continuous delay ($\\tau = 1$ yr $< \\tau_-$); at $T_r = 8$ yr the "
        "ordering reverses",
        "but stable under continuous delay ($\\tau = 1$ yr $< \\tau_-$, the unstable window's "
        "lower edge); at $T_r = 8$ yr the ordering reverses",
        "tau-minus")

    t = sub1(t,
        "carries the companion delay study's certified Hopf pair at 3.666 and 150.358 yr; "
        "the sampled operator's exact crossing",
        "carries the companion delay study's certified Hopf pair at 3.666 and 150.358 yr "
        "(Author et al., in review); the sampled operator's exact crossing",
        "companion-s3")

    # ---------------- A1: undelayed-limit reconciliation (Section 3.4) ----------------
    RECONCILE = (
        "**The undelayed limit, reconciled explicitly.** Three statements of this manuscript "
        "bear on the undelayed loop and are now read together rather than left implicit. "
        "Section 2.3 declares the continuous-delay equation and the logistic hold map to be "
        "the same feedback loop under two delay operators; Section 3.2 states that under "
        "hyperbolicity the sampled multipliers satisfy $\\mu_j(T_r) = 1 + T_r\\lambda_j + "
        "O(T_r^2)$, so that small-$T_r$ sampled stability follows the sign of the continuous "
        "eigenvalue $\\lambda_j$; and this section records both that the undelayed equilibrium "
        "of the hold-map core is already unstable (annual $\\rho = 1.00035$) and that the same "
        "loop under continuous delay is stable at $\\tau = 1$ yr, below the companion's first "
        "Hopf crossing at 3.666 yr. Those records do not close at the zero-delay limit. If the "
        "continuous eigenvalue $\\lambda$ is positive — the direction the sampled record "
        "suggests through Section 3.2's relation — then the continuous-delay equation is "
        "unstable as $\\tau \\to 0$ and an even number of crossings must lie between $0$ and "
        "$3.666$ yr that neither this manuscript nor the companion's certified pair reports. "
        "If $\\lambda \\le 0$, then the sampled instability persisting down to $T_r = 0.2$ yr "
        "is inconsistent with Section 3.2's transfer conditions on this parameterisation. The "
        "eigenvalue $\\lambda$ is not printed in this manuscript (the spectral-margins record "
        "above; Appendix A), so the reconciliation is recorded as open rather than "
        "adjudicated: the operator-scoped records stand as recorded — annual instability under "
        "sampling, stability under continuous delay at $\\tau = 1$ yr, and the reversal at "
        "$T_r = 8$ yr — and Section 2.3's same-loop declaration and Section 3.2's transfer "
        "statement are read as scoped to their own hypotheses, not as a continuity argument "
        "connecting the two records at zero delay."
    )
    t = sub1(t,
        "the cross-plant observation of Section 2.3 is now a same-plant one.\n\n**The "
        "protective controller on the same maps.**",
        "the cross-plant observation of Section 2.3 is now a same-plant one.\n\n" + RECONCILE +
        "\n\n**The protective controller on the same maps.**",
        "reconcile-insert")

    # ---------------- A9: slow-stock reclassification (Section 3.4 Records) ----------------
    t = sub1(t,
        "relative tail standard-deviation thresholds 2% and 0.1%) agrees with the spectral "
        "record: anchovy, sprat, and cod converge at every $T_r \\in [1,20]$; the slow-stock "
        "class shows a persistent oscillation at $T_r = 10$ yr only (relative tail standard "
        "deviation 5.5%; dominant period $\\approx 24$ yr in both stock and effort; effort "
        "excursion 537% against a biomass excursion of 18%), converging at every other grid "
        "point.",
        "relative tail standard-deviation thresholds 2% and 0.1%) agrees with the spectral "
        "record for the three faster classes, which converge at every $T_r \\in [1,20]$. The "
        "slow-stock class does not agree with its own multiplier record: it shows a persistent "
        "oscillation at $T_r = 10$ yr only (relative tail standard deviation 5.5%; dominant "
        "period $\\approx 24$ yr in both stock and effort; effort excursion 537% against a "
        "biomass excursion of 18%), converging at every other grid point, against a multiplier "
        "record with no crossings anywhere on the grid. A persistent oscillation at a linearly "
        "stable fixed point is bistability, a non-decayed transient, or a "
        "classification-threshold artefact; the record does not distinguish among them, and "
        "the cell is reported as a disagreement between the reconstruction's two records, not "
        "as an agreement.",
        "a9-slow")

    t = sub1(t,
        "(2.1–2.6%, against a stable multiplier record without error) while",
        "(2.1–2.6%, against a stable multiplier record without error — cells read as "
        "noise-driven variance rather than oscillation, since the 2% relative tail threshold "
        "is not noise-adjusted) while",
        "a9-noise")

    # ---------------- R23: the Reading reworded ----------------
    t = sub1(t,
        "but does not reproduce the anchovy 3–4 yr or the sprat 6–12 yr response regions. On "
        "this declared plant family those classes converge at every review interval, and the "
        "only instability the reconstructed loop produces is its own long-horizon band, "
        "entering at 34–42 yr and extending to the grid's end, which has no counterpart among "
        "the archived windows. A match is a consistency statement about the archived record; "
        "the mismatches do not adjudicate the archived values, whose generating computation is "
        "not available — they establish only that this declared family does not reproduce "
        "those windows. The reconstruction therefore supplies",
        "but not the anchovy 3–4 yr or the sprat 6–12 yr response regions: on this declared "
        "plant family those classes converge at every review interval, and the only "
        "instability the reconstructed loop produces is its own long-horizon band, entering at "
        "34–42 yr and extending to the grid's end, which has no counterpart among the archived "
        "windows. The comparison, however, is uninformative rather than a non-reproduction. "
        "The stage map declares no catchability; the table is computed at the imported value "
        "$q = 0.001$; and at the declared sensitivity $q = 0.1$ every verdict in the table "
        "flips — every class unstable at annual review ($\\rho(1) \\ge 1.29$), the slow-stock "
        "class unstable across the entire grid — so a match or a mismatch at either value is a "
        "statement about this declared family at an undeclared scale, not an adjudication of "
        "the archived values, whose generating computation is not available. The "
        "reconstruction therefore supplies",
        "reading-reword")

    # ---------------- R24: "four-state" defined + companion site 4 (Section 3.7) ----------------
    t = sub1(t,
        "cohort resonance supplies an alternative mechanism, its period 15–25 times shorter "
        "than the four-state prediction.",
        "cohort resonance supplies an alternative mechanism, its period 15–25 times shorter "
        "than the four-state prediction — the stage-structured review map's closed loop of "
        "four state components (adults $A$, juveniles $J$, memory signal $Z$, held effort "
        "$E$), whose slow-stock class carries the centuries-scale dominant timescales of "
        "Section 3.3.",
        "four-state")

    t = sub1(t,
        "baseline instability window ($\\approx 0.022$ yr⁻¹ at $\\eta = 0.914$)",
        "baseline instability window ($\\approx 0.022$ yr⁻¹ at $\\eta = 0.914$; Author et al., "
        "in review)",
        "companion-s4")

    # ---------------- R23 + consistency: Section 4.1 ----------------
    t = sub1(t,
        "the archived windows' provisional status and the reconstruction's non-reproduction of "
        "them are stated in Sections 3.3 and 3.4;",
        "the archived windows' provisional status and the reconstruction's comparison with "
        "them are stated in Sections 3.3 and 3.4;",
        "s41-comparison")

    t = sub1(t,
        "the Euler-reported 47.5 yr crossing being a command-step artefact — under the "
        "logistic hold map.\n\nWith the complete crossing record in hand",
        "the Euler-reported 47.5 yr crossing being a command-step artefact — under the "
        "logistic hold map. The stage-map layer of that record carries a declared limitation "
        "of its own: the stage map fixes no catchability, the reconstruction imports the "
        "hold-map core's $q = 0.001$, and at the declared sensitivity $q = 0.1$ every verdict "
        "of the Section 3.4 comparison flips — every class unstable at annual review "
        "($\\rho(1) \\ge 1.29$), the slow-stock class unstable across the entire grid "
        "($\\rho(50) = 7.8$) — so the archived-window comparison is uninformative at the "
        "undeclared scale rather than a non-reproduction (Section 3.4's Reading).\n\nWith the "
        "complete crossing record in hand",
        "s41-q")

    # ---------------- 4.6 relocation (both audits) ----------------
    h46 = "### 4.6 Distributive constraints where reproducible"
    if t.count(h46) != 1 or t.count("### 4.7 Limitations") != 1:
        raise SystemExit("FAIL: Section 4.6/4.7 anchors")
    i46 = t.find(h46)
    i47 = t.find("### 4.7 Limitations")
    body46 = t[i46 + len(h46):i47].strip("\n")
    if not (body46.startswith("Where the social side of the cod case can be carried")
            and body46.endswith("in the Supplementary material.")
            and "| Population | registered licence holders" in body46
            and body46.count("\n| ") >= 3):
        raise SystemExit("FAIL: Section 4.6 body extraction")
    STUB = (
        "The social side of the cod case is carried at measurement level, but outside the "
        "Discussion's technical flow: the constituency-definition mismatch table (licence "
        "holders against census-subdivision residents; fishing income against all-resident "
        "sector income; the undeclared floor), the Statistics Canada community-level series "
        "(tables 38-10-0167-01 and 38-10-0168-01), the measured-floor construction $(I_k, "
        "c_k)$ with its componentwise non-decline rule, and the admitted world-hook "
        "instruments are relocated to Appendix B, with the full instrument detail and the "
        "unreproduced pipeline register in the Supplementary material (S6). What the case does "
        "not measure is the summary: no licence-holder panel exists, the community series is "
        "not one, and no measured floor is operational — the distributive constraints remain "
        "declared rather than resolved (Section 4.7 (viii))."
    )
    t = t[:i46] + h46 + "\n\n" + STUB + "\n\n" + t[i47:]

    # ---------------- appendices A (registration + Table 3) and B (4.6 material) ----------------
    APPENDIX_A = """## Appendix A. Registration and reproducibility record (consolidated)

This appendix consolidates the registration meta-text that Sections 2.2, 2.4, and 2.5 previously carried in the main flow, so that the Methods keep only load-bearing status statements; each consolidated statement is preserved here. The vocabulary convention: **declared** fixes an object in this manuscript's own record (a convention, a comparator class, or a sensitivity layer stated in the text); **registered** attaches a computational artifact to the archive (solver configuration, seeds, identifiers, calibration records); **pre-registered** dates and freezes a plan before any run, as the stage-map reconstruction of Section 3.4 does. The consolidated requirements:

- The solver configuration and initial histories are a declared registration requirement; until that computational record is complete, the stage-output values carry provisional status (Sections 2.2 and 3.3).
- The RAM stock identifiers and the eligibility table are a declared registration requirement (Section 2.4).
- The full null-calibration record — AR(1) coefficient estimation, detrending inside each null replicate, missing-data treatment, and the number of Monte Carlo replicates — is a registered requirement attached with the computational archive (Section 2.4).
- The simulation code and seeds are a declared registration requirement (Section 2.5).

Two further consolidated records. First, the members of the logistic-core parameter vector that the text never prints ($r$, $K$, $E_{\\max}$, $\\delta_0$, $Z_{\\rm ref}$, $\\Delta_{\\rm ref}$, $\\delta$, $\\tau_m$), the linearised fixed point $(N^*, E^*, Z^*)$ and its interiority to the nonsmooth regions of $\\Phi_k$ and $\\Pi_{[0,E_{\\max}]}$, the monodromy's numerical construction, and the continuous eigenvalue $\\lambda$ and crossing angle $\\theta$ of Section 3.4's records are part of this declared computational record; Table 3 collects what the manuscript itself prints. Second, the Data availability statement tracks the deposit status of the same requirements (including the reconstruction's dated plan, campaign code, and output tables); the prospective designs of Section 4.5 remain preregistration targets with no registration identifier or archived protocol.

**Table 3.** Parameter values printed in this manuscript for the logistic hold-map core and the stage-structured reconstruction. No value here is newly computed; entries the text does not print are marked as such and remain attached to the declared computational record (this appendix).

| Object | Parameter | Value as printed | Printed at |
|---|---|---|---|
| Logistic hold-map core | catchability $q$ | 0.001 | Section 3.4 (Plant paragraph) |
| Logistic hold-map core | softplus sharpness $k$ | 10 | Section 3.4 (Plant paragraph) |
| Logistic hold-map core | effort-law gain $\\eta$ | 0.914 (continuous-delay asides on the same loop) | Sections 3.3 and 3.7 |
| Logistic hold-map core | $r$, $K$, $E_{\\max}$, $\\delta_0$, $Z_{\\rm ref}$, $\\Delta_{\\rm ref}$, $\\delta$, $\\tau_m$ | not printed in this manuscript | declared computational record (this appendix) |
| Logistic hold-map core | linearised fixed point $(N^*, E^*, Z^*)$; interiority to the nonsmooth regions of $\\Phi_k$ and $\\Pi$ | not printed in this manuscript | declared computational record (this appendix) |
| Logistic hold-map core | crossing record | 47.536, 79.143, 2.306, 6.501 yr; $\\rho$ = 1.00035, 1.00055, 0.9838, 0.9967 | Section 3.4 |
| Logistic hold-map core | scan construction | 200,001-point scan with bisection over $[0.2, 200]$ yr | Section 3.4 |
| Stage reconstruction | class natural mortality $M$ and recruitment delay $\\tau$ | anchovy (0.90, 1), sprat (0.40, 2), cod (0.20, 5), slow-stock (0.045, 25) yr | Section 3.4 (Plant paragraph, with sources) |
| Stage reconstruction | steepness $h$ | 0.75; declared sensitivity layer $\\{0.6, 0.9\\}$ | Section 3.4 |
| Stage reconstruction | scale and survival | $A_0 = 100$; $s_A = s_J = e^{-M}$; $\\beta = (c-1)/A_0$, $\\alpha = c(1-s_A)/s_J$, $c = 4h/(1-h)$ | Section 3.4 |
| Stage reconstruction | catchability $q$ | 0.001; declared sensitivity 0.1 | Section 3.4 |
| Stage reconstruction | softplus sharpness $k$ | 10 | Section 3.4 |
| Stage reconstruction | derivative construction | central finite differences, step $10^{-6}$, chain-rule cross-check to $10^{-4}$ | Section 3.4 |
| Stage reconstruction | scan grid | $T_r \\in \\{1,\\ldots,50\\}$ yr at annual internal steps | Section 3.4 |
| Stage reconstruction | trajectory classification | 2000 review-steps, tail 500, relative tail standard-deviation thresholds 2% and 0.1%; initial condition at the unfished plant equilibrium, memory filled, effort at half the equilibrium | Section 3.4 |"""

    APPENDIX_B = ("## Appendix B. Distributive constraints where reproducible "
                  "(relocated from Section 4.6)\n\n" + body46)

    t = sub1(t, "## Data availability",
                APPENDIX_A + "\n\n" + APPENDIX_B + "\n\n## Data availability",
                "appendices-insert")

    # ---------------- References: companion entry (fresh letter D) ----------------
    t = sub1(t,
        "Philosophical Transactions of the Royal Society A, 370: 1166–1184.\n\nBenjamini, Y., "
        "and Hochberg, Y. 1995.",
        "Philosophical Transactions of the Royal Society A, 370: 1166–1184.\n\nAuthor, D., "
        "et al., in review. Delay-induced regime change in harvested stocks: the mobilising "
        "and protective channels of institutional feedback. Companion delay-dynamics "
        "study.\n\nBenjamini, Y., and Hochberg, Y. 1995.",
        "ref-companion")

    v21 = t

    # =====================================================================
    # mechanical checks (all fail loudly)
    # =====================================================================
    if v21.count("several dozen") != 0:
        raise SystemExit("FAIL: 'several dozen' still present")
    if v21.count("*Version log (v21).*") != 1 or v21.count("*Version log (v20).*") != 0:
        raise SystemExit("FAIL: version log replacement")

    # 42-stock counts unchanged; the only new "42" is the harmonised abstract one
    n42_old = len(re.findall(r"42-[Ss]tock", v20))
    n42_new = len(re.findall(r"42-[Ss]tock", v21))
    if n42_old != 4 or n42_new != n42_old:
        raise SystemExit(f"FAIL: 42-stock counts {n42_old} -> {n42_new} (expected 4 -> 4)")
    for phrase in [
        "a Selected 42-Stock Spectral Screen",
        "a multiplicity-controlled spectral screen of 42 annually assessed stocks",
        "a frozen 42-stock cohort of the RAM Legacy Stock Assessment Database",
        "### 3.5 The selected 42-stock spectral screen",
        "The 42-stock screen returns a spectral null",
        "36–42 yr",
        "34–42 yr",
    ]:
        if v21.count(phrase) != v20.count(phrase):
            raise SystemExit(f"FAIL: 42-carrying phrase changed: {phrase!r}")
    if len(re.findall(r"\b42\b", v21)) < len(re.findall(r"\b42\b", v20)):
        raise SystemExit("FAIL: '42' tokens lost (the only permitted additions are the "
                         "harmonised abstract, the ledger row, and the version log)")

    # registration-vocabulary reduction in the main body; appendix carries the text
    narrow = re.compile(r"\b(registered|registration|preregistration|preregistered|pre-registered)\b")
    main20 = v20[v20.find("## 1 Introduction"):v20.find("## Data availability")]
    main21 = v21[v21.find("## 1 Introduction"):v21.find("## Appendix A")]
    c20, c21 = len(narrow.findall(main20)), len(narrow.findall(main21))
    if not c21 < c20:
        raise SystemExit(f"FAIL: registration-vocabulary main-body count not reduced ({c20} -> {c21})")
    if "declared registration requirement" in main21 or "registered requirement" in main21:
        raise SystemExit("FAIL: registration meta-phrases remain in the main body")
    appA = v21[v21.find("## Appendix A"):v21.find("## Appendix B")]
    if appA.count("declared registration requirement") < 3 or appA.count("a registered requirement") != 1:
        raise SystemExit("FAIL: Appendix A does not carry the consolidated registration text")

    # resolved-by-clock items untouched (body excludes the version-log line)
    body21 = "\n".join(l for l in v21.splitlines() if not l.startswith("*Version log (v21).*"))
    if body21.count("2026-09-01") != v20.count("2026-09-01"):
        raise SystemExit("FAIL: frozen plan date count changed")
    if body21.count("Rose (2026)") != v20.count("Rose (2026)"):
        raise SystemExit("FAIL: Rose (2026) citations changed")

    # terminology: no 'mobilising' in the body; exactly the log mention + the companion title
    seg_main = v21[v21.find("## 1 Introduction"):v21.find("## References")]
    if "mobilising" in seg_main:
        raise SystemExit("FAIL: 'mobilising' survives in the main body")
    if v21.count("mobilising") != 2:
        raise SystemExit(f"FAIL: 'mobilising' total {v21.count('mobilising')} != 2 (log + reference title)")

    # tables: existing byte-identical; new tables itemized
    def table_lines(s):
        return [l for l in s.splitlines() if l.startswith("|")]
    old_tl, new_tl = table_lines(v20), table_lines(v21)
    LEDGER_HDR = "| Claim | Evidential status | Record |"
    T3_HDR = "| Object | Parameter | Value as printed | Printed at |"
    if new_tl.count(LEDGER_HDR) != 1 or new_tl.count(T3_HDR) != 1:
        raise SystemExit("FAIL: new-table headers not found exactly once")
    li = new_tl.index(LEDGER_HDR)
    ti = new_tl.index(T3_HDR)
    if new_tl[li + 1] != "|---|---|---|" or new_tl[ti + 1] != "|---|---|---|---|":
        raise SystemExit("FAIL: new-table separators malformed")
    ledger_block = new_tl[li:li + 28]           # header + sep + 26 claim rows
    t3_block = new_tl[ti:ti + 17]               # header + sep + 15 parameter rows
    if len(ledger_block) != 28 or len(t3_block) != 17:
        raise SystemExit("FAIL: new-table blocks have wrong size")
    rest = new_tl[:li] + new_tl[li + 28:]
    k = rest.index(T3_HDR)
    rest = rest[:k] + rest[k + 17:]
    if rest != old_tl or len(old_tl) != 35:
        raise SystemExit("FAIL: existing table lines are not byte-identical and in order")
    if not (v21.find("## Appendix B") < v21.find("| Object | Candidate definition |")):
        raise SystemExit("FAIL: the 4.6 mismatch table was not relocated into Appendix B")
    if v21.count("### 4.7 Limitations") != 1 or v21.count(h46) != 1:
        raise SystemExit("FAIL: section headings after relocation")
    if v21.count(body46) != 1:
        raise SystemExit("FAIL: 4.6 body not preserved verbatim exactly once")

    # frozen numbers: nothing lost
    for s in ["47.536", "79.143", "2.306", "6.501", "1.00035", "1.00055", "0.9838",
              "0.9967", "3.666", "150.358", "257.8", "537%", "0.895", "0.923",
              "0.956", "0.994", "0.67", "7.8", "1.29", "2.2–2.6", "0.022", "0.061",
              "3.7", "0.31", "0.51", "34.42", "+0.42"]:
        if v21.count(s) < v20.count(s):
            raise SystemExit(f"FAIL: frozen value lost or reduced: {s!r}")

    # expected new strings
    for needle, label in [
        ("**Box 1. Claims at their exact evidential status.**", "Box 1"),
        ("## Appendix A. Registration and reproducibility record (consolidated)", "Appendix A"),
        ("## Appendix B. Distributive constraints where reproducible (relocated from Section 4.6)", "Appendix B"),
        ("**Table 3.** Parameter values printed in this manuscript", "Table 3 caption"),
        ("**Spectral margins of the annual-review verdict.**", "margins paragraph"),
        ("**The undelayed limit, reconciled explicitly.**", "reconciliation paragraph"),
        ("every class's annual-review verdict flips", "R23 abstract"),
        ("every verdict of the Section 3.4 comparison flips", "R23 s4.1"),
        ("uninformative rather than a non-reproduction", "R23 reading"),
        ("Author, D., et al., in review. Delay-induced regime change in harvested stocks", "companion ref"),
        ("DFO, 2011, 2016, 2022, 2024", "DFO 2022 cited"),
        ("f_{\\max} = f(S^*) > 0", "f_max"),
        ("$\\det(D\\mathcal P_{T_r}(X^*)-e^{i\\theta}I)=0$", "monodromy on D P"),
        ("$g$ is its maturation delay", "g defined"),
        ("the exact solution, over one review interval, of the linearised effort law", "C_E C_Z defined"),
        ("the unstable window's lower edge", "tau_- defined"),
        ("the stage-structured review map's closed loop of four state components", "four-state defined"),
        ("a constant regularisation offset", "delta defined"),
        ("bands that descend from the archived, unreproduced stage-map diagnostics", "A4 lineage"),
        ("disagreement between the reconstruction's two records", "A9 slow-stock"),
        ("noise-driven variance rather than oscillation", "A9 error cells"),
        ("42 annually assessed stocks", "abstract 42"),
        ("are consolidated in Appendix A, which also fixes the vocabulary convention", "registration pointer"),
        ("relocated to Appendix B", "4.6 stub pointer"),
        ("What the case does not measure is the summary", "4.6 stub summary"),
    ]:
        if needle not in v21:
            raise SystemExit(f"FAIL: expected string missing [{label}]: {needle!r}")

    # companion in-text citations: exactly the four load-bearing sites
    n_comp = body21.count("Author et al., in review")
    if n_comp != 4:
        raise SystemExit(f"FAIL: companion in-text citations = {n_comp}, expected 4")
    if body21.count("Author, D., et al., in review") != 1:
        raise SystemExit("FAIL: companion reference entry not present once in the list")

    open(DST, "w", encoding="utf-8").write(v21)
    print(f"OK: wrote {DST}")
    print(f"    lines: {len(v20.splitlines())} -> {len(v21.splitlines())}")
    print(f"    registration vocab (main body): {c20} -> {c21}")
    print(f"    table lines: {len(old_tl)} -> {len(new_tl)} "
          f"(ledger 28 + parameter 17 new; existing 35 byte-identical, 4.6 table relocated)")
    m = re.search(r"## Abstract\n(.*?)\n\n\*\*Keywords", v21, re.S)
    print(f"    abstract words: {len(m.group(1).split())}")


if __name__ == "__main__":
    main()
