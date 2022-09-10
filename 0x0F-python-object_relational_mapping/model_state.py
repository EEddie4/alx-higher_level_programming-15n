#!/usr/bin/python3
"""[contains the class definition of a State and an instance
Base = declarative_base()]
"""

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """[6. First state model]

    Args:
        Base
    """

    __tablename__ = 'states'
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True,
        unique=True
    )
    name = Column(
        String(128),
        nullable=False
    )
