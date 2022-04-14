#!/usr/bin/python3
"""
lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':
    """
    Results must be sorted in ascending order by states.id
    Results must be displayed as they are in the example below
    """
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    cur.fetchall()
    for state in state:
        if state[1][0] == "N":
            print(state)

    cur.close()
    db.close()
