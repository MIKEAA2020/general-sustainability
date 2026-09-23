# The Stochastic Selector — Joint Audit Record and Dispositions (v1)

**Audited artifact.** `paper2_stochastic_selector_v1` ("The Stochastic
Selector: Exact Rational Belief-State Safety Values under Partial
Observation"), first edition, 3 pp., with verification script
`paper2_stochastic_selector_v1_verify.py` (record 10/10, re-run and
confirmed passing at audit opening).

**Audits.** Two independent reviews supplied by the owner in a single
document (`uploads/stochastic selector.txt`): a nine-item technical review
(gemini) and a summary-judgement review (grok). They are adjudicated
jointly below, item by item, against the actual artifacts (source,
rendered PDF, verification record), per the programme's
verify-before-fix discipline.

**Method.** (i) The first edition's verification record was re-executed at
audit opening (10/10). (ii) Every audit claim was checked against the
LaTeX source and the rendered PDF (text extraction, including the exact
count and location of typographical defects). (iii) Each accepted repair
was implemented in a new edition (`paper2_stochastic_selector_v2`, no
artifact overwritten) and re-verified by an extended record of fifteen
check families (15/15), which also absorbs both audits' own computations
as verified results. (iv) Genuine fixes ship only in the new edition;
companion lineages are not edited (within-lineage discipline).

---

## Part I — Evaluation of the two audits

**What the audits establish.** Both reviews converge on four genuine
defects of the first edition: (1) the selector's nonemptiness sentence
conflates the argmax set with the value-one level (gemini item 5; grok
"wording/definitional"); (2) three formal gaps in the model's boundary
cases — transitions outside the safe set, the observation law at the
absorbing state, and witness masking (gemini item 3); (3) broken internal
references rendering as "(Section )" (gemini item 8; grok "leftover
placeholders"); (4) the alpha-vector dimension statement
(|X|+1) inconsistent with the displayed two-coordinate witnesses (gemini
item 4; grok "harmless but unremarked"). Both further flag the "kink"
terminology for what is a jump discontinuity in the parameter (gemini 7;
grok), and the "in-window adaptivity" phrasing for what is open-loop
time-variation (grok; echoed in gemini 1–2). These findings are confirmed
against the artifacts and accepted.

**Where the audits err.** (i) gemini item 1 labels the class-parameter
gap a "fatal technical contradiction." Adjudication: the rendered first
edition scopes its agreement theorem "over the declared hold class" and
states the unrestricted-class value separately in its Theorem 2(e), whose
content the first edition's verification record had already verified by
brute force; the audited mathematics is internally consistent. What the
audit found is real but narrower: Proposition 1's backup ranges over all
actions with no class parameter, so the agreement theorem's restriction
was not licensed *as a formal matter*. Severity: corrected — a
formalization gap, not a computational contradiction. (ii) gemini's count
of broken references (three, one in the abstract) is inaccurate: the
rendered edition contains exactly two instances (Introduction and
Declarations); the abstract contains none. (iii) gemini item 2 ("collapse
of the timing obstruction") overstates: the companion papers' timing
certificates are stated for declared blind-window control classes, so the
class scope is intrinsic to those statements; nothing collapses. grok's
reading of the same matter is the correct one. (iv) Both audits compute
the unrestricted-class value as 1 on {z0 ≥ 2} "for k ≥ 2"; the
recomputation performed for this record sharpens the statement — a single
action already saves both branches at z0 ≥ 2, so the unrestricted value
is 1 on {z0 ≥ 2} for every k ≥ 1, and the two classes coincide exactly at
the one-step horizon (verified; adopted into the second edition's class
declaration).

**What the audits confirm.** grok's "technical points that check out"
(the recursion's identity with finite-horizon POMDP value iteration; the
rationality chain; the honestly stated exponential growth; the
deterministic degeneration; the deficit bounds; the 48-cell agreement;
the two-floor instance) are each re-confirmed by the second edition's
extended verification record.

---

## Part II — Dispositions

**J1 (gemini 1; cf. grok). Proposition 1 lacks the policy-class
parameter. — ACCEPTED AS FORMAL REPAIR; SEVERITY CORRECTED.** The value
and recursion are class-parameterized (`V^Π_k`, admissible sets `A(Π)`),
with the blind-window segment form for non-Markov classes
(Proposition 1 of the second edition). The sharpened class declaration
(coincidence at k = 1; difference exactly on the timing cells for
k ≥ 2) is added to Theorem 2(e) and verified (check S8). Not a
contradiction in the computed mathematics: see Part I.

**J2 (gemini 2). "Collapse of the timing obstruction." — REJECTED as a
defect of the companion papers; ACCEPTED as a scoping clarification in
this lineage.** New Remark (the timing obstruction is class-scoped)
states the reading explicitly: the closed forms are hold-class
(sampled-review) values; the unrestricted class differs exactly on the
timing cells; no companion statement is altered. The companion lineage is
not edited (within-lineage discipline; its certificates are already
class-scoped by construction).

**J3 (gemini 3). Boundary cases of the model. — ACCEPTED.** State space
restated as `V ∪ {⊥}` with total transition rows; absorbing `⊥` with its
own observation `y_⊥`, so observation laws sum to one at every belief;
masked backups with `α(⊥) = 0` anchored at `Γ_0 = 1_V`. Verified (check
S12).

**J4 (gemini 4; grok). Witness dimension. — ACCEPTED.** Witnesses are
indexed by `V ∪ {⊥}`; the two-floor witnesses pad to (1,0,0), (0,1,0);
the first edition's displays suppressed a zero coordinate — now stated in
the text and verified (check S14).

**J5 (gemini 5; grok). Selector nonemptiness. — ACCEPTED (both audits
converge).** The attaining (argmax) set `Γ^s_k(b)` — nonempty for finite
`A`, no viability content — is separated from the value-one level
`S^Π_k(b)`, whose nonemptiness corresponds exactly to `V_k(b) = 1`. The
first edition's sentence is repaired; the distinction is verified
instance by instance (check S13).

**J6 (gemini 6). Adversarial support reading vs. expectation. —
ACCEPTED.** New Remark (the two operators): the deterministic
degeneration replaces the expectation by the robust Bellman operator; it
is a theorem about that operator, not a claim about the stochastic plant.
Proposition 2 is reworded accordingly; its content was verified as
stated (check S3) and is unchanged.

**J7 (gemini 7; grok). "Kink locus." — ACCEPTED, WITH A SHARPENING.**
Theorem 2(c) is restated: the witness family changes exactly at z0 = 2 at
the one-step horizon and at z0 = 1 + k at horizon k ≤ T_obs (in
particular *not* at z0 = 2 when k = 2 — the joint recomputation corrects
the first edition's unscoped phrasing); the value's parameter jumps sit
exactly at z0 = 1 + min(k, T_obs) (jump 1/2); kinks in the strict sense
belong to the piecewise-linear value in the belief coordinates. Verified
(checks S6, S15).

**J8 (gemini 8; grok). Broken references. — ACCEPTED.** Evidence: exactly
two rendered instances ("(Section )": Introduction; Declarations), caused
by referencing an unnumbered section; the abstract is clean (both audits'
counts and locations slightly inaccurate; the defect real). Edition 2
references Section 6 literally; a post-build probe confirms no broken
reference remains.

**J9 (gemini 9). Ambiguity in Proposition 3(ii). — ACCEPTED.** The k-step
robust kernel `W_k` is defined in belief space (a family of beliefs, not
a state subset) and the statement repaired.

**J10 (grok). Presentation gaps. — PARTIALLY ACCEPTED.** The fifteen
check families are now listed in Section 6 with a complexity note
(worst-case law; the two-witness reason; 384 vectors, maximal denominator
1; deduplication as the only pruning needed on the audited classes); the
declarations' repository path is rephrased and names the second edition's
script. The proofs remain one-paragraph sketches by design of a
main-only paper; a supplementary with complete proofs remains an optional
owner-side item and is recorded as such.

**J11 (grok). "The script remains the sole evidence." — ADDRESSED.** The
listed families, the audit record (this document), and the reproduction
command in the declarations constitute the evidence chain; the script
remains the computational evidence of record, per the programme's
verification discipline.

---

## Part III — The second edition

`paper2_stochastic_selector_v2` (4 pp., dated September 24, 2026)
implements J1–J11. Changes visible to a reader: class-parameterized value
theory; completed model (total rows, absorbing observation, masked
witnesses); attaining set vs. value-one level; the two-operators remark;
the class-scope remark; restated Theorem 2(c) and sharpened 2(e); the
vacuous-indicator remark; listed verification families with complexity
note; repaired references; updated declarations with the AI-assistance
disclosure for both editions.

## Part IV — Verification and build record

Verification: `paper2_stochastic_selector_v2_verify.py`, fifteen check
families (S1–S15), all passing, exact rational arithmetic, standard
library, deterministic; it regenerates every number in the paper and
absorbs both audits' computations (oscillation table, unrestricted-class
values, jump loci). Build: Tectonic 0.15.0, zero overfull boxes; 4 pages;
post-build probes confirm the repaired references, the new terminology,
and the declarations. The first edition's artifacts are retained
unmodified; the second edition ships as new files with this record and
the source package.

**Declarations.** Funding: none. Competing interests: none. The two
audits were supplied by the owner; their adjudication, the repairs, the
extended verification record, and this document were prepared with AI
assistance under the programme's verification discipline.
