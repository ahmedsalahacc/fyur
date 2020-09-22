"""empty message

Revision ID: 950f67f6a31d
Revises: ecfa54cb1ac4
Create Date: 2020-09-20 20:55:41.742830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '950f67f6a31d'
down_revision = 'ecfa54cb1ac4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venues', sa.Column('genres', sa.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venues', 'genres')
    # ### end Alembic commands ###