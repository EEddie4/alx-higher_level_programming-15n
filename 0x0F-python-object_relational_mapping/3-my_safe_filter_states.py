#!/usr/bin/python3
"""[script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. safe from MySQL injections!]
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """[validate the quantity of arguments passed]
    """
    if len(argv) != 5:
        print('Usage: 0-select_states user psw db state_name_searched')
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
    cur = db.cursor()

    cur.execute("""
        SELECT
            *
        FROM
            states
        WHERE
            name
        LIKE
            %s
        ORDER BY
            id ASC
        """, (search,))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
