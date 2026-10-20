
# binarybit-ops

Source code for Binary Bit Ops / Nexus, the corporate operating system used by
Binary Bit Technologies. Part of the Hybrid Development Environment (HDE) Phase 3.

## Scope
Binary Bit Ops/Nexus remains the live PHP/MySQL application hosted on Truehost cPanel.
This repository governs code review, testing and release evidence only.
It does not authorise a Kubernetes or database migration of the live application.

## Core workflows
- Attendance and clocking
- Access permissions and roles
- Projects
- Timesheets

## Contribution rules
- All changes go through a pull request. Direct pushes to `main` are blocked.
- At least one approval is required, and the reviewer must not be the author.
- Required status checks must pass before merging.
- Every change needs a linked ticket, test evidence and a rollback note.
- Releases that change attendance, access, project or time data need a database
  backup and a tested migration plan.

## Security
- Never commit passwords, API keys, database credentials, `.env` files or SQL dumps.
- Use `config.example.php`-style templates with placeholder values only.
- Do not commit real staff or attendance data.
- If a secret is committed by mistake, tell the project manager immediately so it
  can be rotated.

## Branching
- `main` is protected and always releasable.
- Work happens on `feature/*`, `fix/*` or `hotfix/*` branches.

## Releases
Approved changes are released through the existing controlled Truehost release path,
with release, security and service evidence returned to the Binary Bit Ops DevOps cockpit.

## Related repositories
- `hde-infrastructure`
- `hde-gitops`
- `hde-pipelines`
- `hde-docs-evidence`

## Contacts
Project manager: Lelo

## Phase 3 non-production demonstrator

The isolated [Phase 3 demonstrator](phase3-demonstrator/README.md) supports HDE WBS task 3.10. It is a separate, disposable workload for the HDE delivery path and is not the live PHP/MySQL Nexus application hosted on Truehost.
