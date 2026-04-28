
# CI/CD Python Project – Docker First

This repository demonstrates how to design a professional CI/CD pipeline
using Docker as the core execution environment.

The project intentionally uses simple Python tasks so that the focus remains on:
- Continuous Integration
- Continuous Delivery
- Code Quality
- Security
- Reproducibility

## Architecture Overview
The project is inspired by real-world DevSecOps pipelines including:
- Version control and code reviews
- Automated testing and static analysis
- Security testing
- Artifact generation
- Release and deployment stages

## Project Structure
app/           → Python application modules
tests/         → Unit tests
docker/        → Docker & Docker Compose
.github/       → CI/CD pipelines
terraform/     → Infrastructure as Code (simulation)
docs/          → Technical documentation


## Requirements
- Git
- Docker (Docker Desktop)

## Development Model
The project is developed incrementally:
1. Repository & CI skeleton
2. Python logic and tests
3. Quality gates and security
4. Infrastructure-as-Code and approvals