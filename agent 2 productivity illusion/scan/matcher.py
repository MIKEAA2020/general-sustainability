"""ID + semantic matching of master claims to revision paragraphs.

Default semantic backend: scikit-learn TF-IDF + cosine, **combined with a BM25
lexical score** (weighted 0.6/0.4) and a domain-keyword bonus. Optional
sentence-transformers embeddings back the cosine term if importable (e.g.
all-mpnet-base-v2, allenai/specter, SciBERT via sentence-transformers).

**Supersession is NOT decided here.** During matching an item is only ever
covered / partial / missing / ambiguous (from the score). Supersession is decided
in a later pass (`scan.status.resolve_statuses`) from (a) an explicit numeric
`SUPERSEDED` verdict, or (b) explicit supersession markers in the revision text —
never from a low semantic score or the mere presence of a match.
"""
import re
from typing import Optional

import numpy as np

from .models import Claim, Match

# Narrow, explicit supersession markers: only a DIRECT statement that an item was
# superseded / withdrawn / does not transfer. Excludes words like "spurious" and
# "original-model only" that appear when the revision merely DISCUSSES supersession.
SUPERSEDED_MARK = re.compile(
    r'(superseded|withdraw(n|s|n)?|does not (transfer|carry over|reproduce)|'
    r'is (now )?superseded|no longer (holds|reproduces|applies))', re.I)
# Broad "no longer applies" markers used for the numeric-verdict path.
SUPERSEDED_VERDICT = re.compile(r'superseded|does not (carry over|transfer|reproduce)', re.I)

KEY_TERMS = ('jevons hutchinson brander wackernagel borucke lin galli blomqvist giampietro saltelli '
             'may antibiotic basin shame dde pydelay half omega saddle separatrix clamp ramp knife blow '
             'method-dependent interpol metadata hygiene keywords modelling modeling period lag rebound '
             'dimensionless chi lambda transcendental eigenvalue spurious trivial recovery grid footnote '
             'multiplicative additive asymmetr debt productivity illusion residual basin mask deficit '
             'carrying overshoot floor falsifiable stable frac non-generic preserve')


def _nums(t):
    return set(re.findall(r'\d+\.\d+|\d+', t))


def _bm25(a_texts, b_texts, k1=1.5, b=0.75):
    """BM25 relevance matrix (rows=a_texts, cols=b_texts), normalised to [0,1]."""
    import math
    from collections import Counter
    toks = [re.findall(r'\w+', t.lower()) for t in list(a_texts) + list(b_texts)]
    na = len(a_texts)
    a_toks, b_toks = toks[:na], toks[na:]
    avgdl = (sum(len(t) for t in b_toks) / len(b_toks)) if b_toks else 1.0
    N = len(b_toks)
    df = Counter()
    for t in set().union(*[set(t) for t in b_toks]):
        df[t] = sum(1 for tt in b_toks if t in tt)
    idf = {t: math.log(1 + (N - df[t] + 0.5) / (df[t] + 0.5)) for t in df}
    S = np.zeros((na, len(b_toks)))
    for i, qt in enumerate(a_toks):
        for j, dt in enumerate(b_toks):
            dcount = Counter(dt)
            if not dcount:
                continue
            s = 0.0
            for q in set(qt):
                if q in dcount:
                    f = dcount[q]
                    s += idf.get(q, 0.1) * (f * (k1 + 1)) / (f + k1 * (1 - b + b * len(dt) / avgdl))
            S[i, j] = s
    if S.size and S.max() > 0:
        S = S / S.max()
    return S


class SemanticMatcher:
    def __init__(self, model_name=None, semantic_threshold=0.75, partial_threshold=0.55,
                 id_weight=1.0, sem_weight=0.6, bm25_weight=0.4,
                 key_weight=0.20, ci=None):
        self.semantic_threshold = semantic_threshold
        self.partial_threshold = partial_threshold
        self.id_weight = id_weight
        self.sem_weight, self.bm25_weight, self.key_weight = sem_weight, bm25_weight, key_weight
        self._st = None
        try:
            if model_name:
                from sentence_transformers import SentenceTransformer
                self._st = SentenceTransformer(model_name)
        except Exception:
            self._st = None

    def _cosine(self, a_texts, b_texts):
        """Cosine similarity matrix in [0,1] (shared TF-IDF space or embeddings)."""
        if self._st is not None:
            A = self._st.encode(a_texts, normalize_embeddings=True)
            Bv = self._st.encode(b_texts, normalize_embeddings=True)
            S = np.asarray(A) @ np.asarray(Bv).T
        else:
            from sklearn.feature_extraction.text import TfidfVectorizer
            allt = list(a_texts) + list(b_texts)
            vec = TfidfVectorizer(lowercase=True, ngram_range=(1, 2),
                                  max_features=40000, min_df=1)
            X = vec.fit_transform(allt).toarray()
            na, nb = len(a_texts), len(b_texts)
            A, Bv = X[:na], X[na:]
            A = A / (np.linalg.norm(A, axis=1, keepdims=True) + 1e-9)
            Bv = Bv / (np.linalg.norm(Bv, axis=1, keepdims=True) + 1e-9)
            S = A @ Bv.T
        return S

    def match_claims(self, master_claims, revision_claims):
        rev_texts = [c.text for c in revision_claims]
        master_texts = [c.text for c in master_claims]
        if rev_texts:
            cos = self._cosine(master_texts, rev_texts)
            bm = _bm25(master_texts, rev_texts)
            cos = (cos - cos.min()) / (cos.max() - cos.min() + 1e-9)
            S = self.sem_weight * cos + self.bm25_weight * bm
        else:
            S = np.zeros((len(master_texts), 0))

        rev_by_section = {}
        for c in revision_claims:
            rev_by_section.setdefault(c.section, []).append(c.text)

        matches = []
        corpus = " ".join(rev_texts).lower()
        for i, mc in enumerate(master_claims):
            sem = S[i] if S.size else np.zeros(len(rev_texts))
            j = int(np.argmax(sem)); best_sem = float(sem[j])
            # corpus-level coverage of the item's distinctive numbers / keywords
            mnums = _nums(mc.text)
            num_cov = sum(1 for n in mnums if n in corpus) / len(mnums) if mnums else 0.0
            keys = [k for k in KEY_TERMS.split() if k in mc.text.lower() and k in corpus]
            key_cov = min(len(keys) / 3.0, 1.0)
            # section-level similarity bonus (if revision uses stable headings)
            sec_bonus = 0.0
            sec_txts = rev_by_section.get(mc.section, [])
            if sec_txts:
                _cos = self._cosine([mc.text], sec_txts)
                sec_bonus = float(np.max(_cos)) * 0.05
            score = 0.5 * num_cov + 0.3 * key_cov + 0.2 * best_sem + sec_bonus
            clean_id = re.sub(r'\s+', '', mc.id)
            id_hit = any(clean_id in re.sub(r'[^A-Za-z0-9.]', '', rc.text) for rc in revision_claims)
            rc = revision_claims[j]
            if id_hit:
                score = max(score, 0.9); method = "id"
            else:
                method = "semantic"
            # status is SCORE-DERIVED ONLY (no supersession here)
            if score >= self.semantic_threshold or num_cov >= 0.7:
                status = "covered"
            elif score >= self.partial_threshold or num_cov >= 0.34:
                status = "partial"
            else:
                status = "missing"
            matches.append(Match(master_claim=mc, revision_claim=rc, method=method,
                                 score=round(score, 3), status=status))
        return matches


def explicit_marker(candidate_texts):
    """True if any candidate revision text carries an explicit supersession marker."""
    return any(bool(SUPERSEDED_MARK.search(t)) for t in candidate_texts)
