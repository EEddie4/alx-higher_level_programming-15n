#!/usr/bin/python3
"""[script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa]
"""

from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    host = 'localhost'
    user = argv[1]
    psw = argv[2]
    db = argv[3]
    search = argv[4]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@{}/{}'.format(user, psw, host, db),
        pool_pre_ping=True
    )
    session = sessionmaker(bind=engine)()

    states = session.query(State).filter(
        State.name == search).order_by(State.id.asc()).all()

    if not states:
        print('Not found')
        exit(1)

    for state in states:
        print('{}'.format(state.id))
