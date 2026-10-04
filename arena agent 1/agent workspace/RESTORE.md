# What was pushed, and how to get it back

Everything created in this workspace is on GitHub. The workspace itself was
emptied on purpose (120 MiB -> 25 KiB), keeping only this note and the two
push scripts.

## The push

Repository: **MIKEAA2020/general-sustainability**
Branch: **`e2-v3-source-year`** (created from `lean-audit-v4` @ `c2fe8fc`,
the E2 v27 tip)

| commit | contents |
|---|---|
| `5d86ebbbc3` | **E2 v3 (source-year) deposit** — 72 files, 4.2 MiB. Paper v29 (tex + PDF), 9 figures, the runner, kernels, families, elevation/structure/identification campaigns and their outputs, and the three verification scripts (301 battery checks, 157-quantity basis audit, 97-mutation sabotage harness). |
| `4f5e22f476` | **Remaining workspace creations** — 208 files, 4.1 MiB, under `arena agent 1/agent workspace/` with their workspace-relative paths (paper versions, Lean formalizations, audit records, notes). |
| `dea609a022` | **Last un-pushed artifacts** — 10 files (v2 intervention results and boundaries, elevation k-grid, ARV figure record, `texcheck.py`, `push_v34.py`, a Lean index, the P1 false-positive instantiation). |

Nothing was deleted before it was verified on the branch: every file's git
blob hash was compared against the branch tree, and the 3 remaining files
(`repo_paths.json`, `tree.json`, `tree_main.json`) were generated indexes of
the repository, re-derivable from any clone.

## Restore

```bash
git clone -b e2-v3-source-year \
  https://github.com/MIKEAA2020/general-sustainability.git repo

# the LaTeX engine (tectonic 0.17.0, x86_64 musl) — only if you need to rebuild
curl -sL -o /tmp/tec.tar.gz \
  "$(curl -s https://api.github.com/repos/tectonic-typesetting/tectonic/releases/latest \
     | python3 -c 'import json,sys; \
print([a["browser_download_url"] for a in json.load(sys.stdin)["assets"] \
if "x86_64-unknown-linux-musl" in a["name"]][0])')"
mkdir -p tools && tar -xzf /tmp/tec.tar.gz -C tools && chmod +x tools/tectonic
```

## Where the E2 paper now lives

`arena agent 1/paper rewrites/latex/paperE2_cod_intervention_v29.{tex,pdf}`
plus `figs_e2_v3/fig1..fig9`. Re-run the checks from that folder:

```bash
cd "repo/arena agent 1/paper rewrites/latex"
python3 paperE2_cod_intervention_v29_verification.py      # 301 passed, 0 failed
E2_REPO=/path/to/repo/wave_e_cod \
  python3 paperE2_cod_intervention_v29_basis_audit.py     # 157 / 0 on v2 / 0 unexplained
python3 paperE2_cod_intervention_v29_sabotage.py          # 97 mutations, 0 holes
```

## Still open

* **Zenodo** — re-deposit as v3, keeping v2. Issue a new version with a note
  naming the convention change; do not overwrite. Needs a human.
* The branch has not been merged into `main`.

---

# 2026-09-30 — workspace trimmed back under budget

The repository was cloned into `repo/` to unblock the Phase 1 claim audit. That added
**924 MB / 6,407 files**, far past the workspace snapshot cap (~128 MB / 10,000 files). The cap
began pruning on its own: `repo/` self-trimmed from 6,407 files to 2,416 before any deletion was
done by hand.

## What was pushed first (nothing deleted before it was verified on the branch)

| commit | contents |
|---|---|
| `e8755a1624` | Restored unit 1 (`paper01_v63`), Phase 0 closure, Phase 1 stale-value pass |
| `4febe9921c` | Emergency push: 15 unit-source `.tex`, all `papers/*.md`, all tooling, 2.6 MB |
| `4a803d296a` | Sweep completion: everything never previously committed — 252 files, 15.1 MB |

A full sweep then compared every workspace file against the branch tree by basename.
**Result: the entire workspace is mirrored.** The only file not committed is excluded on purpose
(see below).

## What was deleted from the workspace

All three are recoverable; none contained workspace-original content.

| Deleted | Size | Recover by |
|---|---|---|
| `repo/` | 106 MB at deletion (was 924 MB) | `git clone -b e2-v3-source-year https://github.com/MIKEAA2020/general-sustainability.git repo` |
| `tools/` | 69 MB — `tectonic` 26 MB + `tcache` 44 MB | the `curl` / `tar` command in the Restore section above |
| `lean/` | 1.2 MB | present in the repository |

**Workspace after deletion: 15 MB in 253 files** — comfortably under the cap.

## Deliberately NOT committed

- **The GitHub PAT** — a credential, and this repository is **public**: it must never be
  committed. It persists as local files only; see "GitHub PAT persistence" below.
- **`p5/reps.pkl`** — a 40-byte pickle, referenced by no script in the workspace. Contents
  recorded here so nothing is lost: `[[0, 5, 9, 12], [1, 5, 9, 13]]`. Pickles are also an
  arbitrary-code-execution risk to anyone loading one from a public repository, so it stays out.

## Consequence for compilation

No LaTeX toolchain is obtainable in this session — `apt` needs root, and the tectonic release
fetch returns a 9-byte non-gzip file. Deleting `tools/` removes the last local engine, so **all
checks on the papers remain static** (brace balance, environment balance, dangling `\ref`,
8-gram content coverage). Compilation is unverified and this is recorded as residual risk in
`papers/PRIOR_ART_PASS.md` §3.1 and `papers/PHASE0_MERGE_VERIFICATION.md`.

---

# 2026-10-04 — GitHub PAT persistence (owner directive)

The repository is **public**, so the fine-grained GitHub PAT (Contents: read/write on this
repo, 93-char format) is **never committed** — it persists as local files only, in three
copies, all mode 600:

| copy | location | survives |
|---|---|---|
| durable / tooling | `/home/z/my-project/.github_pat` | durable-volume snapshots (read by `gh_bootstrap.sh`) |
| explicit backup | `/home/z/my-project/backup/.github_pat` | durable-volume snapshots |
| workspace root | `arena agent 1/agent workspace/.github_pat` (untracked) | any reset that leaves the clone in place |

Recovery after any reset, in order:

1. If any copy survives: `cp <copy> /home/z/my-project/.github_pat && chmod 600 /home/z/my-project/.github_pat`
2. `bash /home/z/my-project/gh_bootstrap.sh` — rebuilds `.git-credentials` (durable volume +
   home mirror), re-applies the git config, verifies with `ls-remote`, and falls back
   through the three copies above if the durable copy is missing.
3. If the clone is gone: `git clone -b e2-v3-source-year https://github.com/MIKEAA2020/general-sustainability.git`
4. If no copy survives: the owner must reissue a PAT (93-char fine-grained format,
   Contents read/write on this repo). The 2026-10-03/04 failure mode — a stale 92-char
   token restored by a durable-volume rollback — is documented in the worklogs.

The `.gitignore` rule `.github_pat` is load-bearing: it keeps every local copy out of any
future sweep. If this repository is ever made private and the owner then wants the token
tracked in-git like other workspace files, that requires an explicit new directive; until
then, never paste the token value into any committed file, worklog, or commit message.
