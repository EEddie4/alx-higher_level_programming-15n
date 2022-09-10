#!/usr/bin/python3
"""[file similar to model_state.py named model_city.py that
contains the class definition of a City.]
"""

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from model_state import State
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """[City model]

    Args:
        Base
    """

    __tablename__ = 'cities'
    id = Column(
        Integer,
        primary_key=True
    )
    name = Column(
        String(128),
        nullable=False
    )
    state_id = Column(
        Integer,
        ForeignKey(State.id)
    )
