#!/usr/bin/python3
"""
A script that lists the state objects with name
passed as an argument
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import NoResultFound

if __name__ == "__main__":

    # Assign arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db = sys.argv[3]
    state_search = sys.argv[4]

    # Create the engine
    engine = create_engine('mysql+mysqldb://%s:%s@localhost/%s' %
                           (mysql_username, mysql_password, mysql_db),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session to query the db
    Session = sessionmaker(bind=engine)

    # Instantiate the session
    session = Session()

    # Query to get all results
    results = ""
    rows = session.query(State).all()
    for i in rows:
        if state_search in i.name:
            results = i.id

    if results != "":
        print(results)
    else:
        print("Not Found")

    # Close Session
    session.close()
