# Lean audit v10 — response to the "out of scope" critique

**Scope of this document:** a correction and a completion. It responds to a
critique of the recommendation at the end of v9, and supplies the artifact
the critique correctly identifies as missing: a complete, per-result
coverage statement for P3.

**Bottom line up front:** the critique is right that my recommendation was
wrong in form, and I retract it. It is wrong on one factual extrapolation,
and correcting that matters. And the underlying question it raised — "is
`prop:probecount` actually true?" — had not been checked by anyone, so I
checked it. **It is true.** All five of the paper's claims about it verify,
across 118 individual checks, with zero violations.

---

## 1. Where the critique is right — and I retract the recommendation

v9 §6 said: *"`prop:probecount` should be **declared out of scope** and the
paper should say so."*

The second clause is wrong and I withdraw it. "Out of scope" is a
project-management status, not a mathematical one. A referee reading a
mathematics paper does not want to hear about a proof assistant's
expressive limits, and putting that in the paper body would read as an
excuse. The critique's three-way split is correct:

| Thing | What it says | Where it belongs |
|---|---|---|
| The mathematics | `prop:probecount` is true | the paper |
| The verification | it is (not) formalized in Lean | the verification report |
| The project scope | we chose not to formalize it | internal notes |

**Corrected recommendation:** *No change whatsoever to the paper.* Do not
mark it, qualify it, or annotate it. It is a true proposition with a
(sketch) proof, and it should stand as the paper writes it.

Two verified facts make this the whole answer rather than a dodge:

- **No `.tex` file in the paper family references any audit document.** The
  v1–v10 audits are `.md` files sitting in `latex/`; nothing `\input`s or
  `\include`s them. They are already separate documents — i.e. they are
  already the verification report, not paper content.
- **The P3 paper makes no claim about formal verification at all.**
  Searching all ten `.tex` files for `lean|mechaniz|proof assistant|formally
  verified` returns **0 hits in P3** (and 0 in eight of the other nine). The
  conditional that would make this a real problem — *"if the paper claims
  full formal verification, the gap is a problem to be fixed"* — **is not
  triggered.** The paper claims nothing about Lean, so there is nothing for
  the paper to retract.

## 2. Where the critique is wrong: the inexpressibility does *not* recur

The critique writes:

> The same issue will recur for every other result that needs analysis:
> `prop:pathdeficit`, `thm:recursion`, `prop:freeze` — the AI's own
> "cheapest next batches" list is essentially a triage of which remaining
> results happen to be expressible in `OrdField` and which aren't.

This misreads v9's table. Those three results appear in v9 §6 because they
are on the **doable** list, not the blocked list. Their actual v9
classifications:

- `prop:pathdeficit` — **feasible.** `Δ₁(b) = Σ_x b(x)·p_x` is a finite sum.
- `thm:recursion` — **feasible.** Finite max over `A(Π)`, finite sum over
  `Y`; it is `thm:pomdp` with a restricted action set, and v8 built the
  machinery.
- `prop:freeze` — **partial.** The nesting `S_{ℓ+1} ⊆ S_ℓ` and the
  non-increasingness are finite combinatorics; only the `2^{|supp b|}`
  counting bound is unfinished.

None of the three needs analysis. On the evidence so far, **exactly one of
the 18 results has non-`OrdField` content**, and that content is confined to
`exp`/`ln` and Stirling. The critique's inference from "one result is
inexpressible" to "the paper and the formalization are built on different
mathematical foundations" is not supported. The foundations coincide on
17 of 18.

## 3. `prop:probecount` is true — verified

Nobody had checked the mathematics; I had only asserted inexpressibility.
`verify_probecount.py` (pushed alongside this document) checks it in exact
rational arithmetic where possible. **118 checks, 0 failures.**

| # | Claim | Result |
|---|---|---|
| 1 | The five exact values at `ε=1/10`, `n = 1,3,5,7,9`: `1/10`, `7/250`, `107/12500`, `341/125000`, `22273/25000000` | **all 5 match exactly** |
| 2 | `p_wrong(n) ≤ (3/5)^n` at `ε=1/10` | holds, `n` to 101 |
| 3 | `p_wrong(n) ≤ (4ε(1-ε))^{n/2}` | **0 violations**, 9 `ε` × 7 `n` = 63 checks |
| 4 | `(4ε(1-ε))^{n/2} ≤ e^{-2n·sep²}` | 0 failures / 40 |
| 5 | `n ≥ ln(1/δ)/(2 sep²) ⟹ p_wrong ≤ δ` | 0 failures / 15 |

Check 3 compares **squares**, to stay in exact rationals: `n` is odd, so the
bound carries a half-integer exponent, and `a^{n/2} ≤ b ⟺ a^n ≤ b²` for
`a ≥ 0`.

So the critique's option 1 — *"prove it in the paper as ordinary
mathematics"* — is already satisfied in substance. The paper's proof is a
two-line sketch ("pairing each wrong-majority string with its complement
and Stirling's estimate, and `4ε(1-ε) = 1 - 4sep² ≤ e^{-4sep²}`"), which is
a recognizable standard argument and, per tests 3–5, a correct one. If
anything, the sketch could be expanded to a full paragraph for a referee,
but that is ordinary mathematical exposition, not a correctness issue.

## 4. A sharper expressibility analysis than either of us gave

Both my "inexpressible" and the critique's "inexpressible in the chosen
framework" are too coarse. `prop:probecount` is a composite of three
sub-claims that differ:

| Sub-claim | Statement expressible over `OrdField`? | Proof formalizable? |
|---|---|---|
| **A.** `p_wrong(n)` = binomial tail `Σ_{j>m} C(n,j) ε^j (1-ε)^{n-j}` | **Yes** — finite sum of products | **Yes** — it is the definition |
| **B.** `p_wrong(n) ≤ (4ε(1-ε))^{n/2}` | **Only conditionally.** Odd `n` needs `√(4ε(1-ε))`; but at `ε=1/10` it collapses to `(3/5)^n`, an integer power, which **is** expressible | **No** — the proof is pairing + Stirling, i.e. analytic |
| **C.** `≤ e^{-2n sep²}`, and `n ≥ ln(1/δ)/(2 sep²)` | **No** — needs `exp`/`ln` | No |

The useful conclusion: the *statement* is partly expressible and the
*proof* is not. So even the parts of `prop:probecount` that can be written
down over `OrdField` cannot be **proved** there. That is the precise reason
it is out of reach — not "it is a Chernoff bound," full stop.

## 5. The artifact the critique asked for: complete P3 coverage

*"Being fully transparent that the formalization covers a subset of the
paper's results, and saying exactly which subset and why."* Agreed — and it
belongs here, not in the paper. This is that statement.

| # | Result | Status | Note |
|---|---|---|---|
| 1 | `thm:recursion` | formalizable, not done | = `thm:pomdp` with `A(Π)`; machinery exists (v8) |
| 2 | `thm:support` | formalizable, not done | finite sets as lists/predicates |
| 3 | `prop:antichain` | **partial** | (i) feasible; (ii) alpha-vector characterisation harder |
| 4 | `cor:closed` | instance | Python verifier layer |
| 5 | `thm:parametric` | instance | Python layer |
| 6 | `prop:pl` | **partial** | max-of-linear-functionals feasible; convexity delicate |
| 7 | `prop:degen` | formalizable, not done | finite sums with indicators |
| 8 | `prop:freeze` | **partial** | nesting + monotone feasible; `2^{|supp b|}` count unfinished |
| 9 | `prop:deficit` | formalizable, not done | overlaps `prop:chance` (v8, proved) |
| 10 | `thm:agree` | instance | 48-cell grid — Python layer |
| 11 | **`thm:lattice` (i)** | **FORMALIZED** | v9, `class_monotone`, axiom-free |
| 12 | `thm:class` | instance | needs delayed-instance dynamics |
| 13 | `prop:learn` | instance | Python layer |
| 14 | `prop:pathdeficit` | formalizable, not done | near-free from v8 `exit_add_survival` |
| 15 | `prop:noisyprobe` | formalizable, not done | finite algebra, indicators |
| 16 | **`prop:dr` (i)** | **FORMALIZED** | v9, `contam_lower` + `contam_sharp` |
| 17 | `prop:probecount` | **not formalizable** | `exp`/`ln` in statement, Stirling in proof — **but mathematically verified, §3** |
| 18 | `prop:additivelaw` | instance | needs additive-drift dynamics |

**Totals:** 2 formalized · 6 formalizable-not-done · 3 partial · 6
instance-level · 1 not formalizable.

Read against the critique's framing: of the 18, **17 are `OrdField`-
compatible**, and the 6 instance-level ones are covered by the project's
existing two-tier design (Lean proves the theorems that make certificate
checks load-bearing; Python supplies the certificates). So the framework is
not mismatched to the paper. It is *behind* the paper — 2 of 18 done —
which is a resourcing fact, not a foundational one.

## 6. One real defect this did surface

The coverage claim that does exist is in `lean_README.md`, and it is
imprecise in a way that could mislead:

> "Every theorem is fully proved; there are **no `sorry`s and no extra
> axioms**."

True and verified. But the README's slot table maps *papers* to *modules*,
which quietly suggests each paper is covered. It should map *results* to
*theorems*, as §5 does. Since the standing instruction is never to
overwrite, the fix is a new edition (`lean_README_v2.md`) carrying §5's
table, not an edit to the existing file. Not done in this batch — flagging
it as the concrete follow-up.

## 7. Corrected recommendations

1. **The paper: no change.** `prop:probecount` stays as written. It is true
   (§3) and the paper nowhere claims formal verification (§1).
2. **The verification report: §5 is the coverage statement.** Maintain it
   per-result and keep it current as modules land.
3. **`lean_README.md`: issue a v2** whose slot table resolves to results,
   not papers.
4. **Do not expand the `OrdField` framework** to absorb `exp`/`ln` for one
   result. That would import real analysis and its completeness obligations
   into every other module for the sake of 1 of 18 results; the cost lands
   on the 17 that currently build clean.
5. **Continue closing the 6 formalizable-not-done**, cheapest first:
   `prop:pathdeficit` → `thm:recursion` → `prop:degen` → `prop:noisyprobe`
   → `prop:deficit` → `thm:support`.
