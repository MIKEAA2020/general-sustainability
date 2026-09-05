#!/usr/bin/env python3
"""
apply_batch7_wave4_p4.py — fail-loud build of paper4_delay_dynamics_v27.md from v26,
plus the ONE allowed append to paper4_supplementary_v4.md (R21's S11 relocation).

Implements the wave-4 P4 items (owner-directed, "cite, don't drop"):
  R18 [claude]  §1.1's second cross-ref error: "bifurcation analysis occupies
      Sections 2–9" → Sections 2–5 locally (§6 protective, §8 sample-and-hold,
      §9 global numerics).
  R19 [grok ×3] The G5 registration sentence (the compute-core Hopf pair
      3.666149 / 150.358477) is relocated from §7.6's registration list to §5.1,
      where the pair is certified — relabelled as the base-core (1) record
      (Supplementary S9.5), not a §7 object. §7's certified gates are now G2–G4.
  R20 [claude]  Definitions at first use: σ_geo (§2.4), γ_U (§2.3, with the MPF
      detritus equation U̇ = m(X) − γ_U U now displayed), ε_U (§2.4), α and β
      (Remark 5.1, from S5's K–L block), plus a σ_geo recall in Remark 5.1.
  R21 [both]    MPF material to the supplement: the η_crit sweep + pair-birth
      structure, the intermittency diagnostics, and the >300-parameterisation
      screen record — appended to paper4_supplementary_v4.md as S11 (clearly
      labelled, verbatim from v26), with one-sentence pointers keeping the key
      numbers (η_crit ≈ 2.337, CV 1.58, r = −0.47, >300 parameterisations) in
      the main text at both former sites (§9.3 and §10.4).
  R22 [grok]    "within 0.05%" → reproduced to within the bracket width (0.4%);
      ω_A^* quoted at sweep resolution; §10.1's "version-robust" repeat restated
      at bracket resolution.

Presentation tail (verified open at v26):
  §9.2 multiplier digits / 1.1×10⁻⁷ precision fusion unfused (certificate vs
      corroboration); the revision-history changelog narration stripped from
      §9.2/§9.3 (superseded readings recorded compactly in the version log);
      §1.2's digits rounded (13-digit endpoints, ρ values, fold digits,
      "provisional"); M3-B defined in the §2.3 family list; the §6.2(b) "c > 0"
      Routh entry defined; the Halanay decay rate renamed ν (η stays the effort
      response); the Lyapunov eigenvector pair renamed v, w (q stays
      catchability); the early-warning stock gap written |N̂ − N| (S stays the
      yield); Zhang et al. 2013, Moore 1979, Cloud–Moore–Kearfott 2009 cited in
      text; §9.5's uncited literature r-range scoped to the paper's own
      computation; §11.6 trimmed to the two next theorems (grant list recorded
      in one line + supplement S6); §8 gains the consolidated channel × scheme
      table, the 2/|C_E| = 2.352 yr Euler-limit sentence, the annual growth
      rates, and the stock-mode reading of the protective radius.

Non-destructive: no frozen verdict, spectral record, or table value changes;
the §5.1 certified row and the §9 fold/multiplier records are byte-identical;
§1.2's stripping rounds in §1.2 only (full precision remains in §5.1/§9); the
G5 numbers move (§7.6 → §5.1) without alteration; no new computation is
performed (the 2/|C_E|, e-folding, and stock-mode figures are one-line
arithmetic restatements of constants already printed in §6.2/§8).  Every edit
asserts its anchor appears exactly once; every mechanical check fails loudly.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "arena agent 1", "paper rewrites",
                   "paper4_delay_dynamics_v26.md")
DST = os.path.join(HERE, "..", "arena agent 1", "paper rewrites",
                   "paper4_delay_dynamics_v27.md")
SUP = os.path.join(HERE, "..", "arena agent 1", "paper rewrites",
                   "paper4_supplementary_v4.md")


def sub1(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise SystemExit(f"FAIL [anchor {label}]: expected exactly 1 occurrence, found {n}")
    return text.replace(old, new)


S11_SECTION = """---

## S11. Relocated MPF Material (Wave-4 Relocation)

*Appended at the wave-4 revision (main-text v27) to receive material relocated from the main article's Section 9.3 (the MPF paragraph) and Section 10.4, on the joint audit's routing of the MPF numerics to the supplement. Every value below is reproduced verbatim from the main text's v26; nothing is recomputed, and the main text retains one-sentence pointers carrying the key numbers ($\\eta_{\\mathrm{crit}} \\approx 2.337$; inter-excursion-interval coefficient of variation $1.58$ and return-map anticorrelation $r = -0.47$; the more-than-$300$-parameterisation screen).*

### S11.1 The $\\eta_{\\mathrm{crit}}$ sweep and the pair-birth structure

The absence of a baseline Hopf is parametric: Hopf roots first appear at $\\eta_{\\mathrm{crit}} \\approx 2.337$, with two interleaving pairs over $\\eta \\in (2.337, 3]$ (at $\\eta = 2.5$: $\\approx0.6$, $54.2$, $92.9$, $113.1$ yr; at $\\eta = 3.0$ one pair spans $\\approx4.5$–$41.2$ yr; at the out-of-range $\\eta = 10$: $17.568$/$18.362$ yr with a supercritical-consistent onset, exponent $0.59$, inferred). The pair-birth structure behind the interleaving is registered: the large-delay pair is born at $\\eta_{\\mathrm{crit}} \\approx 2.337$ ($\\tau_- \\approx 71.2$, $\\tau_+ \\approx 72.9$ yr) and migrates downward as $\\eta$ rises, while the small-delay pair is born at $\\eta \\approx 2.454$ with $\\tau_- \\to 0$ at its onset.

### S11.2 The slow-fast intermittency diagnostics ($\\eta = 10$, above $\\tau_+$)

Above $\\tau_+$ at $\\eta = 10$ the attractor is diagnosed as irregular slow-fast intermittency, with diagnostics inconsistent with a simple period-one or low-period orbit — the underlying global bifurcation mechanism (a homoclinic connection among the candidates) is unresolved. The diagnostics: a broad onset-interval spectrum with no sharp peak, a thin map-like Poincaré section on $Z$-crossings, inter-excursion-interval coefficient of variation $1.58$, and return-map anticorrelation $r = -0.47$ — with the large-amplitude time fraction rising monotonically from $0\\%$ at $\\tau = 18.4$ to $100\\%$ by $\\tau \\approx 22$ and no sharp second threshold separating quiet and captured regimes; the present diagnostics neither identify a homoclinic mechanism nor exclude torus breakdown.

### S11.3 The sigmoid-gated effort screen (more than $300$ parameterisations)

A sigmoid-gated effort variant of the same ecological core — the saturating gate $\\sigma(Z_\\tau/Z_0)$ of the main text's Section 10.4, whose linearisation at equilibrium decreases in deployed effort and contains no factor $\\eta E^*/\\Delta_{\\mathrm{ref}}$ — was screened across more than $300$ parameterisations (Newton eigenvalue tracking, joint modulus minimisation, nonlinear integration) without finding a genuine delay-induced Hopf — a numerical negative result over the sampled domain, not a structural impossibility theorem. The screen's loop-gain reading (it does not establish that autocatalysis is necessary for a Hopf pair, and the gated law (1) is not of this class) is stated where it belongs, in the main text's Section 10.4; this record is deposited here per the wave-4 relocation.
"""

V27_LOG = (
    "*Version log (v27).* Implements the wave-4 items of the joint-audit evaluation's P4 remaining-points "
    "list (R18–R22 and the registered presentation tail), owner-directed as cite-not-drop. (R18) Section 1.1's "
    "second cross-ref error is corrected: the delayed mobilising channel's local bifurcation analysis occupies "
    "Sections 2–5, with the protective channel in Section 6, sample-and-hold review in Section 8, and the global "
    "numerics in Section 9 (the earlier 'Sections 2–9' pointer was wrong). (R19) The G5 registration sentence is "
    "relocated from Section 7.6's registration list to Section 5.1, where the Hopf pair is certified: the "
    "registered compute-core Hopf pair $3.666149$/$150.358477$ is a record of the base core (1) (Supplementary "
    "S9.5), not an object of the maturation-delayed system of Section 7, whose certified gates are now G2–G4. "
    "(R20) $\\sigma_{\\mathrm{geo}}$ (geological-reservoir adequacy ratio), $\\gamma_U$ (detritus export rate), and "
    "$\\varepsilon_U$ (fast-variable slaving parameter) are defined at first use in Sections 2.3–2.4, $\\alpha$ and "
    "$\\beta$ (the fast block's $K$–$L$ coupling weights) at first use in Remark 5.1, and the MPF detritus equation "
    "$\\dot U = m(X) - \\gamma_U U$ is displayed in Section 2.3. (R21) The MPF $\\eta_{\\mathrm{crit}}$ sweep (the "
    "interleaving pair values at $\\eta = 2.5$, $3.0$, $10$; exponent $0.59$; the pair-birth values $\\tau_- "
    "\\approx 71.2$, $\\tau_+ \\approx 72.9$ yr and $\\eta \\approx 2.454$), the intermittency diagnostics (the "
    "spectrum, Poincaré-section, and time-fraction records), and the $300$-parameterisation screen record are "
    "relocated to the supplement's new S11 (appended to paper4_supplementary_v4.md, the one allowed edit to that "
    "file); one-sentence pointers retain the key numbers ($\\eta_{\\mathrm{crit}} \\approx 2.337$; coefficient of "
    "variation $1.58$; anticorrelation $-0.47$; more than $300$ parameterisations). (R22) The 'within $0.05\\%$' "
    "version-robustness claim is restated as reproduction to within the four-state bracket width ($0.4\\%$), at "
    "both its Section 9.3 site and Section 10.1's repeat, and $\\omega_A^*$ is quoted at sweep resolution. "
    "Presentation tail: Section 9.2's multiplier corroboration is unfused from the $10^{-7}$ fold-certificate "
    "precision (the Krawczyk box is the certificate; the multiplier table is corroboration at its own recorded "
    "digits); the revision-history narration is retired from the results narrative and recorded here — the "
    "superseded readings are: the earlier two-fold reading (basin collapse in $[5.574, 5.576]$ yr; large-branch "
    "multiplier $0.964$ at $5.5815$; corrected values $0.240 \\to 0.2040$ and $1.0514 \\to 1.0192$, and the M3-B "
    "form's $1.0514 \\to 0.998983$), the earlier capture-onset bracket $[148.125, 148.438]$ yr, the earlier "
    "'interior large family' (residual $\\sim10^{-13}$ on $[147.5, 160]$, amplitude $15.9$–$19.5$), the earlier "
    "third family 'at $E \\ge E_{\\max}$ collocating down to $\\tau \\approx 144.5$', the three-state's earlier "
    "$\\approx148$ yr upper-fold reading, the earlier qualitative basin asymmetry, the earlier possible-fold "
    "reading of the capture boundary, the $15\\%$ earlier-estimate comparison, and the independence-discipline "
    "clause on seeding; Section 1.2's digits are rounded (the 13-digit endpoints, $\\rho$ values, fold digits, "
    "and 'provisional' are removed there; full precision remains in Sections 5.1 and 9); M3-B is defined in the "
    "Section 2.3 family list; the Section 6.2(b) Routh entry $c$ is defined; the Halanay decay rate is renamed "
    "$\\nu$ (so $\\eta$ stays the effort-response coefficient); the Lyapunov eigenvector pair is renamed $v, w$ "
    "(so $q$ stays the catchability); the early-warning stock gap is written $|\\hat N - N|$ (so $S$ stays the "
    "yield); Zhang, Shen, and Chen (2013), Moore (1979), and Cloud, Moore, and Kearfott (2009) are cited in "
    "text; the Section 9.5 literature $r$-range is scoped to the paper's own computed window; Section 11.6 is "
    "trimmed to the two next theorems with the grant list recorded in one line (supplement S6); and Section 8 "
    "gains the consolidated channel × scheme table, the $2/|C_E| = 2.352$ yr Euler-limit sentence, the annual "
    "growth rates, and the stock-mode reading of the protective radius. No theorem, spectral record, or table "
    "value changes; no new computation is performed (the $2/|C_E|$, e-folding, and stock-mode figures are "
    "one-line arithmetic on constants already printed in Sections 6.2 and 8)."
)

TABLE_BLOCK = """**The consolidated sampled-data record (channel × scheme × review interval).** Every entry below is a record already stated in this section (Propositions 6.2 and 8.1, Theorem 8.1, and the scheme-dependence remark), collected in one table; the mobilising native-ZOH row's annual radius is not a recorded quantity of this paper.

| Channel | Monodromy scheme | $\\rho$ at $T_r = 1$ yr | Unit-circle crossings on the tested grids |
|---|---|---|---|
| Protective | Euler (11) | $0.9838$ | $\\rho = 1$ at $T_r \\approx 2.306$ yr (grid resolution; Euler command-step artefact, within $2\\%$ of the scalar Euler limit $2/|C_E| = 2.352$ yr) |
| Protective | Exact held-measurement (13) | $0.9838$ | none on $[0.2, 300]$ yr; maximum $0.9967$ at $T_r = 0.2$ yr |
| Protective | Native ZOH ($M_{\\mathrm{ZOH}}$) | $0.9928$ | none on $[0.2, 200]$ yr |
| Mobilising | Euler (12) | $1.00055$ | complex pair at $47.536$ yr and $-1$ at $79.143$ yr (command-step artefacts; exact-map radii there $0.786$ and $0.597$) |
| Mobilising | Exact held-measurement (13) | $1.00035$ | one complex pair at $T_r = 6.50$ yr ($0.9846 \\pm 0.1746\\,i$; third eigenvalue $0.1647$) |
| Mobilising | Native ZOH ($M_{\\mathrm{ZOH}}$) | not recorded | one complex pair at $T_r = 6.7279$ yr ($0.9855 \\pm 0.1699\\,i$) |

Two readings travel with the table. First, the annual-review mobilising growth rate is small in absolute terms: $\\rho - 1 = 5.5\\times10^{-4}$ per review cycle (Euler) and $3.5\\times10^{-4}$ (exact) — e-folding times of roughly $1800$ and $2900$ review cycles respectively — so the annual-review instability is the $\\tau = 0$ instability of Section 5.1 seen through a one-year hold that supplies too little phase, not a fast divergence. Second, the protective annual radius is the slow stock mode: the uncoupled modes of the protective hold-and-update map at annual cadence sit at $e^{A_N} \\approx 0.982$ (stock; $A_N = -0.0179$), $e^{-d} \\approx 0.819$ (memory; $d = 0.2$), and $1 + C_E \\approx 0.150$ (effort; $C_E = -0.850336$), and the recorded $\\rho(M_p(1)) = \\rho(M_{\\mathrm{ex}}(1)) = 0.9838$ — the same value under the two update schemes — is that stock mode, only weakly coupled by the controller; the protective maximum $0.9967$ at $T_r = 0.2$ yr likewise matches the stock mode's $e^{A_N T_r} \\approx 0.996$. The protective sampled-data record therefore says that the slow stock mode decays under review, not that the controller stabilises an otherwise unstable loop."""


def build_paper():
    t = open(SRC, encoding="utf-8").read()
    v26 = t

    # ---------------- version log (follows the file's one-paragraph convention) ----
    old_log_start = "*Version log (v26).*"
    if t.count(old_log_start) != 1:
        raise SystemExit("FAIL: v26 version log anchor")
    idx = t.find(old_log_start)
    log_end = t.find("\n\n## Abstract", idx)
    if log_end == -1:
        raise SystemExit("FAIL: version log terminator")
    t = t[:idx] + V27_LOG + t[log_end:]

    # ---------------- R18 + §1.1 Zhang citation (L19/L23) ----------------
    t = sub1(t,
        "maturation and stage structure (Aiello and Freedman, 1990; Kuang, 1993).",
        "maturation and stage structure (Aiello and Freedman, 1990; Kuang, 1993), and "
        "harvested predator–prey systems whose paired ecological delays are Hopf "
        "objects in their own right (Zhang, Shen, and Chen, 2013).",
        "s11-zhang")
    t = sub1(t,
        "The hen's loop is then the delayed mobilising channel whose bifurcation "
        "analysis occupies Sections 2–9.",
        "The hen's loop is then the delayed mobilising channel, whose local "
        "bifurcation analysis occupies Sections 2–5 (the protective channel is "
        "Section 6; sample-and-hold review, Section 8; the global numerics, "
        "Section 9).",
        "r18")

    # ---------------- §1.2 digit stripping (R docket; grok+claude) ----------------
    t = sub1(t,
        "certified by interval Newton on the cubic with outward rounding: τ− ∈ "
        "[3.6661490142739, 3.6661490142743] yr and τ+ ∈ [150.3584773101408, "
        "150.3584773101421] yr at Candidate A (Section 4.1).",
        "certified by interval Newton on the cubic with outward rounding — near 3.7 "
        "and 150 yr at Candidate A, with the 13-digit enclosures displayed in "
        "Section 5.1's table.",
        "s12-item3")
    t = sub1(t,
        "The protective channel is stable under annual review ($\\rho = 0.9838$), and "
        "its instability threshold at $T_r \\approx 2.306$ yr is a discretisation "
        "artefact of the Euler factor $1 + T_r C_E$ — provably not a Hopf of the "
        "continuous system (Section 6.2).",
        "The protective channel is stable under annual review (spectral radius below "
        "one), and its apparent instability threshold near 2.3 yr is a discretisation "
        "artefact of the Euler update — provably not a Hopf of the continuous system "
        "(Section 6.2).",
        "s12-item5a")
    t = sub1(t,
        "The mobilising channel is unstable under annual review ($\\rho = 1.00055$ "
        "Euler; $1.00035$ exact) and has its restabilising complex unit-circle "
        "crossing — the spectral signature of a Neimark–Sacker bifurcation, with "
        "nonlinear conditions not verified — at $T_r = 6.50$ yr under the exact "
        "held-measurement update (Proposition 8.1). The Euler-reported 47.536 yr "
        "crossing and its $-1$ multiplier at 79.143 yr are command-step artefacts.",
        "The mobilising channel is unstable under annual review (spectral radius just "
        "above one under both the Euler and the exact update) and has its "
        "restabilising complex unit-circle crossing — the spectral signature of a "
        "Neimark–Sacker bifurcation, with nonlinear conditions not verified — at "
        "about 6.5 yr under the exact held-measurement update (Proposition 8.1). The "
        "Euler-reported half-century crossing and its companion $-1$ crossing are "
        "command-step artefacts.",
        "s12-item5b")
    t = sub1(t,
        "the lower boundary resolves into a single fold at $\\tau = 5.5872362$ yr of "
        "one S-shaped branch",
        "the lower boundary resolves into a single fold near 5.6 yr of one S-shaped "
        "branch",
        "s12-item6a")
    t = sub1(t,
        "a second fold certified at the discrete-collocation level at "
        "$\\tau_{f2} = 64.4023272$ yr of a second S-branch",
        "a second fold certified at the discrete-collocation level near 64.4 yr of a "
        "second S-branch",
        "s12-item6b")
    t = sub1(t,
        "The saddle-node-of-periodic-orbits classification remains **provisional** "
        "against a crisis alternative.",
        "The saddle-node-of-periodic-orbits classification is stated at its "
        "certification tier in Section 9.2.",
        "s12-item6c")
    t = sub1(t,
        "so the 148.6–149.5 capture onset is a basin boundary rather than a fold",
        "so the capture onset near 149 yr is a basin boundary rather than a fold",
        "s12-item6d")
    t = sub1(t,
        "the link from the stable returning arm's last record ($\\tau = 64.438$) to "
        "that cycle over an $\\approx 84$-yr gap is an unverified conjecture",
        "the link from the stable returning arm's last record to that cycle over an "
        "$\\approx 84$-yr gap is an unverified conjecture",
        "s12-item6e")

    # ---------------- M3-B family-list definition (docket) ----------------
    t = sub1(t,
        "Four variants delimit the robustness of the results. No invariant set",
        "The reference member of the family is **M3-B (boundary-exact gated)** — the "
        "core (1) itself, whose multiplicative saturation gate enforces $E \\in "
        "[0, E_{\\max}]$ exactly (Theorem 2.1); its crossings, folds, and basins are "
        "the paper's reference records (Sections 5.1 and 9.3). Four further variants "
        "delimit the robustness of those results. No invariant set",
        "m3b-def")

    # ---------------- R20: MPF U-equation display + γ_U at first use ----------------
    t = sub1(t,
        "signed memory $\\dot Z = (-\\dot X - Z)/\\tau_m$, and the bounded effort law",
        "signed memory $\\dot Z = (-\\dot X - Z)/\\tau_m$, the detritus equation "
        "$\\dot U = m(X) - \\gamma_U U$ (the detritus compartment receives the full "
        "mortality flux $m(X) = dX + cX^2$ and exports it at the specific rate "
        "$\\gamma_U > 0$, yr$^{-1}$ — the equation the invariance argument below "
        "uses), and the bounded effort law",
        "mpf-udot")

    # ---------------- R20: §2.4 σ_geo and ε_U definitions ----------------
    t = sub1(t,
        "First, in the ideal large-reservoir limit $\\sigma_{\\mathrm{geo}} = 1$ the "
        "specialised system satisfies the working-core equations exactly",
        "First, in the ideal large-reservoir limit $\\sigma_{\\mathrm{geo}} = 1$ — "
        "where $\\sigma_{\\mathrm{geo}} \\in (0,1]$ is the geological-reservoir "
        "adequacy ratio, a dimensionless companion-ledger quantity measuring how far "
        "the geological reservoir sustains the working core's donor draw "
        "($\\sigma_{\\mathrm{geo}} = 1$ the ideal limit, $1 - \\sigma_{\\mathrm{geo}}$ "
        "the scale of the finite-reservoir perturbation) — the specialised system "
        "satisfies the working-core equations exactly",
        "s24-sigma-geo")
    t = sub1(t,
        "(a standard Tikhonov/Fenichel-type argument; Hale and Verduyn Lunel, 1993, "
        "Ch. 9, Diekmann et al., 1995) — and at the baseline",
        "(a standard Tikhonov/Fenichel-type argument; Hale and Verduyn Lunel, 1993, "
        "Ch. 9, Diekmann et al., 1995; $\\varepsilon_U$ is the fast-variable slaving "
        "parameter, of the order of the slow-to-fast timescale ratio $r/\\gamma_U$, "
        "with $\\gamma_U$ the detritus export rate of the MPF core, Section 2.3) — "
        "and at the baseline",
        "s24-eps-u")

    # ---------------- §5.1: Moore/Cloud citations + R19 G5 relocation site ----------------
    t = sub1(t,
        "no such full certificate is claimed here, and none is claimed for any "
        "global fold (Section 9, and the supplementary material).",
        "no such full certificate is claimed here, and none is claimed for any "
        "global fold (Section 9, and the supplementary material). The interval "
        "machinery itself is standard (Moore, 1979; Cloud, Moore, and Kearfott, "
        "2009). The pair is registered as gate G5 of the registration campaign (gate "
        "log deposited with the supplementary material, S9): the registered "
        "compute-core Hopf pair $3.666149$ / $150.358477$ yr — the base core (1)'s "
        "institutional-delay certificates, reproduced by the recovered compute core "
        "(Supplementary S9.5) — certifies this pair; it is a record of the compute "
        "core, not an object of the delayed-recruitment system of Section 7.",
        "s51-cites-g5")

    # ---------------- q*/p eigenvector rename (docket: q is catchability) ----------------
    t = sub1(t,
        "under unit Hermitian normalisation of the right eigenvector and "
        "$q^*\\Delta'(i\\omega)p = 1$:",
        "under unit Hermitian normalisation of the right eigenvector $v$ and its "
        "adjoint $w$, with the normalisation $w^*\\Delta'(i\\omega)v = 1$ ($w^*$ the "
        "conjugate transpose; the eigenvector pair is denoted $v, w$ so that $q$ "
        "remains the catchability throughout):",
        "qstar-p")

    # ---------------- R20: α, β in Remark 5.1's (H1) ----------------
    t = sub1(t,
        "proved analytically on the parameter set $\\alpha + \\eta\\beta < 1$, with "
        "the sweep-quantified margin",
        "proved analytically on the parameter set $\\alpha + \\eta\\beta < 1$ — where "
        "$\\alpha$ and $\\beta$ are the two coupling weights of the fast block's "
        "$K$–$L$ Jacobian displayed in Supplementary S5, so that the inequality is "
        "that block's uniform-Hurwitz condition — with the sweep-quantified margin",
        "alpha-beta")
    t = sub1(t,
        "(add $O(1 - \\sigma_{\\mathrm{geo}})$ for the finite reservoir)",
        "(add $O(1 - \\sigma_{\\mathrm{geo}})$ for the finite reservoir, "
        "$\\sigma_{\\mathrm{geo}}$ being the geological-reservoir adequacy ratio of "
        "Section 2.4)",
        "s53-sigma-recall")

    # ---------------- §6.2(b): define the Routh entry c ----------------
    t = sub1(t,
        "has first column entries $1, 1.0682, c > 0, c_0' > 0$.",
        "has first column entries $1,\\ 1.0682,\\ c,\\ c_0'$, where $c = "
        "(1.0682\\,c_1' - c_0')/1.0682$ is the standard third first-column entry of a "
        "cubic's Routh array (the quotient $(a_2a_1 - a_0)/a_2$ with $a_2 = 1.0682$, "
        "$a_1 = c_1'$, $a_0 = c_0'$), and both $c > 0$ and $c_0' > 0$.",
        "routh-c")

    # ---------------- §6.4: the 2/|C_E| sentence (docket) ----------------
    t = sub1(t,
        "so the crossing is a property of the Euler factor *combined with* the hold "
        "dynamics.",
        "so the crossing is a property of the Euler factor *combined with* the hold "
        "dynamics — and it sits within about $2\\%$ of the explicit-Euler stability "
        "limit of the scalar effort equation, $T_r < 2/|C_E| = 2.352$ yr (with "
        "$C_E = -0.850336$; the limit at which the scalar factor $1 + T_r C_E$ "
        "itself reaches $-1$), which makes the discretisation origin of the crossing "
        "self-evident.",
        "two-over-ce")

    # ---------------- R19: G5 removal from §7.6 ----------------
    t = sub1(t,
        "the nonlinear ground truth (G4), and the registered compute-core Hopf pair "
        "$3.666149$ / $150.358477$ (G5).",
        "and the nonlinear ground truth (G4).",
        "s76-g5-out")

    # ---------------- §8: consolidated table + growth rates + stock-mode ----------------
    t = sub1(t,
        "— confirming the DC-gain ($L(0) = 0$) loss of coupling.\n\n---\n\n"
        "## 9. Global Numerics at Declared Certification Levels",
        "— confirming the DC-gain ($L(0) = 0$) loss of coupling.\n\n" + TABLE_BLOCK +
        "\n\n---\n\n## 9. Global Numerics at Declared Certification Levels",
        "s8-table")

    # ---------------- §9.2: multiplier precision unfusion + changelog strip (a) ----
    t = sub1(t,
        "— cross $+1$ within $1.1\\times10^{-7}$ of the fold (small arm: $1.0192$ at "
        "$\\tau = 5.584$ falling to $0.9942$ at $5.587$; large arm: $0.2040$ at "
        "$\\tau = 4.0$ rising to $0.9692$ at $5.5815$).",
        "— cross $+1$ at the fold: the campaign's recorded crossing proximity is "
        "$1.1\\times10^{-7}$ in $\\tau$, the fold-location certificate is the "
        "Krawczyk enclosure above, and the multiplier records are corroboration at "
        "their own, coarser, precision (small arm: $1.0192$ at $\\tau = 5.584$ "
        "falling to $0.9942$ at $5.587$; large arm: $0.2040$ at $\\tau = 4.0$ rising "
        "to $0.9692$ at $5.5815$ — $\\tau$ recorded to three decimals, multipliers "
        "to four, so the tabulated points bracket the crossing without resolving it "
        "at the $10^{-7}$ proximity, which is the campaign's record, not an "
        "interpolation of the table).",
        "s92-fusion")
    t = sub1(t,
        "An earlier two-fold reading (basin collapse in $\\tau \\in [5.574, 5.576]$ "
        "yr versus a small-branch fold near $5.587$ yr, large-branch multiplier "
        "$0.964$ at $5.5815$) is not reproduced by the present computation: the "
        "registered record places the basin-bisection endpoint $0.011$ yr below the "
        "fold and returns large-branch multiplier $0.2040$ at $\\tau = 4.0$ (not "
        "$0.240$) and small-arm multiplier $1.0192$ at $5.584$ (not $1.0514$); on "
        "these points the earlier values are superseded by the registered record.",
        "The registered record places the basin-bisection endpoint $0.011$ yr below "
        "the fold and returns large-branch multiplier $0.2040$ at $\\tau = 4.0$ and "
        "small-arm multiplier $1.0192$ at $5.584$; superseded earlier values on "
        "these points are recorded in the version log, not in this section.",
        "s92-changelog-a")
    t = sub1(t,
        "the large-stock (H1) and near-equilibrium (H3) histories settle — reversing "
        "the earlier qualitative asymmetry.",
        "the large-stock (H1) and near-equilibrium (H3) histories settle.",
        "s92-changelog-b")
    t = sub1(t,
        "the depleted history is captured at $\\tau = 5.575$ (reversing the earlier "
        "asymmetry); every tested history settles",
        "the depleted history is captured at $\\tau = 5.575$; every tested history "
        "settles",
        "fig1-changelog")

    # ---------------- §9.2 upper-boundary changelog strips ----------------
    t = sub1(t,
        " — and the earlier provisional description of that boundary as a possible "
        "fold location is displaced by the basin record.",
        ".",
        "s92-changelog-c")
    t = sub1(t,
        "An earlier \"interior large family\" (residual $\\sim10^{-13}$ on $\\tau "
        "\\in [147.5, 160]$, amplitude $15.9$–$19.5$) was not re-tested here, under "
        "the independence discipline that forbids seeding a campaign from prior "
        "values. An earlier upper bracket $[148.125, 148.438]$ yr, a "
        "basin-bisection estimate of the capture onset, is not reproduced; the "
        "registered grids place the onset at $[148.6, 149.5]$ yr.",
        "The registered grids place the onset at $[148.6, 149.5]$ yr.",
        "s92-changelog-d")
    t = sub1(t,
        "($0.100$ at $\\tau = 150.31$ and $1.874$ at $\\tau = 130$, within $15\\%$ "
        "of the earlier estimates)",
        "($0.100$ at $\\tau = 150.31$ and $1.874$ at $\\tau = 130$)",
        "s92-changelog-e")
    t = sub1(t,
        "An earlier third family \"at $E \\ge E_{\\max}$ collocating down to $\\tau "
        "\\approx 144.5$\", reported as an inadmissible continuation branch, is "
        "displaced by the finding that the face-riding cycle is reached from "
        "admissible histories in the upper window:",
        "The face-riding cycle is reached from admissible histories in the upper "
        "window:",
        "s92-changelog-f")

    # ---------------- §9.3 M3-B changelog strips ----------------
    t = sub1(t,
        "both arms cross $+1$ there; the earlier two-fold reading — a stable "
        "large-cycle fold near $5.574$–$5.575$ yr and a separate small-branch fold "
        "near $5.587$ yr, multiplier $1.0514 \\to 0.998983$ — is superseded by the "
        "present record",
        "both arms cross $+1$ there; superseded earlier readings are recorded in "
        "the version log",
        "m3b-changelog-a")
    t = sub1(t,
        ", an earlier bracket $[148.125, 148.438]$ yr is not reproduced, and the "
        "fold type",
        ", and the fold type",
        "m3b-changelog-b")

    # ---------------- R22: four-state paragraph (§9.3) ----------------
    t = sub1(t,
        "The turnover stability boundary at $\\tau = 0$ is $\\omega_A^* \\approx "
        "0.001316298$ (gated $\\approx0.001330$), located by a 1798-point "
        "equilibrium sweep,",
        "The turnover stability boundary at $\\tau = 0$ is $\\omega_A^* \\approx "
        "0.001316$ (the sweep's recorded value is $0.001316298$; quoted at sweep "
        "resolution, not enclosure precision; gated $\\approx0.001330$), located by "
        "a 1798-point equilibrium sweep,",
        "r22-omega")
    t = sub1(t,
        "matches the four-state's upper fold bracket ($\\approx64.4$ yr, persistent "
        "orbit of amplitude $\\approx11$ at $64.5$, continuation failure by $64.25$) "
        "within $0.05\\%$ — the upper fold location is version-robust, the "
        "three-state's earlier $\\approx148$ yr reading having been a "
        "basin-boundary estimate — while the Hopf pair stays within a few percent",
        "falls inside the four-state's upper fold bracket $[64.25, 64.5]$ yr "
        "(persistent orbit of amplitude $\\approx11$ at $64.5$, continuation failure "
        "by $64.25$): reproduced to within the bracket width — the bracket spans "
        "$0.25$ yr, or $0.4\\%$ of the fold value, so the version-robustness of the "
        "upper fold location is a bracket-resolution statement — while the Hopf "
        "pair stays within a few percent",
        "r22-bracket")

    # ---------------- R21: MPF paragraph relocation (§9.3) ----------------
    t = sub1(t,
        "The absence of a baseline Hopf is parametric: Hopf roots first appear at "
        "$\\eta_{\\mathrm{crit}} \\approx 2.337$, with two interleaving pairs over "
        "$\\eta \\in (2.337, 3]$ (at $\\eta = 2.5$: $\\approx0.6$, $54.2$, $92.9$, "
        "$113.1$ yr; at $\\eta = 3.0$ one pair spans $\\approx4.5$–$41.2$ yr; at the "
        "out-of-range $\\eta = 10$: $17.568$/$18.362$ yr with a "
        "supercritical-consistent onset, exponent $0.59$, inferred). Above $\\tau_+$ "
        "at $\\eta = 10$ the attractor is diagnosed as irregular slow-fast "
        "intermittency, with diagnostics inconsistent with a simple period-one or "
        "low-period orbit — the underlying global bifurcation mechanism (a "
        "homoclinic connection among the candidates) is unresolved. The "
        "diagnostics: a broad onset-interval spectrum with no sharp peak, a thin "
        "map-like Poincaré section on $Z$-crossings, inter-excursion-interval "
        "coefficient of variation $1.58$, and return-map anticorrelation $r = "
        "-0.47$ — with the large-amplitude time fraction rising monotonically from "
        "$0\\%$ at $\\tau = 18.4$ to $100\\%$ by $\\tau \\approx 22$ and no sharp "
        "second threshold separating quiet and captured regimes; the present "
        "diagnostics neither identify a homoclinic mechanism nor exclude torus "
        "breakdown. The pair-birth structure behind the interleaving is registered: "
        "the large-delay pair is born at $\\eta_{\\mathrm{crit}} \\approx 2.337$ "
        "($\\tau_- \\approx 71.2$, $\\tau_+ \\approx 72.9$ yr) and migrates downward "
        "as $\\eta$ rises, while the small-delay pair is born at $\\eta \\approx "
        "2.454$ with $\\tau_- \\to 0$ at its onset. A sigmoid-gated effort variant "
        "of the same ecological core was screened across more than $300$ "
        "parameterisations without finding a genuine delay-induced Hopf — a "
        "numerical negative result over the sampled domain, not a structural "
        "impossibility theorem.",
        "The absence of a baseline Hopf is parametric: Hopf roots first appear at "
        "$\\eta_{\\mathrm{crit}} \\approx 2.337$; above $\\tau_+$ at $\\eta = 10$ "
        "the attractor is diagnosed as irregular slow-fast intermittency "
        "(inter-excursion-interval coefficient of variation $1.58$, return-map "
        "anticorrelation $r = -0.47$; the underlying global bifurcation mechanism is "
        "unresolved). The full $\\eta_{\\mathrm{crit}}$ sweep with the interleaving "
        "pair values and the pair-birth structure, the intermittency diagnostics, "
        "and the sigmoid-gated effort screen (more than $300$ parameterisations "
        "without finding a genuine delay-induced Hopf — a numerical negative result "
        "over the sampled domain, not a structural impossibility theorem) are "
        "relocated to the supplement (S11), with Section 10.4 carrying the screen's "
        "loop-gain reading.",
        "r21-mpf")

    # ---------------- §9.5: literature r-range scoped to the paper's own computation ----
    t = sub1(t,
        "The literature range $r \\in [0.005, 0.4]$ yr$^{-1}$ is wider than the "
        "instability window.",
        "Reported literature ranges of intrinsic growth rates are wider than the "
        "instability window; the quoted $r \\in [0.005, 0.4]$ yr$^{-1}$ range is not "
        "independently sourced in this paper, so the identification warning is "
        "scoped to the paper's own computed two-crossing window, $r \\in (0.008, "
        "0.06)$ yr$^{-1}$ (Section 9.3) — against any plausible empirical spread of "
        "$r$, most assessed stocks fall outside the window.",
        "r-range")

    # ---------------- R22: §10.1 version-robust repeat ----------------
    t = sub1(t,
        "the upper fold is version-robust at $\\approx64.4$ yr (certified "
        "three-state second fold $64.4023$; four-state bracket $[64.25, 64.5]$)",
        "the upper fold is version-robust at bracket resolution ($\\approx64.4$ yr: "
        "certified three-state second fold $64.4023$; four-state bracket "
        "$[64.25, 64.5]$, whose $0.4\\%$ width sets that resolution)",
        "r22-s101")

    # ---------------- Halanay η → ν (docket) ----------------
    t = sub1(t,
        "with decay rate the unique $\\eta > 0$ solving $\\eta = \\alpha_0 - "
        "\\beta_0 e^{\\eta\\tau}$ (Halanay, 1966).",
        "with decay rate the unique $\\nu > 0$ solving $\\nu = \\alpha_0 - "
        "\\beta_0 e^{\\nu\\tau}$ (Halanay, 1966; the decay rate is denoted $\\nu$ "
        "here so that $\\eta$ remains the effort-response coefficient of Section 2 "
        "throughout).",
        "halanay-nu")

    # ---------------- §10.4: 300-screen pointer (R21, second site) ----------------
    t = sub1(t,
        "a search of more than 300 randomised parameterisations (Newton eigenvalue "
        "tracking, joint modulus minimisation, nonlinear integration) found no "
        "genuine imaginary-axis root of the general feedback equation (14).",
        "a search of more than 300 randomised parameterisations found no genuine "
        "imaginary-axis root of the general feedback equation (14) (the screen "
        "record — the method stack of Newton eigenvalue tracking, joint modulus "
        "minimisation, and nonlinear integration, and the nonexistence reading — is "
        "deposited in the supplement, S11, which also carries the relocated MPF "
        "sweep and intermittency records).",
        "s104-screen")

    # ---------------- §11.4: S-for-stock fix ----------------
    t = sub1(t,
        "the raw gap $|\\hat S - S|$ is not itself an operational statistic",
        "the raw gap $|\\hat N - N|$ between an estimated and the true stock "
        "(written in the paper's stock symbol, since $S(N)$ is the yield) is not "
        "itself an operational statistic",
        "s-for-stock")

    # ---------------- §11.6: grant-text trim ----------------
    t = sub1(t,
        "The following are stated as open problems with declared gaps: persistence "
        "of a transverse fold of periodic orbits under small typed coupling "
        "(requires a verified fold baseline, spectral separation, and regularity of "
        "the infinite-dimensional Poincaré map); the RFDE/hybrid "
        "transition-persistence analogue; an $n$-patch super-equilibrium criterion "
        "(two-patch instances verified, the $n$-patch equivalence open); a "
        "variable-time delayed-hybrid information kernel with compact "
        "piecewise-history phase space; a restricted delay-separation principle for "
        "modularly identified governance loops; and — in the direction suggested by "
        "the mobilising channel's autocatalytic mechanism — an exergy-limited "
        "controller class for which the loop-gain exclusion of Theorem 10.1 can be "
        "established analytically (a declared conjecture: sufficiently low "
        "deployable exergy reduces the loop gain below every admissible "
        "Hopf-frequency modulus condition; not universal — depletion of "
        "institutional capacity may also disable protective action or create "
        "hysteresis).",
        "Two genuine next theorems are stated with their declared gaps, with the "
        "first Lyapunov coefficient of the exact-hold map's Neimark–Sacker crossing "
        "as the matching open computation: the Church–Lessard upgrade of the Hopf "
        "certificates (Section 11.3's first stated open task, taken together with "
        "the continuum off-grid residual stage of both folds), and persistence of a "
        "transverse fold of periodic orbits under small typed coupling (requires a "
        "verified fold baseline, spectral separation, and regularity of the "
        "infinite-dimensional Poincaré map). The further programme directions "
        "carried by the open-problem register — an RFDE/hybrid "
        "transition-persistence analogue, an $n$-patch super-equilibrium criterion, "
        "a variable-time delayed-hybrid information kernel, a restricted "
        "delay-separation principle for modularly identified governance loops, and "
        "an exergy-limited controller class with its declared conjecture and "
        "non-universality caveat — are recorded in the supplement's open-problem "
        "register (S6) and are not elaborated here: none connects to a theorem "
        "proved in this paper.",
        "s116-trim")

    # ---------------- supplementary pointer: v3 → v4 + S11 ----------------
    t = sub1(t,
        "are provided in the accompanying file `paper4_supplementary_v3.md` "
        "(S1–S10).",
        "are provided in the accompanying file `paper4_supplementary_v4.md` "
        "(S1–S10), together with the relocated MPF material of S11 (the "
        "$\\eta_{\\mathrm{crit}}$ sweep and pair-birth structure, the slow-fast "
        "intermittency diagnostics, and the sigmoid-gated effort screen record; "
        "wave-4 relocation from Sections 9.3 and 10.4).",
        "supp-pointer")

    # ================= mechanical checks =================
    v27 = t
    body = "\n".join(l for l in v27.splitlines()
                     if not l.startswith("*Version log (v27).*"))

    # R18: the wrong pointer is gone (it may survive only as a quotation inside
    # the version log line, as with the E1 build's convention); the corrected
    # pointer is present
    if "Sections 2–9" in body:
        raise SystemExit("FAIL: R18 'Sections 2–9' still present in the body")
    if "occupies Sections 2–5" not in v27:
        raise SystemExit("FAIL: R18 corrected pointer missing")
    # §1.1's other pointer (fixed at v26) still correct
    if "The phase-stabilised window of Section 5.1" not in v27:
        raise SystemExit("FAIL: v26's Section 5.1 pointer lost")
    # Cor 6.1's proof still uses the deployment pair (v26 fix retained)
    if "no imaginary root exists for any $(\\tau_M, \\tau_p)$" not in v27:
        raise SystemExit("FAIL: Cor 6.1 proof (τ_M, τ_p) pair lost")

    # R19: G5 out of §7, present at its new §5.1 site, numbers move unaltered
    if "and the registered compute-core Hopf pair $3.666149$ / $150.358477$ (G5)" in v27:
        raise SystemExit("FAIL: R19 G5 sentence still in §7.6 list")
    s7 = v27[v27.find("## 7. The Delayed-Recruitment"):v27.find("## 8. The Review Interval")]
    if "G5" in s7:
        raise SystemExit("FAIL: R19 any G5 mention left inside §7")
    for needle in [
        "Gate G5" if False else "gate G5 of the registration campaign",
        "a record of the compute core, not an object of the delayed-recruitment "
        "system of Section 7",
        "reproduced by the recovered compute core (Supplementary S9.5)",
    ]:
        if needle not in v27:
            raise SystemExit(f"FAIL: R19 relocation sentence missing: {needle!r}")
    if "the nonlinear ground truth (G4)." not in v27:
        raise SystemExit("FAIL: R19 §7.6 list closing on G4")

    # R20: definitions at first use + the displayed Ů equation
    for needle in [
        "geological-reservoir adequacy ratio",
        "the detritus equation $\\dot U = m(X) - \\gamma_U U$",
        "the fast-variable slaving parameter",
        "$\\alpha$ and $\\beta$ are the two coupling weights of the fast block's "
        "$K$–$L$ Jacobian",
        "the detritus export rate of the MPF core",
    ]:
        if needle not in v27:
            raise SystemExit(f"FAIL: R20 definition missing: {needle!r}")

    # R21: pointers keep the key numbers; the relocated detail is gone from §9.3
    s93 = v27[v27.find("**MPF (primitive-flux core).**"):v27.find("### 9.4")]
    for needle in ["$\\eta_{\\mathrm{crit}} \\approx 2.337$",
                   "coefficient of variation $1.58$", "anticorrelation $r = -0.47$",
                   "more than $300$ parameterisations"]:
        if needle not in s93:
            raise SystemExit(f"FAIL: R21 §9.3 pointer lost: {needle!r}")
    for gone in ["two interleaving pairs over", "pair-birth structure behind the "
                 "interleaving is registered", "no sharp peak",
                 "rising monotonically from $0\\%$ at $\\tau = 18.4$"]:
        if gone in s93:
            raise SystemExit(f"FAIL: R21 relocated detail still in §9.3: {gone!r}")
    if "the supplement, S11" not in v27:
        raise SystemExit("FAIL: R21 §10.4 S11 pointer missing")

    # R22: honest precision restatements (the old phrasing may survive only as
    # a quotation inside the version log line)
    if "within $0.05\\%$" in body:
        raise SystemExit("FAIL: R22 'within 0.05%' still present in the body")
    for needle in ["reproduced to within the bracket width",
                   "bracket-resolution statement",
                   "quoted at sweep resolution, not enclosure precision",
                   "version-robust at bracket resolution"]:
        if needle not in v27:
            raise SystemExit(f"FAIL: R22 restatement missing: {needle!r}")

    # Presentation tail
    if "cross $+1$ within $1.1\\times10^{-7}$ of the fold" in v27:
        raise SystemExit("FAIL: §9.2 precision fusion still present")
    if "corroboration at" not in v27 or "not an interpolation of the table" not in v27:
        raise SystemExit("FAIL: §9.2 unfused wording missing")
    for gone in ["An earlier two-fold reading", "is superseded by the present record",
                 "An earlier \\\"interior large family\\\"", "An earlier upper bracket",
                 "An earlier third family", "reversing the earlier",
                 "the earlier provisional description", "the three-state's earlier",
                 "within $15\\%$ of the earlier estimates", "(not $0.240$)",
                 "(not $1.0514$)", "forbids seeding"]:
        if gone.replace('\\"', '"') in body:
            raise SystemExit(f"FAIL: changelog narration still in body: {gone!r}")
    # the retired numbers survive in the version log (cite, don't drop)
    log = v27[v27.find("*Version log (v27).*"):v27.find("\n\n## Abstract")]
    for needle in ["148.125", "1.0514", "15.9", "144.5", "0.998983", "5.574"]:
        if needle not in log:
            raise SystemExit(f"FAIL: retired changelog number missing from the "
                             f"version log: {needle!r}")
    # §1.2 stripped of the computation-log digits
    s12 = v27[v27.find("### 1.2 Contributions"):v27.find("### 1.3 Organization")]
    for gone in ["0142739", "150.358477", "5.5872362", "64.4023272", "0.9838",
                 "1.00055", "1.00035", "2.306", "47.536", "79.143", "148.6",
                 "64.438", "provisional"]:
        if gone in s12:
            raise SystemExit(f"FAIL: §1.2 still carries {gone!r}")
    for keep in ["near 3.7 and 150 yr", "about 6.5 yr", "near 5.6 yr", "near 64.4 yr",
                 "capture onset near 149 yr"]:
        if keep not in s12:
            raise SystemExit(f"FAIL: §1.2 rounded form missing: {keep!r}")
    # M3-B defined; Routh c defined; Halanay ν; v/w; |N̂ − N|
    for needle in ["**M3-B (boundary-exact gated)**",
                   "$c = (1.0682\\,c_1' - c_0')/1.0682$",
                   "the unique $\\nu > 0$ solving $\\nu = \\alpha_0 - \\beta_0 "
                   "e^{\\nu\\tau}$",
                   "$w^*\\Delta'(i\\omega)v = 1$",
                   "$|\\hat N - N|$"]:
        if needle not in v27:
            raise SystemExit(f"FAIL: presentation-tail fix missing: {needle!r}")
    if "$q^*\\Delta'(i\\omega)p = 1$" in v27:
        raise SystemExit("FAIL: q*/p collision still present")
    if "$|\\hat S - S|$" in v27:
        raise SystemExit("FAIL: S-for-stock collision still present")
    # §11.6 trimmed
    if "The following are stated as open problems with declared gaps" in v27:
        raise SystemExit("FAIL: §11.6 grant list untrimmed")
    if "Two genuine next theorems" not in v27:
        raise SystemExit("FAIL: §11.6 trimmed form missing")
    # §8 additions
    for needle in ["**The consolidated sampled-data record (channel × scheme × "
                   "review interval).**",
                   "$2/|C_E| = 2.352$ yr",
                   "e-folding times of roughly $1800$ and $2900$ review cycles",
                   "is that stock mode, only weakly coupled by the controller"]:
        if needle not in v27:
            raise SystemExit(f"FAIL: §8 table-layer item missing: {needle!r}")
    # citations added
    for needle in ["(Zhang, Shen, and Chen, 2013)", "(Moore, 1979; Cloud, Moore, "
                   "and Kearfott, 2009)"]:
        if needle not in v27:
            raise SystemExit(f"FAIL: uncited reference not cited: {needle!r}")
    # r-range scoped
    if "not independently sourced in this paper" not in v27:
        raise SystemExit("FAIL: §9.5 r-range scoping missing")
    # supplementary pointer updated
    if "paper4_supplementary_v3.md" in v27:
        raise SystemExit("FAIL: stale supplementary pointer v3")
    if "paper4_supplementary_v4.md" not in v27:
        raise SystemExit("FAIL: supplementary pointer v4 missing")

    # ---- frozen-value byte-identity / count bookkeeping ----
    # §5.1's certified table row byte-identical and unique in both versions
    row = ("| M3-B (gated), interval-certified | $\\tau_- \\in [3.6661490142739, "
           "3.6661490142743]$, $\\tau_+ \\in [150.3584773101408, 150.3584773101421]$ |")
    if v26.count(row) != 1 or v27.count(row) != 1:
        raise SystemExit("FAIL: §5.1 certified row not byte-identical and unique")
    exact_counts = {
        # needle: (v26, v27) — v27 counts document every change
        "64.402327203368": (2, 2),      # §9.2/§9.3 certificates untouched
        "64.402327203372": (2, 2),      # §9.2/§9.3 certificates untouched
        "5.587236198689": (1, 1),       # Krawczyk box untouched
        "5.587236198691": (1, 1),       # Krawczyk box untouched
        "64.402327895": (1, 1),         # turning-point stall untouched
        "0.001316298": (1, 1),          # sweep value retained (restated honestly)
        "150.358477": (7, 6),           # -2: §1.2's two 13-digit forms (mandated
                                         #      strip); G5 pair moves §7.6→§5.1
                                         #      intact; +1 quoted in the version log
        "3.6661490142739": (2, 1),      # §5.1's row retained; §1.2's copy stripped
        "150.3584773101408": (2, 1),    # ditto
        "150.3584773101421": (2, 1),    # ditto
        "5.5872362": (6, 5),            # §1.2's fold digits stripped
        "64.4023272": (7, 6),           # §1.2's fold digits stripped
        "148.6": (9, 8),                # §1.2's capture onset stripped
        "64.438": (4, 3),               # §1.2's last-record digit stripped
        "0.9838": (4, 6),               # §6.4/§8 records intact; the table
                                         # re-states it twice and the stock-mode
                                         # reading once (all verbatim)
        "1.00055": (2, 2), "1.00035": (2, 2),
        "47.536": (8, 8), "79.143": (7, 7), "2.306": (7, 7),
        "0.9846": (1, 2), "0.1746": (1, 2), "0.1647": (1, 2),
        "6.7279": (1, 2), "0.9928": (1, 2), "0.9855": (1, 2), "0.1699": (1, 2),
        "0.9967": (2, 4),
    }
    for needle, (c26, c27) in exact_counts.items():
        if v26.count(needle) != c26:
            raise SystemExit(f"FAIL: v26 baseline count for {needle!r} is "
                             f"{v26.count(needle)}, expected {c26}")
        if v27.count(needle) != c27:
            raise SystemExit(f"FAIL: v27 count for {needle!r} is {v27.count(needle)}, "
                             f"expected {c27} (v26 had {c26})")
    # the three previously-uncited references are still listed (and now cited)
    for ref in ["Zhang, G.D., Shen, Y., Chen, B.S., 2013.",
                "Cloud, M.J., Moore, R.E., Kearfott, R.B., 2009.",
                "Moore, R.E., 1979."]:
        if v27.count(ref) != 1:
            raise SystemExit(f"FAIL: reference entry not unique: {ref!r}")
    # Abstract byte-identical
    a26 = v26[v26.find("## Abstract"):v26.find("## 1. Introduction")]
    a27 = v27[v27.find("## Abstract"):v27.find("## 1. Introduction")]
    if a26 != a27:
        raise SystemExit("FAIL: abstract changed")
    # line-count bookkeeping: the only line additions are the §8 consolidated
    # table block (12 lines: caption, blank, header, separator, six rows, blank,
    # readings) plus one blank separator line
    if len(v27.splitlines()) != len(v26.splitlines()) + 13:
        raise SystemExit(f"FAIL: line count changed {len(v26.splitlines())} -> "
                         f"{len(v27.splitlines())} (expected +13, the §8 table)")

    open(DST, "w", encoding="utf-8").write(v27)
    return v26, v27


def append_supplement():
    s = open(SUP, encoding="utf-8").read()
    if "## S11." in s:
        # Idempotent re-run: the S11 append must be byte-identical to the
        # expected block and sit at the very end of the file (any other S11
        # content fails loudly).
        if not s.endswith(S11_SECTION):
            raise SystemExit("FAIL: supplement carries an S11 block that does not "
                             "match the expected append (manual edit?)")
        s = s[:-len(S11_SECTION)]
        if "## S11." in s:
            raise SystemExit("FAIL: more than one S11 block in the supplement")
    if not s.endswith("\n"):
        s += "\n"
    s += S11_SECTION
    # checks: the relocated numbers are all present exactly as in the main text's v26
    for needle in ["$\\eta_{\\mathrm{crit}} \\approx 2.337$", "(2.337, 3]$",
                   "$54.2$, $92.9$, $113.1$ yr", "$17.568$/$18.362$ yr",
                   "exponent $0.59$", "$\\tau_- \\approx 71.2$", "$\\eta \\approx 2.454$",
                   "coefficient of variation $1.58$", "$r = -0.47$",
                   "from $0\\%$ at $\\tau = 18.4$ to $100\\%$ by $\\tau \\approx 22$",
                   "Newton eigenvalue tracking, joint modulus minimisation, "
                   "nonlinear integration",
                   "more than $300$ parameterisations"]:
        if needle not in s:
            raise SystemExit(f"FAIL: S11 relocated record missing {needle!r}")
    open(SUP, "w", encoding="utf-8").write(s)


def main():
    v26, v27 = build_paper()
    append_supplement()
    print(f"OK: wrote {DST}")
    print(f"OK: appended S11 to {SUP}")
    print(f"    v26 {len(v26)} chars -> v27 {len(v27)} chars; "
          f"lines {len(v26.splitlines())} -> {len(v27.splitlines())}")
    print("    G5 relocated §7.6 -> §5.1; MPF material -> supplement S11; "
          "all mechanical checks passed.")


if __name__ == "__main__":
    main()
