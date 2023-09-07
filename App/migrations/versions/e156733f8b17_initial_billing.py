"""Initial billing

Revision ID: e156733f8b17
Revises: 5d8ce588a9dd
Create Date: 2023-09-07 14:39:08.892633

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e156733f8b17'
down_revision: Union[str, None] = '5d8ce588a9dd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
