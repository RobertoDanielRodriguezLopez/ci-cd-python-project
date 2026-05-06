# =========================
# Configuration
# =========================
APP_SERVICE := app
DOCKER_COMPOSE := docker compose -f docker/docker-compose.yml
TERRAFORM_DIR := terraform

.DEFAULT_GOAL := help

# =========================
# Help
# =========================
help:
	@echo ""
	@echo "Available commands:"
	@echo ""
	@echo " Development:"
	@echo "   dev           Build and run the app locally (detached)"
	@echo "   dev-safe      Run CI checks locally, then start the app"
	@echo ""
	@echo " Testing:"
	@echo "   test          Run unit and API tests"
	@echo "   coverage      Run test coverage report"
	@echo ""
	@echo " Security:"
	@echo "   security      Run security scans (bandit, pip-audit)"
	@echo ""
	@echo " Infrastructure (safe):"
	@echo "   infra-check   Terraform init + validate (NO apply)"
	@echo ""
	@echo " Cleanup:"
	@echo "   clean         Stop local containers"
	@echo ""

# =========================
# Docker (Local Dev Only)
# =========================
docker-build:
	$(DOCKER_COMPOSE) build

docker-up:
	$(DOCKER_COMPOSE) up -d

docker-down:
	$(DOCKER_COMPOSE) down

# =========================
# Tests (Local CI Mirror)
# =========================
test-unit:
	$(DOCKER_COMPOSE) run --rm $(APP_SERVICE) pytest tests/unit

test-api:
	$(DOCKER_COMPOSE) run --rm $(APP_SERVICE) pytest tests/api

test: test-unit test-api

# =========================
# Security
# =========================
security-bandit:
	$(DOCKER_COMPOSE) run --rm $(APP_SERVICE) bandit -r app

security-deps:
	@echo "Running dependency audit (informational)"
	-$(DOCKER_COMPOSE) run --rm $(APP_SERVICE) pip-audit

security: security-bandit security-deps

# =========================
# Coverage (Optional)
# =========================
coverage:
	$(DOCKER_COMPOSE) run --rm \
        -e COVERAGE_FILE=/tmp/.coverage \
        $(APP_SERVICE) pytest --cov=app --cov-report=term

# =========================
# Terraform (Safe Operations Only)
# =========================
terraform-init:
	terraform -chdir=$(TERRAFORM_DIR) init

terraform-validate:
	terraform -chdir=$(TERRAFORM_DIR) validate

infra-check: terraform-init terraform-validate
	@echo "Terraform validation complete ✅"
	@echo "NOTE: apply/destroy are intentionally NOT part of the Makefile"

# =========================
# Local CI (Mirror of GitHub Actions CI)
# =========================
ci: docker-build test security infra-check
	@echo "Local CI checks passed ✅"

# =========================
# Development Flows
# =========================
dev: docker-build docker-up

dev-safe: ci docker-up

# =========================
# Cleanup
# =========================
clean: docker-down
