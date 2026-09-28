# Lean audit — v46

Branch `lean-audit-v4`. Build unchanged: **rc = 0, 60 jobs**, zero
warnings, zero `sorry`, zero axioms.

This turn closes the two items left open by v45: the ECOMOD
supplement inconsistency, and the P3 verifier gap — plus the same
version skew found in the other three papers.

---

## 1. ECOMOD SI §S5.3b — fixed

The cereal-sentinel row carried two problems, both from an older OWID
vintage:

* growth reported **3.11×**, while the same section reported
  `d ln b_f = +1.128` for the same quantity. `e^1.128 = 3.089`.
* the 2022 endpoint given as **4.21 t/ha**. The OWID series shipped in
  the repo gives **4.1826** for 2022 and **4.2283** for 2023 — so 4.21
  belongs to neither year.

Recomputed from the repo's own data: 1961 = 1.3532, 2022 = 4.1826,
ratio **3.0909**, `d ln = +1.1285` — which matches the section's
existing log-change exactly.

`03_SUPPLEMENTARY_INFORMATION_v2` → **v3** (source never overwritten):

* table row: 4.21 → 4.18 t/ha; 3.11× → 3.09×
* prose: "yield rose 3.11×" → 3.09×
* added a **vintage note** recording the source file, both endpoints,
  the ratio and the log-change, so the next reader can re-derive it and
  can see what the earlier draft contained.

The manuscript never carried the error (zero occurrences of 3.11, 3.09
or 4.21), so this was contained to the supplement.

## 2. The version-skew gap — closed in all four papers

v45 found the P3 paper at v12/v13 with its newest battery at v11. The
same pattern turned out to hold in **all four** papers: each named a
verifier older than itself, so the current text was not what the
battery read.

Each was closed the same way — build a self-consistent pair, where the
paper names the verifier that reads it:

| paper | was | now | battery |
|---|---|---|---|
| P1 | v63, no named battery | v63 (unchanged) | **25/25**, run from the artifact |
| P3 | v13 → named v11 (reads v11) | **v14** → names v14 | **32/32**, exit 0 |
| comp | v19 → named v18 (reads v18) | **v20** → names v20 | **49/49**, exit 0 |
| EBC | v12 → named v10 (reads v10) | **v13** → names v13 | **30/30**, exit 0 |

**136 checks across the four papers, all passing.**

The single edit in each new paper version is the Code-availability
pointer to its own verifier. No scientific content changed.

### `viacert` — resolved, not written off

comp's one remaining failure in v45 was
`ModuleNotFoundError: No module named 'viacert'`, which I reported as
an uninstallable dependency. That was wrong: **`viacert` ships in the
repo** at `latex/viacert/`. Downloaded and run:

```
viacert selftest: 12/12 checks pass     (exit 0)
```

comp is therefore clean at 49/49 with no caveats.

### P1's 25 checks — located and executed

P1 names no in-tree battery; its §Machine verification points at a
figshare deposit and at "S8" of the supplement. Both exist:

* `research_program/paper1_instantiation/typed_false_positive_instantiation.py`
  — run directly: **`[25/25 checks passed]`, exit 0, 45 s**;
* the supplement's **S8. The 25-Check Enumeration** lists all 25, each
  mapped to the main-text claim it supports.

## 3. Two false findings I nearly reported, both from one habit

**`curl -o` writes HTTP error bodies to disk.** This turn I downloaded
`paper1_supplementary_v12.md` from the wrong directory, got a 404, and
`curl -o` saved the JSON error as a "5-line file". I read it as a
**stub supplement with no S8** and very nearly reported P1's
supplementary material as missing. It is 36,553 bytes and contains a
complete S8.

This is the **second** time: in v45 I reported the absent
`paper2_probabilistic_sufficiency_v12_verification.py` as a "141-byte
stub" for the same reason.

The rule, now applied: after any `curl -o`, verify the payload is not
an error object before reading it.

## 4. Discipline note on the needle updates

Each new verifier failed exactly one check at first: the paper named
the *old* script. The fix was to edit the **paper** to name its own
verifier — the opposite of editing a needle to match whatever the text
happens to say. Given the 736 defect in v44, where a needle was
hard-coded and locked an error in, the direction of the edit matters:
here the needle was right and the text was stale.

## 5. Deliverables

* `paper2_probabilistic_sufficiency_v14.tex` + `…_v14_verification.py`
* `paper2_computational_certification_v20.tex` + `…_v20_verification.py`
* `paper2_exact_belief_computation_v13.tex` + `…_v13_verification.py`
* `03_SUPPLEMENTARY_INFORMATION_v3.md` (ECOMOD)
* `lean_README_v21.md`, this audit.

## 6. Caveats

* No `pdflatex` anywhere; **no paper version has been compiled**.
* All four batteries were run in reconstructed directory trees. The
  chained-script dependencies are wide (three scripts and three `.tex`
  siblings for P3, nested two levels; five figure PDFs; the `viacert`
  package), and in-repo the chains will resolve without that setup.
* Nothing in this audit re-checked the *content* of any needle beyond
  the naming ones; the 736 lesson — that a needle can assert a false
  string — applies to all 136.
