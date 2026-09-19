#!/usr/bin/env python3
"""
apply_batch7_wave4_p3.py — fail-loud build of paper3_material_ledgers_v28.md from v27.

Implements the wave-4 P3 items (owner-directed, "cite, don't drop", non-destructive):

  R11 [both]  "horizontal exhaustion estimate" -> "exhaustion-horizon estimate" (§1.1, §11).
  R12 [both]  B = b·M defining clause at first use (§1.1) + §11 token harmonised to b·M.
  R13 [claude] Deep-time scoping sentence reconciling §1.1's regeneration claims.
  R14 [claude] Mt/kt harmonisation in §6.5.3 (arithmetic unchanged).
  R15 [claude] §9 hand-off projection: six right-hand sides, A^geo restored to the list.
  R16 [grok]  μ, ν, ρ defining clause at §2.2 first use + harmonised §9 gloss; retirement
              fraction re-lettered ρ -> ρ_P; Theorem 15's hybrid state/flux re-lettered
              χ/η; Definition 6's A_0 declared local; notation table moved to the head of
              §2 and extended with the previously omitted symbols (the notation pass).
  Docket      Demotions (status relabels on the unchanged 1–20 counter, numbers preserved
              so the supplementary statement inventory still resolves by number):
              Thm 2 -> Remark 2, Thm 3 -> Lemma 3, Thm 4 -> Proposition 4, Thm 6 ->
              Proposition 6, Lemma 16 -> Remark 16, Thm 17 -> Proposition 17, Thm 18 ->
              Proposition 18, Thm 20 -> Proposition 20; every cross-reference updated.
  Docket      The four-row (2) and seven-compartment (Theorem 8) incidence matrices
              displayed, with mechanical column-sum checks.
  Docket      The R0 split: R_ext / R_K / R_frozen (union symbol retained).
  Docket      Theorem 14's E >= 0 hypothesis + the constant-flux comparison labelled.
  Docket      §9 field-difference reconciliation, recomputed at the same (N, A, U):
              difference = κ_A K − γ_U U  (≈ 0.535 at quasi-rest U; 5.000 = κ_A K at
              U = 0), replacing the three inconsistent readings; units fixed.
  Docket      Classification-matrix Θ_F cell reconciled with §6.5.4.
  Docket      USGS single-vintage pin (MCS 2026 declared the pinned source of record).
  Docket      §11 no longer re-argues the weak/strong regimes (consensus 7).
  Docket      Three uncited companions cited (in-text + References, fresh letters D/E/F).
  R17 [both]  (a) Indo-Gangetic daggered row stays first, caveat adjacent and explicit;
              (b) fisheries headline cohort stays in place (KEEP-IN-PLACE) with the
              v4.66 broad-cohort reading and S5's retraction cross-referenced at the
              headline site.  Both recorded in the text.
  Length      Bounded §1.1 strip (elevator restatement, no-drift triple) + §11 tightening;
              remainder registered with its reason.
  Housekeeping  Supplementary pointer v6 -> v7.

Non-destructive: no frozen verdict, score, or table value changes. All pre-existing
markdown table rows are byte-identical except the classification matrix's Θ_F cell
(the endorsed contradiction fix) and the notation table's moved/extended cross-reference
cells; the two incidence displays are new content. Every edit asserts its anchor occurs
exactly once; every mechanical check fails loudly.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "arena agent 1", "paper rewrites",
                   "paper3_material_ledgers_v27.md")
DST = os.path.join(HERE, "..", "arena agent 1", "paper rewrites",
                   "paper3_material_ledgers_v28.md")


def sub1(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise SystemExit(f"FAIL [anchor {label}]: expected exactly 1 occurrence, found {n}")
    return text.replace(old, new)


# ---------------------------------------------------------------- incidence matrices
SBLOCK = r"""$$S_{\mathrm{block}} =
\begin{pmatrix}
1 & -1 & -1 & 0 & 0 & 0 & 0 & 0 \\
-1 & 1 & 0 & -1 & 1 & 1 & -1 & 0 \\
0 & 0 & 0 & 0 & 0 & -1 & 1 & -1 \\
0 & 0 & 0 & 1 & -1 & 0 & 0 & 0
\end{pmatrix}.$$"""

ST7 = r"""$$S_{\mathcal{T}} =
\begin{pmatrix}
1 & -1 & -1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1-\alpha & 0 & 0 & 0 & 0 & 1 & -1 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1-\rho_P & -1 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\
0 & 0 & \alpha & 1 & -1 & 0 & 0 & 0 & \rho_P & 0 \\
-1 & 1 & 0 & -1 & 1 & 1 & -1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & -1 & 1 & -1 & 0 & 0
\end{pmatrix}.$$"""


def parse_matrix(block):
    """Extract the numeric/symbolic entries of a pmatrix block as a list of rows."""
    body = block.split(r"\begin{pmatrix}", 1)[1].split(r"\end{pmatrix}", 1)[0]
    rows = []
    for line in body.split(r" \\"):
        line = line.strip()
        if not line:
            continue
        rows.append([tok.strip() for tok in line.split("&")])
    return rows


def eval_token(tok, alpha, rho_p):
    tok = tok.replace(" ", "")
    if tok in ("1", "-1", "0"):
        return int(tok)
    if tok == r"\alpha":
        return alpha
    if tok == r"\rho_P":
        return rho_p
    if tok == r"1-\alpha":
        return 1 - alpha
    if tok == r"1-\rho_P":
        return 1 - rho_p
    raise SystemExit(f"FAIL: unparseable matrix token {tok!r}")


def column_sums(block, alpha=0.3, rho_p=0.45):
    rows = parse_matrix(block)
    ncol = len(rows[0])
    if any(len(r) != ncol for r in rows):
        raise SystemExit("FAIL: ragged matrix rows")
    sums = [sum(eval_token(r[j], alpha, rho_p) for r in rows) for j in range(ncol)]
    return rows, sums


def main():
    t = open(SRC, encoding="utf-8").read()

    # ---------------- version log ----------------
    old_log_start = "*Version log (v27).*"
    idx = t.find(old_log_start)
    if idx != t.find("\n*Version log") + 1 or t.count(old_log_start) != 1:
        raise SystemExit("FAIL: v27 version log anchor")
    log_end = t.find("\n\n## Abstract", idx)
    if log_end == -1:
        raise SystemExit("FAIL: version log terminator")
    new_log = (
        "*Version log (v28).* Implements the wave-4 items of the joint-audit evaluation's P3 "
        "remaining-points list (R11–R17 plus the structural docket), owner-directed as "
        "cite-not-drop and non-destructive. (R11) \"horizontal exhaustion estimate\" is "
        "corrected to \"exhaustion-horizon estimate\" at both sites (Section 1.1, Section 11). "
        "(R12) The scalar reading $B = b\\cdot M$ of Section 1.1 now carries its defining clause "
        "(the aggregate regeneration flow: $b$ the per-unit-mass regeneration rate, $M$ the "
        "natural-block mass; letters local to the introduction, since from Section 2.2 on $B$ "
        "names the gross turnover $R + T$), and Section 11's token is harmonised to $b\\cdot M$. "
        "(R13) The deep-time clause of Section 1.1 is scoped: slow regeneration is a statement "
        "about geological donors and mineral stocks, while the tabulated regenerative "
        "compartments renew on human timescales — the contradiction is reconciled, the claim "
        "kept. (R14) Section 6.5.3's world figures are harmonised to kt ($74{,}000{,}000$ kt = "
        "$74{,}000$ Mt against $240{,}000$ kt/yr; arithmetic unchanged). (R15) Section 9's "
        "hand-off projection lists the closed block's six right-hand sides — $A^{\\mathrm{geo}}$ "
        "restored to the list. (R16, the notation pass) $\\mu, \\nu, \\rho$ receive a defining "
        "clause at their Section 2.2 first use and a harmonised Section 9 gloss; the "
        "product-retirement fraction is re-lettered $\\rho_P$ (freeing $\\rho$ for the price "
        "parameter); Conditional Theorem 15's hybrid state and flux are re-lettered $\\chi$ and "
        "$\\eta$; Definition 6's $A_0$ is declared local to Section 7; and the notation table "
        "moves to the head of Section 2, extended with the previously omitted symbols ($b$, "
        "$h_m/r_m$, $B$-as-biomass, $A_0$, $G_0$, $P$, $\\varepsilon$, $\\Theta$ vs $\\Theta_F$, "
        "$\\tau$, $d$, $K_{\\mathrm{maint}}$, $\\lambda$, $\\nu$, $E$, $\\alpha$, $r$). (Docket: "
        "theorem inflation) The eight audited inflations are demoted as status relabels on the "
        "unchanged 1–20 statement counter — Theorem 2 $\\to$ Remark 2, Theorem 3 $\\to$ Lemma 3, "
        "Theorem 4 $\\to$ Proposition 4, Theorem 6 $\\to$ Proposition 6, Lemma 16 $\\to$ Remark "
        "16, Theorem 17 $\\to$ Proposition 17, Theorem 18 $\\to$ Proposition 18, Theorem 20 $\\to$ "
        "Proposition 20 — with every cross-reference updated; retained theorems keep their "
        "numbers, so the supplementary statement inventory (v7) still resolves every reference "
        "by number, with a recorded status-word offset. (Docket: incidence display) The "
        "four-row block incidence of (2) (whose row sums read off $\\dot M = -qEN - "
        "C^{A,\\mathrm{lim}}$) and the seven-compartment incidence of Theorem 8 are displayed, "
        "with column-sum checks. (Docket: $\\mathcal{R}_0$ split) Theorem 13's rest set is split "
        "into $\\mathcal{R}_{\\mathrm{ext}}$, $\\mathcal{R}_K$, and $\\mathcal{R}_{\\mathrm{frozen}}$ "
        "(the union symbol $\\mathcal{R}_0$ retained for the two geochemical families), and "
        "Theorem 12(iii)'s misuse is corrected. (Docket: Theorem 14) The $E \\ge 0$ hypothesis "
        "is stated, and the constant-flux comparison is labelled as a comparison flux, not a "
        "donor-limited primitive. (Docket: Section 9 reconciliation) Reason 2's field "
        "difference is recomputed with both vector fields written at the same "
        "$(N, A^{\\mathrm{act}}, U)$: $\\kappa_A K - \\gamma_U U$ — approximately $0.535$ stock "
        "units per year at the working point's quasi-rest detritus level ($\\gamma_U U = T^* "
        "\\approx 4.47$) and $\\kappa_A K = 5.000$ at $U = 0$ — replacing the three inconsistent "
        "readings ($4.47$ / $O(\\kappa_A K) = O(5)$ / $4.652$ vs $-0.348$); the $c$ and $B^*$ "
        "units are corrected to stock units per year. (Docket: $\\Theta_F$) The classification "
        "matrix's fisheries cell now matches Section 6.5.4 (gross-loss analogue only, not a "
        "member of the hierarchy). (Docket: USGS pin) MCS 2026 is declared the single pinned "
        "source of record, the carried pin anchors are displayed, and the per-row re-pin is "
        "registered as the open data action. (R17, owner decisions, both KEEP-IN-PLACE) The "
        "Indo-Gangetic daggered row stays first with its do-not-reuse caveat made adjacent at "
        "the table; the fisheries headline cohort stays in place, with the v4.66 "
        "broad-cohort reading stated as the primary public-release comparison and S5's "
        "non-reproducibility record explicitly cross-referenced at the headline site. (Docket: "
        "companions) The three companion studies — delay-dynamics, review screen, assessment "
        "separation — carry in-text citations (fresh letters D, E, F) and reference entries. "
        "(Docket: Section 11) The conclusion no longer re-argues the weak/strong regimes and "
        "closes on the inventory. (Docket: length) The bounded Section 1.1 strip (elevator "
        "restatement, no-drift triple statement) plus the Section 11 tightening remove the "
        "audited redundancy; the remainder of the 21k-to-12k reduction is registered with its "
        "reason (the restructure-level cuts would remove content the auditors called the "
        "publishable core). Housekeeping: the supplementary pointer cites v7. No frozen "
        "verdict, score, or table value changes: all pre-existing table rows are "
        "byte-identical except the classification matrix's $\\Theta_F$ cell (the endorsed "
        "contradiction fix) and the notation table's moved/extended cross-reference cells; the "
        "two incidence displays are new content."
    )
    t = t[:idx] + new_log + t[log_end:]

    # ---------------- §1.1: R12 defining clause ----------------
    t = sub1(t,
        "The scalar reading $B = b\\cdot M$ against consumption is the weak-sustainability "
        "flow check: does the cycle close in aggregate?",
        "The scalar reading $B = b\\cdot M$ — the aggregate regeneration flow, with $b$ the "
        "per-unit-mass regeneration rate and $M$ the natural-block mass; letters local to the "
        "introduction, since from Section 2.2 on $B$ names the gross turnover $R + T$ while $M$ "
        "keeps the natural-block-mass reading — against consumption is the weak-sustainability "
        "flow check: does the cycle close in aggregate?",
        "r12-def")

    # ---------------- §1.1: no-drift triple dedup (length item) ----------------
    t = sub1(t,
        "a timescale longer than it is taken. A static $C \\le B$ can be re-satisfied on a "
        "path that is already committed to failure. The scenario-conditioned hitting time of "
        "Section 6.5.2 exists to give the drift a horizon. The balance is a rate condition, "
        "and it also has to hold as a growth condition: a $C \\le B$ satisfied at each "
        "instant does not by itself rule out the path on which consumption or population "
        "grows faster than the regeneration and substitution available — the same no-drift "
        "requirement. The reserve classification itself encodes this.",
        "a timescale longer than it is taken. The scenario-conditioned hitting time of "
        "Section 6.5.2 exists to give the drift a horizon. The reserve classification itself "
        "encodes this.",
        "s11-nodrift")

    # ---------------- §1.1: R11 site 1 ----------------
    t = sub1(t,
        "so a horizontal exhaustion estimate built on a reserve figure carries",
        "so an exhaustion-horizon estimate built on a reserve figure carries",
        "r11-s1")

    # ---------------- §1.1: R13 deep-time scoping ----------------
    t = sub1(t,
        "On human-relevant timescales substitution is the dominant term; natural "
        "regeneration acts far more slowly — often on deep-time scales — and is included for "
        "physical completeness rather than as a co-equal mechanism (Daly, 1990).",
        "On human-relevant timescales substitution is the dominant term; natural "
        "regeneration acts far more slowly — often on deep-time scales — and is included for "
        "physical completeness rather than as a co-equal mechanism (Daly, 1990). The "
        "deep-time clause is scoped to the slow compartments — geological donors and mineral "
        "stocks, whose renewal runs on deep time. The regenerative compartments this "
        "article's applied record tabulates renew on human timescales — a crop within a "
        "season, an aquifer within years to decades, a fish stock within years — so for them "
        "regeneration is a co-equal or dominant term, and the regime question is decided by "
        "the rate of use relative to that renewal, not by any deep-time regeneration.",
        "r13-scope")

    # ---------------- §1.1: weak/strong framed as a reading (joint (B) block) ----------------
    t = sub1(t,
        "Weak and strong sustainability are not competing hypotheses but two regimes of one "
        "dynamic system, distinguished not by whether substitution alone keeps pace with "
        "depletion but by whether the material cycle can be closed at the rate of use.",
        "Weak and strong sustainability are not competing hypotheses but two regimes of one "
        "dynamic system, distinguished not by whether substitution alone keeps pace with "
        "depletion but by whether the material cycle can be closed at the rate of use — a "
        "reading of the two regimes developed for the ledger, not the received distinction of "
        "the literature, which turns on the substitutability of natural capital (Neumayer, "
        "2013; Ekins et al., 2003).",
        "s11-weakstrong-reading")

    # ---------------- §1.1: elevator restatement compression (length item) ----------------
    t = sub1(t,
        "The yield-inflation sense of the productivity illusion is the wear phase. Measured "
        "yield stays up because the supporting pool is being drawn down, and nothing in the "
        "yield series records the drawdown.",
        "The yield-inflation sense is the wear phase: measured yield stays up while nothing "
        "in the yield series records the drawdown.",
        "s11-elevator")

    # ---------------- §1.1: thin antecedent ----------------
    t = sub1(t,
        "The size of the pool is a property of the resource. Whether that drawdown is "
        "recoverable is a property of the rate.",
        "The size of the pool is a property of the resource. Whether a drawdown is "
        "recoverable is a property of the rate.",
        "s11-antecedent")

    # ---------------- §2.2: companion citation at first mention ----------------
    t = sub1(t,
        "These donor primitives instantiate one of three recharge laws that appear across "
        "this article and the companion analyses (each under review); the three are distinct "
        "objects, tabulated once so that none is silently substituted for another:",
        "These donor primitives instantiate one of three recharge laws that appear across "
        "this article and the companion delay-dynamics analysis (Author, D., et al., in "
        "review); the three are distinct objects, tabulated once so that none is silently "
        "substituted for another:",
        "companion-d-table")

    # ---------------- §2.2: R16 mu/nu/rho defining clause ----------------
    t = sub1(t,
        "Under the institutional-failure specialization ($\\mu = \\nu = \\rho = 0$, "
        "$C^A = 0$) the closed natural block is",
        "Under the institutional-failure specialization ($\\mu = \\nu = \\rho = 0$ and "
        "$C^A = 0$ — the product, waste, and price parameters $\\mu, \\nu, \\rho$ of the "
        "unreduced ledger, its macroeconomic-feedback, recycling, and price-response "
        "channels, set to zero together with the mining intensity $C^A$; the parameters are "
        "glossed at their Section 5.4 site) the closed natural block is",
        "r16-munurho")

    # ---------------- §2.2: four-row incidence display ----------------
    t = sub1(t,
        "the existence clause behind every 'classical solution' statement below.\n\n"
        "When product, waste, and the inert sink are restored",
        "the existence clause behind every 'classical solution' statement below.\n\n"
        "The incidence discipline of Section 2.1, written out for the closed block, is the "
        "four-row block incidence — rows $(N, A^{\\mathrm{act}}, A^{\\mathrm{geo}}, U)$, "
        "columns gross regeneration $rNs$, density-dependent return $rN^2 s/K$, harvest "
        "$qEN$, uptake $T = \\kappa_A N s$, detritus return $\\gamma_U U$, geological "
        "recharge $e_{GA}$, geological return $e_{AG}$, mining $C^{A,\\mathrm{lim}}$:\n"
        + SBLOCK + "\n"
        "Every column is a two-compartment transfer or a block-boundary export: the six "
        "internal columns sum to zero, and the two exports — harvest and mining — carry the "
        "column sums $-1$ each, so summing the four rows reads off $\\dot M = -qEN - "
        "C^{A,\\mathrm{lim}}$, the mass identity proved as Theorem 7, directly from the "
        "display (under the institutional-failure specialization the mining column is "
        "inactive, $C^A = 0$). The harvest column is written at the declared $\\alpha = 0$ "
        "routing, under which harvest exits the block; a detritus-routed fraction "
        "$\\alpha > 0$ moves $\\alpha$ into the $U$ entry of that column and reduces the "
        "block export to $(1-\\alpha)qEN$ — the full-ledger routing displayed in Section "
        "4.2.\n\n"
        "When product, waste, and the inert sink are restored",
        "s22-incidence")

    # ---------------- §2.2: companion citation at the (Z, E) pair ----------------
    t = sub1(t,
        "The pair is the registered object of the companion delay-dynamics analysis (under "
        "review; eq. (1) and Section 2.4 of that analysis) and is not analysed in this "
        "article.",
        "The pair is the registered object of the companion delay-dynamics analysis "
        "(Author, D., et al., in review; eq. (1) and Section 2.4 of that analysis) and is "
        "not analysed in this article.",
        "companion-d-zepair")

    # ---------------- §2.3: retirement fraction re-lettered rho -> rho_P ----------------
    t = sub1(t,
        "routed to $U$ and retirement fraction $\\rho \\in [0,1]$ returning to $U$ rather "
        "than $W$",
        "routed to $U$ and retirement fraction $\\rho_P \\in [0,1]$ returning to $U$ rather "
        "than $W$",
        "rhoP-intro")
    t = sub1(t,
        "$$\\dot z = S(\\alpha, \\rho)\\, v(z, u),",
        "$$\\dot z = S(\\alpha, \\rho_P)\\, v(z, u),",
        "rhoP-zdot")
    t = sub1(t,
        "$$S(\\alpha, \\rho) =",
        "$$S(\\alpha, \\rho_P) =",
        "rhoP-matrix-head")
    t = sub1(t,
        "0 & 1 & \\alpha & -1 & 0 & 0 & 0 & \\rho \\\\",
        "0 & 1 & \\alpha & -1 & 0 & 0 & 0 & \\rho_P \\\\",
        "rhoP-matrix-u")
    t = sub1(t,
        "0 & 0 & 0 & 0 & 0 & 0 & 0 & 1-\\rho\n\\end{pmatrix}",
        "0 & 0 & 0 & 0 & 0 & 0 & 0 & 1-\\rho_P\n\\end{pmatrix}",
        "rhoP-matrix-w")
    t = sub1(t,
        "the constant splits $\\alpha$ and $\\rho$, the compartment set,",
        "the constant splits $\\alpha$ and $\\rho_P$, the compartment set,",
        "rhoP-splits")

    # ---------------- §2.6: demotion Theorem 2 -> Remark 2 ----------------
    t = sub1(t,
        "**Theorem 2 (Registered-family support-saturated identity).**",
        "**Remark 2 (Registered-family support-saturated identity).**",
        "demote-thm2")
    t = sub1(t,
        "readout of the Theorems 1–2 family",
        "readout of the Theorem 1 and Remark 2 family",
        "xref-12-family")

    # ---------------- notation table: remove from §2.6 ----------------
    nt_start = "**Notation.** One letter carries one sort wherever a computation is displayed"
    nt_end = "| $\\theta$ | declared constitutive parameter vector; sink-generation fraction " \
             "$\\theta_K$ (subscripted) | §2.1, eq. (1); §2.4 |"
    i0 = t.find(nt_start)
    i1 = t.find(nt_end)
    if i0 == -1 or i1 == -1 or i1 < i0:
        raise SystemExit("FAIL: notation table block not found")
    i1 += len(nt_end)
    # swallow the trailing blank line so §2.6 closes cleanly
    if t[i1:i1 + 2] == "\n\n":
        i1 += 1
    t = t[:i0] + t[i1:]

    # ---------------- notation table: extended, at the head of §2 ----------------
    new_table = (
        "**Notation.** One letter carries one sort wherever a computation is displayed; "
        "section-local aliases are declared where they occur, and the incidence operator is "
        "never written $N$ (which is reserved for the living stock). The table sits at the "
        "head of Section 2 so that every alias is declared before use:\n\n"
        "| Symbol | Meaning | Where |\n"
        "|---|---|---|\n"
        "| $N$ | living stock; nutrient stock (local to §2.4) | §2.2; §2.4 |\n"
        "| $S_{\\mathcal{T}}$ | typed stoichiometric (incidence) operator | §2.1, Lemma 3, "
        "Proposition 4, Theorem 5, Theorem 8 |\n"
        "| $v$ | non-negative primitive flux vector | §2.1 |\n"
        "| $S$ | moiety readout $S = Cx$ | Lemma 3, §6 |\n"
        "| $s$ | support factor $A^{\\mathrm{act}}/(A^{\\mathrm{act}}+A_0)$ | §2.2 |\n"
        "| $\\sigma$ | donor fraction $A^{\\mathrm{geo}}/(A^{\\mathrm{geo}}+A_{g0})$ | §2.2 |\n"
        "| $\\varsigma$ | noise scale of the stochastic surrogates | §7 |\n"
        "| $M$ | natural-block mass $N + A^{\\mathrm{act}} + A^{\\mathrm{geo}} + U$ | "
        "Theorems 7, 14 |\n"
        "| $\\widehat{M}$ | demand-coverage matrix of the physical deficit | §5.4 |\n"
        "| $K$ | carrying capacity; sink stock (local to §2.4); maintainability kernel "
        "$K_{\\mathrm{maint}}$ (subscripted) | §2.2; §2.4; §6.3 |\n"
        "| $T$ | gross uptake $\\kappa_A N s$; finite horizon (local to each statement) | "
        "§2.2; Theorems 1, 5 |\n"
        "| $C$ | moiety-composition matrix; operative extraction-law readout; mining "
        "intensity $C^A$ | Lemma 3; §5.4; §2.2 |\n"
        "| $B$ | $R + T$; barriers (local to §3.1); aggregate regeneration flow "
        "$b \\cdot M$ (local to §1.1); fisheries biomass $B_t$ and reference $B_{\\min}$ "
        "(local to §6.5.2, §7.5) | §2.2; §3.1; §1.1; §6.5.2 |\n"
        "| $b$ | boundary-transfer term; service balance $b_i$ (subscripted); specific "
        "regeneration rate (local to §1.1) | Lemma 3, Proposition 4, Theorem 5; §5.1; §1.1 |\n"
        "| $R$ | net regeneration; log-margin $R_B$ (local to §6.5.4) | §2.2; §6.5.4 |\n"
        "| $r$ | intrinsic growth rate; net boundary inflow $r_m$ (subscripted, §3.3) | "
        "§2.2; §2.6; §3.3 |\n"
        "| $G$ | geological pool (scaffold); reserves (local to §6.5.3, §7.6); donor stock "
        "$G_0$ (subscripted) | §2.3; §6.5.3; §9 |\n"
        "| $I$ | inert sink; boundary input $I_N$ (subscripted) | §2.2; §2.4 |\n"
        "| $z$ | six-compartment state (local to §2.3) | §2.3 |\n"
        "| $h$ | harvest primitive; net boundary outflow $h_m$ (subscripted, §3.3); "
        "geometric-Brownian drift (local to §7.5) | §2.3; §3.3; §7.5 |\n"
        "| $x$ | ledger state | §2.1, Lemma 3, Proposition 4, Theorem 5 |\n"
        "| $y$ | declared boundary states feeding the primitive fluxes | §2.1, eq. (1) |\n"
        "| $\\theta$ | declared constitutive parameter vector; sink-generation fraction "
        "$\\theta_K$ (subscripted); parameter set $\\Theta$ and fisheries pressure time "
        "$\\Theta_F$ (distinct objects) | §2.1, eq. (1); §2.4; §6.4, §6.5.4 |\n"
        "| $E$ | extraction effort, $E \\ge 0$ along classical solutions | §2.2; §4.5; "
        "Theorem 14 |\n"
        "| $\\alpha$ | harvest routing fraction; directional support fraction "
        "$\\alpha_{\\mathrm{reg}}$ (subscripted) | §2.2–§2.3, §4.2; §5.3 |\n"
        "| $\\rho_P$ | product-retirement fraction routing $r_P$ to $U$ versus $W$ "
        "(re-lettered from $\\rho$) | §2.3; §4.3; §4.4; §8.1 |\n"
        "| $\\mu, \\nu, \\rho$ | product, waste, and price parameters of the unreduced "
        "ledger (zero in the single-resource specialization); $\\mu$ also the growth "
        "parameter of Theorem 1 and the drift of the §7 surrogates; $\\nu$ also the "
        "inverse-Gaussian mean (local to §7.3) | §2.2; §5.4; §9 |\n"
        "| $\\varepsilon$ | drift bracket (Proposition 17); probabilistic level (§6.4); "
        "resource-threshold fraction (§6.5.2, §7.6); donor-draw diagnostic "
        "$\\varepsilon_G$ (subscripted); slack (§10.1) | §6.2; §6.4; §6.5.2; §9; §10.1 |\n"
        "| $\\tau$ | hitting and exit times ($\\tau_B$, $\\tau_m^{\\pm}$, "
        "$\\tau_{\\mathrm{exit}}$) | §3.6; §6.3 |\n"
        "| $d$ | disturbance (§2.1); demand vector (§5.2); drift distance (local to §7.3) | "
        "§2.1; §5.2; §7.3 |\n"
        "| $A_0$ | half-saturation constant (§2.2); latest observed anomaly (local to "
        "§7.2–§7.4) | §2.2; §7.2 |\n"
        "| $\\lambda$ | inverse-Gaussian shape parameter | §7.3 |\n"
        "| $\\chi, \\eta$ | hybrid state and primitive-flux vector of Conditional Theorem "
        "15 (re-lettered from $r$, $\\nu$) | §4.8 |\n"
        "| $P$ | product compartment; production rate (local to §6.5.3, §7.6) | "
        "§2.2–§2.3; §6.5.3 |\n"
    )
    t = sub1(t,
        "## 2. The Typed Primitive Ledger\n\n### 2.1 Typed stocks, primitive fluxes, and "
        "the incidence discipline",
        "## 2. The Typed Primitive Ledger\n\n" + new_table + "\n### 2.1 Typed stocks, "
        "primitive fluxes, and the incidence discipline",
        "notation-table-move")

    # ---------------- §3.1: Prop 2 comparison-flux label ----------------
    t = sub1(t,
        "on the closed ledger (2), constant extraction at a rate exceeding regeneration is "
        "exactly mass-balanced (Theorem 7 states the identity)",
        "on the closed ledger (2), constant extraction at a rate exceeding regeneration — a "
        "comparison flux, not a donor-limited primitive of the ledger's own discipline — is "
        "exactly mass-balanced (Theorem 7 states the identity)",
        "prop2-comparison")

    # ---------------- demotions: labels ----------------
    t = sub1(t,
        "**Theorem 3 (Flux reconstruction under a typed balance law).**",
        "**Lemma 3 (Flux reconstruction under a typed balance law).**",
        "demote-thm3")
    t = sub1(t,
        "**Theorem 4 (Conservation-law reduction).**",
        "**Proposition 4 (Conservation-law reduction).**",
        "demote-thm4")
    t = sub1(t,
        "**Theorem 6 (Finite exhaustion under uniform negative drift).**",
        "**Proposition 6 (Finite exhaustion under uniform negative drift).**",
        "demote-thm6")
    t = sub1(t,
        "**Lemma 16 (Exact specialization deficit identity).**",
        "**Remark 16 (Exact specialization deficit identity).**",
        "demote-lem16")
    t = sub1(t,
        "**Theorem 17 (Local threshold-horizon bracket).**",
        "**Proposition 17 (Local threshold-horizon bracket).**",
        "demote-thm17")
    t = sub1(t,
        "**Theorem 18 (Inverse-Gaussian first passage).**",
        "**Proposition 18 (Inverse-Gaussian first passage — a standard fact, stated for "
        "notation).**",
        "demote-thm18")
    t = sub1(t,
        "**Theorem 20 (Geometric-Brownian correction).**",
        "**Proposition 20 (Geometric-Brownian correction — a standard fact, stated for "
        "notation).**",
        "demote-thm20")

    # ---------------- demotions: cross-references ----------------
    t = sub1(t,
        "*Proof.* By Theorem 3, $\\dot S_m = (C S_{\\mathcal{T}} v + Cb)_m$.",
        "*Proof.* By Lemma 3, $\\dot S_m = (C S_{\\mathcal{T}} v + Cb)_m$.",
        "xref-lem3-thm5proof")
    t = sub1(t,
        "this is the hybrid variant of Theorem 4, retained at its own conditional status",
        "this is the hybrid variant of Proposition 4, retained at its own conditional status",
        "xref-prop4-hybrid")
    t = sub1(t,
        "the composition matrix $C$ of Theorem 3, a different object from the coverage "
        "vector $C(t)$",
        "the composition matrix $C$ of Lemma 3, a different object from the coverage vector "
        "$C(t)$",
        "xref-lem3-s54")
    t = sub1(t,
        "Its companion is the one-sided exhaustion theorem of Section 3.6, whose "
        "counterexample",
        "Its companion is the one-sided exhaustion proposition of Section 3.6, whose "
        "counterexample",
        "xref-prop6-s62")
    t = sub1(t,
        "Theorem 18 applies. Under the Stratonovich convention",
        "Proposition 18 applies. Under the Stratonovich convention",
        "xref-prop18-proof")
    t = sub1(t,
        "holds for every trajectory of either the specialized ledger or the reduced core "
        "(Lemma 16).",
        "holds for every trajectory of either the specialized ledger or the reduced core "
        "(Remark 16).",
        "xref-rem16-s9")
    t = sub1(t,
        "carries its own finite-time scope (Theorems 1–2: the replacement is pointwise",
        "carries its own finite-time scope (Theorem 1 and Remark 2: the replacement is "
        "pointwise",
        "xref-12-s9")
    t = sub1(t,
        "(iii) The first-passage theorems of Section 7 concern declared stochastic "
        "surrogates",
        "(iii) The first-passage propositions of Section 7 concern declared stochastic "
        "surrogates",
        "xref-s7props")

    # ---------------- §4.2: seven-compartment incidence display ----------------
    t = sub1(t,
        "The seven-compartment incidence claimed by Theorem 8 is not displayed separately: "
        "it is the pattern of the displayed six-compartment $S(\\alpha,\\rho)$ of Theorem 9 "
        "with the inert column (no outflow) appended and the harvest column split by "
        "$(\\alpha, 1-\\alpha)$.",
        "The seven-compartment incidence claimed by Theorem 8 — in the compartment order of "
        "its statement, with the closed block's primitive fluxes, the pattern of the "
        "displayed six-compartment $S(\\alpha, \\rho_P)$ of Theorem 9 with the inert column "
        "(no outflow from the inert compartment) appended and the harvest column split by "
        "$(\\alpha, 1-\\alpha)$ — is displayed here. Rows $(N, P, W, I, U, A^{\\mathrm{act}}, "
        "A^{\\mathrm{geo}})$; columns gross regeneration, density-dependent return, harvest, "
        "uptake, detritus return, $e_{GA}$, $e_{AG}$, mining (to product), product "
        "retirement, inert-bound transfer (waste $\\to$ inert):\n"
        + ST7 + "\n"
        "Every column is a two-compartment transfer under the unit-sum routing constraints, "
        "so $\\mathbf{1}^\\top S_{\\mathcal{T}} = 0$ column by column — Theorem 8's "
        "conservation, at sight — and the natural-block rows $(N, U, A^{\\mathrm{act}}, "
        "A^{\\mathrm{geo}})$ reproduce the four-row display of Section 2.2, with the harvest "
        "column now carrying its full routing ($\\alpha$ to $U$, $1-\\alpha$ to $P$) instead "
        "of the block-export convention of the $\\alpha = 0$ corner. The waste-routed mining "
        "variant appends a column with $-1$ in the $A^{\\mathrm{geo}}$ row and $+1$ in the "
        "$W$ row under the same pattern. The retirement split $(\\rho_P, 1-\\rho_P)$ and the "
        "inert-bound source (the absorbing stock $W$) are declared routing choices of this "
        "displayed instance; the incidence pattern — every primitive a two-compartment "
        "transfer, column sums zero — is the theorem's content, and no classification "
        "depends on the declared choices.",
        "s42-incidence")

    # ---------------- §4.3 / §4.4: rho_P in the proofs ----------------
    t = sub1(t,
        "$\\rho r_P - r_P + (1-\\rho)r_P = 0$",
        "$\\rho_P r_P - r_P + (1-\\rho_P)r_P = 0$",
        "rhoP-thm9proof")
    t = sub1(t,
        "at $U = 0$, $\\dot U = m + \\alpha h + \\rho r_P \\ge 0$",
        "at $U = 0$, $\\dot U = m + \\alpha h + \\rho_P r_P \\ge 0$",
        "rhoP-thm11-u")
    t = sub1(t,
        "at $W = 0$, $\\dot W = (1-\\rho)r_P \\ge 0$",
        "at $W = 0$, $\\dot W = (1-\\rho_P)r_P \\ge 0$",
        "rhoP-thm11-w")

    # ---------------- §4.5: Theorem 12(iii) R_ext ----------------
    t = sub1(t,
        "(iii) $N = 0$ forces $R = T = 0$ and reduces to the extinction family "
        "$\\mathcal{R}_0$ of Theorem 13.",
        "(iii) $N = 0$ forces $R = T = 0$ and reduces to the extinction family "
        "$\\mathcal{R}_{\\mathrm{ext}}$ of Theorem 13.",
        "r0-thm12iii")

    # ---------------- §4.6: Theorem 13 R0 split ----------------
    t = sub1(t,
        "**Theorem 13 (Vanishing-extraction rest set).** *With vanishing extraction "
        "($E \\equiv 0$), the rest points of the closed natural block (2) are exactly the "
        "two families*\n"
        "$$\\mathcal{R}_0 = \\bigl\\{ N = 0,\\ U = 0,\\ A^{\\mathrm{act}} = "
        "A^{\\mathrm{eq,intrinsic}}\\,\\sigma(A^{\\mathrm{geo}}),\\ A^{\\mathrm{geo}} \\ge 0 "
        "\\bigr\\} \\cup \\bigl\\{ N = K,\\ U = \\kappa_A K s/\\gamma_U,\\ "
        "A^{\\mathrm{act}} = A^{\\mathrm{eq,intrinsic}}\\,\\sigma,\\ A^{\\mathrm{geo}} \\ge 0 "
        "\\bigr\\},$$\n"
        "*where in the second family $s = A^{\\mathrm{act}}/(A^{\\mathrm{act}} + A_0)$ is "
        "evaluated at the solution — together with the frozen-biomass face $\\{(N, 0, 0, 0) "
        ": N \\ge 0\\}$, on which $s = 0$ identically and the biomass is frozen at its "
        "initial value. With $E > 0$ constant, no *interior* rest point (with $N_* > 0$) "
        "exists (Theorem 12); the extinction face of this set persists at positive effort, "
        "because extraction $qEN$ vanishes identically at $N = 0$, and it is a boundary rest "
        "rather than an interior one (Section 4.6). If $A_{g0} = 0$ and $\\sigma \\equiv 1$ "
        "is imposed for $A^{\\mathrm{geo}} > 0$, the $\\mathcal{R}_0$ ray is $A^{\\mathrm{act}} "
        "= A^{\\mathrm{eq,intrinsic}}$, $A^{\\mathrm{geo}} > 0$ — the endpoint "
        "$A^{\\mathrm{geo}} = 0$ is excluded, because there the donor-limited recharge "
        "vanishes and $\\dot A^{\\mathrm{act}} = -\\omega_A A^{\\mathrm{eq,intrinsic}} < 0$.",
        "**Theorem 13 (Vanishing-extraction rest set).** *With vanishing extraction "
        "($E \\equiv 0$), the rest points of the closed natural block (2) are exactly the "
        "three sets — the extinction family $\\mathcal{R}_{\\mathrm{ext}}$, the "
        "carrying-capacity family $\\mathcal{R}_K$, and the frozen-biomass face "
        "$\\mathcal{R}_{\\mathrm{frozen}}$; the union symbol $\\mathcal{R}_0 = "
        "\\mathcal{R}_{\\mathrm{ext}} \\cup \\mathcal{R}_K$ is retained for the two "
        "geochemical families:*\n"
        "$$\\mathcal{R}_{\\mathrm{ext}} = \\bigl\\{ N = 0,\\ U = 0,\\ "
        "A^{\\mathrm{act}} = A^{\\mathrm{eq,intrinsic}}\\,\\sigma(A^{\\mathrm{geo}}),\\ "
        "A^{\\mathrm{geo}} \\ge 0 \\bigr\\}, \\qquad \\mathcal{R}_K = \\bigl\\{ N = K,\\ U = "
        "\\kappa_A K s/\\gamma_U,\\ A^{\\mathrm{act}} = "
        "A^{\\mathrm{eq,intrinsic}}\\,\\sigma,\\ A^{\\mathrm{geo}} \\ge 0 \\bigr\\},$$\n"
        "*where in the second family $s = A^{\\mathrm{act}}/(A^{\\mathrm{act}} + A_0)$ is "
        "evaluated at the solution — together with the frozen-biomass face "
        "$\\mathcal{R}_{\\mathrm{frozen}} = \\{(N, 0, 0, 0) : N \\ge 0\\}$, on which $s = 0$ "
        "identically and the biomass is frozen at its initial value. With $E > 0$ constant, "
        "no *interior* rest point (with $N_* > 0$) exists (Theorem 12); the extinction face "
        "$\\mathcal{R}_{\\mathrm{ext}}$ of this set persists at positive effort, because "
        "extraction $qEN$ vanishes identically at $N = 0$, and it is a boundary rest rather "
        "than an interior one (Section 4.6). If $A_{g0} = 0$ and $\\sigma \\equiv 1$ is "
        "imposed for $A^{\\mathrm{geo}} > 0$, the shared active-pool ray of "
        "$\\mathcal{R}_{\\mathrm{ext}}$ and $\\mathcal{R}_K$ is $A^{\\mathrm{act}} = "
        "A^{\\mathrm{eq,intrinsic}}$, $A^{\\mathrm{geo}} > 0$ — the endpoint "
        "$A^{\\mathrm{geo}} = 0$ is excluded, because there the donor-limited recharge "
        "vanishes and $\\dot A^{\\mathrm{act}} = -\\omega_A A^{\\mathrm{eq,intrinsic}} < 0$.",
        "r0-split")

    # ---------------- §4.7: Theorem 14 E >= 0 hypothesis ----------------
    t = sub1(t,
        "**Theorem 14 (Integrable extraction).** *Let $M = N + A^{\\mathrm{act}} + "
        "A^{\\mathrm{geo}} + U$. Then $M(t) = M(0) - \\int_0^t qE(s)N(s)\\, ds \\ge 0$, so*",
        "**Theorem 14 (Integrable extraction).** *Assume $E(s) \\ge 0$ along the trajectory "
        "(effort is nonnegative; $N \\ge 0$ along classical solutions is Theorem 10's). Let "
        "$M = N + A^{\\mathrm{act}} + A^{\\mathrm{geo}} + U$. Then $M(t) = M(0) - \\int_0^t "
        "qE(s)N(s)\\, ds \\ge 0$, so*",
        "thm14-egte")

    # ---------------- §4.7: constant-flux comparison label ----------------
    t = sub1(t,
        "A constant extraction flux $c > 0$ exhausts the budget in finite time",
        "A constant extraction flux $c > 0$ — a comparison flux only, not a donor-limited "
        "primitive the ledger's own discipline admits as a sustained law — exhausts the "
        "budget in finite time",
        "thm14-comparison")

    # ---------------- §4.8: Theorem 15 re-letter r,nu -> chi,eta ----------------
    t = sub1(t,
        "**Conditional Theorem 15 (Hybrid moiety balance).**\n*Assume:*\n\n*(H1) $r$ is "
        "absolutely continuous between locally finite event times with left and right "
        "limits at events.*\n\n*(H2) $\\dot r = \\mathsf{S}\\nu + b$ with $\\nu \\ge 0$, "
        "separate reverse columns, and donor-limited negative boundary flows.*\n\n*(H3) "
        "$\\mathsf{L}^\\top \\mathsf{S} = 0$.*\n\n*Then*\n"
        "$$\\mathsf{L}^\\top r(t) - \\mathsf{L}^\\top r(0) = \\int_0^t \\mathsf{L}^\\top b\\, "
        "ds + \\sum_{t_k \\le t} \\mathsf{L}^\\top \\bigl[ r(t_k^+) - r(t_k^-) \\bigr].$$",
        "**Conditional Theorem 15 (Hybrid moiety balance).**\n*Let $\\chi$ denote the "
        "hybrid state and $\\eta \\ge 0$ its primitive-flux vector — letters local to this "
        "statement, re-lettered from $r$ and $\\nu$ so that $r$ stays the growth rate of "
        "Section 2.2 and $\\nu$ a macro parameter of Section 5.4. Assume:*\n\n*(H1) $\\chi$ "
        "is absolutely continuous between locally finite event times with left and right "
        "limits at events.*\n\n*(H2) $\\dot \\chi = \\mathsf{S}\\eta + b$ with $\\eta \\ge "
        "0$, separate reverse columns, and donor-limited negative boundary flows.*\n\n*(H3) "
        "$\\mathsf{L}^\\top \\mathsf{S} = 0$.*\n\n*Then*\n"
        "$$\\mathsf{L}^\\top \\chi(t) - \\mathsf{L}^\\top \\chi(0) = \\int_0^t "
        "\\mathsf{L}^\\top b\\, ds + \\sum_{t_k \\le t} \\mathsf{L}^\\top \\bigl[ "
        "\\chi(t_k^+) - \\chi(t_k^-) \\bigr].$$",
        "thm15-reletter")
    t = sub1(t,
        "an internal-transformation jump requires $\\mathsf{L}^\\top(r^+ - r^-) = 0$",
        "an internal-transformation jump requires $\\mathsf{L}^\\top(\\chi^+ - \\chi^-) = 0$",
        "thm15-jump")

    # ---------------- §6.5: classification-matrix Theta_F cell ----------------
    t = sub1(t,
        "| $J_A^{\\mathrm{gross}}$, $H_A^{\\mathrm{gross}}$ | turnover / dependency | no | "
        "no | this (isolated gross loss) |",
        "| $J_A^{\\mathrm{gross}}$, $H_A^{\\mathrm{gross}}$ | turnover / dependency | no | "
        "no | gross-loss analogue only — not a member (§6.5.4) |",
        "thetaf-cell")

    # ---------------- §6.5.2: R17(a) dagger footnote adjacent to the row ----------------
    t = sub1(t,
        "| global mean | $-0.4$ | $-14$ | $-33.0$ | $\\approx 47.5$ |\n\n"
        "The basin rows are reported extractions",
        "| global mean | $-0.4$ | $-14$ | $-33.0$ | $\\approx 47.5$ |\n\n"
        "† *Quarantine note, adjacent to the row it marks (recorded data-vintage decision: "
        "the row stays first, daggered).* The Indo-Gangetic magnitude must not be reused "
        "numerically: it sits an order of magnitude beyond published basin-mean trends and "
        "awaits re-derivation from the product's basin masks — the full quarantine record "
        "is the paragraph below. The row is retained only as the worked instance of the "
        "index construction and enters no classification.\n\n"
        "The basin rows are reported extractions",
        "r17a-dagger")

    # ---------------- §6.5.2: R17(b) headline-site disclosure ----------------
    t = sub1(t,
        "The fisheries column reports the pure-decay proxy $\\mathrm{ADH} = "
        "F^{-1}\\log(\\mathrm{SSB}_{\\mathrm{now}}/(0.2\\max\\mathrm{SSB}))$ under current "
        "$F$, with median $\\approx 1.8$ yr across the 43 assessed stocks with finite SSB "
        "and $F$ series, computed with $\\mathrm{ADH} = 0$ entered for the eight stocks "
        "already at or below the reference — the zero convention of the source table's "
        "caption, which the median includes.",
        "The fisheries column reports the pure-decay proxy $\\mathrm{ADH} = "
        "F^{-1}\\log(\\mathrm{SSB}_{\\mathrm{now}}/(0.2\\max\\mathrm{SSB}))$ under current "
        "$F$, with median $\\approx 1.8$ yr across the 43 assessed stocks with finite SSB "
        "and $F$ series — the archived pull, kept in place as the headline cohort by the "
        "recorded data-vintage decision — computed with $\\mathrm{ADH} = 0$ entered for the "
        "eight stocks already at or below the reference, the zero convention of the source "
        "table's caption, which the median includes. Two disclosures ride the headline site "
        "(both recorded, neither a demotion of the number): the archived 43-stock cohort is "
        "reproduced by neither public RAM Legacy release — S5's version-sensitivity record, "
        "cross-referenced here, is the retraction and the row-by-row re-verification — and "
        "the v4.66 public-release broad-cohort reading (454 stocks, median $3.39$ yr) is "
        "the primary public-release comparison, executed in S5 and detailed below.",
        "r17b-headline")

    # ---------------- §6.5.2: review-screen companion citation ----------------
    t = sub1(t,
        "the fast-maturing class the companion review screen selects by its annual-review "
        "eligibility criterion",
        "the fast-maturing class the companion review screen (Author, E., et al., in "
        "review) selects by its annual-review eligibility criterion",
        "companion-e-screen")

    # ---------------- §6.5.3: R14 Mt/kt harmonisation ----------------
    t = sub1(t,
        "at approximately $74{,}000$ Mt of world reserves and $240{,}000$ kt/yr of "
        "production (U.S. Geological Survey, 2026) this is approximately $309$ years.",
        "at approximately $74{,}000{,}000$ kt ($74{,}000$ Mt) of world reserves and "
        "$240{,}000$ kt/yr of production (U.S. Geological Survey, 2026) this is "
        "approximately $309$ years.",
        "r14-units")

    # ---------------- §6.5.3: USGS single-vintage pin ----------------
    t = sub1(t,
        "the country horizons reproduce the recorded MCS-vintage ratios, and re-pinning "
        "every row to the single MCS 2026 vintage — whose 2025 world production column "
        "reads $\\approx 250{,}000$ kt — is a registered revision requirement. MCS 2026 "
        "reports Australia's reserves as $120{,}000$ kt (JORC-compliant; the main table "
        "retains the pre-2026 value of $5{,}800{,}000$ kt under the quarantine dagger "
        "rather than leaving the cell blank), so the displayed pre-2026 Australian row is "
        "quarantined pending the re-pin.",
        "the country horizons reproduce the recorded MCS-vintage ratios. The vintage is "
        "pinned once: the single pinned source of record is MCS 2026 (U.S. Geological "
        "Survey, 2026), and every figure this article quotes at pin status is that "
        "vintage's — the 2025 world production column $\\approx 250{,}000$ kt and "
        "Australia's reserves $120{,}000$ kt (JORC-compliant). The displayed country rows "
        "remain at their recorded pre-2026 vintage under the quarantine dagger (the "
        "Australian $5{,}800{,}000$ kt among them, retained rather than blanked), kept in "
        "place as worked instances of the reserve-life construction; completing the re-pin "
        "— replacing the displayed rows row by row with the pinned vintage's per-country "
        "reserve figures — is the registered open data action, it requires the per-country "
        "MCS 2026 reserve table, and no displayed classification depends on it.",
        "usgs-pin")

    # ---------------- §7.2: Definition 6 A_0 local declaration ----------------
    t = sub1(t,
        "**Definition 6 (Observed-drift Brownian surrogate).** *Let $A_0$ be the latest "
        "observed anomaly and $\\mu = \\widehat\\mu < 0$ the fitted drawdown rate. On the "
        "scale of the tabulated series define*",
        "**Definition 6 (Observed-drift Brownian surrogate).** *Let $A_0$ (local to "
        "Sections 7.2–7.4; not the half-saturation constant of Section 2.2) be the latest "
        "observed anomaly and $\\mu = \\widehat\\mu < 0$ the fitted drawdown rate. On the "
        "scale of the tabulated series define*",
        "def6-a0")

    # ---------------- §8.1: rho_P ----------------
    t = sub1(t,
        "the mining flux $c_G$ and the recycling routes $\\alpha, \\rho$",
        "the mining flux $c_G$ and the recycling routes $\\alpha, \\rho_P$",
        "rhoP-s81")

    # ---------------- §9: R15 six right-hand sides ----------------
    t = sub1(t,
        "**The hand-off projection.** Under the institutional-failure specialization, the "
        "macroeconomic block, prices, and demand do not appear in $(\\dot N, \\dot A, "
        "\\dot U, \\dot Z, \\dot E)$: each of the five right-hand sides depends only on the "
        "block's own variables and the delayed memory, and none contains the "
        "macroeconomic states, prices, or demand.",
        "**The hand-off projection.** Under the institutional-failure specialization, the "
        "macroeconomic block, prices, and demand do not appear in $(\\dot N, \\dot "
        "A^{\\mathrm{act}}, \\dot A^{\\mathrm{geo}}, \\dot U, \\dot Z, \\dot E)$ — the "
        "closed block's six right-hand sides, geological donor included: each depends only "
        "on the block's own variables and the delayed memory, and none contains the "
        "macroeconomic states, prices, or demand.",
        "r15-sixrhs")

    # ---------------- §9: harmonised mu/nu/rho gloss ----------------
    t = sub1(t,
        "**The exact shared object.** Under the single-resource specialization of Section "
        "5.4 ($\\mu = \\nu = \\rho = 0$, the macroeconomic-feedback, recycling, and mining "
        "channels switched off, and $C^A = 0$) — with the local stock equation $\\dot N = R "
        "- qEN$, the deficit identity",
        "**The exact shared object.** Under the single-resource specialization of Section "
        "5.4 ($\\mu = \\nu = \\rho = 0$ — the product, waste, and price parameters of the "
        "unreduced ledger: its macroeconomic-feedback, recycling, and price-response "
        "channels, per the Section 2.2 gloss — and the mining intensity $C^A = 0$) — with "
        "the local stock equation $\\dot N = R - qEN$, the deficit identity",
        "r16-s9-gloss")

    # ---------------- §9: reason 2 field-difference reconciliation ----------------
    t = sub1(t,
        "2. At the working equilibrium the two $A^{\\mathrm{act}}$ vector fields differ by "
        "an $O(1)$ term — in fact by $B^* - R^* = T^* \\approx 4.47$ stock units per year, "
        "the gross uptake at the working point, not a small residual.",
        "2. At the working equilibrium the two $A^{\\mathrm{act}}$ vector fields, written "
        "at the same state $(N, A^{\\mathrm{act}}, U)$, differ by "
        "$\\omega_A\\bigl(A^{\\mathrm{eq,W}} - A^{\\mathrm{eq,intrinsic}}\\sigma\\bigr) - "
        "\\gamma_U U = \\kappa_A K - \\gamma_U U$ under the registered scale separation "
        "($\\sigma \\approx 1$): approximately $0.535$ stock units per year at the working "
        "point's quasi-rest detritus level (where $\\gamma_U U = T^* \\approx 4.47$, the "
        "gross uptake at the working point) and $\\kappa_A K = 5.000$ stock units per year "
        "at $U = 0$ — an $O(1)$ to $O(\\kappa_A K)$ discrepancy, not a small residual. The "
        "two same-state flux readings behind it are the working recharge "
        "$\\omega_A(A^{\\mathrm{eq,W}} - A^{\\mathrm{act,*}}) = 4.652$ and the closed donor "
        "flow $e_{GA} - e_{AG} \\approx -0.348$, whose signed difference is $4.652 + 0.348 "
        "= 5.000 = \\kappa_A K$; the difference is $U$-dependent because the working field "
        "omits the detritus return $\\gamma_U U$ that the closed field carries — the "
        "U-handling split is part of this obstruction, and $B^* - R^* = T^*$ is the working "
        "system's turnover balance, not the field difference.",
        "s9-reason2")

    # ---------------- §9: trichotomy paragraph ----------------
    t = sub1(t,
        "The five reasons form a trichotomy: (1)–(3) are short-time obstructions — the two "
        "$A^{\\mathrm{act}}$ fields differ by $O(\\kappa_A K) = O(5)$ at the working point, "
        "and trajectories of the two systems diverge on $O(1)$ time scales;",
        "The five reasons form a trichotomy: (1)–(3) are short-time obstructions — the two "
        "$A^{\\mathrm{act}}$ fields differ by $\\kappa_A K - \\gamma_U U$ at the same "
        "state, which is $O(1)$ at the working point's quasi-rest detritus level "
        "($\\approx 0.535$) and at most $\\kappa_A K = O(5)$ (at $U = 0$), and trajectories "
        "of the two systems diverge on $O(1)$ time scales;",
        "s9-trichotomy")

    # ---------------- §9: unit corrections ----------------
    t = sub1(t,
        "at the closed-block extraction rate $c = qE^*N^* \\approx 0.187$ yr$^{-1}$ the "
        "budget bound is",
        "at the closed-block extraction rate $c = qE^*N^* \\approx 0.187$ stock units per "
        "year the budget bound is",
        "s9-units-c")
    t = sub1(t,
        "at the working completion's recharge flux $B^* \\approx 4.652$ yr$^{-1}$ the draw "
        "scale is",
        "at the working completion's recharge flux $B^* \\approx 4.652$ stock units per "
        "year the draw scale is",
        "s9-units-b")

    # ---------------- §9: companion citation at the interface contract ----------------
    t = sub1(t,
        "The partition between this article and the companion delay-dynamics analysis is "
        "fixed by an interface contract.",
        "The partition between this article and the companion delay-dynamics analysis "
        "(Author, D., et al., in review) is fixed by an interface contract.",
        "companion-d-s9")

    # ---------------- §10.1: assessment companion citation ----------------
    t = sub1(t,
        "The companion assessment analysis proves the dynamic form of the same separation "
        "for transition operators;",
        "The companion assessment analysis (Author, F., et al., in review) proves the "
        "dynamic form of the same separation for transition operators;",
        "companion-f-assessment")

    # ---------------- §11: rewrite paragraph 2 ----------------
    t = sub1(t,
        "The article likewise locates substitution within the ledger rather than alongside "
        "it. Weak and strong sustainability are two regimes of one system, distinguished by "
        "whether the material cycle closes at the rate of use. Weak sustainability is the "
        "idealized regime in which slow consumption and population let substitution "
        "(dominant, with regeneration deeper-time and included for completeness) "
        "redistribute matter so that it is used as it arises, and in which byproducts are "
        "therefore not waste. Waste is the relational status of matter that accumulates "
        "when that redistribution fails in time, for lack of knowledge, technology, or "
        "timely re-routing; no substance is waste by its nature; the driver is the rate of "
        "use, since the same substances close the loop at a consumption rate the cycle can "
        "absorb and fail to do so — accumulating as waste or showing up as a local "
        "depletion — at a consumption rate that exceeds the rate at which substitution and "
        "regeneration can re-loop the matter. A substitute is either a recycled flux "
        "returned to the regenerating pool or a non-renewable drawdown on a second "
        "compartment — different ledger entries with different statuses — and the ledger "
        "keeps stock compartments first-class, with the scalar $B\\cdot M$ against "
        "consumption the operational reading on top of it. A horizontal exhaustion estimate "
        "built on a reserve figure carries the substitution and technology premises of the "
        "reserve classification, not a physical forecast. For ecological-economics "
        "measurement, the implication is that \"strong\" and \"weak\" sustainability are "
        "not rival doctrines but two readings of one typed stock–flow ledger — and the "
        "vector reading is what carries the certificate.",
        "The article likewise locates substitution within the ledger rather than alongside "
        "it. The weak and strong regimes of Section 1.1 are two readings of one typed "
        "stock–flow ledger — distinguished by whether the material cycle closes at the rate "
        "of use; the reading is developed once, in the introduction, and is not re-argued "
        "here. They are not rival doctrines: the vector reading is the one that carries the "
        "certificate, the scalar $b\\cdot M$ check of Section 1.1 is the operational "
        "reading on top of it, and a substitute is either a recycled flux returned to the "
        "regenerating pool or a non-renewable drawdown on a second compartment — different "
        "ledger entries with different statuses. An exhaustion-horizon estimate built on a "
        "reserve figure carries the substitution and technology premises of the reserve "
        "classification, not a physical forecast. For ecological-economics measurement, "
        "that is the closing statement: not rival doctrines but two readings of one ledger, "
        "and the vector reading is what carries the certificate.",
        "s11-rewrite")

    # ---------------- References: three companion entries ----------------
    t = sub1(t,
        "Aubin, J.-P., 1991. Viability Theory. Birkhäuser, Boston.",
        "Author, D., et al., in review. Delay-induced regime change in harvested stocks: "
        "the mobilising and protective channels of institutional feedback, and the review "
        "interval as control. Companion delay-dynamics study.\n\n"
        "Author, E., et al., in review. Periodic review as sampled governance: "
        "sample-and-hold dynamics of assessment-driven effort control, a selected 42-stock "
        "spectral screen, and the Northern Cod case. Companion review-screen study.\n\n"
        "Author, F., et al., in review. The limits of compensatory aggregation: a formal "
        "separation of weak and strong sustainability assessment. Companion "
        "assessment-separation study.\n\n"
        "Aubin, J.-P., 1991. Viability Theory. Birkhäuser, Boston.",
        "refs-companions")

    # ---------------- Housekeeping: supplementary pointer v7 ----------------
    t = sub1(t,
        "The accompanying file `paper3_supplementary_v6.md` carries:",
        "The accompanying file `paper3_supplementary_v7.md` carries:",
        "supp-v7")

    v28 = t

    # ================= mechanical checks =================
    body_lines = [l for l in v28.splitlines() if not l.startswith("*Version log (v28).*")]
    body = "\n".join(body_lines)
    src_body_lines = [l for l in open(SRC, encoding="utf-8").read().splitlines()
                      if not l.startswith("*Version log (v27).*")]
    src_body = "\n".join(src_body_lines)

    # R11: no "horizontal exhaustion" anywhere outside the version log
    if "horizontal exhaustion" in body:
        raise SystemExit("FAIL [R11]: 'horizontal exhaustion' still present")
    if body.count("exhaustion-horizon estimate") != 2:
        raise SystemExit("FAIL [R11]: expected 2 'exhaustion-horizon estimate' sites")

    # R12
    if "B = b\\cdot M$ — the aggregate regeneration flow" not in body:
        raise SystemExit("FAIL [R12]: defining clause missing")
    if "B\\cdot M" in body:
        raise SystemExit("FAIL [R12]: §11 still carries $B\\cdot M$")
    if "the scalar $b\\cdot M$ check of Section 1.1" not in body:
        raise SystemExit("FAIL [R12]: §11 harmonised token missing")

    # R13
    if "The deep-time clause is scoped to the slow compartments" not in body:
        raise SystemExit("FAIL [R13]: scoping sentence missing")
    if "often on deep-time scales" not in body:
        raise SystemExit("FAIL [R13]: original claim dropped")

    # R14
    if "$74{,}000{,}000$ kt ($74{,}000$ Mt)" not in body:
        raise SystemExit("FAIL [R14]: harmonised units missing")
    if "approximately $74{,}000$ Mt of world reserves" in body:
        raise SystemExit("FAIL [R14]: old mixed display still present")

    # R15
    if "each of the five right-hand sides" in body:
        raise SystemExit("FAIL [R15]: 'five right-hand sides' still present")
    if "the closed block's six right-hand sides, geological donor included" not in body:
        raise SystemExit("FAIL [R15]: six-RHS list missing")

    # R16
    if "the product, waste, and price parameters $\\mu, \\nu, \\rho$ of the unreduced " \
       "ledger" not in body:
        raise SystemExit("FAIL [R16]: §2.2 defining clause missing")
    if "retirement fraction $\\rho \\in [0,1]$" in body:
        raise SystemExit("FAIL [R16]: retirement fraction still uses bare ρ")
    if "retirement fraction $\\rho_P \\in [0,1]$" not in body:
        raise SystemExit("FAIL [R16]: ρ_P re-letter missing")
    if "$\\dot r = \\mathsf{S}\\nu + b$" in body:
        raise SystemExit("FAIL [R16]: Theorem 15 hybrid r/ν still present")
    if "$\\dot \\chi = \\mathsf{S}\\eta + b$" not in body:
        raise SystemExit("FAIL [R16]: Theorem 15 χ/η missing")
    if "local to Sections 7.2–7.4; not the half-saturation constant" not in body:
        raise SystemExit("FAIL [R16]: Definition 6 A_0 declaration missing")
    if "The table sits at the head of Section 2" not in body:
        raise SystemExit("FAIL [notation]: relocated table lead-in missing")
    for row_needle, label in [
        ("| $\\rho_P$ | product-retirement fraction", "ρ_P table row"),
        ("| $\\mu, \\nu, \\rho$ | product, waste, and price parameters", "μνρ table row"),
        ("| $b$ | boundary-transfer term", "b table row"),
        ("| $A_0$ | half-saturation constant", "A_0 table row"),
        ("| $\\varepsilon$ | drift bracket", "ε table row"),
        ("| $\\chi, \\eta$ | hybrid state", "χη table row"),
        ("| $\\tau$ | hitting and exit times", "τ table row"),
        ("maintainability kernel $K_{\\mathrm{maint}}$ (subscripted)", "K_maint row"),
    ]:
        if row_needle not in body:
            raise SystemExit(f"FAIL [notation]: table row missing [{label}]")

    # Demotions: labels present, old labels absent, stale references absent
    for label, old in [
        ("**Remark 2 (Registered-family support-saturated identity).**",
         "**Theorem 2 (Registered-family"),
        ("**Lemma 3 (Flux reconstruction under a typed balance law).**",
         "**Theorem 3 (Flux reconstruction"),
        ("**Proposition 4 (Conservation-law reduction).**",
         "**Theorem 4 (Conservation-law reduction)"),
        ("**Proposition 6 (Finite exhaustion under uniform negative drift).**",
         "**Theorem 6 (Finite exhaustion"),
        ("**Remark 16 (Exact specialization deficit identity).**",
         "**Lemma 16 (Exact specialization"),
        ("**Proposition 17 (Local threshold-horizon bracket).**",
         "**Theorem 17 (Local threshold-horizon"),
        ("**Proposition 18 (Inverse-Gaussian first passage — a standard fact, stated for "
         "notation).**", "**Theorem 18 (Inverse-Gaussian"),
        ("**Proposition 20 (Geometric-Brownian correction — a standard fact, stated for "
         "notation).**", "**Theorem 20 (Geometric-Brownian"),
    ]:
        if label not in body:
            raise SystemExit(f"FAIL [demotion]: new label missing: {label[:40]}")
        if old in body:
            raise SystemExit(f"FAIL [demotion]: old label still present: {old[:40]}")
    for stale in ["Theorem 2", "Theorem 3", "Theorem 4", "Theorem 6",
                  "Theorem 17", "Theorem 18", "Theorem 20", "Lemma 16",
                  "Theorems 1–2", "Theorems 3–5"]:
        if re.search(r"\b" + re.escape(stale) + r"\b", body):
            raise SystemExit(f"FAIL [demotion]: stale reference '{stale}' in body")

    # Cross-reference consistency: every numbered reference resolves to a defined label
    defined = set()
    for m in re.finditer(
            r"\*\*(?:Conditional )?(Theorem|Proposition|Lemma|Remark|Corollary|Definition|"
            r"Observation)\s+(\d+)(?:\s*\(|\.\*\*)", v28):
        defined.add((m.group(1), int(m.group(2))))
    required = {
        ("Theorem", 1), ("Remark", 2), ("Lemma", 3), ("Proposition", 4),
        ("Theorem", 5), ("Proposition", 6), ("Theorem", 7), ("Theorem", 8),
        ("Theorem", 9), ("Theorem", 10), ("Theorem", 11), ("Theorem", 12),
        ("Theorem", 13), ("Theorem", 14), ("Theorem", 15), ("Remark", 16),
        ("Proposition", 17), ("Proposition", 18), ("Corollary", 19),
        ("Proposition", 20), ("Proposition", 1), ("Proposition", 2),
    }
    required.update(("Definition", n) for n in range(1, 7))
    if defined != required:
        missing = required - defined
        extra = defined - required
        raise SystemExit(f"FAIL [labels]: defined set mismatch; missing={missing}, "
                         f"extra={extra}")
    refs = []
    for m in re.finditer(
            r"\b(Theorem|Proposition|Lemma|Remark|Corollary|Definition)s?\s+"
            r"([\d,\s\u2013\-]+)", body):
        typ = m.group(1)
        chunk = m.group(2)
        ints = [int(x) for x in re.findall(r"\d+", chunk)]
        # expand "a–b" ranges
        rng = re.search(r"(\d+)\s*[\u2013\-]\s*(\d+)", chunk)
        if rng and rng.group(1) != rng.group(2):
            lo, hi = int(rng.group(1)), int(rng.group(2))
            ints = list(range(lo, hi + 1))
        for n in ints:
            refs.append((typ, n))
    for typ, n in refs:
        if (typ, n) not in defined:
            raise SystemExit(f"FAIL [xref]: reference ({typ} {n}) does not resolve")

    # Incidence matrices: exact strings + column-sum arithmetic
    if v28.count(SBLOCK) != 1:
        raise SystemExit("FAIL [incidence]: four-row display not present exactly once")
    if v28.count(ST7) != 1:
        raise SystemExit("FAIL [incidence]: seven-compartment display not present exactly "
                         "once")
    rows4, sums4 = column_sums(SBLOCK)
    exp4 = [["1", "-1", "-1", "0", "0", "0", "0", "0"],
            ["-1", "1", "0", "-1", "1", "1", "-1", "0"],
            ["0", "0", "0", "0", "0", "-1", "1", "-1"],
            ["0", "0", "0", "1", "-1", "0", "0", "0"]]
    if rows4 != exp4:
        raise SystemExit("FAIL [incidence]: four-row matrix rows wrong")
    if sums4 != [0, 0, -1, 0, 0, 0, 0, -1]:
        raise SystemExit(f"FAIL [incidence]: four-row column sums {sums4} wrong (expected "
                         "zeros except harvest and mining = -1)")
    if sum(sums4) != -2:
        raise SystemExit("FAIL [incidence]: four-row total sum wrong (dot M identity)")
    rows7, sums7 = column_sums(ST7)
    if len(rows7) != 7 or len(rows7[0]) != 10:
        raise SystemExit("FAIL [incidence]: seven-compartment matrix shape wrong")
    if any(abs(s) > 1e-9 for s in sums7):
        raise SystemExit(f"FAIL [incidence]: seven-compartment column sums {sums7} not all "
                         "zero (conservation violated)")
    # natural-block submatrix: rows (N, U, A^act, A^geo) on the block's columns
    # (gross regen, density return, harvest, uptake, detritus, e_GA, e_AG, mining)
    sub = [[rows7[i][j] for j in range(8)] for i in [0, 4, 5, 6]]
    if sub[0] != ["1", "-1", "-1", "0", "0", "0", "0", "0"]:
        raise SystemExit("FAIL [incidence]: N row of submatrix wrong")
    if sub[1][:2] + sub[1][3:] != ["0", "0", "1", "-1", "0", "0", "0"]:
        raise SystemExit("FAIL [incidence]: U row of submatrix wrong (harvest = α)")
    if sub[2][:2] + sub[2][3:] != ["-1", "1", "-1", "1", "1", "-1", "0"]:
        raise SystemExit("FAIL [incidence]: A^act row of submatrix wrong")
    if sub[3][:2] + sub[3][3:] != ["0", "0", "0", "0", "-1", "1", "-1"]:
        raise SystemExit("FAIL [incidence]: A^geo row of submatrix wrong")
    if eval_token(rows7[4][2], 0.3, 0.45) != 0.3:
        raise SystemExit("FAIL [incidence]: harvest U-entry is not α")
    if "is not displayed separately" in body:
        raise SystemExit("FAIL [incidence]: old 'not displayed separately' claim remains")

    # R0 split
    for needle in ["\\mathcal{R}_{\\mathrm{ext}}", "\\mathcal{R}_K",
                   "\\mathcal{R}_{\\mathrm{frozen}}"]:
        if needle not in body:
            raise SystemExit(f"FAIL [R0]: {needle} missing")
    if "the $\\mathcal{R}_0$ ray" in body:
        raise SystemExit("FAIL [R0]: unsplit 'R_0 ray' remark remains")
    if "extinction family $\\mathcal{R}_{\\mathrm{ext}}$ of Theorem 13" not in body:
        raise SystemExit("FAIL [R0]: Theorem 12(iii) fix missing")
    if "the rest points of the closed natural block (2) are exactly the three sets" \
       not in body:
        raise SystemExit("FAIL [R0]: 'exactly the two families' not corrected")

    # Theorem 14
    if "**Theorem 14 (Integrable extraction).** *Assume $E(s) \\ge 0$" not in body:
        raise SystemExit("FAIL [Thm14]: E ≥ 0 hypothesis missing")
    if "a comparison flux only, not a donor-limited primitive" not in body:
        raise SystemExit("FAIL [Thm14]: comparison-flux label missing")

    # §9 reconciliation (recomputed values)
    for needle, label in [
        ("\\kappa_A K - \\gamma_U U", "field-difference formula"),
        ("approximately $0.535$ stock units per year", "quasi-rest value"),
        ("$\\kappa_A K = 5.000$ stock units per year", "U=0 value"),
        ("$4.652 + 0.348 = 5.000 = \\kappa_A K$", "signed flux difference"),
        ("0.187$ stock units per year", "c units"),
        ("$B^* \\approx 4.652$ stock units per year", "B* units"),
        ("$\\gamma_U U = T^* \\approx 4.47$", "T* quasi-rest"),
    ]:
        if needle not in body:
            raise SystemExit(f"FAIL [§9]: {label} missing")
    if "differ by an $O(1)$ term — in fact by $B^* - R^* = T^*$" in body:
        raise SystemExit("FAIL [§9]: old reason-2 claim remains")
    if "$B^* \\approx 4.652$ yr$^{-1}$" in body:
        raise SystemExit("FAIL [§9]: yr^-1 unit on B* remains")
    if "$c = qE^*N^* \\approx 0.187$ yr$^{-1}$" in body:
        raise SystemExit("FAIL [§9]: yr^-1 unit on c remains")

    # Theta_F cell
    if "gross-loss analogue only — not a member (§6.5.4)" not in body:
        raise SystemExit("FAIL [ThetaF]: reconciled cell missing")
    if "this (isolated gross loss)" in body:
        raise SystemExit("FAIL [ThetaF]: old cell remains")

    # USGS pin
    if "The vintage is pinned once: the single pinned source of record is MCS 2026" \
       not in body:
        raise SystemExit("FAIL [USGS]: pin declaration missing")
    if "is a registered revision requirement" in body:
        raise SystemExit("FAIL [USGS]: old 'registered revision requirement' remains")

    # R17 decisions
    if "Quarantine note, adjacent to the row it marks" not in body:
        raise SystemExit("FAIL [R17a]: dagger footnote missing")
    if "kept in place as the headline cohort by the recorded data-vintage decision" \
       not in body:
        raise SystemExit("FAIL [R17b]: headline keep-in-place decision missing")
    if "Two disclosures ride the headline site" not in body:
        raise SystemExit("FAIL [R17b]: headline disclosures missing")
    if "the primary public-release comparison" not in body:
        raise SystemExit("FAIL [R17b]: v4.66 primary comparison missing")

    # Companions
    for needle, label in [
        ("Author, D., et al., in review. Delay-induced regime change", "ref D"),
        ("Author, E., et al., in review. Periodic review as sampled governance", "ref E"),
        ("Author, F., et al., in review. The limits of compensatory aggregation", "ref F"),
        ("(Author, D., et al., in review; eq. (1) and Section 2.4", "in-text D (ZE pair)"),
        ("companion delay-dynamics analysis (Author, D., et al., in review); the three",
         "in-text D (recharge table)"),
        ("(Author, D., et al., in review) is fixed by an interface contract", "in-text D (§9)"),
        ("companion review screen (Author, E., et al., in review) selects", "in-text E"),
        ("companion assessment analysis (Author, F., et al., in review) proves",
         "in-text F"),
        ("Companion delay-dynamics study.", "D tag"),
        ("Companion review-screen study.", "E tag"),
        ("Companion assessment-separation study.", "F tag"),
    ]:
        if needle not in v28:
            raise SystemExit(f"FAIL [companions]: {label} missing")

    # §11 rewrite
    if "Waste is the relational status of matter that accumulates" in body:
        raise SystemExit("FAIL [§11]: weak/strong re-argument still present")
    if "Waste is a relational status, not an intrinsic property" not in body:
        raise SystemExit("FAIL [§11]: §1.1 content wrongly dropped")
    if "the reading is developed once, in the introduction, and is not re-argued here" \
       not in body:
        raise SystemExit("FAIL [§11]: closing statement missing")

    # Housekeeping
    if "paper3_supplementary_v7.md" not in body:
        raise SystemExit("FAIL [housekeeping]: v7 pointer missing")
    if "paper3_supplementary_v6.md" in body:
        raise SystemExit("FAIL [housekeeping]: v6 pointer remains")

    # Table rows byte-identical except itemised changes
    def table_rest(text):
        """All markdown table lines, with the (relocated) notation table's contiguous
        run removed — so the remaining rows can be compared pairwise."""
        lines = text.splitlines()
        out, i = [], 0
        while i < len(lines):
            if lines[i].startswith("| Symbol | Meaning | Where |"):
                i += 1
                while i < len(lines) and lines[i].startswith("|"):
                    i += 1
                continue
            if lines[i].startswith("|"):
                out.append(lines[i])
            i += 1
        return out

    old_rest = table_rest(src_body)
    new_rest = table_rest(body)
    thetaf_old = ("| $J_A^{\\mathrm{gross}}$, $H_A^{\\mathrm{gross}}$ | turnover / "
                  "dependency | no | no | this (isolated gross loss) |")
    thetaf_new = ("| $J_A^{\\mathrm{gross}}$, $H_A^{\\mathrm{gross}}$ | turnover / "
                  "dependency | no | no | gross-loss analogue only — not a member "
                  "(§6.5.4) |")
    if len(old_rest) != len(new_rest):
        raise SystemExit(f"FAIL [tables]: line counts {len(old_rest)} -> {len(new_rest)} "
                         "after removing the notation block")
    diffs = [(a, b) for a, b in zip(old_rest, new_rest) if a != b]
    if diffs != [(thetaf_old, thetaf_new)]:
        raise SystemExit(f"FAIL [tables]: unexpected table-row differences: {diffs}")

    # Version log sanity
    if not v28.startswith("# Typed Flux Ledgers"):
        raise SystemExit("FAIL: title damaged")
    if v28.count("*Version log (v28).*") != 1:
        raise SystemExit("FAIL: version log not exactly once")

    open(DST, "w", encoding="utf-8").write(v28)
    wc = len(v28.split())
    wc_old = len(open(SRC, encoding="utf-8").read().split())
    print(f"OK: wrote {DST}")
    print(f"    words: {wc_old} -> {wc} (delta {wc - wc_old})")
    print(f"    lines: {len(v28.splitlines())}; statements defined: {len(defined)}; "
          f"references checked: {len(refs)}")
    print(f"    incidence checks: 4-row column sums {sums4} (harvest/mining = -1 exports); "
          f"7-compartment column sums all zero")


if __name__ == "__main__":
    main()
