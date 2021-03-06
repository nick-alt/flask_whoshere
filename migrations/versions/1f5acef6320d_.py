"""empty message

Revision ID: 1f5acef6320d
Revises: 89ddfed69469
Create Date: 2020-04-15 18:13:38.662866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f5acef6320d'
down_revision = '89ddfed69469'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.drop_column('user', 'event_id')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.VARCHAR(length=120), nullable=True))
    op.add_column('user', sa.Column('event_id', sa.INTEGER(), nullable=True))
    op.drop_index(op.f('ix_user_username'), table_name='user')
    # ### end Alembic commands ###
