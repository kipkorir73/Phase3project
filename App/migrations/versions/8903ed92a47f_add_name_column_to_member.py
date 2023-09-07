"""Add name column to Member

Revision ID: 8903ed92a47f
Revises: b85f4d206581
Create Date: 2023-09-07 13:51:03.980584

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8903ed92a47f'
down_revision: Union[str, None] = 'b85f4d206581'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
