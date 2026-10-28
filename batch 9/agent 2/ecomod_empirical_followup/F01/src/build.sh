#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p .cache/tex
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=.cache/tex manuscript/followup_F01_stage1.tex
cp .cache/tex/followup_F01_stage1.pdf manuscript/followup_F01_stage1.pdf
