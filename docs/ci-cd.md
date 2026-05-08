# CI/CD Pipeline

## Overview

This project implements a production‑ready CI/CD pipeline using
GitHub Actions, designed to enforce quality, security, and controlled
deployments.

The pipeline follows a strict separation of responsibilities:

- **Continuous Integration (CI)** validates every change
- **Continuous Deployment (CD)** deploys only approved and validated code

---

## Pipeline Triggers

### Continuous Integration (CI)

CI is executed automatically on:

- Every Pull Request
- Every push to the main branch

This guarantees continuous validation before and after merges.

---

### Continuous Deployment (CD)

CD is executed only when:

- Code is pushed to main
- All required CI checks pass
- Manual approval is granted via GitHub Environments

No deployments occur from feature branches or Pull Requests.

---

## CI/CD Separation of Concerns

A strict separation exists between CI and CD.

### Continuous Integration (CI)

CI focuses exclusively on verification, never on deployment.

CI responsibilities include:

- Executing unit tests
- Executing API tests
- Running static security analysis
- Scanning dependencies for vulnerabilities
- Performing SonarCloud analysis
- Enforcing Quality Gates

---

### Continuous Deployment (CD)


CD is responsible for production changes only.

CD responsibilities include:

- Applying Terraform infrastructure changes
- Deploying the application to EC2
- Managing the Docker runtime lifecycle
- Verifying application health post‑deployment

CD is protected by:
- Manual approval
- Environment‑scoped secrets
- Branch protection rules

---

## Continuous Integration Pipeline

### CI Stages

1. **Code Checkout**  
   The repository is checked out with full history available to ensure
   accurate analysis by quality tools.

2. **Test Execution**  
   - Unit tests validate core business logic
   - API tests validate HTTP contracts and responses  
   Test failures immediately stop the pipeline.

3. **Security Analysis**  
   - **Bandit** performs static analysis of Python code
   - **pip‑audit** scans dependencies for known vulnerabilities

4. **SonarCloud Analysis**  
   - Code quality
   - Coverage on new code
   - Maintainability
   - Reliability
   - Security issues

5. **Quality Gate Enforcement**  
   A Quality Gate determines whether the change is acceptable.  
   Failing the Quality Gate blocks Pull Request merges automatically.

---

## Quality Gates

A Pull Request cannot be merged unless:

- All tests pass
- Security checks pass
- SonarCloud Quality Gate passes

---

## Continuous Deployment Pipeline

### Deployment Flow

When CD is triggered:

1. Terraform validates and applies infrastructure changes
2. The EC2 public IP is retrieved dynamically from Terraform outputs
3. GitHub Actions connects to the EC2 instance via SSH
4. The instance pulls the latest code from main
5. Docker Compose rebuilds and restarts the application container
6. A health check verifies successful deployment

---

### Production Protection

Production deployment is protected by:

- GitHub Environments (production)
- Manual approval before deployment
- Secrets scoped exclusively to the production environment

---

## Docker in the Deployment Pipeline

Docker is the runtime environment, not a CI artifact.

Key characteristics:

- Docker runs only on the EC2 instance
- GitHub Actions never runs application containers
- Docker Compose orchestrates the application lifecycle
- The same Docker configuration is used locally and in production

After deployment, the application continues running independently of
the pipeline.

---

## Failure Strategy

The pipeline follows a fail‑fast strategy:

- Any failing CI stage stops execution immediately
- Clear logs identify the source of failure
- No partial deployments are allowed
- Production changes are applied only after full validation