#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p .cache/tex
for name in ecomod_C16_main ecomod_C16_SI; do
  latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=.cache/tex "$name.tex"
  cp ".cache/tex/$name.pdf" "$name.pdf"
done
