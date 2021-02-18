.DEFAULT_GOAL := build
.PHONY: build publish package coverage test lint docs venv
PROJ_SLUG = maker_hub
PY_VERSION = 3.9
LINTER = flake8

build: 
	npm install
	npm run-script build

run:
	npm install
	npm run-script build
	npm start

migrate:
	flask db init
	flask db migrate
	flask db upgrade

lint:
	$(LINTER) $(PROJ_SLUG)

test: lint
	py.test --cov-report term --cov=$(PROJ_SLUG) tests/

venv :
	pipenv shell

install:
	pipenv install --dev