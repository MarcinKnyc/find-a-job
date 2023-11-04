"""Links offers

Revision ID: 74fc460b66f3
Revises: 
Create Date: 2023-11-04 14:03:30.465590

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74fc460b66f3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("create schema links")
    op.execute("create schema offers")
    op.create_table('links',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('link', sa.Text(), nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('link'),
    schema='links'
    )
    op.create_table('offers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(), nullable=False),
    sa.Column('hiring_organization', sa.Text(), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('valid_through', sa.DateTime(), nullable=False),
    sa.Column('address_country', sa.Text(), nullable=False),
    sa.Column('address_region', sa.Text(), nullable=False),
    sa.Column('address_locality', sa.Text(), nullable=False),
    sa.Column('postal_code', sa.Text(), nullable=True),
    sa.Column('street_address', sa.Text(), nullable=True),
    sa.Column('employment_type', sa.Text(), nullable=False),
    sa.Column('industry', sa.Text(), nullable=False),
    sa.Column('base_salary', sa.Float(), nullable=True),
    sa.Column('job_benefits', sa.Text(), nullable=True),
    sa.Column('responsibilities', sa.Text(), nullable=False),
    sa.Column('experience_requirements', sa.Text(), nullable=False),
    sa.Column('link_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['link_id'], ['links.links.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='offers'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('offers', schema='offers')
    op.drop_table('links', schema='links')
    op.execute("drop schema links")
    op.execute("drop schema offers")
    # ### end Alembic commands ###
