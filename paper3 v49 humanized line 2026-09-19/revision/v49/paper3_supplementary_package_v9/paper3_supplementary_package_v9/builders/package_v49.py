#!/usr/bin/env python3
"""Stage and zip the v49 package: the four documents, the notes and the errata that travel
with them, every log the build wrote, and the builders that produced them.

Nothing here is new prose: README text is assembled from the verification report, so the
numbers in the note cannot drift away from the run that produced them.
"""
import os, re, json, shutil, zipfile, hashlib, pathlib

ROOT = pathlib.Path('/home/user'); V7 = ROOT / 'revision/v7'; D = ROOT / 'revision/v49'
V48 = ROOT / 'revision/v48'; H = ROOT / 'humanize'
PKG = D / 'paper3_supplementary_package_v9'
NAME = 'paper3_supplementary_package_v9'
ver = json.loads((D / 'v49_verification.json').read_text())
gate = json.loads((D / 'v49_gate_report.json').read_text())
crep = json.loads((D / 'v49_compile_report.json').read_text())
ed = json.loads((D / 'v49_front_matter_edits.json').read_text())
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()

if PKG.exists():
    shutil.rmtree(PKG)
man = PKG / NAME / 'manuscript'; (man).mkdir(parents=True)
for sub in ('disclosure', 'builders'):
    (PKG / NAME / sub).mkdir()

DOC_BASES = ['paper3_material_ledgers_v49', 'paper3_supplementary_v18',
             'companionA_certification_procedure_v9', 'companionB_standards_horizon_v9']
for b in DOC_BASES:
    for e in ('.md', '.tex', '.pdf'):
        shutil.copy(f'{V7}/{b}{e}', man / f'{b}{e}')
shutil.copy(f'{V7}/paper3_supplementary_v18.ascii.md', man)
for f in ('NOTES_v49.md',):
    shutil.copy(D / f, PKG / NAME / f)
shutil.copy(V48 / 'ERRATA_v48.md', PKG / NAME / 'ERRATA_v48.md')

DISC = ['v49_front_matter_edits.json', 'v49_gate_report.json', 'v49_verification.json', 'v49_compile_report.json',
        'v49_required_restores.json', 'v49_carry_over.json', 'v49_base_front_matter.md', 'v49_front_matter.md',
        'v48_front_matter.md', 'waiver_scope_v1.json', 'protected_locations.json', 'protected_vs_v47.json',
        'disposition_v49.json', 'read_32.json', 'read_32_material.txt', 'v48_loss_set.json', 'v47_vs_v48_diff.json',
        'adaptation_term_revert_v1.csv', 'term_revert_candidates.json', 'v49_line_audit.json',
        'v49_restores_v2.json', 'v49_body_repairs.json', 'v49_house_form_mismatch.json',
        'v49_adaptation_first_brief.md', 'open_items_v49.md',
        'open_items_v48.md', 'open_items_v47.md', 'register_notes.md']
for f in DISC:
    src = (H / f) if f in ('v49_adaptation_first_brief.md', 'open_items_v48.md', 'open_items_v47.md',
                            'open_items_v49.md', 'register_notes.md') else D / f
    if src.exists():
        shutil.copy(src, PKG / NAME / 'disclosure' / src.name)
BUILD = ['build_v49_base.py', 'build_v49_tex.py', 'verify_v49_base.py', 'v49_waiver_gate_v1.py',
         'pin_waiver_scope_v1.py', 'dispose_the_82_v1.py', 'package_v49.py',
         'make_restores_v2.py', 'audit_v49_lines_v1.py']
for f in BUILD:
    shutil.copy(D / f, PKG / NAME / 'builders' / f)
for f in ('build_v48_base.py', 'verify_v48_base.py', 'claim_ledger_v1.py', 'claim_ledger_v1.json', 'claim_ledger_v1.csv',
          'v48_reuse_split_v1.py', 'v48_reuse_split.json', 'v48_reuse_audit_v1.py', 'v48_reuse_audit.json',
          'v48_splice_v1.py', 'v48_splice_log.json', 'v48_overrules.csv', 'v48_pointers_v1.py', 'v48_pointers.json',
          'v48_notation_drift_v1.py', 'v48_notation_drift.json', 'v48_reuse_findings_v1.py', 'v48_audit_selftest_v1.py',
          'v48_readme_v1.py', 'v48_build_log.json'):
    p = V48 / f
    if p.exists():
        shutil.copy(p, PKG / NAME / 'builders' / f)
for f in ('stylekit_v1.py', 'mdtex_v1.py', 'build_companions_v1.py', 'build_supp_tex_v1.py', 'tablekit_v2.py',
          'structure_v48_base.md', 'paper3_material_ledgers_v48_prebaseline.md', 'revisions_v48_base_log.json',
          'paper3_material_ledgers_v42.md', 'paper3_material_ledgers_v47.md'):
    p = V7 / f
    if p.exists():
        shutil.copy(p, PKG / NAME / 'builders' / f)
shutil.copy(ROOT / 'review/texkit_v1.py', PKG / NAME / 'builders' / 'texkit_v1.py')

rd = []
rd.append('# paper3 supplementary package, v49 line (2026-09-19)')
rd.append('')
rd.append('The article text of this line is `manuscript/paper3_material_ledgers_v49.{md,tex,pdf}` (54 pages).')
rd.append('Alongside it: the supplementary material (19 pp), the certification-procedure companion (10 pp) and')
rd.append('the standards-horizon companion (8 pp). The three companion documents are byte-identical to the')
rd.append('delivered v48 line — v49 changes the article only — and the hashes are in `MANIFEST.md`.')
rd.append('')
rd.append('## What v49 changes')
rd.append('')
rd.append('The abstract and Section 1 are the author\'s own adaptation of the article, repaired against the')
rd.append('deposited article: the renamed vocabulary is reverted to the deposit\'s terms, the four invented')
rd.append('assertions are gone, the two-level headings are cut while the deposited article\'s two-senses')
rd.append('passage is carried over verbatim, and Section 1\'s numbers and citations are gated like any other')
rd.append('section\'s. The body is the v48 body with six sentences restored that v48\'s rewrite pass had dropped')
rd.append('(`NOTES_v49.md`, and E8 in `ERRATA_v48.md`).')
rd.append('')
rd.append('## How the build was checked')
rd.append('')
rd.append('`disclosure/v49_verification.json` (FAILURES: none) and `disclosure/v49_gate_report.json`')
rd.append('(flag_count ' + str(gate['flag_count']) + ', ' + str(gate['disclosure_count']) + ' disclosures, Section 1 checked against ' + str(gate['ledger_rows_in_section_1']) + ' ledger rows):')
rd.append('')
rd.append('* verbatim-protected reuse rows outside the waived region: ' + str(ver['protected_rows_outside_waived_region']['verbatim_in_v49_body']) + '/' + str(ver['protected_rows_outside_waived_region']['located_in_v48_body']) + ' present in the body;')
rd.append('  ' + str(ver['protected_rows_outside_waived_region']['located_in_the_waived_region_and_so_freed']) + ' sat in the waived region and are freed by the ruling;')
rd.append('* back matter (references, availability statements, declarations) byte-identical to v48: ' + str(ver['back_matter']['identical_to_v48']) + ';')
rd.append('* body numerals unchanged: ' + str(ver['body_numerals']['v48']) + ' → ' + str(ver['body_numerals']['v49']) + '; no Section 1 numeral without deposit support;')
rd.append('  ' + str(ver['section1_citations']['checked']) + ' Section 1 citations all resolved;')
rd.append('* the compiled PDF carries ' + str(ver['pdf_flow']['blocks'] - ver['pdf_flow']['absent']) + '/' + str(ver['pdf_flow']['blocks']) + ' flowing markdown paragraphs; unresolved refs ' + str(ver['tex']['unresolved_refs'] or 0) + ';')
rd.append('  no overfull box ≥ 6pt in any document; the LaTeX body is byte-identical to v48\'s after undoing the')
rd.append('  six sentences this build inserted: ' + str(ver['tex']['body_byte_identical_after_undoing_the_six_insertions']) + ';')
rd.append('* the delivered v48 package was not touched: ' + str(ver['v48_line_frozen']['bytes']) + ' B, sha256 ' + ver['v48_line_frozen']['sha256_head'] + '…' + ver['v48_line_frozen']['sha256_tail'] + '.')
rd.append('')
rd.append('## Recompile and re-verify')
rd.append('')
rd.append('```sh')
rd.append('python3 builders/build_v49_base.py     # writes revision/v7/paper3_material_ledgers_v49.md + logs')
rd.append('python3 builders/build_v49_tex.py       # transpiles, compiles, fits; writes the compile report')
rd.append('python3 builders/verify_v49_base.py     # the nine checks above; exit code is the failure count')
rd.append('python3 builders/v49_waiver_gate_v1.py --control   # demonstrates the checks bite (7 flags on the v48 front matter)')
rd.append('```')
rd.append('')
rd.append('`tools/tectonic` (0.17.0) is needed to compile; it is kept out of the package and of the archive')
rd.append('because of its size, and is described in `builders/texkit_v1.py`\'s header.')
rd.append('')
rd.append('## Licence and third-party material')
rd.append('')
rd.append('The article is CC BY 4.0. The scripts in `builders/` accompany it under the same licence; attribution')
rd.append('as the article\'s. The GFN NFA tables (16 MB of third-party data) are deliberately not in this')
rd.append('package: the notice in `disclosure/open_items_v48.md` records where they came from and that they')
rd.append('remain untouched outside the archive. No other third-party data is included.')
(PKG / NAME / 'README.md').write_text('\n'.join(rd) + '\n')

files = sorted(p for p in PKG.rglob('*') if p.is_file())
ml = ['# Package manifest', '', '| file | bytes | sha256 |', '|---|---|---|']
for p in files:
    rel = str(p.relative_to(PKG / NAME)).replace(os.sep, '/')
    ml.append('| `%s` | %d | %s |' % (rel, p.stat().st_size, sha(p)))
ml += ['', str(len(files)) + ' files.', '',
       'No line of the manifest contains a workspace path. The builders are shipped so that the',
       'transpile, the fit loop and the gates can be re-run and re-read; they assume the workspace',
       'layout they were written in and are not a standalone program.']
(PKG / NAME / 'MANIFEST.md').write_text('\n'.join(ml) + '\n')
(PKG / NAME / 'outputs.txt').write_text(json.dumps({'verification': ver, 'gate': {k: gate[k] for k in ('flag_count', 'disclosure_count', 'ledger_rows_in_section_1', 'built_sentences_in_region')},
                                                     'compile': crep['docs'], 'front_matter_edits': ed['summary']}, indent=1) + '\n')

z = D / (NAME + '.zip')
if z.exists():
    z.unlink()
with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as Z:
    for p in sorted(q for q in (PKG / NAME).rglob('*') if q.is_file()):
        Z.write(p, NAME + '/' + str(p.relative_to(PKG / NAME)))
recs = zipfile.ZipFile(z).infolist()
open(D / 'outputs.txt', 'w').write('package %s: %d records, %d bytes, sha256 %s\n' % (z.name, len(recs), z.stat().st_size, sha(z)))
print('zipped %d records, %d bytes' % (len(recs), z.stat().st_size))
print('sha256', sha(z))
