# Build Roadmap

This project is built in stages. Each stage produces something that **works and is committed**
before the next begins. Nothing here requires knowing the whole stack up front.

Check boxes off as you go. The commit history is part of the deliverable — it shows the
project was built deliberately, not dumped in one upload.

---

## Stage 0 — Repository and documentation foundation
**Skills: Git, Markdown, technical writing**
**Prerequisite: none — start here today**

- [ ] Create the remote repository and push this scaffold
- [ ] Write a real `.gitignore` before the first code commit
- [ ] Practice the branch → commit → pull request → merge cycle on a docs change
- [ ] Write ADR 0002 recording your choice of cloud provider and why
- [ ] Protect the `main` branch so changes must arrive by pull request

> **Why this stage matters:** this is where the change-control story starts. A repo where
> everything was committed straight to `main` in one push tells a very different story than
> one with reviewed, described, incremental changes.

---

## Stage 1 — A working application, locally, with no cloud at all
**Skills: Python, pytest**
**Prerequisite: Stage 0**

- [ ] A single Python function that accepts a transaction and validates it
- [ ] Reject invalid transactions with clear, specific errors
- [ ] Unit tests covering valid input, each invalid case, and edge cases
- [ ] Store transactions in a local file or SQLite — deliberately simple
- [ ] Every state change appends a record to a local audit log

> **Do not skip this.** Getting the domain logic and the audit model right on your laptop,
> where iteration is free, is far easier than debugging it inside AWS. The audit model is the
> heart of this project.

---

## Stage 2 — Containerize
**Skills: Docker**
**Prerequisite: Stage 1**

- [ ] `Dockerfile` that builds and runs the application
- [ ] `docker-compose.yml` for local development
- [ ] Container runs as a non-root user
- [ ] Image builds reproducibly from a clean clone
- [ ] ADR recording your base image choice and why

---

## Stage 3 — Continuous integration
**Skills: GitHub Actions (or GitLab CI), YAML**
**Prerequisite: Stage 2**

- [ ] Pipeline runs on every pull request
- [ ] Lint (`ruff` or `flake8`) → unit tests → build container
- [ ] Pipeline **fails** the build on test failure — prove it with a deliberately broken commit,
      then fix it in the next commit
- [ ] Status badge in the README

> **Portfolio note:** that deliberately broken commit and its fix is evidence you understand
> what CI is *for*. Leave it in the history.

---

## Stage 4 — First infrastructure as code
**Skills: Terraform, AWS fundamentals, IAM**
**Prerequisite: AWS account + Terraform Associate coursework**

- [ ] Terraform creates an S3 bucket and nothing else — start small
- [ ] Remote state backend configured
- [ ] Bucket has versioning enabled, public access blocked, encryption on
- [ ] `terraform destroy` works cleanly — verify cost returns to zero
- [ ] ADR on remote state and why local state is unacceptable for team work

> **Cost discipline:** set a billing alarm before creating your first resource. Document your
> teardown procedure in `scripts/`. Running up a surprise bill is the most common way these
> projects die.

---

## Stage 5 — Deploy the application to AWS
**Skills: ECS/Fargate or Lambda, VPC, security groups**
**Prerequisite: Stage 4**

- [ ] Application runs in AWS, reachable through an API endpoint
- [ ] Networking defined in Terraform — private subnets, no public database
- [ ] Least-privilege IAM role per component, no wildcard permissions
- [ ] Secrets in Secrets Manager or Parameter Store, never in code or environment files

---

## Stage 6 — The immutable audit trail
**Skills: S3 Object Lock, versioning, CloudTrail**
**Prerequisite: Stage 5**

- [ ] Every transaction state change writes an audit record to S3
- [ ] S3 Object Lock in compliance mode — records cannot be deleted or altered, even by you
- [ ] CloudTrail enabled, logging to a separate bucket with restricted delete permissions
- [ ] Audit records include: what changed, who, when, from where, and a hash of prior state
- [ ] **Attempt to delete an audit record and document the failure** — that screenshot is evidence

> This is the stage that makes the project worth building. Everything before it is plumbing.

---

## Stage 7 — Security scanning in the pipeline
**Skills: tfsec/Checkov, Trivy, supply chain basics**
**Prerequisite: Stages 3 and 4**

- [ ] `terraform plan` runs on every pull request and posts the diff
- [ ] `tfsec` or `Checkov` scans infrastructure code, fails on high severity
- [ ] `Trivy` scans the container image, fails on critical CVEs
- [ ] Include one deliberately insecure branch the pipeline rejects — screenshot it

---

## Stage 8 — Controlled deployment
**Skills: CD, environments, approval gates**
**Prerequisite: Stage 7**

- [ ] Separate `dev` and `prod` environments in Terraform
- [ ] Deploy to `dev` automatically on merge to `main`
- [ ] Deploy to `prod` only after a **manual approval gate**
- [ ] Document the change-control flow in `docs/`

> The approval gate is a small technical detail that signals something large: that you
> understand production change control in a regulated environment.

---

## Stage 9 — Observability
**Skills: CloudWatch, metrics, alerting, runbooks**
**Prerequisite: Stage 5**

- [ ] Structured JSON logging throughout the application
- [ ] Metrics: transaction volume, error rate, processing latency
- [ ] Alarms on error-rate and latency thresholds
- [ ] A written runbook for each alarm: what it means, how to diagnose, how to resolve

> This is condition-based monitoring. You already know this discipline from HUMS — instrument
> the system, watch the trend, act before the failure. Say so in the runbook introduction.

---

## Stage 10 — The evidence package
**Skills: everything above, plus technical writing**
**Prerequisite: Stages 6 and 9**

- [ ] A script that generates a timestamped evidence package for a transaction or date range
- [ ] Complete `AUDIT.md` answering the assessor question from the README end to end
- [ ] Architecture diagram in `docs/diagrams/`
- [ ] Final README pass, written for a hiring manager who will spend ninety seconds on it

---

## Rules for the whole build

1. **Every stage ends with a working, committed state.** Never leave the repo broken.
2. **Branch for every change.** Even solo. The habit is the point.
3. **Write the ADR when you make the decision**, not months later when you've forgotten the alternatives.
4. **Tear down AWS resources when not actively working.** Budget alarm on from day one.
5. **When you get stuck, commit the partial work on a branch and write down what you tried.**
   That record is more valuable to your learning than a clean history.
