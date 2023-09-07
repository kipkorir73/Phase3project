"""Initial schema

Revision ID: e41f291ef149
Revises: 8c626fed7dac
Create Date: 2023-09-07 14:37:34.767363

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e41f291ef149'
down_revision: Union[str, None] = '8c626fed7dac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
