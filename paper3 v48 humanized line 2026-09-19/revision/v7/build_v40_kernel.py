#!/usr/bin/env python3
r"""v40: the recomputation's consequences, written back into the article and the supplementary.

The computation the companion commentary named as the thing standing between it and a full paper has been run
(revision/v7/analysis/nfa_tau/, on the two editions of the accounts obtainable without an account). Four
consequences for the main text and one for the supplementary:

  E1  A provenance error the run exposed: Remark 33 attributes its 2022 figure to Lin et al. (2018), but that
      release's series ends in 2014, as the table itself shows. The sentence now names the edition the year
      comes from and keeps Lin et al. for what they do document.
  E2  The "four-day difference" sentence gains the third cause the run measured, which is not a vintage at all:
      the level at which the accounts are aggregated.
  E3  Remark 37, a structural fact the run turned up and which no sentence stated: two component ratios are
      identities at a world aggregate, so the restricted minimum is pinned at 365 d in every year. It is
      labelled because it is a result -- the rule that produced v39's Proposition 43.
  E4/E5  Data and code availability record the two edition tables, their checksums and the registration gate.
  E6   The numbering note, Remarks 33-36 -> 33-37.
  S17  Supplementary v11 = v10 plus the recomputation record, its table generated from the CSV the script wrote.

Every number interpolated here is read from the run's CSVs, not transcribed: see `stats()`.
"""
import csv
import json
import os
import re

R = '/home/user/revision/v7'
A = f'{R}/analysis/nfa_tau'
SRC, SRC_T = f'{R}/paper3_material_ledgers_v39.md', f'{R}/paper3_material_ledgers_v39.tex'
MD_OUT, TEX_OUT = f'{R}/paper3_material_ledgers_v40.md', f'{R}/paper3_material_ledgers_v40.tex'
LOG = f'{R}/revisions_v40_kernel_log.json'
SUPP_IN, SUPP_OUT = f'{R}/paper3_supplementary_v10.md', f'{R}/paper3_supplementary_v11.md'

# --------------------------------------------------------------------- md -> tex dialect (copied from the
# v39 builder so that importing it cannot re-run that builder's writes; see structure_v39.md's note)
SQ = '\u25a1'


def _prose(t):
    t = re.sub(r'\*\*(.+?)\*\*', lambda m: '\\textbf{' + m.group(1) + '}', t, flags=re.S)
    t = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', lambda m: '\\emph{' + m.group(1) + '}', t, flags=re.S)
    return t.replace(SQ, '\\ensuremath{\\square}')


def m2t(s):
    out, i = [], 0
    tok = re.compile(r'\$\$[\s\S]*?\$\$|\$[^$]*\$|\\[[\s\S]*?\\]')
    for m in tok.finditer(s):
        out.append(_prose(s[i:m.start()]))
        t = m.group(0)
        if t.startswith('$$'):
            out.append('\\[ ' + t[2:-2].replace('\n', ' ').strip() + ' \\]')
        elif t[0] == '$':
            out.append('\\(' + t[1:-1].replace('\n', ' ').strip() + '\\)')
        else:
            out.append('\\[' + t[2:-2] + '\\]')
        i = m.end()
    out.append(_prose(s[i:]))
    return ''.join(out)


def to_tex(s):
    t = m2t(s)
    for a, b in (('\u2014', '---'), ('\u2013', '--'), ('\u2019', "'"), ('\u201c', '"'), ('\u201d', '"')):
        t = t.replace(a, b)
    return t


def flex(s):
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c.isspace():
            j = i
            while j < len(s) and s[j].isspace():
                j += 1
            out.append(r'\s+')
            i = j
            continue
        if c in '_^{}&%#\\':
            out.append('(?:' + re.escape('\\' + c) + '|' + re.escape(c) + ')')
        else:
            out.append(re.escape(c))
        i += 1
    return ''.join(out)


def pattern(s):
    """Whitespace-flexible, backslash-tolerant, and split on math delimiters so md $..$ matches tex \\(..\\)."""
    return re.compile(r'(?:\$|\\\(|\\\))'.join(flex(p) for p in s.split('$')))



# --------------------------------------------------------------------- corrected prose rule
# The converter this article's lineage has always used applies the bold and italic rules to the *prose
# segments between math tokens*, so an emphasis span that contains inline math (`*Compensation holds at
# fraction $\kappa$*`) or that opens immediately after a bold run (`**Remark 33 (…).** *claim…*`) is left as
# literal asterisks in the tex. Five sites in the manuscript are affected, four of them result-bearing
# statements, and the PDF of record has printed them as stray asterisks since at least v38. The fix protects
# the math tokens with sentinels, converts emphasis over the whole paragraph, then restores the math.
SQ2 = '\u25a1'


def esc_sp(u):
    """Escape LaTeX specials one character at a time, so no replacement string has to survive Python quoting."""
    return ''.join(('\\' + ch) if ch in '_%#&{}$' else ch for ch in u)
# math *and* code spans are held out of the prose rules; the manuscript's own pipeline renders a backticked
# span as \texttt{...} with the specials escaped, and this builder has to agree with it or an inserted
# sentence would print its backticks.
MATH = re.compile(r'\$\$[\s\S]*?\$\$|\$[^$]*\$|\\[[\s\S]*?\\]|`[^`\n]*`')


def _prose_f(t):
    t = re.sub(r'\*\*(.+?)\*\*', lambda m: '\x01' + m.group(1) + '\x01', t, flags=re.S)
    t = re.sub(r'(?<![\x01*])\*([^*\x01]+?)\*(?!\*)', lambda m: '\\emph{' + m.group(1) + '}', t, flags=re.S)
    t = re.sub('\x01(.+?)\x01', lambda m: '\\textbf{' + m.group(1) + '}', t, flags=re.S)
    return t.replace(SQ2, '\\ensuremath{\\square}')


def m2t_f(s):
    held = {}

    def stash(m):
        k = '\x02%d\x03' % len(held)
        t = m.group(0)
        if t[0] == '`':
            v = '\\texttt{' + esc_sp(t[1:-1]) + '}'
        elif t.startswith('$$'):
            v = '\\[ ' + t[2:-2].replace('\n', ' ').strip() + ' \\]'
        elif t[0] == '$':
            v = '\\(' + t[1:-1].replace('\n', ' ').strip() + '\\)'
        else:
            v = '\\[' + t[2:-2] + '\\]'
        held[k] = v
        return k

    out = _prose_f(MATH.sub(stash, s))
    for k, v in held.items():
        out = out.replace(k, v)
    return out


def to_tex_f(s):
    t = m2t_f(s)
    for a, b in (('\u2014', '---'), ('\u2013', '--'), ('\u2019', "'"), ('\u201c', '"'), ('\u201d', '"')):
        t = t.replace(a, b)
    return t


def skel(s):
    r"""Content skeleton: letters and digits with LaTeX command *names* and emphasis marks removed. Command
    arguments survive, so a dropped \label or \ref still shows up as a difference, while `*x*` and \emph{x}
    compare equal --- which is what the E8 guard needs, since that pass changes only markup."""
    t = re.sub(r'\\[a-zA-Z]+\*?', ' ', s)
    t = re.sub(r'[{}\\`$*]', ' ', t)
    return ''.join(re.findall(r'[A-Za-z0-9]', t))

# --------------------------------------------------------------------- numbers read from the run
def stats():
    rows = list(csv.DictReader(open(f'{A}/tau_by_year_2018edition.csv')))
    dl = list(csv.DictReader(open(f'{A}/edition_delta.csv')))
    g = lambda r, k: float(r[k])
    by = {int(r['year']): r for r in rows}
    ks = [r for r in rows if int(r['year']) >= 2005]
    dec = {}
    for r in rows:
        dec.setdefault(int(r['year']) // 10 * 10, []).append(g(r, 'prem_noc'))
    gaps = [g(r, 'tau_noc') - g(r, 'tau_all') for r in ks]
    rat = [g(r, 'tau_noc') / g(r, 'tau_all') for r in ks]
    dev = max(abs(rr - 1 / (1 - g(r, 'carbon_share'))) for r, rr in zip(ks, rat))
    ad = [abs(g(r, 'd_tau_all')) for r in dl]
    nd = [abs(g(r, 'd_tau_noc')) for r in dl]
    V = dict(
        NYEARS=str(len(rows)), IDC=str(sum(1 for r in rows if abs(g(r, 'r_crop') - 1) < 1e-9
                                           and abs(g(r, 'r_built') - 1) < 1e-9)),
        NPIN=str(sum(1 for r in rows if abs(g(r, 'pmin_noc') - 365.0) < 1e-6)),
        DEV=f'{dev:.1e}', RLO=f'{min(rat):.2f}', RHI=f'{max(rat):.2f}',
        GAPMEAN=f'{sum(gaps)/len(gaps):.1f}', GAPLO=f'{min(gaps):.1f}', GAPHI=f'{max(gaps):.1f}',
        CSLO=f'{100*min(g(r, "carbon_share") for r in ks):.1f}',
        CSHI=f'{100*max(g(r, "carbon_share") for r in ks):.1f}',
        SPREAD=f'{max(abs(g(r, "tau_all") - g(r, "tau_all_national")) for r in ks):.1f}',
        SPREAD0=f'{max(abs(g(r, "tau_all") - g(r, "tau_all_national")) for r in ks):.0f}',
        DALLMEAN=f'{sum(ad)/len(ad):.1f}', DALLMAX=f'{max(ad):.1f}',
        DNOCMEAN=f'{sum(nd)/len(nd):.1f}', DNOCMAX=f'{max(nd):.1f}',
        FRAG=f'{(sum(nd)/len(nd))/(sum(ad)/len(ad)):.1f}',
        DN=str(sum(1 for i in range(1, len(rows)) if g(rows[i], 'prem_noc') < g(rows[i - 1], 'prem_noc'))),
        NSTEP=str(len(rows) - 1),
        DEC=', '.join(f'{k}s {sum(v)/len(v):.0f} d' for k, v in sorted(dec.items())),
        CHK=' · '.join(l.strip() for l in open(f'{A}/checksums.txt') if l.strip()),
    )
    for y in (1961, 1980, 2000, 2014):
        V[f'P{y}'] = f'{g(by[y], "prem_noc"):.0f}'
        V[f'A{y}'] = f'{g(by[y], "tau_all"):.1f}'
    tbl = ['| year | carbon share of demand | τ_agg, carbon in the ratio set | τ_agg, carbon demand excluded |'
           ' gap, d | restricted premium |', '|---|---:|---:|---:|---:|---:|']
    for y in (1961, 1980, 2000, *range(2005, 2015)):
        r = by[y]
        tbl.append(f'| {y} | {100*g(r,"carbon_share"):.1f}% | {g(r,"tau_all"):.1f} d | '
                   f'{g(r,"tau_noc"):.1f} d | {g(r,"tau_noc")-g(r,"tau_all"):.1f} d | '
                   f'{g(r,"prem_noc"):.1f} d |')
    V['TABLE'] = '\n'.join(tbl)
    return V, by


V, BY = stats()
print('run read: ' + ' | '.join(f'{k}={V[k]}' for k in ('NYEARS', 'IDC', 'NPIN', 'GAPMEAN', 'SPREAD', 'FRAG')))


def sub(t):
    for k, v in V.items():
        t = t.replace('@' + k + '@', v)
    assert '@' not in t, f'unsubstituted placeholder: {t[t.index("@"):t.index("@")+20]}'
    return t


# --------------------------------------------------------------------- the text, as templates with
# placeholders, held here so that no LaTeX backslash passes through a Python escape
REMARK = sub(r"""**Remark 37 (Two component ratios are identities at a world aggregate).** *On the world aggregate of the published accounts the restricted minimum $\tau_{\min}$ is 365 d in every year of the series, because the two components whose demand is the area itself --- cropland and built-up land --- have $b_i = d_i$ identically; the restricted premium is then the distance of the aggregate date past the year boundary, and its decline measures the dispersion of the three yield-based components around a level the accounts fix, not a convergence the ecosystem exhibits.* *Verification.* On the 2018 edition, $r_{\mathrm{crop}} = r_{\mathrm{built}} = 1$ exactly in @IDC@ of @NYEARS@ years and $\tau_{\min}^{\mathrm{NOC}} = 365$ d in @NPIN@ of @NYEARS@; over the last decade of that series the ratio $\tau_{\mathrm{agg}}^{\mathrm{NOC}}/\tau_{\mathrm{agg}}^{\mathrm{ALL}}$ equals $1/(1-s_{\mathrm{carbon}})$ to within @DEV@, where $s_{\mathrm{carbon}}$ is carbon's share of demand and runs between @CSLO@% and @CSHI@%. The computation is one weighted sum of the published component rows, and the record is the supplementary's S17. *Consequence.* A premium computed at a world aggregate and a premium computed on a country's own component table are not two readings of one ecological fact, because only at the aggregate level are two of the ratios pinned by the convention that prices world demand at world-average yields; the level at which the accounts were read belongs to the number the way a data vintage does, and Section 10.2's sensitivity sentence says so.""")

E1_OLD = ("on the world totals of the National Footprint and Biocapacity Accounts as tabulated by Lin et al. "
          "(2018), the 2022 aggregate ratio is $0.584$ of biocapacity to demand, so")
E1_NEW = ("on the world totals of the 2025 edition of the National Footprint and Biocapacity Accounts --- the "
          "edition whose series contains that year, since the release Lin et al. (2018) document runs from 1961 "
          "to 2014 --- the 2022 aggregate ratio is $0.584$ of biocapacity to demand, so")

E2_OLD = ("and that four-day difference is vintage and nowcasting rather than arithmetic. The figures are world "
          "totals, not any territory's.")
E2_NEW = sub("and that four-day difference is vintage, nowcasting and aggregation level rather than arithmetic. "
             "On the newest edition of the accounts that can be fetched without an account --- the 2018 edition, "
             "whose series ends in 2014 --- reading the publisher's world aggregate instead of summing the "
             "national rows moves that date by up to @SPREAD0@ d over the last decade of the release, while a "
             "whole edition step on a closed year moves it by at most @DALLMAX@ d. A gap of a few days is "
             "therefore evidence about neither the arithmetic nor the vintage alone: which level the accounts are "
             "aggregated at is a choice the reader makes, and on this release it is worth as much as an edition. "
             "The figures are world totals, not any territory's.")

E4_OLD = "The parameter tables of Section 2 are declared parameterizations. No other data were used."
E4_NEW = ("The overshoot-date arithmetic of Section 10.2 and Remark 33 is read off the component tables of the "
          "National Footprint and Biocapacity Accounts, whose current edition the publisher distributes free but "
          "behind registration. The two editions used for the sensitivity check recorded in the supplementary's "
          "S17 --- the 2018 edition, with series 1961 to 2014, and the 2017 edition, with series 1961 to 2013, "
          "both deposited by the publisher under CC BY-SA 4.0 --- are archived with the reproduction bundle, "
          "together with the checksums of the tables as read and the script that computes both conventions from "
          "them. The parameter tables of Section 2 are declared parameterizations. No other data were used.")

E5_OLD = "The scripts read no data other than the public products named in the data availability statement."
E5_NEW = ("A fourth script is deliberately not claimed: the overshoot-date recomputation that supports Remark 37 "
          "and the supplementary's S17 is archived as a separate analysis record beside the reproduction bundle, "
          "because the bundle's manifest scopes it to arithmetic on declared figures and forbids it from ingesting "
          "data. That record reads only the two edition tables named above, needs nothing beyond the standard "
          "library, prints the aggregation diagnostic Section 10.2 reports, and re-runs on a newer edition of the "
          "accounts by changing two file names rather than any line of arithmetic.")

NOTE_OLD, NOTE_NEW = ("with Remarks 33\u201336, so no label is repeated",
                      "with Remarks 33\u201337, so no label is repeated")

S17 = sub(r"""

## S17 · The overshoot-date recomputation, and what a gap of a few days is worth

*Added at v11, against main-text v40. This is the computation the companion commentary named as the one thing
standing between it and a full paper, and it changed two sentences of the article; it is recorded in full here
because the article keeps only its conclusions.*

**Data.** Two editions of the National Footprint and Biocapacity Accounts, chosen because they are the newest
ones obtainable without an account: the 2018 edition (series 1961–2014, the release Lin et al. (2018)
documents) and the 2017 edition (1961–2013), both deposited by the publisher under CC BY-SA 4.0. The current
edition is free but registration-gated, so the 2022 row quoted in the article's Remark 33 is not reproducible
from an open download, and that limitation is stated here rather than left for a reader to discover. The
checksums of the two tables as read: @CHK@

**Arithmetic.** Exactly the article's, on the publisher's `World` rows: component totals in gha for
`record ∈ {BiocapTotGHA, EFConsTotGHA}`, then $\tau_{\mathrm{agg}} = 365\sum_i b_i/\sum_i d_i$ and
$\Pi_\tau = \tau_{\mathrm{agg}} - 365\min_i(b_i/d_i)$, computed once with all six demand components (ALL, the
published convention, in which the carbon row's zero biocapacity forces the minimum ratio to 0 and the premium
to the whole date) and once with carbon demand removed from numerator and denominator and the weights
renormalised over the five components of positive biocapacity (NOC, the article's restricted set). No
interpolation, no model, no network, no third-party library.

**Results.** The 2018 edition, world aggregate, days of a 365-day year:

@TABLE@

Four findings, each reproducible from the table by inspection.

1. **The premium's downward trend survives the exclusion.** With carbon demand removed, the restricted premium
   on this release runs @P1961@ d (1961), @P1980@ d (1980), @P2000@ d (2000), @P2014@ d (2014); the decade
   means are @DEC@, with @DN@ of @NSTEP@ year-on-year changes negative. The article's series — 547, 346, 251,
   173 d, read off a later edition — carries the same sign and shape and sits 4–8% above this release on the
   shared years, which is a further instance of the point the article makes about vintages rather than a
   contradiction of it.
2. **The two conventions part by about a year, and by a known factor.** Over 2005–2014 the restricted date
   exceeds the published-convention date by @GAPMEAN@ d on average (@GAPLO@–@GAPHI@ d), a ratio of @RLO@ to
   @RHI@, and that ratio equals $1/(1-s_{\mathrm{carbon}})$ to within @DEV@, with $s_{\mathrm{carbon}}$ between
   @CSLO@% and @CSHI@%. Excluding carbon is not a refinement: it multiplies the reported date by two and a half.
3. **The restricted date is the fragile one.** From the 2017 to the 2018 edition the aggregate date moves by
   @DALLMEAN@ d on average and @DALLMAX@ d at most on a closed year, while the restricted date moves by
   @DNOCMEAN@ d on average and @DNOCMAX@ d at most — a factor of @FRAG@. The reason is structural: the excluded
   denominator is the smaller quantity, so an absolute revision in the non-carbon components is divided by less.
   A headline-versus-recomputed difference of a few days is inside that noise for the restricted date and
   outside it for the aggregate date, so which date a difference is about decides whether it deserves a sentence.
4. **Aggregation level accounts for as much as vintage does.** Reading the publisher's `World` row rather than
   summing the national rows moves the aggregate date by up to @SPREAD@ d over the last decade of the release;
   and summing them *including* the `World` row — the natural first attempt at a world total in a table that
   carries both, and the error this record exists to document — doubles both sides of every ratio, which leaves
   the number of Earths untouched and moves the date by about a week. A few-day disagreement between a published
   headline and a reader's own recomputation is therefore expected, and it is not primarily a matter of vintage.

**The identity the article's Remark 37 records.** $r_{\mathrm{crop}} = r_{\mathrm{built}} = 1$ exactly in @IDC@
of @NYEARS@ years, and $\tau_{\min}^{\mathrm{NOC}} = 365$ d in @NPIN@ of @NYEARS@: at a world aggregate the
footprint of a component whose demand *is* the area is priced at world-average yields, so biocapacity and
demand coincide by construction. The restricted minimum is thus not an observed convergence, and any reading of
the premium as the components coming together has to name the level at which it was computed.

**Reproducing and extending.** `analysis/nfa_tau/recompute_tau.py`, with the per-year outputs
`tau_by_year_2018edition.csv` and `tau_by_year_2017edition.csv`, the revision ledger `edition_delta.csv`, the
complete stdout `results.txt`, `checksums.txt`, the two tables as fetched under `source/` with a manifest
recording their retrieval commands and the hashes of the archive and its extracted member, and a `README.md`
recording the licence, the aggregation trap and the reason the current edition is not fetched. Re-running on a
newer edition is two file names, not a code change.
""")

# --------------------------------------------------------------------- apply
md = open(SRC).read()
TEX = open(SRC_T).read()
EDITS = []


def rep(name, old, new):
    """Apply one edit to both dialects. The tex side is searched in the corrected dialect first and in the
    inherited one second, because the paragraphs the inherited rule mangled are exactly those where the file's
    current tex does not match a faithful conversion of the md."""
    global md, TEX
    mo = pattern(to_tex_f(old)).search(TEX) or pattern(to_tex(old)).search(TEX)
    assert mo, f'{name}: tex anchor miss'
    mmd = pattern(old).search(md)
    assert mmd, f'{name}: md anchor miss'
    md = md[:mmd.start()] + new + md[mmd.end():]
    TEX = TEX[:mo.start()] + to_tex_f(new) + TEX[mo.end():]
    EDITS.append(dict(name=name, md=[[mmd.group(0), new]], tex=[[mo.group(0), to_tex_f(new)]]))


rep('E1-edition-attribution', E1_OLD, E1_NEW)
rep('E2-aggregation-level', E2_OLD, E2_NEW)
rep('E4-data-availability', E4_OLD, E4_NEW)
rep('E5-code-availability', E5_OLD, E5_NEW)
rep('E6-numbering-note', NOTE_OLD, NOTE_NEW)

def fix_italic(t):
    """m2t's italic rule refuses a `*` that directly follows the `**` closing a bold run, which is exactly
    how this article opens a remark's claim sentence. The literal asterisks left in the converted text are
    those spans, paired in order, so they are closed here rather than by loosening the general rule (which the
    rest of the document depends on)."""
    n = t.count('*')
    assert n and n % 2 == 0, f'unbalanced asterisks after conversion: {n}'
    segs = t.split('*')
    res = []
    for k, seg in enumerate(segs):
        if k % 2 == 0:
            res.append(seg)
        else:
            res.append('\\emph{' + seg + '}')
    return ''.join(res)


anchor = "### 10.3 Negative and boundary content is first-class"
i = md.index(anchor)
INS_M = REMARK + "\n\n"
md = md[:i] + INS_M + md[i:]
j = TEX.index('\\subsubsection{10.3 Negative')
b = TEX.rfind('\n\n', 0, j) + 2
RTEX = to_tex_f(REMARK)
assert '\\emph{' in RTEX and '*' not in RTEX, RTEX[:200]
INS_T = RTEX + "\n\n"
TEX = TEX[:b] + INS_T + TEX[b:]
assert md.count(INS_M) == 1 and TEX.count(INS_T) == 1, 'insertion not unique'
EDITS.append(dict(name='E3-remark-37', md=[['', INS_M]], tex=[['', INS_T]]))


# --------------------------------------------------------------------- E11/E12: the supplementary pointer, which
# still named v9 three revisions after that file stopped being the accompanying one --- the defect the underscore
# budget in the gate caught, since a path in prose cannot help but print its underscores.
rep('E11-supplementary-filename',
    "The accompanying file `paper3_supplementary_v9.md` carries:",
    "The accompanying file `paper3_supplementary_v11.md` carries:")
rep('E12-supplementary-enumeration',
    "and the worked exhibits of Sections 6.2, 6.5 and 10.1 with their reproduction record and the statement\ninventory extended to the new labels (S9).",
    "and the worked exhibits of Sections 6.2, 6.5 and 10.1 with their reproduction record and the statement\n"
    "inventory extended to the new labels (S9). What v39 folded out of the article is here rather than gone: the\n"
    "G3P basin-row provenance (S5.4), the identifiability and value records (S10, S11) and the registered\n"
    "template detail that left Sections 8.1 and 8.2 (S14 to S16). And S17, added with this revision, is the\n"
    "overshoot-date recomputation behind Remark 37, with the two edition tables it read named and hashed.")

# --------------------------------------------------------------------- E7: the stray emphasis, md side
# Theorem 13's closing sentence carries `no *interior* rest point` nested inside an italic span that runs to
# the end of the paragraph, which no markdown reader resolves consistently. The inner pair is the defect: the
# word needs no emphasis there, and the sentence already contrasts boundary and interior rest points in words.
E7_OLD = "With $E > 0$ constant, no *interior* rest point (with $N_* > 0$) exists (Theorem 12)"
E7_NEW = "With $E > 0$ constant, no interior rest point (with $N_* > 0$) exists (Theorem 12)"
def repm(name, old, new):
    """An md-only edit; the tex side of this paragraph is corrected by E8's re-conversion pass, which matches
    paragraphs by alphanumeric skeleton and so does not care that the current tex mangled the emphasis."""
    global md
    mmd = pattern(old).search(md)
    assert mmd, f'{name}: md anchor miss'
    md = md[:mmd.start()] + new + md[mmd.end():]
    EDITS.append(dict(name=name, md=[[mmd.group(0), new]], tex=[]))


repm('E7-nested-emphasis', E7_OLD, E7_NEW)

# --------------------------------------------------------------------- E8: re-convert the four paragraphs
# whose emphasis the inherited rule could not close. The set is enumerated rather than scanned: a whole-document
# scan against this builder's own copy of the converter flags 40 paragraphs, because the pipeline that produced
# the manuscript handled the prose rule correctly everywhere except where an emphasis span crosses inline math or
# opens directly after a bold run --- the two failure modes below --- and rewriting 205 or 40 paragraphs to
# adopt a second converter would be churn with no gain. Each replacement is guarded by an alphanumeric-skeleton
# test, so only markup can change, and the pairs are logged so the build reverses exactly.
E8_SITES = [
    'Fix a partition of the declared compartments into donor and recipient sides',   # Definition 40
    'Proposition 42 (No conservation law crosses a type class',                      # emphasis crosses math
    'Theorem 13 (Vanishing-extraction rest set',                                      # nested emphasis, E7
    'Proposition 43 (The institutional-failure subsystem is exactly closed',          # emphasis after bold
]
by_skel = {}
for tpara in re.split(r'\n\n+', TEX):
    if tpara.strip():
        by_skel.setdefault(skel(tpara), []).append(tpara)
E8PAIRS = []
for site in E8_SITES:
    m = pattern(site).search(md)
    assert m, f'E8: no md paragraph for {site[:40]}'
    a = md.rfind('\n\n', 0, m.start()) + 2
    b = md.find('\n\n', m.start())
    fixed = to_tex_f(md[a:b if b > 0 else len(md)])
    hits = [t for t in by_skel.get(skel(fixed), []) if t.count('*') > fixed.count('*')]
    assert len(hits) == 1, f'E8: {site[:40]} -> {len(hits)} stale tex paragraphs'
    E8PAIRS.append((hits[0], fixed))
for old_p, new_p in E8PAIRS:
    assert TEX.count(old_p) == 1, 'E8: stale tex paragraph not unique'
    TEX = TEX.replace(old_p, new_p, 1)
print(f'E8: reconverted {len(E8PAIRS)} paragraph(s), all guarded by skeleton equality')
print('    ' + ' | '.join(re.search(r'[A-Za-z][A-Za-z ,]{6,46}', o).group(0).strip() for o, _ in E8PAIRS))

# --------------------------------------------------------------------- E10: a dangling internal citation the
# pointer scan turned up. "Definition 19" has never been a label of this article (it is absent from every
# vintage in the line, and number 19 is occupied by Corollary 19); the joint programme it means is the one
# whose value Proposition 37 identifies as the exact threshold, in the same subsection.
rep('E10-dangling-citation',
    "and on the joint polytope exactness follows from Definition 19's\nprogramme",
    "and on the joint polytope exactness follows from Proposition 37's\njoint programme")

# --------------------------------------------------------------------- E9: two heading markers that an older
# splice of the Declarations block left as literal text, duplicating the \subsection commands already there.
HASH_FIXES = []
for h in ('Code availability', 'Declaration of competing interest'):
    stray = f'\\#\\# {h}'
    k = TEX.find(stray)
    assert k > 0, f'E9: {h} stray marker not found'
    a = TEX.rfind('\n', 0, k) + 1                      # start of the stray line
    b = TEX.find('\n\n', k) + 2                        # end of the blank line after it
    ctx = TEX[max(0, a - 60):a]                        # enough preceding text to make the pair unique
    old, new = ctx + TEX[a:b], ctx
    assert TEX.count(old) == 1, 'E9: removal is not uniquely locatable'
    TEX = TEX.replace(old, new, 1)
    HASH_FIXES.append((old, new))
assert '\\#\\#' not in TEX, 'a stray heading marker survived'
print('E9: removed duplicated markdown heading markers from the tex:', len(HASH_FIXES))
EDITS.append(dict(name='E9-heading-markers', md=[], tex=[list(x) for x in HASH_FIXES]))
SRC_TEX = open(SRC_T).read()
for k, a, b in (('labels', '\\label{', '\\label{'), ('refs', '~\\ref{', '~\\ref{'),
                ('environments', '\\begin{', '\\begin{')):
    assert TEX.count(a) == SRC_TEX.count(b), f'E8/E9 changed the count of {k}'

open(MD_OUT, 'w').write(md)
bad = sorted({c for c in TEX if ord(c) > 127})
unescaped = [m.start() for m in re.finditer(r'(?<!\\)\$', TEX)]
assert not bad and not unescaped, f'tex hygiene: {bad[:6]} {unescaped[:3]}'
open(TEX_OUT, 'w').write(TEX)
json.dump(EDITS + [dict(name='E8-reconvert-converter', md=[], tex=[list(x) for x in E8PAIRS])],
          open(LOG, 'w'), indent=1)

supp = open(SUPP_IN).read()
assert 'Proposition 42 states what no such check can buy' in supp and '## S16' in supp
open(SUPP_OUT, 'w').write(supp.rstrip('\n') + '\n' + S17)

print(f'article v40: {len(md)} B md, {len(TEX)} B tex, {len(md.split())} words (v39 {len(open(SRC).read().split())})')
print(f'supplementary v11: {len(supp)+len(S17)} words added {len(S17.split())}')
print('remark 37 present in md:', '**Remark 37' in md, '| in tex:', '\\textbf{Remark 37' in TEX,
      '| italics in tex:', TEX.count('\\emph{On the world aggregate'))
print('label check:', len(re.findall(r'\*\*(Theorem|Proposition|Definition|Lemma|Corollary|Remark|Algorithm)s? \d+', md)))
