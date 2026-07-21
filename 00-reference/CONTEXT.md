# CONTEXT.md — Private Career Reference

## Purpose

Hold the private, stable facts that govern every tailored resume.

## Inputs

- Layer 4 (working): Cameron's supplied resumes and explicit corrections.
- Layer 4 (working): career details gathered through targeted onboarding
  questions until Cameron approves them.

## Process

1. Preserve original evidence unchanged in `source/`.
2. Record approved career facts once in `career-history.md` with stable claim IDs.
3. Keep contact fields separate in `contact.md`.
4. Mark uncertain material `[TODO: confirm]`; it is ineligible for resumes.

## Outputs

- `career-history.md` — canonical career claims.
- `contact.md` — final-render contact fields.
- `source/` — retained originals.

## Rules

- `career-history.md` is the sole career-claim authority.
- `contact.md` is used only for final rendering.
- `source/` retains original evidence unchanged.
- Populated files are Git-ignored and require a separate private backup.
- Generated applications never update this layer automatically.
