#!/usr/bin/env python3
"""v39: the structural verdict measured rather than opined.

The label-citation graph of v38 was computed (see review/corpus_and_split_v1.md): the seven result-bearing
sections {2,3,4,5,6,7,10} form a single strongly connected component -- all 21 mutually reachable pairs -- and
34 of 61 statements are cited outside their home section. So no split exists: any cut duplicates the definitional
front end. What the graph *does* show is that Sections 8 and 9 carry 0 numbered statements while consuming
3,378 characters, and that Section 6.5 carries an extraction-provenance paragraph whose home is the
supplementary's version record. v39 acts on that: one promotion, two demotions, no deletion.

  P1  Section 9's exact-projection claim is a result stated as prose. It is labelled (Proposition 43) and given
      its one-line proof, because an unlabelled assertion in a zero-statement section is the one thing a reader
      cannot cite.
  D1  The G3P basin-row provenance paragraph moves to the supplementary's S5 record, where the vintage,
      version-sensitivity and row-by-row re-verification already live; the article keeps the classification
      sentence and a pointer.
  D2  Sections 8.1 and 8.2 are condensed to their registered status and their gap, with the ladder detail moved
      to the supplementary next to the ladders it duplicates.

Every demoted sentence is re-emitted verbatim in revision/v7/paper3_supplementary_v10.md, and
verify_v39_build.py asserts that: nothing is dropped anywhere in this batch.
"""
import re, sys, json

R = '/home/user/revision/v7'
sys.path.insert(0, R)
from build_v35_kernel import m2t, pattern            # noqa: E402

SRC = f'{R}/paper3_material_ledgers_v38.md'
MD_OUT, TEX_OUT = f'{R}/paper3_material_ledgers_v39.md', f'{R}/paper3_material_ledgers_v39.tex'
LOG = f'{R}/revisions_v39_kernel_log.json'
SUPP_OUT = f'{R}/paper3_supplementary_v10.md'

md = open(SRC).read()
MOVED = {}


def grab(start_marker, end_marker, key):
    """Whole paragraphs from start_marker up to (not including) end_marker; recorded as moved text."""
    i = md.index(start_marker)
    j = md.index(end_marker, i)
    block = md[i:j].rstrip('\n')
    MOVED[key] = block
    return block


# ---------------------------------------------------------------- D1: the basin-row provenance paragraph
B1 = grab("""The basin rows are reported extractions from the G3P v1.12 basin series,""",
          """\n| Country | Reserves""", 'g3p_provenance')
REPL1 = ("""The basin rows are reported extractions from the G3P v1.12 basin series, used here only to exhibit the
index construction of Section 6.5.1 and never as product-endorsed values: the window-minimum column is implied
arithmetically through the index formula, every row must be re-derived from the product's basin masks before any
numerical reuse, and the extraction provenance --- including why the Indo-Gangetic row is the extreme case and
how its fitted segment convention enters --- is recorded in the supplementary's S5.4 with the vintage record it
belongs to. The classification status assigned below does not depend on the magnitudes.""")

# ---------------------------------------------------------------- D2: the two registered templates
def para(start_marker):
    a = md.index(start_marker)
    b = md.index('\n\n', a)
    return md[a:b]


B2a = para("The phosphorus domain enters at registered template status")
B2b = para("The groundwater template enters at registered status with an admitted object")
MOVED['templates'] = ("### 8.1 The phosphorus template\n\n" + B2a + "\n\n"
                      "### 8.2 The groundwater template and the two-pool gap\n\n" + B2b)
REPL2a = ("""The phosphorus domain enters at registered template status: an identification ladder for the
resource-product-waste-detritus structure of Section 2.3, whose constitutive content --- yield and loss
functions, recovery fractions, the price response of the reserve classification --- is declared and not
established, and whose reserve and production quantities carry their source vintage (U.S. Geological Survey,
2026). The ladder's competing-model structure and its falsification protocols are recorded obligations rather
than results. The ladders themselves are the supplementary's S2, next to the groundwater ladder this one pairs
with, and the registered detail these paragraphs used to carry --- the competing-model structure and the
falsification protocols in full --- is its S14; nothing in Sections 6 to 10 uses either.""")
REPL2b = ("""The groundwater template enters at registered status with one admitted object and one declared gap: the
admitted object is the one-pool affine approximation behind the anomaly-persistence index of Section 6.5.1, and
the two-pool model --- active storage with a slow donor pool, the two-compartment structure of Section 2.2 ---
is not established. The registered identification requirements for closing that gap, and the discipline that
leakage terms may not absorb unexplained residuals, are the subject of the supplementary's S2.1, and none of
them is met by the record used in Section 6.5; the registration as this article previously stated it is the
supplementary's S14.""")

# ---------------------------------------------------------------- P1: label Section 9's projection result
i = md.index("**The hand-off projection.**")
j = md.index('\n\n', i)
PROJ = md[i:j]
NEWPROJ = ("""**Proposition 43 (The institutional-failure subsystem is exactly closed).** *Under the institutional-failure
specialization of Section 5.4, the ecological-institutional subsystem on $(N, A^{\\mathrm{act}}, A^{\\mathrm{geo}},
U, Z, E)$ is an exact closed projection of the ledger for every parameter value: no singular limit, no small
parameter and no timescale separation is required, and no macroeconomic variable enters its vector field.*
*Proof.* The six right-hand sides displayed above depend only on the block's own states and the delayed memory; a
subsystem whose vector field involves no excluded variable is invariant, and invariance is the projection. The
converse fails by construction --- the excluded block is driven by the subsystem --- so the projection is
one-way, and Section 5's macroeconomic readouts remain available without being determined. $\\square$

What the proposition does not claim is the next step, and the distinction is the point of stating it: the
memory-effort pair $(Z, E)$ is the gated three-state core and working four-state core of the companion
delay-dynamics analysis (under review; its eq. (1), the gated three-state core, and its Section 2.4, which
relates that core to the working four-state model), not an object of this article, and the semiconjugacy
condition $D\\pi(\\xi) f(\\xi) = F(\\pi(\\xi))$ on the history phase space --- which would carry closed-block
results across to that system --- is made under the citation and is not re-proved here.""")


DAGGER_OLD = ("""the full quarantine record is the paragraph below.""")
DAGGER_NEW = ("""its full provenance is the supplementary's S5.4.""")
assert md.count(DAGGER_OLD) == 1


# ---------------------------------------------------------------- D3: the article's own self-pointer
# the md is hard-wrapped, so the phrase is taken as it actually stands rather than typed out
_ms = re.search(r'Section\s+1\.5\s+draw their own', md)
assert _ms and md.count(_ms.group(0)) == 1, 'standards self-pointer not located'
STD_OLD = _ms.group(0)
STD_NEW = STD_OLD.replace('1.5', '1.2')

# ---------------------------------------------------------------- assemble: replace, then append nothing
new_md = (md.replace(B1, REPL1).replace(B2a, REPL2a).replace(B2b, REPL2b).replace(PROJ, NEWPROJ)
            .replace(DAGGER_OLD, DAGGER_NEW).replace(STD_OLD, STD_NEW))
assert new_md != md and B1 in md and B2a in md and B2b in md

# numbering note: the added-label list gains Proposition 43
NOTE_OLD = ("and Propositions 25\u201332 and 36\u201337 and 39\u201342, with Remarks 33\u201336,")
NOTE_NEW = ("and Propositions 25\u201332 and 36\u201337 and 39\u201343, with Remarks 33\u201336,")
assert new_md.count(NOTE_OLD) == 1
new_md = new_md.replace(NOTE_OLD, NOTE_NEW)

# ---------------------------------------------------------------- the tex twin
tx = open(f'{R}/paper3_material_ledgers_v38.tex').read()


def to_tex(s_):
    """md -> tex dialect, plus the punctuation the shipped tex writes in ASCII."""
    t = m2t(s_)
    for a, b in (('\u2014', '---'), ('\u2013', '--'), ('\u2019', "'"), ('\u201c', '"'), ('\u201d', '"')):
        t = t.replace(a, b)
    return t


def texswap(old_md, new_md_txt, name):
    global tx
    o, n = to_tex(old_md), to_tex(new_md_txt)
    mo, mn = pattern(o).search(tx), None
    if not mo:
        print(f'  {name}: TEX ANCHOR MISS'); sys.exit(1)
    tx = tx[:mo.start()] + n + tx[mo.end():]
    return mo.group(0)


t0 = texswap(DAGGER_OLD, DAGGER_NEW, 'D0')
t9 = texswap(STD_OLD, STD_NEW, 'D3')
t1 = texswap(B1, REPL1, 'D1')
# D2 spans two \subsubsection headings, whose tex wording wraps and whose body carries \ensuremath
# conversions; anchor the whole span in the tex instead of the md paragraphs.
a1 = tx.index('\\subsubsection{8.1 The phosphorus')
a1 = tx.rfind('\n\n', 0, a1) + 2
a3 = tx.index('\\subsubsection{8.3 Extractor-side')
b3 = tx.rfind('\n\n', 0, a3) + 2
old_span = tx[a1:b3]
def heading(span, key):
    a = span.index(key)
    b = span.index('\\label{', a)
    return span[a:span.index('\n', b)]


h81 = heading(old_span, '\\subsubsection{8.1')
h82 = heading(old_span, '\\subsubsection{8.2')
assert h81.endswith('}') and h82.endswith('}')
new_tx = (h81 + '\n\n' + to_tex(REPL2a) + '\n\n' + h82 + '\n\n' + to_tex(REPL2b) + '\n\n')
tx = tx[:a1] + new_tx + tx[b3:]
t2a, t2b = h81, h82
old_span_out = old_span
t3 = texswap(PROJ, NEWPROJ, 'P1')
tx = tx.replace(to_tex(NOTE_OLD), to_tex(NOTE_NEW))
bad = sorted({c for c in tx if ord(c) > 127})
print('tex non-ascii:', bad, '| $ in tex:', tx.count(chr(36)),
      '| display-dollar left:', '$$' in tx)
if bad or '$$' in tx:
    sys.exit(1)
open(MD_OUT, 'w').write(new_md)
open(TEX_OUT, 'w').write(tx)
json.dump([
    {'name': 'D3-standards-self-pointer', 'md': [[STD_OLD, STD_NEW]], 'tex': [[t9, to_tex(STD_NEW)]]},
    {'name': 'D0-dagger-note-repoint', 'md': [[DAGGER_OLD, DAGGER_NEW]], 'tex': [[t0, to_tex(DAGGER_NEW)]]},
    {'name': 'D1-g3p-provenance', 'md': [[B1, REPL1]], 'tex': [[t1, to_tex(REPL1)]]},
    {'name': 'D2-template-ladders', 'md': [[B2a, REPL2a], [B2b, REPL2b]], 'tex': [[old_span_out, new_tx]]},
    {'name': 'P1-projection-labelled', 'md': [[PROJ, NEWPROJ]], 'tex': [[t3, to_tex(NEWPROJ)]]},
    {'name': 'numbering-note-43', 'md': [[NOTE_OLD, NOTE_NEW]], 'tex': [[to_tex(NOTE_OLD), to_tex(NOTE_NEW)]]},
], open(LOG, 'w'), indent=1)

# ---------------------------------------------------------------- supplementary v10 = v9 + new sections + moved text
v9 = open('/home/user/revision/v6/paper3_supplementary_v9.md').read()
cand = open(f'{R}/supplementary_v9_candidate.md').read()
sec10 = cand[cand.index('## 2. S11'):cand.index('## 3. S12')]
sec11 = cand[cand.index('## 3. S12'):cand.index('## 4. Items')]
sec10 = sec10.replace('## 2. S11 \u00b7 Per-parameter identifiability status',
                      '## S10 \u00b7 Per-parameter identifiability status (main-text v39)').replace(
    'Status vocabulary is the article', 'Status vocabulary is the article')
sec11 = sec11.replace('## 3. S12 \u00b7 Material and energy value: what is checkable, and what is not',
                      '## S11 \u00b7 Material and energy value: what is checkable, and what is not (main-text v39)')
tail = f"""
---

# Part III - additions at v10, against main-text v39

The two tables below are the fields the review cycle kept deferring, and the three records after them are
material the main text no longer carries because its structural audit put it here: the extraction provenance of
the G3P basin rows (S5.4, continuing the S5 record it belongs to), the registered domain-template ladders
(S14, next to the S2 ladders they elaborate), and the proof-obligation row for `Typed`, which now cites the
main text's Definition 47 instead of pointing at an undefined use of the word "typing". Nothing was deleted
from the article in this round: S5.4 and S14 reproduce the demoted passages verbatim.

{sec10.strip()}

{sec11.strip()}

## S5.4 \u00b7 G3P basin-row extraction provenance (demoted from main-text Section 6.5.2)

*The main text keeps the classification sentence and this record's pointer; what follows is the demoted
provenance, reproduced without change. Deictic words are the main text's: "the classification status assigned
below" named the table that still follows it there.*

{MOVED['g3p_provenance']}

## S14 \u00b7 Registered domain-template detail (demoted from main-text Sections 8.1 and 8.2)

*The main text now states the registered status and the gap for each template and points here; the ladders
above (S2) are the objects these paragraphs name, so the two records belong together.*

{MOVED['templates']}

## S16 \u00b7 S7's discharge column, restated against main-text v39

Part II added S7 while the article was at v33, and three of its "discharged by" pointers name loci that
the renumbering has since moved. Nothing in S7 is wrong in substance; these are the labels to read today,
and the `Typed` row is corrected in S15 rather than here.

| Entry | S7 says | Read this instead in v39 |
|---|---|---|
| `Balanced` | \u00a73.2 | Lemma 3, with the typing of Definition 47 |
| `Conserved` | Definition 23, Proposition 1 | Proposition 4 with Theorems 7\u20139; Definition 23 is now the bounded-residual clause of \u00a73.4, and the Proposition 1 of that row is the layering counter's, not the main counter's |
| `Admissible` | \u00a73.2 Proposition 2 and its thermodynamic clause | Definitions 1 and 42, with Proposition 40 for the empty-corridor case |
| `Safe` | \u00a73.5 envelope theorem, \u00a76.3\u20136.4, Theorem 24 | Theorem 24 unchanged, plus Definitions 45 and 46 for the deadline and the envelope it is read against |

The same care applies to the sentence after the table: "`Conserved \u21d2 Balanced` for the conserved
quantities (Proposition 1)" is the layering counter's Proposition 1, which is the main counter's Proposition 4.

## S15 \u00b7 `Typed` proof-obligation row, corrected

| predicate | statement | main-text locus | witness | fails when |
|---|---|---|---|---|
| `Typed` | every compartment carries a declared type and unit, and no column of `S_T` is both a transfer and a conversion | Definitions 47, Proposition 42 | the declaration `(Ty, ty, Cv)` itself | a row sums unlike types, or a conversion is booked as a sum |

`Typed` is the only one of the eight obligations decidable from a declaration alone rather than from a
declaration and a trajectory; Proposition 42 states what no such check can buy, namely a conservation law
crossing a type class.
"""
open(SUPP_OUT, 'w').write(v9.rstrip('\n') + '\n' + tail)
print('\nwrote', MD_OUT, len(new_md), 'B |', TEX_OUT, len(tx), 'B |', SUPP_OUT,
      len(open(SUPP_OUT).read()), 'B')
print('moved blocks recorded:', {k: len(v) for k, v in MOVED.items()})
print('article words:', len(new_md.split()), '(was', len(md.split()), ')')
