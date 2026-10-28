#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p .cache/tex
for stem in ecomod_continued_13_revision_draft_20261029 ecomod_continued_13_revision_draft_20261029_SI; do
  latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=.cache/tex "$stem.tex"
  cp ".cache/tex/$stem.pdf" "$stem.pdf"
done
