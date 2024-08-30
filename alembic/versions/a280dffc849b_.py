"""empty message

Revision ID: a280dffc849b
Revises: c9d5a149e8ec
Create Date: 2024-08-30 12:07:44.539812

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a280dffc849b'
down_revision: Union[str, None] = 'c9d5a149e8ec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
