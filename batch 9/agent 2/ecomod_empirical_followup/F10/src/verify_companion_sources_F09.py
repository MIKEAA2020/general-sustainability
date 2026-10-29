"""Verify pinned companion PDFs in excluded cache; download only with --download.
No full PDF, page image or extracted page text is written to the publication package.
This verifies source identity, NOT the provider implementation or ecological results.
"""
from pathlib import Path
import argparse, hashlib, json
import requests
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
CAP = 25_000_000


def acquire(row, directory):
    size = row['bytes']
    if not 0 < size <= CAP:
        raise ValueError('Document exceeds frozen transfer guard')
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / (row['key'] + '.pdf')
    tmp = target.with_suffix('.part')
    count = 0
    digest = hashlib.sha256()
    try:
        with requests.get(row['final_url'], headers={
            'If-Match': row['etag'], 'Accept-Encoding': 'identity'
        }, stream=True, timeout=(20, 90)) as response:
            if response.status_code != 200 or response.headers.get('ETag') != row['etag']:
                raise ValueError('Pinned source identity mismatch')
            with tmp.open('wb') as stream:
                for chunk in response.iter_content(262144):
                    count += len(chunk)
                    if count > min(size, CAP):
                        raise ValueError('Transfer guard exceeded')
                    digest.update(chunk)
                    stream.write(chunk)
        if count != size or digest.hexdigest() != row['sha256']:
            raise ValueError('Source length/hash mismatch')
        tmp.replace(target)
    finally:
        if tmp.exists():
            tmp.unlink()
    return target


def verify_local(row, directory):
    path = directory / (row['key'] + '.pdf')
    if not path.exists():
        raise FileNotFoundError('Pinned PDF not cached; use --download explicitly')
    if path.stat().st_size != row['bytes'] or row['bytes'] > CAP:
        raise ValueError('Cached source size mismatch')
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(262144), b''):
            digest.update(chunk)
    if digest.hexdigest() != row['sha256']:
        raise ValueError('Cached source hash mismatch')
    pages = len(PdfReader(path).pages)
    if pages != row['pages']:
        raise ValueError('Source page count mismatch')
    return {'key': row['key'], 'bytes': row['bytes'], 'sha256': row['sha256'],
            'pages': pages, 'full_body_identity_verified': True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache', type=Path, default=ROOT.parent / '.cache/cci_companion_R02')
    parser.add_argument('--download', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    registry = json.loads((ROOT / 'metadata/companion_review_F09/source_registry_F09.json').read_text())
    results = []
    for row in registry['documents']:
        if args.download and not (args.cache / (row['key'] + '.pdf')).exists():
            acquire(row, args.cache)
        results.append(verify_local(row, args.cache))
    result = {'documents': results, 'source_identity_only': True,
              'provider_code_verified': False, 'ecological_validation_established': False}
    content = json.dumps(result, indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content)
    else:
        print(content)


if __name__ == '__main__':
    main()
