#!/usr/bin/env python3
# Deep normalized content-integrity scan: every earlier paper2 version vs v27.
# Axes: prose sentences, math blocks, citations, labels, headings, captions,
#       theorem/proposition/... statement bodies.
import re, os, json, sys

LATEX = "/home/user/arena agent 1/paper rewrites/latex"
NEW = f"{LATEX}/paper2_obstruction_calculus_v27.tex"

def read(p):
    return open(p, encoding="utf-8").read()

def strip_comments(t):
    return re.sub(r"(?m)^%.*$", "", t)

def mask_math(t):
    # environments -> MATHT
    for env in ["equation*?","align\\*?","gather\\*?","eqnarray\\*?","multline\\*?","split","cases","aligned"]:
        t = re.sub(r"\\begin\{"+env+r"\}.*?\\end\{"+env+r"\}", " MATHT ", t, flags=re.S)
    t = re.sub(r"\\\[.*?\\\]", " MATHT ", t, flags=re.S)
    t = re.sub(r"\\\(.*?\\\)", " MATHT ", t, flags=re.S)
    t = re.sub(r"\$\$.*?\$\$", " MATHT ", t, flags=re.S)
    t = re.sub(r"\$[^$]*\$", " MATHT ", t)
    return t

def unwrap_style(t):
    for cmd in ["emph","textbf","textit","textrm","mathrm","text","texttt","mbox","underline"]:
        t = re.sub(r"\\"+cmd+r"\{([^{}]*)\}", r"\1", t)
    return t

def strip_cmds(t):
    t = re.sub(r"\\[a-zA-Z]+\\?[ \t]*(\[[^\]\n]*\])?", " ", t)
    t = t.replace("{"," ").replace("}"," ")
    return t

def norm(t):
    t = t.lower()
    t = re.sub(r"[^a-z0-9]+", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t

def sentences(t):
    t = strip_comments(t)
    t = mask_math(t)
    t = unwrap_style(t)
    t = strip_cmds(t)
    t = re.sub(r"\s+", " ", t)
    out = []
    for p in re.split(r"(?<=[.;:])\s+", t):
        n = norm(p)
        if len(n.split()) >= 8:
            out.append(n)
    return out

def math_blocks(t):
    t = strip_comments(t)
    out = []
    for env in ["equation\\*?","align\\*?","gather\\*?","eqnarray\\*?","multline\\*?"]:
        for m in re.findall(r"\\begin\{"+env+r"\}(.*?)\\end\{"+env+r"\}", t, flags=re.S):
            b = re.sub(r"\\label\{[^}]*\}","",m)
            b = re.sub(r"\\tag\{[^}]*\}","",b)
            b = re.sub(r"\s+"," ",b).strip()
            if len(b) >= 10:
                out.append(b)
    for m in re.findall(r"\\\[(.*?)\\\]", t, flags=re.S):
        b = re.sub(r"\s+"," ",m).strip()
        if len(b) >= 10:
            out.append(b)
    return out

def citations(t):
    return sorted(set(re.findall(r"\\cite[a-z]*\{([^}]*)\}", t)))

def labels(t):
    return sorted(set(re.findall(r"\\label\{([^}]*)\}", t)))

def headings(t):
    t = strip_comments(t)
    return sorted(set(re.findall(r"\\subsubsection\{([^}]*)\}", t)))

def captions(t):
    t = strip_comments(t)
    return [norm(x) for x in re.findall(r"\\caption\{([^}]*)\}", t)]

def env_bodies(t, envs):
    t = strip_comments(t)
    out = []
    for e in envs:
        for m in re.findall(r"\\begin\{"+e+r"\}(.*?)\\end\{"+e+r"\}", t, flags=re.S):
            b = m
            b = mask_math(b)
            b = unwrap_style(b)
            b = strip_cmds(b)
            b = re.sub(r"\s+"," ",b).strip()
            out.append(norm(b))
    return out

ENVS = ["theorem","proposition","corollary","remark","example","definition"]

new = read(NEW)
new_sent = sentences(new)
new_math = math_blocks(new)
new_cite = citations(new)
new_lab  = labels(new)
new_head = headings(new)
new_cap  = captions(new)
new_env  = env_bodies(new, ENVS)
NEW_SENT_STR = " ".join(new_sent)
NEW_MATH_SET = set(new_math)
NEW_CITE_SET = set(new_cite)
NEW_LAB_SET  = set(new_lab)
NEW_HEAD_SET = set(new_head)
NEW_CAP_SET  = set(new_cap)
NEW_ENV_SET  = set(new_env)

versions = ["12","13","14","15","16","16_1","16_2","17","18","19","20","21","22","23","24","25","26"]
paths = {v: (f"/tmp/oldvers/v{v}.tex" if v in ("12","13","14") else f"{LATEX}/paper2_obstruction_calculus_v{v}.tex") for v in versions}

report = {}
for v in versions:
    p = paths[v]
    if not os.path.exists(p):
        print("missing", p); continue
    t = read(p)
    missing_sent = [s for s in sentences(t) if s not in NEW_SENT_STR]
    missing_math = [m for m in math_blocks(t) if m not in NEW_MATH_SET]
    missing_cite = [c for c in citations(t) if c not in NEW_CITE_SET]
    missing_lab  = [l for l in labels(t)  if l not in NEW_LAB_SET]
    missing_head = [h for h in headings(t) if h not in NEW_HEAD_SET]
    missing_cap  = [c for c in captions(t) if c not in NEW_CAP_SET]
    missing_env  = [e for e in env_bodies(t, ENVS) if e not in NEW_ENV_SET]
    report[v] = dict(sent=missing_sent, math=missing_math, cite=missing_cite,
                     lab=missing_lab, head=missing_head, cap=missing_cap, env=missing_env)
    print(f"v{v}: missing sentences={len(missing_sent)} math={len(missing_math)} "
          f"cites={len(missing_cite)} labels={len(missing_lab)} headings={len(missing_head)} "
          f"captions={len(missing_cap)} env-bodies={len(missing_env)}")

json.dump({k:{kk:vv for kk,vv in v.items()} for k,v in report.items()},
          open("/tmp/scan_report.json","w"), indent=1)
print("\nreport saved to /tmp/scan_report.json")
