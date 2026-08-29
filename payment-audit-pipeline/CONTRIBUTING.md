# Working Agreement

This is a solo project, but it follows team conventions on purpose. The habits are the point,
and the commit history is part of what this repository demonstrates.

## Branching

- `main` is always deployable and is protected
- Work happens on branches: `feat/`, `fix/`, `docs/`, `infra/`, `chore/`
- Example: `feat/transaction-validation`, `infra/s3-audit-bucket`

## Commits

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(api): add transaction validation for negative amounts
fix(audit): correct hash chain ordering on concurrent writes
docs(adr): record decision to use S3 Object Lock
infra(terraform): add remote state backend
```

Write the *why* in the body when the change is not obvious. Future you will need it, and so
will anyone reviewing this repository.

## Pull requests

Every change to `main` arrives by pull request, including your own. Each PR should state:

1. What changed
2. Why
3. How it was verified

Review your own PR before merging. Read the diff as if someone else wrote it. This catches
more than you would expect and builds the habit that matters in a regulated shop.

## Architecture decisions

Any decision that would be expensive to reverse gets an ADR in `docs/decisions/`. Write it
when you make the decision, while the alternatives are still fresh.

## Definition of done

A stage is complete when:

- [ ] It works
- [ ] Tests pass in CI
- [ ] Documentation is updated
- [ ] Nothing secret is committed
- [ ] Cloud resources are torn down or intentionally left running with known cost
