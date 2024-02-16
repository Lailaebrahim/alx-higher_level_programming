#!/usr/bin/python3
import MySQLdb
import sys


def list_states(username, password, db_name):
    db = MySQLdb.connect(host=username, port=3306, user="root", passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])