# Start Here

This is your Stage 0 walkthrough. It should take one to two evenings, and it is entirely
Git and Markdown — no cloud, no cost, no AWS knowledge required.

Delete this file when Stage 0 is complete. Its removal is your first real commit.

---

## Step 1 — Create the remote repository

Create an empty repository named `payment-audit-pipeline` on GitHub or GitLab.
Do **not** initialize it with a README, license, or .gitignore — this scaffold already has them.

Make it **public**. The visibility is the point.

## Step 2 — Push this scaffold

```bash
cd payment-audit-pipeline
git init
git add .
git commit -m "chore: initial project scaffold with documentation structure"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

## Step 3 — Protect main

In repository settings, enable branch protection on `main`:

- Require a pull request before merging
- (Optional now, required at Stage 3) Require status checks to pass

You will be approving your own pull requests. That is fine. The discipline is what matters,
and a reviewer can see it in the history.

## Step 4 — Practice the full cycle on a real change

Personalize the README. Do it the long way, on a branch:

```bash
git checkout -b docs/personalize-readme

# Edit README.md -- adjust the "Why I built this" section in your own words

git add README.md
git commit -m "docs(readme): personalize project background section"
git push -u origin docs/personalize-readme
```

Then open a pull request in the web UI, read your own diff, and merge it.

```bash
git checkout main
git pull
git branch -d docs/personalize-readme
```

Do this cycle three or four times on small documentation changes until it is muscle memory.
That fluency is worth more than any single feature you could build this month.

## Step 5 — Write your first real ADR

Copy `docs/decisions/0000-template.md` to `0002-cloud-provider-selection.md` and record your
choice of AWS, including what you considered and rejected.

You already know the answer is AWS — your degree track is AWS-specialized. Write it down
anyway, with the actual alternatives and actual reasoning. The habit of documenting a decision
*while you still remember the alternatives* is the skill being practiced here.

## Step 6 — Update the roadmap

Check off the Stage 0 boxes in `ROADMAP.md`. Commit that on a branch too.

---

## What "done" looks like for Stage 0

- Public repository with this scaffold pushed
- `main` protected
- At least four commits, each on its own branch and merged by pull request
- ADR 0002 written
- Stage 0 checked off in ROADMAP.md
- This file deleted

## Then what

Stage 1 is pure Python: validate a transaction, write an audit record, test both. No cloud.
Come back to your roadmap and work the next box.

Do not read ahead to Stage 6 and feel overwhelmed. The stages exist so that you never have to
hold the whole system in your head at once. That is the same reason a maintenance manual is
written in procedures rather than prose.
