#!/usr/bin/python3
import MySQLdb
import sys

def list_states(username, password, db_name):
    db = MySQLdb.connect(host=username, port=3306, usr="root", passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print( row )
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len( sys.argv ) == 4:
        list_states( sys.argv[1], sys.argv[2], sys.argv[3] )
    else:
        print( "Usage: {} <username> <password> <database_name>".format( sys.argv[0] ) )
