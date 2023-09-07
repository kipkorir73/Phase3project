"""Initial Attendance

Revision ID: 5d8ce588a9dd
Revises: e41f291ef149
Create Date: 2023-09-07 14:38:30.981733

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5d8ce588a9dd'
down_revision: Union[str, None] = 'e41f291ef149'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
