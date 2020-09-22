"""empty message

Revision ID: ecfa54cb1ac4
Revises: 79aa6da15aab
Create Date: 2020-09-20 16:36:47.977383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecfa54cb1ac4'
down_revision = '79aa6da15aab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('seeking_description', sa.String(), nullable=True))
    op.add_column('artists', sa.Column('seeking_venue', sa.Boolean(), nullable=False))
    op.add_column('venues', sa.Column('seeking_desc', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venues', 'seeking_desc')
    op.drop_column('artists', 'seeking_venue')
    op.drop_column('artists', 'seeking_description')
    # ### end Alembic commands ###
