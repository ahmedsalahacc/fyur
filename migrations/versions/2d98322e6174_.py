"""empty message

Revision ID: 2d98322e6174
Revises: 950f67f6a31d
Create Date: 2020-09-20 23:07:59.915692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d98322e6174'
down_revision = '950f67f6a31d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venues', sa.Column('website', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venues', 'website')
    # ### end Alembic commands ###
