# tectonic - the compile step needs this directory

`build_v48_base.py`, `build_supp_tex_v1.py` and `build_companions_v1.py` invoke the engine by absolute path:
`/home/user/tools/tectonic`. The 26 MB binary that was here is archived in the paper3 snapshot on GitHub
(`tools/tectonic` inside `paper3 v48 humanized line 2026-09-19/` on the branch `archive/paper3-v48-workspace`
of `MIKEAA2020/general-sustainability`) and was removed from the workspace to clear the budget.

Restore it either way, then check the hash before trusting it:

```
# 1. from the release (needs network, nothing else)
curl -sL -o /tmp/tectonic.tar.gz \
  https://github.com/tectonic-typesetting/tectonic/releases/download/tectonic%400.17.0/tectonic-0.17.0-x86_64-unknown-linux-musl.tar.gz
mkdir -p /home/user/tools && tar -xzf /tmp/tectonic.tar.gz -C /home/user/tools && chmod 755 /home/user/tools/tectonic

# 2. or from the archive branch, byte-for-byte the file this workspace built with
git clone --filter=blob:none --no-checkout -b archive/paper3-v48-workspace \
  https://github.com/MIKEAA2020/general-sustainability /tmp/gs
cd /tmp/gs && git sparse-checkout set 'paper3 v48 humanized line 2026-09-19/tools' && git checkout
install -m 755 '/tmp/gs/paper3 v48 humanized line 2026-09-19/tools/tectonic' /home/user/tools/tectonic

# verify - this is the hash of the binary that produced the four PDFs in the v8 package
sha256sum /home/user/tools/tectonic
# a98aa59ad5c1df39a6c9e56cbfc5088f2b11d6c179c0130b97998e4bd46a46da
```

Two things this workspace learned the hard way, both recorded here so they do not repeat: the executable bit is
not preserved by the workspace snapshot, so a restored `tools/tectonic` comes back `Permission denied` and every
compile fails for a reason that looks like a LaTeX error; and the first run after an install downloads tectonic's
format bundle into `~/.cache/tectonic` (42 MB, outside the snapshot, so it is free of the budget but not free of
time - about a minute).

What still works without the binary, and what does not - established by running each of them, not by reading the
sources. Runs: `/home/user/revision/v48/verify_v48_base.py`, whose typesetting group reads the PDFs already on disk
and does not invoke the engine (`*** ALL CHECKS PASS ***` on 2026-09-19 with the binary absent, then again green with
it restored), and `build_v48_package.py`, which copies existing PDFs. Does not run: any builder that compiles -
`build_v48_base.py` and the two companion builders - and `revision/v7/verify_v47_base.py`, because it calls
`texkit_v1.compile_log()`, which is where the absolute path above is defined (`TECTONIC = '/home/user/tools/tectonic'`
in `revision/v7/texkit_v1.py`). If you see `FileNotFoundError: /home/user/tools/tectonic` from the v47 gate, this is
the reason, and the gate is not reporting a defect in the document.

The recipe above was executed on 2026-09-19 rather than merely written: a sparse checkout of this branch returned
`tools/tectonic` at 26,401,904 bytes with sha256 `a98aa59a…`, mode `-rwxr-xr-x`, reporting `Tectonic 0.17.0`, and
both gates then passed. Two environment notes from the same exercise: git carries the executable bit in the tree
(`100755`), so the `chmod` above is needed only when the file arrives by way of the workspace snapshot or a plain
`curl` extraction; and the gates and the packaging script import `pymupdf`, which no snapshot carries, so a fresh
sandbox needs `pip install --quiet pymupdf pypdf` first.
