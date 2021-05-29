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
