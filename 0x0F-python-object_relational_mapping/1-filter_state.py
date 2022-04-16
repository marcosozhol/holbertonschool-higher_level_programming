#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""


if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    cur.fetchall()
    for state in state:
        if state[1][0] == "N":
            print(state)
