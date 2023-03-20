#!/usr/bin/python3
import sys
import MySQLdb
"""
A script that selects all states from the states
Table
"""
user_name = sys.argv[1]
user_pass = sys.argv[2]
db_name = sys.argv[3]
db = MySQLdb.connect(host="localhost:3306", user=user_name,
                     password=user_pass, db=db_name)

cursor = db.cursor()

cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
results = cursor.fetchall()
for id, name in results:
    print("(%s, '%s')" % (id, name))
db.close()
