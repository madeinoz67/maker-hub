update:
	poetry update

install:
	poetry install

docs-build:
	poetry run mkdocs build

docs-serve: docs-build
	poetry run mkdocs serve

docs-clean:
	rm -rf site/

test:
	pytest --no-cov
