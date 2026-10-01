#!/usr/bin/env python3
"""Verify byte-for-byte Lean sources and the archived reproducibility snapshot.
Fail closed if either the checkout or the snapshot differs from the fixed manifest.
This does not replace a Lean build or axiom-footprint execution.
"""
import csv
import hashlib
import io
from pathlib import Path
import tarfile

ROOT = Path(__file__).resolve().parent.parent
HERE = Path(__file__).resolve().parent

def git_blob(data: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()

with (HERE / 'SOURCE_MANIFEST.tsv').open(newline='') as f:
    rows = list(csv.DictReader(f, delimiter='\t'))
assert len(rows) == 69, f'Expected 67 Lean project files plus two footprint-check sources, got {len(rows)}'
expected = {row['path']: row for row in rows}
check_sources = {'lean_repro/AxiomFootprint.lean', 'lean_repro/AllFootprints.lean'}
assert len(expected) == len(rows) and all(p.startswith('lean/') or p in check_sources for p in expected)
actual_paths = {str(p.relative_to(ROOT)) for p in (ROOT / 'lean').rglob('*') if p.is_file() and not p.is_symlink() and '.lake' not in p.parts}
actual_paths.update(check_sources)
assert set(expected) == actual_paths, f'Changed Lean project file set: {sorted(actual_paths ^ set(expected))}'
archive = HERE / 'source_snapshot.tar.gz'
assert hashlib.sha256(archive.read_bytes()).hexdigest() == (HERE / 'SOURCE_ARCHIVE.sha256').read_text().split()[0]
with tarfile.open(archive, 'r:gz') as tf:
    members = {m.name: m for m in tf.getmembers()}
    assert set(members) == set(expected), f'Archive path mismatch: {sorted(set(members) ^ set(expected))}'
    for path, row in expected.items():
        assert members[path].isfile() and not members[path].issym(), path
        archived = tf.extractfile(members[path]).read()
        checked_out = (ROOT / path).read_bytes()
        for label, data in [('archive', archived), ('checkout', checked_out)]:
            assert len(data) == int(row['bytes']), (path, label, 'size')
            assert git_blob(data) == row['git_blob_sha1'], (path, label, 'Git blob')
            assert hashlib.sha256(data).hexdigest() == row['sha256'], (path, label, 'SHA-256')
        assert archived == checked_out, path
print(f'INPUTS VERIFIED: {len(rows)} project/check-source files; archive SHA-256 {(HERE / "SOURCE_ARCHIVE.sha256").read_text().split()[0]}')
print('SOURCE COMMIT:', (HERE / 'SOURCE_COMMIT.txt').read_text().strip())
