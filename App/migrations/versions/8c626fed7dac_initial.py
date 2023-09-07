"""initial

Revision ID: 8c626fed7dac
Revises: 8903ed92a47f
Create Date: 2023-09-07 14:01:38.883067

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c626fed7dac'
down_revision: Union[str, None] = '8903ed92a47f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
