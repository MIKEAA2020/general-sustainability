#!/usr/bin/env python3
"""The reuse splice: put the ledger-cleared sentences into the article, and keep them there through the style pass.

v47 let a whole paragraph ship from the draft when the block could be proved to say the same thing. v48 replaces that
judgement with the claim ledger's, which is made one sentence at a time. The splice therefore has two halves, and the
second one is the reason the first can be trusted:

  `insert()` runs on the deposited article, before the register pass. A reused row is a draft sentence that restates
  a deposit sentence; the deposit sentence is found with the ledger's own instruments - `blocks(pairs=True)` (the
  maths-deleted block the row was paired with, and its raw twin index for index) and `sentences()` - by matching the
  row's `dep` normal form against the *processed* sentences and taking the sentence at the same index in the raw
  twin. Then the raw sentence is replaced in the document by string surgery.

  `protect()` runs after the register pass and the two document conventions, which rewrite words inside those same
  sentences. Any reused sentence the pass altered is put back as the draft wrote it, and the two conventions
  (`in review` to `under review`, and the self-reference map) are re-applied to the restored text, because citation
  status and the paper's name for itself are not style surfaces.

Everything the locator cannot place is reported and ships from the deposit, which is the direction the ruling says to
err in. A row whose draft text is a fragment - the splitter cut it at a `$$` display or at "eq." before a
parenthesised number - is never inserted, because a fragment in a paragraph breaks the paragraph. Figures are
guarded by counting how many times each is actually written in the document, so a swap can never leave the paper
stating less than it did.

Writes `v48_splice_log.json`. Returns the text and the counts the build note prints.
"""
import difflib
import json
import re
from collections import Counter, defaultdict

import claim_ledger_v1 as cl
import stylekit_v1 as sk

V48 = '/home/user/revision/v48'
SPLIT = f'{V48}/v48_reuse_split.json'
AUDIT = f'{V48}/v48_reuse_audit.json'
LEDGER = f'{V48}/claim_ledger_v1.json'

# re.I matters: the builder's own map is case-insensitive, and a restored sentence beginning "This article builds"
# would otherwise keep a self-reference the rest of the document does not use
CONVENTION = [(re.compile(r'\bin review\*(?=\W)', re.I), 'under review*'),
              (re.compile(r'\bin review\b(?=[^a-z])', re.I), 'under review'),
              (re.compile(r'\bnow in review\b', re.I), 'now under review'),
              (re.compile(r'\b(?:this|the) article\u2019s\b', re.I), 'the account\u2019s'),
              (re.compile(r"\b(?:this|the) article's\b", re.I), "the account's"),
              (re.compile(r'\bin (?:this|the) article\b', re.I), 'here'),
              (re.compile(r'\b(?:this|the) article\b', re.I), 'this paper')]
ANAPHORIC = re.compile(r'^(?:They|These|Those|This|That|It|Both|Their|Its|He|She|Which)\b')
CONNEXIVE = re.compile(r'^(?:And|But|So|Yet|Nor|Also|Moreover|Further|Additionally|Hence|Thus)\b')


LABEL = re.compile(r'\*\*(?:Theorem|Proposition|Lemma|Corollary|Definition|Remark|Exhibit|Counterexample|'
                   r'Example|Protocol|Assumption|Conditional Theorem|Non-example|Table)\b')
# the statement's identity is its name, number *and* the parenthetical title, so a row that would retitle a
# proposition is refused even when the label count is unchanged - Proposition 2 in v48.1 picked up the draft's
# "The layers do not collapse" over the deposit's untitled statement, which is a change to the document, not to prose
STMT = re.compile(r'\*\*(Definition|Lemma|Proposition|Theorem|Corollary|Remark)(\s+\d+(?:\.\d+)?)([^.)]*)\)\.\*\*')


def stmts(s):
    return sorted(m.group(1) + ' ' + m.group(2).strip() + (m.group(3) or '').strip() for m in STMT.finditer(s))
STRUCTURAL = re.compile(r'\n\s*\n|\$\$|^\s*\||^\s*#|^\s*>|^\s*```', re.M)


def _span_ok(matched, target):
    r"""the match has to be about as long as the sentence it stands for and must not swallow a blank line, a
    display or a table row between its words - `\s+` between words will happily do that, and the splice would
    move structure instead of a sentence"""
    return len(matched) <= 1.30 * len(target) + 40 and not STRUCTURAL.search(matched)


PLURAL_ANA = {'They', 'These', 'Those', 'Both', 'Their', 'Its'}


def _words(s):
    return {w.strip('.,;:\"“”’()') for w in s.split() if len(w) > 3}


def _antecedent_survives(pronoun, target, draft, sibs, at):
    """whether the swap leaves the next sentence something to point at.

    Three cases, in order. If the row restates the sentence it replaces closely enough (a little over half its
    content words), the paragraph says what it said and nothing downstream can notice - D0148 and D0152 are this
    case and the first version of the guard refused them for nothing. If the next sentence opens on a plural
    ("They are not", "Both readings are"), a plural is needed, so some plural of the replaced sentence has to
    survive in the row replacing it. If it opens on a singular ("It is", "This is"), the pronoun is holding a whole
    clause rather than a noun, and no word list settles that, so the row has to be about the same things to go in.
    """
    tw, dw = _words(target), _words(draft)
    ov = len(tw & dw)
    if ov >= max(2, int(0.55 * len(tw))):
        return True
    if pronoun in PLURAL_ANA:
        tp = {w.lower().rstrip('.;,') for w in target.split() if w.rstrip('.;,').endswith('s') and len(w) > 4}
        dp = {w.lower().rstrip('.;,') for w in draft.split() if w.endswith('s') and len(w) > 4}
        return bool(tp & dp)
    return ov >= max(2, int(0.4 * len(tw)))


def is_fragment(s):
    return not re.search(r'[.!?\u201d\u2019)\]`\u2026]$', s.strip())


def _fold(t):
    """one figure, one key: the deposit writes `240{,}000`, the draft writes `240,000`"""
    return re.sub(r'(?<=\d),(?=\d)', '', t.replace('{,}', ','))


def _vals(t):
    return sk.values(_fold(t))


def _cnt(text, v):
    return len(re.findall(r'(?<![\d.])' + re.escape(v) + r'(?![\d])', _fold(text)))


def _rx(s):
    """a pattern for a sentence that survives line wrapping: its words in order, any run of whitespace between"""
    return re.compile(r'\s+'.join(map(re.escape, s.split())))


def load():
    reuse = json.load(open(SPLIT))['reuse']
    audit = {r['id']: r['draft'] for r in json.load(open(AUDIT))}
    led = {r['id']: r for r in json.load(open(LEDGER))['rows']}
    return reuse, audit, led


def prose_state(txt):
    """which sk-blocks may be edited, in document order: after the first numbered heading, outside the back matter"""
    blocks = sk.split_blocks(txt)
    seen_h = in_back = False
    ok = set()
    for i, b in enumerate(blocks):
        st = b.strip()
        if st.startswith('#'):
            if re.match(r'^#{1,6}\s+\d', st):
                seen_h = True
            if sk.BACK.match(st):
                in_back = True
            continue
        if seen_h and not in_back and sk.is_flow(b) and '$$' not in b and '|' not in b and '```' not in b:
            ok.add(i)
    return blocks, ok


def insert(txt):
    """splice the reused sentences into the deposited article, ahead of the register pass"""
    reuse, audit, led = load()
    pbp = cl.blocks(txt, pairs=True)
    processed = [x[0] for x in pbp]
    rawtwin = [x[1] for x in pbp]
    psents = [cl.sentences(t) for t in processed]
    rsents = [cl.sentences(r) for r in rawtwin]
    by_norm = defaultdict(list)
    for bi, sents in enumerate(psents):
        for si, s in enumerate(sents):
            k = cl.norm(s)
            if k:
                by_norm[k].append((bi, si))
    out = txt
    done = Counter()
    log = []
    for x in sorted(reuse, key=lambda r: r['id']):
        rid = x['id']
        draft = (audit.get(rid) or x['text']).strip()
        dep = led.get(rid, {}).get('dep') or ''
        dn = cl.norm(dep)
        if not dn:
            done['no-deposit-sentence'] += 1
            log.append(dict(id=rid, state='the ledger found no deposit sentence for it - ships from the deposit'))
            continue
        if is_fragment(draft):
            done['fragment'] += 1
            log.append(dict(id=rid, state='fragment - not spliced; its block carries the deposit sentence',
                            draft=draft[:140]))
            continue
        where = by_norm.get(dn)
        if not where:
            near = difflib.get_close_matches(dn, list(by_norm.keys()), n=1, cutoff=0.60)
            if near:
                where = by_norm[near[0]]
                done['fuzzy'] += 1
            else:
                done['unfound'] += 1
                log.append(dict(id=rid, state='the deposit sentence could not be located - ships from the deposit',
                                dep=dn[:140]))
                continue
        bi, si = where[0]
        target = rsents[bi][si] if si < len(rsents[bi]) else rsents[bi][-1]
        if not target:
            done['empty-target'] += 1
            continue
        if '$$' in target or '```' in target or '|' in target:
            # the ledger's raw twin keeps the display and table lines its pairing filter drops, so a sentence taken
            # from it can run straight through a `$$` block; replacing that would delete the display, which the
            # guard catches. The row ships from the deposit instead, and is counted
            done['display-entangled'] += 1
            log.append(dict(id=rid, state='its deposit sentence runs through a display or table - not spliced, '
                                          'the display is carried as it stands', block=bi))
            continue
        pat = _rx(target)
        spots = [m for m in pat.finditer(out)]
        if not spots:
            done['not-in-document'] += 1
            log.append(dict(id=rid, state='the located sentence is not in the document verbatim - left alone',
                            block=bi))
            continue
        if len(spots) > 1:
            done['ambiguous'] += 1
            log.append(dict(id=rid, state=f'the sentence occurs {len(spots)} times - not spliced, ambiguity is not '
                                          f'a coin toss', block=bi))
            continue
        m = spots[0]
        if not _span_ok(m.group(0), target):
            done['span-crossed-structure'] += 1
            log.append(dict(id=rid, state='the one place that matches runs across a blank line, a display or a '
                                          'table - not spliced; a splice there moves structure',
                            matched=len(m.group(0)), target=len(target)))
            continue
        if len(LABEL.findall(target)) != len(LABEL.findall(draft)) or stmts(target) != stmts(draft):
            # a theorem statement is not prose to be swapped: the article counts them, the gate checks the count,
            # and the draft's version of the sentence does not always carry the bold label the deposit puts first
            done['statement-label'] += 1
            log.append(dict(id=rid, state='the deposit sentence carries a theorem or table label the draft row does '
                                          'not reproduce - the statement stays as the article writes it',
                            labels=(len(LABEL.findall(target)), len(LABEL.findall(draft)))))
            continue
        # a row is only safe to splice when the sentences on either side of it still cohere without it: D0089 took
        # out the sentence "the distinction matters because \u201ctime to depletion\u201d is publicly used as if all
        # three were one quantity", and left the article's own next sentence - "They are not, and the worked
        # instances..." - answering a question nobody had asked. A reused row that opens a paragraph on "And" is the
        # same fault by symmetry: the draft wrote it after a sentence that is not there
        sibs = cl.sentences(rawtwin[bi])
        at = [k for k, s in enumerate(sibs) if cl.norm(s) == cl.norm(target)]
        at = at[0] if at else sibs.index(rsents[bi][si]) if rsents[bi][si] == target else None
        if at is not None:
            nxt = sibs[at + 1].strip() if at + 1 < len(sibs) else ''
            an = ANAPHORIC.match(nxt)
            if an and not _antecedent_survives(an.group(0), target, draft, sibs, at):
                done['antecedent-lost'] += 1
                log.append(dict(id=rid, state='not spliced - the sentence after it takes its antecedent from the one '
                                          'this row would replace', next=sibs[at + 1][:120]))
                continue
            if at == 0 and CONNEXIVE.match(draft):
                done['dangling-connective'] += 1
                log.append(dict(id=rid, state='not spliced - the row opens a paragraph with a connective that '
                                          'pointed back at a draft sentence this document does not have',
                                draft=draft[:120]))
                continue
        vt = set(_vals(target))
        vd = set(_vals(draft))
        if vt - vd:
            lost = sorted(v for v in vt - vd if _cnt(out, v) <= 1)
            if lost:
                done['refused-figure'] += 1
                log.append(dict(id=rid, state='refused - the swap would leave a figure unstated', values=lost[:6]))
                continue
            done['figure-carried-elsewhere'] += 1
        out = out[:m.start()] + draft + out[m.end():]
        done['inserted'] += 1
        log.append(dict(id=rid, state='inserted before the style pass', block=bi, want=draft[:150]))
    return out, done, log


def conventions(t):
    for rx, rep in CONVENTION:
        if rx.pattern.endswith("article\\b"):
            def cap(m, _r=rep):
                return _r if not m.group(0)[0].isupper() else _r[0].upper() + _r[1:]
            t = rx.sub(cap, t)
        else:
            t = rx.sub(rep, t)
    return t


def protect(txt, log):
    """the register pass and the conventions have been through the reused sentences; put the drafts back.

    Matching is by Jaccard overlap of content words rather than a rebuilt index each time: the pass rewrites words
    inside a sentence, which moves its normal form, and the sentences wanting repair are few. The whole text is
    joined once at the end, not once per restoration.
    """
    reuse, audit, led = load()
    want = {}
    for l in log:
        if l['state'].startswith('inserted'):
            x = next(r for r in reuse if r['id'] == l['id'])
            want[l['id']] = (audit.get(l['id']) or x['text']).strip()
    blocks, ok = prose_state(txt)
    entries = []
    for i in sorted(ok):
        for s in cl.sentences(blocks[i]):
            k = cl.norm(s)
            if k:
                entries.append((i, s, k, frozenset(k.split())))
    restored = damaged = missed = 0
    for rid, draft in sorted(want.items()):
        if _rx(draft).search(txt):
            continue                                  # the pass left it as the draft wrote it
        damaged += 1
        dt = frozenset(cl.norm(draft).split())
        best, bs = None, 0.0
        for (i, s, k, ks) in entries:
            j = len(dt & ks) / max(1, len(dt | ks))
            if j > bs:
                bs, best = j, (i, s)
        if not best or bs < 0.50:
            missed += 1
            log.append(dict(id=rid, state='the pass changed this sentence and it could not be found again - it ships '
                                           'as the pass left it', want=draft[:150], best_overlap=round(bs, 3)))
            continue
        i, cur = best
        m = _rx(cur).search(blocks[i])
        if not m or not _span_ok(m.group(0), cur) or len(LABEL.findall(cur)) != len(LABEL.findall(draft)):
            missed += 1
            continue
        vt, vd = set(_vals(cur)), set(_vals(draft))
        lost = sorted(v for v in vt - vd if _cnt(txt, v) <= 1)
        if lost:
            missed += 1
            log.append(dict(id=rid, state='restoring the draft sentence would lose a figure - left with the pass',
                            values=lost[:4]))
            continue
        blocks[i] = blocks[i][:m.start()] + conventions(draft) + blocks[i][m.end():]
        entries = [(a, b, c, d) for (a, b, c, d) in entries if not (a == i and b == cur)]
        restored += 1
    if restored:
        txt = sk.join_blocks(blocks)
    return txt, dict(reused_into_the_pass=len(want), damaged_by_pass=damaged, restored=restored,
                     left_with_the_pass=missed)


def guard(before, after):
    a, b = set(_vals(after)), set(_vals(before))
    assert not [v for v in a if v not in b], f'the reuse introduced a figure the paper does not state: {sorted(a-b)[:5]}'
    assert not [v for v in b if v not in a], f'the reuse lost a figure the paper states: {sorted(b-a)[:5]}'
    assert len(re.findall(r'(?m)^\|', after)) == len(re.findall(r'(?m)^\|', before)), 'the reuse disturbed a table'
    for tag in ('$$', '```'):
        assert after.count(tag) == before.count(tag), f'the reuse disturbed a {tag} region'
    style_only = sorted(set(sk.values(after)) ^ set(sk.values(before)))
    return style_only


def apply(txt):
    """one call for a standalone run: insert, register-free conventions, protect, and the guards"""
    out, done, log = insert(txt)
    out2, sp = protect(conventions(out), log)
    style_only = guard(txt, out2)
    spl = dict(rows=len(json.load(open(SPLIT))['reuse']), insert=dict(done), protect=sp,
               separator_style_only=style_only, log=log)
    json.dump(spl, open(f'{V48}/v48_splice_log.json', 'w'), indent=1)
    return out2, {k: v for k, v in spl.items() if k != 'log'}


if __name__ == '__main__':
    import sys
    txt = open(sys.argv[1]).read()
    out, s = apply(txt)
    open(sys.argv[2], 'w').write(out)
    print(json.dumps(s, indent=1))
