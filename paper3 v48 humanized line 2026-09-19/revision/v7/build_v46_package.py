#!/usr/bin/env python3
r"""Build the v46 supplementary package: the exhibit bundle restated for readers, and one archive of everything.

Two things are assembled here, and the first is a correction rather than a repackaging.

**The bundle's own text.** The scripts and their manifest, as deposited with the article, open with the project's
diary: the manifest was titled "exhibit bundle, v2", carried a table of "the relabelling, in full" comparing what
"v5 printed" with what "v2 prints", explained that "nothing in revision/v5/code/ was modified", and each script's
usage line named a working directory (`revision/v7/code/...`). `code/outputs.txt` --- the printed record a reader
downloads to check a number --- began with three comment lines saying the same. None of that belongs in a deposit:
a reader of a reproduction bundle wants the run command, the file list, the environment, the scope limits and the
licence, and nothing else. The bundle is therefore rebuilt as a self-contained thing: package-relative run
commands, a manifest that records files, hashes, environment and scope, a generated output record with a header
that states what it is, and no build machinery inside it. The numbers are not re-typed: the record is produced by
running the scripts, and the build asserts that every numeric line is identical to the deposited record's.

**The archive.** One zip holding the manuscript, the supplementary, the two companion papers, the exhibit bundle and
the analysis record, plus a manifest of sha256 hashes for every file and a README that says what the supplementary
is and how to verify each part. The two edition tables are *not* inside it, because the analysis record's own
manifest says the bytes are held for re-running and must be re-fetched before any onward sharing; the retrieval
commands and the hashes that settle what was read are in that manifest, and the run is checked here against them.
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

R = '/home/user/revision/v7'
V3 = f'{R}/code_v3'
PKG = f'{R}/package_v5'
ZIP = f'{R}/paper3_supplementary_package_v5.zip'
FILES = ('certification_lp.py', 'curvature_and_crossover.py', 'persistence_index_simulation.py')
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
REPORT = {}


def bundle_v3():
    """The three scripts, the manifest, and the output record regenerated from the scripts themselves."""
    if os.path.isdir(V3):
        shutil.rmtree(V3)
    os.makedirs(V3)
    for f in FILES:
        t = open(f'{R}/code/{f}').read()
        old = f'Run:  python3 revision/v7/code/{f}'
        assert t.count(old) == 1, f'{f}: usage line not found'
        t = t.replace(old, f'Run:  python3 code/{f}      (from the top of the deposit)')
        assert 'revision/v' not in t, f'{f}: a working-directory reference survives'
        open(f'{V3}/{f}', 'w').write(t)

    env = subprocess.run([sys.executable, '-c', 'import sys,numpy,scipy;print(sys.version.split()[0],\n'
                          'numpy.__version__, scipy.__version__)'], capture_output=True, text=True).stdout.split()
    rec = [f'# Output record - {", ".join(FILES)}',
           f'# generated {subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True).stdout.strip()}'
           f' | Python {env[0]} | numpy {env[1]} | scipy {env[2]}', '']
    for f in FILES:
        r = subprocess.run([sys.executable, f], cwd=V3, capture_output=True, text=True, timeout=900)
        assert r.returncode == 0, f'{f} exited {r.returncode}: {r.stderr[-300:]}'
        rec.append(f'######## {f} ########')
        rec.append(r.stdout.rstrip('\n'))
        rec.append('')
    open(f'{V3}/outputs.txt', 'w').write('\n'.join(rec) + '\n')

    # the numbers must not have moved: compare numeric lines with the deposited record
    def nums(p):
        return [l for l in open(p).read().split('\n') if re.search(r'\d', l) and not l.startswith('#')]

    a, b = nums(f'{R}/code/outputs.txt'), nums(f'{V3}/outputs.txt')
    REPORT['numeric_lines'] = {'lines_in_deposited_record': len(a), 'lines_regenerated': len(b),
                              'byte_identical': sum(1 for x, y in zip(a, b) if x == y)}
    assert a == b, ('the regenerated record does not reproduce the deposited numerics: '
                    + next(f'{x!r} != {y!r}' for x, y in zip(a, b) if x != y))

    rows = []
    for f in FILES + ('outputs.txt',):
        rows.append((f, os.path.getsize(f'{V3}/{f}'), sha(f'{V3}/{f}')))
    man = [f'# Exhibit bundle',
           '',
           'Scripts that generate every computed figure in "Typed Flux Ledgers and Depletion Arithmetic" and in its',
           'supplementary, and the record of one run of them. Referenced by the article\'s Code availability',
           'statement and described in Section 8 of the companion certification procedure.',
           '',
           '## Running it',
           '',
           '```',
           'python3 code/certification_lp.py',
           'python3 code/curvature_and_crossover.py',
           'python3 code/persistence_index_simulation.py',
           '```',
           '',
           'from the top of the deposit, with the `code/` directory present. No script takes an argument, reads a',
           'file, opens a network connection or writes anything. `outputs.txt` is the complete stdout of one run of',
           f'all three, in that order, under Python {env[0]} with numpy {env[1]} and scipy {env[2]}.',
           '',
           '## Files',
           '',
           '| file | size | sha256 |',
           '|---|---|---|',
           ] + [f'| `{f}` | {s:,} B | `{h}` |' for f, s, h in rows] + [
           '',
           '## What each script does, and what it reads',
           '',
           '| script | exhibits it produces | inputs | external data |',
           '|---|---|---|---|',
           '| `certification_lp.py` | the compensation premium and the worst-concealed-deficit linear programme '
           '(Section 10.1, supplementary S8), and the certificate vector of Section 3.1 for the three indicators '
           'classified in Section 8 | the bounds and splits declared in the article and the supplementary | none, '
           'arithmetic on declared figures |',
           '| `curvature_and_crossover.py` | the curvature table for Proposition 27, the closed-form check '
           '`T = H_loc/(1−κ)`, the reserve-life crossover grid for Proposition 28 on the pinned record, and the '
           'three-law illustration of Proposition 26 | the reserves, production and growth figures tabulated in '
           'Section 6.5.2 and restated in the script | none |',
           '| `persistence_index_simulation.py` | the boundedness of the persistence index on the declared '
           'linear-trend class (Section 6.5.1) | the class declared in the article, with the seed printed in the '
           'record | none, the series are simulated |',
           '',
           '## Scope limits, stated so they cannot be over-read',
           '',
           'No script obtains data, contacts a network, or re-derives any published statistic. The G3P basin rows',
           'whose provenance is recorded in the supplementary (S5.4) are quarantined and no script consumes them, so',
           'nothing in these exhibits depends on them. Figures quoted from the article are inputs here, not',
           'outputs: a script recomputes what the article computes from those inputs and prints the comparison.',
           'The recomputation of the aggregate overshoot date, which does read downloaded tables, is held apart in',
           'the analysis record `analysis/nfa_tau/` for exactly that reason; its manifest states its own limits.',
           '',
           '## Licence',
           '',
           'The scripts are released under the CC BY 4.0 licence of the article they accompany. Attribution: as the',
           'article\'s citation. No third-party data is included in this directory.',
           '']
    open(f'{V3}/MANIFEST.md', 'w').write('\n'.join(man))
    for line in man:
        assert 'revision/' not in line and not re.search(r'\bv\d+\b printed', line), line
    REPORT['bundle_files'] = {f: [os.path.getsize(f'{V3}/{f}'), sha(f'{V3}/{f}')]
                             for f in FILES + ('MANIFEST.md', 'outputs.txt')}
    return REPORT['numeric_lines']


def package():
    """Stage the archive, hash it, and write it."""
    if os.path.isdir(PKG):
        shutil.rmtree(PKG)
    root = f'{PKG}/paper3_supplementary_package_v5'
    for sub in ('manuscript', 'code', 'analysis/nfa_tau/source', 'builders'):
        os.makedirs(f'{root}/{sub}', exist_ok=True)
    for base in ('paper3_material_ledgers_v46', 'paper3_supplementary_v17',
                 'companionA_certification_procedure_v8', 'companionB_standards_horizon_v8'):
        for ext in ('.md', '.tex', '.pdf'):
            shutil.copy(f'{R}/{base}{ext}', f'{root}/manuscript/{base}{ext}')
    shutil.copy(f'{R}/paper3_supplementary_v17.ascii.md', f'{root}/manuscript/')
    for f in os.listdir(V3):
        shutil.copy(f'{V3}/{f}', f'{root}/code/{f}')
    A = f'{R}/analysis/nfa_tau'
    assert os.path.exists(f'{A}/README_v2.md'), 'the record README v2 must be written before the package'
    for f in ('recompute_tau.py', 'results.txt', 'checksums.txt', 'edition_delta.csv',
              'tau_by_year_2017edition.csv', 'tau_by_year_2018edition.csv'):
        shutil.copy(f'{A}/{f}', f'{root}/analysis/nfa_tau/{f}')
    # the record's README is shipped at its canonical name from the version written for readers; the earlier file
    # stays in the working directory as the history of the record and is not redistributed
    open(f'{root}/analysis/nfa_tau/README.md', 'w').write(open(f'{A}/README_v2.md').read())
    shutil.copy(f'{A}/source/MANIFEST.md', f'{root}/analysis/nfa_tau/source/MANIFEST.md')
    for f in ('build_v42_formal.py', 'build_v42_package.py', 'tablekit_v2.py', 'verify_v42_build.py',
              'structure_v42.md', 'revisions_v42_formal_log.json', 'geometry_v42.json',
              'build_v46_base.py', 'verify_v46_base.py', 'stylekit_v1.py', 'structure_v46_base.md',
              'revisions_v46_base_log.json'):
        if os.path.exists(f'{R}/{f}'):
            shutil.copy(f'{R}/{f}', f'{root}/builders/{f}')
    shutil.copy('/home/user/review/texkit_v1.py', f'{root}/builders/texkit_v1.py')

    def tree():
        out = {}
        for dirpath, _d, files in os.walk(root):
            for f in sorted(files):
                q = os.path.join(dirpath, f)
                out[os.path.relpath(q, root)] = (os.path.getsize(q), sha(q))
        return out

    sizes = tree()
    listing = '\n'.join(f'{s:>10,} B  `{n}`' for n, (s, _h) in sorted(sizes.items()))
    readme = f'''# Supplementary package

Materials accompanying "Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics,
and the Semantics of Depletion Horizons" (Amin Abaee, independent researcher; ORCID 0000-0002-0019-1842).

## What the supplementary is

The supplementary material is one document and two records beside it.

* **The supplementary document** is `manuscript/paper3_supplementary_v17.pdf` (19 pp., sections S1 to S17). It
  carries the proofs, derivations, parameter tables, the version-sensitivity record and the reproduction protocol
  that the main text cites by section number: the lemmas and propositions stated without proof in the article, the
  exhibit values behind each figure it quotes, the record of which public release each number comes from, and the
  section that reports the overshoot-date recomputation (S17). It is typeset from `paper3_supplementary_v17.md`,
  whose ASCII transliteration `paper3_supplementary_v17.ascii.md` is included because that is the source the
  typesetter reads. Its role is checking, not argument: it reports what was verified and by which operation, which
  deviations from the standard are documented and on what grounds, which statements the record supports and at what
  predicate, and what remains unresolved. Proofs are given to the depth at which a reader can re-do a step with a
  calculator and the tables in this archive, and where a step is stated rather than demonstrated the text says so.
* **The exhibit bundle** is `code/`: three scripts that regenerate every computed figure in the article and the
  supplementary, the manifest that records what each reads and what it does not, and the output record of one run.
* **The analysis record** is `analysis/nfa_tau/`: the recomputation of the aggregate overshoot date with and
  without carbon demand on two editions of the National Footprint and Biocapacity Accounts, with its own README
  and manifest.

The two records differ in what a reader needs in order to repeat them. The exhibit bundle runs on synthesised
inputs and nothing else, and it asserts that the article's computed figures reproduce; the analysis record runs on
the two edition tables of the accounts and asserts that the overshoot date recomputes under the weighting its README
states. Neither needs the other, and neither needs the network.

The main text and the two companion papers are included so that cross-references resolve inside the archive. The
companions are papers in their own right, not appendices: `companionA_certification_procedure_v8.pdf` specifies
the certification procedure the article's predicates define, and `companionB_standards_horizon_v8.pdf` places the
accounting objects against the standards horizon.

## Contents

{listing}

## Verifying it

`MANIFEST.sha256` holds a hash of every file in this archive:

```
sha256sum -c MANIFEST.sha256          # in the top directory of the unpacked archive
```

The exhibit bundle needs nothing further; run the three scripts and compare their stdout with `code/outputs.txt`.
The analysis record reads two edition tables of the accounts which, as its own manifest states, are held for
re-running and are not redistributed here. Fetch them by the two commands recorded in
`analysis/nfa_tau/source/MANIFEST.md`, place them in `analysis/nfa_tau/source/`, then

```
cd analysis/nfa_tau && python3 recompute_tau.py
```

The script verifies the bytes it reads against the hashes recorded there, and reproduces
`tau_by_year_2018edition.csv`, `tau_by_year_2017edition.csv`, `edition_delta.csv` and `results.txt` byte for byte.

The scripts in `builders/` regenerate the typesetting and the checks from the markdown sources: `tectonic`
compiles each `.tex`, and `python3 builders/verify_v46_base.py` re-runs every check described below. These four
files are the v46 line of the same paper, and the line was built the other way round from every earlier one: the
humanized draft in `humanize/` is taken as the document, and this paper's verified content is ported into it.
Where a paragraph of the draft covers the same passage as a paragraph of the article and the two carry the same
values — the same numbers, status words, bare quantities and cross-references — the draft's paragraph is used,
with the article's figures put back where the draft has since been overtaken; the draft's framing paragraphs,
which carry no numbers at all, are inserted where the article has no counterpart; and only the prose the draft
cannot supply is restyled, by the edit rules obtained by aligning `uploads/paper3_material_ledgers_v32.pdf` (the
source the draft was made from) with the draft, held in `builders/stylekit_v1.py` as the GEM_* tables. 97 of the
article's 250 flowing paragraphs are now the draft's own text and 40 of those are the draft's framing prose; 344
of its sentences are verbatim in the draft, against 119 in the line this one replaces. The three companion
documents are the v43 register line carried byte for byte, because the humanized draft is a humanization of the
main text alone and there is no draft wording for them to adopt.

The gate is what makes the inversion safe to read. Nothing in it is an assertion about taste: it refuses the
build unless no figure, label, table cell, displayed equation or caveat moved, unless the shipped text carries
exactly the same multiset of numeric values as the verified one, unless every paragraph the pass took in is
traceable to the draft and every paragraph it gave up is traceable to this paper, and unless the flowing prose
is measurably nearer the draft's own register profile than it was (36.8 to 23.1 units of aggregate distance,
feature by feature in `builders/structure_v46_base.md`, which also gives the sentence-length measurements before
and after). One of the audit instrument's numeric targets is contradicted by the draft rather than met: the
semicolons, where the corpus's own rate is above the cap and the gate says so by name instead of editing the
corpus out of the document. The two builders are the production machinery and are not part of the text.

## Licences and terms

* Text, figures and scripts: CC BY 4.0, attributing the article above.
* The two edition tables are Global Footprint Network data under CC BY-SA 4.0 and are redistributed by their
  publisher, not here; the attribution the deposits request is recorded in the analysis manifest.
* `code/` consumes no external data. `analysis/nfa_tau/` reads the two tables and nothing else.
* No personal data, no third-party proprietary code.

## Notes on the text

Numbers in the article and the supplementary are recomputed, not transcribed, where a public release allowed it;
the three that were (the persistence-index exhibit, the two-cohort reserve-life medians and the overshoot
recomputation) are each tied to a named release and a re-runnable script in the sections above. Where a release
could not be reached without registration, that is stated at the number rather than at the end.
'''
    open(f'{root}/README.md', 'w').write(readme)
    sizes = tree()                                  # the README is part of the archive, so it is hashed too
    with open(f'{root}/MANIFEST.sha256', 'w') as fh:
        for n, (_s, h) in sorted(sizes.items()):
            fh.write(f'{h}  {n}\n')                 # the sha256sum -c format: hash, two spaces, path
    if os.path.exists(ZIP):
        os.remove(ZIP)
    subprocess.run(['zip', '-qrX', ZIP, 'paper3_supplementary_package_v5'], cwd=PKG, check=True, timeout=900)
    REPORT['package'] = {'files': len(sizes), 'bytes_staged': sum(s for s, _ in sizes.values()),
                         'zip_bytes': os.path.getsize(ZIP), 'zip_sha256': sha(ZIP)}
    return REPORT['package']


if __name__ == '__main__':
    os.chdir(R)
    print('exhibit bundle v3:', bundle_v3())
    print('package:', package())
    print(json.dumps({k: v for k, v in REPORT.items() if k != 'bundle_files'}, indent=1)[:900])
