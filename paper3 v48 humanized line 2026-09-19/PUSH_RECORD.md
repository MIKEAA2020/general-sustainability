# What is on GitHub, and what may therefore be deleted locally

Pushed 2026-09-19 from this workspace, so the sandbox can be pruned without losing anything.

* **repo**: `MIKEAA2020/general-sustainability`. The token in `uploads/github_pat.txt` cannot create a
  repository (`POST /user/repos` answers `403 Resource not accessible by personal access token`), so the
  archive went to the repo where paper3's earlier line already lives (`arena agent 1/paper
  rewrites/latex/paper3_material_ledgers_v31.tex` and `_v32`, the reconstructed ledgers, the submission zips).
* **branch**: `archive/paper3-v48-workspace` - an **orphan** branch, one commit, no parent. Nothing else in the
  repo was written to: `main`, `edwards-framework-e1` and `edwards-framework-e1-audit-implementation` still point
  where they pointed before this session, and every push I made was a `--force` on this single ref. `main`'s head is
  `d4ec2171a2c7` ("worklog Task 98 push record: remote main 4568560 -> bdf7765", 2026-09-18T18:29:54Z, `Z User`),
  dated the day before this session, so the repo's own line of work was not disturbed by anything here. It is
  moving on its own, though, and did so while this record was being written: `ls-remote` answered `d4ec2171a2c7` and
  then `a1255b7e7038` minutes later. That is the reason for the last sentence of this bullet and not a problem -
  nothing in this workspace pushes to `main`, and the archive lives on its own ref.
  **An earlier draft of this file asserted that `main` stood at `a19a80d1…`, and that sha is not a commit in this
  repository at all** - `GET /repos/.../commits/main/a19a80d1f4b53d1e0f6b67ad0f9fba2e5d1c9f14` answers `No commit
  found for SHA` - so it was a bad transcription of mine, and the reassurance resting on it happened to be true for
  a different reason. Check with `git ls-remote https://github.com/MIKEAA2020/general-sustainability refs/heads/main`
  rather than trusting any sha fixed in prose, including the ones below. Worth knowing: `main` has its own top-level
  `tools/` folder, unrelated to the `tools/` inside this archive folder; nothing was merged between the two.
* **folder**: `paper3 v48 humanized line 2026-09-19/` - 477 files, every workspace file except the exclusions
  below, each keeping its workspace-relative path beneath that folder. 68.9 MB in the tree, 9 files over 1 MB, one
  of which (`tools/tectonic`, 25.2 MB) is deliberately present in the archive and absent from the workspace, so the
  per-file check reports 476 identical and 1 archived-only.
* **commits on it**, each a complete orphan snapshot, so only the last is reachable after the force-pushes:
  `8763235e…` (first, carried 76 files of pure duplication), `9e841ef6…` (added `tools/tectonic` and the recovered
  `revision/v7/texkit_v1.py`, dropped the staging duplicates), `7addc9cf…` (the re-packaged v8 archive and
  `tools/README.md`), `f8f19a77…` (a `DOWNLOADS.md` one edit behind - the per-file check caught it), `f0c5440db8…`
  (the record's own corrections), and the tip, which contains this sentence and cannot name its own hash. Read the
  tip with `git ls-remote https://github.com/MIKEAA2020/general-sustainability archive/paper3-v48-workspace`. - 477 files, 68.9 MB in the tree, one orphan
  commit with no parent, built in the throwaway git dir `/tmp/pushgit2` (the workspace is not a repository, so
  nothing of yours was put under version control). Two earlier snapshots of the same folder, `8763235e…` and
  `9e841ef6…`, were superseded by force-push and nothing else on the remote moved: the first carried 76 files of
  pure duplication (the `package_v7/` staging tree, byte-identical to the zip beside it), the second lacked this
  round's refresh. `git ls-remote https://github.com/MIKEAA2020/general-sustainability archive/paper3-v48-workspace`
  is the authority if these lines ever disagree.
* **what the last refresh changed**: `paper3_supplementary_package_v8.zip` is the re-package that matches the
  workspace files rather than the build before it - sha256 `3ad72c04f57985c8ed53b2d31c05bc889a0449c21ad946e229ead53aa0564fa7`
  at 2,202,539 bytes, and its manuscript md and pdf are byte-identical to the copies archived before the re-run,
  which is the evidence the rebuild was deterministic; `tools/README.md` was added where the binary used to sit;
  `DOWNLOADS.md`, `PUSH_RECORD.md` and the two `code_v3` run records were updated. `tools/tectonic` was **kept in
  the snapshot** even though it is gone from the workspace: the instruction was to push the binary before deleting
  it, and dropping it here would have made the deleted copy unreachable once the earlier commit was orphaned.

To restore: `git fetch origin archive/paper3-v48-workspace`, check it out, and copy the folder's contents back over
the workspace root - `revision/`, `revision/v48/`, `humanize/`, `humanized/`, `repo_audits/`, `review/`, `summary/`,
`work/`, `tools/README.md`, `uploads/`, `DOWNLOADS.md` and this file return as they were, including the v48 build's
md, tex and pdf, the eight package archives and every audit record.

## Verified before anything was deleted

Each archived blob was hashed against the workspace file it came from - `git hash-object` per path, compared with
the blob oid the pushed tree reports - and the branch's file set was compared with the local commit's. For the current head: **477 blobs, 476 compared to the workspace with 0 missing and 0 differing**, `truncated:
false`, remote branch head equal to the local commit. The 477th is `tools/tectonic`, which the workspace no longer
has, so it was checked the other way round: the blob was fetched back out of GitHub and it is 26,401,904 bytes with
sha256 `a98aa59a…` - the exact value the recorded build produced. That round trip is what makes deleting the binary
a verified loss of nothing. Only after these checks was anything removed.

A note on self-reference: a commit cannot contain its own hash, so the archived copy of this file describes the
refresh as "the commit after `9e841ef6`" while this workspace copy names it.

## What has been deleted locally, and what that costs

Round 1 (after the first snapshot): `revision/v7/package_v1` … `package_v7` staging trees, `.v43gate` …
`.v48gate`, `.logtmp`, `vcheck/`, `/tmp/pushgit` - 137 MB to 124 MB, and to 88 MB once the tarball and `/tmp/fp`
went. Round 2 (after the second snapshot verified): `tools/tectonic` (26 MB), the regenerated `.v47gate` /
`.v48gate` / `.logtmp` / `vcheck/` and `__pycache__`.

* **the one operational cost** is that `/home/user/tools/tectonic` is gone, and it is reached by absolute path, so
  anything that compiles stops: the four `.tex` builds behind `build_v48_base.py` and the companion builders, and
  `revision/v7/verify_v47_base.py`, which recompiles through `texkit_v1.compile_log()`. What keeps running in place
  is `revision/v48/verify_v48_base.py` (reads the PDFs on disk: `*** ALL CHECKS PASS ***`) and `build_v48_package.py`
  (copies them). `tools/README.md` has the two ways to bring the engine back and the hash to check - **and it was
  actually run today**: the sparse checkout returned the binary byte-for-byte (`a98aa59a…`, mode 755, `Tectonic
  0.17.0`), after which both gates passed, which is the end-to-end proof that the deletion cost nothing but the
  26 MB. The binary was then deleted again.
* **not deleted**: the two NFA edition tables (16 MB, pending the decision recorded below), the eight
  `paper3_supplementary_package_v*.zip` archives (the deliverable line, and the evidence that each gate was run
  against the package it covers), the `revision/v2` … `v6` history, and your `github/gs` clone, which the snapshot
  does not even carry.
* a fresh sandbox needs `pip install --quiet pymupdf pypdf pulp` as well: installed packages are not part of the
  workspace snapshot, and neither is the executable bit, which is why a restored `tools/tectonic` must be
  `chmod 755` before it stops answering `Permission denied`.
* sizes, measured after all of this: `du -sh /home/user` says **139 MB**, of which **71 MB is `.cache`** - pip and
  tectonic state that the snapshot never carried in the first place - so the workspace proper is **69 MB**. The one
  lever left is the 16 MB of NFA tables in `revision/v7/analysis/nfa_tau/source/`, which are not on GitHub and stay
  on disk until you decide how to handle them (next section).

## Recovery after the budget episode, and what it turned up

The snapshot that was over budget re-materialised the workspace at 03:07 on 2026-09-19 with reset mtimes, so mtime
could not serve as a loss signal. The pre-restore artefacts were used as the ledger instead: the 74 files inside
`paper3_supplementary_package_v8.zip` (built before the episode), each hashed against the workspace file at its real
path, plus the 47-file listing of `revision/v48` taken beforehand, diffed against the directory now.

* **one loss found**: `revision/v7/texkit_v1.py` - the module `verify_v47_base.py` imports - was gone. Recovered by
  copying `review/texkit_v1.py` into place, which is byte-identical to the copy the accepted v47 line ships
  (`sha256 12b904ac…`), so the recovery is verified rather than approximate. It is now archived at its real path.
* **nothing else missing**: all 74 package files are byte-identical to their archived copies (0 differing, 0
  truncated), every file the v48 packaging manifest lists exists (the 13 that first looked absent were a gap in my
  path search, not in the workspace - they live under `analysis/nfa_tau/` and `code_v3/` and were confirmed
  byte-identical), and no `__pycache__` entry in `revision/v48` is orphaned, which is what a deleted module leaves
  behind. The file-count cap on the snapshot (~10,000) never bound: 542 files were present.
* **the pipeline was then run end to end** as the real completeness proof: `build_v48_base.py` (four compiles
  `rc=0`, overfull 0 and right 0.0pt on all four documents, 54/19/10/8 pages, 195 of 195 flowing paragraphs on the
  page, 208 sentences placed verbatim, 17 damaged and 17 restored), `verify_v48_base.py`
  (`*** ALL CHECKS PASS ***`), and `verify_v47_base.py` (`ALL CHECKS PASS`) - the last one only possible because
  `texkit_v1.py` is back.
* the toolchain lost nothing permanently: `tools/tectonic` was pushed into the snapshot before it was deleted,
  `sha256 a98aa59ad5c1df39a6c9e56cbfc5088f2b11d6c179c0130b97998e4bd46a46da`.

## Excluded from the push, and why

| what | why | how to get it back |
| --- | --- | --- |
| `uploads/github_pat.txt` | a credential; a repository is not where it belongs | you hold it - it is not something this workspace produced |
| `revision/v7/analysis/nfa_tau/source/NFA_2018_edition_kaggle.csv`, `NFA_2017_edition_kaggle.zip` (16 MB) | **not pushed, and this is a decision I have left to you rather than taken.** The manifest beside them states that the edition tables are redistributed by no one in this package and that a third party is to be referred to the named deposits; this repository is public, so pushing them there would contradict the recorded terms for the sake of local disk, which the hashes make unnecessary. `source/MANIFEST.md` itself **is** archived, so the exclusion and the route back are legible | the two `curl` commands recorded in that manifest and in `DOWNLOADS.md`, then `sha256sum` against `60968f7c…` and `55474f1a…` (the values the manifest already carried, which is how the surviving copies were shown to be the analysed ones); `recompute_tau.py` re-checks them |
| `tools/tectonic.tar.gz` | a download, superseded by the binary it produced, which *is* archived | `DOWNLOADS.md` has the `curl` |
| `revision/v7/package_v*`, `.v4*gate`, `.logtmp`, `vcheck/` | derived scratch: staging trees duplicating the pushed archives, gate extracts each run rewrites | `unzip` the matching archive, or re-run the builder or gate |
| `github/` | another repository's working copy, left alone by instruction; it has no remote configured, which is why it was not assumed re-clonable | your own copy |
| `.cache`, `.local`, `.npm`, `__pycache__` | machine state, already outside the workspace snapshot | n/a |

Asked and answered on 2026-09-19: **leave them exactly as they are**. Not pushed anywhere, not deleted, not put in
a private repository - so the 16 MB stays in the workspace and the recorded hashes plus `recompute_tau.py` remain the
route back if you ever want it gone. The other decision taken at the same time: the archive **stays an orphan branch**,
not folded into `main` and not deleted - which is why the recipe below is left here unused rather than executed.

## To fold the archive into `main` as a folder instead of a branch

Not done, by your decision. If it is ever wanted, these are the commands:

```
git clone --filter=blob:none https://github.com/MIKEAA2020/general-sustainability gs
cd gs && git fetch origin archive/paper3-v48-workspace
git checkout main
git checkout archive/paper3-v48-workspace -- 'paper3 v48 humanized line 2026-09-19'
git commit -m 'add the paper3 v48 humanized line archive (workspace copy, 2026-09-19)' && git push
```

To drop the branch afterwards: `git push origin --delete archive/paper3-v48-workspace`.

One caution that belongs beside this record rather than in a commit message: `metabolic-curvature-measure` has a
`.env` committed on its `main`, and this workspace holds a live `github_pat.txt` in `uploads/`. Both are worth
rotating or moving out of version control and out of plain files; `git filter-repo` is the blunt instrument for the
first, a fresh scoped token for the second.
