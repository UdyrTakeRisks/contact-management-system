"""Update Migration

Revision ID: 15a0cfb2bbb9
Revises: beeb29dfa8aa
Create Date: 2024-11-04 23:19:56.394019

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '15a0cfb2bbb9'
down_revision: Union[str, None] = 'beeb29dfa8aa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
