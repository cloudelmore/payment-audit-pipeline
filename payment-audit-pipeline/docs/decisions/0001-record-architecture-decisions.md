# ADR 0001: Record architecture decisions

**Date:** 2026-08-28
**Status:** Accepted

## Context

This project is a portfolio artifact as much as a working system. A reviewer evaluating it
cares less about *what* was built than about whether the builder can reason about tradeoffs
and defend choices under scrutiny.

Undocumented decisions are also expensive in practice. Six months on, the reasoning behind a
non-obvious choice is gone, and the choice gets either blindly preserved or carelessly
reversed.

This mirrors a discipline from aviation maintenance: a maintenance action without a
corresponding logbook entry did not legally happen. The record is not overhead attached to the
work — the record is part of the work.

## Decision

Every architecturally significant decision will be recorded as a numbered ADR in
`docs/decisions/`, using the template in `0000-template.md`.

A decision is architecturally significant if reversing it later would be expensive: choice of
cloud provider, data store, audit mechanism, deployment model, or anything touching the
security or compliance posture.

ADRs are written when the decision is made, not retroactively.

## Alternatives considered

### Alternative A: Document decisions in ARCHITECTURE.md only
- **Pros:** one file, less structure to maintain
- **Cons:** loses chronology; no record of superseded decisions; the file becomes a
  description of the current state rather than a history of reasoning
- **Why not chosen:** the reasoning and its evolution are the valuable part

### Alternative B: Rely on commit messages and pull request descriptions
- **Pros:** no extra artifacts; already part of the workflow
- **Cons:** buried and effectively unsearchable; a reviewer will not excavate Git history to
  find out why DynamoDB was chosen over Aurora
- **Why not chosen:** discoverability

## Consequences

- Each significant decision costs an extra fifteen to thirty minutes to record
- A reviewer can trace the reasoning behind the system without an interview
- Superseded decisions stay visible, showing how understanding developed
- Writing the alternatives section forces genuine consideration of alternatives, which is
  the real benefit
