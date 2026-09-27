# Lean verification audit — v33
## Repair A adopted: the downstream check, and the notation fix the paper also needs

Branch `lean-audit-v4`. Build: **rc = 0, 42 jobs, 39 imported modules, zero
warnings, zero `sorry`** (fresh-clone verified, §7).

One new module, `Formalizations/P3_SupportRepair.lean`. No existing file
edited. Also drafted (paper-side, not Lean): `paper2_repairA_thm_support_v1.tex`.

---

## 1 · The decision, and the textual evidence for it

**Adopted: repair A.** `thm:support` keeps the unrestricted sequential
class; `𝒲_k` in its statement becomes the **feedback** recursion
(`Wmem` in the layer). A remark covers repair C — on a blind window the two
recursions coincide (`Wmem_eq_Wblind_of_blind`, v28, the set-level form of
`thm:lattice`'s `V^{ol} = V^{seq,blind}`).

The audit found **independent textual evidence** that A is the intended
reading, at paper line 415:

> "This is a statement about the declared class, proved by direct
> enumeration below — **not a corollary of Theorem `thm:support`, whose
> value is the unrestricted one**."

The paper itself distinguishes the two values and says `thm:support`'s is
the unrestricted one. Repair B (keep `𝒲_k` blind, re-read `V_k` as
sequential-blind) would contradict that sentence; repair A does not. A also
moves the paper *towards* the literature it cites at line 164
(Chatterjee–Doyen–Henzinger 2009 on almost-sure safety depending only on
belief supports — a statement about general policies, not fixed
schedules).

No new mathematics was needed: `VFb_eq_one_iff_Wmem` (v32) already *is*
the repaired `thm:support`, consequence 1.

---

## 2 · Downstream check (directive 1)

Every use of `𝒲_k`, `thm:support`, and the blind/feedback distinction,
checked against the layer.

| where | what the paper says | status under repair A |
|---|---|---|
| `thm:support`, support identity (310–312) | `supp(b⁺(·|a,y)) = Post(supp b, a, y)` | **proved** — `P3_Support.support_identity` (v25), on `SafeMDP` (it needs genuine `T`, `g`). **Unaffected** |
| `thm:support`, consequence 1 (315–317) | `V_k(b) = 1 ⟺ supp(b) ∈ 𝒲_k` | **proved, repaired** — `VFb_eq_one_iff_Wmem` (v32) |
| `thm:support`, consequence 2 (321–323) | `1 - V_k(b) ≥ min_{x ∈ supp b} b(x)` | **proved, newly in literal form** — `VFb_min_mass_bound_one` (v33 §1) |
| `thm:support`, consequence 3 (324) | `V_k` non-increasing | **proved** — `VFb_antitone` (v29). **Unaffected** |
| `prop:degen` (644–661) | blind window, declared class `Π_B`; survived-mass formula; `V_k(b) = 1` if a jointly surviving blind sequence exists | **proved, stronger** — `VR_eq_total_iff_Wblind` (v30) is the full iff, `min_mass_bound` (v12) the deficit. **Unaffected**: `prop:degen` never names `𝒲_k` |
| `prop:deficit` (i) (793–795) | chance-constrained common action | **NOT formalized** — it is a statement about `SafeMDP`'s stochastic kernels (exit probabilities `p(x,a) = 1 - Σ_{x'} T`), i.e. the *other* operator, out of scope by the v24 decision. **Unaffected** by repair A |
| `prop:deficit` (ii) (796–798) | if `b ∉ 𝒲^{bel}_k` then `Δ_k(b) ≥ min_x b(x)` | **proved, newly in the paper's vocabulary** — `deficit_min_mass_of_not_Wbel` (v33 §2); previously only as `min_mass_bound` (v12), whose hypothesis is spelled out per-tuple. **Unaffected — but see §3** |
| `prop:deficit` (iii) (804–805) | monotone deficit; cites `thm:support` for `V_{k+1} ≤ V_k` | **proved** — `VFb_antitone`; the citation is to the monotonicity alone, which holds on both readings. **Unaffected** |
| `prop:freeze` (687–701) | `𝒮_{ℓ+1} ⊆ 𝒮_ℓ`; `V_ℓ` non-increasing; **"stabilizes after at most `2^{|supp b|}` strict decreases"** | monotonicity **proved** (`VfamAdm_antitone` v30, `VFb_antitone` v29); **the `2^{|supp b|}` bound is NOT proved** — see §4 |
| `thm:lattice` (900–1010) | `V^{ol} = V^{seq,blind}` | **proved** at set level — `Wmem_eq_Wblind_of_blind` (v28). This is the remark covering repair C. **Unaffected** |
| Intro, line 52 | "the value-one level … coincides with the viable-set recursion `𝒲_k`" | **consistent** once `𝒲_k` means `𝒲^{fb}_k` |
| Intro, line 56 | "an antichain, **Sperner-bounded**" | Sperner decision stands: cited, not formalized, marked *by decision* |
| Line 164 | relation to CDH 2009 | no formalization needed; repair A aligns with it |

**Nothing downstream breaks under repair A** — with one exception, which
is not a theorem but the notation, and is the next section.

---

## 3 · The one thing that does break: `𝒲^{bel}_k` is the analogue of the *blind* recursion

Paper line 251–253 defines three symbols:

> `𝒲_k` the calculus's viable-set recursion (a family of state sets), and
> `𝒲^{bel}_k` **its belief-space analogue** (a family of beliefs)

and line 789–791 defines `𝒲^{bel}_k` as

> the family of beliefs whose support admits a jointly surviving
> **declared-class** sequence.

Declared-class = blind. So `𝒲^{bel}_k` is the belief-space form of
**`Wblind`**, not of `Wmem`. Today that is consistent: `𝒲_k` (lines
302–304) is also blind. Under repair A it stops being consistent — if
`𝒲_k` becomes the feedback recursion while `𝒲^{bel}_k` keeps its
published definition, the sentence "its belief-space analogue" is false.

`P3_SupportRepair` §3 says this in code. `Wfbel` is the belief-space
analogue of the *repaired* `𝒲_k`, `Wbel` the published one (v33 §2), and

```
theorem Wfbel_not_Wbel :
    ∃ M k b, totalD M b = 1 ∧ Wfbel M k b ∧ ¬ Wbel M k b
```

exhibits a **normalized** belief in one and not the other — the same
witness as v32's `paper_literal_thm_support_fails`, read as a statement
about the two symbols.

**Recommended notation fix (paper-side).** Three names, not two:

| symbol | space | recursion |
|---|---|---|
| `𝒲^{fb}_k` | state | feedback — used in `thm:support` |
| `𝒲_k` | state | blind (declared-class) — used in `prop:degen` |
| `𝒲^{bel}_k` | belief | blind — used in `prop:deficit` (ii) |

and line 252 must say `𝒲^{bel}_k` is the analogue of **`𝒲_k`**, not of
`𝒲^{fb}_k`. Redefining `𝒲^{bel}_k` as the feedback analogue instead would
break `prop:deficit` (ii)'s proof, which cites `prop:degen` — the blind
proposition. That is the one place where incautious relabelling does
damage, and it is why the check was worth doing: the obvious edit (rename
everything to the repaired symbol) is the wrong one.

The draft edit is in `paper2_repairA_thm_support_v1.tex` §1, §4.

---

## 4 · One gap the repair does not close: `prop:freeze`'s `2^{|supp b|}`

`prop:freeze` asserts `V_ℓ(b)` "stabilizes after at most
`2^{|supp b|}` strict decreases". The layer proves monotonicity
(`VfamAdm_antitone`, v30) and finiteness of the range
(`VfamAdm_finite_range`, v30), but **not** the count.

This is worth separating from Sperner. The Sperner bound in
`prop:antichain` (iii) is *cited* by the paper, so not formalizing it
verifies the paper faithfully. The `2^{|supp b|}` bound is the paper's own
claim, so leaving it unformalized is a genuine coverage gap — a small one
(it needs only `|subsetsOf l| = 2^{|l|}`, a short induction on the list,
plus the observation that strict decreases are bounded by the size of the
value's range), but it is not "someone else's theorem". Offered, not done:
say the word and it is the next module.

---

## 5 · The finding, recorded (directive 2)

Recorded here, in `lean_README_v9.md`'s `thm:support` row, and in
`P3_SupportRepair`'s header — not buried in a commit message:

> **The paper's `thm:support` was false as printed.** It named the
> unrestricted sequential class (value `VFb`, viability `Wmem`) and paired
> it with the blind recursion `Wblind`. `paper_literal_thm_support_fails`
> (v32) exhibits a normalized belief — mass `1/2` on each of `p` and `q`,
> on a model with deterministic kernels and a deterministic observation
> map — with `VFb_2(b) = 1` and `supp(b) ∉ Wblind_2`, so the forward
> implication fails. **Repair A** (restate `𝒲_k` as the feedback
> recursion) is adopted; the repaired statement is `VFb_eq_one_iff_Wmem`
> and is proved. The paper will be edited to match.

Coverage row for `thm:support` (directive 5): **result — proved on the
repaired reading** (`VFb_eq_one_iff_Wmem`, `VFb_min_mass_bound_one`,
`VFb_antitone`, `support_identity`). Not "partial", not "under repair B".
The blind twin `VR_eq_one_iff_Wblind` is retained as `prop:degen`'s
consequence 1, which is what it always was.

---

## 6 · The remark the paper should add (directive 3)

Drafted in `paper2_repairA_thm_support_v1.tex` §3. The point is that
`Wmem ⊄ Wblind` is a property of the model, not merely a defect to be
patched: **feedback is strictly stronger than a fixed schedule here, under
deterministic kernels and a deterministic observation map, in the
strongest form available — all or nothing** (`V^{Π_seq} = 1` while
`V^{Π_B} < 1` on the same normalized belief), and the two agree exactly on
a blind window. That is a statement worth having in the paper on its
merits; the fact that it is also the diagnosis of the false theorem makes
it cheap to add.

The draft also spells out the **proof** edit: the printed converse
("with deterministic observations the realized observation path is fixed by
the declared sequence") is invalid for a feedback policy — determinism
makes the path determined *by the policy and the initial state*, not fixed
in advance of them, and a policy is not a sequence. §2 of the draft gives
the replacement induction against the feedback recursion. Notation alone
would not have fixed the proof.

---

## 7 · Build state

`lake build` → **rc = 0, 42 jobs**, 39 imported modules, zero warnings,
zero `sorry`; verified by cloning `lean-audit-v4` at the pushed commit into
`/var/tmp` and building there (not `/tmp` — a full clone costs ~906 M
against a 993 M tmpfs).

P3 totals unchanged: **11 result · 1 partial · 6 instance · 1 out of
reach**, the partial being `prop:antichain` (iii) (count cited to Sperner,
not formalized, by decision).

Technical note for the next turn: **`by_contra` is not available** in this
dependency-free layer (reported as *unknown tactic*); use
`by_cases h : p` and discharge the negative branch with
`cases … <;> simp_all`. `cases`, `by_cases`, `simp_all`, `native_decide`
and `decide` are all available.

## 8 · Files

| file | status |
|---|---|
| `lean/Formalizations/P3_SupportRepair.lean` | new, green (42 jobs) |
| `lean/Formalizations.lean` | 38 → 39 imports |
| `paper2_repairA_thm_support_v1.tex` | **new, paper-side draft** — notation edit, restated theorem, new remark, proof replacement |
| `lean_README_v9.md` | new; supersedes v8 (42 jobs / 39 imports, repair-A rows) |
| `lean_audit_v33.md` | this file |
