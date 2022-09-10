#!/usr/bin/python3
"""[7. All states via SQLAlchemy]
"""

from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    """ Base.metadata.create_all(engine) """

    session = sessionmaker(bind=engine)()
    states = session.query(State).order_by(State.id.asc()).all()

    for state in states:
        print('{}: {}'.format(state.id, state.name))
    session.close()
