#!/usr/bin/env bash
# Builds dist/learning-coach.zip for uploading to claude.ai (Customize > Skills > Upload a skill).
# The ZIP must contain the skill folder itself at its top level.
set -euo pipefail
cd "$(dirname "$0")/../skills"
mkdir -p ../dist
rm -f ../dist/learning-coach.zip
zip -rq ../dist/learning-coach.zip learning-coach
unzip -l ../dist/learning-coach.zip
