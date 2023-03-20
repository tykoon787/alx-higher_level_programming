#!/usr/bin/python3
"""
A script that selects cities by states
"""

import sys
import MySQLdb

if __name__ == "__main__":
    user_name = sys.argv[1]
    user_pass = sys.argv[2]
    db_name = sys.argv[3]
    state_input = sys.argv[4]
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=user_name,
                         password=user_pass,
                         db=db_name)

    cursor = db.cursor()

    cursor.execute(
        "SELECT cities.name FROM cities\
                JOIN states ON cities.state_id = states.id\
                    WHERE states.name = %s", (state_input,)
    )
    results = cursor.fetchall()

    city_list = []
    for row in results:
        city_list.append(row[0])
    print(", ".join(city_list))
    cursor.close()
    db.close()
