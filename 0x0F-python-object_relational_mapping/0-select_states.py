#!/usr/bin/python3
"""
List All States in the `hbtn_0e_0_usa` database
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Using MySQLdb to connect to database
    """
    dbConnect = MySQLdb.connect(
            host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    dbCursor = dbConnect.cursor()
    dbCursor.execute("SELECT * FROM states")

    rows = dbCursor.fetchall()
    for r in rows:
        print(r)
