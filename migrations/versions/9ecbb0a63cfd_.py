"""empty message

Revision ID: 9ecbb0a63cfd
Revises: 555f0e2a9f6e
Create Date: 2017-02-15 23:09:03.309197

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ecbb0a63cfd'
down_revision = '555f0e2a9f6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('messages_user_id_fkey', 'messages', type_='foreignkey')
    op.create_foreign_key(None, 'messages', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.add_column('users', sa.Column('password', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    op.drop_constraint(None, 'messages', type_='foreignkey')
    op.create_foreign_key('messages_user_id_fkey', 'messages', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###