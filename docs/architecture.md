# Architecture

## Overview

This project is designed to demonstrate a production‑ready software delivery
architecture for a Python backend application.

The architecture is clear with the separation of responsibilities between:

- Application logic
- Runtime execution
- CI/CD orchestration
- Infrastructure provisioning
- Security and quality enforcement

The system is designed to closely resemble real‑world architectures used
in professional engineering teams.

---

## High‑Level Architecture

Developer → Pull Request → CI → Quality Gate → main → CD (approval) → EC2 → Docker → API

The architecture is composed of four explicit layers, each with a clearly
defined responsibility.

---

## Application Layer

The application logic is intentionally simple and deterministic.
Its purpose is to act as a stable base for demonstrating:

- Testability
- CI/CD enforcement
- Security controls
- Production runtime isolation

---

## API Layer

The API is implemented using FastAPI and exposes application functionality
through a REST interface.

**Key design characteristics:**

- Explicit request and response models
- Clear HTTP status codes
- Automatic OpenAPI / Swagger documentation
- Stateless request handling

The API layer depends on the application layer, but not vice versa.

---

## Runtime Architecture (Docker)

Docker is the production runtime of the system.

It is not used as a CI artifact and not executed inside GitHub Actions.
Instead, Docker runs directly on the EC2 instance.

**Key Principles**

- Docker runs only on the EC2 host
- GitHub Actions never executes the application
- The application always runs inside a container
- The same runtime is used locally and in production

**Runtime Components**

- Dockerfile
Defines a reproducible build for the application runtime


- docker-compose.yml
Orchestrates container execution and application startup


Containers isolate the application from the host operating system and ensure
consistent behavior across environments.

---

## Deployment Architecture (EC2 + Docker)

During a production deployment:

1. Terraform ensures the EC2 infrastructure exists
2. GitHub Actions connects to the EC2 instance via SSH
3. The EC2 host pulls the latest code from main
4. Docker Compose rebuilds the application image
5. The container is restarted
6. The API runs inside Docker using uvicorn

Once deployed, the container continues running independently of the pipeline.

---

## CI/CD Separation of Concerns

The architecture enforces a clear separation between CI and CD.

**Continuous Integration (CI)**

CI is responsible for validation only:

- Unit and API tests
- Static security analysis
- Dependency vulnerability scanning
- SonarCloud quality analysis
- Quality Gate enforcement

CI never deploys code and never accesses production credentials.

**Continuous Deployment (CD)**

CD is responsible for production changes:

- Infrastructure provisioning via Terraform
- Application deployment via Docker
- Runtime health verification

CD is protected by manual approvals and environment‑scoped secrets.

---

## Infrastructure Layer (Terraform)

Infrastructure is provisioned using Terraform.

Key architectural principles:

- Infrastructure is declarative
- State is remote and locked
- Deployments are idempotent
- Infrastructure lifecycle is independent from application logic

Terraform executions occur only during controlled deployment stages.

---

## Security and Governance

Security is enforced across multiple layers of the architecture:

- Static analysis and dependency scanning during CI
- Quality Gates blocking unapproved changes
- Branch protection enforcing controlled merges
- Environment‑based approval for production deployments
- Secrets scoped to environments

Security controls are integrated directly into the workflow.