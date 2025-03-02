"""New table-naming style

Revision ID: 90c0c215fb6f
Revises: 67a914e208f0
Create Date: 2025-03-02 12:42:48.639126

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '90c0c215fb6f'
down_revision: Union[str, None] = '67a914e208f0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
