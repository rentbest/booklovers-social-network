"""New table-naming style

Revision ID: c2f95fb71ee4
Revises: 90c0c215fb6f
Create Date: 2025-03-02 12:43:42.446897

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c2f95fb71ee4'
down_revision: Union[str, None] = '90c0c215fb6f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
