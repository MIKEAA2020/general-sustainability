# Lean audit — v44

Branch `lean-audit-v4`. Build unchanged: **rc = 0, 60 jobs**, zero
warnings, zero `sorry`, zero axioms.

---

## 1. The 736 vs 496 question — resolved, and it was a real defect

The EBC glance table reported **736** stored antichain while the abstract
and the census proposition reported **496**. I flagged this in v42 as
"possibly different measures, not verified". It is verified now, and the
glance table is **wrong**.

**What each number counts:**

| number | formula | what it is |
|---|---|---|
| **496** | `16 + 15 × 32` | the **antichain**: 16 maximal singletons at the edge, 32 maximal pairs at each of the 15 levels above |
| **736** | `16 + 15 × (16 + 32)` | **all survivable sets**: the same pairs, plus the 16 singletons at every level above |

The extra 240 sets are exactly the **non-maximal singletons above the
edge** — the sets the antichain discipline exists to discard. So 736 is
a meaningful count, but it is not the stored antichain, and a row
labelled *"Raw vs stored"* that reports it misstates the compression the
paper is about.

Three sources already said 496: the census proposition
(`prop:census`, with its proof `16 + 15 × 32 = 496`), the abstract, and
the verifier's own computation (`stored = 16 + 15 * 32`, labelled
*"stored maximal sets"*). Only the glance table said 736.

## 2. The worse half: the verifier enforced the error

The verifier's needle check did not merely fail to catch this — it
**hard-coded the wrong number**:

```python
# paper2_exact_belief_computation_v10_verification.py
"...$2^{16} = 65{,}536$ raw subsets, $736$ stored antichain",   # needle
stored = 16 + 15 * 32        # ...the computation, two checks earlier
```

A needle that asserts the presence of a string cannot verify the string
is *correct*. The script computed 496 and then required the paper to
print 736. Its header docstring carried 736 too. So the battery was
self-inconsistent and passed 30/30 regardless.

This is worth stating generally: **needle checks police
prose-against-prose, never prose-against-math.** They caught nothing here
and locked the error in. The real protection was the independent
computation, which is what exposed it.

## 3. What was changed

| file | change |
|---|---|
| `paper2_exact_belief_computation_v12.tex` | glance table row → *"$2^{16} = 65{,}536$ raw subsets per level, $496$ stored maximal sets"* |
| `..._v10_verification.py` | needle → 496; header docstring → 496 |

Both had to move together — fixing the paper alone would have turned the
30/30 green run red.

**A deviation from the standing rule, flagged deliberately.** The
"never overwrite, new versions only" rule governs paper sources. Here I
edited the verifier **in place**, because the paper references it by
exact filename (its own needle requires that name to appear in the
`.tex`), so renaming it would break the self-reference and leave the
defective needle live under the old name. Recording the deviation rather
than making it silently.

## 4. Re-verified

```
$ python3 paper2_exact_belief_computation_v10_verification.py
verification: 30/30 checks pass     (exit 0, 7m30s)
```

Post-fix cross-check: the new needle is present in v12, and the string
`736` no longer appears anywhere in the paper.

**Caveat, unchanged:** no `pdflatex` in this environment; v12 is not
compiled.

## 5. Still open

* Titles and abstracts across all four papers — not yet reviewed.
* Supplementary material — not yet reviewed.
* Whether other needles in the battery hard-code values rather than
  deriving them. This one did; the method does not generalise cheaply,
  and the same class of defect could sit in any of the other 29 checks.
