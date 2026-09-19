#!/usr/bin/env python3
r"""v41 (article), v12 (supplementary), v3 (both companions): presentation, not content.

No measurement changes: no figure, no condition, no proof step and no scope statement is altered. Every span
removed narrates the corpus's own revision history --- version numbers, what an earlier draft printed, what a
reviewer asked, whether a computation had yet been run --- which is not part of a paper's argument. Two things are
added: the companion studies are cited, because they belong to the record this article speaks to, and the numbering
note states the convention instead of accounting for a revision. References are re-lettered 2026a-e because five
same-author-year works now exist.

Each edit is logged as an (old, new) pair per file, so that a gate can reverse the new file back to the old one
byte for byte and can prove that no removed span carries a numeral.
"""
import json
import os
import re
import subprocess
import sys

R = '/home/user/revision/v7'
sys.path.insert(0, R)

src = open(f'{R}/build_v40_kernel.py').read()                    # the article's own md -> tex converter
src = src[:src.index('# --------------------------------------------------------------------- numbers read from the run')]
G = globals()
exec(compile(src, 'v40helpers', 'exec'), G)
pattern, to_tex_f = G['pattern'], G['to_tex_f']

LOGS = {}
DASH, NDASH = '\u2014', '\u2013'


def flex(s):
    """Whitespace-flexible literal: how the corpus's own builder matches a span across re-wrapping."""
    return r'\s+'.join(map(re.escape, s.split()))


def cut(s, start, end):
    """The exact span of s from `start` through the end of `end`, both matched flexibly."""
    ms = list(re.finditer(flex(start), s))
    assert len(ms) == 1, f'start count {len(ms)} for {start[:44]!r}'
    me = re.search(flex(end), s[ms[0].start():])
    assert me, f'end {end[:44]!r} not found after start'
    return s[ms[0].start():ms[0].start() + me.end()]


def upto(s, start, end):
    """The span of s from `start` up to (not including) the first `end` after it."""
    ms = list(re.finditer(flex(start), s))
    assert len(ms) == 1, f'start count {len(ms)} for {start[:44]!r}'
    me = re.search(flex(end), s[ms[0].start():])
    assert me, f'end {end[:44]!r} not found after start'
    return s[ms[0].start():ms[0].start() + me.start()]


def apply_pairs(src_path, out_path, pairs, tag):
    """Logged md edits, applied in order, with a reversal log per file."""
    s = open(src_path).read()
    log = []
    for name, old, new in pairs:
        ms = list(re.finditer(flex(old), s))
        assert len(ms) == 1, f'{tag}/{name}: md anchor count {len(ms)}'
        s = s[:ms[0].start()] + new + s[ms[0].end():]
        log.append(dict(name=name, md=[ms[0].group(0), new],
                        md_spans=[[ms[0].start(), ms[0].group(0), new]]))
    open(out_path, 'w').write(s)
    LOGS[tag] = log
    print(f'  {os.path.basename(out_path)}: {len(s.split())} words, {len(log)} logged edits')
    return s


# ===================================================================== article v41
md0 = open(f'{R}/paper3_material_ledgers_v40.md').read()
ART = [
    ('N1-numbering-note',
     cut(md0, '(Numbering note: the two layering propositions', 'reconciled in its S6.)'),
     "(Numbering: the two layering propositions of this section carry their own counter, Propositions 1" + NDASH +
     "2. Every other numbered statement runs on one sequence shared by definitions, lemmas, propositions, "
     "theorems, corollaries and remarks, so each number belongs to exactly one statement and the kind name says "
     "which; the sequence reaches 47, and its maxima are Definition 47, Lemma 4, Proposition 43, Theorem 24 and "
     "Remark 37. The supplementary" + '\u2019'.join(['', 's']) + " statement inventory reconciles its status words "
     "with these labels in S6."),

    ('N2-supplementary-file',
     'The accompanying file `paper3_supplementary_v11.md` carries:',
     'The accompanying supplementary file carries:'),
    ('N3-supplementary-inventory',
     cut(md0, 'inventory extended to the new labels (S9).', 'named and hashed.'),
     "inventory extended to the later labels (S9); the extraction provenance of the G3P basin rows (S5.4); the\n"
     "per-parameter identifiability and value records (S10, S11); the registered template detail behind Sections\n"
     "8.1 and 8.2 at its full extent (S14 to S16); and the recomputation of the aggregate overshoot date reported\n"
     "in Remark 37, with the two editions of the accounts it reads named, licensed and hashed (S17)."),
    ('N4-remark33-tail',
     cut(md0, 'which is a statement about the construction rather than about any territory, and it is the one applied',
         'to state.'),
     'which is a statement about the construction rather than about any territory.'),
    ('N5-aggregation-clause',
     cut(md0, 'A gap of a few days is', 'as much as an edition.'),
     "A difference of a few days therefore discriminates\nneither the arithmetic nor the vintage on its own: the "
     "level at which the accounts are aggregated is a choice made in\nreading them, and on this release it moves "
     "the date by as much as an edition step."),
    ('N6-remark37-record',
     "The computation is one weighted sum of the published component rows, and the record is the supplementary's S17.",
     'The computation is a weighted sum of the published component rows, recorded in the supplementary (S17).'),
    ('N7-remark37-level',
     "the level at which the accounts were read belongs to the number the way a data vintage does, and Section "
     "10.2's sensitivity sentence says so.",
     'the level at which the accounts are read is part of the quantity, as Section 10.2 records.'),
    ('N8-code-availability',
     cut(md0, 'A fourth script is deliberately not claimed:', 'any line of arithmetic.'),
     "The overshoot-date recomputation reported in Remark 37 and in the supplementary (S17) is archived "
     "separately from the reproduction bundle, whose manifest restricts that bundle to arithmetic on declared "
     "figures and excludes data ingestion. It reads the two edition tables named in the data availability "
     "statement, requires nothing beyond the Python standard library, prints the aggregation diagnostic reported "
     "in Section 10.2, and reproduces its tabulated outputs from the archived copies of those tables; a newer "
     "edition of the accounts is run by supplying a different input file."),
    ('N9-cite-methods-companion',
     'Five rules, each carried by a proved or defined statement of this article, jointly prevent double counting '
     'and phantom mass:',
     'Five rules, each carried by a proved or defined statement of this article and specified as a checkable '
     'procedure in the companion methods study (Abaee, 2026d), jointly prevent double counting and phantom '
     'mass:'),
    ('N10-cite-commentary',
     'An aggregate overshoot date is therefore optimistic in a known direction, which is a statement about the '
     'construction rather than about any territory.',
     'An aggregate overshoot date is therefore optimistic in a known direction, which is a statement about the '
     "construction rather than about any territory; what this settles, and what it leaves open against the "
     'accounting standards, is taken up in the companion commentary (Abaee, 2026e).'),
    ('N11-reference-entries',
     cut(md0, 'Abaee, A., 2026. The limits of compensatory aggregation', 'Companion assessment-separation study.'),
     'Abaee, A., 2026c. The limits of compensatory aggregation: a formal separation of weak and strong '
     'sustainability assessment. Zenodo. https://doi.org/10.5281/zenodo.22545740. Companion '
     'assessment-separation study.\n\n'
     'Abaee, A., 2026d. Certifying a typed ledger: the predicates, the programmes, the vintages, and the '
     'reproduction bundle. Companion methods study, submitted with this article.\n\n'
     'Abaee, A., 2026e. What the accounts settle, and what they leave open: depletion as a cost of production, '
     'and the missing step from a rate to a horizon. Companion commentary, submitted with this article.'),
    ('N12-reference-letters',
     'Abaee, A., 2026. Delay-induced regime change',
     'Abaee, A., 2026a. Delay-induced regime change'),
    ('N17-merge-inventory',
     '(S5). At this revision it additionally carries the proof obligations attached to each entry',
     '(S5); the proof obligations attached to each entry', 1),
    ('N18-remark36-title',
     '**Remark 36 (What the type structure buys, and what it does not).**',
     '**Remark 36 (What the type structure yields, and what it does not).**', 1),
    ('N13-reference-letters',
     'Abaee, A., 2026. Periodic review as sampled governance',
     'Abaee, A., 2026b. Periodic review as sampled governance', 1),
    ('N14-in-text-letters', '(Abaee, 2026, doi:10.5281/zenodo.22554217',
     '(Abaee, 2026a, doi:10.5281/zenodo.22554217', 3),
    ('N15-in-text-letters', '(Abaee, 2026, doi:10.5281/zenodo.22554297',
     '(Abaee, 2026b, doi:10.5281/zenodo.22554297', 1),
    ('N16-in-text-letters', '(Abaee, 2026, doi:10.5281/zenodo.22545740',
     '(Abaee, 2026c, doi:10.5281/zenodo.22545740', 1),
]

# ===================================================================== supplementary v12
sup0 = open(f'{R}/paper3_supplementary_v11.md').read()
SUP = [
    ('T1-s17-scope',
     cut(sup0, '*Added at v11, against main-text v40.', 'keeps only its conclusions.*'),
     "*This section records the recomputation of the aggregate overshoot date with and without carbon demand, on\n"
     "two editions of the National Footprint and Biocapacity Accounts, with the data provenance, the arithmetic\n"
     "and the reproduction command in full; the main text carries its conclusions in Section 10.2 and Remark 37.*"),
    ('T2-s17-rerun',
     cut(sup0, 'Re-running on a', 'not a code change.'),
     'A newer edition of the accounts is run by\nsupplying a different input file; the arithmetic is unchanged.'),
    ('T3-s17-limitation',
     'from an open download, and that limitation is stated here rather than left for a reader to discover.',
     'from an open download, and the limitation is recorded here.'),
    ('T4-s17-error',
     'and the error this record exists to document ' + DASH + ' doubles both sides of every ratio',
     DASH + ' an error this section documents, which doubles both sides of every ratio'),
    ('T5-s17-material',
     'so which date a difference is about decides whether it deserves a sentence.',
     'so whether a difference of a few days is material depends on which date it concerns.'),
    ('T6-s17-excluding',
     'Excluding carbon is not a refinement: it multiplies the reported date by two and a half.',
     'Excluding carbon demand multiplies the reported date by a factor of two and a half rather than refining it.'),
    ('T7-heading', '## S5.4 ' + DASH.replace(DASH, '\u00b7') + ' G3P basin-row extraction provenance (demoted from main-text Section 6.5.2)',
     '## S5.4 \u00b7 G3P basin-row extraction provenance (the record behind main-text Section 6.5.2)'),
    ('T8-heading',
     '## S14 \u00b7 Registered domain-template detail (demoted from main-text Sections 8.1 and 8.2)',
     '## S14 \u00b7 Registered domain-template detail (the full extent behind main-text Sections 8.1 and 8.2)'),
    ('T9-heading', '## S10 \u00b7 Per-parameter identifiability status (main-text v39)',
     "## S10 \u00b7 Per-parameter identifiability status, with the main text's labels"),
    ('T10-heading', '## S11 \u00b7 Material and energy value: what is checkable, and what is not (main-text v39)',
     '## S11 \u00b7 Material and energy value: what is checkable, and what is not'),
    ('T11-heading', "## S16 \u00b7 S7's discharge column, restated against main-text v39",
     "## S16 \u00b7 S7's discharge column, restated against the main text's labels"),
    ('T12-heading', '## S9.4 \u00b7 Statement inventory at v33', '## S9.4 \u00b7 Statement inventory, extended form'),
]


SUP += [
    ('T13-contents',
     'Section S5 carries the corrected fisheries cohort protocol, the broad-cohort comparison, and the '
     'version-sensitivity record against the two public RAM Legacy releases.',
     'Section S5 carries the corrected fisheries cohort protocol, the broad-cohort comparison, and the '
     'version-sensitivity record against the two public RAM Legacy releases. Sections S7 to S9 carry the proof '
     'obligations of the certification state, the linear programmes with the reading rule for an infeasible '
     'programme, and the worked exhibits, promotion rules, reproduction record and statement inventory; S10 and '
     'S11 record what is and is not checkable in the applied classifications; S5.4, S14, S15 and S16 hold the '
     'extraction provenance, the domain-template detail and the label reconciliations the main text points to; '
     'and S17 records the recomputation of the aggregate overshoot date with carbon demand excluded.'),
    ('T14-part2', cut(sup0, '# Part II \u2014 additions at v9', 'the statement labels of S9.4 are the article' + chr(39) + 's own.'),
     "# Part II \u00b7 Certification obligations, programmes, and the statement inventory\n\n"
     "The three sections below hold the material the main text points to rather than carries: the proof "
     "obligations of the certification state (S7), the linear programmes of the closure-cone, deficit and "
     "critical-margin statements with the reading rule for an infeasible programme (S8), and the worked "
     "exhibits, promotion rules, reproduction record and extended statement inventory (S9). Section references "
     "are to the main text\u2019s numbering, and the statement labels are the main text\u2019s own."),
    ('T15-s94-intro',
     cut(sup0, 'Main counter 1\u201333, with the layering counter', 'an aggregate overshoot date) | 10.2 |'),
     "Main counter 1\u201347, with the layering counter (Propositions 1\u20132) separate, per \u00a73.1. Every "
     "statement numbered from 21 onward, with the section it sits in:"),
    ('T16-s94-unnumbered', 'Two unnumbered notes are added alongside them:',
     'Two unnumbered notes sit alongside the inventory:'),
    ('T17-part3', cut(sup0, '# Part III - additions at v10', 'the demoted passages verbatim.'),
     "# Part III \u00b7 Checkability records and the detail behind the applied sections\n\n"
     "The two tables below record what is and is not checkable in the applied classifications, and the records "
     "after them hold material the main text points to rather than carries: the extraction provenance of the "
     "G3P basin rows (S5.4, continuing the S5 record it belongs to), the registered domain-template ladders "
     "(S14, next to the S2 ladders they elaborate), and the proof-obligation row for `Typed` (S15, which cites "
     "the main text\u2019s Definition 47 in place of an undefined use of the word \u201ctyping\u201d). S5.4 and S14 "
     "give that material at its full extent."),
    ('T18-author-cells',
     cut(sup0, '`[author]` cells \u2014 **none**.', 'than a pull date.'),
     "No cell in these tables is left for the author to fill. Every row was read off the main text, the "
     "deposited repository at `refs/tags/edwards-framework-e1`, or a published source, and the cell that would "
     "otherwise have required the analysis repository is closed by the release identifier together with S5.1\u2019s "
     "row-level vintage check \u2014 a stronger claim than a pull date."),
    ('T19-s16-preamble',
     cut(sup0, 'Part II added S7 while the article was at v33', 'corrected in S15 rather than here.'),
     "Three of S7\u2019s \u201cdischarged by\u201d pointers name sections that no longer carry the statements they "
     "cite; none of the three is wrong in substance. The table below gives the labels to read against the main "
     "text as it stands, and the `Typed` row is corrected in S15 rather than here."),
    ('T20-s16-table-head', '| Entry | S7 says | Read this instead in v39 |', '| Entry | S7 says | Read this instead |'),
    ('T21-s15-deliver', 'Proposition 42 states what no such check can buy, namely a conservation law',
     'Proposition 42 states what no such check can deliver, namely a conservation law'),
    ('T22-s17-title', '## S17 \u00b7 The overshoot-date recomputation, and what a gap of a few days is worth',
     '## S17 \u00b7 The overshoot-date recomputation, and the significance of a difference of a few days'),
    ('T23-s6-preamble',
     cut(sup0, '*This section records the naming offset between this file', 'maps them to the main text' + chr(39) + 's\ncurrent labels.*'),
     "*This section records the naming offset between this file and the main text's statement labels: S1\u2013S5 "
     "carry the supplementary's own status words, and the table maps them to the main text's labels.*"),
    ('T24-s6-counter', 'The 1\u201320 counter carries the results in order of appearance',
     'The main counter carries the results in order of appearance'),
    ('T25-lead-in', 'This supplementary accompanies the main text.',
     'This file is the supplementary material to the main text.'),
]


# ===================================================================== companion A v3
a0 = open(f'{R}/companionA_certification_procedure_v2.md').read()
A3 = [
    ('A1-header',
     cut(a0, '*A methods companion to', 'supplementary v10).*'),
     '*A methods companion to "Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise\n'
     'Diagnostics, and the Semantics of Depletion Horizons", and to the companion commentary on the accounting\n'
     'standards (Abaee, 2026e).*'),
    ('A2-no-deliberately', 'It deliberately does', 'It does'),
    ('A3-declared-numbers',
     cut(a0, 'the bundled exhibits run on declared numbers, which is the whole point of', 'Section 8.'),
     'the bundled exhibits operate on declared numbers, which limits what they can\nestablish; Section 8 records '
     'that limitation.'),
    ('A4-section8-title',
     '## 8. The reproduction bundle, its v2 relabelling, and the analysis record beside it',
     '## 8. The reproduction bundle and the analysis record'),
    ('A5-run-command',
     '$ python3 revision/v7/code/certification_lp.py # and the other two, same directory',
     '$ python3 code/certification_lp.py # and the other two, from the top of the deposit'),
    ('A6-manifest-line',
     cut(a0, '`code/MANIFEST.md` at v2 carries the versions', 'for review:'),
     '`code/MANIFEST.md` records the script versions, the run command and the scope limits, one of which\n'
     'matters in review:'),
    ('A7-no-changelog',
     cut(a0, '**What v2 changed, and why nothing was overwritten.**', 'as exhibits:'),
     "**Deposited material is not edited in place.** A correction to a printed label or to a script ships as a new\n"
     "bundle, so that a reader holding any earlier deposit reproduces exactly what that deposit printed. The\n"
     "labels in the scripts and their outputs are those of the main text as it stands, and the build record asserts\n"
     "that a re-run matches the archived output line for line.\n\n"
     "The two tables the bundle prints are the ones quoted in the main text, and both are worth reading as\n"
     "procedures rather than as exhibits:"),
    ('A9-section9-title', '## 9. What the tool cannot buy', '## 9. What the tool cannot certify'),
    ('A10-cannot-deliver', 'states what no typing can buy ' + DASH + ' a',
     'states what no typing can deliver ' + DASH + ' a'),
    ('A11-specification',
     cut(a0, 'Two obligations are not currently checkable by anyone', 'rather than a silence.'),
     'Two obligations are not currently checkable from the archived material, the author included. What would\n'
     'make each checkable is stated here, so that the gap is a declared requirement rather than a silence.'),
    ('A12-software-note',
     cut(a0, 'stated in the scripts. The v2 changes are labels', 'all three scripts.'),
     'stated in the scripts.'),
    ('A13-availability',
     cut(a0, '## 11. Deposition, and what to hand to an editor', 'rather than shipped.'),
     "## 11. Availability of the deposited material, and its licence\n\n"
     "The article line and this companion are distinct works and are archived as separate records: the main text\n"
     "with its supplementary material, the `code/` reproduction bundle and the `analysis/nfa_tau/` record beside\n"
     "it are deposited with the article, and this companion carries a bundle of its own. Each record comprises, as\n"
     "files, the compiled PDF, the LaTeX source, the markdown source of record, the supplementary material where\n"
     "applicable, the code bundle and the output record. The licence of the underlying data does not transfer to\n"
     "the code and is not implied by it: the RAM Legacy release quoted here is CC-BY-4.0, which permits\n"
     "reproducing the four spot values of Section 7 with attribution and grants nothing over the archived extract\n"
     "itself, which is therefore described by its protocol rather than redistributed."),
    ('A14-code-availability-head', "**Code availability, in the form the main text's statement expects.**",
     '**Code availability.**'),
    ('A15-no-version-in-bundle', 'bundle `code/` at version 2, with', 'bundle `code/`, with'),
    ('A16-output-record', '(the run record is in Section 8)', '(the output record is in Section 8)'),
    ('A17-references',
     '\n---\n\n## Declarations\n\n**Funding.**',
     '\n---\n\n## References\n\nAbaee, A., 2026. Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics, and the Semantics of Depletion Horizons. Zenodo. https://doi.org/10.5281/zenodo.22554177.\n\nAbaee, A., 2026e. What the Accounts Settle, and What They Leave Open: Depletion as a Cost of Production, and the Missing Step from a Rate to a Horizon. Companion commentary, submitted with this article.\n\nRicard, D., Minto, C., Jensen, O.P., Baum, J.K., 2012. Examining the knowledge base and status of commercially exploited marine species with the RAM Legacy Stock Assessment Database. Fish and Fisheries 13, 380--398. https://doi.org/10.1111/j.1467-2979.2011.00435.x\n\n---\n\n## Declarations\n\n**Funding.**'),
]

# ===================================================================== companion B v3
b0 = open(f'{R}/companionB_standards_horizon_v2.md').read()
B3 = [
    ('B1-header',
     cut(b0, '*A commentary accompanying', 'Section 7 reports it.*'),
     '*A commentary accompanying "Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise\n'
     'Diagnostics, and the Semantics of Depletion Horizons", and the companion to the methods study on certifying\n'
     'a typed ledger (Abaee, 2026d). Nothing here is proved: the arithmetic is quoted from the main text or\n'
     'recomputed in Section 7 from the accounts themselves, and the standards statements are cited. Where the\n'
     "main text's labels are used, they are its own.*"),
    ('B2-no-counter', 'the companion carries no theorem counter, deliberately.',
     'the companion carries no theorem counter.'),
    ('B3-opening',
     cut(b0, 'A reviewer of the main text asked', 'defence:'),
     'The accounting standards now record depletion as a cost of production. A reader of the main text will ask\n'
     'whether that closes the gap the article opens, and the answer is a single sentence, which this commentary\n'
     'defends:'),
    ('B4-scope-of-section7',
     cut(b0, 'One question this file used', 'reported side by side.'),
     'Section 7 carries the recomputation of the aggregate overshoot date with carbon demand excluded, on the\n'
     'accounts themselves, with the two conventions reported side by side.'),
    ('B5-release-naming', 'is the cheapest available protection. It costs nothing but honesty.',
     'is the least costly protection available.'),
    ('B6-section7-opening',
     cut(b0, 'The question this section used to pose is now answered on data.', 'It has been run on'),
     'This section reports the restricted and unrestricted series recomputed with carbon demand excluded, to\n'
     "answer three questions: whether the sign of the premium's trend survives the exclusion; how far the\n"
     'restricted and unrestricted dates separate over the last decade; and whether the four-day difference\n'
     'recorded in B11 widens or closes as the accounts are read. The arithmetic is run on'),
    ('B7-no-criticism', 'This is not a criticism of the standard. A statistical standard must classify',
     'A statistical standard must classify'),
    ('B8-release-practice',
     cut(b0, 'It is why the sentence in B11 about naming releases is worth', 'more than it looks.'),
     'This is the specific reason for the release-naming practice of B11.'),
    ('B9-download-check',
     cut(b0, 'the run reproduces its three outputs byte for byte', 'downloading anything.'),
     'a re-run reproduces its three outputs byte for byte from the archived\ncopies, a verification that requires '
     'no download.'),
    ('B10-section5-title',
     '## 5. Two things a standard cannot buy, and a third it should not be asked for',
     '## 5. Two things a standard cannot supply, and a third it should not be asked to supply'),
    ('B11-aggregation-practice', 'which is why the practice has to name the aggregation level as well as the release.',
     'so the practice of naming a release has to name the aggregation level with it.'),
    ('B12-reporter-item',
     "and B21 shows the level is worth days on its own, so it belongs in the sentence, not in a footnote.",
     "and B21 measures the level's contribution in days, so it belongs in the same sentence as the release."),
    ('B13-vintage-corrected',
     cut(b0, "The main text's Remark 33 now names the edition", 'corrected the same way.'),
     'The main text\u2019s Remark 33 names the edition the year comes from and keeps that citation for the '
     'construction it documents.'),
    ('B14-no-changelog',
     (_b14 := upto(b0, '## 10. What changed at v2, and why v1 was not edited', '## References')),
     _b14[_b14.rindex('---'):]),
    ('B15-references',
     '## References\n\nGlobal Footprint Network, 2021.',
     '## References\n\nAbaee, A., 2026. Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics, and the Semantics of Depletion Horizons. Zenodo. https://doi.org/10.5281/zenodo.22554177.\n\nAbaee, A., 2026d. Certifying a Typed Ledger: The Predicates, the Programmes, the Vintages, and the Reproduction Bundle. Companion methods study, submitted with this commentary.\n\nGlobal Footprint Network, 2021.'),
]

ART = [e if len(e) >= 4 else (e[0], e[1], e[2], 1) for e in ART]
ART = [e if len(e) == 5 else e + (None,) for e in ART]
for n, e in enumerate(ART):                      # the tex renders the numbering note with `` '' quotes and a
    if e[0] == 'N1-numbering-note':               # stray space before a semicolon, so its span is located by hand
        ART[n] = e[:4] + (('(Numbering note: the two layering propositions', 'reconciled in its S6.)'),)

if __name__ == '__main__':
    os.chdir(R)
    print('\narticle: v40 -> v41')
    md = open(f'{R}/paper3_material_ledgers_v40.md').read()
    tx = open(f'{R}/paper3_material_ledgers_v40.tex').read()
    log = []
    for name, old, new, cnt, ovr in ART:
        ms = list(re.finditer(flex(old), md))
        assert len(ms) == cnt, f'article/{name}: md anchor count {len(ms)} != {cnt}'
        md_spans = []
        for m in reversed(ms):
            md_spans.append([m.start(), m.group(0), new])
            md = md[:m.start()] + new + md[m.end():]
        if ovr:
            m1 = re.search(flex(ovr[0]), tx)
            assert m1, f'{name}: tex start miss'
            m2 = re.search(flex(ovr[1]), tx[m1.start():])
            assert m2, f'{name}: tex end miss'
            ts = [type('Span', (), {})(), ]
            ts[0].rng = (m1.start(), m1.start() + m2.end(), tx[m1.start():m1.start() + m2.end()])
        else:
            pass
            po = pattern(to_tex_f(old))                    # the same text in the manuscript's tex dialect
            ts = list(po.finditer(tx))
            assert len(ts) == cnt, f'article/{name}: tex anchor count {len(ts)} != {cnt}'
        nt = 'The accompanying supplementary file carries:' if name == 'N2-supplementary-file' else to_tex_f(new)
        spans = [m.rng if hasattr(m, 'rng') else (m.start(), m.end(), m.group(0)) for m in ts]
        tex_spans = []
        for i, j, txt in reversed(spans):
            tex_spans.append([i, txt, nt])
            tx = tx[:i] + nt + tx[j:]
        log.append(dict(name=name, md=[ms[0].group(0), new], md_spans=md_spans,
                        tex=[spans[0][2], nt], tex_spans=tex_spans, count=cnt))
    open(f'{R}/paper3_material_ledgers_v41.md', 'w').write(md)
    bad = sorted({c for c in tx if ord(c) > 127})
    assert not bad, f'tex non-ascii {bad[:5]}'
    assert not [m for m in re.finditer(r'(?<!\\)\$', tx)], 'stray $ in tex'
    open(f'{R}/paper3_material_ledgers_v41.tex', 'w').write(tx)
    LOGS['article'] = log
    print(f'  article md {len(md.split())} words, tex {len(tx)} B, {len(log)} edits')

    print('\nsupplementary: v11 -> v12')
    lab = re.compile(r'^\*\*(Definition|Lemma|Proposition|Theorem|Corollary|Remark)\s+(\d+)\s*\((.*?)\)\.\*\*')
    secx = re.compile(r'^#{2,5}\s+([0-9]+(?:\.[0-9]+)*)')
    sec, rows = '', []
    for line in md.split('\n'):
        ms = secx.match(line)
        if ms:
            sec = ms.group(1)
        m = lab.match(line)
        if m and 21 <= int(m.group(2)) <= 47:
            rows.append((int(m.group(2)), f'{m.group(1)} {m.group(2)} ({m.group(3)})', sec))
    rows.sort()
    assert len(rows) >= 30, f'S9.4 regenerated rows {len(rows)}'
    for must in ('Definition 21 (Closure cone)', 'Theorem 24 (Critical-margin budget)',
                 'Proposition 32 (Boundedness of the persistence index on the declared trend class)',
                 'Remark 33 (One-signed bias of an aggregate overshoot date)'):
        assert any(t == must for _, t, _ in rows), f'S9.4 dropped {must}'
    assert any(t.startswith('Definition 47') for _, t, _ in rows), 'S9.4 misses the last definition'
    table = ('| Label | Section |\n|---|---|\n' +
             '\n'.join(f'| {t} | {s2} |' for _, t, s2 in rows))
    for e in SUP:
        if e[0] == 'T15-s94-intro':
            SUP[SUP.index(e)] = (e[0], e[1], e[2] + '\n\n' + table)

    apply_pairs(f'{R}/paper3_supplementary_v11.md', f'{R}/paper3_supplementary_v12.md', SUP, 'supplementary')

    import build_companions_v1 as bc
    print('\ncompanion A: v2 -> v3')
    apply_pairs(f'{R}/companionA_certification_procedure_v2.md', f'{R}/companionA_certification_procedure_v3.md',
                A3, 'companionA')
    print('\ncompanion B: v2 -> v3')
    apply_pairs(f'{R}/companionB_standards_horizon_v2.md', f'{R}/companionB_standards_horizon_v3.md', B3,
                'companionB')
    json.dump(LOGS, open(f'{R}/revisions_v41_formal_log.json', 'w'), indent=1)

    print('\ncompiling')
    r = subprocess.run(['/home/user/tools/tectonic', 'paper3_material_ledgers_v41.tex', '-o', '.'], cwd=R,
                       capture_output=True, text=True, timeout=1200)
    print('  article pdf:', 'ok' if r.returncode == 0 else (r.stdout + r.stderr)[-600:])
    for base in ('companionA_certification_procedure_v3', 'companionB_standards_horizon_v3'):
        bc.build(f'{base}.md', base)
    print('\ndone: run verify_v41_formal.py')
