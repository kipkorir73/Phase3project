"""Initial schema

Revision ID: b85f4d206581
Revises: 8b421c8ff379
Create Date: 2023-09-06 20:40:16.564856

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b85f4d206581'
down_revision: Union[str, None] = '8b421c8ff379'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
