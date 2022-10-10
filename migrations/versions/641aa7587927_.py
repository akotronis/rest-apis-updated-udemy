"""empty message

Revision ID: 641aa7587927
Revises: 07c57a908e41
Create Date: 2022-10-10 13:08:31.764847

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '641aa7587927'
down_revision = '07c57a908e41'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('description', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('items', 'description')
    # ### end Alembic commands ###