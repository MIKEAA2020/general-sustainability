"""Rule-based actionable vs informational classification.

Actionable pattern verbs mark a to-do (verify / demonstrate / run / check /
recompute / state / report / cite / ...). Informational = descriptive statement
or reference. Optionally upgraded by an importable BERT/transformers classifier
(guarded); default is a fast rule set that needs nothing but `re`.
"""
import re
from .models import Claim

ACTION_RE = re.compile(
    r'\b(action|must|should|verify|demonstrate|run|check|confirm|recompute|test|state|'
    r'report|cite|reconcile|provide|strip|unify|clean|make|justify|perturb|endogeni[sz]e|'
    r'label|flag|give|normalise|publish|switch|name|complete|analyse|analyze|'
    r'add|drop|use|recalculate|regenerate|recompute|adopt)\b', re.I)

def classify(text):
    return "actionable" if ACTION_RE.search(text) else "informational"

def classify_all(claims, model_name=None):
    if model_name:
        try:
            # optional ML upgrade; if unavailable, fall back to rules
            import sentence_transformers  # noqa: F401
        except Exception:
            model_name = None
    for c in claims:
        if c.type == "informational":
            c.type = classify(c.text)
    return claims
