#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states
where `name` matches the argument from the database `hbtn_0e_0_usa`
and is safe from MySQL Injections.
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
    dbCursor.execute("SELECT * FROM states WHERE name LIKE BINARY %(name)s \
            ORDER BY states.id ASC", {'name': argv[4]})

    rows = dbCursor.fetchall()
    for r in rows:
        print(r)
