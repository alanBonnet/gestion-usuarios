"""empty message

Revision ID: c9d5a149e8ec
Revises: ca67f080bbe1
Create Date: 2024-08-30 12:06:37.353027

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9d5a149e8ec'
down_revision: Union[str, None] = 'ca67f080bbe1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
