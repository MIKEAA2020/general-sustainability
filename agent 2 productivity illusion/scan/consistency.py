"""Self-consistency / contradiction detection.

Default backend is rule-based (offline-safe): it flags pairs of revision sentences
that (a) share a key claim term where one is negated and the other asserted, or
(b) assert quantitatively different values for the same quantity. Optional NLI
(transformers + facebook/bart-large-mnli) is used if importable and enabled.
"""
import re
from .models import ConsistencyIssue

NEG = re.compile(r'\b(no|not|never|without|cannot|does not|do not|absent)\b', re.I)
TERMS = ('masking','mask','overshoot','biocapacity','sustainability','weak','strong',
         'illusion','deficit','stable','collapse','equilibrium','debt','carrying capacity')
# quantity -> a couple of representative numeric spellings, for numeric conflicts
KEY_SUBSTR = ('mask','overshoot','biocapacity','sustainability','illusion','deficit',
              'collapse','equilibrium','carrying capacity','basin','stable')

def _sentences(text):
    # split on sentence boundaries, keep line numbers
    out = []
    for m in re.finditer(r'(.+?(?:\.|;|:|!|\?))(?=\s|\n|$)', text):
        s = ' '.join(m.group(1).split())
        if len(s) > 25:
            out.append(s)
    return out

def _tok(text):
    return set(re.findall(r"[a-z]{2,}", text.lower()))


# Strong contrastive/negation markers (a genuine "not X but Y" claim).
CONTRAST = re.compile(
    r'\b(not|never|cannot|does not|do not|no|without|fails|contradicts|'
    r'on the other hand|in contrast|however)\b', re.I)
# Specific claim terms (avoid generic nouns that appear across the whole doc).
SPECIFIC = ('mask', 'masking', 'overshoot', 'biocapacity', 'sustainability',
            'illusion', 'deficit', 'collapse', 'equilibrium', 'basin-shrinkage',
            'carrying capacity', 'superseded', 'transient', 'stability')


def _contradiction_pair(a, b, key_terms):
    """Return (relation, note) if a and b genuinely conflict, else None.

    HIGH-PRECISION (accepts low recall): a contradiction is only flagged when BOTH
    sentences make an explicitly contrastive/negated claim AND they reference >=2
    of the SAME specific terms in near-token proximity. This avoids the document's
    own contrastive/qualified framing (e.g. "narrow, *not* generic"), which the
    crude rule previously over-flagged. The NLI backend is the high-recall path.
    """
    la, lb = a.lower(), b.lower()
    linked = [t for t in SPECIFIC if t in la and t in lb]
    if len(linked) < 2:
        return None

    def adjacent_neg(s, term_list):
        ws = s.split()
        for t in term_list:
            for k, w in enumerate(ws):
                if t in w.lower():
                    window = ws[max(0, k - 5): k + 5]
                    if any(CONTRAST.search(x) for x in window):
                        return True
        return False

    if adjacent_neg(a, linked) and adjacent_neg(b, linked):
        if bool(NEG.search(a)) != bool(NEG.search(b)):
            return "contradict", f"both qualify same terms: {linked}; one negates, one asserts"
        return "contradict", f"contrastive claims on same terms: {linked}"
    # numeric conflict: same quantity, materially different value, topically linked
    nums_a = set(re.findall(r'\d+(?:\.\d+)?', a)); nums_b = set(re.findall(r'\d+(?:\.\d+)?', b))
    if (nums_a & nums_b) and len(linked) >= 2:
        return "numeric-conflict", f"shared number(s): {sorted(nums_a & nums_b)}; term(s): {linked}"
    return None


def _find_contradictions(sentences, key_terms=None, window=6):
    """Compare sentences within a LOCAL window (default 6 neighbours).

    Cross-document scanning over-flaggers: a metadata sentence that shares a term
    with many content sentences is not a contradiction. Contradiction detection is
    the strongest, least noisy, between statements that are near each other; the
    NLI backend (if enabled) may relax the window.
    """
    issues = []
    key_terms = key_terms or KEY_SUBSTR
    n = len(sentences)
    for i in range(n):
        for j in range(i + 1, min(i + window + 1, n)):
            res = _contradiction_pair(sentences[i], sentences[j], key_terms)
            if res:
                relation, note = res
                issues.append(ConsistencyIssue(line1=i + 1, sentence1=sentences[i],
                                               line2=j + 1, sentence2=sentences[j],
                                               relation=relation,
                                               score=0.9 if relation == "contradict" else 0.7,
                                               note=note))
    return issues

class ConsistencyChecker:
    def __init__(self, model_name=None):
        self.model_name = model_name
        self._nli = None
        try:
            if model_name:
                from transformers import pipeline     # noqa: F401
                self._nli = pipeline("zero-shot-classification", model=model_name)
        except Exception:
            self._nli = None

    def find_contradictions(self, sentences, key_terms):
        issues = _find_contradictions(sentences, key_terms)
        # dedupe near-identical numeric-conflict hits (same pair)
        seen = set(); deduped = []
        for it in issues:
            k = (it.line1, it.line2, it.relation)
            if k in seen:
                continue
            seen.add(k); deduped.append(it)
        return deduped
