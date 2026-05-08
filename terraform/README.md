# Terraform – Infrastructure as Code

## Overview

This directory contains Terraform configuration used to provision and manage
real cloud infrastructure.

Terraform is an active and essential component of the deployment workflow,
responsible for creating and maintaining the infrastructure that hosts the
application in production.

Infrastructure changes are applied automatically during the Continuous
Deployment (CD) stage, after all validation and approval requirements are met.

---

## Managed Infrastructure

---

The Terraform configuration manages infrastructure components such as:

- EC2 instances used as the application runtime
- Security Groups controlling network access
- Networking configuration required for application exposure
- Remote backend and state locking for safe concurrent changes

All infrastructure resources are version‑controlled and auditable.

---

## Integration with CI/CD

Terraform is executed as part of the Continuous Deployment (CD) pipeline
implemented with GitHub Actions.

### When Terraform Runs

- Only on `main` branch changes
- Only after all CI checks pass
- Only after manual approval via GitHub Environments

### Pipeline Responsibilities

During deployment, Terraform:

1. Initializes the configured backend
2. Validates infrastructure definitions
3. Applies infrastructure changes idempotently
4. Produces outputs consumed by subsequent deployment steps

---

## State Management and Safety

Terraform state is managed using a remote backend with locking enabled.

This ensures:

- Safe concurrent terraform operations
- State consistency across pipeline runs
- Prevention of accidental or conflicting changes

---

## Security Considerations

- Terraform credentials are injected only during the CD job
- Secrets are scoped to the production environment
- Infrastructure changes require manual approval
- No credentials are exposed to CI or Pull Requests

## Usage Notes

Terraform is not intended to be run manually during normal development.

Expected usage is:

- Automated execution via GitHub Actions
- Controlled through branch protection and approvals
- Reviewed through code changes in Pull Requests