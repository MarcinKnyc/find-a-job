"""experience requirements can be null

Revision ID: f55ccad78a4a
Revises: 79e374599075
Create Date: 2023-11-04 17:53:06.607705

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f55ccad78a4a'
down_revision: Union[str, None] = '79e374599075'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('offers', 'experience_requirements',
               existing_type=sa.TEXT(),
               nullable=True,
               schema='offers')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('offers', 'experience_requirements',
               existing_type=sa.TEXT(),
               nullable=False,
               schema='offers')
    # ### end Alembic commands ###
