# Security

## Overview

Security in this project is implemented following a DevSecOps approach,
where security controls are integrated directly into the CI/CD pipeline
rather than applied as a separate or manual process.

The objective is not to provide exhaustive enterprise level security,
but to demonstrate how security concerns are enforced early, automatically,
and consistently as part of the software delivery lifecycle.

---

## Security Scope

The security model focuses on early‑stage application and pipeline security.

Covered areas include:

- Static analysis of application source code
- Detection of known vulnerabilities in dependencies
- Enforcement of security rules during Pull Requests
- Blocking of unapproved or risky changes before merge

Security checks are designed to be:

- Automated
- Repeatable
- Fast

---

## Static Application Security Testing (SAST)

### Tool: Bandit

**Bandit** is used for static analysis of Python source code.

Bandit detects common security issues, including:

- Use of insecure functions
- Weak cryptographic patterns
- Hardcoded credentials or secrets
- Potential injection vectors

Bandit is executed automatically during Continuous Integration (CI).

### Enforcement

- Findings are reported during Pull Requests
- Critical findings cause the CI pipeline to fail
- Failed security checks block PR merges automatically

This ensures insecure code never reaches the main branch.

---

## Dependency Vulnerability Scanning

### Tool: pip‑audit

**pip‑audit** scans project dependencies against known vulnerability databases.

The scan identifies:

- Vulnerable dependencies
- Outdated packages with known CVEs
- Supply‑chain risks introduced via third‑party libraries

### Enforcement

- Dependency scanning runs in CI
- Findings are visible directly in Pipeline logs
- Vulnerabilities are treated as quality signals, not optional warnings

This provides early visibility into dependency‑level risks.

---

## SonarCloud Security Analysis

Security analysis is complemented by **SonarCloud**, which evaluates:

- Security hotspots
- Code smells related to insecure patterns
- Maintainability concerns that may lead to future vulnerabilities

SonarCloud security findings are evaluated as part of the Quality Gate.

A failing Quality Gate blocks Pull Request merges automatically.

---

## CI Integration and Enforcement

Security checks are deeply integrated into CI:

- Executed automatically on every Pull Request
- No manual intervention required
- Failures immediately stop the pipeline
- Security issues are surfaced before merge, not after deployment

---

## Production Security Controls

Production access is protected through pipeline governance:

- No direct pushes to main
- Pull Requests and CI success required
- Manual approval required for production deployments
- Secrets scoped to the production environment
- Infrastructure changes controlled via Terraform

While application‑level security is enforced in CI, production deployment security
is managed through workflow and infrastructure controls.