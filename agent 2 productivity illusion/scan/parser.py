"""Markdown -> Claim list, preserving source line numbers for hyperlinking.

The master's actionable items live under `### 12X` headings as either
numbered sub-items (12A/12B/12C/12D/12E) or `**12G.N - ...**` bolded items.
We keep the same IDs the audit produced (12A.1 ... 12G.7). The revision is chunked
into paragraphs, each carrying its starting line number and nearest section heading.
"""
import re
from pathlib import Path
from .models import Claim

def _line_of(text, index):
    return text.count("\n", 0, index) + 1

def parse_master(path):
    text = Path(path).read_text()
    claims = []
    sec_pat = re.compile(r'^### 12([A-H])\.\s*(.+)$', re.M)
    secs = {}
    for m in sec_pat.finditer(text):
        nxt = sec_pat.search(text, m.end())
        body_start = m.end()                       # absolute offset where the body begins
        body = text[body_start: nxt.start() if nxt else len(text)]
        secs[m.group(1)] = (body_start, body)
    for lbl, (bstart, body) in secs.items():
        if lbl in "ABCD":
            pat = re.compile(r'(?:^|\n)\s*(\d{1,2})\.\s+', re.M)
            st = [m for m in pat.finditer(body)]
            for i, m in enumerate(st):
                seg = body[m.start(): st[i + 1].start() if i + 1 < len(st) else len(body)]
                for line in seg.split("\n"):
                    if line.strip() and not re.match(r'^\s*\d+\.\s*$', line):
                        title = re.sub(r'[*_#]', '', line).strip(); break
                else:
                    title = ""
                claims.append(Claim(id=f"12{lbl}.{m.group(1)}", text=" ".join(seg.split()),
                                    source_file=str(path),
                                    line_number=_line_of(text, bstart + m.start()),
                                    section=f"12{lbl}", type="informational"))
        elif lbl == "G":
            # 12G items are `**12G.N — title.**` followed by the substantive body (bullets /
            # paragraphs) up to the next item. Capture heading + body so the claim text is
            # informative for matching (heading-only queries are uninformative).
            pat = re.compile(r'\*\*12G\.(\d{1,2})\b\s*[-\u2013\u2014]\s*(.+?)\*\*', re.S)
            starts = [(m.start(), m) for m in pat.finditer(body)]
            for k, (m) in enumerate(starts):
                m = m[1]
                end = starts[k + 1][0] if k + 1 < len(starts) else len(body)
                full = body[m.start(): end]
                cl_text = " ".join(full.split())
                claims.append(Claim(id="12G." + m.group(1), text=cl_text,
                                    source_file=str(path),
                                    line_number=_line_of(text, bstart + m.start()),
                                    section="12G", type="informational"))
        elif lbl == "E":
            claims.append(Claim(id="12E.1", text=" ".join(body.split()), source_file=str(path),
                                line_number=_line_of(text, bstart), section="12E", type="informational"))
    return claims

def parse_revision(path):
    """Return paragraph claims for the revision, with line numbers + section."""
    lines = Path(path).read_text().splitlines()
    section = "Preamble"
    paragraphs = []  # (section, start_line, text)
    buf, start = [], None
    for i, ln in enumerate(lines):
        m = re.match(r'^(#{2,3})\s+(.*)$', ln)
        if m:
            if buf:
                paragraphs.append((section, start, " ".join(buf))); buf = []
            section = m.group(2).strip()
            start = i + 1
            continue
        if not ln.strip():
            if buf:
                paragraphs.append((section, start, " ".join(buf))); buf = []
            start = None
        else:
            if start is None:
                start = i + 1
            buf.append(ln)
    if buf:
        paragraphs.append((section, start, " ".join(buf)))
    return [Claim(id=f"rev-pg-{k}", text=t, source_file=str(path), line_number=st,
                  section=sec, type="informational")
            for k, (sec, st, t) in enumerate(paragraphs)]
