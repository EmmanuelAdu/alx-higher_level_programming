#!/usr/bin/python3
"""
List All `states` with `name` starting with letter `N`
in the `hbtn_0e_0_usa` database
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Using MySQLdb to connect to database
    """
    dbConnect = MySQLdb.connect(
            host="localhost", user=argv[1], port=3306,
            passwd=argv[2], db=argv[3])

    dbCursor = dbConnect.cursor()
    dbCursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
            ORDER BY states.id ASC")

    rows = dbCursor.fetchall()
    for r in rows:
        print(r)
