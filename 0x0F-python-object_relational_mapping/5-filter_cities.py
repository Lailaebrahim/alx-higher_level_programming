#!/usr/bin/python3
"""displays all cities here state matches the argument"""
import MySQLdb
import sys


def list_states(username, password, db_name, st_search):
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities
                   INNER JOIN states ON cities.state_id=states.id
                   WHERE states.name=%s""", (st_search,))
    rows = cur.fetchall()
    temp = []
    for row in rows:
        for value in row:
            temp.append(value)
    print(*temp, sep=", ")
    cur.close()
    db.close()


if __name__ == "__main__":
    list_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
