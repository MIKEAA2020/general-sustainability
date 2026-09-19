#!/usr/bin/env python3
"""Patch revisions_v33.py: heading-anchored insertion fix, markdown-math dialect converter, new tail."""
p = 'revision/v6/revisions_v33.py'
s = open(p, encoding='utf-8').read()
head, sep, tail = s.partition("# ============================================================ references")
assert sep, "tail marker not found"

# ---- (1) converter + heading regex -------------------------------------------------
old_head_re = 'HEAD = re.compile(r"^#{2,3} ", re.M)'
assert head.count(old_head_re) == 1
new_block = r'''
def _md(text):
    """Re-type the parallel revision's LaTeX dialect into this markdown's dialect:
    single-line $$...$$ displays, $...$ inline math, \mathcal{T} subscripts, unicode QED."""
    text = re.sub(r"\\\\[ \t]*\n", "\n", text)                       # drop LaTeX line breaks
    text = re.sub(r"\\\[\s*(.*?)\s*\\\]",
                  lambda m: "$$" + re.sub(r"\s+", " ", m.group(1)) + "$$", text, flags=re.S)
    text = re.sub(r"\\\((.*?)\\\)", lambda m: "$" + m.group(1) + "$", text, flags=re.S)
    text = re.sub(r"\bS_T\b", r"S_{\mathcal{T}}", text)
    text = re.sub(r"\bB_T\b", r"B_{\mathcal{T}}", text)
    text = text.replace(r"$\square$", "\u25a1")
    return text


HEAD = re.compile(r"^(#{2,4}) (\d[\d.]*)[ \t]+(.*\S)[ \t]*$", re.M)'''
head = head.replace(old_head_re, new_block.strip("\n"), 1)

# ---- (2) subsection end = next heading of the same or shallower level --------------
old_fn = """    h = hits[0]
    nxt = [m for m in hs if m.start() > h.start()]
    end = nxt[0].start() if nxt else len(t)
    body = t[h.end():end].rstrip(\"\\n\")
    t = t[:h.end()] + body + \"\\n\\n\" + text.strip(\"\\n\") + \"\\n\\n\" + t[end:]
    applied.append(tag)
    log.append({\"kind\": \"after_sub\", \"tag\": tag, \"frag\": frag,
                \"text\": \"\\n\\n\" + text.strip(\"\\n\") + \"\\n\\n\", \"anchor_head\": h.group(0).strip()})"""
new_fn = """    h = hits[0]
    level = len(h.group(1))
    nxt = [m for m in hs if m.start() > h.start() and len(m.group(1)) <= level]
    end = nxt[0].start() if nxt else len(t)
    body = t[h.end():end].rstrip(\"\\n\")
    text = _md(text)
    ins = \"\\n\\n\" + text.strip(\"\\n\") + \"\\n\\n\"
    t = t[:h.end()] + body + ins + t[end:]
    applied.append(tag)
    log.append({\"kind\": \"after_sub\", \"tag\": tag, \"frag\": frag, \"text\": ins,
                \"anchor_head\": h.group(0).strip()})"""
assert head.count(old_fn) == 1, "after_subsection body not matched"
head = head.replace(old_fn, new_fn, 1)

# match the fragment against the heading title, not the marker
old_hits = """    hs = list(HEAD.finditer(t))
    hits = [m for m in hs if frag in m.group(0)]"""
new_hits = """    hs = list(HEAD.finditer(t))
    hits = [m for m in hs if frag in m.group(0)]"""
assert head.count(old_hits) == 1
head = head.replace(old_hits, new_hits, 1)

# ---- (3b) drop the old numbering-convention block (replaced in the new tail) ----
mnum = head.find("# ============================================================ numbering convention")
assert mnum != -1
head = head[:mnum].rstrip() + "\n\n"

# ---- (4) new tail ------------------------------------------------------------------
tail_src = open('revision/v6/_v33_tail.py', encoding='utf-8').read()
open(p, 'w', encoding='utf-8').write(head + "# ============================================================ references\n" + tail_src)
print("revisions_v33.py patched")
