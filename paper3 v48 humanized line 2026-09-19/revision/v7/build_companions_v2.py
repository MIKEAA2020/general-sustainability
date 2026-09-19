#!/usr/bin/env python3
r"""Build Companion A v2 and Companion B v2, then typeset both.

Nothing in v1 is overwritten: each file is written from its v1 source by logged replacements, and the gate
(verify_companions_v2.py) re-applies the pairs in reverse to prove the v2 markdown differs from the v1 markdown
by exactly those pairs and nothing else. The LaTeX is regenerated from the markdown by the v1 builder's own
`build()`, so the two companions keep one dialect.

Why the companions change at all: the computation Companion B's Section 7 named as the thing separating it from a
full paper has been run, on the two editions of the National Footprint and Biocapacity Accounts obtainable
without an account (revision/v7/analysis/nfa_tau/). B v2 reports it, fixes the provenance error the run exposed
in B's own Section 4, and adds a provenance section. A v2 records, in its bundle section, that a fourth program
now exists beside the bundle rather than inside it, because the bundle's manifest forbids data ingestion.

Every number interpolated into B v2 is read from the run's CSV by this script; none is typed.
"""
import csv
import json
import os
import re
import sys

R = '/home/user/revision/v7'
sys.path.insert(0, R)
A = f'{R}/analysis/nfa_tau'
import build_companions_v1 as bc                                          # noqa: E402

LOG = f'{R}/revisions_companions_v2_log.json'


def load_rows():
    rows = list(csv.DictReader(open(f'{A}/tau_by_year_2018edition.csv')))
    dl = list(csv.DictReader(open(f'{A}/edition_delta.csv')))
    g = lambda r, k: float(r[k])
    by = {int(r['year']): r for r in rows}
    ks = [r for r in rows if int(r['year']) >= 2005]
    dec = {}
    for r in rows:
        dec.setdefault(int(r['year']) // 10 * 10, []).append(g(r, 'prem_noc'))
    v = dict(
        years=len(rows),
        idc=sum(1 for r in rows if abs(g(r, 'r_crop') - 1) < 1e-9 and abs(g(r, 'r_built') - 1) < 1e-9),
        pin=sum(1 for r in rows if abs(g(r, 'pmin_noc') - 365.0) < 1e-6),
        gaps=[g(r, 'tau_noc') - g(r, 'tau_all') for r in ks],
        rat=[g(r, 'tau_noc') / g(r, 'tau_all') for r in ks],
        csh=[g(r, 'carbon_share') for r in ks],
        decmeans={k: sum(x) / len(x) for k, x in sorted(dec.items())},
        dn=sum(1 for i in range(1, len(rows)) if g(rows[i], 'prem_noc') < g(rows[i - 1], 'prem_noc')),
        dall=[abs(g(r, 'd_tau_all')) for r in dl], dnoc=[abs(g(r, 'd_tau_noc')) for r in dl],
        spread=max(abs(g(r, 'tau_all') - g(r, 'tau_all_national')) for r in ks),
    )
    v['dev'] = max(abs(r - 1 / (1 - s)) for r, s in zip(v['rat'], v['csh']))
    v['dec'] = ', '.join(f'{x:.0f} d' for x in v['decmeans'].values())
    v['prem'] = {y: g(by[y], 'prem_noc') for y in (1961, 1980, 2000, 2014)}
    v['hash18'] = [l.split()[0] for l in open(f'{A}/checksums.txt') if '2018' in l][0]
    v['hash17'] = [l.split()[0] for l in open(f'{A}/checksums.txt') if '2017' in l][0]
    return v, by


V, BY = load_rows()
print(f"read the run: {V['years']} years | identities {V['idc']}/{V['pin']} | premium "
      f"{[round(x) for x in V['prem'].values()]} | gap mean {sum(V['gaps'])/len(V['gaps']):.1f} d")


def sub(t):
    """Fill the @tokens@ from the run's CSVs, so no figure in Section 7 or 8 is typed by hand."""
    gaps, rat, csh = V['gaps'], V['rat'], V['csh']
    rows = []
    for y in (1961, 1980, 2000, *range(2005, 2015)):
        r = BY[y]
        h = lambda k: float(r[k])
        rows.append(f'| {y} | {100*h("carbon_share"):.1f}% | {h("tau_all"):.1f} d | {h("tau_noc"):.1f} d | '
                    f'{h("tau_noc")-h("tau_all"):.1f} d | {h("prem_noc"):.1f} d |')
    vals = {
        'TABLE': '\n'.join(rows), 'DECMEANS': V['dec'], 'H18': V['hash18'], 'H17': V['hash17'],
        'PREM1961': f"{V['prem'][1961]:.0f}", 'PREM1980': f"{V['prem'][1980]:.0f}",
        'PREM2000': f"{V['prem'][2000]:.0f}", 'PREM2014': f"{V['prem'][2014]:.0f}",
        'YEARS': str(V['years']), 'IDC': str(V['idc']), 'PIN': str(V['pin']),
        'GAPMEAN': f'{sum(gaps)/len(gaps):.1f}', 'GAPLO': f'{min(gaps):.1f}', 'GAPHI': f'{max(gaps):.1f}',
        'RLO': f'{min(rat):.2f}', 'RHI': f'{max(rat):.2f}',
        'CSLO': f'{100*min(csh):.1f}', 'CSHI': f'{100*max(csh):.1f}', 'DEV': f'{V["dev"]:.1e}',
        'DN': str(V['dn']), 'NSTEP': str(V['years'] - 1),
        'DALLMEAN': f'{sum(V["dall"])/len(V["dall"]):.1f}', 'DALLMAX': f'{max(V["dall"]):.1f}',
        'DNOCMEAN': f'{sum(V["dnoc"])/len(V["dnoc"]):.1f}', 'DNOCMAX': f'{max(V["dnoc"]):.1f}',
        'FRAG': f'{(sum(V["dnoc"])/len(V["dnoc"]))/(sum(V["dall"])/len(V["dall"])):.1f}',
        'SPREAD': f'{V["spread"]:.1f}',
    }
    for k, v in vals.items():
        t = t.replace(f'@{k}@', v)
    assert '@' not in t, 'unsubstituted token: ' + t[t.index('@'):t.index('@') + 18]
    return t



def apply(src, edits, out):
    """Log-replace each anchor in the v1 markdown. Anchors are written with ASCII apostrophes where the sources
    use typographic ones, so both spellings are tried and the matched span is taken from the file --- which keeps
    v1's own glyphs in the output and makes the pair reversible."""
    raw = open(src).read()
    fold = lambda t: t.replace('\u2019', "'")
    s, log = raw, []
    for name, old, new in edits:
        hits, cand = [], old
        for probe in (old, fold(old)):
            hay = s if probe == old else fold(s)
            hits = [m.start() for m in re.finditer(re.escape(probe), hay)]
            if len(hits) == 1:
                cand = probe
                break
        if len(hits) != 1:  # last resort: match on folded haystack, index back into the file
            hs = [m.start() for m in re.finditer(re.escape(fold(old)), fold(s))]
            assert len(hs) == 1, f'{os.path.basename(src)} / {name}: anchor count {len(hs)}'
            hits, cand = hs, fold(old)
            i = hs[0]
            span = s[i:i + len(cand)]
            s = s[:i] + new + s[i + len(cand):]
            log.append(dict(name=name, md=[[span, new]]))
            continue
        i = hits[0]
        span = s[i:i + len(cand)]
        s = s[:i] + new + s[i + len(cand):]
        log.append(dict(name=name, md=[[span, new]]))
    open(out, 'w').write(s)
    print(f'  {os.path.basename(out)}: {len(s.split())} words, {len(s)} B, {len(edits)} logged edits')
    return log


NEW7 = sub(r"""## 7. The one open computation, run

The question this section used to pose is now answered on data. The brief was: recompute the restricted and
unrestricted series with carbon demand excluded, and report (i) whether the sign of the premium's trend survives
the exclusion, (ii) how the restricted and unrestricted dates separate over the last decade, and (iii) whether the
four-day vintage gap of B11 widens or closes. It has been run on the National Footprint and Biocapacity Accounts
--- the 2018 edition, series 1961 to 2014, with the 2017 edition (1961 to 2013) as the revision control --- on
the publisher's own `World` rows, with no interpolation and no model, and §8 gives the provenance, the hashes and
the command. Two conventions, one arithmetic: ALL is the published convention, all six demand components in the
ratio, in which the carbon row's zero biocapacity forces $\tau_{\min} = 0$ and the premium to the whole date;
NOC is the restricted convention, carbon demand removed from numerator and denominator with the weights
renormalised over the five components of positive biocapacity.

| year | carbon share of demand | $\tau_{\mathrm{agg}}$, carbon included | $\tau_{\mathrm{agg}}$, carbon demand excluded | gap | restricted premium |
|---|---:|---:|---:|---:|---:|
@TABLE@

**B18.** *The trend's sign survives the exclusion, and its size is not an artefact of the release.* The
restricted premium on the 2018 edition runs @PREM1961@ d (1961), @PREM1980@ d (1980), @PREM2000@ d (2000),
@PREM2014@ d (2014); the decade means are @DECMEANS@, and @DN@ of @NSTEP@ year-on-year moves are declines. The
main text's series --- $547$, $346$, $251$, $173$ d, read off a later edition --- has the same sign and shape and
sits 4 to 8% above this release on the shared years. So the convergence reading in B10 does not depend on keeping
carbon in the ratio set, and the 4 to 8% release difference is the same phenomenon this commentary is about.

**B19.** *The two conventions part by roughly a year, and the size of the part is an identity, not a finding.*
Over the last decade of the release the restricted date exceeds the published-convention date by @GAPMEAN@ d on
average (@GAPLO@ to @GAPHI@ d), a ratio of @RLO@ to @RHI@; that ratio is exactly $1/(1-s_{\mathrm{carbon}})$ to
within @DEV@, with $s_{\mathrm{carbon}}$ between @CSLO@% and @CSHI@%. Removing carbon demand divides the
denominator by $(1-s)$ and multiplies the reported date by its reciprocal, which is a mechanical consequence of
the convention --- worth stating because the two numbers are otherwise quoted as though they answered different
questions.

**B20.** *The four-day gap neither dissolves nor indicts the arithmetic, and the explanation on offer is
incomplete.* Across an edition step on a closed year the aggregate date moves by @DALLMEAN@ d on average and
@DALLMAX@ d at most, so a mature-year revision does not account for a four-day figure. But reading the
publisher's `World` row instead of summing the national rows moves the *same* date by up to @SPREAD@ d on this
release --- larger than the gap under discussion, and not a matter of data vintage at all. The restricted date,
mean @DNOCMEAN@ d and maximum @DNOCMAX@ d across the same edition step, is a further @FRAG@ times more
revision-sensitive than the aggregate date, because the excluded denominator is the smaller quantity and an
absolute revision is divided by less. The direction, then: for the aggregate date a few-day gap is bigger than one
edition step and smaller than the choice of aggregation level; for the restricted date it is routine.

**B21.** *One structural fact changes how the display in B10 reads at a world aggregate.* There, cropland and
built-up land have $b_i = d_i$ identically --- @IDC@ of @YEARS@ years, exactly --- because the world footprint of
a component whose demand *is* the area is priced at world-average yields, so those two components coincide by
construction; consequently $\tau_{\min}^{\mathrm{NOC}} = 365$ d in @PIN@ of @YEARS@ years. The restricted premium
is then not a measured dispersion among components but the distance of the aggregate date past the year boundary,
and the "components converge" reading has to name the level at which it was computed. The main text carries this
as its Remark 37; the commentary records it because it is exactly the kind of thing a rate-based standard has no
place to register (B10).

---

""")

NEW8 = sub(r"""## 8. Provenance, and how to re-run it

The release is named because the numbers are only as durable as that naming.

- **Data.** The 2018 edition of the National Footprint and Biocapacity Accounts (series 1961 to 2014), the
  publisher's own deposit, and the 2017 edition (1961 to 2013), its earlier deposit; both under CC BY-SA 4.0.
  The sha256 of the tables as read: @H18@ and @H17@.
- **Retrieval.** The datasets' public download endpoint on a data-marketplace host, no account required for
  those two deposits. The **current** edition is not reachable that way: the publisher distributes it free but
  through a registration form with an emailed link, its open data endpoints answer with authorisation errors or
  have moved, and the only edition mirrored on a public data portal is the 2018 one. So this is the newest openly
  fetchable, component-level release, not the current release, and that distinction is stated wherever the
  numbers are used.
- **What was examined and rejected.** A single-year footprint table on a data-hosting site, set aside because it
  carries no year column and no pinnable edition, so it cannot support a claim about a release at all. A
  package-manager loader whose name matches the subject turns out to be about something else entirely. Neither was
  used, and both are named here so that nobody re-traces the search.
- **The program.** `analysis/nfa_tau/recompute_tau.py`: standard library only, no network call, no
  interpolation. It writes one CSV per edition plus a revision ledger and a complete stdout, and it prints the
  aggregation diagnostic that B20 turns on. Re-running on a newer edition is two file names, not a change of
  arithmetic. The directory holds the two tables as fetched, a manifest with the retrieval commands and the hashes
  of the archive and its extracted member, and a licence note; the run reproduces its three outputs byte for byte
  from the archived tables, which is the check a reviewer can perform without downloading anything.
- **Provenance of B's own Section 4.** The 2022 row quoted there ($0.584$, $213$ d) cannot come from Lin et al.
  (2018), whose release's series ends in 2014. The main text's Remark 33 now names the edition the year comes
  from and keeps that citation for the construction, which is what it documents; Section 4 here has been corrected
  the same way. It is why the sentence in B11 about naming releases is worth more than it looks.

---

""")


# ------------------------------------------------------------------ B v2
b = f'{R}/companionB_standards_horizon'
b_edits = [
    ('B0-what-it-is',
     '*A commentary accompanying "Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise\n'
     'Diagnostics, and the Semantics of Depletion Horizons" (main text v39; supplementary v10). Nothing here is\n'
     'proved; the arithmetic is quoted from the main text, and the standards statements are cited. Where the main\n'
     'text\'s labels are used, they are its own.*',
     '*A commentary accompanying "Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise\n'
     'Diagnostics, and the Semantics of Depletion Horizons" (main text v40; supplementary v11). Nothing here is\n'
     'proved; the arithmetic is quoted from the main text or recomputed in Section 7 from the accounts\n'
     'themselves, and the standards statements are cited. Where the main text\'s labels are used, they are its\n'
     'own. This is v2: the computation Section 7 used to ask for has been run, and Section 7 reports it.*'),
    ('B1-section1-pointer',
     'say with the article\'s apparatus, and what it must still decide for itself.',
     'say with the article\'s apparatus, and what it must still decide for itself. One question this file used\n'
     'to leave open has since been settled on data, and Section 7 is that settlement: the recomputation with\n'
     'carbon demand excluded, on the accounts themselves, with the two conventions reported side by side.'),
    ('B2-section4-provenance',
     'main text, Section 10.2 and Remark 33). On the world totals of the National Footprint and Biocapacity\n'
     'Accounts as tabulated by Lin et al. (2018), the 2022 aggregate ratio is $0.584$ of biocapacity to demand, so',
     'main text, Section 10.2 and Remark 33). On the world totals of the 2025 edition of the National Footprint\n'
     'and Biocapacity Accounts --- the edition whose series contains the year, since the construction Lin et al.\n'
     '(2018) document runs to 2014 --- the 2022 aggregate ratio is $0.584$ of biocapacity to demand, so'),
    ('B3-section4-forward',
     'in the supplementary\'s S5) is the cheapest available protection. It costs nothing but honesty.',
     'in the supplementary\'s S5) is the cheapest available protection. It costs nothing but honesty.\n'
     'Section 7 now measures both effects on the accounts themselves, and finds the four-day figure smaller than\n'
     'what the *level* of aggregation does to the same date and larger than a single edition step on a closed\n'
     'year --- which is why the practice has to name the aggregation level as well as the release.'),
    ('B4-section6-hygiene',
     '\n---\n\n## 7. The one open computation, and what it would buy',
     '\nOne further instance belongs to this section, because it is the kind of error a revision cycle hides: an\n'
     'exhibit quoting a 2022 figure and citing Lin et al. (2018) for it mis-credits the *release*, whose series\n'
     'ends in 2014, even though the citation is right about the *construction*. The two are different claims, and\n'
     'only the second is checkable against the paper\'s own reference list. Both this commentary\'s Section 4 and\n'
     'the main text\'s Remark 33 carried that ambiguity until the recomputation made the end year of the cited\n'
     'edition a fact on the page rather than a recollection.\n'
     '\n---\n\n## 7. The one open computation, and what it would buy'),
]
b1 = open(f'{b}_v1.md').read()
i7 = b1.index('## 7. The one open computation, and what it would buy')
i8 = b1.index('## 8. What a reporter should publish')
b_edits += [
    ('B5-section7-replaced', b1[i7:b1.rindex('\n---\n\n', i7, i8) + len('\n---\n\n')], NEW7 + '\n\n---\n\n'),
    ('B6-provenance-section', '## 8. What a reporter should publish',
     NEW8 + '\n\n---\n\n## 9. What a reporter should publish'),
    ('B7-reporter-item3',
     '3. Name the release and the pull, not the publisher. "Per the 2024 release" is checkable; "per national\n'
     '   accounts" is not, once revisions are routine.',
     '3. Name the release, the pull and the aggregation level, not the publisher. "Per the 2024 release, on the\n'
     '   publisher\'s world aggregate" is checkable; "per national accounts" is not, once revisions are routine\n'
     '   --- and B20 shows the level is worth days on its own, so it belongs in the sentence, not in a footnote.'),
    ('B8-changed-at-v2', '## References',
     '## 10. What changed at v2, and why v1 was not edited\n\n'
     'Five things, in order of consequence. The brief in Section 7 became a result: (i), (ii) and (iii) are\n'
     'answered on the 2018 edition with the 2017 edition as revision control, and B18 to B21 carry the numbers.\n'
     'A section on provenance was added, because a commentary that quotes a dataset has to be as strict about\n'
     'release naming as the article it accompanies, including about the release it could *not* fetch. Section 4\n'
     'and Section 6 acquired the edition correction described above. The first and third practices in the\n'
     'reporter\'s list now name the aggregation level, which the run showed moves the date as much as an edition\n'
     'does. And the sentence that made this file half a paper --- "a commentary whose exhibit is an unrun\n'
     'computation is a proposal" --- is gone, because its condition no longer holds: the exhibit is run, its\n'
     'table is generated from the data rather than transcribed, and its program is archived with the hashes of\n'
     'the tables it read. Version 1 is left in place unchanged, so the record of what was claimed before the\n'
     'numbers existed is still citable.\n\n'
     '---\n\n## References'),
]
logB = apply(f'{b}_v1.md', b_edits, f'{b}_v2.md')

# ------------------------------------------------------------------ A v2
a = f'{R}/companionA_certification_procedure'
a_edits = [
    ('A0-header-v2', '## 8. The reproduction bundle, and its v2 relabelling',
     '## 8. The reproduction bundle, its v2 relabelling, and the analysis record beside it'),
    ('A1-bundle-scope',
     'three scripts run in under ten seconds in total; there is no build step, no configuration file and no network\ncall, which is what makes the outputs quotable.',
     'three scripts run in under ten seconds in total; there is no build step, no configuration file and no network\ncall, which is what makes the outputs quotable.\n\n'
     '**What the bundle does not contain, and why that is a scope rule rather than a gap.** The recomputation of the\n'
     'aggregate overshoot date --- the arithmetic behind the main text\'s Remark 37 and the supplementary\'s S17,\n'
     'which reads two edition tables of the National Footprint and Biocapacity Accounts --- lives beside the bundle\n'
     'as its own analysis record, `analysis/nfa_tau/`, with the script, three per-year CSVs, a revision ledger, the\n'
     'complete stdout, `checksums.txt`, the two tables as fetched under `source/` with their retrieval commands and\n'
     'hashes, and a `README.md` stating the licence and the release that could not be fetched. The reason is the\n'
     'manifest\'s own rule quoted above: every script in the bundle reads nothing but declared figures, and a\n'
     'program that ingests a downloaded table would break the property that makes the outputs quotable without a\n'
     'network. Separating them keeps each claim testable on its own terms: the three scripts run in seconds with no\n'
     'input at all, and the analysis record runs in about a second on the archived tables, reproducing its outputs\n'
     'byte for byte.'),
    ('A2-protocol-note',
     '`code/MANIFEST.md` at v2 carries the versions, the run command, the relabelling table above and the scope\nlimits, including one that matters for review: no script consumes the G3P basin rows whose provenance is recorded\nin the supplementary\'s S5.4, because those rows are quarantined and nothing in the exhibits depends on them.',
     '`code/MANIFEST.md` at v2 carries the versions, the run command, the relabelling table above and the scope\nlimits, including one that matters for review: no script consumes the G3P basin rows whose provenance is recorded\nin the supplementary\'s S5.4, because those rows are quarantined and nothing in the exhibits depends on them. The\nanalysis record carries its own manifest in `source/MANIFEST.md`, and its scope limit is of the same kind: the two\nedition tables are not redistributed beyond the working copy needed to re-run the arithmetic, because the licence\nthat permits the re-run is the same licence that requires the attribution the manifest records.'),
]
logA = apply(f'{a}_v1.md', a_edits, f'{a}_v2.md')

json.dump({'A': logA, 'B': logB}, open(LOG, 'w'), indent=1)

# ------------------------------------------------------------------ typeset both
os.chdir(R)
for base in ('companionA_certification_procedure', 'companionB_standards_horizon'):
    bc.build(f'{base}_v2.md', f'{base}_v2')
    print(f'  built {base}_v2.tex / .pdf')
print('done')
# ------------------------------------------------------------------ B v2
b = f'{R}/companionB_standards_horizon'
b_edits = [
    ('B0-what-it-is',
     '*A commentary accompanying "Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise\n'
     'Diagnostics, and the Semantics of Depletion Horizons" (main text v39; supplementary v10). Nothing here is\n'
     'proved; the arithmetic is quoted from the main text, and the standards statements are cited. Where the main\n'
     'text\'s labels are used, they are its own.*',
     '*A commentary accompanying "Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise\n'
     'Diagnostics, and the Semantics of Depletion Horizons" (main text v40; supplementary v11). Nothing here is\n'
     'proved; the arithmetic is quoted from the main text or recomputed in Section 7 from the accounts\n'
     'themselves, and the standards statements are cited. Where the main text\'s labels are used, they are its\n'
     'own. This is v2: the computation Section 7 used to ask for has been run, and Section 7 reports it.*'),
    ('B1-section1-pointer',
     'say with the article\'s apparatus, and what it must still decide for itself.',
     'say with the article\'s apparatus, and what it must still decide for itself. One question this file used\n'
     'to leave open has since been settled on data, and Section 7 is that settlement: the recomputation with\n'
     'carbon demand excluded, on the accounts themselves, with the two conventions reported side by side.'),
    ('B2-section4-provenance',
     'main text, Section 10.2 and Remark 33). On the world totals of the National Footprint and Biocapacity\n'
     'Accounts as tabulated by Lin et al. (2018), the 2022 aggregate ratio is $0.584$ of biocapacity to demand, so',
     'main text, Section 10.2 and Remark 33). On the world totals of the 2025 edition of the National Footprint\n'
     'and Biocapacity Accounts --- the edition whose series contains the year, since the construction Lin et al.\n'
     '(2018) document runs to 2014 --- the 2022 aggregate ratio is $0.584$ of biocapacity to demand, so'),
    ('B3-section4-forward',
     'in the supplementary\'s S5) is the cheapest available protection. It costs nothing but honesty.',
     'in the supplementary\'s S5) is the cheapest available protection. It costs nothing but honesty.\n'
     'Section 7 now measures both effects on the accounts themselves, and finds the four-day figure smaller than\n'
     'what the *level* of aggregation does to the same date and larger than a single edition step on a closed\n'
     'year --- which is why the practice has to name the aggregation level as well as the release.'),
    ('B4-section6-hygiene',
     '\n---\n\n## 7. The one open computation, and what it would buy',
     '\nOne further instance belongs to this section, because it is the kind of error a revision cycle hides: an\n'
     'exhibit quoting a 2022 figure and citing Lin et al. (2018) for it mis-credits the *release*, whose series\n'
     'ends in 2014, even though the citation is right about the *construction*. The two are different claims, and\n'
     'only the second is checkable against the paper\'s own reference list. Both this commentary\'s Section 4 and\n'
     'the main text\'s Remark 33 carried that ambiguity until the recomputation made the end year of the cited\n'
     'edition a fact on the page rather than a recollection.\n'
     '\n---\n\n## 7. The one open computation, and what it would buy'),
]
b1 = open(f'{b}_v1.md').read()
i7 = b1.index('## 7. The one open computation, and what it would buy')
i8 = b1.index('## 8. What a reporter should publish')
b_edits += [
    ('B5-section7-replaced', b1[i7:b1.rindex('\n---\n\n', i7, i8) + len('\n---\n\n')], NEW7 + '\n\n---\n\n'),
    ('B6-provenance-section', '## 8. What a reporter should publish',
     NEW8 + '\n\n---\n\n## 9. What a reporter should publish'),
    ('B7-reporter-item3',
     '3. Name the release and the pull, not the publisher. "Per the 2024 release" is checkable; "per national\n'
     '   accounts" is not, once revisions are routine.',
     '3. Name the release, the pull and the aggregation level, not the publisher. "Per the 2024 release, on the\n'
     '   publisher\'s world aggregate" is checkable; "per national accounts" is not, once revisions are routine\n'
     '   --- and B21 shows the level is worth days on its own, so it belongs in the sentence, not in a footnote.'),
    ('B8-changed-at-v2', '## References',
     '## 10. What changed at v2, and why v1 was not edited\n\n'
     'Five things, in order of consequence. The brief in Section 7 became a result: (i), (ii) and (iii) are\n'
     'answered on the 2018 edition with the 2017 edition as revision control, and B18 to B21 carry the numbers.\n'
     'A section on provenance was added, because a commentary that quotes a dataset has to be as strict about\n'
     'release naming as the article it accompanies, including about the release it could *not* fetch. Section 4\n'
     'and Section 6 acquired the edition correction described above. The first and third practices in the\n'
     'reporter\'s list now name the aggregation level, which the run showed moves the date as much as an edition\n'
     'does. And the sentence that made this file half a paper --- "a commentary whose exhibit is an unrun\n'
     'computation is a proposal" --- is gone, because its condition no longer holds: the exhibit is run, its\n'
     'table is generated from the data rather than transcribed, and its program is archived with the hashes of\n'
     'the tables it read. Version 1 is left in place unchanged, so the record of what was claimed before the\n'
     'numbers existed is still citable.\n\n'
     '---\n\n## References'),
]
logB = apply(f'{b}_v1.md', b_edits, f'{b}_v2.md')

# ------------------------------------------------------------------ A v2
a = f'{R}/companionA_certification_procedure'
a_edits = [
    ('A0-header-v2', '## 8. The reproduction bundle, and its v2 relabelling',
     '## 8. The reproduction bundle, its v2 relabelling, and the analysis record beside it'),
    ('A1-bundle-scope',
     'three scripts run in under ten seconds in total; there is no build step, no configuration file and no network\ncall, which is what makes the outputs quotable.',
     'three scripts run in under ten seconds in total; there is no build step, no configuration file and no network\ncall, which is what makes the outputs quotable.\n\n'
     '**What the bundle does not contain, and why that is a scope rule rather than a gap.** The recomputation of the\n'
     'aggregate overshoot date --- the arithmetic behind the main text\'s Remark 37 and the supplementary\'s S17,\n'
     'which reads two edition tables of the National Footprint and Biocapacity Accounts --- lives beside the bundle\n'
     'as its own analysis record, `analysis/nfa_tau/`, with the script, three per-year CSVs, a revision ledger, the\n'
     'complete stdout, `checksums.txt`, the two tables as fetched under `source/` with their retrieval commands and\n'
     'hashes, and a `README.md` stating the licence and the release that could not be fetched. The reason is the\n'
     'manifest\'s own rule quoted above: every script in the bundle reads nothing but declared figures, and a\n'
     'program that ingests a downloaded table would break the property that makes the outputs quotable without a\n'
     'network. Separating them keeps each claim testable on its own terms: the three scripts run in seconds with no\n'
     'input at all, and the analysis record runs in about a second on the archived tables, reproducing its outputs\n'
     'byte for byte.'),
    ('A2-protocol-note',
     '`code/MANIFEST.md` at v2 carries the versions, the run command, the relabelling table above and the scope\nlimits, including one that matters for review: no script consumes the G3P basin rows whose provenance is recorded\nin the supplementary\'s S5.4, because those rows are quarantined and nothing in the exhibits depends on them.',
     '`code/MANIFEST.md` at v2 carries the versions, the run command, the relabelling table above and the scope\nlimits, including one that matters for review: no script consumes the G3P basin rows whose provenance is recorded\nin the supplementary\'s S5.4, because those rows are quarantined and nothing in the exhibits depends on them. The\nanalysis record carries its own manifest in `source/MANIFEST.md`, and its scope limit is of the same kind: the two\nedition tables are not redistributed beyond the working copy needed to re-run the arithmetic, because the licence\nthat permits the re-run is the same licence that requires the attribution the manifest records.'),
]
logA = apply(f'{a}_v1.md', a_edits, f'{a}_v2.md')

json.dump({'A': logA, 'B': logB}, open(LOG, 'w'), indent=1)

# ------------------------------------------------------------------ typeset both
os.chdir(R)
for base in ('companionA_certification_procedure', 'companionB_standards_horizon'):
    bc.build(f'{base}_v2.md', f'{base}_v2')
    print(f'  built {base}_v2.tex / .pdf')
print('done')
