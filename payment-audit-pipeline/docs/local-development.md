# Local Development

> **Status:** fill in as you complete Stage 1 and Stage 2.

## Prerequisites

- Python 3.11+
- Docker Desktop
- Git
- AWS CLI (not needed until Stage 4)

## Setup

```bash
git clone <your-repo-url>
cd payment-audit-pipeline
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running tests

```bash
pytest
```

## Running the application

*Fill in at Stage 1.*

## Running in Docker

*Fill in at Stage 2.*

## Cost safety

Before creating any AWS resource in Stage 4:

1. Set a billing alarm on the account
2. Confirm `scripts/teardown.sh` works
3. Tear down resources at the end of each working session

You are learning on your own money. Treat teardown as part of the work, not an afterthought.
