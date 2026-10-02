# Family audit v47 — all eight papers

> ## ⚠ CORRECTION — read `family_audit_v48_empirical_correction.md` first
>
> **§2.1 of this note is wrong and is retracted.** It states that "the program's
> entire empirical footprint is one fish stock." That claim was made by
> generalising from the eight papers in the list, without examining the
> repository as a whole. The repo in fact contains at least fifteen live
> manuscripts whose empirical work spans **six independent real-world systems in
> four domains**, including a full second wave-E replication on the Edwards
> Aquifer and multi-stock screens over 42 fish stocks.
>
> Section 2's criticism of the family on "broad practical interest" is therefore
> **misdirected**, and is withdrawn. Sections 1 (the battery audit) and 2.2–2.4
> partly stand; see v48 §3 for exactly what is withdrawn, what is revised, and
> what is unchanged. v48 also records that the programme has already documented
> a per-paper venue strategy, which changes the criteria against which §2 should
> have been judged.

Two questions were asked: (1) have all the family papers been checked?
(2) do they clear the bar a top journal applies? This note answers both.
Everything below was produced today; nothing is carried over on trust.

---

## 1. Have all the family papers been checked?

**No — not before today.** Prior work covered four files: `paper1_assessment_separation_v63`,
`paper2_computational_certification`, `paper2_probabilistic_sufficiency`, and
`paper2_exact_belief_computation`. The other five members of the family named in
your list — **obstr, ws, minimax, ARV, E1** — had not been examined at all.
They have now been.

Latest version of each, as it stands on `lean-audit-v4`:

| short name | file | latest |
|---|---|---|
| obstr | `paper2_obstruction_calculus_v55_Automatica_routes.tex` | v55 |
| comp | `paper2_computational_certification_v20.tex` | v20 |
| ws | `paper2_worked_systems_v17.tex` | v17 |
| minimax | `minimax_dual_certificates_v12.tex` | **v12 (new today)** |
| ebc | `paper2_exact_belief_computation_v13.tex` | v13 |
| psuff | `paper2_probabilistic_sufficiency_v14.tex` | v14 |
| ARV | `applied_regime_viability_v9.tex` | v9 |
| E1 | `paperE1_cod_forecast_ladder_v59.tex` | v59 |

### 1.1 Battery results

Every battery was downloaded and run in a clean directory against its own paper,
with all chained scripts, data files and figures fetched from the repo.

| paper | battery | result | exit |
|---|---|---|---|
| obstr v55 | **none exists** | — | — |
| comp v20 | `_v20_verification.py` | 49/49 | 0 |
| ws v17 | `_v17_verification.py` | 55/55 (+ 57 chained lineage) | 0 |
| minimax v12 | `_v12_verify.py` | 70/70 (+ chain v3 20/20) | 0 |
| ebc v13 | `_v13_verification.py` | 30/30 | 0 |
| psuff v14 | `_v14_verification.py` | 32/32 | 0 |
| ARV v9 | `_v9_verification.py` | 250/250 | 0 |
| E1 v59 | `_v59_verification.py` | 73/73 | 0 |

**661 checks** in total (584 top-level, 77 chained). All green, and — for the
four batteries I tested by sabotage — genuinely falsifiable: corrupting
`paperE1_cod_forecast_ladder_v59.tex` drops E1 to 72/73 with exit 1, and
corrupting `minimax_dual_certificates_v12.tex` drops minimax to 69/70 with
exit 1.

### 1.2 Two defects found, both in minimax

**(a) The entire minimax verifier lineage v2–v11 could not fail.** Every one of
them ends with

```python
PASS, FAIL = [], []
def chk(cond, name):
    (PASS if cond else FAIL).append(name)
...
n_pass = sum(1 for ok in PASS if ok)        # PASS holds names, i.e. strings —
raise SystemExit(0 if n_pass == len(PASS) else 1)   # so this is always len(PASS)
```

Failures were removed from numerator *and* denominator, and the exit code was
always 0. A sabotaged tex moved the report from `63/63` to `62/62` with exit 0 —
the failure disappeared instead of being reported. Versions v6–v11 carried a
second bug on top of it: the forbidden-marker loop tested `needle`, the previous
loop's leftover variable, so 14 intended absence checks collapsed into one
duplicated presence check.

Both are repaired in v12: every check is recorded and printed, the exit code is
honest, the absence loop tests `bad`, and the chained-seed figure is measured
rather than printed as a literal.

**Consequence to keep on record:** any figure quoted from a minimax v2–v11
script carries no information. v1 uses sound accounting and its 8/8 is real;
v2–v11 are not evidence of anything.

**(b) A real content defect, hidden by (a) for six versions.** Table `tab:checks`
claimed

> martingale property at every cell, all **8192** policies

for family G1. Under the paper's own definition (`π_k` constant on the cells of
`P_k`, `|A_k| = 2`, with `P_1, P_2, P_3` having 2, 4 and 8 cells) the policy
space is `2^2 · 2^4 · 2^8 = 2^14 = 16384`. The enumerator was right and the
printed number was wrong by a factor of two. The tower and martingale properties
themselves hold on all 16384 policies, so **no theorem is affected — only the
count.** Paper and needle now both read 16384.

The other five failures revealed by honest accounting were stale needles, all
needle-side, now corrected to the actual typeset strings (remark title, a
spurious leading `(`, `Chv\'{a}tal` with a braced accent, and the `}` in
`\textbf{Keywords:}`).

### 1.3 obstr has no battery — and one unsupported claim

`paper2_obstruction_calculus_v55` is the largest paper in the family (19.0k
words) and the one the others are companions to. There is **no
`paper2_obstruction_calculus_*` verification script anywhere in the repo** —
zero `.py` files match. Its Code-availability paragraph offers
`paper2_coverage_audit.py`, which regenerates Table `tab:coverage` (one of three
tables) and, on inspection, **does not read the `.tex` at all** — it computes the
audit and prints a LaTeX table body. It is a generator, not a check.

Separately, §"A two-patch protection audit" states:

> Both computations are machine-verified in exact integer arithmetic, and the
> verification script regenerates the table verbatim.

There is no script for `tab:patch`. I wrote one (`fam/ob/patch_audit.py`) and
audited the table independently. **Good news: every claim in it is correct** —
the full-information kernel is exactly `{z ≥ 1} \ {(1,1)}`; the certainly-safe
readings are exactly `y ≥ 4`; all six belief rows carry the verdict the paper
prints; and the common-action certificate fires (empty safe-action intersection)
on each of the three nonviable rows. The content is right; only the artifact was
missing.

So obstr's mathematics survives its first independent check. But the flagship
currently has the weakest verification support in the family, which is the
inverse of what the situation calls for — and after today's minimax finding,
that is the highest-risk item on the list.

---

## 2. Do they clear the bar?

Short answer: **not uniformly, and not for the reason the family's own
verification record might suggest.** The exact-arithmetic discipline is
genuinely excellent and is a real methodological contribution in its own right.
The gap is elsewhere: in empirical breadth, in standalone legibility, and in the
one place the family does not check — the flagship.

### 2.1 The decisive numbers

| paper | words | self-cites (Abaee) | of which 2026, unpublished | real data? |
|---|---|---|---|---|
| obstr | 18,978 | 2 | 0 | no |
| comp | 10,788 | 14 | 12 | no |
| ws | 10,919 | 13 | 12 | no |
| minimax | 5,502 | 13 | 11 | no |
| ebc | 3,807 | 7 | 6 | no |
| psuff | 11,682 | 7 | 6 | no |
| ARV | 6,256 | 8 | 7 | **yes** |
| E1 | 20,951 | 14 | 10 | **yes** |
| P1 | 27,814 | 18 | 15 | no (disclaims) |

Two facts dominate.

**The program's entire empirical footprint is one fish stock.** E1 and ARV both
work Northern cod, NAFO 2J3KL. Every other paper uses synthetic or symbolic
instances. P1 states it outright: *"No empirical result about any specific
resource system"* and *"nothing here is an empirical claim."* That is honest and
correctly scoped — but it means the family cannot claim "empirical or applied
contributions of broad practical interest" on the strength of one case study in
one fishery, however well executed.

**The instances are small, and the papers say so.** The audited universes are a
`2^9` belief space, 36 belief pairs, a 93-cell grid, 256 augmented cells. `ws`
is candid: *"These examples do not constitute a general taxonomy of viability
failures; they supply exact counterexamples, finite censuses, and reproducible
benchmarks."* A referee at a general-interest journal will ask what the largest
system is that this handles, and the family does not currently answer that.

### 2.2 Where each paper sits

**Clears the novelty bar on its own terms.**

- **obstr** — the strongest claim in the family. The complementary direction
  (certifying *non*viability) genuinely has received less systematic treatment,
  and the Veliov/tangency positioning makes that concrete. Caveat the paper
  itself states: the certificates *"do not exhaust the complement of the
  epistemic kernel,"* and the residual dynamic gap is shown to decompose into a
  phase that is *undecidable* by any certificate pair reading only the window
  sub-model. Much of the paper is a careful map of its own limits. Honest, but
  it softens the "here is the instrument" headline.
- **P1** — the quantifier-order separation is a clean, transferable idea, and
  the practical message (report separately-binding floors individually, because
  the aggregate cannot distinguish the rescuable from the impossible) is the
  kind of sentence that travels. At 27.8k words it is over the limit of most
  journals that would want it.
- **E1** — a well-constructed null result with an unusually candid limitation
  section: *"a conditional hindcast, not an operational forecast"*; power below
  15% against two alternatives; specificity conditional on the tested model
  class; the two reference points disagree on 29 of 71 years. Null results are
  publishable and this one is decision-relevant — the closing line, that the
  period's uncertainty accumulated in the observation and reference-point layer
  rather than in forecast structure, is the actual finding. But it needs a venue
  that wants that, and it needs the null framed as the contribution rather than
  as a failure to find one.
- **ARV** — the most complete applied paper: obstruction structure certified on
  public assessment data, in exact rational arithmetic, with a 250-check script.
  One case study, but a real one.

**Strong work, but framed as companions — needs a standalone reason to exist.**

- **comp, ws, psuff** — each is substantial (10–12k words) with a real battery.
  The issue is not quality. It is that each is legible mainly as a satellite of
  obstr, and each leans on 6–12 unpublished 2026 self-citations. A referee
  evaluating `minimax` or `psuff` alone cannot verify the object it studies.
- **minimax** — the measure dual is a genuine unification (Farkas pair, sparse
  witness, and Isaacs drift as special cases). But 11 of its 13 self-citations
  are to unpublished 2026 work, it is 5.5k words, and it closes by recording its
  main extensions as *conjectures* while explicitly *not* closing the gap it
  inherits. At a top journal this reads as a section of obstr, not a paper.

**Too thin to stand alone at a top journal.**

- **ebc** — 3.8k words, and its own subtitle says *"A computational companion to
  the belief-state safety-value theory."* Its contribution (the 1,048,576 → 496
  antichain collapse, the doubling ladder) is real but is a computational annex
  to `psuff`. As a standalone submission it is a short companion note.

### 2.3 Four structural issues, in the order I would address them

1. **Build a battery for obstr.** Highest priority. The flagship has none; one
   of its three tables has a generator that never reads the tex; and one § makes
   a "machine-verified ... regenerates the table verbatim" claim for a table with
   no script. Today's minimax case is the argument: a battery that cannot fail
   concealed a wrong printed count for six versions. Without one, obstr's
   verification claims rest on nothing checkable.
2. **Reduce the unpublished-self-citation load.** `minimax` (11), `comp` (12),
   `ws` (12), `P1` (15) all rest on a web of 2026 manuscripts a referee cannot
   open. Two options: make each paper's headline claim self-contained, or
   consolidate the family into fewer, larger papers. Given point 4 below,
   consolidation is probably the better move.
3. **Broaden the empirical base, or narrow the claim.** One stock cannot carry
   "broad practical interest." Either add a second empirical system — the
   Edwards forecasts (E3/E4) already in the repo are the obvious candidate — or
   stop claiming applied breadth and target the family squarely at methods
   venues. Right now the framing asks for the former while the evidence supports
   the latter.
4. **Consider merging.** `ebc` into `psuff` (same theory, one is the other's
   computational annex); `minimax` into `obstr` (same object, one is the other's
   dual). That would convert four least-publishable-adjacent units into two
   papers with genuine weight, and cut the self-citation graph roughly in half.

### 2.4 A presentation note

The abstracts are exceptionally dense with numerals. `ebc`'s is 1,708 characters
of almost unbroken enumeration; `comp`'s opens with a displayed inequality
containing six named error terms before it has said why the reader should care.
The instinct — show the numbers because the numbers are exact and checkable — is
right, but at the desk-read stage it works against the family. The exactness is
the strongest asset here; it needs one sentence of motivation in front of it.

---

## 3. Caveats on this audit

- I read the **abstracts** of all eight (plus P1) in full, and targeted sections
  of obstr and minimax. I have not read the bodies of `comp`, `ws`, `psuff`,
  `ARV` or `E1` line by line. The §2 judgements about novelty and scope rest on
  abstracts and structural measurements, not on full reads.
- **Nothing has been compiled.** There is no `pdflatex` in this environment, so
  no paper has been typeset. Table and figure counts are from source.
- A green battery is necessary, not sufficient. Needle checks police prose
  against prose; a needle can assert a false string (the 736 case) or, as in
  minimax v6–v11, assert nothing at all. The 661 checks passing is real
  evidence, but it is not a proof that the mathematics is right.
