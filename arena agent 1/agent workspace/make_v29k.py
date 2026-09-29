#!/usr/bin/env python3
"""v29k repair pass.

Three defects the v29j cadence pass introduced or exposed:

K1  The cadence block was spliced INTO the middle of the source-year
    sentence in 3.4: the sentence had no closing full stop, a longtable
    sat between the clause and its final subordinate clause, and the
    trailing clause was orphaned after the table.  Restore the sentence
    and move the block after it.

K2  The cadence table was numbered 8 but is the SECOND table first cited
    in the text (3.4, before the depensation table of 3.6).  Journals
    require numbering in order of first citation.  Renumber: cadence
    becomes Table 2 and Tables 2..7 shift to 3..8.

K3  Data availability said "The primary kernel tables (Tables 1 and 2,
    Sections 3.1--3.5) are produced by run_intervention_v3.py".  Table 2
    is the 3.6 depensation table, produced by three other scripts named
    in the same paragraph.  Reduce to Table 1.
"""
import io
import re
import shutil

TEX = "/home/user/fam/e2/paperE2_cod_intervention_v29.tex"
shutil.copy(TEX, "/tmp/v29j_before_repair.tex")
tex = io.open(TEX, encoding="utf-8").read()
orig = tex
log = []


def sub1(tag, old, new):
    global tex
    n = tex.count(old)
    assert n == 1, f"{tag}: anchor matched {n} times, need exactly 1"
    tex = tex.replace(old, new, 1)
    log.append(tag)


# ---------------------------------------------------------------- K1
START = "The horizon is not a property of the policy"
END = "\n\\end{longtable}\n"
i = tex.index(START)
j = tex.index(END, i) + len(END)
block = tex[i:j]
assert "Table 8" in block, "block does not look like the cadence block"
tex = tex[:i] + tex[j:]
# the orphaned tail clause follows the vacated gap
tail = "\nwhile leaving \\(a_{\\max}\\) unchanged."
k = tex.index(tail, i)
tex = tex[:k] + tex[k + len(tail):]
# close the sentence properly and re-insert the block after it
sub1("K1a close the source-year sentence and re-insert the block",
     "by the source-year one (\\(329.0\\) kt)\n",
     "by the source-year one (\\(329.0\\) kt)" + tail + "\n\n"
     + block.rstrip("\n") + "\n\n")
log.append("K1b cadence block moved after the restored sentence")

# ---------------------------------------------------------------- K2
# "Table 17" (a citation to Regular et al. 2025) must survive untouched:
# require a digit that is not followed by another digit.
def shift(t):
    t = re.sub(r"Table 8(?![0-9])", "Table \x00CAD\x00", t)
    for a, b in ((7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3)):
        t = re.sub(r"Table %d(?![0-9])" % a, "Table %d" % b, t)
    return t.replace("Table \x00CAD\x00", "Table 2")


before = re.findall(r"Table [0-9]+(?![0-9])", tex)
tex = shift(tex)
tex = shift(tex) if re.search(r"Table \x00CAD\x00", tex) else tex
after = re.findall(r"Table [0-9]+(?![0-9])", tex)
assert "Table 17" in tex, "the citation Table 17 was damaged"
nums = set(re.findall(r"Table ([0-9]+)(?![0-9])", tex))
assert nums <= set("12345678") | {"17"}, f"unexpected table numbers {sorted(nums)}"
# every renumbered site, for the record
log.append("K2 renumbered: %s" % ", ".join(
    f"{a}->{b}" for a, b in zip(before, after) if a != b))

# ---------------------------------------------------------------- K3
sub1("K3 kernel-table provenance reduced to Table 1",
     "The primary kernel\ntables (Tables 1 and 2, Sections 3.1--3.5) are produced by",
     "The primary kernel\ntable (Table 1, Sections 3.1--3.5) is produced by")

io.open(TEX, "w", encoding="utf-8").write(tex)
print("\n".join("  " + x for x in log))
print("lines %d -> %d" % (orig.count("\n"), tex.count("\n")))
