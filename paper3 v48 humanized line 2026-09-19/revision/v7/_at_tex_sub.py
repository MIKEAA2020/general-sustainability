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


