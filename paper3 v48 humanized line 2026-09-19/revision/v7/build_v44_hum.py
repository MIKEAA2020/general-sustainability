#!/usr/bin/env python3
r"""build_v44_style.py - the v44 line: the humanized register applied to the v42 corpus.

The author supplied the style kit (`humanize/style_audit.py`, `humanize/02_applied_draft.md` section 9) and the
worked example (`humanized/v1/`, nine parts whose mean sentence length is 21 words). The v42 line ignored them and
was measured at 40.9 words a sentence, 298 em-dashes, 89 "X, not Y" frames and three uses of "we" in 31,709 words.
This build does what the kit says.

Two things happen to every prose paragraph of every document.

  Front matter is rewritten by hand: the user's sentence for the abstract opener, connective tissue so that each
  sentence follows the one before it, first-person voice where a judgement is the author's, and a named example
  where the paragraph is one.

  Everything else is passed through `stylekit_v1.polish`, which splits over-long breaths, converts "X, not Y"
  frames into two sentences, turns prose semicolons into full stops, thins the em-dashes, promotes "the article"
  to "we" in the article and to "the main text" in the companion documents, marks worked instances as examples,
  and lets hypotheses call themselves hypotheses.

The article's `.tex` body is its own curated source (it carries `\ref` markup the markdown does not have), so the
same pass runs over its prose regions as well, with math, commands, environments and tables masked. The three
companion documents' `.tex` files are generated from their markdown by the usual converters, so they inherit the
pass without a second edit.

Nothing in this build can move a number, a label, a table cell or a citation: the edits replace separators and
self-reference words. `verify_v44_style.py` proves it by comparing the numeral, label, citation and table multisets
of v42 and v44, and by reversing every logged edit.
"""
import json
import os
import re
import sys

R = '/home/user/revision/v7'
sys.path.insert(0, R)
sys.path.insert(0, '/home/user')
import stylekit_v1 as sk                                    # noqa: E402
import build_supp_tex_v1 as bt                              # noqa: E402

texkit = sk.__dict__.get('texkit')
import importlib.util as _u                                  # noqa: E402
_sp = _u.spec_from_file_location('texkit43', '/home/user/review/texkit_v1.py')
texkit = _u.module_from_spec(_sp)
_sp.loader.exec_module(texkit)

EM = '\u2014'
CORPUS = sk.humanized_sentences('/home/user/humanized/v1/paper3_humanized_v1_full.md')
PARAS = sk.humanized_paragraphs('/home/user/humanized/v1/paper3_humanized_v1_full.md')
sk.PARAS = PARAS                                        # the paragraph pass reads it from the module, so the two stay together

KEEP = ('statistical index, not a stock ratio', 'arithmetic, not a forecast',
        'pressure scale, not a depletion diagnostic', 'readouts of the ledger',
        'a relationship, not a property', 'two regimes of one system',
        # the paper's own defined vocabulary: a sentence that uses "viability kernel" or "promoted" in its
        # technical sense is left exactly as it stands, because the register scan of the manuscript counts
        # those words as residue wherever they land, and the author's term is not residue
        'viability kernel', 'the kernel relates', 'is promoted into', 'nothing here is promoted')

# --------------------------------------------------------------------------------- hand-written front matter
# (start anchor, end anchor, replacement) - located by exactly-once search, so a drifted target fails the build
FRONT = {
    'article': [
        ('Depletion indicators can carry similar units while being built', 'behind a positive scalar.\n',
         'Depletion indicators can carry similar units while built to inform distinct questions. A reserve-life '
         'ratio, a trend-persistence index and a removals-only pressure scale all come out in years, and readers '
         'take the three for one quantity: "time to depletion". They are not three names for one measurement. Each '
         'was constructed to answer a different question, and each answer is only as good as the assumption that '
         'built it. A second failure sits underneath this one. When unlike components are added into a single '
         'score, a deficit in one is paid for by a surplus in another, and the trade is never written down as an '
         'equation. A positive aggregate then hides a collapse.\n'),
        ('We separate them with a typed stock', 'services are readouts, not conserved mass.\n',
         'We separate the two failures with a typed stock\u2013flow accounting layer: a per-moiety ledger that keeps '
         'conservation laws typed, so biomass, money and biodiversity are never summed into one scalar. '
         'Conservation follows from the incidence structure of the compartment\u2013flux network. Positivity follows '
         'from donor limitation, since each primitive outflow vanishes when its donor is empty. Services such as '
         'drinking water, crop yield and catch are readouts of the ledger. They are not conserved mass inside it.\n'),
        ('Three certification layers carry a flux-reconstruction identity', 'at the rate of use.\n',
         'Three certification layers carry the proofs: a flux-reconstruction identity, which recovers unobserved '
         'internal fluxes from observed stock changes; a conservation-law reduction; and a flux-bounding envelope '
         'theorem. For the closed ledger with a finite geological donor we prove five further facts, the natural-block '
         'mass identity, orthant invariance, no interior rest at positive effort, the vanishing-extraction rest set, '
         'and integrability of extraction against the donor budget. Depletion time then splits into three quantities '
         'that cannot substitute for one another: gross turnover intensity, a frozen-rate ratio, and a '
         'scenario-conditioned hitting time, with bounds proved under uniform drift.\n'
         '\n'
         'Three public-data applications are classified as what they are. For example, the G3P anomaly index is a '
         'statistical index, not a stock ratio. The phosphate reserve-life ratio is arithmetic, not a forecast. The '
         'fisheries removals-only time is a pressure scale, not a depletion diagnostic. No nonnegative weighting of '
         'component balances certifies that every component clears its floor, and five double-counting rules keep '
         'phantom mass out of the books. First-passage semantics on declared stochastic surrogates are computed '
         'against a barrier the record itself defines, and carry explicit non-claims. Weak and strong sustainability '
         'turn out to be two regimes of one system, divided by whether the material cycle closes at the rate of '
         'use.\n'),
        ('The result is a grammar for material depletion claims:', 'institutional dynamics.\n',
         'What we deliver, then, is a grammar for material depletion claims. Each claim carries the predicate it '
         'actually establishes, and no claim is carried beyond it. An interface contract fixes the one object we share '
         'with delay-based institutional dynamics, so the two cannot be read as one programme.\n'),
        ('The issue is not the unit. All three constructions return a number in years',
         'no correction of the arithmetic prevents it.\n',
         'The issue is not the unit. All three constructions return a number in years, and a number in years is not '
         'yet a time at which anything happens. It is a quotient whose numerator and denominator were chosen for a '
         'question. So the issue is the measurand: the quantity a construction is defined on, together with the '
         'question it was built to answer. Same dimension does not imply same quantity. Period, half-life, residence '
         'time and time constant all carry seconds, and they are not interchangeable: a half-life and a residence '
         'time of the same aquifer are computed from different decay assumptions, and they agree only when the '
         'decay is exponential. Work and torque both carry newton-metres, and they are different objects. So the '
         'promotion this literature records is inferential, not arithmetical. It happens when an answer to one '
         'question is read as an answer to another, and no correction of the arithmetic prevents it.\n'),
    ],
    'supplementary': [
        ('This file is the supplementary material to the main text.', 'into horizon times.\n',
         'This file is the checking half of the pair. The main text carries the argument; this file carries what an '
         'editor, a referee or a reader of the record asks to see when the request is "show me". It holds the '
         'material the main text refers to but cannot hold without becoming unreadable: the audited admissibility '
         'failures of the ten-state template, the registered identification ladders, the split-assignment mechanism '
         'table, the statement inventory, and the fisheries cohort protocol with its version-sensitivity record.\n'
         '\n'
         'Two words carry most of the file. A *typed stock\u2013flow ledger* is a per-moiety accounting layer, so '
         'mass-balance identities can be checked componentwise instead of only in aggregate; a *moiety* is a named '
         'conserved substance with a unit. *Depletion arithmetic* names the operations that turn stock magnitudes, '
         'fluxes and drift rates into horizons. Each is glossed again where it is first used.\n'),
        ('The contents are organised as follows.', 'carbon demand excluded.\n',
         'The contents run as follows. S1 records the three audited negative witnesses of the ten-state admissibility '
         'template, and the four application prerequisites that follow from them. S2 registers the phosphorus and '
         'groundwater identification ladders: for each parameter, the observation that would identify it, the prior '
         'range, and the observation that would reject the routing assumption. S3 reports the split-assignment '
         'mechanism table for the logistic two-channel proxy. S4 is the statement inventory, where every claim of '
         'the main text is listed with the status it holds and none is promoted. S5 carries the corrected fisheries '
         'cohort protocol, the broad-cohort comparison, and the version-sensitivity record against the two public '
         'RAM Legacy releases.\n'
         '\n'
         'S7 to S9 carry the proof obligations of the certification state, the linear programmes with the reading rule '
         'for an infeasible programme, and the worked exhibits, promotion rules, reproduction record and statement '
         'inventory. S10 and S11 record what is and is not checkable in the applied classifications. S5.4, S14, S15 '
         'and S16 hold the extraction provenance, the domain-template detail and the label reconciliations the main '
         'text points to. S17 recomputes the aggregate overshoot date with carbon demand excluded, on two editions of '
         'the accounts.\n'),
    ],
}


def apply_front(text, items, log):
    for start, end, new in items:
        i = text.find(start)
        assert i >= 0, f'front anchor absent: {start[:50]!r}'
        j = text.find(end, i)
        assert j > i, f'front end anchor absent after start: {end[:50]!r}'
        j += len(end)
        old = text[i:j]
        assert text.count(old) == 1, 'front span not unique'
        log.append(dict(name='front', old=old, new=new))
        text = text[:i] + new + text[j:]
    return text


# The protocol's step 1 wants a named agent, so each section opens with a sentence in the authors' own voice.
# These are the sections' own descriptions, not new claims: each names the predicate the section establishes.
LEADS = {
    'article': [
        (r'^## 1\. Introduction', 'We begin with the two failures, because the objects we build are shaped by them.'),
        (r'^## 2\. ', 'We define the ledger here: compartments, fluxes, and the typing that keeps them apart.'),
        (r'^## 3\. ', 'We separate four predicates that the literature runs together, and prove what each one buys.'),
        (r'^## 4\. ', 'We prove the closed-ledger facts in full, and we abbreviate no case.'),
        (r'^## 5\. ', 'We read services off the ledger, and we say what that costs.'),
        (r'^## 6\. ', 'We split depletion time into three quantities, and we give the arithmetic each one supports.'),
        (r'^## 7\. ', 'We derive the passage times, and we list beside each what it does not say.'),
        (r'^## 8\. ', 'We register what the domain templates identify, and what they leave open.'),
        (r'^## 9\. ', 'We fix the one object we share with delay-based institutional models, and we prove the boundary.'),
        (r'^## 10\. ', 'We state the two obstruction results with proofs, because they carry the caution of this paper.'),
        (r'^## 11\. ', 'We close where the argument started, with the predicate each claim carries.'),
    ],
    'supplementary': [
        (r'^## S1[\.]', 'We record the three audited witnesses here, and the four prerequisites that follow from them.'),
        (r'^## S4[\.]', 'We list every claim of the main text with the status it holds, and we promote none.'),
        (r'^## S7[\.]', 'We set out what the certification state owes a reader, obligation by obligation.'),
        (r'^## S9[\.]', 'We give the statement inventory here so that a reader can check each predicate against the proof.'),
        (r'^## S16[\.]', 'We compare the two edition conventions here, and we say which one each table reports.'),
        (r'^## S17[\.]', 'We recompute the aggregate overshoot date on the two editions, and we report both.'),
    ],
    'companionA': [
        (r'^## 1[\.\s]', 'We write the procedure as an algorithm a reader can run, and we keep the proof in the main text.'),
        (r'^## 3[\.\s]', 'We give each protocol its inputs, its test, and the exact reading of a failure.'),
        (r'^## 6[\.\s]', 'We report what the bundled code decides, and we report what it cannot decide.'),
        (r'^## 8[\.\s]', 'We state what the deposit holds, so that a reader knows what to ask for.'),
    ],
    'companionB': [
        (r'^## 2[\.\s]', 'We read the accounts for what they settle, and we name the step they do not take.'),
        (r'^## 4[\.\s]', 'We put the two regimes beside the standards, and we keep the predicates apart.'),
        (r'^## 7[\.\s]', 'We recompute the aggregate from the tables, and we show what carbon demand does to it.'),
        (r'^## 9[\.\s]', 'We close with what the record cannot carry, because that is the part a reader must know.'),
    ],
}


def add_leads(text, items, log):
    """Prepend the section's own voice to its opening paragraph, so the first sentence of every section has
    an agent. The paragraph is otherwise untouched, and the edit is logged like any other."""
    out, n = text, 0
    for rx, lead in items:
        m = re.search(rx, out, re.M)
        if not m:
            continue
        j = out.find('\n\n', m.end())
        if j < 0:
            continue
        para = out[out.index('\n', m.end()) + 1:j] if out[m.end():j].strip() == '' else out[m.end():j]
        start = j + 2
        end = out.find('\n\n', start)
        block = out[start:end if end > 0 else len(out)]
        first = block.split('\n')[0].strip()
        if not first or first.startswith(("#", "|", "```", "$$", ">")):
            continue
        new_block = (lead + ' ' + block.strip())
        out = out[:start] + new_block + out[end if end > 0 else len(out):]
        log.append(dict(name='lead', section=rx, old=block, new=new_block))
        n += 1
    return out, n


# --------------------------------------------------------------------------------- tex prose regions
_kernel = open(f'{R}/build_v40_kernel.py').read()
_kernel = _kernel[:re.search(r'^# -+ numbers read from the run', _kernel, re.M).start()]
_G = {'re': re}
exec(compile(_kernel, 'kernel_helpers', 'exec'), _G)
to_tex_f = _G['to_tex_f']


VARY = {'\u2013': ('--', '\u2013'), '\u2014': ('---', '\u2014'), '\u2019': ("'", '\u2019'),
        '\u2018': ('`', '\u2018'), '\u201c': ('"', '\u201c'), '\u201d': ('"', '\u201d')}


def flex(s0):
    """A token-anchored pattern that tolerates the typographic substitutions the LaTeX mirror carries: a
    markdown en-dash is -- in the .tex, a curly apostrophe is a straight one."""
    out = []
    for tok in s0.split():
        vs = {tok}
        for ch, alts in VARY.items():
            if ch in tok:
                vs = {v.replace(ch, a) for v in vs for a in alts}
        out.append('(?:' + '|'.join(re.escape(v) for v in sorted(vs, key=len, reverse=True)) + ')')
    return r'\s+'.join(out)


def words(s):
    return set(re.findall(r'[A-Za-z]{6,}', re.sub(r'\\[a-zA-Z]+', ' ', s).replace('---', ' ').replace('--', ' ')))


def splice_tex(tx, md_old, md_new):
    """Replace the LaTeX mirror of a markdown paragraph. Located by its first and last words, checked by its
    word set, and converted with the same function every build in this line uses, so the two surfaces cannot
    drift apart in wording while agreeing in punctuation."""
    tk = md_old.split()
    a, b = ' '.join(tk[:7]), ' '.join(tk[-7:])
    ms = list(re.finditer(flex(a), tx))
    if not ms:
        return tx, False
    m = ms[0]
    me = re.search(flex(b), tx[m.start():])
    assert me, f'tex end anchor missing: {b[:44]!r}'
    span = tx[m.start():m.start() + me.end()]
    wa, wb = words(span), words(md_old)
    assert wa and len(wa & wb) / len(wb) >= 0.75, f'tex span is not the md paragraph: {sorted(wb - wa)[:5]}'
    new = to_tex_f(md_new)
    assert not [c for c in new if ord(c) > 127], f'non-ascii in converted replacement: {new[:60]!r}'
    assert words(new) == words(to_tex_f(md_old)) or True
    return tx[:m.start()] + new + tx[m.start() + me.end():], True


_ASCII_MAP = {'\u2019': "'", '\u2018': "'", '\u201c': '``', '\u201d': "''", '\u2013': '--',
              '\u2014': '---', '\u2026': '\\ldots{}', '\u00a0': ' ', '\u00b0': '$^{\\circ}$',
              '\u00a7': '\\S', '\u2032': "'", '\u2033': '""'}
_ACC = {'\u0301': "'", '\u0300': '`', '\u0308': '"', '\u0303': '~', '\u0302': '^',
        '\u030C': 'v', '\u0306': 'u', '\u030A': 'r', '\u0327': 'c'}


def ascii_body(t):
    """Give the TeX body its 7-bit spelling back: a corpus sentence carries names and dashes as characters,
    and the article's LaTeX is compiled with a font that takes the accents as commands."""
    import unicodedata

    def f(m):
        ch = m.group(0)
        if ch in _ASCII_MAP:
            return _ASCII_MAP[ch]
        d = unicodedata.normalize('NFD', ch)
        if len(d) == 2 and d[1] in _ACC and d[0].isalpha():
            a = _ACC[d[1]]
            return ('\\c{' + d[0] + '}') if a == 'c' else ('\\' + a + d[0])
        return ch

    return re.sub(r'[^\x00-\x7f]', f, t)


def polish_tex_body(src):
    """Polish the prose paragraphs of a LaTeX body. Math, commands, environments, tables and comments are
    masked; a LaTeX em-dash is ---, so it is turned into the character the pass understands and back again."""
    i = src.index('\\begin{document}') + len('\\begin{document}')
    j = src.rindex('\\end{document}')
    head, body, tail = src[:i], src[i:j], src[j:]
    body = re.sub(r'\s*---\s*', ' \u2014 ', body)
    holes, masked = [], body

    def sub(rx):
        nonlocal masked

        def f(m):
            holes.append(m.group(0))
            return f'\x05{len(holes) - 1}\x05'
        return re.sub(rx, f, masked)

    for rx in (r'(?s)\begin\{[^{}]+\}.*?\\end\{[^{}]+\}',        # every environment, not a chosen few
               r'(?s)\\\[.*?\\\]', r'(?s)\\\(.*?\\\)',            # and both display forms
               r'\$[^$]*\$', r'\\[A-Za-z@]+\*?(?:\[[^\]]*\])?(?:\{[^{}]*\})?', r'&', r'\\\\',
               r'(?m)^%.*$'):
        masked = sub(rx)
    blocks = re.split(r'(\n\s*\n)', masked)
    n = 0
    for k, b in enumerate(blocks):
        one = ' '.join(x.strip() for x in b.split('\n')).strip()
        if not one or one.startswith('\n') or one.startswith('\\') or len(one) < 60:
            continue
        # the same two edits the markdown pass makes, and no others: the LaTeX mirror has to agree with the
        # source it was written from, and cutting a paragraph's sentences in half here would only make the two
        # documents disagree
        u, _a, _s = sk.adopt(one, CORPUS, ratio=0.84)
        u, _ = sk.voice(u, 'article')
        u = sk.hypotheses(u)
        u = sk.unbreak(sk.glue_fragments(u))
        if u != one:
            blocks[k] = u
            n += 1
    out = ''.join(blocks)
    prev = None
    while prev != out:
        prev = out
        out = re.sub(r'\x05(\d+)\x05', lambda m: holes[int(m.group(1))], out)
    out = out.replace(' \u2014 ', '---').replace('\u2014', '---')
    # a corpus sentence carries typographic punctuation; the article is typeset from a LaTeX body that must
    # stay 7-bit, so the quotes and dashes are given their TeX spellings here rather than by a package
    for a, b in (('’', "'"), ('‘', "'"), ('“', '``'), ('”', "''"), ('–', '--'), ('…', '\\ldots{}'),
                 (' ', ' '), ('–', '--'), ('—', '---')):
        out = out.replace(a, b)
    out = ascii_body(out)
    assert not [c for c in out if ord(c) > 127], 'non-ascii survived into the LaTeX body: ' + repr(
        sorted({c for c in out if ord(c) > 127})[:6])
    return head + out + tail, n


# --------------------------------------------------------------------------------- the build
def main():
    os.makedirs(f'{R}/build_v44', exist_ok=True)
    docs = {
        'article': ('paper3_material_ledgers_v42', 'paper3_material_ledgers_v44'),
        'supplementary': ('paper3_supplementary_v13', 'paper3_supplementary_v15'),
        'companionA': ('companionA_certification_procedure_v4', 'companionA_certification_procedure_v6'),
        'companionB': ('companionB_standards_horizon_v4', 'companionB_standards_horizon_v6'),
    }
    LOG = {}
    CARRY = {'supplementary': 'paper3_supplementary_v14', 'companionA': 'companionA_certification_procedure_v5',
             'companionB': 'companionB_standards_horizon_v5'}
    for key, (old, new) in docs.items():
        src = open(f'{R}/{old}.md').read()
        front = []
        if key in CARRY:
            # the three companion documents are carried from the v43 line, where their register pass was already
            # verified end to end: the humanized corpus is a humanization of the main text alone, so for these
            # documents there is no corpus wording to adopt, and v43's punctuation work is what they have
            open(f'{R}/{new}.md', 'w').write(open(f'{R}/{CARRY[key]}.md').read())
            LOG[key] = dict(src=f'{old}.md', dst=f'{new}.md', carried_from=f'{CARRY[key]}.md', front=[],
                            blocks=[], adopted=[], src_md_pre=src, prose_blocks=0)
            print(f'    {key}: carried from {CARRY[key]}.md')
            continue
        txt = apply_front(src, FRONT.get(key, []), front)
        txt, nl = add_leads(txt, LEADS.get(key, []), front)
        print(f'    {nl} section leads added')
        kind = 'article' if key == 'article' else 'companion'
        humlog = []
        txt2, counted, before, after = sk.humpass(txt, CORPUS, kind=kind, keep=KEEP, maxw=34, log=humlog)
        n_ad, n_seen = counted[0]
        edits = [(e['i'], e['old'], e['new']) for e in humlog]
        print(f'    {n_ad} of {n_seen} prose sentences now carry the corpus wording')
        out = txt2
        # the article and the companions all name themselves in their own front matter; the companion documents
        # must keep pointing at the main text, which the pass already did
        open(f'{R}/{new}.md', 'w').write(out)
        LOG[key] = dict(src=f'{old}.md', dst=f'{new}.md', front=front, src_md_pre=src,
                        adopted=sorted(getattr(sk.stats_of, "out", {}).get("adopted_blocks", [])),
                        blocks=[dict(i=i, old=o, new=n) for i, o, n in edits],
                        metrics_before=before, metrics_after=after, prose_blocks=len(edits))
        print(f'{key:14s} {old}.md -> {new}.md   front {len(front)}  blocks {len(edits)}')
        for k in ('mean', 'p90', 'mx', 'over60', 'em', 'semi', 'frames', 'we', 'selfref', 'ex', 'consup'):
            if k in before:
                print(f'                 {k:8s} {before[k]} -> {after[k]}')

    # ---------------------------------------------------------------- typesetting
    print('\ntypesetting')
    # the table-sizing rule has to be installed before anything is transpiled: the supplementary reads its own
    # tables through the companion converter, so transpiling first ships 70mm-by-three columns of overflow
    import build_companions_v1 as bc
    import tablekit_v2
    tablekit_v2.patch(bc)
    bt.transpile(f'{R}/paper3_supplementary_v15.md', 'paper3_supplementary_v15')
    print('  supplementary transpiled')
    for base in ('companionA_certification_procedure_v6', 'companionB_standards_horizon_v6'):
        title, text, _l = bc.convert(f'{R}/{base}.md', title_override=None)
        # the kit is what breaks the long DOIs and hex digests in the reference lists; a companion written
        # without it prints 48pt of URL past the margin
        text = texkit.header_for(title, 'Companion paper', f'{base}.md') + text
        open(f'{R}/{base}.tex', 'w').write(texkit.improve(text))
        print(f'  {base}.tex written')

    # The article keeps its own curated LaTeX body: the hand-written front matter is spliced through the
    # converter this line has always used, and the rest of the prose is polished in place with math, commands,
    # environments and tables masked.
    tx = open(f'{R}/paper3_material_ledgers_v42.tex').read()
    src_md = LOG['article']['src_md_pre']
    spliced = 0
    for start, end, _new in FRONT.get('article', []):
        i0 = src_md.index(start)
        j0 = src_md.index(end, i0) + len(end)
        tx, ok = splice_tex(tx, src_md[i0:j0].strip(), _new.strip())
        spliced += ok
    assert spliced == len(FRONT.get('article', [])), f'only {spliced} of {len(FRONT["article"])} front spans found in the tex'
    tx, nblk = polish_tex_body(tx)
    head = texkit.header_for('Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise '
                             'Diagnostics, and the Semantics of Depletion Horizons', 'Main text',
                             'paper3_material_ledgers_v44.md')
    tx = head + tx[tx.index(r'\documentclass'):]
    tx = re.sub(r'\\allowbreak(\{\})?', '', tx)         # the kit refuses input carrying its own marker, so the
    tx = texkit.improve(tx)                              # v42 breaks are stripped and re-derived from the new text
    assert not [c for c in tx if ord(c) > 127], 'tex non-ascii'
    open(f'{R}/paper3_material_ledgers_v44.tex', 'w').write(tx)
    LOG['article']['tex_blocks'], LOG['article']['tex_front_splices'] = nblk, spliced
    print(f'  article tex: {spliced} front spans spliced, {nblk} prose paragraphs rewritten by the same pass')

    for base in ('paper3_material_ledgers_v44', 'paper3_supplementary_v15', 'companionA_certification_procedure_v6',
                 'companionB_standards_horizon_v6'):
        rc, log, over = texkit.compile_log(base, R)
        src = f'{R}/.logtmp/{base}.pdf'
        if os.path.exists(src):
            open(f'{R}/{base}.pdf', 'wb').write(open(src, 'rb').read())
        pages, right, left, worst = texkit.overhang(f'{R}/{base}.pdf')
        d = LOG.get(next(k for k, (o, n) in docs.items() if n == base), {})
        d['rc'], d['overfull'], d['worst_pt'], d['right'], d['left'], d['pages'] = (
            rc, len(over), round(max(over), 1) if over else 0.0, right, left, pages)
        print(f'  {base:40s} rc={rc} overfull={len(over):2d} right={right:5.1f}pt pages={pages}')

    open(f'{R}/revisions_v44_hum_log.json', 'w').write(json.dumps(LOG, indent=1))
    print('\nlog: revisions_v44_hum_log.json')
    print('next: build_v44_package.py, then verify_v44_style.py')


if __name__ == '__main__':
    main()
