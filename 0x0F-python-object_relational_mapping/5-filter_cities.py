#!/usr/bin/python3
"""
This script lists all `cities` from the database `hbtn_0e_4_usa`.
by the argument from the `state`
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Using MySQLdb to connect to database
    """
    db_connect = MySQLdb.connect(
            host="localhost", user=argv[1], port=3306,
            passwd=argv[2], db=argv[3])

    ''' Using the `with` keyword to automatically perform the operation '''
    with db_connect.cursor() as db_cursor:
        db_cursor.execute("""
                     SELECT
                        cities.id, cities.name
                     FROM
                        cities
                     JOIN
                        states
                     ON
                        cities.state_id = states.id
                     WHERE
                        states.name LIKE BINARY %(state_name)s
                     ORDER BY
                        cities.id ASC
                        """, {'state_name': argv[4]})
        row_selected = db_cursor.fetchall()

        if row_selected is not None:
            print(", ".join([row[1] for row in row_selected]))
