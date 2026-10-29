"""Explicit add-only publication to the author's authorized repository.
Refuses an existing F09 prefix, verifies old file modes/hashes, uses non-force ref
update and downloads every published file for byte verification. No token logging.
Run only with --publish and an authorized token file outside the package.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse, base64, hashlib, json, re
import requests

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'batch 9/agent 2/ecomod_empirical_followup/F09/'
API = 'https://api.github.com/repos/MIKEAA2020/general-sustainability'


def require(value, message):
    if not value:
        raise ValueError(message)


def publish(token_file, receipt):
    match = re.search(r'github_pat_[A-Za-z0-9_]+', token_file.read_text())
    require(match is not None, 'Authorized token not found')
    token = match.group()
    session = requests.Session()
    session.headers.update({'Authorization': 'Bearer ' + token, 'Accept': 'application/vnd.github+json'})

    def api(method, path, **kwargs):
        response = session.request(method, API + path, timeout=120, **kwargs)
        if not response.ok:
            raise RuntimeError('GitHub HTTP ' + str(response.status_code))
        return response.json()

    manifest = json.loads((ROOT / 'artifact_manifest_F09.json').read_text())
    paths = {r['path'] for r in manifest['files']} | {'artifact_manifest_F09.json'}
    actual = {str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file()
              and not any(x in {'.cache', '__pycache__'} for x in p.relative_to(ROOT).parts)}
    require(paths == actual, 'Manifest coverage mismatch')
    for row in manifest['files']:
        require(hashlib.sha256((ROOT / row['path']).read_bytes()).hexdigest() == row['sha256'], 'Artifact changed')
    head = api('GET', '/git/ref/heads/main')['object']['sha']
    tree = api('GET', '/git/commits/' + head)['tree']['sha']
    obj = api('GET', '/git/trees/' + tree, params={'recursive': '1'})
    require(not obj.get('truncated'), 'Old tree truncated')
    old = {r['path']: r for r in obj['tree'] if r['type'] != 'tree'}
    require(not any(k.startswith(PREFIX) for k in old), 'F09 already exists; never overwrite')
    known = {r['sha'] for r in old.values() if r['type'] == 'blob'}
    entries = []
    for rel in sorted(paths):
        data = (ROOT / rel).read_bytes()
        require(token.encode() not in data, 'Credential found in artifact')
        blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
        sha = blob if blob in known else api('POST', '/git/blobs', json={
            'content': base64.b64encode(data).decode(), 'encoding': 'base64'})['sha']
        require(sha == blob, 'Blob mismatch')
        entries.append({'path': PREFIX + rel, 'mode': '100644', 'type': 'blob', 'sha': sha})
    newtree = api('POST', '/git/trees', json={'base_tree': tree, 'tree': entries})['sha']
    obj = api('GET', '/git/trees/' + newtree, params={'recursive': '1'})
    require(not obj.get('truncated'), 'New tree truncated')
    after = {r['path']: r for r in obj['tree'] if r['type'] != 'tree'}
    for path, row in old.items():
        require(after[path]['sha'] == row['sha'] and after[path]['mode'] == row['mode']
                and after[path]['type'] == row['type'], 'Prior content changed')
    require(set(after) - set(old) == {r['path'] for r in entries}, 'Unexpected path changes')
    require(api('GET', '/git/ref/heads/main')['object']['sha'] == head, 'Branch advanced; stop safely')
    commit = api('POST', '/git/commits', json={
        'message': 'Add empirical follow-up F09: integrate page-cited CCI uncertainty and validation evidence; preserve numerical outputs, author controls, eight holds and all prior content',
        'tree': newtree, 'parents': [head]})['sha']
    require(api('GET', '/git/ref/heads/main')['object']['sha'] == head, 'Branch advanced; stop safely')
    api('PATCH', '/git/refs/heads/main', json={'sha': commit, 'force': False})
    require(api('GET', '/git/ref/heads/main')['object']['sha'] == commit, 'Publication head mismatch')

    def check(row):
        raw = base64.b64decode(api('GET', '/git/blobs/' + row['sha'])['content'])
        require(raw == (ROOT / row['path'][len(PREFIX):]).read_bytes(), 'Published byte mismatch')
        return True

    with ThreadPoolExecutor(max_workers=4) as pool:
        verified = sum(pool.map(check, entries))
    result = {'commit': commit, 'parent': head, 'verified_files': verified,
              'prior_paths_modes_hashes_preserved': len(old), 'F08_unchanged': True,
              'new_independent_local_validation': False, 'national_admissions_changed': False,
              'published': True, 'prefix': PREFIX}
    receipt.parent.mkdir(parents=True, exist_ok=True)
    receipt.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--publish', action='store_true')
    parser.add_argument('--token-file', type=Path, required=True)
    parser.add_argument('--receipt', type=Path, default=ROOT.parent / '.cache/cci_companion_R02/publication_receipt_F09.json')
    args = parser.parse_args()
    if not args.publish:
        raise SystemExit('No write requested; supply --publish explicitly')
    publish(args.token_file, args.receipt)


if __name__ == '__main__':
    main()
