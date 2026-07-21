# CONTEXT.md — Applications

## Purpose

Hold one private folder per captured job posting and its derived application
materials.

## Inputs

- Layer 4 (working): one live job URL or pasted description.
- Layer 3 (reference): approved claims from
  `../00-reference/career-history.md`.

## Process

Follow the root `CONTEXT.md`: capture `posting.md`, create `match.md`, draft
`resume.md`, run the fact check, obtain approval, then render DOCX/PDF.

## Outputs

- `Company-name-year-mm-dd-job position/posting.md`
- `Company-name-year-mm-dd-job position/match.md`
- `Company-name-year-mm-dd-job position/resume.md`
- Approved `Cameron Turner_resume.docx` and `Cameron Turner_resume.pdf` when
  requested.

## Rules

- Every application folder and artifact is Git-ignored.
- Preserve the captured posting and YAML status in place.
- Never treat a tailored resume as a source for another application.
