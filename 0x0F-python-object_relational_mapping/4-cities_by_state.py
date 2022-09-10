#!/usr/bin/python3
"""[script that lists all cities from the database hbtn_0e_4_usa]
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """[validate the quantity of arguments passed]
    """
    if len(argv) != 4:
        print('Usage: 4-cities_by_state user psw db')
        exit(1)

    host = 'localhost'
    port = 3306
    user = argv[1]
    passwd = argv[2]
    db_name = argv[3]

    db = MySQLdb.connect(
        host=host,
        port=port,
        user=user,
        passwd=passwd,
        db=db_name
    )
    cursor = db.cursor()

    cursor.execute("""
        SELECT
            cities.id, cities.name, states.name
        FROM
            cities, states
        WHERE
            cities.state_id = states.id
        ORDER BY
            cities.id ASC
        """)
    cities = cursor.fetchall()
    for city in cities:
        print(city)
    cursor.close()
    db.close()
