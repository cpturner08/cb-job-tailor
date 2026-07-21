#!/bin/sh
set -eu

project_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$project_root"

test -f README.md
test -f CONTEXT.md
test -f AGENTS.md
test -f CLAUDE.md
test -f 00-reference/career-history.md
test -f 00-reference/contact.md
test -f tests/fixtures/service-delivery-manager.md

git check-ignore -q 00-reference/career-history.md
git check-ignore -q 00-reference/contact.md
git check-ignore -q 00-reference/source/2026_Cameron_Turner_Resume.docx
git check-ignore -q 01-applications/_smoke-service-delivery-manager/resume.md

python3 scripts/check_resume.py --self-test
python3 scripts/check_resume.py \
  01-applications/_smoke-service-delivery-manager/resume.md

if rg -qi '\bPMP\b' 01-applications/_smoke-service-delivery-manager/resume.md; then
  echo "FAIL: unsupported PMP certification leaked into resume" >&2
  exit 1
fi

echo "PASS: project structure, privacy boundary, gap handling, and fact gate"
