#!/usr/bin/env python3
"""Commit additions/renames to a branch of the blob:none no-checkout clone WITHOUT checking out.
Usage: gitpush_index.py <repo> <branch> <message> <plan.json>
plan.json: {"add": [[local_path, repo_path], ...], "rename": [[old_repo_path, new_repo_path], ...], "add_text": [[repo_path, text], ...]}
Safety: refuses if any path would be deleted relative to the tip other than the rename sources."""
import json, subprocess, sys, os
repo, branch, msg, planf = sys.argv[1:5]
plan = json.load(open(planf))
def git(*a, inp=None):
    r = subprocess.run(['git', *a], cwd=repo, input=inp, capture_output=True, text=True)
    if r.returncode: raise SystemExit(f"git {' '.join(a)} failed: {r.stderr}")
    return r.stdout
tip = git('rev-parse', f'origin/{branch}').strip()
git('read-tree', tip)
# renames
for old, new in plan.get('rename', []):
    ls = git('ls-files', '-s', '--', old).strip().splitlines()
    if not ls: raise SystemExit(f"rename source missing: {old}")
    for line in ls:
        meta, path = line.split('\t', 1)
        mode, sha, _ = meta.split()
        newpath = new + path[len(old):] if path != old else new
        git('update-index', '--add', '--cacheinfo', f'{mode},{sha},{newpath}')
        git('update-index', '--force-remove', '--', path)
# additions
def add_blob(repo_path, content_path=None, text=None):
    if text is not None:
        sha = git('hash-object', '-w', '--stdin', inp=text).strip()
    else:
        sha = git('hash-object', '-w', '--', os.path.abspath(content_path)).strip()
    mode = '100755' if (content_path and os.access(content_path, os.X_OK) and content_path.endswith('.sh')) else '100644'
    git('update-index', '--add', '--cacheinfo', f'{mode},{sha},{repo_path}')
for local, rp in plan.get('add', []):
    if os.path.isdir(local):
        for root, _, files in os.walk(local):
            for f in sorted(files):
                lp = os.path.join(root, f); rel = os.path.relpath(lp, local)
                add_blob(rp.rstrip('/') + '/' + rel, content_path=lp)
    else:
        add_blob(rp, content_path=local)
for rp, text in plan.get('add_text', []):
    add_blob(rp, text=text)
# safety: deletions relative to tip must be exactly the rename sources
dels = git('diff', '--cached', '--name-only', '--diff-filter=D', tip).strip().splitlines()
allowed = set()
for old, new in plan.get('rename', []):
    for line in subprocess.run(['git','ls-tree','-r','--name-only',tip,'--',old],cwd=repo,capture_output=True,text=True).stdout.strip().splitlines():
        allowed.add(line)
bad = [d for d in dels if d not in allowed]
if bad: raise SystemExit(f"unexpected deletions: {bad[:10]}")
tree = git('write-tree').strip()
commit = git('commit-tree', tree, '-p', tip, '-m', msg).strip()
git('update-ref', f'refs/heads/{branch}', commit)
print(git('diff', '--no-renames', '--shortstat', '--cached', tip).strip())
print('renamed', len(allowed), 'files;', 'commit', commit[:7], 'on', branch)
