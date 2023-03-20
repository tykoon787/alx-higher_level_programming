#!/usr/bin/python3
"""
A script that selects all states from the states
Table that start with N
"""

import sys
import MySQLdb

if __name__ == "__main__":
    user_name = sys.argv[1]
    user_pass = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=user_name,
                         password=user_pass,
                         db=db_name)

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states where name LIKE BINARY 'N%'\
            ORDER BY states.id ASC")
    results = cursor.fetchall()
    for row in results:
        print("%s" % (row,))

    cursor.close()
    db.close()
