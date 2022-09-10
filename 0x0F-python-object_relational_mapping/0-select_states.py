#!/usr/bin/python3
"""[a script that lists all states from the database hbtn_0e_0_usa]
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """[validate the quantity of arguments passed]
    """
    if len(argv) != 4:
        print('Usage: 0-select_states username password database')
        exit(-1)

    db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3], port=3306)
    cur = db.cursor()

    cur.execute('SELECT * FROM states ORDER BY id ASC')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()
