# Payment Transaction Pipeline with Immutable Audit Trail

A cloud-native payment transaction pipeline built to satisfy the evidence requirements
of a regulated financial environment.

---

## The problem this solves

A payments company can process transactions. That part is not hard.

The hard part is answering an assessor who asks:

> *"Show me every change to transaction 8842. Who made it, when, from where — and prove
> to me the record has not been altered since."*

In most environments that answer is assembled by hand from exported logs, screenshots, and
spreadsheets, days after it was asked for. This project builds the system that answers it
automatically, with evidence that stands on its own.

## What it does

- Accepts payment transactions through an authenticated API
- Validates, enriches, and persists each transaction
- Writes an append-only, tamper-evident record of every state change
- Exposes a query interface for transaction lookup and audit reconstruction
- Generates a timestamped evidence package for any transaction or date range

## Status

🚧 **In active development.** This project is being built in stages. See
[ROADMAP.md](ROADMAP.md) for the build sequence and current progress.

## Architecture

See [ARCHITECTURE.md](ARCHITECTURE.md) for the design, and
[docs/decisions/](docs/decisions/) for the record of *why* each significant choice was made,
including the alternatives that were rejected.

## Audit and evidence model

See [AUDIT.md](AUDIT.md) — this is the document that explains how the system answers the
assessor's question above.

## Tech stack

| Layer | Technology |
|---|---|
| Application | Python |
| Infrastructure | Terraform (AWS) |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Testing | pytest |
| Security scanning | tfsec / Checkov, Trivy |

## Running locally

See [docs/local-development.md](docs/local-development.md).

## Why I built this

I spent 25 years in aviation — as an A&P mechanic at United and PSA Airlines, then as an
Army maintenance test pilot and aviation safety officer. In that world, the documentation
*is* the compliance artifact. If a maintenance action is not recorded correctly, it did not
legally happen, and a regulator can ask you to prove it years later.

Financial services has the same requirement and the same failure mode. This project applies
the discipline of one to the other.
