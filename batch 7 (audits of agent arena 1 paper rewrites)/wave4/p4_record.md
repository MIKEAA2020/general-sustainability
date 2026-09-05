# P4 wave-4 implementation record (Task 73-d)

**Paper:** `arena agent 1/paper rewrites/paper4_delay_dynamics_v26.md` → **`paper4_delay_dynamics_v27.md`**
**Build:** `batch 7 (audits of agent arena 1 paper rewrites)/apply_batch7_wave4_p4.py` (fail-loud,
asserted-once anchors; 28 `sub1` replacements + the version-log splice; mechanical checks below).
**Supplement:** `paper4_supplementary_v4.md` — the ONE allowed edit to an existing supplementary
file: a clearly-labelled append (S11, 17 inserted lines, 0 deletions; git-verified append-only).
**Line numbers** are v26 → v27 (v27 gains 13 lines from the §8 consolidated-table block:
666 → 679). Method: every item was verified open at v26 by direct read/grep before the edit;
no new computation was performed anywhere (the 2/|C_E| = 2.352, e-folding ≈ 1800/2900, and
stock-mode figures are one-line arithmetic restatements of constants already printed in
§6.2/§8 — noted per item below).

---

## R-items (the joint evaluation's P4 wave-4 list)

### R18 [claude] §1.1's second cross-ref error — IMPLEMENTED
- v26 L23: "whose bifurcation analysis occupies Sections 2–9" (§6 is the protective channel,
  §8 sample-and-hold, §9 global numerics — the pointer was wrong).
- v27 L23: "whose local bifurcation analysis occupies Sections 2–5 (the protective channel is
  Section 6; sample-and-hold review, Section 8; the global numerics, Section 9)".
- Mechanical: "Sections 2–9" absent from the body (it survives only as a quotation inside the
  version-log line, per the E1 build's convention); "occupies Sections 2–5" present.
- The *other* §1.1 pointer (claude's "phase-stabilised window of Section 4") was already fixed
  at v26 — **ALREADY PRESENT** at v27 L23: "The phase-stabilised window of Section 5.1" (verified;
  v26's version log records the wave-2 fix).

### R19 [grok, flagged three times] G5 pair imported into §7.6 — IMPLEMENTED (relocation)
- Old site: v26 L418 (§7.6's registration list): "…, the nonlinear ground truth (G4), and the
  registered compute-core Hopf pair $3.666149$ / $150.358477$ (G5)."
- New site: v27 **L226** (§5.1, immediately after the certification paragraph that scopes the
  enclosures, i.e. where the Hopf pair is certified — the §5.1 interval-certified table row is
  at v27 L224): "The pair is registered as gate G5 of the registration campaign (gate log
  deposited with the supplementary material, S9): the registered compute-core Hopf pair
  $3.666149$ / $150.358477$ yr — the base core (1)'s institutional-delay certificates,
  reproduced by the recovered compute core (Supplementary S9.5) — certifies this pair; it is a
  record of the compute core, not an object of the delayed-recruitment system of Section 7."
- The §7.6 list now closes on G4: v27 L418 "…, and the nonlinear ground truth (G4)." — §7
  carries **no G5 mention at all** (checked: the §7 span is G-free apart from G2–G4).
- The relocation matches the supplement's own record (S9.5 "Compute-core self-check (G5)":
  the recovered compute core reproduces the committed certificates 3.666149/150.358477) and
  grok's fix ("G5 does not belong in this section"). The numbers moved unaltered: grep-count
  "150.358477" 7 → 6 (−2 from the mandated §1.2 strip; the §7.6 copy moved to §5.1 intact;
  +1 quoted in the version log).

### R20 [claude] Undefined symbols where used — IMPLEMENTED
- **σ_geo** (first use §2.4): v27 L110 defines it at first use — "where
  $\sigma_{\mathrm{geo}} \in (0,1]$ is the geological-reservoir adequacy ratio, a dimensionless
  companion-ledger quantity measuring how far the geological reservoir sustains the working
  core's donor draw ($\sigma_{\mathrm{geo}} = 1$ the ideal limit, $1 - \sigma_{\mathrm{geo}}$
  the scale of the finite-reservoir perturbation)" — phrased exactly on the paper's own
  perturbation statement, no invented content. A recall is added at §5.3's use (v27 L252:
  "…, $\sigma_{\mathrm{geo}}$ being the geological-reservoir adequacy ratio of Section 2.4").
- **γ_U** (first use §2.3's MPF invariance argument): defined with the displayed equation —
  v27 L106 now displays the MPF detritus equation **$\dot U = m(X) - \gamma_U U$** ("the
  detritus compartment receives the full mortality flux $m(X) = dX + cX^2$ and exports it at
  the specific rate $\gamma_U > 0$, yr$^{-1}$ — the equation the invariance argument below
  uses"). This is exactly the equation the invariance computation
  $\frac{d}{dt}(X+U) = -qEX - \gamma_U U$ requires (Ṅ = g − m − h at A = 0; U̇ = m − γ_U U).
- **ε_U** (§2.4): v27 L110 defines it inside the existing citation parenthetical —
  "$\varepsilon_U$ is the fast-variable slaving parameter, of the order of the slow-to-fast
  timescale ratio $r/\gamma_U$, with $\gamma_U$ the detritus export rate of the MPF core,
  Section 2.3" — matching the sentence's own "fast-variable slaving parameter $r/\gamma_U$".
- **α, β** (Remark 5.1's H1): v27 L242 — "where $\alpha$ and $\beta$ are the two coupling
  weights of the fast block's $K$–$L$ Jacobian displayed in Supplementary S5, so that the
  inequality is that block's uniform-Hurwitz condition" (S5's K–L block carries exactly this
  determinant/trace structure with the iff condition $\alpha + \eta\beta < 1$; the definition
  adds no new mathematics).
- The MPF **Ů equation** is now displayed (see γ_U above) — claude's "a $\dot U$ equation [is]
  used in the invariance argument but never displayed" is closed.

### R21 [grok A23 + claude] MPF material to the supplement — IMPLEMENTED
- **Supplement append** (the one allowed edit to an existing supplementary file):
  `paper4_supplementary_v4.md` gains **S11 "Relocated MPF Material (Wave-4 Relocation)"**
  (S11.1 the η_crit sweep + pair-birth structure; S11.2 the slow-fast intermittency
  diagnostics; S11.3 the sigmoid-gated effort screen), with a clearly-labelled header noting
  the relocation, that every value is reproduced verbatim from the main text's v26, and that
  nothing is recomputed. Git diff: 17 insertions, 0 deletions (append-only, verified).
- **Main text pointers** (one sentence each, keeping the key numbers — cite, don't drop):
  - §9.3 (v27 L502): "Hopf roots first appear at $\eta_{\mathrm{crit}} \approx 2.337$; above
    $\tau_+$ at $\eta = 10$ the attractor is diagnosed as irregular slow-fast intermittency
    (inter-excursion-interval coefficient of variation $1.58$, return-map anticorrelation
    $r = -0.47$; …). The full $\eta_{\mathrm{crit}}$ sweep with the interleaving pair values
    and the pair-birth structure, the intermittency diagnostics, and the sigmoid-gated effort
    screen (more than $300$ parameterisations without finding a genuine delay-induced Hopf …)
    are relocated to the supplement (S11), with Section 10.4 carrying the screen's loop-gain
    reading."
  - §10.4 (v27 L569): the screen statement keeps "more than 300 randomised parameterisations …
    found no genuine imaginary-axis root" and adds the deposit pointer "(the screen record —
    the method stack of Newton eigenvalue tracking, joint modulus minimisation, and nonlinear
    integration, and the nonexistence reading — is deposited in the supplement, S11 …)";
    §10.4's interpretation sentences stay where they belong.
- Site verification: the "more than 300 parameterisations" fact stood at exactly two v26 sites
  — §9.3 (L489, the MPF paragraph) and §10.4 (L556). The docket's "§9.6 region" label is read
  as the second of these two sites: §9.6 (the scaffold companion) carries no 300-screen fact
  (verified by grep; §9.6's searches are the scaffold_hopf_search scans). Both actual sites
  are dispositioned above.
- The supplementary-material pointer (v27 L679) now names `paper4_supplementary_v4.md`
  (v26 pointed at the stale v3) and S11's contents. **paper4_supplementary_v4.md was
  modified** — this is the ONE allowed append; all prior paper versions are untouched
  (git status: v26 unmodified).

### R22 [grok] "within 0.05%" beside a 0.4%-wide bracket and a 7-digit ω_A^* — IMPLEMENTED
- v26 L487 (§9.3 four-state): "matches the four-state's upper fold bracket … within $0.05\%$ —
  the upper fold location is version-robust, the three-state's earlier ≈148 yr reading…".
- v27 L500: "falls inside the four-state's upper fold bracket $[64.25, 64.5]$ yr …: reproduced
  to within the bracket width — the bracket spans $0.25$ yr, or $0.4\%$ of the fold value, so
  the version-robustness of the upper fold location is a bracket-resolution statement".
- **ω_A^* at sweep resolution**: v27 L500 — "$\omega_A^* \approx 0.001316$ (the sweep's
  recorded value is $0.001316298$; quoted at sweep resolution, not enclosure precision; gated
  $\approx0.001330$)" — the 7-digit value stays in the record, honestly labelled (the
  0.001316298 grep-count is unchanged: 1).
- **§10.1's repeat** (grok: "§10.1 repeats it"): v27 L541 — "version-robust at bracket
  resolution (… four-state bracket $[64.25, 64.5]$, whose $0.4\%$ width sets that resolution)".

---

## Presentation-tail docket (each verified open at v26 first)

| Item | Disposition | Evidence (v26 → v27) |
|---|---|---|
| §9.2 multiplier digits / 1.1×10⁻⁷ precision fusion | **IMPLEMENTED** | v26 L468 fused "cross $+1$ within $1.1\times10^{-7}$ of the fold (small arm: 1.0192 at 5.584 …)" into one precision. v27 L481 separates them: "the campaign's recorded crossing proximity is $1.1\times10^{-7}$ in $\tau$, the fold-location certificate is the Krawczyk enclosure above, and the multiplier records are corroboration at their own, coarser, precision (… — $\tau$ recorded to three decimals, multipliers to four, so the tabulated points bracket the crossing without resolving it at the $10^{-7}$ proximity, which is the campaign's record, not an interpolation of the table)". Every number retained; grok's A19 ("the Krawczyk box is the certificate; the multiplier table is corroboration. Don't fuse them") and claude's digit note are both answered without new digits (the "no new computations" rule bars regenerating the multiplier table at higher precision — claude's ask for more digits is declined on that ground and the honest coarseness disclosure stands in its place). |
| Revision-history changelog narration in the main text [both] | **IMPLEMENTED** | Six-plus passages stripped from §9.2/§9.3: v26 L468 (two-fold reading + "(not 0.240)"/"(not 1.0514)" + "superseded by the registered record"), L470 ("reversing the earlier qualitative asymmetry"), L475 (Figure 1 caption "(reversing the earlier asymmetry)"), L477 ("the earlier provisional description … is displaced", the "interior large family" + independence-discipline passage, "An earlier upper bracket [148.125, 148.438] … is not reproduced", "within 15% of the earlier estimates", "An earlier third family … is displaced"), L483 (M3-B's "the earlier two-fold reading — … multiplier $1.0514 \to 0.998983$ — is superseded", "an earlier bracket … is not reproduced"), L487 ("the three-state's earlier ≈148 yr reading"). All retired numbers are preserved in the one-line version-log note (v27 L3), per the audits' "put superseded numbers in a supplement changelog" / the task's "one-line version-log note" — checked: 148.125, 1.0514, 0.998983, 15.9, 144.5, 5.574, 0.964 all present in the log, absent from the body. |
| §1.2 digit stripping [grok + claude: "an introduction is not a computation log"] | **IMPLEMENTED** | v27 §1.2 (L33, L37, L39): 13-digit endpoints → "near 3.7 and 150 yr … with the 13-digit enclosures displayed in Section 5.1's table" (also correcting the stale "(Section 4.1)" pointer to the table's actual site); ρ values ($0.9838$, $1.00055$, $1.00035$) → "spectral radius below one" / "just above one under both the Euler and the exact update"; 2.306 → "near 2.3 yr"; 6.50 → "about 6.5 yr" (the abstract's own rounded form); 47.536/79.143 → "the Euler-reported half-century crossing and its companion $-1$ crossing"; fold digits 5.5872362/64.4023272 → "near 5.6 yr"/"near 64.4 yr"; 148.6–149.5 → "capture onset near 149 yr"; ($\tau = 64.438$) → "last record"; "remains **provisional** against a crisis alternative" → "is stated at its certification tier in Section 9.2". Full precision remains in §5.1's table row and §9 (grep-counts asserted: "64.402327203368" 2→2, "5.587236198689" 1→1, the certified row byte-identical and unique). |
| M3-B never defined | **IMPLEMENTED** | v27 L99 (§2.3's family list): "The reference member of the family is **M3-B (boundary-exact gated)** — the core (1) itself, whose multiplicative saturation gate enforces $E \in [0, E_{\max}]$ exactly (Theorem 2.1); its crossings, folds, and basins are the paper's reference records (Sections 5.1 and 9.3). Four further variants delimit the robustness of those results." (claude: "'M3-B' (gated) is used in the §5.1 table but is not a member of the §2.3 family list".) |
| Undefined "c > 0" Routh entry (§6.2(b)) | **IMPLEMENTED** | v27 L328: "first column entries $1,\ 1.0682,\ c,\ c_0'$, where $c = (1.0682\,c_1' - c_0')/1.0682$ is the standard third first-column entry of a cubic's Routh array (the quotient $(a_2a_1 - a_0)/a_2$ with $a_2 = 1.0682$, $a_1 = c_1'$, $a_0 = c_0'$), and both $c > 0$ and $c_0' > 0$" — pure algebra on the printed coefficients, no computed value added. |
| Halanay η collision | **IMPLEMENTED** | v27 L557 (§10.2): the Halanay decay rate is renamed "$\nu$": "with decay rate the unique $\nu > 0$ solving $\nu = \alpha_0 - \beta_0 e^{\nu\tau}$ (Halanay, 1966; the decay rate is denoted $\nu$ here so that $\eta$ remains the effort-response coefficient of Section 2 throughout)" (claude: "the Halanay paragraph reuses η (effort response) for the decay rate"). |
| q*/p notation collision | **IMPLEMENTED** | v27 L232 (§5.2): "under unit Hermitian normalisation of the right eigenvector $v$ and its adjoint $w$, with the normalisation $w^*\Delta'(i\omega)v = 1$ ($w^*$ the conjugate transpose; the eigenvector pair is denoted $v, w$ so that $q$ remains the catchability throughout)" (claude: "q is catchability and p is unused elsewhere"). |
| S-for-stock collision | **IMPLEMENTED** | v27 L589 (§11.4): "the raw gap $|\hat N - N|$ between an estimated and the true stock (written in the paper's stock symbol, since $S(N)$ is the yield)" (claude: "$|\hat S - S|$ uses $S$ for the stock; $S(N)$ is yield in this paper"). |
| Uncited r-literature range | **IMPLEMENTED** (scoped; no citation available) | The audits name no citation for the r-range (grok §9.5: "literature range r∈[0.005,0.4] … uncited"; claude [P]: same), so the claim is scoped to the paper's own computation per the task's fallback: v27 L516 — "the quoted $r \in [0.005, 0.4]$ yr$^{-1}$ range is not independently sourced in this paper, so the identification warning is scoped to the paper's own computed two-crossing window, $r \in (0.008, 0.06)$ yr$^{-1}$ (Section 9.3)". The number stays (cite-don't-drop), honestly labelled. Site note: the range sits in §9.5 (v26 L503); the task's "§10 region" label is read as this site (the only occurrence). |
| Three uncited-but-listed references [both] | **IMPLEMENTED** (cited, not dropped) | Zhang, Shen, and Chen (2013) → cited at §1.1's contemporary-ecological-delay literature (v27 L19: "…and harvested predator–prey systems whose paired ecological delays are Hopf objects in their own right (Zhang, Shen, and Chen, 2013)" — matches the reference's subject: Hopf of a predator-prey system with predator harvesting and two delays). Moore (1979) and Cloud, Moore, and Kearfott (2009) → cited together at the natural home, §5.1's interval-Newton certification paragraph (v27 L226: "The interval machinery itself is standard (Moore, 1979; Cloud, Moore, and Kearfott, 2009)"). All three reference entries were already listed (verified unique in v27). |
| §11.6 grant text untrimmed | **IMPLEMENTED** | v27 L597: trimmed to the two next theorems (the Church–Lessard upgrade + fold persistence, with the NS Lyapunov coefficient of the exact-hold map named as the matching open computation — grok's list), with the grant items (RFDE/hybrid analogue, n-patch, variable-time kernel, delay-separation, exergy-limited class) recorded in one line and routed to the supplement's open-problem register (S6), which already carries all six items verbatim — nothing destroyed. |
| §8–§9 campaign tables layer | **IMPLEMENTED** (four concrete asks) / **DECLINED** (see below) | (1) Consolidated table — v27 L456–L465 (§8, after the scheme-dependence remark): the channel × scheme × $T_r$ table (Protective/Mobilising × Euler (11)/Exact (13)/Native ZOH, with $\rho$ at $T_r = 1$ and the crossing records), every entry a value already stated in §6.4/§8; the unrecorded mobilising-ZOH annual radius is marked "not recorded". (2) The 2/\|C_E\| sentence — v27 L365 (§6.4, where the 2.306 crossing is discussed): "within about $2\%$ of the explicit-Euler stability limit of the scalar effort equation, $T_r < 2/|C_E| = 2.352$ yr (… the limit at which the scalar factor $1 + T_r C_E$ itself reaches $-1$)" — one division of the printed $C_E = -0.850336$. (3) Growth rates — v27 L467: "$\rho - 1 = 5.5\times10^{-4}$ per review cycle (Euler) and $3.5\times10^{-4}$ (exact) — e-folding times of roughly $1800$ and $2900$ review cycles … the $\tau = 0$ instability of Section 5.1 seen through a one-year hold that supplies too little phase". (4) Stock-mode reading — v27 L467: the uncoupled modes $e^{A_N} \approx 0.982$, $e^{-d} \approx 0.819$, $1 + C_E \approx 0.150$ (one-line evaluations of the printed $A_N = -0.0179$, $d = 0.2$, $C_E = -0.850336$), the recorded $\rho(M_p(1)) = \rho(M_{\mathrm{ex}}(1)) = 0.9838$ identified as the stock mode, the $0.9967$ maximum matched to $e^{A_N T_r} \approx 0.996$, and claude's reading stated: "the protective sampled-data record says that the slow stock mode decays under review, not that the controller stabilises an otherwise unstable loop." |
| Cor 6.1 proof τ_m-vs-τ_M typo | **ALREADY PRESENT** | v27 L377 (unchanged from v26): "no imaginary root exists for any $(\tau_M, \tau_p)$" — the wave-2 (v26) fix is in place; verified, not re-edited. |
| §1.1 cross-refs (both) | one **ALREADY PRESENT**, one **IMPLEMENTED** | "Section 4" (phase-stabilised window): already fixed at v26 — v27 L23 "The phase-stabilised window of Section 5.1" (verified). "Sections 2–9": R18 above (IMPLEMENTED). |

---

## Declines (with reasons — no new computations in this wave)

1. **Claude's RH-margin quantification** ("the annual-review instability is the τ=0
   instability (RH margin ≈ 6×10⁻⁵)"): the margin value is not a printed record of this
   paper (it is claude's own recomputation of the undelayed cubic's RH slack). Declined as a
   number; the qualitative identification is implemented in the growth-rate sentence (v27
   L467) on the paper's own §5.1 record.
2. **Claude's eigenvalue triple of $M_p(1)$ as recorded values** (0.984 / 0.80 / 0.15): the
   paper records only $\rho(M_p(1)) = 0.9838$, not the spectrum. Restating the uncoupled
   modes ($e^{A_N}$, $e^{-d}$, $1 + C_E$) from printed constants is implemented; presenting
   the perturbed eigenvalues themselves would be a new (if small) computation. Declined in
   that form.
3. **Claude's flip-type classification of the protective Euler crossing at 2.306 yr**: the
   paper's own record attributes the crossing to the Euler factor–hold-flow interaction, and
   no recorded eigenvalue type exists. The algebraic scalar-factor fact is implemented (the
   $-1$ limit $2/|C_E| = 2.352$ yr and the 2% proximity); asserting the map's crossing type
   is declined.
4. **Claude's start-of-period recomputation** (its alternative reading moves the mobilising
   crossing to ≈3.0 yr): contradicted by the paper's registered scheme-dependence record
   (6.5013 yr under start-of-period measurement, v27 L454's remark, which the audits'
   verification half itself accepts as re-executed). No re-run in this wave; the registered
   record stands and the convention disclosure already in the text is the honest state.
5. **Per-campaign tables for §9** (claude's priority 11: "a table per campaign would halve
   [§8–§9]"): the docket's concrete asks (the consolidated table, 2/|C_E|, growth rates,
   stock-mode) are implemented; converting §9.2/§9.3's prose records into per-campaign tables
   is a restructure-scale pass on frozen record prose, out of this wave's scope (registered,
   not declined on merit).

## Non-destructiveness verification (mechanical, in the build script)

- The §5.1 interval-certified table row is byte-identical and unique in v26 and v27.
- grep-count bookkeeping (v26 → v27), every delta documented: "64.402327203368" 2→2,
  "64.402327203372" 2→2, "5.587236198689" 1→1, "64.402327895" 1→1, "0.001316298" 1→1,
  "150.358477" 7→6 (−2 = the mandated §1.2 strip; the §7.6→§5.1 G5 move is count-preserving;
  +1 quoted in the version log), "3.6661490142739" 2→1 (§5.1's copy retained; §1.2's
  stripped), "5.5872362" 6→5, "64.4023272" 7→6, "148.6" 9→8, "64.438" 4→3 (all §1.2 strips),
  "0.9838" 4→6 / "47.536" 8→8 / "79.143" 7→7 / "2.306" 7→7 / "1.00055" 2→2 / "1.00035" 2→2 /
  "0.9846" 1→2 / "6.7279" 1→2 / "0.9928" 1→2 / "0.9967" 2→4 (the §6.4/§8 records are intact;
  the new consolidated table re-states values verbatim).
- The Abstract is byte-identical (v25's stripped form untouched); no theorem statement,
  hypothesis list, proof, figure caption number, or fold/multiplier/spectral record value was
  altered — the §9.2 fusion fix, the changelog strips, and the R22 restatements re-express
  the same recorded numbers at their honest precision.
- No new computation: the only derived figures are 2/|C_E| = 2.352 (one division of a printed
  constant), the e-folding times 1/(ρ−1) ≈ 1800/2900 (one division each of printed ρ), and
  the stock-mode exponentials $e^{-0.0179} \approx 0.982$, $e^{-0.2} \approx 0.819$,
  $e^{-0.00358} \approx 0.996$ (single exponentials of printed constants) — all flagged in
  the version log as one-line arithmetic.
- Only two files under "arena agent 1/" touched: `paper4_delay_dynamics_v27.md` (created) and
  `paper4_supplementary_v4.md` (the one allowed append, 17 insertions / 0 deletions). v26 and
  all prior versions byte-untouched (git status clean apart from those two + the new script).
