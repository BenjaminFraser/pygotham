"""empty message

Revision ID: c16bcdd1f01e
Revises: 90f1af83d9b6
Create Date: 2016-09-28 00:22:29.708204

"""

# revision identifiers, used by Alembic.
revision = 'c16bcdd1f01e'
down_revision = '90f1af83d9b6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sponsors', sa.Column('twitter_handle', sa.String(length=15), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sponsors', 'twitter_handle')
    ### end Alembic commands ###
