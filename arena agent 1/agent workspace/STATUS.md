# Lean verification environment — status & findings

Date: 2026-09-27. Owner: MIKEAA2020 (GitHub PAT supplied, auth verified).

## 1. The budget problem and how it's solved

The workspace snapshot is capped at ~128 MB, but:

| Thing | Real size |
|---|---|
| One Lean toolchain | ~2.9 GB |
| mathlib source + olean tree | ~6.5–7.4 GB |
| mathlib compressed cache (`.ltar`) | ~450 MB |

**None of that may live under `/home/user`.** Everything heavy is under
`/var/tmp/lean` (writable, on the 25 GB root disk, *not* snapshotted).
Only small `.lean` sources, notes and scripts live in `/home/user`.

- `ELAN_HOME=/var/tmp/lean/elan`, `LAKE_HOME=/var/tmp/lean/elan/lake`
- `XDG_CACHE_HOME=/var/tmp/lean/xdgcache` — mathlib's cache tool writes ~450 MB
  to `$XDG_CACHE_HOME/mathlib`; if left default it lands in `/home/user/.cache`
  (excluded from snapshots, but it wastes the shared disk).
- Re-provision any time with `source ./lean-bootstrap.sh`.

Current persisted footprint: **~10 KB** (`du -sh --exclude=.cache /home/user`).

## 2. Machine

2 cores, ~2 GB RAM, no swap, 25 GB disk. Builds are CPU/RAM-bound.

## 3. Measured benchmarks (all real, this session)

| Scenario | Jobs | Wall time | Peak RSS |
|---|---|---|---|
| `import Mathlib` (whole), elaborating 1 file | 8,977 | **870 s** (~14.5 min) | ~1 GB |
| Narrow imports (`Mathlib.Basic.Real.Basic` + `Mathlib.Tactic`) | 3,119 | **139 s** (2.3 min) | — |
| **real project** `automata-/supplementary/lean/BST` | 2,104 | **413 s** (6.9 min) | ~1 GB |

**Incremental rebuilds do not recompile mathlib** — verified 0 mathlib `.olean`
files touched during a rebuild. Cost is *elaborating your own file*, so the
single biggest lever is **narrow imports**, ~6× faster.

## 4. Toolchains installed

```
leanprover/lean4:v4.33.0-rc2   <- automata- pin
leanprover/lean4:v4.34.1       <- general-sustainability pin
leanprover/lean4:v4.35.0-rc3   <- current mathlib master pin
```

## 5. Findings — the two Lean-bearing repos

### `automata-` → `supplementary/lean/BST`  ✅ BUILDS CLEAN

- Pins `leanprover/lean4:v4.33.0-rc2`, mathlib rev `1f0fbd1ad9ff`.
- `lake update` 185 s; `lake exe cache get` 25 s; `lake build` **413 s, rc=0**,
  2,104 jobs, "Build completed successfully".
- **No `sorry`, no `admit`, no `axiom`** anywhere. 17 theorems/lemmas:
  Anova 2, Centring 4, Halving 5, Refine 3, Sandwich 3.
- `lakeOptions`: `autoImplicit = false`.
- Warnings only (not errors):
  - `Mathlib.Data.Real.Basic` **deprecated → `Mathlib.Basic.Real.Basic`**
    (Anova:10, Halving:14, Sandwich:11)
  - `BST/Sandwich.lean:38` unused variables `hx₁`, `hx₂`.

**Important:** the prebuilt olean cache *does* resolve for this old pinned rev
(8,960 files). I initially flagged this repo as risky on the assumption an old
rev would force a from-source build of ~9,000 modules on 2 cores / 2 GB. That
assumption was **wrong** — the cache is content-hash keyed and works fine.

### `general-sustainability` → `lean/Formalizations`  (not built yet)

- Pins `leanprover/lean4:v4.34.1` (installed).
- **`lake-manifest.json` has zero packages** — deliberate: `Prelude.lean` states
  the project has no external dependencies (no Mathlib) so `lake build` works
  offline on a bare toolchain.
- 11 files, self-contained ordered-field (`OrdField`) formalization.
  `P1_AssessmentSeparation.lean` is 160 KB (the big one).
- Should build in **seconds**, not minutes.

## 6. The key consequence for "which theorems are faulty"

Because BST builds **green at its own pinned rev**, a fault cannot show up
there. Faults only appear when the target moves — i.e. building the *later*
versions against a **newer** mathlib, where things like
`Mathlib.Data.Real.Basic → Mathlib.Basic.Real.Basic` become hard errors.

So "gold-standard `lake build`" needs a decision from you:
- **(a) pinned rev** — reproduces the project as declared; BST already passes.
- **(b) newer mathlib** (v4.34.1 / v4.35.0-rc3) — actually surfaces breakage,
  but changes the declared dependency, and needs a second mathlib tree.

Disk is currently **3.7 GB free**, so a second full mathlib tree (~7 GB) will
**not** fit until the existing one is cleared.

## 7. live.lean-lang.org (playground)

Good for triage, with one caveat: it runs a **current** mathlib/Lean, not the
project's pinned old rev. A snippet that passes there may still fail at the pin,
and vice versa. Use it to isolate a suspicious theorem; confirm with a real
`lake build`.

## 8. Waiting on you

No papers arrived with your message. You said you'd upload them separately.
