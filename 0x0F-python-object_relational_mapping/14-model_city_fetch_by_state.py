#!/usr/bin/python3
"""[script 14-model_city_fetch_by_state.py that prints all City objects
from the database hbtn_0e_14_usa]
"""

from model_state import Base, State
from sys import argv
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    host = 'localhost'
    user = argv[1]
    psw = argv[2]
    db = argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@{}/{}'.format(user, psw, host, db),
        pool_pre_ping=True
    )

    session = sessionmaker(bind=engine)()

    usa = session.query(City, State) \
        .join(State, State.id == City.state_id) \
        .order_by(City.id.asc()) \
        .all()

    for city in usa:
        print("{}: ({}) {}".format(city.State.name,
                                   city.City.id,
                                   city.City.name))
