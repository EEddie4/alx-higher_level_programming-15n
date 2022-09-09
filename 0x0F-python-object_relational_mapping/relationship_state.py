#!/usr/bin/python3
""" module that contains the class definition of a State and an instance
"""

# related third party imports
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ State class:
                inherits from Base Tips
                links to the MySQL table states
                class attribute id that represents a column of
                an auto-generated, unique integer, can’t be null and
                is a primary key class attribute name that represents
                a column of a string with maximum 128 characters
                and can’t be null
    """
    __tablename__ = 'states'

    id = Column(Integer(), primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref='state')
