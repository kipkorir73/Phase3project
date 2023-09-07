"""Initial ration

Revision ID: 8b421c8ff379
Revises: 2a6fc86f560e
Create Date: 2023-09-06 19:35:56.263607

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8b421c8ff379'
down_revision: Union[str, None] = '2a6fc86f560e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
