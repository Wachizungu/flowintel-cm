"""empty message

Revision ID: 8626dbc8e984
Revises: b34064d1a92c
Create Date: 2024-09-20 10:19:06.412106

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.exc import OperationalError


# revision identifiers, used by Alembic.
revision = '8626dbc8e984'
down_revision = 'b34064d1a92c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    try:
        with op.batch_alter_table('case', schema=None) as batch_op:
            batch_op.drop_index('ix_case_title')
    except OperationalError:
        print("Index already dropped")

    try:
        with op.batch_alter_table('case__misp__object', schema=None) as batch_op:
            batch_op.alter_column('case_id',
                existing_type=sa.INTEGER(),
                nullable=True)
    except OperationalError:
        pass

    try:
        with op.batch_alter_table('misp__attribute__instance__uuid', schema=None) as batch_op:
            batch_op.create_index(batch_op.f('ix_misp__attribute__instance__uuid_attribute_instance_uuid'), ['attribute_instance_uuid'], unique=False)
            batch_op.create_index(batch_op.f('ix_misp__attribute__instance__uuid_instance_id'), ['instance_id'], unique=False)
            batch_op.create_index(batch_op.f('ix_misp__attribute__instance__uuid_misp_attribute_id'), ['misp_attribute_id'], unique=False)
    except OperationalError:
        print("Index already exist")

    try:
        with op.batch_alter_table('task', schema=None) as batch_op:
            batch_op.drop_index('ix_task_title')
    except OperationalError:
        print("Index already dropped")

    try:
        with op.batch_alter_table('task', schema=None) as batch_op:
            batch_op.alter_column('title', existing_type=sa.String(length=64),
                    type_=sa.String())
            batch_op.alter_column('url', existing_type=sa.String(length=64),
                    type_=sa.String())
    except OperationalError:
        print("Task Title already changed")
    
    try:
        with op.batch_alter_table('case', schema=None) as batch_op:
            batch_op.alter_column('title', existing_type=sa.String(length=64),
                    type_=sa.String())
    except OperationalError:
        print("Case Title already changed")

    try:
        with op.batch_alter_table('case__template', schema=None) as batch_op:
            batch_op.alter_column('title', existing_type=sa.String(length=64),
                    type_=sa.String())
    except OperationalError:
        print("Case template Title already changed")

    try:
        with op.batch_alter_table('task__template', schema=None) as batch_op:
            batch_op.alter_column('title', existing_type=sa.String(length=64),
                    type_=sa.String())
            batch_op.alter_column('url', existing_type=sa.String(length=64),
                    type_=sa.String())
    except OperationalError:
        print("Task template Title already changed")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.create_index('ix_task_title', ['title'], unique=False)

    with op.batch_alter_table('misp__attribute__instance__uuid', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_misp__attribute__instance__uuid_misp_attribute_id'))
        batch_op.drop_index(batch_op.f('ix_misp__attribute__instance__uuid_instance_id'))
        batch_op.drop_index(batch_op.f('ix_misp__attribute__instance__uuid_attribute_instance_uuid'))

    with op.batch_alter_table('case__misp__object', schema=None) as batch_op:
        batch_op.alter_column('case_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('case', schema=None) as batch_op:
        batch_op.create_index('ix_case_title', ['title'], unique=False)

    # ### end Alembic commands ###
