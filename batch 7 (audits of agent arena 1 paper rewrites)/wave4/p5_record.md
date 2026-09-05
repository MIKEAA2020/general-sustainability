# P5 wave-4 record — paper5_sampled_governance_v21.md (from v20)

Task ID 73-e · Build: `apply_batch7_wave4_p5.py` (fail-loud; anchors asserted exactly
once; all mechanical checks below were executed by the script and passed).
Source: `arena agent 1/paper rewrites/paper5_sampled_governance_v20.md` (465 lines,
untouched — md5 14008514fdd4b59a0e281fb1fe4802bb before and after the build).
Output: `arena agent 1/paper rewrites/paper5_sampled_governance_v21.md` (541 lines).
Audit basis: `grok claude paper 5.txt` (both halves), JOINT_AUDIT_EVALUATION.md R23/R24
(lines 1119–1142) + the P5 (A)-block consensus items 1–7 (lines 419–438), and
WAVE2_IMPLEMENTATION.md §2/§3 (P5 v20 regression repair; the middle layer left open).

Non-destructiveness, machine-checked by the script: Table 1, Table 2, the Section 3.4
comparison table, and the Section 4.6 mismatch table are byte-identical (the last
relocated verbatim into Appendix B); "several dozen" → 0 occurrences; the 42-stock
phrase counts unchanged (4); no frozen number lost (checked list: 47.536, 79.143,
2.306, 6.501, 1.00035, 1.00055, 0.9838, 0.9967, 3.666, 150.358, 257.8, 537%, 0.895,
0.923, 0.956, 0.994, 0.67, 7.8, 1.29, 0.022, 0.061, 34.42, +0.42, …); the registration-
vocabulary count in the main body reduced 33 → 30 with the appendix carrying the
consolidated statements; "2026-09-01" (1) and "Rose (2026)" (2) body counts unchanged.

---

## Per-item dispositions

### R23 — q-sensitivity surfacing [both — consensus 3, partial] — IMPLEMENTED
- Abstract (v21 L11): new sentence after the command-step-artefact sentence — "The
  archived regions are also not robust to the catchability scale the stage record never
  declared: at $q = 0.1$, against the reconstruction's imported $q = 0.001$, every
  class's annual-review verdict flips, so the archived-versus-reconstructed comparison
  is uninformative at that undeclared scale rather than a non-reproduction."
- §4.1 (v21 L357, end of the first paragraph): "…the stage map fixes no catchability,
  the reconstruction imports the hold-map core's $q = 0.001$, and at the declared
  sensitivity $q = 0.1$ every verdict of the Section 3.4 comparison flips — every class
  unstable at annual review ($\rho(1) \ge 1.29$), the slow-stock class unstable across
  the entire grid ($\rho(50) = 7.8$) — so the archived-window comparison is
  uninformative at the undeclared scale rather than a non-reproduction (Section 3.4's
  Reading)." (All numbers are the paper's own printed §3.4 records; nothing computed.)
- Reading reworded (v21 L301) per claude's blunter framing: "The comparison, however, is
  uninformative rather than a non-reproduction. The stage map declares no catchability;
  the table is computed at the imported value $q = 0.001$; and at the declared
  sensitivity $q = 0.1$ every verdict in the table flips — … — so a match or a mismatch
  at either value is a statement about this declared family at an undeclared scale, not
  an adjudication of the archived values…". The v20 "does not reproduce the anchovy 3–4
  yr or the sprat 6–12 yr response regions" framing and the "they establish only that
  this declared family does not reproduce those windows" clause are absorbed into the
  recombined sentence; the factual content (convergence at every interval, the
  long-horizon band 34–42 yr, no archived counterpart) is retained verbatim in meaning.
- §4.1 consistency: "the reconstruction's non-reproduction of them" → "the
  reconstruction's comparison with them" (v21 L357) so the paragraph does not contradict
  its own new sentence. §3.3's lead statement ("does **not** reproduce the multi-year
  windows") is deliberately left: it is the factual record at the declared $q$, and the
  Reading/§4.1/abstract now carry the uninformative-at-undeclared-scale framing on top
  of it (claude's ask targeted the Reading).
- Box 1 row (v21 L39–40) states the q-sensitivity and the uninformative-comparison
  status in the ledger.

### R24 — Notation unification [claude E10 + grok's notation notes] — IMPLEMENTED
Unification map (choices recorded, per the audits' preference):
- **M (monodromy)** → retired. §2.3's operative condition is now
  $\det(D\mathcal P_{T_r}(X^*)-e^{i\theta}I)=0$, "with $D\mathcal P_{T_r}(X^*)$ the
  Jacobian of the review map at its fixed point (the monodromy matrix of the sampled
  loop)" (v21 L141) — matching the $D\mathcal P_{T_r}(X^*)$ already used in §2.3's next
  paragraph.
- **M (production maximum, Lemma 2.2)** → $f_{\max}$ (v21 L194, 196 and three further
  sites in the proof). **M now denotes natural mortality only** (cod case and stage
  classes; $M_x$ extra mortality, subscripted).
- **S** → two declared scopes, fenced: surplus production $S(N)$ (logistic plant,
  eq. (2)) / $S(A)$ (stage plant, §3.4) in the control sections; spawning stock biomass
  (reported as SSB in Table 2) in the cod case. The notation paragraph (v21 L83) states
  the scopes, that "the two scopes of $S$ never share an equation", and that "no symbol
  serves two sorts". (Renaming the cod $S$ was impossible without altering equation (5)
  and Table 2's byte-identity; declaration + fencing is the non-destructive
  unification.)
- **δ** → defined at the $\Phi_k$ equation (v21 L129): "with shift $\delta$ a constant
  regularisation offset (distinct from and unrelated to the effort-law gain $\delta_0$)
  and sharpness $k$ — the value used in the computed records, $k = 10$, is stated at its
  use site in Section 3.4 and collected in Table 3 of Appendix A" (grok's line item:
  "state $k$ with the equation"). The same site records that the §3.4 multiplier records
  presuppose a fixed point interior to the nonsmooth regions of $\Phi_k$ and $\Pi$, with
  the equilibrium coordinates not printed (claude's interiority ask, answered honestly —
  the value is an archive item, not asserted).
- **g** → defined at first use (v21 L254): "$g$ is its maturation delay, and the
  response regions are located through the product $rg$" (on the delayed-recruitment
  continuous-delay parameterisation).
- **C_E, C_Z** → defined at their introduction (v21 L262): the exponential update is
  "the exact solution, over one review interval, of the linearised effort law
  $\dot e = C_E e + C_Z z$ with the assessment $z$ held, where $C_E$ and $C_Z$ are the
  coefficients of that linearisation (the partial derivatives of $F_B$ with respect to
  $E$ and $Z$ at the compared fixed point; unrelated to the removals $C$ of the cod
  case), and equation (4)'s increment is the forward-Euler discretisation of the same
  linear object."
- **"four-state"** → defined at its use (v21 L317): "the stage-structured review map's
  closed loop of four state components (adults $A$, juveniles $J$, memory signal $Z$,
  held effort $E$), whose slow-stock class carries the centuries-scale dominant
  timescales of Section 3.3."
- **extractive vs mobilising** → **"extractive"** chosen (the term of §§1–2 and of both
  audits' running text; grok: "extractive vs protective"; claude lists "extractive" as
  the §1–2 term). All six "mobilising" body occurrences replaced (crossing record ×3,
  Figure 1 caption, one-plant contrast, §4.1). The choice is recorded in the version
  log; the companion's reference-title "Mobilising" is its real title and is kept.
- **τ₋** (adjacent gap found during the pass) → defined inline (v21 L274): "the
  unstable window's lower edge".
- Machine check: "mobilising" absent from the main body; total occurrences exactly 2
  (version-log record + companion reference title).

### Claims-ledger box [both — consensus 5] — IMPLEMENTED
Box 1, "Claims at their exact evidential status" (v21 L20–50), placed after the
Keywords / before §1 (grok: "a one-page 'claims at their exact status' box after the
abstract"; claude D: consolidated claim-status). 26 rows: claim → evidential status →
record pointer, covering every numerical window, ρ, and empirical count (the operator
crossings and ρ values, the archived stage windows, the reconstruction records and the
q = 0.1 layer, the MATCH/MISMATCH status, the screen/power/case-search counts, the cod
table and the constrained-M hypotheses, the stall, the obstruction, the prospective
designs, the distributive constraints). Lead sentence: "Nothing in this box is new; the
body sections carry the full statements." Itemised in the build: 28 table lines
(header + separator + 26 rows).

### Registration-vocabulary appendix [both — consensus 6] — IMPLEMENTED
Appendix A, "Registration and reproducibility record (consolidated)" (v21 L411–420):
- a vocabulary convention (declared / registered / pre-registered, each defined);
- the four movable registration meta-statements preserved as bullets (solver
  configuration and initial histories; RAM identifiers and eligibility table; the full
  null-calibration record; simulation code and seeds) with their section pointers;
- the consolidated unprinted-parameters/λ/θ record and the Data-availability/§4.5
  status.
One pointer left in the main flow (§2.2, v21 L137): "…are consolidated in Appendix A,
which also fixes the vocabulary convention for 'declared', 'registered', and
'pre-registered'." The main-flow meta-sentences were removed (§2.2 "declared
registration requirement"; §2.4 RAM-identifiers sentence and null-calibration
sentence; §2.5 seeds sentence); the load-bearing status statements (provisional
status, caveats, reconstruction's pre-registration) remain in the main text.
Machine-checked: narrow registration-vocabulary count in the main body 33 → 30; the
meta-phrases "declared registration requirement"/"registered requirement" are absent
from the main body and present in Appendix A (3 + 1); the Data-availability and
Supplementary-note occurrences (back matter) are unchanged.

### Logistic-core parameter table [claude A6] — IMPLEMENTED
Table 3 (v21 L422–440, in Appendix A so the table numbering order is preserved:
Table 2 sits in §3.8 before it): 15 rows collecting the parameter values the
manuscript itself prints — logistic core (q = 0.001; k = 10; η = 0.914 as printed in
the continuous-delay asides; the crossing record; the 200,001-point scan) and the stage
reconstruction (class (M, τ) sets with sources; h = 0.75 with the {0.6, 0.9} layer;
A₀ = 100 and the survival/steepness algebra; q = 0.001 with 0.1 sensitivity; k = 10;
the finite-difference derivative construction and cross-check; the scan grid; the
trajectory-classification configuration). Entries the text never prints (r, K, E_max,
δ₀, Z_ref, Δ_ref, δ, τ_m; the linearised fixed point (N*, E*, Z*) and its interiority)
are explicitly marked "not printed in this manuscript" and attached to the declared
computational record — claude's A6 answered honestly under the no-new-computations
rule. Caption: "No value here is newly computed." Itemised in the build: 17 table lines.

### λ/θ/margin reporting for ρ = 1.00035 [both — grok + claude A2] — IMPLEMENTED
New §3.4 paragraph "Spectral margins of the annual-review verdict" (v21 L268), after
the complete crossing record: reports the recorded margins (ρ = 1.00035 exact,
1.00055 Euler, 0.9838 protective annual, 0.9967 protective maximum; the modulus
exceeding unity by 3.5×10⁻⁴ — a restatement of the printed 1.00035); the recorded
multiplier types (complex pair at 6.501 yr; real −1 at 79.143/2.306 yr); the explicit
statement that the dominant multiplier's angle θ and the continuous eigenvalue λ are
**not printed in this manuscript** and belong to the declared computational record
(Appendix A); and the sensitivity caveat (the verdict at this margin is conditional on
the monodromy's numerical construction and the unprinted parameter vector; what the
margin does not condition is the ordering across updates/channels and the crossing
directions). No new computations: every number is the paper's own printed record.

### A1 undelayed-stability reconciliation (§2.3 vs §3.2 vs §3.4) [both] — IMPLEMENTED
New §3.4 paragraph "The undelayed limit, reconciled explicitly" (v21 L276), after the
one-plant contrast: quotes and binds the three sites (§2.3's same-loop declaration,
§3.2's transfer relation $\mu_j = 1 + T_r\lambda_j + O(T_r^2)$, §3.4's undelayed-
instability and stable-at-τ=1 records), states the non-closure precisely (if λ > 0, an
even number of crossings must lie in (0, 3.666) yr that no record reports; if λ ≤ 0,
the sampled instability down to T_r = 0.2 yr contradicts §3.2's transfer conditions),
and records the reconciliation as **open** because λ is not printed (archive item) —
the operator-scoped records stand as recorded. No verdict changed; claude's "report λ"
is satisfied by the honest statement that λ is an archive item (computing it would
violate the no-new-computations rule; the derivation is left to the archive, and the
margins paragraph + Appendix A register it).

### A9 slow-stock "agreement" reclassification [claude] — IMPLEMENTED
§3.4 Records (v21 L288): "agrees with the spectral record for the three faster
classes… The slow-stock class does not agree with its own multiplier record: … against
a multiplier record with no crossings anywhere on the grid. A persistent oscillation at
a linearly stable fixed point is bistability, a non-decayed transient, or a
classification-threshold artefact; the record does not distinguish among them, and the
cell is reported as a disagreement between the reconstruction's two records, not as an
agreement." The 30%-error cells: "cells read as noise-driven variance rather than
oscillation, since the 2% relative tail threshold is not noise-adjusted." The
MATCH/MISMATCH table row is untouched (byte-identity) and the Reading's
archived-pattern claim is retained (the archived pattern IS reproduced; the
reclassified item is the agreement with the reconstruction's own spectral record).
The positive-from-noise threshold adjustment itself is a computation — declined here,
registered as the honest status statement.

### Screen-band lineage acknowledgment [claude A4] — IMPLEMENTED
§2.4 (v21 L149): the predeclared bands are now glossed "— bands that descend from the
archived, unreproduced stage-map diagnostics of Section 3.3 (its observable-specific
dominant peaks near 4 and 8 yr in biomass and 12 and 60 yr in effort) and carry that
record's provisional status into the screen's target definition."

### §4.6's relocation [both — grok §5, claude A10/E11] — IMPLEMENTED
The full §4.6 material (mismatch table + both paragraphs, byte-identical, 5 table
lines) is relocated to **Appendix B** (v21 L442–452). §4.7's numbering and the
cross-references are untouched (the stub keeps the §4.6 heading). The Discussion keeps
grok's alternative — a brief "what the case does not measure" paragraph (v21 L401)
pointing to Appendix B and the Supplementary material (S6). Reason the target is an
in-file appendix rather than the Supplementary file: the repo rule forbids modifying
any existing file under "arena agent 1/" besides creating v21 — the audits' "move to
Supplementary" is implemented at the closest permitted locus, and recorded here and in
the version log.

### "42 vs several dozen" harmonisation [both] — IMPLEMENTED
Abstract (v21 L13): "a multiplicity-controlled Lomb–Scargle screen of 42 annually
assessed stocks" (matching §1's own phrasing). Machine-checked: "several dozen" = 0;
"42-stock"/"42-Stock" count unchanged (4); all 42-carrying phrases unchanged.

### Companion citation [both] — IMPLEMENTED (cite, don't drop)
- Reference entry (v21 L476, alphabetical position after Ashwin): "Author, D., et al.,
  in review. Delay-induced regime change in harvested stocks: the mobilising and
  protective channels of institutional feedback. Companion delay-dynamics study."
  Fresh letter D (A/B/C are taken by the E1/E2/E3/E4 companion entries); the title is
  paper4_delay_dynamics' real title from its file header, shortened by dropping the
  third clause exactly as E1 v11's pattern shortens this paper's title.
- In-text citations at the four load-bearing "companion delay study" sites: §2.1 (v21
  L114), §3.4 opening (L262), §3.4 one-plant contrast (L274), §3.7 budworm (L323) —
  "(Author et al., in review)".
- Machine-checked: exactly 4 in-text occurrences + 1 reference entry.

### Housekeeping: DFO (2022) — IMPLEMENTED (cite, don't drop)
§2.7 (v21 L202): "The case evidence is the assessment record (the recovery-potential
and sequential stock assessments: DFO, 2011, 2016, 2022, 2024)." This is the
contextually-correct site — the case's evidence base is the DFO assessment record, of
which SAR 2022/041 is the interim assessment between the 2016 table and the 2024
assessment used by the Rose (2026) comparison; no content is attributed to the 2022
document beyond its membership of the record (nothing is invented).

### Rose (2026) and the frozen 2026-09-01 plan date — ALREADY PRESENT / RESOLVED-BY-CLOCK
Not edited, per instruction. Line evidence: the §3.4 reconstruction paragraph retains
"pre-registered (plan dated and frozen 2026-09-01, before any run; …)" (v21 L284); Rose
(2026) citations unchanged at §3.8 (v21 L349) and §4.3 (L367). Machine-checked: body
counts unchanged (2026-09-01: 1; Rose (2026): 2). The repo clock (2026-09) is past
both dates — resolved-by-clock, as recorded in the wave-3 joint assessment.

## Declined / out of scope (with reasons)
- **"sampled governance" vs "sample-and-hold governance" (grok §6)** — not elevated to
  R24's enumerated fix list (the joint evaluation's R24 text enumerates S, M, δ, g,
  C_E, C_Z, four-state, extractive-vs-mobilising only). Both terms are defined at first
  use (abstract "an architecture we call *sample-and-hold governance*"; §1 "This paper
  calls that architecture *sampled governance*"); harmonising them is a title-level
  change outside this wave's mandate.
- **"thirty-plus" vs "more than thirty" (claude Title/Abstract note)** — the joint item
  covers only the 42 count ("use 42 throughout"); both thirty-phrasings mean the same
  and were left as-is.
- **§2.3 "Three objects are in play" / §4.7 (iii) "two operators" count (claude §2.3)** —
  not elevated to the wave-4 docket; the operator statements themselves are bound by
  the new reconciliation paragraph.
- **Figure 1 caption "four update pairs" → "four update × channel combinations", the
  `figs_p5/` image path, and the θ strong-resonance check (claude §3.4 notes)** — not
  elevated; θ is recorded as not-printed in the new margins paragraph, which is the
  no-new-computation answer.
- **Lemma 2.2 application to seal predation (claude E7) and Prop 2.1 demotion** — not
  in the wave-4 docket (would change what is claimed, not presentation).
- **Claude's §3.4 note "the nonlinear trajectory runs use an 'exact update' that is
  never defined"** — C_E/C_Z are now defined (the linear object); defining the
  nonlinear trajectory-level update's construction would assert content the manuscript
  does not record, so it is left to the archive; only the enumerated definitions were
  implemented.

## Build mechanics (all asserted by the script)
- 42 `sub1` anchor edits, each asserted to occur exactly once; §4.6 body extracted and
  re-inserted verbatim (asserted to appear exactly once in v21, after the Appendix B
  heading).
- Existing tables byte-identical and in original order after splicing out the two new
  tables (35 lines: Table 1 block 9, comparison block 8, Table 2 block 13, §4.6 block
  5 — the last now inside Appendix B).
- New tables itemised: Box 1 = 28 lines (26 claim rows), Table 3 = 17 lines (15
  parameter rows); total table lines 35 → 80.
- "several dozen" 0; "mobilising" 0 in the main body (2 total: version log + companion
  title); companion citations 4 + 1; registration vocabulary main-body 33 → 30 with
  Appendix A carrying 3 "declared registration requirement" + 1 "a registered
  requirement"; 42-stock counts 4 → 4; frozen-value list all ≥ v20 counts;
  "2026-09-01" and "Rose (2026)" body counts unchanged; version log replaced (v21
  present, v20 absent).
