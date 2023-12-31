"""exported_to_qdrant column

Revision ID: e06f56c3c8dd
Revises: f55ccad78a4a
Create Date: 2023-11-04 18:10:27.252697

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e06f56c3c8dd'
down_revision: Union[str, None] = 'f55ccad78a4a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('offers', sa.Column('exported_to_qdrant', sa.DateTime(), nullable=True), schema='offers')
    # todo: execute
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('offers', 'exported_to_qdrant', schema='offers')
    # ### end Alembic commands ###
