# Architecture

## Overview

This project is designed to demonstrate a production-style CI/CD pipeline
for a Python backend application, focusing on automation, quality, security,
and reproducibility rather than application complexity.

The architecture follows clear separation of concerns between application logic,
API layer, testing, infrastructure, and CI/CD configuration.

---

## Project Structure

![CI/CD Pipeline](images/Project-Structure.png)

---

## Application Layer

The application logic is intentionally simple and deterministic.
Its purpose is to serve as a stable base for demonstrating testing,
CI/CD, and quality practices.

Core logic is kept independent from the API layer to allow:

- Unit testing without HTTP
- Reuse of logic
- Clear separation of responsibilities

---

## API Layer

The API is implemented using FastAPI and exposes the application logic
through a REST interface.

Key design principles:

- Clear request and response models
- Explicit HTTP status codes
- Swagger/OpenAPI documentation

---

## Testing Strategy

Testing is split into two levels:

- **Unit tests**: validate core business logic in isolation
- **API tests**: validate HTTP contracts and responses

All tests are executed inside Docker to ensure consistent behavior
across environments.

---

## Containerization

The project follows a Docker-first approach:

- No reliance on local Python environments
- Reproducible execution
- Same runtime used locally and in CI