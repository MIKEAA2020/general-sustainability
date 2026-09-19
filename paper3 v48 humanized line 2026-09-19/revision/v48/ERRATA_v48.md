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
