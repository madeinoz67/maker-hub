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

ci: codespell lint bandit test ## Run all checks (codespell, lint, bandit, test)
.PHONY: ci

test:  ## Run tests
	poetry run pytest . --no-cov
.PHONY: test

lint:  ## Run linting with flake8 
	poetry run flake8 . \
	--count \
	--ignore=F841,W503 \
	--max-complexity=26 \
	--max-line-length=88 \
	--statistics \
	--exclude .venv
.PHONY: lint

codespell:  ## Find typos with codespell
	poetry run codespell --ignore-words-list=nd,nin --skip=".venv"
.PHONY: codespell

bandit:  ## Run static security analysis with bandit
	poetry run bandit app -r
.PHONY: bandit

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

docker-compose: ## Run docker-compose
	docker-compose up
.PHONY: docker-compose

salted: ## generate salt
	poetry run python gen_Salt.py
.PHONY: salted

help: Makefile
	@grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'
