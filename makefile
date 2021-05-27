update:
	poetry update

install:
	poetry install

docs-build:
	poetry run mkdocs build

docs-serve: docs-build
	poetry run mkdocs serve --dev-addr 127.0.0.1:5000

docs-clean:
	rm -rf site/

test:
	poetry run pytest --no-cov
