#!/usr/bin/env python3
"""Wave-23 / Task 99, part 6: refresh the supplementary submission package
in place --- paper4_supplementary_v8.zip --- so its README names the
manuscript it now accompanies (v40, the cleanup round).

Why in place: the supplement DOCUMENT is unchanged this round (the
wave-23 scans found zero supplement artifacts), so no supplement version
bump and no new zip filename is warranted; but the README's Manuscript
line quotes the current manuscript's filename/checksums, which advanced
v39 -> v40.  The built-asset precedent (the graphical abstract
regenerated in place, waves 11/12 and Task 98) applies: git history
preserves the previous zip bytes, and this script records BOTH sha256
values (old and new) fail-loud.

What changes inside the package:
  1. README.md --- the Manuscript line (v39 -> v40 filename + md5s +
     the one-line round description); the "Package built" paragraph
     gains the v40 refresh sentence.
  2. verification/packaging_refresh_2026-09-19_v40.md --- NEW: the
     refresh note (what changed, what did not, the byte-identity
     verification of the payload).
  3. MANIFEST.sha256 --- regenerated over the new tree.

What does NOT change (verified byte-for-byte, file by file):
  every payload file under code_and_records/ and figure/, the
  supplementary document itself, the prior verification notes (v7/v8
  refresh notes, the re-execution record + logs).
"""
from __future__ import annotations

import hashlib
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PR = ROOT / "arena agent 1/paper rewrites"
ZIP = PR / "submission_zips/paper4_supplementary_v8.zip"

OLD_SHA256 = (
    "6af7de2051f98271f3b6f2d7708ce470c0f3ed65ce1b298e3b02f838d1339846"
)
OLD_V39_MD5 = "5ca3850f3dd3b22f917cc4b0e5dcd583"
NEW_V40_MD5 = "931bf92e8f6eeed77a08fcffc5c78daa"
NEW_V40_TEX_MD5 = "0ce11af0262a80b15a2a24bf1695254f"
NEW_V40_PDF_MD5 = "3d7f3c04680286581fba97c7d4bf1d28"
OLD_V39_PDF_MD5 = "65971aae315f74065b02104d00d28cf8"

REFRESH_NOTE = """# Packaging refresh — 2026-09-19 (v40; Task 99)

The manuscript advanced v39 -> v40 (the wave-23 cleanup round: exactly
one anchored edit — Section 1.1's phantom-strawman clause
"rather than opposed in caricature" removed; every frozen block
byte-identical; 45 pages unchanged; three byte-identical tectonic
builds, tex md5 0ce11af0262a80b15a2a24bf1695254f).  The supplementary
document is UNCHANGED at v8 (the wave-23 artifact scan found zero
supplement sites), so the package version stays v8 and this refresh is
in place (the built-asset precedent; the previous zip's sha256
6af7de2051f98271f3b6f2d7708ce470c0f3ed65ce1b298e3b02f838d1339846 is
preserved in git history and in the round record).

Changed in this refresh: the README's Manuscript line (v40 filename and
checksums) and this note; MANIFEST.sha256 regenerated.  Everything
else — the 79 payload files under code_and_records/ and figure/, the
supplementary document paper4_supplementary_v8.md, the prior
verification notes and logs — is byte-identical to the previous
package, verified file-by-file by this refresh script before rebuild.
"""


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> int:
    NEW_SHA256 = (
        "ed8e99679494e32e106c9af64587ab0ebabdac379c6850ce36b643cf00a776bd"
    )
    current = sha256(ZIP)
    if current == NEW_SHA256:
        # already refreshed: verify the post-state and exit green
        with zipfile.ZipFile(ZIP) as zf:
            nn = zf.namelist()
            assert len(nn) == 91, f"entry count {len(nn)}"
            assert ("paper4_supplementary_v8/verification/"
                    "packaging_refresh_2026-09-19_v40.md") in nn
            rtxt = zf.read(
                "paper4_supplementary_v8/README.md").decode("utf-8")
            assert NEW_V40_MD5 in rtxt and OLD_V39_MD5 not in rtxt
        print("  the package is already at the v40 refresh "
              f"(sha256 {NEW_SHA256}); post-state verified")
        print("\nrefresh_package_v40: ALL CHECKS PASS (idempotent)")
        return 0
    assert current == OLD_SHA256, (
        f"the on-disk zip is neither the pre-state nor the post-state: "
        f"{current}"
    )

    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        with zipfile.ZipFile(ZIP) as zf:
            names = zf.namelist()
            assert len(names) == 104, f"unexpected entry count {len(names)}"
            zf.extractall(tdp)
        tree = tdp / "paper4_supplementary_v8"
        assert tree.is_dir()

        # snapshot the payload for post-edit byte-identity verification
        payload = {}
        for p in sorted(tree.rglob("*")):
            if p.is_file():
                payload[p.relative_to(tree).as_posix()] = p.read_bytes()
        n_payload = len(payload)
        assert n_payload == 90, f"unexpected file count {n_payload}"

        # 1. the README Manuscript line: v39 -> v40
        readme = tree / "README.md"
        old_line = (
            f"**Manuscript:** *Governance delay and the stability of "
            f"harvested stocks: mobilising and protective feedback rules, "
            f"and the review interval as a design parameter* — "
            f"`paper4_delay_dynamics_v39.md` (md5 `{OLD_V39_MD5}`), LaTeX "
            f"`paper4_delay_dynamics_v39.tex` (md5 "
            f"`629a97ae7a92c4146f2be1ff4fd3f1fe`; three consecutive "
            f"byte-identical tectonic builds), rendered PDF "
            f"`paper4_delay_dynamics_v39.pdf` (md5 `{OLD_V39_PDF_MD5}`; "
            f"45 pages)."
        )
        new_line = (
            f"**Manuscript:** *Governance delay and the stability of "
            f"harvested stocks: mobilising and protective feedback rules, "
            f"and the review interval as a design parameter* — "
            f"`paper4_delay_dynamics_v40.md` (md5 `{NEW_V40_MD5}`), LaTeX "
            f"`paper4_delay_dynamics_v40.tex` (md5 "
            f"`{NEW_V40_TEX_MD5}`; three consecutive byte-identical "
            f"tectonic builds), rendered PDF "
            f"`paper4_delay_dynamics_v40.pdf` (md5 `{NEW_V40_PDF_MD5}`; "
            f"45 pages). The v40 round: one anchored edit (Section 1.1's "
            f"phantom-strawman clause removed); every frozen block "
            f"byte-identical to v39's."
        )
        rt = readme.read_text(encoding="utf-8")
        assert rt.count(old_line) == 1, "the v39 Manuscript line not found"
        rt = rt.replace(old_line, new_line)
        old_built = (
            "**Package built:** 2026-09-18 (the same day as the v7 "
            "refresh), from repository `MIKEAA2020/general-sustainability` "
            "(Task 98, the retitle round; the v8 refresh of the v7 package "
            "built at commit `4568560`/Task 97)."
        )
        new_built = (
            "**Package built:** 2026-09-18 (the same day as the v7 "
            "refresh), from repository `MIKEAA2020/general-sustainability` "
            "(Task 98, the retitle round; the v8 refresh of the v7 package "
            "built at commit `4568560`/Task 97); refreshed in place "
            "2026-09-19 (Task 99, the v40 cleanup round — the README's "
            "Manuscript line advanced to v40; the payload byte-identical, "
            "verified file-by-file; see "
            "`verification/packaging_refresh_2026-09-19_v40.md`)."
        )
        assert rt.count(old_built) == 1, "the Package-built line not found"
        rt = rt.replace(old_built, new_built)
        readme.write_text(rt, encoding="utf-8")

        # 2. the refresh note (new file)
        note = tree / "verification/packaging_refresh_2026-09-19_v40.md"
        note.write_text(REFRESH_NOTE, encoding="utf-8")

        # 3. byte-identity verification: every ORIGINAL payload file
        #    unchanged except README.md (and MANIFEST regenerated below)
        changed = {"README.md"}
        for rel, before in payload.items():
            if rel in changed or rel == "MANIFEST.sha256":
                continue
            after = (tree / rel).read_bytes()
            assert after == before, f"payload file drifted: {rel}"
        print(f"  payload byte-identity: {n_payload - 2} files verified "
              f"unchanged (README edited; MANIFEST regenerated)")

        # 4. regenerate MANIFEST.sha256 (the wave-22 convention: sha256
        #    of every packaged file except MANIFEST itself)
        entries = []
        for p in sorted(tree.rglob("*")):
            if p.is_file() and p.name != "MANIFEST.sha256":
                entries.append(
                    f"{hashlib.sha256(p.read_bytes()).hexdigest()}  "
                    f"{p.relative_to(tree).as_posix()}"
                )
        manifest = tree / "MANIFEST.sha256"
        manifest.write_text("\n".join(entries) + "\n", encoding="utf-8")
        n_manifest = len(entries)
        assert n_manifest == 90, f"manifest entry count {n_manifest}"
        print(f"  MANIFEST.sha256 regenerated: {n_manifest} entries")

        # 5. rebuild the zip deterministically (sorted names, fixed
        #    timestamps, deflate)
        out = tdp / "paper4_supplementary_v8.zip"
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
            for p in sorted(tree.rglob("*")):
                if p.is_file():
                    zi = zipfile.ZipInfo(
                        "paper4_supplementary_v8/"
                        + p.relative_to(tree).as_posix(),
                        date_time=(2026, 9, 19, 12, 0, 0),
                    )
                    zi.compress_type = zipfile.ZIP_DEFLATED
                    zi.external_attr = 0o644 << 16
                    zf.writestr(zi, p.read_bytes())
        new_sha = sha256(out)

        # 6. verify the rebuilt zip: entry count, the supplement document
        #    and a payload sample byte-identical, the new note present
        with zipfile.ZipFile(out) as zf:
            nn = zf.namelist()
            assert len(nn) == 91, f"rebuilt entry count {len(nn)}"
            assert ("paper4_supplementary_v8/verification/"
                    "packaging_refresh_2026-09-19_v40.md") in nn
            assert ("paper4_supplementary_v8/paper4_supplementary_v8.md"
                    in nn)
            inner = zf.read(
                "paper4_supplementary_v8/paper4_supplementary_v8.md")
            assert inner == payload["paper4_supplementary_v8.md"], (
                "the supplement document drifted in the rebuild"
            )
            for rel in ("code_and_records/dr_registration/"
                        "campaign_p4_dr_registration.py",
                        "figure/fig2_five_regime_topology_v2.png"):
                assert zf.read(
                    f"paper4_supplementary_v8/{rel}") == payload[rel], (
                    f"payload drifted in the rebuild: {rel}"
                )
            rtxt = zf.read("paper4_supplementary_v8/README.md").decode()
            assert NEW_V40_MD5 in rtxt and OLD_V39_MD5 not in rtxt
        print(f"  rebuilt zip verified: 91 entries; supplement document "
              f"and payload samples byte-identical; the README carries "
              f"the v40 checksums with the v39 md5 absent")

        # 7. replace the package in place; record both sha256 values
        shutil.copy2(out, ZIP)
        assert sha256(ZIP) == new_sha
        print(f"  OLD zip sha256: {OLD_SHA256}")
        print(f"  NEW zip sha256: {new_sha}")

    print("\nrefresh_package_v40: ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
