"""create game table

Revision ID: 2d78598a3724
Revises: None
Create Date: 2014-08-02 16:43:50.349999

"""

# revision identifiers, used by Alembic.
revision = '2d78598a3724'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('theme', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('start', sa.DateTime(), nullable=False),
    sa.Column('end', sa.DateTime(), nullable=True),
    sa.Column('location_one', sa.String(), nullable=True),
    sa.Column('location_two', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game')
    ### end Alembic commands ###
