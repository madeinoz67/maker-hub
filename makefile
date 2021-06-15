SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules
.DEFAULT_GOAL := help

install:  ## install all dependencies locally
	poetry install
.PHONY: install

update:  ## update project dependencies locally (run after git update)
	poetry update
.PHONY: update

ci: typecheck lint test ## Run all checks (test, lint, typecheck)
.PHONY: ci

test:  ## Run tests
	poetry run pytest . 
.PHONY: test

lint:  ## Run linting
	poetry run black --check .
	poetry run isort -c .
	poetry run flake8 .
	poetry run pydocstyle .
.PHONY: lint

lint-fix:  ## Run autoformatters
	poetry run black .
	poetry run isort .
.PHONY: lint-fix

typecheck:  ## Run typechecking
	poetry run mypy --show-error-codes --pretty .
.PHONY: typecheck

docs-build: ## Build documentation
	poetry run mkdocs build
.PHONY: docs-build

docs-serve: docs-build ## Build docs and server on port localhost:5000
	poetry run mkdocs serve --dev-addr 127.0.0.1:5000
.PHONY: docs-serve

docs-clean: ## Cleanup docs generation
	rm -rf site/
.PHONY: docs-clean

schema-revision: ## Generate new DB Schema Revision
	poetry run alembic revision --autogenerate -m "$(message)"
.PHONY: schema-revision

schema-upgrade: ## Migrate DB Schema to latest
	poetry run alembic upgrade head
.PHONY: schema-upgrade

schema-downgrade:  ## Downgrade DB schema to previous version
	poetry run alembic downgrade -1
.PHONY: schema-downgrade

help: Makefile
	@grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'
