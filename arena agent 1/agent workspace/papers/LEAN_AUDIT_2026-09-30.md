# Lean statement audit — all papers — 2026-09-30

## Method and its limits

**A toolchain was deliberately NOT installed.** Doing so previously (`.elan`, hundreds of MB)
breached the ~128 MB workspace snapshot cap. The audit is therefore **static**: every claim was
checked against the Lean source in `/home/user/lean` by parsing the files with comments
stripped.

Consequences, stated plainly:
- **Verifiable here**: `sorry`/`admit`/`axiom`/`constant` absence; declaration counts; presence
  of named declarations; module counts; the toolchain pin.
- **NOT verifiable here**: that the project still *builds*, and the axiom footprints
  (`#print axioms`). Both require a working toolchain.

## State of the Lean tree

| | value |
|---|---|
| `.lean` files | 64 |
| under `Formalizations/` | **60** |
| distinct logical modules (excluding `_vN`) | 44 |
| declarations (all kinds) | 1,603 |
| `sorry` | **0** |
| `admit` | **0** |
| `axiom` declarations | **0** |
| `constant` declarations | **0** |
| `lean-toolchain` pin | `leanprover/lean4:v4.34.1` |

A first scan flagged 12 `axiom`/`constant` hits in 7 files. **All 12 are the English word
"constant" in prose and doc-comments** (`/-- Membership in K is constant on every observation
fibre. -/`, "disturbance constant implies…", "constant expected drift"). None is a Lean
declaration. The layer is genuinely gap-free.

## Claim-by-claim

| paper | claim | verdict |
|---|---|---|
| 1 | `P1_Obstruction` has **58 declarations** | **CORRECT** — 33 theorems + 25 defs = 58 (excl. 1 structure, 3 inductive). Convention now stated explicitly. |
| 1 | named decls `finite_horizon_sound`, `finite_horizon_complete`, `Wk_antitone`, `Wk_descending`, `commonSafe`, `Blocked`, `blocked_iff`, `preOp_mono`, `tree_sound` | **ALL 9 PRESENT** |
| 3 | "**54 modules**" | **STALE → corrected to 60** |
| 4 | `Minimax_Dual` has **21 theorems and lemmas** | **CORRECT** (21 theorems + 3 defs) |
| 5 | EBC has **16 modules, 134 declarations** | **CORRECT** — 16 files; 134 theorems (total declarations incl. 38 defs + 2 inductives = 174). Paper says "134 theorem and lemma declarations", which is exact. |
| 1, 4, 5 | "Lean~4 **v4.14.0**" | **STALE** — pin is now `v4.34.1` |
| 1, 4, 5 | "**60 build jobs** pass" | **UNVERIFIABLE NOW** — dated from the v4.14.0 run |

## Changes made

Version bump: `paper01` v60→**v61**, `paper03` v12→**v13**, `paper04` v14→**v15**,
`paper05` v12→**v13**, `paper09b` v1→**v2**, `paper11` v62→**v63**, `paper11c` v1→**v2**.

1. Removed the stale `v4.14.0` from the body of papers 1, 4, 5.
2. Added a **Verification provenance** paragraph to papers 1, 3, 4, 5 stating: the pin is
   `v4.34.1`; checks were run under `v4.14.0`; source invariants re-verified 2026-09-30;
   **the build has not been re-run since the pin moved**, so build-job figures are dated.
3. Paper 1: made the "58" convention explicit (33 theorems + 25 definitions).
4. Papers 3 and 5: "54 modules" → "60 modules under `Formalizations/`".

## Under-claims found and corrected

Three papers had Lean modules in the tree but never mentioned them. These were **not** errors,
but they were leaving evidence on the table.

| paper | module | content | added |
|---|---|---|---|
| 9b (ARV) | `Formalizations.ARV`, 2 files, 29 decls, 28 theorems | `bracket_upper_form1/2`, `bracket_sandwich_form1/2`, `bracket_upper_lt_one_iff`, `bracket_subunitary_form1/2`, `bracket_subunitary_of_upper_form1/2` + `omax` primitives | new `\section{Mechanized verification}` — **directly formalizes `lem:bracket`, the harvest-free multiplier bracket** |
| 11c (WS) | `Formalizations.WS`, 2 files, 6 decls, 5 theorems | `master_monotone`, `monotone_action_axis` | new `\subsection{Mechanized verification}` — **formalizes `prop:master`** |
| 11 (E1) | `Formalizations.E1`, 1 file, 5 theorems | `ladder_telescope`, `ladder_bound_upper`, `ladder_bound_lower`, `ladder_bracket`, `ladder_ascent` | note added before Conclusions |

In each case the scope limit is stated: the bracket algebra / monotonicity theorem / ladder
inequality is proved, while the upstream extraction, enumeration and estimation are script
computations and are **not** proved. Paper 11c's wording makes the arrangement explicit: *"the
theorem that organises the table is proved, while the entries in the table are computed."*

## Papers with no Lean claim

Papers 2, 6 make Lean claims without version or count (checked, no stale numbers). Papers 7, 8,
9 (Part I), 10, 10b, 11b make **no** Lean claim — correct, since no Lean module corresponds to
them and their verification is script-based. No false claim was introduced.

## Compile verification

All seven changed files compiled with tectonic: 21, 13, 8, 6, 8, 12 and 41 pages; **zero
undefined references, zero errors**.

## 2026-10-01 count correction (supersedes two 2026-09-30 count verdicts only)

The source-level count rows for Minimax and EBC above were incomplete. A reproducible comment-stripped declaration-header census at `content_audit/claim_alignment/reconcile_lean_counts.py` finds **22** `theorem` headers and zero `lemma` headers in `latest/lean/Minimax_Dual.lean` (including the Unicode-named `ψsingle_sum` at line 244); an ASCII-only declaration-name filter returns the formerly quoted **21**. The historical counting command was not saved, so that exact mechanism is a reproducible explanation, not a proven account of the old command. For the 16 source-matched EBC modules, the correct count is **138** theorem headers, zero lemma headers. The formerly reported **134** is exactly reproduced by a bare-line `^\s*theorem` filter that overlooks four `@[simp] theorem` declarations: `EBC_Deadline.holdRep_zero`, `EBC_Deadline.matchedRep_zero`, `EBC_Dynamics.natToK_zero`, `EBC_Dynamics.natToK_succ`. The subsequent provisional **135** figure in the scientific-validity review was likewise an incomplete static count and is superseded. This correction is a source enumeration, **not** a fresh Lean build or an axiom-footprint check; all original historical build caveats remain.
