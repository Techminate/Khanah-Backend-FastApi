"""Removed slug to items model

Revision ID: d83318068f5f
Revises: 5a969df6395a
Create Date: 2022-03-09 00:24:58.229036

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd83318068f5f'
down_revision = '5a969df6395a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('items', 'slug')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('slug', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
    # ### end Alembic commands ###