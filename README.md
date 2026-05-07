# CI/CD Python Project

## Project Overview

This project demonstrates a production‑ready CI/CD pipeline for a Python
application, implemented using Docker, GitHub Actions, Terraform, and
SonarCloud, following modern DevSecOps and infrastructure governance
principles.

The goal of the project is not application complexity, but to showcase a
real‑world software delivery architecture, including:

- CI with quality and security enforcement
- Protected CD with approvals
- Infrastructure as Code
- Container‑based runtime in production
- Release management and governance practices

This repository represents a complete, hardened delivery workflow comparable
to what is used in professional engineering teams.

---

## Project Structure

The repository is organized to clearly separate application code, CI/CD
pipelines, infrastructure, runtime configuration, and documentation.

![Project Structure](docs/images/Project-Structure.png)

---

## Application Overview

---

The application itself is intentionally simple and deterministic, acting as
a stable vehicle for CI/CD and architectural practices.
It includes three Python components:


1. **Dictionary**
Stores and retrieves word definitions.


2. **Cost Calculator**
Calculates total cost including tax, ignoring missing items.


3. **Word Builder**
Builds a word using indexed characters from a list of words.


All application behavior is covered by automated unit and API tests.

---

## High‑Level Architecture

---

Developer → Pull Request → CI → Quality Gate → main → CD (approval) → EC2 → Docker → API

The system is composed of four clearly separated layers:

- CI orchestration (GitHub Actions)
- Infrastructure provisioning (Terraform)
- Runtime orchestration (Docker + Docker Compose)
- Application execution (Python API)

---

## Docker Architecture (Runtime Layer)

---

Docker is not part of CI artifacts in this project — it is the production
runtime.

Key Principles

- Docker runs only on the EC2 instance
- GitHub Actions never runs the application
- The EC2 host executes Docker locally
- The application always runs inside a container

How Docker Is Used

- Dockerfile defines a reproducible runtime image
- docker-compose.yml orchestrates the application
- The same configuration is used locally and in production
- Containers isolate the application from the host OS

During Deployment

On every production deployment:

1. The EC2 instance pulls the latest code from main
2. Docker Compose rebuilds the image using the Dockerfile
3. The application container is restarted
4. The API runs via uvicorn inside the container
5. Docker continues running after the pipeline finishes

Docker is the long‑lived execution layer of the system.

---

## CI/CD Pipeline Overview

---

![CI/CD Pipeline](docs/images/CI-CD-pipeline.png)

---

## Continuous Integration (CI)

---

Triggered On

- Pull Requests
- Pushes to main

CI Responsibilities

✅ Run unit and API tests
✅ Run security scans (Bandit, pip‑audit)
✅ Execute SonarCloud analysis
✅ Enforce Quality Gates
❌ No deployments
❌ No infrastructure changes
❌ No production secrets

Quality Gates

Pull Requests cannot be merged unless:

- Tests pass
- Security checks pass
- SonarCloud Quality Gate passes

This ensures quality enforcement is automatic and non‑optional.

---

## Continuous Deployment (CD)

---

Triggered On

- Push to main
- All CI status checks passing
- Manual approval via GitHub Environment

CD Responsibilities

- Apply Terraform configuration
- Create or update the EC2 instance
- Obtain the EC2 public IP dynamically
- Connect to the instance via SSH
- Deploy the application using Docker Compose
- Execute a health check after deployment

Production Protection

- Deploy requires manual approval (environment: production)
- Production secrets are environment‑scoped
- No deployments occur without explicit authorization

---

## Infrastructure as Code (Terraform)

---

Terraform manages:

- EC2 instance
- Security groups
- Backend state (remote + locking)

Key principles:

- Infrastructure is declarative
- State is remote and locked
- Deployments are repeatable and idempotent
- Infrastructure is independent from CI logic

Terraform is executed only during CD, never in PRs.

## Security (DevSecOps)

---

Security is enforced early in the lifecycle:

- - Bandit: static analysis of Python code
- - pip‑audit: dependency vulnerability scanning
- - SonarCloud: quality, security, maintainability analysis

Security findings in PRs block merges automatically.

---

## Code Coverage

---

- Coverage is generated during CI using pytest‑cov
- Reports are consumed by SonarCloud
- Coverage artifacts are not committed to the repository

Coverage enforcement happens via Quality Gates, not manual review.

---

## Branch Protection & Governance

---

The main branch is fully protected:

- No direct pushes
- Pull Requests required
- CI status checks required
- SonarCloud Quality Gate required
- Manual code review required
- Force pushes disabled

Production deployments are additionally gated via environments.

---

## Local Development

---

Common commands:

make dev        # Run application locally using Docker
make ci         # Run CI checks locally
make coverage   # Local coverage summary (console only)

The local environment mirrors production behavior via Docker.

---

## Work Management

---

Project work is tracked using GitHub Projects, simulating a real team workflow:


- Backlog
- To Do
- In Progress
- Code Review
- Done