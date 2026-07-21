---
title: CB Job Tailor
status: active
review_state: draft
created: 2026-07-21
updated: 2026-07-21
location_stage: incubation
---

# CB Job Tailor

## What it is

A lightweight, agent-driven workflow that turns a job posting into a truthful,
tailored resume using one canonical Markdown career history.

## Approved v1 specification

- A pasted job URL or description produces a captured posting, evidence map,
  tailored Markdown resume, and—when requested—visually verified DOCX/PDF.
- `00-reference/career-history.md` is the only governing source for career
  claims; generated resumes never update it automatically.
- Unsupported requirements are reported as gaps, never converted into skills,
  titles, certifications, dates, responsibilities, or metrics.
- Personal reference files and application artifacts stay Git-ignored and are
  backed up separately before this project graduates.

## Initial job family

IT service delivery and operations leadership:

- Senior IT Operations Manager
- IT Manager
- Service Desk Manager
- Service Delivery Manager
- Incident Manager

## Use

1. Open this folder in Codex or Claude.
2. Paste a job URL or description and ask to tailor a resume.
3. Review the requirement map and answer any targeted gap questions.
4. Approve the Markdown draft before DOCX/PDF generation.

Agents must read [CONTEXT.md](CONTEXT.md) before handling a job posting.

### Application-only Git exception

When a session only reads or updates Git-ignored files under `00-reference/`
and `01-applications/`, skip the start-of-session `git pull`. Run the full Git
session ritual before changing any tracked project file. This avoids a network
permission prompt when no versioned content can change.

## Private data

The populated career history, contact details, source resumes, and generated
applications are intentionally excluded from Git. Only templates, workflow
rules, tests, and code are versioned.

Private backup destination: `[TODO: choose backup location before graduation]`

## Verification

```bash
./tests/smoke-test.sh
python3 scripts/check_resume.py "01-applications/<application>/resume.md"
```

The checker is a narrow hard gate for invented numeric claims. Human review and
the evidence map remain required for nonnumeric facts.

## Status

- [x] Define v1 and privacy boundary.
- [x] Import the supplied 2026 resume into a private canonical career history.
- [x] Add a cross-agent tailoring workflow.
- [x] Add a synthetic posting fixture and metric-claim smoke test.
- [ ] Choose and verify a private backup destination.
- [ ] Test against a real job posting supplied by Cameron.

## Graduation check

- [ ] Needs launchd or always-on process?
- [ ] Needs deploy target?
- [x] Has data worth backing up?
- [ ] Production project depends on this?

The trigger is acknowledged. Cameron explicitly chose to build and test in
incubation before migrating; configure backup and graduate before operational
use.
