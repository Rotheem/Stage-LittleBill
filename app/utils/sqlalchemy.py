import datetime
from typing import Annotated
import uuid

from sqlalchemy import types
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, mapped_column

# Pre-configured field type for UUID primary key (see https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#mapping-whole-column-declarations-to-python-types)
PrimaryKey = Annotated[uuid.UUID, mapped_column(primary_key=True)]


class Base(MappedAsDataclass, DeclarativeBase):
    """Base class for all models.

    The type map is overriden to use our custom datetime type (see https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#customizing-the-type-map)"""

    type_annotation_map = {
        bool: types.Boolean(),
        datetime.date: types.Date(),
        datetime.datetime: types.DateTime(),
        str: types.String(),
        uuid.UUID: types.Uuid(),
    }
