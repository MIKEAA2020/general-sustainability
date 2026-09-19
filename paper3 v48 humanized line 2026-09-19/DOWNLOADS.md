# Third-party downloads cleared from this workspace

Cleared on 2026-09-19 to bring the workspace back under the snapshot budget. Neither is paper3 content and neither
is read by any build, gate or package script (checked: `grep -rl` over `*.py`, `*.md`, `*.sh`, `*.txt` for each path
returned nothing). Each is re-fetched with the command recorded beside it.

## Verified hashes of the three large files, so a re-fetch can be checked

| file | sha256 | size | where it is now |
| --- | --- | --- | --- |
| `tools/tectonic` | `a98aa59ad5c1df39a6c9e56cbfc5088f2b11d6c179c0130b97998e4bd46a46da` | 26,401,904 B | archived on GitHub (see `PUSH_RECORD.md`) and deleted from the workspace |
| `revision/v7/analysis/nfa_tau/source/NFA_2018_edition_kaggle.csv` | `60968f7c9959537f8e67f915aca4259662b5cd42c3a0ec02d094677b4c280ef6` | 11,857,080 B | **not pushed** - the analysis record's own `MANIFEST.md` says nothing there is redistributed by the author and the files must be re-fetched from the named deposits before any onward sharing; verified against that file's recorded hash, so re-fetching restores it exactly |
| `revision/v7/analysis/nfa_tau/source/NFA_2017_edition_kaggle.zip` | `55474f1ac3f8a29c18844744cfa77f58c3561bbb2a2e3f8c43c4d7da19babc10` | 4,639,839 B | same: recorded in `MANIFEST.md`, and `checksums.txt` holds the hash of the extracted CSV (`0dd766d975cd…`), which is the check that a fresh download is the copy that was analysed |

## `tools/` - now empty except `README.md`

The binary is archived on GitHub (branch `archive/paper3-v48-workspace`, at `…/tools/tectonic`) and then deleted
from the workspace along with the rest of the bulk; `tools/README.md` gives the two ways to restore it and the
`sha256sum` to check afterwards - `a98aa59ad5c1df39a6c9e56cbfc5088f2b11d6c179c0130b97998e4bd46a46da`, the hash of
the exact binary that typeset the four documents in the v8 package. The archive's own hash was never recorded, so
the binary's is the anchor: fetch the release asset, extract, and check it against that value.

## `tools/tectonic.tar.gz` - 10,151,914 B (removed first)

The release archive the `tectonic` binary was installed from (`Tectonic 0.17.0`, one member: `tectonic`).
**The binary at `tools/tectonic` was kept**, so every transpile and compile step still runs: the builders call it by
absolute path (`build_v48_base.py:280`, `subprocess.run(['/home/user/tools/tectonic', ...])`). After the archive was
removed, four one-document compiles through that exact path succeeded (`\documentclass{article}` with `240{,}000
kt`, with `$S_{\mathcal T}$`, with `v_{\max}`, and a bare document), and `verify_v48_base.py` still returns
`*** ALL CHECKS PASS ***` with `paper3_supplementary_package_v8.zip` at the same size and hash as when it was
written. One earlier test document failed, and the cause was my test: it put `v_{\max}` outside math mode, so LaTeX
aborted on a missing `$` - nothing to do with the toolchain or the cleanup.

One repair came out of this, unrelated to the cleanup and worth knowing: the binary had lost its **executable
bit** (`Permission denied`), which would have broken the next build's four compiles. It is set again -
`chmod 755 /home/user/tools/tectonic`.

Also true of this workspace and not caused by the cleanup: the snapshot excludes `.cache`, `node_modules` and
installed packages, so a fresh sandbox starts without tectonic's format bundle (`~/.cache/tectonic`, 42 MB
re-downloaded on first compile) and without `pymupdf`, `pypdf` and `pulp`; `pip install --quiet pymupdf pypdf pulp`
is needed before a gate or the LP code runs. Nothing in the budget counts against those, since they are not
snapshotted.

```
curl -L -o /tmp/tectonic.tar.gz \
  https://github.com/tectonic-typesetting/tectonic/releases/download/tectonic%400.17.0/tectonic-0.17.0-x86_64-unknown-linux-musl.tar.gz
tar -xzf /tmp/tectonic.tar.gz -C /home/user/tools && chmod 755 /home/user/tools/tectonic
```

## The two NFA edition tables - fetched by these commands, then hash-checked

```
cd /home/user/revision/v7/analysis/nfa_tau/source
curl -sfL -o "NFA_2018_edition_kaggle.csv" \
  https://www.kaggle.com/api/v1/datasets/download/footprintnetwork/national-footprint-accounts-2018
curl -sfL -o "NFA_2017_edition_kaggle.zip" \
  https://www.kaggle.com/api/v1/datasets/download/kingburrito666/national-footprint-accounts
sha256sum NFA_2018_edition_kaggle.csv NFA_2017_edition_kaggle.zip   # 60968f7c…, 55474f1a…
python3 ../recompute_tau.py                                          # re-checks against checksums.txt
```

## `tmp/fp/` - the `footprint` R package, 3,098,654 B

`footprint_0.2.tar.gz` (CRAN, packaged 2024-07-31) and its extracted source tree (`DESCRIPTION`, `R/`, `man/`,
`tests/`, `vignettes/`). Upstream is `https://github.com/acircleda/footprint`, recorded in the package's own
`DESCRIPTION` under `URL:` and `BugReports:`. It computes airport and lat/long travel footprints; it is not the
data behind paper3's analysis record, which is the two National Footprint and Biocapacity Accounts editions held in
`revision/v7/analysis/nfa_tau/source/` and described by that directory's `MANIFEST.md`.

```
curl -L -o /tmp/footprint_0.2.tar.gz https://cran.r-project.org/src/contrib/footprint_0.2.tar.gz
mkdir -p /home/user/tmp/fp && tar -xzf /tmp/footprint_0.2.tar.gz -C /home/user/tmp/fp
# or: git clone https://github.com/acircleda/footprint /home/user/tmp/fp/footprint
```

## Left alone, deliberately

* **`github/gs`** (1,802,240 B) - a git repo tracking other papers (paper1's EMA package, the agent productivity
  papers), so it *is* unrelated to paper3. It is **not re-clonable**, which is why it stayed: `git remote` lists 0
  remotes, it is a shallow clone (`.git/shallow`), and its single commit (`ee74adb`, "Add
  paper1_assessment_separation_v43.zip", author MIKEAA2020) has an **unreadable blob** - `git show` dies with
  `fatal: unable to read 92744a27abab8bbf80bb973a74eb1cf7c5caae34` - and no copy of that zip exists anywhere in the
  workspace. The tracked entries are symlinks and at least one (`agent`) is dangling. So the repo is already partly
  damaged, but deleting it would finish the job rather than undo it. Say the word and it goes; the 1.8 MB it costs
  is not what puts the workspace over budget.
* **Derived paper3 build trees** a re-run recreates, listed so you can pick: staging directories
  `revision/v7/package_v1` … `package_v6` (15.6 MB total; rebuilt by the packaging scripts), the gate scratch
  extracts `revision/v7/.v43gate` … `.v47gate` (7.7 MB, rewritten by each gate run), `revision/v7/.logtmp`
  (4.9 MB), and `vcheck/paper3_supplementary_package_v7` (2.8 MB, recreated by
  `unzip revision/v7/paper3_supplementary_package_v7.zip -d vcheck`). Clearing the first four would put the
  workspace about 35 MB under the cap without touching any source, PDF or archive.
* **`revision/v7/analysis/nfa_tau/source/`** (16.4 MB: `NFA_2018_edition_kaggle.csv` 11.9 MB,
  `NFA_2017_edition_kaggle.zip` 4.6 MB) - re-downloadable by the two commands recorded in that directory's own
  `MANIFEST.md`, and deliberately not redistributed inside the package; but it is paper3's verification record, so
  clearing it is a decision, not a cleanup.
