#!/usr/bin/python3
"""[a script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.]
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
            name = '{}'
        ORDER BY
            id ASC
        """.format(search))
    states = cur.fetchall()

    for state in states:
        if state[1] == search:
            print(state)
    cur.close()
    db.close()
