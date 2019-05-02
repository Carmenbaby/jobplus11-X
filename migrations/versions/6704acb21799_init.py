"""init

Revision ID: 6704acb21799
Revises: 
Create Date: 2019-05-01 22:31:33.188718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6704acb21799'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('real_name', sa.String(length=20), nullable=True),
    sa.Column('phone', sa.String(length=11), nullable=True),
    sa.Column('work_years', sa.SmallInteger(), nullable=True),
    sa.Column('role', sa.SmallInteger(), nullable=True),
    sa.Column('resume', sa.String(length=128), nullable=True),
    sa.Column('resume_url', sa.String(length=64), nullable=True),
    sa.Column('is_disable', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_name'), 'user', ['name'], unique=True)
    op.create_table('company_detail',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('logo', sa.String(length=256), nullable=False),
    sa.Column('site', sa.String(length=128), nullable=False),
    sa.Column('location', sa.String(length=24), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('about', sa.String(length=1024), nullable=True),
    sa.Column('tags', sa.String(length=128), nullable=True),
    sa.Column('stack', sa.String(length=128), nullable=True),
    sa.Column('team_introduction', sa.String(length=256), nullable=True),
    sa.Column('welfares', sa.String(length=256), nullable=True),
    sa.Column('field', sa.String(length=128), nullable=True),
    sa.Column('finance_stage', sa.String(length=128), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('job',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=24), nullable=True),
    sa.Column('salary_low', sa.Integer(), nullable=False),
    sa.Column('salary_high', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=24), nullable=True),
    sa.Column('description', sa.String(length=1500), nullable=True),
    sa.Column('tags', sa.String(length=128), nullable=True),
    sa.Column('experience_requirement', sa.String(length=32), nullable=True),
    sa.Column('degree_requirement', sa.String(length=32), nullable=True),
    sa.Column('is_fulltime', sa.Boolean(), nullable=True),
    sa.Column('is_open', sa.Boolean(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('views_count', sa.Integer(), nullable=True),
    sa.Column('is_disable', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('resume',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('delivery',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.SmallInteger(), nullable=True),
    sa.Column('response', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['job.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('edu_experience',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('begin_at', sa.DateTime(), nullable=True),
    sa.Column('end_at', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.Column('school', sa.String(length=32), nullable=False),
    sa.Column('specialty', sa.String(length=32), nullable=False),
    sa.Column('degree', sa.String(length=16), nullable=True),
    sa.Column('resume_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['resume_id'], ['resume.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('job_experience',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('begin_at', sa.DateTime(), nullable=True),
    sa.Column('end_at', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.Column('company', sa.String(length=32), nullable=False),
    sa.Column('city', sa.String(length=32), nullable=False),
    sa.Column('resume_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['resume_id'], ['resume.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('preject_experience',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('begin_at', sa.DateTime(), nullable=True),
    sa.Column('end_at', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('role', sa.String(length=32), nullable=True),
    sa.Column('technologys', sa.String(length=64), nullable=True),
    sa.Column('resume_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['resume_id'], ['resume.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_job',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['job.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_job')
    op.drop_table('preject_experience')
    op.drop_table('job_experience')
    op.drop_table('edu_experience')
    op.drop_table('delivery')
    op.drop_table('resume')
    op.drop_table('job')
    op.drop_table('company_detail')
    op.drop_index(op.f('ix_user_name'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
