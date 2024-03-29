#!/usr/bin/python3
"""displays all values in the states table where name matches the argument"""
import MySQLdb
import sys


def list_states(username, password, db_name, st_search):
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states
                   WHERE name = %s
                   ORDER BY id ASC""", (st_search,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    list_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
