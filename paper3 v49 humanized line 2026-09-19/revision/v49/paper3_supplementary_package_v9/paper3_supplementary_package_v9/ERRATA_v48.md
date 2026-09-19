# Errata for the v48 line — `paper3_material_ledgers_v48` and its three companions

Raised 2026-09-19 while scoping the Section 1 waiver for v49, by running the v49 gate against the v48 build. **No
manuscript file was changed in producing this list**, and none of it changes a number, a proof or a result: six of
the seven items sit in the abstract-and-§1 region that v48's build rewrote by hand and that its gate did not check.

Each item says whether v48 *introduced* it or *inherited* it, by comparison with the accepted v47 line
(`revision/v7/paper3_material_ledgers_v47.md`).

| # | item | evidence | v48 or inherited | fixed in v49 by |
| --- | --- | --- | --- | --- |
| E1 | §1 lost the deposit's flagship example: "The first failure mode has a public flagship object. Earth Overshoot Day aggregates component flows into a single calendar date…" | `work/paper3.txt:59`, `v42:27`, v47 1 hit, **v48 0** | introduced by v48 (its hand-written front matter) | restore as deposit content, checked verbatim; G1/G3 already flag its absence |
| E2 | §1 lost the named concept **"aggregation obstruction"** and its §10.1 pointer ("This article formalises this sense as the aggregation obstruction of Section 10.1") | `work/paper3.txt:70`, v47 1 hit, **v48 0**; "obstruction" 7 → 5 document-wide | introduced by v48 | the same; caught by G1's coinage harvest (`term the base coins or emphasises, absent from the build`) |
| E3 | §1 lost two cross-references the previous line carried: **§2.3** and **§6.5.4** | G3 flag `section reference the base carries and the build loses: ['2.3','6.5.4']` | introduced by v48 | G3 blocks on section references; the rewrite must keep the pointers |
| E4 | §1 asserts **the 2008 SNA revision, SEEA 2014 and "(United Nations, 2014)"** — none of which the deposit contains — and the 40-entry reference list has **no 2008 entry** for the year the sentence asserts | `2008` dep 0 / v47 1 / v48 1; `United Nations` dep 0 / v48 4; `SEEA` dep 0 / v48 2; `grep 2008` over the v48 reference list → 0 lines | **inherited** (v47 has it too; it came in with the upgrades line, not with v48) | adjudicate on the merits: add the UN 2008 entry and cite it, or trim the sentence to what the deposit supports. It is a content decision, not a stylistic one, so it needs the author, not the gate |
| E5 | the rewrite moved the phosphate reserve figures **out of math mode** — `$1{,}000{,}000$` / `$6.0\times10^5$` became prose digits — which is build-time normalisation of deposited mathematics in the one region exempt from the rule against it | G1 flag `inline symbol in the base, absent from the build: ['1 , 000 , 000', '600 , 000']`; v47 0 prose hits, v48 1 | introduced by v48 | G1's inline-symbol equality; the value never changed, so this is presentation, but the rule is unconditional |
| E6 | a markdown artifact **reached print**: page 2 of the PDF reads "The drift is concrete. - A **reserve-life ratio** divides a reserve figure…" — a stray list marker and an orphan bold | G0 flag `list marker inside a paragraph`; `v48.md` line at §1.1; v47 clean | introduced by v48 | G0 integrity (list markers, unbalanced emphasis, foreign delimiters) |
| E7 | term dilution in the exempt region: `incidence` 5 → 3 in §1 (37 → 28 document-wide) and `support pool` 4 → 3 | G1 `guard-term count falls (base -> build)` | introduced by v48 | G1 count equality on the registry plus the derived coinage set |

**Why none of this was caught before.** `verify_v48_base.py` has no front-matter check — `grep -i front` over it
returns nothing — because the region is rewritten by hand and the build treated "hand-written" as "already verified".
The paragraph check is markdown-against-PDF, and the verbatim check is the 290-row ruling, so a sentence that was
neither ruled nor required to exist could disappear without a sound. The v49 gate replaces that with G0–G5, which run
on the exempt region too; `revision/v49/waiver_gate_controls.json` holds its output on the v42 → v48 pair: **7
blocking flags and 2 disclosures**, which are E1–E7.

**Standing of the v48 deliverable.** E1, E2, E3, E5, E6, E7 are losses of *specific wording* in framing material; the
argument, every number, every proof, every table and every label in v48 is intact and the gate still passes 57/57
with `*** ALL CHECKS PASS ***`. E4 is the one item that touches substance: a citation the deposited article does not
carry, sitting in the front matter with no reference-list entry. v48 is therefore sound as a technical document and
has one accuracy item to resolve before it is read as final.

---

## Added after the 32-row read (2026-09-19, the day the v49 line was built)

The list above was drawn from the waived region. Reading the 32 reuse rows the splice had absorbed or kept —
the rows the atom test had passed — showed that the same weakness reaches the body, so the earlier claim in
this file that every item sits in the exempt region was too narrow. It is corrected here rather than quietly
rewritten.

| # | item | evidence | v48-introduced or inherited | closed in v49 |
|---|---|---|---|---|
| E8 | six sentences naming a defined object are absent from v48 although the deposited article states them and v42 and v47 both carried them: `monomaterial projection` (D0238, §2.2), `never in the stock` (D0286, §2.5), `differentiated only by` (D0385, §4.3), `replenished by recharge` (D0521, §6.5.1), `two readings of one ledger` (D0719, §11), `not a primitive of the closed natural block` (D0631, §2.5) | phrase counts: deposit 1–2, v42 1–3, v47 1–3, **v48 0** for all six | v48-introduced. Mechanism: the `regen` bucket rewrote a draft sentence that already carried the deposit's wording; the replacement kept the claim's atoms and lost the named object | all six restored verbatim in v49, each placed in its own section |
| E9 | the abstract's two-senses passage was mangled: "The illusion has two senses, and they are distinct. It is the compensatory-aggregation failure above …" keeps the first sense and drops the second (`yield inflation`) together with the `aggregation obstruction` pointer to Section 10.1 | v42 line 29 and v47 carry the full passage; v48 line 31 is the shortened form | v48-introduced | v49 carries the deposited article's form over verbatim |

Two points the author raised that this file should not bury:

* The item numbered **E8** in the instruction "add E8 to the errata" is already on the list above as **E2**
  (`aggregation obstruction` and its Section 10.1 pointer), and its evidence marks it **introduced by v48, not
  inherited** — `aggregation obstruction` counts 1 in the deposit, 1 in v42, 1 in v47, 0 in v48. It is not
  duplicated; the number E8 was reused here for the body items the read found, which are a different class.
* E4 (the 2008 SNA / SEEA 2014 entry) was described above as the only item touching substance. E8 is a second
  one: a diagnostic the paper defines and then never uses is a claim about the paper's own scope.

| E10 | §4.3 states the same sentence twice, plain and then bolded: *"Two scope notes are part of the theorem. **Two scope notes are part of the theorem.**"* | v48 line 874; v42 carries the sentence once, v47 not at all — the twin is a v48 repair artifact | closed in v49 by a logged deletion (`v49_body_repairs.json`), survivor count asserted at 1 |

## E4, revisited by the v49 base swap

E4 recorded that v48's §1 asserts the 2008 SNA revision, SEEA 2014 and `(United Nations, 2014)` — none of
which the deposited article contains — and that the reference list carries no 2008 entry for the year the
sentence asserts. The author's adaptation does not carry that passage, so v49's §1 no longer makes the
unsupported assertion: **E4's substance is gone**, and it is gone because the base changed, not because
anything was argued into the text. What remains is a loose end of the same coin: the entries
`United Nations, 2014` and `United Nations, 2025` are now cited by nobody in the article (`SEEA` and
`United Nations` appear 0 times in v49's body). The line audit reports them separately from the two entries
that were uncited in v42 and v48 as well (`Baez 2023`, `Illakwahhi 2024`), and the fix is an author's
decision — drop the two entries, or restore the passage they supported. This file does not record either
choice as made.
