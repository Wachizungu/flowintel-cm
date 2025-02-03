"""empty message

Revision ID: 8f00b18976f9
Revises: 6a9a28d9fb7a
Create Date: 2025-01-29 11:18:06.561242

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.exc import OperationalError


# revision identifiers, used by Alembic.
revision = '8f00b18976f9'
down_revision = '6a9a28d9fb7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    try:
        with op.batch_alter_table('case', schema=None) as batch_op:
            batch_op.drop_column('taxonomies')
    except OperationalError:
        print("Column 'taxonomies' already dropped from 'Case'")

    try:
        with op.batch_alter_table('case', schema=None) as batch_op:
            batch_op.add_column(sa.Column('is_private', sa.Boolean(), nullable=True))
    except OperationalError:
        print("Column 'is_private' already exist in 'Case'")

    try:
        with op.batch_alter_table('case__template', schema=None) as batch_op:
            batch_op.drop_column('taxonomies')
    except OperationalError:
        print("Column 'taxonomies' already dropped from 'Case_Template'")

    try:
        with op.batch_alter_table('task', schema=None) as batch_op:
            batch_op.drop_column('taxonomies')
    except OperationalError:
        print("Column 'taxonomies' already dropped from 'task'")

    try:
        with op.batch_alter_table('task__template', schema=None) as batch_op:
            batch_op.drop_column('taxonomies')
    except OperationalError:
        print("Column 'taxonomies' already dropped from 'task_template'")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    try:
        with op.batch_alter_table('case', schema=None) as batch_op:
            batch_op.drop_column('is_private')
    except OperationalError:
        print("Column 'is_private' already dropped from 'Case'")

    # ### end Alembic commands ###
