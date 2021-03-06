"""empty message

Revision ID: 79aa6da15aab
Revises: b54b75e1c56c
Create Date: 2020-09-20 15:34:30.232062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79aa6da15aab'
down_revision = 'b54b75e1c56c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artists', 'facebook_link',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('artists', 'genres',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('artists', 'image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
    op.add_column('shows', sa.Column('artist_id', sa.Integer(), nullable=False))
    op.add_column('shows', sa.Column('venue_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'shows', 'artists', ['artist_id'], ['id'])
    op.create_foreign_key(None, 'shows', 'venues', ['venue_id'], ['id'])
    op.drop_column('shows', 'category')
    op.add_column('venues', sa.Column('seeking_talent', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venues', 'seeking_talent')
    op.add_column('shows', sa.Column('category', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'shows', type_='foreignkey')
    op.drop_constraint(None, 'shows', type_='foreignkey')
    op.drop_column('shows', 'venue_id')
    op.drop_column('shows', 'artist_id')
    op.alter_column('artists', 'image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=False)
    op.alter_column('artists', 'genres',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('artists', 'facebook_link',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    # ### end Alembic commands ###
