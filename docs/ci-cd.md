# CI/CD Pipeline

## Overview

This project implements a CI/CD pipeline using **GitHub Actions**
with a strong focus on automation, reproducibility, and quality assurance.

The pipeline is designed to validate the application on every change
without requiring any manual steps, ensuring that code quality and
security standards are consistently enforced.

---

## Pipeline Triggers

The CI pipeline is executed automatically on:

- Every push to the `main` branch
- Every pull request

This ensures continuous validation of changes before and after merging.

---

## Docker-First Approach

All CI steps are executed inside Docker containers.

Benefits of this approach:

- Eliminates "it works on my machine" issues
- Ensures identical runtime environments locally and in CI
- Simplifies dependency management
- Provides reproducible builds

No system-level Python installation is required on the CI runner.

---

## Pipeline Stages

The CI pipeline is composed of the following stages:

### 1. Code Checkout

The repository is checked out with full Git history available.
This allows tools like SonarQube to properly analyze code history
and blame information.

---

### 2. Docker Image Build

A Docker image is built using the project Dockerfile.
This image is reused across subsequent steps to ensure consistency.

---

### 3. Test Execution

Both unit tests and API tests are executed inside the Docker container.

- Unit tests validate core business logic
- API tests validate HTTP contracts and responses

Tests are treated as a quality gate: failures stop the pipeline.

---

### 4. Coverage Generation

Test execution also generates a coverage report.
Coverage metrics are later consumed by SonarQube for quality analysis.

---

### 5. Static Code Analysis (SonarQube)

SonarQube is used to analyze:

- Code quality
- Code coverage
- Maintainability
- Reliability
- Security hotspots

The project enforces a Quality Gate to prevent regressions in quality.

---

### 6. Security Analysis

Security checks are integrated into the pipeline:

- **Bandit** for static security analysis
- **pip-audit** for dependency vulnerability scanning

These checks provide early feedback on potential security risks.

---

## Quality Gates

The pipeline is configured to fail if:

- Tests do not pass
- Code quality degrades below defined thresholds
- Critical security issues are detected

This ensures that only validated changes reach the main branch.

---

## Failure Strategy

The pipeline follows a fail-fast strategy:

- Any failing stage stops the pipeline immediately
- Clear logs are provided to identify the root cause
- No partial or ambiguous states are allowed

---

## Design Decisions

Key decisions behind this pipeline:

- Prefer clarity over overly complex orchestration
- Use standard and widely adopted tools
- Avoid environment-specific assumptions
- Make failures explicit and visible