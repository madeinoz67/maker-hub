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

lint:
	poetry run flake8

test: lint
	poetry run pytest --no-cov

schema-revision:
	poetry run alembic revision --autogenerate -m "$(message)"

schema-upgrade:
	poetry run alembic upgrade head

schema-downgrade:
	poetry run alembic downgrade -1
