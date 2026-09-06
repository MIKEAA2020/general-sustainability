"""Gold-labelled eval set for the master->revision matcher.

This module is now a thin re-export of the VERSIONED gold set. The active set is
`scan/eval_gold_v21.py` (re-keyed to the v21 formal-article wording); the previous
v20 set is preserved as `scan/eval_gold_v20.py`. See those files for the anchor
conventions and provenance. Swap the import below to switch which revision a gold
set is keyed to.
"""
from .eval_gold_v21 import GOLD_PHRASES, HARD_NEG_PHRASES

__all__ = ["GOLD_PHRASES", "HARD_NEG_PHRASES"]
