#!/usr/bin/python3
"""[script that lists all cities from the database hbtn_0e_4_usa]
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """[validate the quantity of arguments passed]
    """
    if len(argv) != 5:
        print('Usage: 4-cities_by_state user psw db search_state_name')
        exit(1)

    host = 'localhost'
    port = 3306
    user = argv[1]
    passwd = argv[2]
    db_name = argv[3]
    search = argv[4]

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
            cities.name
        FROM
            cities
        WHERE
            cities.state_id = (
                SELECT
                    id
                FROM
                    states
                WHERE
                    name = %s
            )
        ORDER BY
            cities.id ASC
        """, (search,))

    cities = cursor.fetchall()
    comma = ''

    for city in cities:
        print('{}{}'.format(comma, city[0]), end='')
        comma = ', '
    print()
    cursor.close()
    db.close()
