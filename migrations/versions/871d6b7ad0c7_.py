"""empty message

Revision ID: 871d6b7ad0c7
Revises: 5cd03995339b
Create Date: 2024-04-24 16:09:26.037707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '871d6b7ad0c7'
down_revision = '5cd03995339b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('note__template',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=36), nullable=True),
    sa.Column('note', sa.String(), nullable=True),
    sa.Column('template_id', sa.Integer(), nullable=True),
    sa.Column('template_order_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['template_id'], ['task__template.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('note__template', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_note__template_template_order_id'), ['template_order_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_note__template_uuid'), ['uuid'], unique=False)

    with op.batch_alter_table('task__template', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nb_notes', sa.Integer(), nullable=True))
        batch_op.create_index(batch_op.f('ix_task__template_nb_notes'), ['nb_notes'], unique=False)
        batch_op.drop_column('notes')

    connection = op.get_bind()
    connection.execute(sa.text(f"UPDATE task__template SET nb_notes = 0"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task__template', schema=None) as batch_op:
        batch_op.add_column(sa.Column('notes', sa.VARCHAR(), nullable=True))
        batch_op.drop_index(batch_op.f('ix_task__template_nb_notes'))
        batch_op.drop_column('nb_notes')

    with op.batch_alter_table('note__template', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_note__template_uuid'))
        batch_op.drop_index(batch_op.f('ix_note__template_template_order_id'))

    op.drop_table('note__template')
    # ### end Alembic commands ###
