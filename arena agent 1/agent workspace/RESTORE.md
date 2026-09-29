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
