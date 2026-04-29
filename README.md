# CI/CD Python Project – Docker‑First DevSecOps Pipeline

## Project Overview

This project demonstrates a complete CI/CD pipeline for a Python application using a Docker‑first and DevSecOps approach.

The focus of the project is the design of a professional software delivery pipeline including testing, quality analysis, security checks, Infrastructure as Code, and work management.

---

## Project Goals

- Build a Docker‑first CI/CD pipeline
- Execute tests and coverage automatically
- Enforce code quality using SonarQube
- Integrate security checks into the pipeline
- Define infrastructure using Terraform (simulated)
- Simulate real team workflow using GitHub Projects

---

## Application Functionality

The application contains three Python tasks:

1. Dictionary  
   Stores and retrieves word definitions.

2. Cost Calculator  
   Calculates the total cost of items including tax and ignores missing items.

3. Word Builder  
   Builds a word by taking indexed characters from a list of words.

All functionality is covered by unit tests.

---

## Project Structure

ci-cd-python-project/
├── app/                    # Application source code
├── tests/                  # Unit tests
├── docker/                 # Docker and Docker Compose configuration
├── .github/workflows/      # CI/CD pipelines
├── terraform/              # Infrastructure as Code (simulated)
├── docs/                   # Technical documentation
├── README.md
└── requirements.txt

---

## Docker‑First Approach

All stages of the project run inside Docker containers:

- Development
- Testing
- CI/CD execution
- Security analysis
- Terraform execution

This guarantees consistent behavior across environments and removes local dependency issues.

---

## CI/CD Pipeline

The CI/CD pipeline automates the following stages:

1. Build and Test  
   - Docker build  
   - pytest execution  

2. Code Quality  
   - Code coverage using pytest‑cov  
   - SonarQube analysis  
   - Quality Gate enforcement  

3. Security (DevSecOps)  
   - Bandit for Python static analysis  
   - pip‑audit for dependency vulnerability scanning  

4. Infrastructure  
   - Terraform plan and apply (simulated, no cloud resources)

---

## Code Quality and Coverage

- Unit tests are implemented using pytest
- Coverage is generated using pytest‑cov
- Coverage reports are imported into SonarQube
- A Quality Gate enforces minimum coverage requirements

---

## Security

Security checks are integrated into the pipeline:

- Bandit performs static code analysis
- pip‑audit checks dependencies for known vulnerabilities

---

## Infrastructure as Code (Terraform)

Infrastructure is defined using Terraform without provisioning real cloud resources.

Features:
- Modular Terraform design
- Environment separation (dev, qa, prod)
- Execution inside Docker
- Zero cost

Terraform is executed using:
- terraform plan
- terraform apply -auto-approve

---

## Work Management

Project work is tracked using GitHub Projects to simulate a real team workflow.

The board includes:
- Backlog
- To Do
- In Progress
- Code Review
- Done

Issues represent tasks and real bugs encountered during development.

---

## Conclusion

This project demonstrates real‑world software delivery practices including CI/CD, DevSecOps, Infrastructure as Code, and team workflow management.