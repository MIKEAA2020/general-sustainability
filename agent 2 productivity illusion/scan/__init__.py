"""scan_revision: a repeatable, auditable, semi-automated master->revision gap scan.

Default backends are offline-safe (scikit-learn TF-IDF + rule-based classification)
so the pipeline runs in CI without downloading large models. Optional heavy
backends (sentence-transformers, transformers/NLI) are used if importable.
"""
__version__ = "0.1.0"
