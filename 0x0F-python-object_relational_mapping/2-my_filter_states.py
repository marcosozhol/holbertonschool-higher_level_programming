#!/usr/bin/python3
"""
Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """4 arguments: mysql username, mysql password, database name
    and state name searched
    """
    server = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                                  passwd=sys.argv[2], database=sys.argv[3])

    curs = server.cursor()

    curs.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
                 .format(sys.argv[4]))

    column = curs.fetchall()

    for row in column:
        if row[1] == sys.argv[4]:
            print(row)

    curs.close()
    server.close()
