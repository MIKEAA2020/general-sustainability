"""F09 preservation/PDF checks and manifest. --write records current checks.
Default mode verifies the published artifact manifest without downloads/builds.
This is technical QA, not validation of ecological estimates.
"""
from pathlib import Path
import argparse, csv, hashlib, json, re
from pypdf import PdfReader
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {'.cache', '__pycache__'}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def files():
    return sorted(p for p in ROOT.rglob('*') if p.is_file()
                  and not any(x in EXCLUDED for x in p.relative_to(ROOT).parts)
                  and p.name != 'artifact_manifest_F09.json')


def require(value, message):
    if not value:
        raise ValueError(message)


def verify_manifest():
    manifest = json.loads((ROOT / 'artifact_manifest_F09.json').read_text())
    paths = {str(p.relative_to(ROOT)) for p in files()}
    require(paths == {r['path'] for r in manifest['files']}, 'Manifest coverage mismatch')
    for row in manifest['files']:
        p = ROOT / row['path']
        require(p.stat().st_size == row['bytes'] and digest(p) == row['sha256'],
                'Artifact identity mismatch: ' + row['path'])
    return len(paths)


def record_checks():
    baseline = ROOT.parent / 'ecomod_followup_F08'
    require(baseline.exists(), 'Original F08 required for write-mode preservation check')
    base = json.loads((baseline / 'artifact_manifest.json').read_text())
    for row in base['files']:
        require(digest(baseline / row['path']) == row['sha256'], 'Original F08 changed')
    inherited = json.loads((ROOT / 'metadata/inherited_unchanged_files_F09.json').read_text())
    for rel, sha in inherited.items():
        require(digest(ROOT / rel) == sha, 'Inherited file changed: ' + rel)
    original_data = [p for p in (baseline / 'data').rglob('*') if p.is_file()]
    for p in original_data:
        require(p.read_bytes() == (ROOT / 'data' / p.relative_to(baseline / 'data')).read_bytes(),
                'Original numerical data changed')
    with (ROOT / 'data/support/physical_admission_F08.csv').open() as stream:
        admissions = list(csv.DictReader(stream))
    require(len(admissions) == 8 and all(r['admission'] == 'hold_not_admitted' for r in admissions), 'Admission changed')
    test_results = {}
    for name in ['tests_F09_all.txt', 'tests_F09_optimized.txt']:
        text = (ROOT / 'metadata' / name).read_text()
        count = int(re.search(r'Ran (\d+) tests', text).group(1))
        require(count == 122 and text.rstrip().endswith('OK'), 'Test failure/missing log')
        test_results[name] = {'passed': count, 'sha256': digest(ROOT / 'metadata' / name)}
    pdfs = {}
    words = json.loads((ROOT / 'configs/study_design.json').read_text())['keywords']
    for part in ['main', 'SI']:
        name = 'followup_F09_' + part
        pdf = ROOT / (name + '.pdf')
        reader = PdfReader(pdf)
        require(len(reader.pages) == 11, 'Unexpected manuscript pagination')
        require(reader.metadata['/Keywords'] == '; '.join(words), 'PDF keywords differ')
        urls = []
        for page in reader.pages:
            for item in page.get('/Annots', []):
                annotation = item.get_object()
                action = annotation.get('/A')
                if action and action.get('/URI'):
                    urls.append(str(action['/URI']))
        require('https://orcid.org/0000-0002-0019-1842' in urls, 'Missing ORCID hyperlink')
        require(any('/ecomod_empirical_followup/F09' in u for u in urls), 'Stale package hyperlink')
        log = (ROOT / '.cache/tex' / (name + '.log')).read_text()
        warnings = [line for line in log.splitlines() if any(s in line for s in ['Overfull', 'Underfull', 'Warning', 'undefined'])]
        require(not warnings, 'LaTeX layout/reference warning')
        doc = pymupdf.open(pdf)
        outside = []
        for number, page in enumerate(doc, 1):
            require('??' not in page.get_text(), 'Unresolved PDF reference')
            for block in page.get_text('dict')['blocks']:
                for line in block.get('lines', []):
                    for span in line['spans']:
                        r = pymupdf.Rect(span['bbox'])
                        if r.x0 < -1 or r.y0 < -1 or r.x1 > page.rect.width + 1 or r.y1 > page.rect.height + 1:
                            outside.append(number)
        require(not outside, 'Text outside PDF page')
        pdfs[part] = {'pages': len(reader.pages), 'sha256': digest(pdf), 'orcid_hyperlink_verified': True,
                      'seven_keywords_verified': True, 'current_package_link_verified': True,
                      'latex_warnings': warnings, 'text_outside_page': outside}
    declaration = r'\href{http://Arena.ai}{Arena.ai} Agent Mode was used to assist with computational methods and literature review.'
    require(declaration in (ROOT / 'followup_F09_main.tex').read_text(), 'Approved declaration differs')
    source_check = json.loads((ROOT / 'metadata/companion_review_F09/source_identity_verification_F09.json').read_text())
    require(len(source_check['documents']) == 4 and all(x['full_body_identity_verified'] for x in source_check['documents']), 'Source identity check absent')
    result = {'revision': 'F09', 'date': '2026-10-29',
              'original_F08_manifest_records_unchanged': len(base['files']),
              'original_F08_manifest_sha256': digest(baseline / 'artifact_manifest.json'),
              'inherited_byte_identical_files': len(inherited), 'original_data_files_unchanged': len(original_data),
              'admissions_hold': 8, 'tests': test_results, 'pdfs': pdfs,
              'manual_visual_inspection_pdf_pages': {'main': [1, 2, 6, 8, 9, 10, 11], 'SI': [3, 7, 11]},
              'provider_stock_table_rows_visually_cross_checked': 16,
              'source_identity_verified_documents': 4, 'source_pdf_text_images_redistributed': False,
              'ecological_validation_established_by_technical_checks': False,
              'new_paired_reference_or_local_covariance': False, 'national_admission_changed': False,
              'previous_packages_deleted': False}
    (ROOT / 'metadata/verification_F09.json').write_text(json.dumps(result, indent=2) + '\n')
    manifest = {'revision': 'F09', 'self_excluded': True, 'excluded_directories': sorted(EXCLUDED),
                'files': [{'path': str(p.relative_to(ROOT)), 'bytes': p.stat().st_size, 'sha256': digest(p)} for p in files()]}
    (ROOT / 'artifact_manifest_F09.json').write_text(json.dumps(manifest, indent=2) + '\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    if args.write:
        record_checks()
    print(json.dumps({'manifest_verified_files': verify_manifest(), 'technical_QA_not_ecological_validation': True}))


if __name__ == '__main__':
    main()
