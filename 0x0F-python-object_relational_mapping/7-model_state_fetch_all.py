#!/usr/bin/python3
"""
A script that lists all state objects from
the database
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

# Assign arguments
mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
mysql_db = sys.argv[3]

# Create the engine
engine = create_engine('mysql+mysqldb://%s:%s@localhost:3306/%s' %
                       (mysql_username, mysql_password, mysql_db),
                       pool_pre_ping=True)
Base.metadata.create_all(engine)

# Create a session to query the db
Session = sessionmaker(bind=engine)

# Instantiate the session
session = Session()

# Query to get all results
results = session.query(State).all()
for result in results:
    print("{}: {}".format(result.id, result.name))

# Close Session
session.close()
