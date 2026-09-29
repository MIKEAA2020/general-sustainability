#!/usr/bin/env python3
"""Repair the mangled LaTeX command names in lean_README_v18.md.

Two command names in the appended v42 section were corrupted by Python
string escapes when the section was generated: the byte sequence that
should read backslash-r-e-f was written as backslash-n-e-f. Rebuilt
here with chr(92) so no escape is interpreted.
"""
import io

PATH = "/home/user/lean_README_v18.md"
BS = chr(92)          # backslash
NL = chr(10)

CORRECT = (
    "Two defects were introduced and caught before the push: a `"
    + BS + "ref{bands}`" + NL
    + "with no matching `" + BS + "label` (the band proposition is `"
    + BS + "ref{prop:bands}`, " + NL
    + "in the section labelled `hamming`), and a `"
    + BS + "noindent` destroyed by a " + NL
    + "Python escape. Post-fix: **unresolved refs none**, braces balanced, "
    + "environments matched."
)

def main():
    s = io.open(PATH, encoding="utf-8", newline="").read()

    # Locate the corrupted paragraph by its two stable anchors.
    start = s.find("Two defects were introduced and caught")
    end = s.find("Python escape. Post-fix:")
    if start < 0 or end < 0:
        print("MISS anchors"); return
    end = s.find(NL, end)                      # end of that line
    old = s[start:end]
    print("--- replacing ---")
    print(repr(old))

    s = s[:start] + CORRECT + s[end:]

    # Sweep any other backslash-n-followed-by-a-command-name left over.
    for tail in ("ef{", "oindent", "abel{", "item", "egin{"):
        s = s.replace(BS + "n" + tail, BS + tail)

    io.open(PATH, "w", encoding="utf-8", newline="").write(s)

    t = io.open(PATH, encoding="utf-8", newline="").read()
    print("--- verification ---")
    for name in ("ref{bands}", "ref{prop:bands}", "noindent", "label"):
        print(f"  {BS + name!r:24} count={t.count(BS + name)}")
    print("  stray CR:", t.count(chr(13)))
    print("  lines:", len(t.split(NL)))

if __name__ == "__main__":
    main()
