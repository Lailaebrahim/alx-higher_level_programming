#!/usr/bin/python3
"""displays all values in the cites from DB"""
import MySQLdb
import sys


def list_cities(username, password, db_name):
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
                   cities INNER JOIN  states ON cities.state_id=states.id
                   ORDER BY cities.id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
