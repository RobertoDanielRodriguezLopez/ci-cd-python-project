# Testing Strategy

## Overview

This project implements a multi‑level automated testing strategy designed
to validate both business logic and API behavior in a reliable and
repeatable way.

Testing exists to support quality enforcement, not as an isolated activity.
All tests are integrated into the Continuous Integration (CI) pipeline and
are mandatory for merging changes into `main`.

---

## Testing Levels

The test suite is divided into two primary levels:

- **Unit tests**
- **API tests**

Each level serves a distinct purpose and contributes to overall confidence
in the system.

---

## Unit Tests

Unit tests validate core business logic in complete isolation from the API
layer and HTTP concerns.

### Characteristics

- Execute individual functions and classes
- No dependency on FastAPI or HTTP
- Fast execution
- Deterministic and repeatable behavior

### Coverage

Unit tests cover logic such as:

- Dictionary operations
- Cost calculation logic
- Word building functionality

By keeping core logic independent from the API layer, unit tests remain:
- Simple
- Focused
- Easy to extend and maintain

---

## API Tests

API tests validate the HTTP interface exposed by the application.

These tests ensure:

- Endpoints respond correctly
- Request/response contracts are respected
- HTTP status codes are accurate
- Application behavior matches external expectations

API tests are implemented using FastAPI’s `TestClient`, avoiding
external services or network dependencies.

---

## Error Handling and Edge Cases

The test suite prioritizes coverage of meaningful execution paths, including:

- Valid inputs
- Edge cases
- Error scenarios exposed via the API

The goal is not exhaustive permutation testing, but confidence in
real‑world usage patterns.

---

## CI Integration

All tests are executed automatically as part of Continuous Integration (CI).

CI behavior:

- Tests run on every Pull Request
- Tests run on every push to `main`
- Test failures immediately stop the pipeline
- Failed tests block merges automatically

This guarantees that no untested changes reach the main branch.

---

## Runtime Separation

Testing and production runtime are intentionally separated:

- Tests run during CI execution
- Production runtime uses Docker on EC2
- CI does not execute the application as a running service

This separation ensures that testing remains fast and deterministic while
production focuses on stable runtime execution.