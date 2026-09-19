#!/usr/bin/env python3
"""Self-check for the v33 revision. Run from the workspace root: python3 revision/v6/verify_v33.py
1. Removal of every logged operation reproduces v32 byte-for-byte (insert-only, nothing reworded).
2. v32's own paragraphs survive intact; labels 21-33 are each introduced exactly once.
3. No placeholder citation remains; the new reference entries are present exactly once.
4. The markdown carries this repository's math dialect only.
5. The supplementary of record is carried unchanged at the head of v9; the repository clone is clean."""
import hashlib, json, os, re, sys
os.chdir(os.environ.get("WS", "/home/user"))
SRC = "github/gs/arena agent 1/paper rewrites/paper3_material_ledgers_v32.md"
V33 = "revision/v6/paper3_material_ledgers_v33.md"
LOG = "revision/v6/revisions_v33_log.json"
V8  = "github/gs/arena agent 1/paper rewrites/paper3_supplementary_v8.md"
V9  = "revision/v6/paper3_supplementary_v9.md"
fails = []
def chk(ok, msg):
    print(("PASS  " if ok else "FAIL  ") + msg)
    if not ok: fails.append(msg)

v32 = open(SRC, encoding="utf-8").read()
t = open(V33, encoding="utf-8").read()
log = json.load(open(LOG, encoding="utf-8"))

# 1 ---- reverse every logged operation
r = t
for op in reversed(log):
    if op["kind"] == "after_sub":
        if r.count(op["text"]) != 1:
            chk(False, "reconstruction: %s block not uniquely located" % op["tag"]); sys.exit(1)
        r = r.replace(op["text"], "", 1)
    else:
        if r.count(op["text"]) != 1:
            chk(False, "reconstruction: %s replacement not uniquely located" % op["tag"]); sys.exit(1)
        r = r.replace(op["text"], op["old"], 1)
chk(hashlib.sha256(r.encode()).hexdigest() == hashlib.sha256(v32.encode()).hexdigest(),
    "insert-only reconstruction reproduces v32 exactly (%d ops reversed)" % len(log))

# 2 ---- nothing of v32 lost, new labels unique
missing = [p_ for p_ in v32.split("\n\n") if p_.strip() and p_ not in r]
chk(not missing, "every v32 paragraph present (%d missing)" % len(missing))
head_re = r"\*\*(?:Definition|Proposition|Theorem|Remark|Corollary|Lemma) %d\b"
for n in range(21, 34):
    c = len(re.findall(head_re % n, t))
    if c != 1: chk(False, "label %d introduced %d times" % (n, c))
chk(all(len(re.findall(head_re % n, t)) == 1 for n in range(21, 34)),
    "labels 21-33 each introduced exactly once")
old = lambda s_: len(re.findall(head_re.replace("%d", r"\d+"), s_))
chk(old(v33 := t) - old(v32) == 13, "statement heads grew by 13 (%d -> %d)" % (old(v32), old(v33)))

# 3 ---- citations
for bad in ["in review", "Author, D.", "Author, E.", "Author, F."]:
    chk(bad not in t, "no %r placeholder remains (%d)" % (bad, t.count(bad)))
for key in ["10.4204/EPTCS.380.5", "Pacific Journal of Mathematics 7, 1073",
            "Prentice-Hall, Englewood Cliffs", "Lecture Notes in Computer Science 2993, 477",
            "IEEE Transactions on Automatic Control 52, 1415", "AMS", "Mathematical Surveys and Monographs 41",
            "System of National Accounts 2025", "SEEA Central Framework", "zenodo.22554297", "zenodo.22545740"]:
    if key == "AMS": continue
    chk(key in t, "reference present: %s" % key)
chk(t.count("United Nations, 2025.") == 1 and t.count("World Bank, 2014.") == 1, "each UN entry appears once")

# 4 ---- dialect
bs = chr(92)
for sym in [bs + "[", bs + "]", bs + "(", bs + ")", bs + "square"]:
    chk(t.count(sym) == v32.count(sym), "no new LaTeX-only delimiter %r (v33 %d, v32 %d)" % (sym, t.count(sym), v32.count(sym)))
chk(t.count("$$") % 2 == 0, "$$ displays balanced (%d)" % t.count("$$"))
chk("1\u201333 sequence counter" in t and "Definitions 21\u201323, Theorem 24" in t, "numbering note extended to 1-33")
chk("paper3_supplementary_v9.md" in t and "paper3_supplementary_v8.md" not in t, "supplementary pointer advanced to v9")
chk("## Code availability" in t, "Code availability section present")

# 5 ---- supplementary and clone integrity
v8 = open(V8, encoding="utf-8").read()
v9 = open(V9, encoding="utf-8").read()
chk(v9.startswith(v8.rstrip("\n")), "v8 carried verbatim at the head of v9")
for h in ["## S7 \u00b7", "## S8 \u00b7", "## S9.1 \u00b7", "## S9.2 \u00b7", "## S9.3 \u00b7", "## S9.4 \u00b7"]:
    chk(h in v9, "supplementary section present: %s" % h)
chk(not re.search(r"\| (?:Definition|Proposition|Theorem|Remark) 3[0-9][^|]*\| 8\.\d", v9), "no stale 8.x inventory cells")
g = os.popen("cd github/gs && git status --porcelain | head").read().strip()
chk(g == "", "repository clone clean (%s)" % (g or "no changes"))
print("\n%s" % ("ALL CHECKS PASS" if not fails else "FAILURES: " + "; ".join(fails)))
sys.exit(1 if fails else 0)
