"""little fix for reviews and books

Revision ID: 67a914e208f0
Revises: c89b0f5432b5
Create Date: 2025-02-28 00:48:21.170489

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '67a914e208f0'
down_revision: Union[str, None] = 'c89b0f5432b5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
