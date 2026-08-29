# Architecture

> **Status:** skeleton. Fill each section in as you build the corresponding stage in
> [ROADMAP.md](ROADMAP.md). Do not try to write this all at once.

## Context

*What problem does this system solve, and for whom? Two or three paragraphs, written for
someone who has not read the README.*

## System overview

*Diagram goes in `docs/diagrams/`. Reference it here.*

```
[ placeholder — replace with your diagram once Stage 5 is complete ]
```

## Components

| Component | Responsibility | Technology | Stage |
|---|---|---|---|
| API | Accept and validate transactions | *TBD* | 1 |
| Processor | Enrich and persist | *TBD* | 1 |
| Audit writer | Append immutable records | *TBD* | 6 |
| Evidence generator | Produce assessor packages | *TBD* | 10 |

## Data model

*Transaction schema. Audit record schema. Explain the hash-chaining approach once built.*

## Security model

- **Identity and access:** *how least privilege is enforced per component*
- **Encryption at rest:** *which keys, managed by whom*
- **Encryption in transit:** *TLS everywhere, including internal hops*
- **Network isolation:** *subnet layout and why*
- **Secrets management:** *where secrets live and how they rotate*

## Control mapping

*Once Stage 6 is complete, map each control to the framework requirement it satisfies.*

| Control | Implementation | Framework reference |
|---|---|---|
| Audit log integrity | *TBD* | *TBD* |
| Access logging | *TBD* | *TBD* |
| Encryption at rest | *TBD* | *TBD* |

## Rejected alternatives

*The most valuable section in this document. For each significant decision, what else did you
consider and why did you not choose it? Detailed records go in `docs/decisions/`.*

## Known limitations

*Be honest here. Every real system has them, and naming them is a sign of engineering maturity
rather than a weakness. A portfolio project that claims no limitations reads as naive.*
