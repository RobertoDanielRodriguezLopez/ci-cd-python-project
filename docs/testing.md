# Testing Strategy

## Overview

This project implements a multi-level testing strategy aimed at validating
both business logic and API behavior in a reliable and reproducible way.

---

## Testing Levels

The test suite is divided into two main categories:

- **Unit tests**
- **API tests**

Each category serves a distinct purpose and is executed automatically
as part of the CI pipeline.

---

## Unit Tests

Unit tests validate the core business logic in isolation, without involving
the API layer or HTTP.

### Characteristics

- Execute individual functions and classes
- Do not require FastAPI or HTTP
- Fast execution
- Deterministic behavior

### Examples

Unit tests cover logic such as:

- Dictionary operations
- Cost calculation
- Word building logic

By keeping this logic independent from the API layer, tests remain simple,
focused, and easy to maintain.

---

## API Tests

API tests validate the HTTP interface exposed by the application.

They ensure that:

- Endpoints respond correctly
- Request/response contracts are respected
- HTTP status codes are appropriate

These tests are implemented using FastAPI’s `TestClient`.

### Characteristics

- Validate full request/response flow
- Focus on externally observable behavior
- Do not test implementation details

---

## Error Handling Coverage

The test suite prioritizes coverage of meaningful execution paths.

These paths are validated manually during development and through API usage.

---

## Coverage Philosophy

Code coverage is treated as a supporting metric, not a goal.

Key principles:

- Coverage thresholds are enforced via Quality Gates
- Meaningful logic paths are tested

The project achieves high coverage while maintaining a clean and readable test suite.

---

## Docker-Based Test Execution

All tests are executed inside Docker containers.

Benefits:

- Consistent execution environment
- Reproducible results across machines
- Identical behavior locally and in CI

This ensures that test results are not affected by local environment differences.

---

## CI Integration

Tests are automatically executed in the CI pipeline on every push
and pull request.

Test failures immediately stop the pipeline, preventing unvalidated
changes from progressing.