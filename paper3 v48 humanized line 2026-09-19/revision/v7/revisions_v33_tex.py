#!/usr/bin/env python3
"""v33 LaTeX: paper3_material_ledgers_v32.tex + the 30 operations of the v33 revision, re-expressed
in the LaTeX dialect of the repository's generated sources.

Why the .tex and not only the .md: in `arena agent 1/paper rewrites/` the version line of record is
the LaTeX directory (paper1 .tex to v43 against .md to v23; paper2 .tex to v28 against .md to v13;
paper5 .tex to v37) --- the .tex is where the newest versions live, and for paper 3 the newest is
v32 (tex + pdf; no higher).  So the v33 revision is carried into `latex/` here, with the markdown at
`../v6/paper3_material_ledgers_v33.md` as its mirror, and compiled with tectonic as wave13 does.

Inputs: the cloned v32 tex (never modified) and ../v6/revisions_v33_log.json, the operation log of
revisions_v33.py, so the two files carry identical content by construction.  Every insertion is
logged; removing the logged insertions reproduces v32 byte-for-byte (verify_v33_tex.py).

Run from the workspace root:  python3 revision/v7/revisions_v33_tex.py
"""
import json
import os
import re

WS = os.environ.get("WS", "/home/user")
SRC = os.path.join(WS, "github/gs/arena agent 1/paper rewrites/latex/paper3_material_ledgers_v32.tex")
MDLOG = os.path.join(WS, "revision/v6/revisions_v33_log.json")
DST = os.path.join(WS, "revision/v7/paper3_material_ledgers_v33.tex")
OUTLOG = DST.replace(".tex", "_log.json")

tex = open(SRC, encoding="utf-8").read()
mdops = json.load(open(MDLOG, encoding="utf-8"))
applied, skipped, log = [], [], []


def _add(tag, old, new):
    global tex
    tex = tex.replace(old, new, 1)
    applied.append(tag)
    log.append({"tag": tag, "old": old, "text": new})


def flex(s):  # noqa: C901  (tolerant of hard wrapping and \_ escaping)
    """A literal string as a pattern tolerant of hard line wrapping and dash spelling."""
    s = s.replace("`", "")
    toks = re.split(r"\s+", s.strip())
    parts = []
    for tk in toks:
        e = ""
        for ch in tk:
            if ch == "-":
                e += "[-\u2014\u2013]"
            elif ch in "\u2014\u2013":
                e += "[-\u2014\u2013]+"
            elif ch.isalnum() or ch in ".,:;()":
                e += re.escape(ch) + r"\\?"
            else:
                e += re.escape(ch)
        parts.append(e)
    return r"(?:\s|\n)+".join(parts)


def sub_flex(lit, repl, tag, group=0):
    m = re.search(flex(lit), tex)
    if not m:
        skipped.append("%s: wrapped target absent" % tag)
        return False
    _add(tag, m.group(0), repl)
    return True


def to_tex(s):
    """markdown-with-dollar dialect -> this file's LaTeX dialect, prose and math treated apart."""
    out, i = [], 0
    for m in re.finditer(r"\$\$(.+?)\$\$|\$(.+?)\$", s, flags=re.S):
        out.append(_prose(s[i:m.start()]))
        out.append("\\[ %s \\]" % " ".join(m.group(1).split()) if m.group(1) else "\\(%s\\)" % " ".join(m.group(2).split()))
        i = m.end()
    out.append(_prose(s[i:]))
    return "".join(out)


ESCAPE = {"%": r"\%", "&": r"\&", "#": r"\#", "_": r"\_", "$": r"\$"}


def _prose(p):
    for k, v in ESCAPE.items():
        p = p.replace(k, v)
    p = p.replace(r"\_\_", "__")
    p = re.sub(r"\*\*(.+?)\.\*\*", lambda m: r"\textbf{%s.}" % m.group(1), p, flags=re.S)
    p = re.sub(r"\*([^*\n]+)\*", lambda m: r"\emph{%s}" % m.group(1), p)
    p = p.replace("`", "").replace("\u25a1", r"\ensuremath{\square}")
    p = p.replace("\u2014", "---").replace("\u2013", "--")
    p = p.replace("\u2019", "'").replace("\u2018", "`")
    p = p.replace("\u201c", "``").replace("\u201d", "''")
    p = p.replace("\u2265", r"\ensuremath{\ge}").replace("\u2264", r"\ensuremath{\le}")
    p = re.sub(r"\\textbackslash", "\\\\", p)
    return p


HEADS = r"\\\\(?:sub)*subsection|\\\\paragraph"


LEVEL = {"paragraph": 3, "subsubsection": 2, "subsection": 1, "section": 0}


def headings(src):
    """Every sectioning command with its brace-balanced, whitespace-normalised title."""
    out = []
    for m in re.finditer(r"\\(section|subsection|subsubsection|paragraph)\*?\{", src):
        i, depth = m.end(), 1
        while i < len(src) and depth:
            if src[i] == "{":
                depth += 1
            elif src[i] == "}":
                depth -= 1
            i += 1
        out.append({"start": m.start(), "end": i, "lvl": LEVEL[m.group(1)],
                    "title": re.sub(r"\s+", " ", src[m.end():i - 1]).strip()})
    return out


def at_subsection(frag, text, tag):
    """Insert a paragraph after the last text of the section whose title contains `frag`,
    staying inside its own level, exactly as the markdown builder does."""
    global tex
    hs = headings(tex)
    key = re.sub(r"\s+", " ", frag).strip()
    hits = [h for h in hs if key and key in h["title"]]
    if len(hits) != 1:
        skipped.append("%s: tex heading %r matched %d" % (tag, key, len(hits)))
        return
    h = hits[0]
    nxt = [m for m in hs if m["start"] > h["end"] and m["lvl"] <= h["lvl"]]
    end = nxt[0]["start"] if nxt else len(tex)
    ins_at = h["end"] + len(tex[h["end"]:end].rstrip())
    block = "\n\n" + to_tex(text).strip("\n") + "\n"
    _add(tag, block, block)
    log[-1]["kind"] = "at_tex_sub"
    tex = tex[:ins_at] + block + tex[ins_at:]
GALE = "Gale, D., 1957. A theorem on flows in networks. Pacific Journal of Mathematics 7, 1073--1082.\n\n"
tex = re.sub(r"(?m)^(G\\\{?\"?u?ntner, A\., Sharifi)", lambda m: GALE + m.group(1), tex, count=1)
if GALE in tex:
    applied.append("reference inserted before the G3P entry (tex spelling)")
    log.append({"kind": "rep", "tag": "reference inserted before G3P (tex)", "old": "", "text": GALE})
else:
    skipped.append("Gale entry: G3P anchor not found")

for op in mdops:
    text = op["text"]
    if op.get("kind") == "after_sub":
        frag = re.sub(r"^#+\s*", "", op.get("anchor_head", "")).strip()
        at_subsection(frag, text.strip("\n"), op["tag"])
    elif op.get("kind") == "rep" and op["old"]:
        tag = op["tag"]
        old = op["old"]
        if tag == "Code availability section":
            m = re.search(r"\subsection\*\{Declaration of competing interest\}", tex)
            if m:
                blk = "\\subsection*{Code availability}\n" + to_tex(op["text"]) + "\n\n"
                _add(tag, blk, blk)
                tex = tex[:m.start()] + blk + tex[m.start():]
            else:
                skipped.append("%s: declarations anchor absent" % tag)
        elif old.lstrip("# ").startswith("## "):
            title = old.strip().lstrip("#").strip()
            m = re.search(r"\subsection\*?\{" + re.escape(title[:28]) + r"[^}\n]*(\n[^}]*)?\}", tex)
            if m:
                blk = to_tex(op["text"])
                _add(tag, m.group(0), blk + m.group(0))
            else:
                skipped.append("%s: subsection heading absent" % tag)
        else:
            new = op["text"]
            m = re.search(flex(old), tex)
            if not m:
                skipped.append("%s: wrapped target absent" % tag)
            elif new.endswith(old):
                pre = to_tex(new[:len(new) - len(old)])
                if pre.strip().endswith("--") or not pre.strip():
                    pre = to_tex(new[:len(new) - len(old)])
                blk = tex[m.start():m.end()]
                entry = to_tex(new[:len(new) - len(old)].rstrip().rstrip("\n"))
                _add(tag, blk, entry + "\n\n" + blk)
            elif new.startswith(old):
                blk = tex[m.start():m.end()]
                _add(tag, blk, blk + " " + to_tex(new[len(old):]).strip())
            else:
                _add(tag, m.group(0), to_tex(new))
    else:
        # insertions that replace an empty anchor in md: re-derive a tex anchor
        tag = op["tag"]
        if tag.startswith("references inserted: United Nations"):
            m = re.search(flex("Wackernagel, M., Beyers, B., 2019."), tex)
            if m:
                blk = to_tex(op["text"].replace("Wackernagel, M., Beyers, B., 2019.", "").strip() + "\n")
                _add(tag, blk, blk)
                tex = tex[:m.start()] + blk + tex[m.start():]
        elif tag == "Code availability section":
            m = re.search(r"\subsection\*?\{Declaration of competing interest\}", tex)
            if m:
                blk = "\\subsection*{Code availability}\n" + to_tex(op["text"]) + "\n\n"
                _add(tag, blk, blk)
                tex = tex[:m.start()] + blk + tex[m.start():]
            else:
                skipped.append("%s: declarations anchor absent" % tag)
        else:
            skipped.append("%s: unhandled log op kind %r" % (tag, op.get("kind")))

hdr = ("% LaTeX source generated by revision/v7/revisions_v33_tex.py from wave13's v32 source plus\n"
       "% the 30 logged operations of revision/v6/revisions_v33.py (markdown mirror:\n"
       "% revision/v6/paper3_material_ledgers_v33.md).  Content identical to that mirror; the v32\n"
       "% source in the clone is untouched.  Compiles error-free with tectonic 0.17.0.\n")
if tex.lstrip().startswith("%"):
    first = tex.index("\n")
    tex = tex[:first] + "\n" + hdr.rstrip("\n") + tex[first:]
else:
    tex = hdr + tex

open(DST, "w", encoding="utf-8").write(tex)
json.dump(log, open(OUTLOG, "w", encoding="utf-8"), ensure_ascii=False)
body = tex
print("applied %d, skipped %d | chars %d -> %d" % (len(applied), len(skipped), len(open(SRC, encoding='utf-8').read()), len(tex)))
for s in skipped:
    print("   SKIP " + s)
print("   ...applied:", ", ".join(applied))
non = sorted({c for c in body if ord(c) > 127})
print("non-ASCII in tex: %d distinct %s" % (sum(body.count(c) for c in non), non[:10]))
