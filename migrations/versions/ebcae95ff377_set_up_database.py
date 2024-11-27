"""set up database

Revision ID: ebcae95ff377
Revises: 
Create Date: 2024-11-27 16:37:04.400585

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "ebcae95ff377"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "missions",
        sa.Column("complete_state", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "spy_cats",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("breed", sa.String(), nullable=False),
        sa.Column("salary", sa.Float(), nullable=False),
        sa.Column("years_experience", sa.Float(), nullable=False),
        sa.Column("mission_id", sa.Integer(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["mission_id"],
            ["missions.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("mission_id"),
    )
    op.create_table(
        "targets",
        sa.Column("mission_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("country", sa.String(), nullable=False),
        sa.Column("note", sa.String(), nullable=False),
        sa.Column("complete_state", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["mission_id"],
            ["missions.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("targets")
    op.drop_table("spy_cats")
    op.drop_table("missions")
    # ### end Alembic commands ###
