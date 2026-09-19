#!/usr/bin/env python3
"""Push the v49 line to the archive branch as an incremental commit.

Same orphan archive branch as the v48 line (never main), folder `paper3 v49 humanized line 2026-09-19/`,
and the tree is built on base_tree so the earlier v48 files - including the archived-only tectonic binary -
are kept. The token is read from uploads/ and never echoed.
"""
import base64, hashlib, json, os, pathlib, urllib.request, urllib.error

ROOT = pathlib.Path('/home/user')
TOK = (ROOT / 'uploads/github_pat.txt').read_text().strip()
API = 'https://api.github.com/repos/MIKEAA2020/general-sustainability'
BR = 'archive/paper3-v48-workspace'
FOLDER = 'paper3 v49 humanized line 2026-09-19'

def req(method, path, body=None, tries=3):
    for k in range(tries):
        r = urllib.request.Request(API + path, method=method,
                                   data=json.dumps(body).encode() if body is not None else None,
                                   headers={'Authorization': 'token ' + TOK, 'Accept': 'application/vnd.github+json',
                                            'Content-Type': 'application/json',
                                            'X-GitHub-Api-Version': '2022-11-28'})
        try:
            with urllib.request.urlopen(r, timeout=180) as f:
                return json.loads(f.read().decode() or '{}')
        except urllib.error.HTTPError as e:
            msg = e.read().decode()[:300]
            if e.code in (403, 429) and k < tries - 1:
                import time; time.sleep(20); continue
            raise RuntimeError('%s %s -> %s %s' % (method, path, e.code, msg))

files = []
def add(rel):
    p = ROOT / rel
    if p.exists() and p.is_file():
        files.append((FOLDER + '/' + rel, p))
for d in sorted((ROOT / 'revision/v49').rglob('*')):
    if d.is_file() and '__pycache__' not in str(d):
        add(str(d.relative_to(ROOT)))
# the four shipped documents travel together: the article is *_v49.*, but the supplementary and the two
# companions recompile with it (the 4-document compile rewrites all four PDFs), so archiving only the
# article left the other three PDFs at whatever bytes an earlier round pushed. Every document the zip
# contains is now pushed loose too, or the archive cannot be used to re-derive the zip.
for pat in ('*_v49.*', '*_v18.*', 'companionA_*_v9.*', 'companionB_*_v9.*'):
    for f in sorted((ROOT / 'revision/v7').glob(pat)):
        if f.suffix in ('.md', '.tex', '.pdf'):
            add('revision/v7/' + f.name)
for f in ('revision/v48/ERRATA_v48.md', 'humanize/v49_adaptation_first_brief.md', 'humanize/open_items_v48.md'):
    add(f)
print(len(files), 'files to push;', round(sum(p.stat().st_size for _, p in files) / 1e6, 1), 'MB')

ref = req('GET', '/git/ref/heads/' + BR)
head = ref['object']['sha']
print('branch head', head[:12])
tree = req('GET', '/git/trees/' + head + '?recursive=1')['tree']
print('existing tree entries', len(tree))
new = []
for path, p in files:
    blob = req('POST', '/git/blobs', {'content': base64.b64encode(p.read_bytes()).decode(), 'encoding': 'base64'})
    new.append({'path': path, 'mode': '100644', 'type': 'blob', 'sha': blob['sha']})
print('blobs created', len(new))
t = req('POST', '/git/trees', {'base_tree': head, 'tree': new})
sizes = sum(p.stat().st_size for _, p in files)
c = req('POST', '/git/commits', {'parents': [head], 'tree': t['sha'],
                                 'message': 'v49 line (2026-09-19): adaptation base for the front matter and Section 1, '
                                            'six lost body sentences restored, E1-E9 closed; waiver gate 0 flags, verifier clean. '
                                            'v48 bytes untouched. %d files, %d B.' % (len(new), sizes)})
req('PATCH', '/git/refs/heads/' + BR, {'sha': c['sha'], 'force': True})
print('branch moved to', c['sha'][:12])
back = req('GET', '/git/ref/heads/' + BR)['object']['sha']
assert back == c['sha'], back
tv = req('GET', '/git/trees/' + c['sha'] + '?recursive=1')['tree']
mine = [e for e in tv if e['path'].startswith(FOLDER)]
print('verified: tree now', len(tv), 'entries,', len(mine), 'under the v49 folder')
# a filename match proves the name is in the tree, not that the bytes are the ones just shipped, and
# this line has been read as a freshness proof before. Compare the git blob SHA-1 instead.
zs = sorted((ROOT / 'revision/v49').glob('paper3_supplementary_package_v*.zip'))
z = zs[-1]
raw = z.read_bytes()
blob = hashlib.sha1(b'blob %d\x00' % len(raw) + raw).hexdigest()
ent = [e for e in mine if e['path'].endswith(z.name)]
print(f'{z.name} in archive with identical bytes:', bool(ent) and ent[0]['sha'] == blob,
      '| git blob', blob[:12] + '…', '| local sha256', hashlib.sha256(raw).hexdigest()[:12] + '…')
