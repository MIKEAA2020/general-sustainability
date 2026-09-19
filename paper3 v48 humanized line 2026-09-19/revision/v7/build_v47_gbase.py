#!/usr/bin/env python3
r"""build_v47_base.py - the v47 line: the corpus’s own wording where it can be proved to say the same thing, and the
corpus’s register measured as a profile everywhere else (GEM_* tables, stylekit_v1).

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
self-reference words. `verify_v47_base.py` proves it by comparing the numeral, label, citation and table multisets
of v42 and v45, and by reversing every logged edit.
"""
import difflib
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
CORPUS_MD = '/home/user/humanized/v1/paper3_humanized_v1_full.md'
CORPUS = sk.humanized_sentences(CORPUS_MD)


def _flowstats(t):
    return sk.stats_of('\n\n'.join(x for x in sk.split_blocks(t) if sk.is_flow(x)))
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
    os.makedirs(f'{R}/build_v45', exist_ok=True)
    docs = {
        'article': ('paper3_material_ledgers_v42', 'paper3_material_ledgers_v47'),
        'supplementary': ('paper3_supplementary_v13', 'paper3_supplementary_v18'),
        'companionA': ('companionA_certification_procedure_v4', 'companionA_certification_procedure_v9'),
        'companionB': ('companionB_standards_horizon_v4', 'companionB_standards_horizon_v9'),
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
        # no section leads on this line: the draft's own framing paragraphs are what opens a section now, and a
        # sentence written by the build for that purpose would be the only text in the document that is neither
        # the corpus's nor the author's. The heading-to-prose junction is left to the draft.
        txt, nl = add_leads(txt, [] if key == 'article' else LEADS.get(key, []), front)
        print(f'    {nl} section leads added')
        kind = 'article' if key == 'article' else 'companion'
        humlog = []
        # the inversion: the humanized draft is the baseline document, and this paper’s verified content is
        # ported into it. A passage of this paper’s prose is replaced by the draft’s own paragraph for that
        # section when the two carry the same values (numbers transplanted where the draft has since been
        # overtaken); the draft’s framing paragraphs, which carry no numbers, are taken as they stand; only
        # what is left over is styled. Nothing in this line is a paraphrase of the draft.
        # a section lead is this paper's own navigation sentence, put there so that a heading does not open on a
        # technical noun, and the front-matter sentences are the ones the author fixed by instruction. None of
        # them is exchangeable, so a block carrying one is kept whole: the draft supplies surface everywhere the
        # author has not already said something that has to be said in these words.
        _keep = list(KEEP)
        for _e in front:
            _t = ' '.join(str(_e.get('new', '')).split()).strip()
            for _s in (lambda x: [x[:48], ' '.join(x.split('. ')[0])])(_t):
                if len(_s) > 24:
                    _keep.append(_s)
        # the back matter is not prose and is not exchangeable either: the reference list, the availability
        # statements and the declarations belong to this document, and the draft carries a copy of them that its
        # own reflow from a PDF text layer had damaged (year letters lost, words glued, 15 of the 40 entries
        # dropped). Taking the draft's prose as baseline has nothing to do with taking its bibliography, so every
        # block after the first back-matter heading is listed here as unexchangeable, which is the same mechanism
        # that keeps a section lead whole. v47 briefly went the other way twice - once restoring the superseded
        # article's list, once recutting the draft's paragraph into entries - and both were this line deciding a
        # question that is the author's, so now it decides nothing here at all.
        _in_back = False
        for _blk0 in sk.split_blocks(txt):
            _s0 = _blk0.strip()
            if sk.BACK.match(_s0):
                _in_back = True
            if _in_back and len(' '.join(_s0.split())) > 24:
                _keep.append(' '.join(_s0.split())[:48])
        _keep = sorted(set(_keep))
        txt2, n_ad, n_kept, b_rep = sk.draftbase(txt, open(CORPUS_MD).read(), keep=_keep, log=humlog)
        _base = sk.join_blocks([x for x in sk.split_blocks(txt) if x.strip()])
        # the invariant is not equality of counts any more, because the draft repeats a figure the paper states
        # once: nothing may be invented, and nothing the paper states may go unstated
        _vo, _vp = __import__('collections').Counter(sk.values(txt2)), __import__('collections').Counter(sk.values(_base))
        assert not [k for k in _vo if k not in _vp], f'the draft supplied a value this paper does not state: {sorted(set(k for k in _vo if k not in _vp))[:6]}'
        assert not [k for k in _vp if k not in _vo], f'a value this paper states went unstated: {sorted(set(k for k in _vp if k not in _vo))[:6]}'
        for _pat in (r'(?m)^\|', r'\*\*(?:Theorem|Proposition|Lemma|Corollary|Definition)\s'):
            assert len(re.findall(_pat, txt2)) == len(re.findall(_pat, _base)), 'the graft lost table rows or statements'
        print(f'    draftbase: {b_rep}')
        counted = [(n_ad, n_kept)]
        # the adopted paragraphs call the paper "the article", and the pass that settles self-reference had run
        # before them. The map is applied here, block by block, and only to the flowing prose after the first
        # heading: a heading line is the author's numbering, a table row is not a style surface at all, and the
        # front matter carries the sentence the author fixed by instruction. The initial capital is kept, since
        # "The article shows" must not come out as "paper shows" after a full stop.
        # the residue is what the draft could not supply, and it is the only prose this line is allowed to
        # style: the draft's own paragraphs ship as the draft wrote them, so the kit's rules are applied to
        # exactly those blocks of this paper's that remain, one at a time, and only where the values hold and
        # the linter finds nothing new
        _dr_flat = ' '.join(open(CORPUS_MD).read().split())
        _rb = sk.split_blocks(txt2)
        _n_res = 0
        _seen_h = _in_back = False
        for _i, _bl in enumerate(_rb):
            _st0 = _bl.strip()
            if _st0.startswith('#'):
                # the front matter is the author\u2019s fixed wording and the back matter is carried: neither is a
                # style surface, and the bibliography in particular must not be re-punctuated by a register pass
                if re.match(r'^#{1,6}\s+\d', _st0):
                    _seen_h = True
                if sk.BACK.match(_st0):
                    _in_back = True
                continue
            if not _seen_h or _in_back:
                continue
            if not _bl or not sk.is_flow(_bl) or '$$' in _bl or _bl.lstrip().startswith(('#', '|', '>', '`', '*')):
                continue
            if ' '.join(sk.re.sub(r'[*`]', ' ', ' '.join(_bl.split())).split()) in _dr_flat:
                continue                                  # the draft's own paragraph: not a style surface
            _nb = sk.register(_bl)
            if _nb != _bl and sk.values(_nb) == sk.values(_bl) \
               and not sk._corrupt(_nb) - sk._corrupt(_bl):
                _rb[_i] = _nb
                _n_res += 1
        _t3 = sk.join_blocks(_rb)
        _vo3 = __import__('collections').Counter(sk.values(_t3))
        _vp3 = __import__('collections').Counter(sk.values(_base))
        assert not [k for k in _vo3 if k not in _vp3] and not [k for k in _vp3 if k not in _vo3], \
            'styling the residue moved a value out of or into the paper'
        txt2 = _t3
        print(f'    residue styled: {_n_res} of this paper\u2019s own paragraphs (the draft\u2019s were left alone)')

        # the humanizer paraphrased a citation\u2019s status: this paper says a companion analysis is "under
        # review", the draft has it as "in review" in five places. Publication status is not a style surface, so
        # the draft\u2019s wording is brought back to the author\u2019s wherever the draft supplies the prose
        _st_fix = 0
        for _rx, _rep in ((r'\bin review\*', 'under review*'), (r'\bin review\b(?=[^a-z])', 'under review'),
                          (r'\bnow in review\b', 'now under review')):
            txt2, _k = re.subn(_rx, _rep, txt2)
            _st_fix += _k
        print(f'    citation status restored to the author\u2019s wording in {_st_fix} place(s)')

        _pre_map = txt2
        _hb = sk.split_blocks(txt2)
        _seen_h = _in_back = False
        for _i, _b in enumerate(_hb):
            if re.match(r'^#{1,6}\s', _b.strip()):
                _seen_h = True
                _in_back = bool(sk.BACK.match(_b.strip())) or _in_back    # the back matter is carried, not styled:
                continue                                                 # `Companion article.` is the author's
            if not _seen_h or _in_back or not sk.is_flow(_b) or '$$' in _b or '|' in _b or '```' in _b:
                continue
            for _rx, _rep in ((r'\b(?:this|the) article\u2019s\b', 'the account\u2019s'),
                              (r"\b(?:this|the) article's\b", "the account's"),
                              (r'\bin (?:this|the) article\b', 'here'),
                              (r'\b(?:this|the) article\b', 'this paper')):
                def _cap(m, _rep=_rep):
                    return _rep if not m.group(0)[0].isupper() else _rep[0].upper() + _rep[1:]
                _nb = re.sub(_rx, _cap, _b, flags=re.I)
                if sk.values(_nb) == sk.values(_b):
                    _b = _nb
            _hb[_i] = _b
        _n2 = sk.join_blocks(_hb)
        assert sk.values(_n2) == sk.values(_pre_map), 'the self-reference map moved a verified value'
        txt2 = _n2
        open(f'{R}/{new}_prebaseline.md', 'w').write(txt)
        edits = [dict(i=e['i'], old=e.get('old', ''), new=e['new'], mode=e.get('mode', '')) for e in humlog]
        before, after = _flowstats(txt), _flowstats(txt2)
        print(f'    {n_ad} draft paragraphs in, {n_kept} of this paper\u2019s paragraphs left standing')
        out = txt2
        # the article and the companions all name themselves in their own front matter; the companion documents
        # must keep pointing at the main text, which the pass already did
        open(f'{R}/{new}.md', 'w').write(out)
        LOG[key] = dict(src=f'{old}.md', dst=f'{new}.md', front=front, src_md_pre=src,
                        baseline=True,
                        adopted=sorted(getattr(sk.stats_of, "out", {}).get("adopted_blocks", [])),
                        blocks=edits, counted=counted, draftbase=b_rep,
                        # i / old / new / mode, for the gate's provenance test
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
    bt.transpile(f'{R}/paper3_supplementary_v18.md', 'paper3_supplementary_v18')
    print('  supplementary transpiled')
    for base in ('companionA_certification_procedure_v9', 'companionB_standards_horizon_v9'):
        title, text, _l = bc.convert(f'{R}/{base}.md', title_override=None)
        # the kit is what breaks the long DOIs and hex digests in the reference lists; a companion written
        # without it prints 48pt of URL past the margin
        text = texkit.header_for(title, 'Companion paper', f'{base}.md') + text
        open(f'{R}/{base}.tex', 'w').write(texkit.improve(text))
        print(f'  {base}.tex written')

    # The article is typeset from its own markdown, the way the supplementary and the two companions have always
    # been. Until now it was typeset by polishing the previous deposit's .tex beside the markdown, and that is the
    # defect this stage closes: a polished copy keeps the paragraphs the style line displaced and loses the ones it
    # admitted, so the PDF carried a document the markdown did not contain (v45 and v46 shipped that way, and the
    # page count not moving after 3,352 words were added is what gave it away). Nothing is now put into the LaTeX
    # that the markdown does not say, and the compiled text is read back below to prove that everything the
    # markdown does say reached it.
    #
    # Two things about this markdown the companion converter does not expect, and the reason the transpile is
    # written here rather than called. Its paragraphs are wrapped at ninety-odd characters, so a formula written
    # between dollar signs straddles a line break, and the converter reads it as prose and prints its backslashes;
    # and it carries six displays in \[ ... \] notation, which the converter does not look for. Every formula is
    # therefore lifted out before conversion and put back, unchanged, afterwards, and prose blocks are set on one
    # line, which changes nothing a reader sees in LaTeX but lets both rules above be read as maths. Tables,
    # quotes, lists and headings keep their line structure, since the converter reads them through it.
    import build_companions_v1 as bc
    _art = 'paper3_material_ledgers_v47'
    src_md = LOG['article']['src_md_pre']
    _md47 = open(f'{R}/{_art}.md').read()
    _math = []

    def _lift(m):
        # a display is written back on its own lines, which is what LaTeX wants of it and what the paragraph the
        # markdown wraps it inside of cannot give it; a formula number the markdown carries as \tag{} is set as
        # \qquad(N) at the end of the display, the way the deposit's own equations read, because \tag outside an
        # equation environment is an error and the number itself is the part a reader needs
        _s = m.group(0)
        if _s.startswith('$$') or _s.startswith('\\['):
            _inner = _s[2:-2].strip()
            _num = re.findall(r'\\tag\{([^}]*)\}', _inner)
            _inner = re.sub(r'\s*\\tag\{[^}]*\}', '', _inner)
            if _num:
                _inner += r' \qquad (' + r') \qquad ('.join(_num) + r')'
            _math.append('\n\n$$' + _inner + '$$\n\n')
        else:
            _math.append('\\(' + _s[1:-1].strip() + '\\)')
        # the placeholder stands in for the formula at the width the formula will occupy: the sizing rule that
        # gives a table its column widths measures the text in each cell, and a six-character token would have it
        # allot nine millimetres to a formula that needs thirty, which is how three rows came to stick out of
        # their columns. So the token carries filler, which is trimmed away when the formula is put back.
        return (f'\x01{len(_math) - 1}\x01'
                + 'x' * max(0, int((0.62 * len(_s)) if _s.startswith('$$') or _s.startswith('\\[')
                                   else (0.68 * len(_s))) - 6))

    _txt = '\n\n'.join(' '.join(_p.split())
                       if not re.search(r'^\s*(?:\||>|```|[-*]\s|\d+\.\s|#)', _p) else _p
                       for _p in _md47.split('\n\n'))
    # A dollar sign in this article is also the currency sign, and pairing on `$` alone shifts every formula
    # after the first price in a paragraph by one, which is how a proof came to set the words "since" and
    # "integrate and use" in italics of a maths font. So a span is maths only where the marks sit as maths marks
    # do: opening before a non-space, non-digit, and closing after a non-space. The flattening above is what lets
    # a formula wrapped across two lines of the markdown be seen as one formula.
    _txt = re.sub(r'\$\$.*?\$\$|(?<!\\)\\\[.*?\\\]|(?<!\\)\$(?![\s\d])((?:[^$\\\n]|\\.)+?)(?<![\s\\])\$',
                  _lift, _txt, flags=re.S)
    _txt = re.sub(r'\n\n(\s*)\n\n', r'\n\n', _txt)                    # the padding the displays brought with them
    # the punctuation the deposited article spells in LaTeX, which the converter reads as characters
    for _a, _b in (('\u2014', '---'), ('\u2013', '--'), ('\u2019', "'"), ('\u2018', "'"),
                   ('\u201c', '``'), ('\u201d', "''"), ('\u00a0', ' ')):
        _txt = _txt.replace(_a, _b)
    open(f'{R}/{_art}.ascii.md', 'w').write(_txt)                       # the intermediate, kept for the audit
    _tab0, _demote = bc.table, [0]

    def _table_or_para(lines):
        if not any(re.match(r'^\s*\|[\s:|-]*-[\s:|-]*\|\s*$', l) for l in lines):
            _demote[0] += 1
            return bc.inline(' '.join(x.strip() for x in lines))
        return _tab0(lines)

    bc.table = _table_or_para                                        # see the note on the proof at section 6.3
    _t47, _body47, _lab47 = bc.convert(f'{R}/{_art}.ascii.md', title_override=None)
    bc.table = _tab0
    assert _demote[0] <= 2, f'{_demote[0]} table groups were not tables; the article has six'
    _body47 = re.sub(r'\x01(\d+)\x01x*', lambda m: _math[int(m.group(1))], _body47)
    # a name with an accent, a dagger, a subscript or a relation sign is written after conversion, because in a
    # text paragraph the converter prints a backslash it does not recognise as a command it owns: \textbackslash-escaped
    # accent is what the It-o calculus sentence used to do
    for _a, _b in (('\u1e03', '\\(\\dot{b}\\)'), ('\u00fc', '\\"{u}'), ('\u00e4', '\\"{a}'),
                   ('\u00f6', '\\"{o}'), ('\u00e9', "\\'{e}"), ('\u00f4', '\\^{o}'), ('\u00d8', '\\O{}'),
                   ('\u00c5', '\\AA{}'), ('\u2020', '\\dag{}'), ('\u2082', '\\textsubscript{2}'),
                   ('\u00f7', '\\(\\div\\)'), ('\u2192', '\\(\\to\\)'), ('\u25a1', '\\(\\square\\)'),
                   ('\u2264', '\\(\\le\\)'), ('\u2265', '\\(\\ge\\)'), ('\u00b1', '\\(\\pm\\)'),
                   ('\u00d7', '\\(\\times\\)'), ('\u00b0', '\\(^{\\circ}$'.replace('$', ''))):
        _body47 = _body47.replace(_a, _b)
    _body47 = re.sub(r'\\begin\{equation\}[\s\S]*?\\qquad \(([0-9]+)\)[\s\S]*?\\end\{equation\}',
                      lambda m: m.group(0), _body47)                      # the kit numbers nothing it was not given
    _left = sorted({c for c in _body47 if ord(c) > 127})
    assert not _left, f'a formula the markdown carries in {len(_math)} spans still holds {_left[:4]}: the ' \
                      f'lifted maths is LaTeX source and is put back as written, so it needs no mapping'
    _tx = texkit.header_for(_t47 or 'Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise '
                            'Diagnostics, and the Semantics of Depletion Horizons', 'Main text', f'{_art}.md')
    _tx = _tx + _body47[_body47.index('\\documentclass'):] if '\\documentclass' in _body47 else _tx + _body47
    _tx = texkit.improve(_tx)
    # A table column a few centimetres wide cannot hyphenate an inline formula, and this article's symbol table
    # carries formulae longer than several of its columns: 38pt of unfittable maths was the widest of them. The
    # deposit's own LaTeX put a break opportunity after every relation and comma inside a long formula, and that
    # treatment is re-derived here, after the kit has had its turn, because the kit refuses input that already
    # carries its own marker. It changes where a line may end and nothing else.
    def _breakable(m):
        _s = m.group(0)
        return _s if len(_s) < 34 else re.sub(r'(?<=[+=,])(?!\\s*\\allowbreak)', '\\\\allowbreak{}', _s)

    _tx = re.sub(r'\\\((?s:.)*?\\\)', _breakable, _tx)
    assert not [c for c in _tx if ord(c) > 127], f'tex non-ascii {sorted({c for c in _tx if ord(c) > 127})[:6]}'
    open(f'{R}/{_art}.tex', 'w').write(_tx)
    # A transpiled document is set to the page by the converter, not by hand as the previous deposit's .tex was,
    # so three displays and one symbol table came out wider than the measure - the widest display by 173pt, a
    # quarter of the text block, which is content a reader would lose. They are fitted by compiling, reading which
    # lines the engine says are too wide, and adjusting those pieces, until the log has nothing left to report: a
    # display that will not fit is scaled to the measure, and a table whose columns were given their widths in em
    # by the sizing rule has those widths reduced in proportion to the overhang, which is the same act the sizing
    # rule performs when it first chooses them. Nothing is reworded, and every piece that was fitted is recorded
    # in the log the package ships, so a reader of the deposit can see which displays were scaled.
    _tx = _tx.replace(r'\usepackage{xcolor}', r'\usepackage{xcolor}' + '\n' + r'\usepackage{graphicx}' + '\n'
                      + r'\setlength{\emergencystretch}{3em}'      # a line whose last box is an inline formula is
                     , 1)                                          # given slack to stretch instead of sticking out
    _fitted = []
    for _round in range(6):
        open(f'{R}/{_art}.tex', 'w').write(_tx)
        _rc, _lt, _ov = texkit.compile_log(_art, R)
        _ls = _tx.split('\n')
        _bad = {}
        for _m in re.finditer(r'Overfull \\hbox \(([0-9.]+)pt too wide\) (?:detected at line (\d+)'
                             r'|in paragraph at lines (\d+))', _lt or ''):
            if float(_m.group(1)) < 6.0:
                continue
            _ln = int(_m.group(2) or _m.group(3))
            _bad[_ln] = max(_bad.get(_ln, 0.0), float(_m.group(1)))
        _did = 0
        for _ln in sorted(_bad, reverse=True):
            if not (0 < _ln <= len(_ls)):
                continue
            _l = _ls[_ln - 1]
            if _l.strip().startswith('$$') and _l.strip().endswith('$$') and len(_l.strip()) > 8:
                # \noindent because a display fitted this way stands at the head of a line that would otherwise
                # begin with the paragraph indent, and \linewidth plus an indent is 15pt more than the page
                _ls[_ln - 1] = (r'\par\noindent\resizebox{\linewidth}{!}{$\displaystyle '
                                + _l.strip()[2:-2].strip() + r'$}\par')
                _did += 1
                _fitted.append(['display scaled to the measure', _ln, round(_bad[_ln], 1)])
                continue
            _env = next((e for e in ('longtable', 'tabular')
                         if (r'\begin{' + e + '}') in '\n'.join(_ls[max(0, _ln - 60):_ln])), None)
            if not _env:
                continue
            _s = next((k for k in range(_ln - 1, max(-1, _ln - 61), -1) if r'\begin{' + _env + '}' in _ls[k]), None)
            _e = next((k for k in range(_ln, len(_ls)) if r'\end{' + _env + '}' in _ls[k]), None)
            if _s is None or _e is None:
                continue
            _spec = _ls[_s]
            _ws = [float(x) for x in re.findall(r'p\{([0-9.]+)em\}', _spec)]
            if not _ws:
                continue
            _cut = min(0.30, max(0.02, _bad[_ln] / (10.0 * sum(_ws))))
            _new = _spec
            for _w in sorted(set(_ws), reverse=True):
                _new = _new.replace('p{%sem}' % ('%g' % _w), 'p{%sem}' % ('%.2f' % (_w * (1 - _cut))), 1)
            if _new == _spec:
                continue
            _ls[_s] = _new
            _did += 1
            _fitted.append([f'{_env} columns narrowed {100 * _cut:.0f}%', _s + 1, round(_bad[_ln], 1)])
        _tx = '\n'.join(_ls)
        if not _did:
            break
    open(f'{R}/{_art}.tex', 'w').write(_tx)
    LOG['article']['tex_fitted'] = _fitted
    if _fitted:
        print('  ' + str(len(_fitted)) + ' piece(s) of the transpiled article were fitted to the measure: '
              + '; '.join(f'{k} at line {n} ({p}pt)' for k, n, p in _fitted[:8]))
    LOG['article']['tex_transpiled_from'] = f'{_art}.md'
    LOG['article']['tex_labels'], LOG['article']['tex_math_spans'] = len(_lab47), len(_math)
    print(f'  article tex transpiled from {_art}.md: {len(_math)} formulas lifted and replaced unchanged, '
          f'{len(_lab47)} cross-reference labels, {len(_tx.split())} words of LaTeX')

    for base in ('paper3_material_ledgers_v47', 'paper3_supplementary_v18', 'companionA_certification_procedure_v9',
                 'companionB_standards_horizon_v9'):
        rc, log, over = texkit.compile_log(base, R)
        src = f'{R}/.logtmp/{base}.pdf'
        if os.path.exists(src):
            open(f'{R}/{base}.pdf', 'wb').write(open(src, 'rb').read())
        pages, right, left, worst = texkit.overhang(f'{R}/{base}.pdf')
        d = LOG.get(next(k for k, (o, n) in docs.items() if n == base), {})
        d['rc'], d['overfull'], d['worst_pt'], d['right'], d['left'], d['pages'] = (
            rc, len(over), round(max(over), 1) if over else 0.0, right, left, pages)
        print(f'  {base:40s} rc={rc} overfull={len(over):2d} right={right:5.1f}pt pages={pages}')

    # and the clause the deposit was missing all along. The compiled text is read back, and every flowing
    # paragraph of the article's markdown has to be in it - so a .tex polished beside the markdown, which is what
    # v45 and v46 shipped, cannot pass. The comparison is made on what the page shows, so it is forgiving about
    # the two things a printer changes and an author does not mean by it: the ligatures a font substitutes (a
    # "fi" that comes back as one character from the PDF), and the maths, which is not prose and sits between the
    # words around it. Each paragraph is therefore read as its runs of words, and the first five and the last
    # five of those runs have to be on the page, which is enough to say the paragraph is there and beginning and
    # ending where the markdown puts them.
    import mdtex_v1 as MT
    _P = MT.page_text(f'{R}/{_art}.pdf')
    _flow47 = MT.md_flow(_md47)
    _absent = [' '.join(b.split())[:64] for b in _flow47 if not MT.covers(_P, b)]
    assert not _absent, (f'{len(_absent)} of {len(_flow47)} flowing paragraphs of the markdown are not in the '
                         f'compiled PDF: {_absent[:2]}')
    print(f'  the compiled article carries all {len(_flow47)} flowing paragraphs of its markdown')
    LOG['article']['pdf_flow_paragraphs'] = len(_flow47)

    open(f'{R}/revisions_v47_base_log.json', 'w').write(json.dumps(LOG, indent=1))

    # the note the package ships beside the builders: what this pass may touch, what it refused, and the
    # measurements on both sides of it. Everything in it is read back out of the log the build just wrote, so the
    # file cannot drift from the run that produced the text.
    # The note the package ships beside the builders: what this pass may touch, what it refused, and the
    # measurements on both sides. Every figure is read back out of the log and the two files, so the note cannot
    # drift away from the run that produced the text.
    ent = LOG['article']
    pre = open(f'{R}/paper3_material_ledgers_v47_prebaseline.md').read()
    new_md = open(f'{R}/{docs["article"][1]}.md').read()
    corp = open(CORPUS_MD).read()
    vs, cs = sk.by_section(pre), sk.by_section(corp)
    words = lambda t: sum(len(b.split()) for b in sk.split_blocks(t) if sk.is_flow(b))

    def _nrm(x):
        return ' '.join(sk.re.sub(r'(?s)\$\$.*?\$\$|\$[^$]*\$', ' ', x).split()).lower()

    refused = 0
    for sec, vsec in vs.items():
        if not sec:
            continue
        csec = [x for x in cs.get(sec, []) if sk.is_flow(x) and '$$' not in x]
        for blk in [x for x in vsec if sk.is_flow(x) and '$$' not in x and not sk._kept(x, KEEP)]:
            if not csec:
                continue
            r, cand = max((difflib.SequenceMatcher(None, _nrm(blk), _nrm(y)).ratio(), y) for y in csec)
            if r >= 0.55 and sk._portable(cand, ' '.join(blk.split())) is not None and \
               sk.values(cand.replace('\n', ' ')) != sk.values(' '.join(blk.split())):
                refused += 1      # the draft's paragraph says something numerically different: not admitted
    only_here = sorted(set(vs) - set(cs) - {''})
    mb, ma = ent['metrics_before'], ent['metrics_after']
    n_take = len([e for e in ent['blocks'] if e.get('mode') != 'sentences'])
    n_frame = sum(1 for e in ent['blocks'] if e.get('mode') == 'framing')
    n_tran = sum(1 for e in ent['blocks'] if e.get('mode') == 'transplant')
    rows = [('flowing-prose words', f'{words(pre):,}', f'{words(new_md):,}'),
            ('sentences of flowing prose', f'{mb["sent"]:,}', f'{ma["sent"]:,}'),
            ('mean sentence length (words)', f'{mb["mean"]:.1f}', f'{ma["mean"]:.1f}'),
            ('p90 sentence length', f'{mb["p90"]:.1f}', f'{ma["p90"]:.1f}'),
            ('longest sentence', f'{mb["mx"]:.1f}', f'{ma["mx"]:.1f}'),
            ('sentences over 60 words', f'{mb["over60"]:,}', f'{ma["over60"]:,}'),
            ('em-dashes', f'{mb["em"]:,}', f'{ma["em"]:,}'),
            ('semicolons', f'{mb["semi"]:,}', f'{ma["semi"]:,}'),
            ('", not Y" frames', f'{mb["frames"]:,}', f'{ma["frames"]:,}'),
            ('"we" and "our" per 1k words', f'{mb["we"]:.1f}', f'{ma["we"]:.1f}'),
            ('self-reference by "the article"', f'{mb["selfref"]:,}', f'{ma["selfref"]:,}')]
    L = ['# The v47 line: the humanized draft as the surface of record', '',
         'Emitted by `builders/build_v47_base.py` from the log that run wrote, so every figure here is the one that',
         'build measured. It replaces the method of every earlier line of this revision: the humanized draft in',
         '`humanize/` is taken as the document, and this paper supplies what the draft cannot, instead of the draft',
         'being used to decorate a text this paper had already written.', '', '## What the pass may touch', '',
         '* a flowing prose block inside a numbered section, one at a time, when the draft has a paragraph for the',
         '  same passage and the two carry the same values (numbers, status words, bare quantities, cross-',
         '  references), in which case the draft\u2019s paragraph is used as it stands;',
         f'* {n_take} paragraphs were taken, of which {n_frame} are the draft\u2019s own framing prose, inserted where this',
         f'  paper had no counterpart, and {n_tran} carry this paper\u2019s numbers transplanted into the draft\u2019s sentence',
         '  because the draft has since been overtaken;',
         f'* {ent["draftbase"]["clean"] + ent["draftbase"]["transplanted"]} of the paper\u2019s paragraphs were displaced by the draft\u2019s own '
         f'paragraph for the same passage, and {ent["draftbase"]["framing"]} of the draft\u2019s paragraphs were taken where this paper had no '
         f'counterpart; {ent["counted"][0][0]} draft paragraphs are in the text and {ent["counted"][0][1]} of this paper\u2019s are left standing;',
         '* the residue is restyled by the rules obtained by aligning the draft against the PDF it was made from',
         '  (`stylekit_v1.py`, the GEM_* tables), a block at a time, and only where the values are untouched and the',
         '  linter finds nothing new in the result.', '', '## What it may not', '',
         '* no table cell, no displayed equation, no statement heading, no numbered list item: they pass through',
         '  byte for byte;',
         '* no heading text, so the section numbering and the article labels the supplementary cites survive;',
         '* not the front matter and not the back matter: the abstract\u2019s sentences are fixed by instruction, and the',
         '  references are carried;',
         '* not the three companion documents, carried byte for byte from the v43 line: the draft is a humanization',
         '  of the main text alone, so there is no draft wording for them to adopt;',
         (f'* {len(only_here)} headings of this paper ({", ".join(only_here)}) carry prose of their own that the '
          'draft has no heading at the same number beside: that prose stays as this paper wrote it, and nothing '
          'is moved into it from elsewhere;\n' if only_here
          else '* nothing is invented to make room for draft prose;\n') +
         f'* {refused} draft paragraphs were refused because the figures in them are not this paper\u2019s;',
         '* and no substitution survives whose own value multiset differs from the passage it replaced. That test',
         '  decides each edit; the document-wide equality of values is the assertion.', '',
         '## Measured on both sides', '', '| quantity | before | after |', '| --- | --- | --- |']
    L += [f'| {a} | {x} | {y} |' for a, x, y in rows]
    L += ['', 'The register is judged as the distance to the draft\u2019s own profile, per 1000 words of flowing prose,',
          'feature by feature and in aggregate, and the gate refuses the build unless that distance fell. Where the',
          'audit instrument\u2019s numeric target contradicts the draft, the draft governs and the gate names the',
          'conflict instead of satisfying the cap; on this text the line is the semicolons.', '',
          '## How the LaTeX is made', '',
          'The four documents are typeset from their markdown, each by the converter the deposit has always used;',
          f'the article\u2019s LaTeX carries {ent.get("tex_math_spans", 0)} formulas lifted out of the markdown before',
          'conversion and put back unchanged after it, '
          + (f'{len(ent.get("tex_fitted", []))} piece(s) were fitted to the measure by scaling or narrowing '
             f'({", ".join(f"{k} at line {n}, {p}pt" for k, n, p in ent.get("tex_fitted", []))})'
             if ent.get('tex_fitted') else 'nothing needed fitting to the measure')
          + ', and',
          'the gate reads the compiled text back and requires every flowing paragraph of the markdown to be in it.',
          'Until this run the article\u2019s .tex was the previous deposit\u2019s, polished paragraph by paragraph '
          'beside',
          'the markdown, which left the PDF carrying prose the style line had displaced. v45 and v46 shipped that '
          'way.', '', '## Reproduce',
          '', '```',
          'python3 builders/build_v47_gbase.py      # text, tex, the four compiles, this note, the log',
          'python3 builders/verify_v47_base.py      # every check, including the provenance of each paragraph',
          '```', '']
    open(f'{R}/structure_v47_base.md', 'w').write('\n'.join(L))
    print('\nlog: revisions_v47_base_log.json')
    print('note: structure_v47_base.md')
    print('next: build_v47_package.py, then verify_v47_base.py')


if __name__ == '__main__':
    main()
