#!/usr/bin/python3
"""
A script that selects all states from the states
Table that matches user input
"""

import sys
import MySQLdb

if __name__ == "__main__":
    user_name = sys.argv[1]
    user_pass = sys.argv[2]
    db_name = sys.argv[3]
    user_input = sys.argv[4]
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=user_name,
                         password=user_pass,
                         db=db_name)

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE BINARY name = '%s'\
            ORDER BY states.id ASC" % (user_input,))
    results = cursor.fetchall()
    for row in results:
        print("%s" % (row,))

    cursor.close()
    db.close()
