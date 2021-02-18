.DEFAULT_GOAL := build
.PHONY: build coverage test lint docs venv
PROJ_SLUG = maker_hub
PY_VERSION = 3.9
LINTER = flake8

build: 
	npm install
	npm run-script build

run: build
	npm start


db_init: 
	flask db init

migrate:
	flask db migrate
	flask db upgrade

init: db_init migrate

lint:
	$(LINTER) $(PROJ_SLUG)

coverage: lint
	py.test --cov-report term --cov=$(PROJ_SLUG) tests/

test: lint
	py.test tests/

venv :
	pipenv shell

install:
	pipenv install --dev