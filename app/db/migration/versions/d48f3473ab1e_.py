"""empty message

Revision ID: d48f3473ab1e
Revises: 
Create Date: 2023-03-02 18:43:58.148788

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd48f3473ab1e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roulette',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('title', sa.TEXT(), nullable=False),
    sa.Column('start', sa.DateTime(timezone=True), nullable=False),
    sa.Column('end', sa.DateTime(timezone=True), nullable=False),
    sa.Column('score', sa.INTEGER(), nullable=False),
    sa.Column('winners_count', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__roulette')),
    sa.UniqueConstraint('id', name=op.f('uq__roulette__id'))
    )
    op.create_table('users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('nickname', sa.VARCHAR(length=30), nullable=False),
    sa.Column('name', sa.VARCHAR(length=15), nullable=False),
    sa.Column('user_type', sa.VARCHAR(length=15), nullable=False),
    sa.Column('surname', sa.VARCHAR(length=20), nullable=False),
    sa.Column('phone', sa.CHAR(length=12), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__users')),
    sa.UniqueConstraint('id', name=op.f('uq__users__id'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('roulette')
    # ### end Alembic commands ###
