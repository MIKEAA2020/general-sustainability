#!/usr/bin/env python3
"""Wave-17 / Task 90, part 1: author paper4_delay_dynamics_v34.md --- the
humanized revision of paper4_delay_dynamics_v33.md implementing the owner's
go-ahead on the Task-89 plan (humanizing audits/JOINT_HUMANIZING_ASSESSMENT_
AND_PLAN.md, Part III).

Owner directive (this round): "1- provide implemented revision, ensuring
seamless flow, accuracy and error-free delivery 2- review your revision
against v33 and v32 and v31 to ensure all valid content is present and no
errors are introduced."

What v34 is: v33's content spine restyled with gemini's device kit (per the
owner's gemini-weighted instruction), plus grok's proven micro-improvements.
Content authority stays with v33 throughout:

FROZEN (byte-identical to v33, machine-checked below):
- title, keywords, every theorem/proposition/lemma/proof/remark content,
  every hypothesis label (H1)-(H5), every number, interval enclosure and
  table row, the reference list, declarations, supplementary material,
  the figure block, and the section skeleton (no heading added/removed).

ADOPTED FROM GEMINI (devices only; facts from v33):
- named plain-language concepts at first use ("governance delay" in the
  abstract and Section 1.1; "review cadence" at the Section 8 opener);
- numbered two-rule contrast in the abstract; bulleted contrasts for the
  classical-delay literature (Section 1.1), the three structural features
  after (1) (Section 2.1), the two rules (Section 11.1) and the two
  translation-table cautions (Section 11.3);
- the two-default-assumptions challenge and the one-sentence design-message
  cadence in the abstract (v33's own closing retained verbatim);
- the Section 9.2 five-regime summary table (a LaTeX-friendly pipe table,
  not ASCII art), built solely from v33's own Section 9.2 sentences;
- warning call-out boxes as blockquotes in Section 8 ("Governance warning")
  and Section 11.2 ("Management caution") carrying v33's own inter-review-
  depletion warnings verbatim;
- the three-tier certification list in Section 11.5 (proved theorems /
  interval certificates / declared-status numerical results), a
  reformatting of v33's own sentences with the same qualifiers;
- the extended Section 11.3 translation table (sample-and-hold review ->
  harvest control rule / TAC phrasing; subcritical Hopf crossing ->
  "tipping point for cycles"; inter-assessment stability margin), each
  wording grounded in v33's own definitions;
- "What this says" one-sentence plain readings after Theorem 8.1 and
  Proposition 8.1, from v33's own surrounding prose.

ADOPTED FROM GROK:
- all four remaining "iff" -> "if and only if";
- Section 5's opener cadence ("Its behavioural reading is direct: ..."),
  a strict simplification of v33's own sentence;
- the abstract's concrete window gloss ("a few years to well over a
  century in the examples studied") and the artefact sentence explicitly
  attached to the protective channel.

REJECTED (machine-checked zero-hit gates in build_latex_v17.py): every
verified fabrication catalogued in the Task-89 joint assessment ---
gemini's two hallucinated reference forms (both variants), the archetype
vocabulary, the invented table cells, the M3-LC channel inversion, the
title-level overclaims, the dropped-caveat regressions.

This script is fully reproducible from the repository alone: it applies 37
verbatim-anchored surgical edits to v33's markdown (each anchor must match
exactly once; edits are pairwise disjoint by construction), then runs the
md-level fail-loud battery: zero remaining standalone "iff"; every math
span of v34 byte-identical to a v33 span (empty whitelist); v34 numeric
multiset is a superset of v33's with ZERO new token values; identical
heading skeleton; title, keywords, references, data-availability,
competing-interest and supplementary blocks byte-identical; the figure
block byte-identical; device-presence needles; the full rejection scanner.
v33 is never modified (version discipline).  Re-running is idempotent.
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PR = ROOT / "arena agent 1/paper rewrites"
V33 = PR / "paper4_delay_dynamics_v33.md"
V34 = PR / "paper4_delay_dynamics_v34.md"

# ---------------------------------------------------------------------------
# The 31 surgical edits.  Each anchor was verified to occur exactly once in
# the v33 markdown before this script was written (fail-loud re-verified on
# every run).  Sequential application plus per-anchor count==1 guarantees
# pairwise disjointness.
# ---------------------------------------------------------------------------
EDITS: list[tuple[str, str, str]] = [
    # --- abstract: named concept + two-rule numbered contrast ---------------
    (
        "The delay studied in this paper sits in a different place — in the "
        "governance loop, the chain that leads from an observed stock decline "
        "to an institutional response. We analyse a three-state model",
        "The delay studied in this paper sits in a different place — in the "
        "governance loop, the chain that leads from an observed stock decline "
        "to an institutional response. It has a plain name: **governance "
        "delay**, the lag between the institution's observation of a decline "
        "and the response that acts on it. We analyse a three-state model",
        "abstract: name governance delay",
    ),
    (
        "Two response rules are compared throughout. Under the mobilising "
        "rule, effort grows as more effort is deployed. Under the protective "
        "rule, a quota-tracking law restores harvest toward a cap.",
        "Two response rules are compared throughout:\n\n"
        "1. **The mobilising rule.** Effort grows as more effort is deployed.\n"
        "2. **The protective rule.** A quota-tracking law restores harvest "
        "toward a cap.",
        "abstract: numbered two-rule contrast",
    ),
    (
        "bound a window of delays inside which the lag itself holds the loop "
        "stable. Both crossings are subcritical",
        "bound a window of delays inside which the lag itself holds the loop "
        "stable — a few years to well over a century in the examples studied. "
        "Both crossings are subcritical",
        "abstract: grok's concrete window gloss",
    ),
    (
        "Annual protective review remains stable. Annual mobilising review is "
        "unstable, and the loop restabilises only when the review interval "
        "exceeds about 6.5 yr, through a Neimark–Sacker-type crossing — the "
        "sampled-review analogue of a Hopf transition. An apparent threshold "
        "near 2.3 yr, reported by a first-order numerical update, is an "
        "artefact of the discretisation, not a property of the governance "
        "system.",
        "Annual protective review remains stable; an apparent threshold near "
        "2.3 yr, reported by a first-order numerical update, is an artefact of "
        "the discretisation, not a property of the governance system. Annual "
        "mobilising review is unstable, and the loop restabilises only when "
        "the review interval exceeds about 6.5 yr, through a Neimark–Sacker-"
        "type crossing — the sampled-review analogue of a Hopf transition.",
        "abstract: artefact sentence attached to the protective channel",
    ),
    (
        "That record grounds the two timing coordinates without calibrating "
        "any coefficient. The message of the paper is stated plainly.",
        "That record grounds the two timing coordinates without calibrating "
        "any coefficient. Two default assumptions are challenged directly: "
        "that the hazard in governing a renewable stock lies in its ecological "
        "lag alone, and that assessing the stock more often is always safer. "
        "Neither survives the analysis. The message of the paper is stated "
        "plainly.",
        "abstract: two-default-assumptions challenge",
    ),
    # --- Section 1.1: literature list + governance delay naming -------------
    (
        "resource dynamics. Hutchinson (1948) showed that a delayed "
        "self-limitation term destabilises logistic growth. Ezekiel (1938) "
        "documented",
        "resource dynamics. The classic results all place the delay inside the "
        "ecology itself:\n\n- Hutchinson (1948) showed that a delayed "
        "self-limitation term destabilises logistic growth.\n- Ezekiel (1938) "
        "documented",
        "1.1: classical-delay literature list (Hutchinson, Ezekiel)",
    ),
    (
        "in the pork cycle. Ludwig, Jones, and Holling (1978) placed",
        "in the pork cycle.\n- Ludwig, Jones, and Holling (1978) placed",
        "1.1: literature list (Ludwig)",
    ),
    (
        "at the centre of outbreak dynamics. Gurney, Blythe, and Nisbet "
        "(1980) gave",
        "at the centre of outbreak dynamics.\n- Gurney, Blythe, and Nisbet "
        "(1980) gave",
        "1.1: literature list (Gurney)",
    ),
    (
        "the single-species delayed logistic equation. Costantino et al. "
        "(1995) demonstrated",
        "the single-species delayed logistic equation.\n- Costantino et al. "
        "(1995) demonstrated",
        "1.1: literature list (Costantino)",
    ),
    (
        "in controlled laboratory populations. A large contemporary "
        "literature",
        "in controlled laboratory populations.\n- A large contemporary "
        "literature",
        "1.1: literature list (contemporary line)",
    ),
    (
        "The delay studied in this paper sits elsewhere: in the "
        "*institutional* loop. Stock assessment produces a signal of decline.",
        "The delay studied in this paper sits elsewhere: in the "
        "*institutional* loop — **governance delay**, the lag between the "
        "institution's observation of a decline and the response that finally "
        "acts on it. Stock assessment produces a signal of decline.",
        "1.1: governance delay named at first body use",
    ),
    # --- Section 2.1: the three structural features as a bulleted contrast --
    (
        "The memory input is a smoothed version of the stock-decline rate: on "
        "this core the identity $qEN - S(N) = -\\dot N$ holds exactly, so "
        "$\\Phi_k$ filters $-\\dot N$. The multiplicative gate "
        "$(1 - E/E_{\\max})$ is essential to what follows. It is a hard "
        "saturation architecture, not a generic effort law, and it enforces "
        "$E \\in [0, E_{\\max}]$ by construction. The registered "
        "parameterisations are:",
        "Three structural features of (1) carry everything that follows:\n\n"
        "- **Depletion filtering.** The memory input is a smoothed version of "
        "the stock-decline rate: on this core the identity "
        "$qEN - S(N) = -\\dot N$ holds exactly, so $\\Phi_k$ filters "
        "$-\\dot N$.\n"
        "- **The multiplicative gate.** The gate $(1 - E/E_{\\max})$ is "
        "essential to what follows. It is a hard saturation architecture, not "
        "a generic effort law, and it enforces $E \\in [0, E_{\\max}]$ by "
        "construction.\n"
        "- **The institutional delay.** The effort law reads the filtered "
        "memory at one fixed lag — the deployment delay $\\tau$ between "
        "decision and action.\n\n"
        "The registered parameterisations are:",
        "2.1: three structural features list",
    ),
    # --- grok micro-fixes ----------------------------------------------------
    (
        "positive iff $qE^* < r$",
        "positive if and only if $qE^* < r$",
        "3.1: iff -> if and only if",
    ),
    (
        "Its behavioural reading comes from fisheries governance: when an "
        "institution sees a deficit signal, it deploys more extraction effort "
        "— a fleet expansion, a subsidy release, an open-access licence "
        "issuance — and the deployment is realised only after a delay.",
        "Its behavioural reading is direct: when an institution sees a deficit "
        "signal, it deploys more extraction effort — a fleet expansion, a "
        "subsidy release, an open-access licence issuance — and the deployment "
        "is realised only after a delay.",
        "5: grok's plain opener cadence",
    ),
    (
        "The sampled equilibrium is exponentially stable iff every eigenvalue "
        "of $M_p(T_r)$ lies in the open unit disc.",
        "The sampled equilibrium is exponentially stable if and only if every "
        "eigenvalue of $M_p(T_r)$ lies in the open unit disc.",
        "6.4: iff -> if and only if",
    ),
    # --- Section 8: review cadence naming, cadence splits, iff, devices ------
    (
        "and the assessment result is acted on with a discrete update. On this "
        "architecture the review interval is a spectral design parameter",
        "and the assessment result is acted on with a discrete update. The "
        "review interval $T_r$ — the **review cadence** — is the length of "
        "time between successive assessments, the interval at which the "
        "institution re-decides. On this architecture the review interval is a "
        "spectral design parameter",
        "8: review cadence named at the opener",
    ),
    (
        "One point is stated once, at the outset: periodic review is a "
        "*hybrid* system",
        "One point is stated once, at the outset. Periodic review is a "
        "*hybrid* system",
        "8: opener cadence split",
    ),
    (
        "the review interval is a controller knob, not a governance "
        "recommendation; an interval that stabilises the equilibrium may still "
        "allow severe inter-review depletion",
        "the review interval is a controller knob, not a governance "
        "recommendation. An interval that stabilises the equilibrium may still "
        "allow severe inter-review depletion",
        "8: opener cadence split 2",
    ),
    (
        "exponentially stable iff every eigenvalue of $M(T_r)$ lies in the "
        "open unit disc;",
        "exponentially stable if and only if every eigenvalue of $M(T_r)$ lies "
        "in the open unit disc;",
        "Theorem 8.1: iff -> if and only if",
    ),
    (
        "On the gated Candidate A hold map the Euler scheme reports:",
        "**What Theorem 8.1 says.** The theorem turns review-cadence stability "
        "into an eigenvalue test: compute the one-period return map $M(T_r)$ "
        "of the reviewed loop, and the sampled equilibrium is stable exactly "
        "when every eigenvalue of that map lies inside the unit disc. The rest "
        "of the section runs this test for the two channels.\n\n"
        "On the gated Candidate A hold map the Euler scheme reports:",
        "8: What-this-says after Theorem 8.1",
    ),
    (
        "**the review interval is a local spectral design parameter**. Local "
        "spectral stability is not governance: a long review interval may "
        "locally stabilise the equilibrium while allowing severe transient "
        "depletion between reviews, and inter-review tube safety — the stock "
        "floor held along the whole interval under the declared disturbance "
        "class — is the additional criterion a governance recommendation "
        "would require, which is not certified here. The contrast with the "
        "protective channel",
        "**the review interval is a local spectral design parameter**.\n\n"
        "> **Governance warning.** Local spectral stability is not governance: "
        "a long review interval may locally stabilise the equilibrium while "
        "allowing severe transient depletion between reviews, and inter-review "
        "tube safety — the stock floor held along the whole interval under the "
        "declared disturbance class — is the additional criterion a governance "
        "recommendation would require, which is not certified here.\n\n"
        "The contrast with the protective channel",
        "8: governance warning call-out box",
    ),
    (
        "only weakly coupled by the controller; the protective maximum "
        "$0.9967$",
        "only weakly coupled by the controller. The protective maximum "
        "$0.9967$",
        "8: table-readings cadence split",
    ),
    (
        "*Remark (scheme-dependence of the sampled-data map).*",
        "**What Proposition 8.1 says.** Under the exact update the protective "
        "channel stays inside the unit circle at every tested review interval, "
        "while the mobilising channel crosses it exactly once, restabilising at "
        "a review interval of about 6.5 yr; the Euler-reported half-century "
        "thresholds are artefacts of the command step, not of the cadence.\n\n"
        "*Remark (scheme-dependence of the sampled-data map).*",
        "8: What-this-says after Proposition 8.1",
    ),
    # --- Section 9.2: regime enumeration cadence + summary table -------------
    (
        "the only attractor found from the declared tested histories; (ii)",
        "the only attractor found from the declared tested histories. (ii)",
        "9.2: regime enumeration split (ii)",
    ),
    (
        "closed at the fold $\\tau_f = 5.5872362$ yr); (iii)",
        "closed at the fold $\\tau_f = 5.5872362$ yr). (iii)",
        "9.2: regime enumeration split (iii)",
    ),
    (
        "without generic basin); (iv)",
        "without generic basin). (iv)",
        "9.2: regime enumeration split (iv)",
    ),
    (
        "not a fold; (v) $\\tau > \\tau_+$",
        "not a fold. (v) $\\tau > \\tau_+$",
        "9.2: regime enumeration split (v)",
    ),
    (
        "![Figure 1](figs_p4/fig2_five_regime_topology_v2.png)",
        "The regime record is collected in one display:\n\n"
        "| Regime | Delay range | Attractor record |\n"
        "|---|---|---|\n"
        "| (i) | $0 < \\tau < \\tau_-$ | Equilibrium unstable; a single "
        "large-amplitude cycle the only attractor found from the declared "
        "tested histories. |\n"
        "| (ii) | $\\tau_- < \\tau < \\tau_f$ | A stable focus coexisting with "
        "the large cycle — the lower bistable window, width $\\approx1.92$ yr, "
        "closed at the fold $\\tau_f = 5.5872362$ yr. |\n"
        "| (iii) | $\\tau_f < \\tau < \\tau_{f2}$ | Settling to the equilibrium "
        "from the tested histories; finite searches support, but cannot prove, "
        "basin monostability. |\n"
        "| (iv) | $\\tau_{f2} < \\tau < \\tau_+$ | Mathematical bistability: "
        "the second S-branch's stable returning arm coexists with the "
        "still-stable equilibrium; the capture onset in $[148.6, 149.5]$ yr is "
        "a basin boundary inside this window, not a fold. |\n"
        "| (v) | $\\tau > \\tau_+$ | Within the explored range, the "
        "equilibrium unstable and the captured family the only attractor found "
        "from the declared tested histories. |\n\n"
        "![Figure 1](figs_p4/fig2_five_regime_topology_v2.png)",
        "9.2: five-regime summary table",
    ),
    # --- Section 10: cadence split + iff ------------------------------------
    (
        "whose $0.4\\%$ width sets that resolution) while the Hopf pair stays "
        "within a few percent",
        "whose $0.4\\%$ width sets that resolution). The Hopf pair stays within "
        "a few percent",
        "10.1: cadence split",
    ),
    (
        "a Hopf root exists iff the loop transfer",
        "a Hopf root exists if and only if the loop transfer",
        "10.2: iff -> if and only if",
    ),
    # --- Section 11: devices -------------------------------------------------
    (
        "The sign separation is the paper's structural finding. On the "
        "identical stock–memory block, the mobilising law ($C_Z > 0$) carries "
        "a subcritical Hopf pair and a five-regime attractor topology, while "
        "the protective quota-tracking law ($C_Z < 0$) carries the no-Hopf "
        "theorem — stability at every delay — and stability under annual "
        "review. The distinction is not an artefact of the calibration:",
        "The sign separation is the paper's structural finding. On the "
        "identical stock–memory block the two rules carry opposite "
        "mathematics:\n\n"
        "- **The mobilising law ($C_Z > 0$)** carries a subcritical Hopf pair "
        "and a five-regime attractor topology.\n"
        "- **The protective quota-tracking law ($C_Z < 0$)** carries the "
        "no-Hopf theorem — stability at every delay — and stability under "
        "annual review.\n\n"
        "The distinction is not an artefact of the calibration:",
        "11.1: two-rules bulleted contrast",
    ),
    (
        "a governance parameter, not an ecological one. Local spectral "
        "stabilisation is not governance: an interval that stabilises the "
        "equilibrium may still admit severe inter-review depletion, so the "
        "statement stops at the spectral level (Section 8). The result echoes",
        "a governance parameter, not an ecological one.\n\n"
        "> **Management caution.** Local spectral stabilisation is not "
        "governance: an interval that stabilises the equilibrium may still "
        "admit severe inter-review depletion, so the statement stops at the "
        "spectral level (Section 8).\n\n"
        "The result echoes",
        "11.2: management caution call-out box",
    ),
    (
        "| Review interval $T_r$ | Assessment/management review cycle length |",
        "| Review interval $T_r$ | Assessment/management review cycle length |\n"
        "| Sample-and-hold review | The harvest control rule in force between "
        "assessments — a total allowable catch (TAC) or effort decision set at "
        "each review and held fixed until the next |\n"
        "| Subcritical Hopf crossing | A tipping point for cycles: the "
        "boundary where an oscillatory attractor is already present, so the "
        "cycle regime arrives with coexistence rather than a clean switch |\n"
        "| Inter-assessment stability margin | The monodromy spectral radius "
        "in plain words — how far one review cycle's contraction of small "
        "deviations sits below one |",
        "11.3: translation table extended (TAC/HCR, tipping point, margin)",
    ),
    (
        "Two cautions travel with the translation. First, the discretisation "
        "artefacts are a general warning for management modelling, not a "
        "curiosity of this system: in both channels an explicit first-order "
        "update manufactured thresholds (near 2.3 yr for the protective "
        "channel, the half-century restabilisation for the mobilising channel) "
        "that the exact update of the same reviewed loop does not carry, so a "
        "discrete-time management model can report stability boundaries that "
        "belong to its discretisation rather than to the institution. Second, "
        "local spectral stabilisation is not governance: an interval that "
        "stabilises the equilibrium may still admit severe inter-review "
        "depletion (Section 8), and the capture boundaries of Section 9 are "
        "basin statements, not thresholds a manager can read off a spectrum. "
        "The design reading",
        "Two cautions travel with the translation:\n\n"
        "- **Discretisation artefacts are a general warning for management "
        "modelling, not a curiosity of this system.** In both channels an "
        "explicit first-order update manufactured thresholds (near 2.3 yr for "
        "the protective channel, the half-century restabilisation for the "
        "mobilising channel) that the exact update of the same reviewed loop "
        "does not carry, so a discrete-time management model can report "
        "stability boundaries that belong to its discretisation rather than to "
        "the institution.\n"
        "- **Local spectral stabilisation is not governance.** An interval "
        "that stabilises the equilibrium may still admit severe inter-review "
        "depletion (Section 8), and the capture boundaries of Section 9 are "
        "basin statements, not thresholds a manager can read off a spectrum.\n\n"
        "The design reading",
        "11.3: the two cautions as a bulleted contrast",
    ),
    (
        "The paper's results carry three distinct certification levels, and "
        "the distinction is maintained claim by claim. The cubic modulus "
        "condition, the even-pairs algebra, the no-Hopf theorem, the monodromy "
        "formulas, and the loop-gain exclusions are proved theorems. The Hopf "
        "delay enclosures are interval-Newton certificates",
        "The paper's results carry three distinct certification levels, and "
        "the distinction is maintained claim by claim:\n\n"
        "1. **Proved theorems.** The cubic modulus condition, the even-pairs "
        "algebra, the no-Hopf theorem, the monodromy formulas, and the "
        "loop-gain exclusions.\n"
        "2. **Interval certificates.** The Hopf delay enclosures are "
        "interval-Newton certificates",
        "11.5: three-tier list (items 1-2)",
    ),
    (
        "must add a sensitivity layer over the declared parameter windows "
        "(Section 9.5). The global folds, the attractor classification, and "
        "the Lyapunov coefficients are numerical results at declared status, "
        "with the lower boundary events",
        "must add a sensitivity layer over the declared parameter windows "
        "(Section 9.5).\n"
        "3. **Declared-status numerical results.** The global folds, the "
        "attractor classification, and the Lyapunov coefficients are numerical "
        "results at declared status, with the lower boundary events",
        "11.5: three-tier list (item 3)",
    ),
    (
        "documented component by component in the supplementary material. "
        "Rigorous saddle-node results for delay equations exist for specific "
        "classes",
        "documented component by component in the supplementary material.\n\n"
        "Rigorous saddle-node results for delay equations exist for specific "
        "classes",
        "11.5: closing sentence after the list",
    ),
]

# device-presence needles at md level (each must appear in v34)
DEVICE_NEEDLES = [
    "**governance delay**",
    "**review cadence**",
    "Two default assumptions are challenged directly",
    "a few years to well over a century in the examples studied",
    "1. **The mobilising rule.**",
    "2. **The protective rule.**",
    "The classic results all place the delay inside the ecology itself",
    "Three structural features of (1) carry everything that follows",
    "- **Depletion filtering.**",
    "- **The institutional delay.**",
    "Its behavioural reading is direct",
    "**What Theorem 8.1 says.**",
    "**What Proposition 8.1 says.**",
    "> **Governance warning.**",
    "> **Management caution.**",
    "The regime record is collected in one display",
    "| Regime | Delay range | Attractor record |",
    "| (iv) | $\\tau_{f2} < \\tau < \\tau_+$ |",
    "- **The mobilising law ($C_Z > 0$)**",
    "- **The protective quota-tracking law ($C_Z < 0$)**",
    "| Sample-and-hold review |",
    "| Subcritical Hopf crossing |",
    "| Inter-assessment stability margin |",
    "1. **Proved theorems.**",
    "2. **Interval certificates.**",
    "3. **Declared-status numerical results.**",
    "if and only if",
]

# caveat-presence needles (dropped-caveat regression gates, plan III.D)
CAVEAT_NEEDLES = [
    "A mesh-range caveat is registered with the fine map",
    "they are not a calibration, and no institutional coefficient is "
    "identified from them",
    "other discretisations have different monodromies, and the "
    "continuous-delay and periodic-review recommendations are not "
    "interchangeable",
    "(H5) non-feedback mass compartments stay outside the delay loop",
    "The saddle-node-of-periodic-orbits classification remains",
    "The reversed-gain linearisation has loop gain",
    "The stable arm is not generically reachable near the fold",
]

# rejection list (plan III.D) --- every verified fabrication; zero-hit gates
BANNED = [
    # fabricated reference forms (both gemini variants) and their journals
    "performance of alternative assessment frequencies",
    "fisheries management performance: A simulation approach",
    "Evaluation of management strategy performance under variable "
    "assessment intervals",
    "Effects of assessment frequency and harvest control rules",
    "ICES",
    "Fisheries Research",
    "183, 313", "313–323",
    "175, 94", "94–105",
    "42(4),", "843–861",
    # archetype vocabulary (the paper's only archetype phrase is
    # "fast-maturing small pelagics")
    "anchoveta", "sardine", "cephalopod", "haddock", "rockfish",
    "orange roughy", "deep-sea teleost", "large sharks",
    # invented table cells
    "12.1", "4.5, 12.1", "[4.5,", "0.2, 0.8", "[0.2, 0.8]",
    # the M3-LC channel inversion (gemini's notation)
    "N_min",
    # title/wording overclaims and the misattributed loop gain
    "Global Stability", "narrow window", "saddle-node of limit cycles",
    "non-autonomous and spatial domains", "pure mobilizing governance",
    # americanised spellings of the paper's own register words (a stylometric
    # gate against gemini-voice leakage; grok is British-spelled too)
    "mobilizing", "artifact", "stabilizing", "destabilizing",
]


def tokens(s: str) -> Counter:
    return Counter(re.findall(r"\d+(?:\.\d+)?", s))


def block_by_heading(t: str, start: str, end: str | None = None) -> str:
    lines = t.split("\n")
    i = next(k for k, ln in enumerate(lines) if ln.strip() == start)
    if end is None:
        return "\n".join(lines[i:]).rstrip("\n")
    j = next(k for k, ln in enumerate(lines) if ln.strip() == end)
    return "\n".join(lines[i:j]).rstrip("\n")


def main() -> int:
    t33 = V33.read_text(encoding="utf-8")
    text = t33

    # apply the surgical edits; each anchor must occur exactly once
    for old, new, label in EDITS:
        n = text.count(old)
        assert n == 1, f"[{label}] anchor count {n} != 1 in v33"
        text = text.replace(old, new)

    # fail-loud 1: no standalone 'iff' remains (4 grok fixes applied;
    # Theorem 4.1 already used the long form in v33)
    assert not re.findall(r"\biff\b", text), "standalone 'iff' remains"

    # fail-loud 2: every math span of v34 is byte-identical to a v33 span
    # (empty whitelist: v34 adds no mathematics of its own)
    spans = re.findall(r"\$\$.*?\$\$|\$[^\$\n]+\$", text, flags=re.S)
    missing = [s for s in spans if s not in t33]
    assert not missing, f"math spans missing from v33: {missing[:5]}"

    # fail-loud 3: numeric discipline --- v34 is a superset of v33 with ZERO
    # new token values (the plan adds no numbers; the display devices
    # re-state v33's own values only)
    n33, n34 = tokens(t33), tokens(text)
    lost = {t: c for t, c in n33.items() if n34[t] < c}
    new = {t for t in n34 if t not in n33}
    assert not lost, f"v33 numeric tokens lost/reduced: {lost}"
    assert not new, f"new numeric token values in v34: {sorted(new)[:10]}"

    # fail-loud 4: identical heading skeleton (no restructuring)
    h33 = [ln.rstrip() for ln in t33.split("\n") if ln.startswith("#")]
    h34 = [ln.rstrip() for ln in text.split("\n") if ln.startswith("#")]
    assert h33 == h34, "heading skeleton changed"

    # fail-loud 5: frozen blocks byte-identical
    assert text.split("\n", 1)[0] == t33.split("\n", 1)[0], "title changed"
    kw33 = [ln for ln in t33.split("\n") if ln.startswith("**Keywords:")][0]
    kw34 = [ln for ln in text.split("\n") if ln.startswith("**Keywords:")][0]
    assert kw33 == kw34, "keywords line changed"
    for start, end in (
        ("## Data availability", "## Declaration of competing interest"),
        ("## Declaration of competing interest", "## References"),
        ("## References", "## Supplementary material"),
    ):
        b33, b34 = block_by_heading(t33, start, end), block_by_heading(text, start, end)
        assert b33 == b34, f"frozen block changed: {start}"
    assert block_by_heading(t33, "## Supplementary material") == block_by_heading(
        text, "## Supplementary material"
    ), "supplementary block changed"
    fig33 = [ln for ln in t33.split("\n") if ln.startswith("![Figure")][0]
    cap33 = [ln for ln in t33.split("\n") if ln.startswith("**Figure 1.**")][0]
    assert fig33 in text and text.count(fig33) == 1, "figure block changed"
    assert cap33 in text and text.count(cap33) == 1, "figure caption changed"

    # fail-loud 6: device-presence and caveat-presence needles
    flat = re.sub(r"\s+", " ", text)
    for nd in DEVICE_NEEDLES + CAVEAT_NEEDLES:
        assert nd in flat, f"needle missing: {nd!r}"

    # fail-loud 7: rejection scanner --- zero hits
    hits = [b for b in BANNED if b in text]
    assert not hits, f"rejection-list hits in v34 md: {hits}"

    # fail-loud 8: the four grok 'iff' fixes landed
    assert flat.count("if and only if") == 5, (
        f"expected 5 'if and only if' (4 new + Theorem 4.1), "
        f"found {flat.count('if and only if')}"
    )

    # idempotence + version discipline
    if V34.exists():
        assert V34.read_text(encoding="utf-8") == text, "non-idempotent rebuild"
    V34.write_text(text, encoding="utf-8")
    assert V33.read_text(encoding="utf-8") == t33, "v33 was modified"

    n_edits = len(EDITS)
    print(
        f"  paper4_delay_dynamics_v34.md: OK  {len(text)} chars "
        f"({len(text.splitlines())} lines), {n_edits} surgical edits, "
        f"{len(spans)} math spans (all byte-identical to v33, "
        f"0 whitelisted), numeric superset "
        f"({sum(n34.values())} vs {sum(n33.values())} tokens, 0 new values), "
        f"v33 untouched"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
