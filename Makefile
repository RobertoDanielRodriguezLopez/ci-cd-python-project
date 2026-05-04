# =========================
# Variables
# =========================
APP_SERVICE=app
DOCKER_COMPOSE=docker compose -f docker/docker-compose.yml
TERRAFORM_DIR=terraform

# =========================
# Docker
# =========================
docker-build:
	$(DOCKER_COMPOSE) build

docker-up:
	$(DOCKER_COMPOSE) up

docker-down:
	$(DOCKER_COMPOSE) down

# =========================
# Tests
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
	@echo Running dependency audit (informational)
	-$(DOCKER_COMPOSE) run --rm $(APP_SERVICE) pip-audit



security: security-bandit security-deps

# =========================
# Coverage (optional)
# =========================
coverage:
	$(DOCKER_COMPOSE) run --rm $(APP_SERVICE) pytest --cov=app

# =========================
# Terraform
# =========================
terraform-init:
	terraform -chdir=$(TERRAFORM_DIR) init

terraform-validate:
	terraform -chdir=$(TERRAFORM_DIR) validate

infra: terraform-init terraform-validate

# =========================
# CI LOCAL
# =========================
ci: docker-build test security infra
	@echo "CI local passed successfully ✅ "

# =========================
# Development
# =========================
dev: docker-build docker-up

dev-safe: ci docker-up

# =========================
# Cleanup
# =========================
clean: docker-down

.DEFAULT_GOAL := ci