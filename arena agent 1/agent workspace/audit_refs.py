"""Audit every external reference in every paper .tex against the full repo tree.

Classifies each unresolved reference as
  MISSING      - no file of that basename exists anywhere in the repository
  MISRESOLVED  - the file exists, but not on the paper's reference path
"""
import json, os, re, glob, urllib.request, collections, sys

TOK = re.search(r"github_pat_[A-Za-z0-9_]+",
                open('/home/user/uploads/github_pat.txt').read()).group(0)
OWNER, REPO, BR = "MIKEAA2020", "general-sustainability", "lean-audit-v4"
H = {"Authorization": "Bearer " + TOK, "Accept": "application/vnd.github+json"}

CACHE = "/home/user/repo_paths.json"
if os.path.exists(CACHE):
    paths = json.load(open(CACHE))
else:
    d = json.load(urllib.request.urlopen(urllib.request.Request(
        f"https://api.github.com/repos/{OWNER}/{REPO}/git/trees/{BR}?recursive=1", headers=H)))
    paths = [t["path"] for t in d["tree"] if t["type"] == "blob"]
    json.dump(paths, open(CACHE, "w"))
PATHSET = set(paths)
BY_BASENAME = collections.defaultdict(list)
for p in paths:
    BY_BASENAME[p.rsplit('/', 1)[-1]].append(p)

LATEX = "arena agent 1/paper rewrites/latex"
texs = sorted(glob.glob(os.path.join("/home/user/repo", LATEX, "*.tex")))

def resolve(base, ref):
    cands = [ref.lstrip('/')] if ref.startswith('/') else []
    cands += [os.path.normpath(os.path.join(base, ref))]
    for extra in (LATEX, "arena agent 1/paper rewrites", "arena agent 1"):
        cands.append(os.path.normpath(os.path.join(extra, ref)))
    for c in cands:
        if c in PATHSET:
            return c
    return None

missing, misresolved = collections.defaultdict(set), collections.defaultdict(set)
nrefs = 0
for t in texs:
    rel = os.path.relpath(t, "/home/user/repo")
    base = os.path.dirname(rel)
    src = open(t, encoding='utf-8', errors='replace').read()
    refs = set(m.group(1).strip()
               for m in re.finditer(r"\\(?:includegraphics|input|include)\s*(?:\[[^\]]*\])?\s*\{([^}]+)\}", src))
    for r in refs:
        nrefs += 1
        if resolve(base, r) is not None:
            continue
        bn = r.rsplit('/', 1)[-1]
        if BY_BASENAME.get(bn):
            misresolved[os.path.basename(t)].add((r, BY_BASENAME[bn][0]))
        else:
            missing[os.path.basename(t)].add(r)

print(f"papers scanned: {len(texs)}")
print(f"includegraphics/input/include refs resolved against {len(PATHSET)} repo blobs: {nrefs}")
print()
print(f"### TRULY MISSING (no file of that name anywhere): {sum(len(v) for v in missing.values())}")
for k in sorted(missing):
    for r in sorted(missing[k]):
        print(f"   {k}: {r}")
if not missing:
    print("   (none)")
print()
print(f"### MISRESOLVED (file exists elsewhere in the repo): {sum(len(v) for v in misresolved.values())}")
for k in sorted(misresolved):
    for r, found in sorted(misresolved[k]):
        print(f"   {k}")
        print(f"       references: {r}")
        print(f"       found at  : {found}")
if not misresolved:
    print("   (none)")
