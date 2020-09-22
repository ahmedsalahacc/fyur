"""empty message

Revision ID: 590c9969421e
Revises: 129dcb5dac70
Create Date: 2020-09-20 13:52:19.620499

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '590c9969421e'
down_revision = '129dcb5dac70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Artists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('city', sa.String(length=120), nullable=False),
    sa.Column('state', sa.String(length=120), nullable=False),
    sa.Column('phone', sa.String(length=120), nullable=False),
    sa.Column('genres', sa.String(length=120), nullable=False),
    sa.Column('image_link', sa.String(length=500), nullable=False),
    sa.Column('facebook_link', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Shows',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('startTime', sa.DateTime(), nullable=False),
    sa.Column('category', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Venues',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('city', sa.String(length=120), nullable=False),
    sa.Column('state', sa.String(length=120), nullable=False),
    sa.Column('address', sa.String(length=120), nullable=False),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('venues')
    op.drop_table('artists')
    op.drop_table('shows')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shows',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('startTime', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='shows_pkey')
    )
    op.create_table('artists',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('city', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('state', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('phone', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('genres', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('image_link', sa.VARCHAR(length=500), autoincrement=False, nullable=False),
    sa.Column('facebook_link', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='artists_pkey')
    )
    op.create_table('venues',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('city', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('state', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('address', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('phone', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('image_link', sa.VARCHAR(length=500), autoincrement=False, nullable=False),
    sa.Column('facebook_link', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='venues_pkey')
    )
    op.drop_table('Venues')
    op.drop_table('Shows')
    op.drop_table('Artists')
    # ### end Alembic commands ###