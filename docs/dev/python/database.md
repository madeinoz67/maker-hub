The project currently uses the light weight SQLite as its underlying database.

## Schema

The projects database schema is managed by [alembic :link:](https://alembic.sqlalchemy.org/en/latest/index.html)

### Making Schema Changes:

### 1. Make a new revision fo the schema

```shell
make schema-revision message="some notes about the changes to the schema revision"
```
or
```shell
poetry run alembic revision --autogenerate -m "some notes about the changes to the schema revision"
```

A new script will be created in the alembic migrations directory, encompassing all the schema changes to the underlying application models.

!!! example
    `...maker_hub/app/db/migrations/versions/82154bb5bc9a_.py ...  done`

!!! important note
    This new revision file should be added to git as soon as possible.

### 2. Editing the 'upgrade' and 'downgrade' functions in the new revision script

In the new revision script file created in *Step 1* there will be 2 sections that require updating to reflect the changes to the schema you will make, i.e. the upgrading of the current schema and downgrading of the new schema back to its previous step.

!!! Example Revision Script

    ```python
    """Create maker-hub parts table

    Revision ID: df07dde39ce9
    Revises: 
    Create Date: 2021-05-29 21:12:31.941787

    """
    import datetime

    import sqlalchemy as sa
    from alembic import op

    # revision identifiers, used by Alembic.
    revision = "df07dde39ce9"
    down_revision = None
    branch_labels = None
    depends_on = None


    def create_parts_table() -> None:
        op.create_table(
            "part",
            sa.Column("id", sa.String, primary_key=True),
            sa.Column("name", sa.String, nullable=True, index=True),
            sa.Column("description", sa.String, nullable=True, index=True),
            sa.Column("created_at", sa.DateTime, default=datetime.datetime.now, index=True),
            sa.Column("updated_at", sa.DateTime, default=datetime.datetime.now, index=True),
            sa.Column("notes", sa.String, nullable=True),
            sa.Column("footprint", sa.String, nullable=True, index=True),
            sa.Column("manufacturer", sa.String, nullable=True, index=True),
            sa.Column(
                "mpn", sa.String, nullable=True, index=True
            ),  # Manufacturers Part Number)
        )


    def upgrade() -> None:
        create_parts_table()


    def downgrade() -> None:
        op.drop_table("part")
    ```

Just like any other python scripts, functions can be written and python modules can be added, in the example above for the upgrade function, its calling a developer created function *create_parts_table()*

!!! Note
    For more detailed information please refer to the [alembic documentation :link:](https://alembic.sqlalchemy.org/en/latest/index.html)

### 3. Upgrading the current schema with the new revision

```shell
make schema-upgrade
```
or
```shell
poetry run alembic upgrade head
```

This will perform the upgrade on the current schema head.

### 4. To rollback a schema change to the previous version

```shell
make schema-downgrade
```
or
```shell
poetry run alembic downgrade -1
```

This will perform the upgrade on the current schema head.
