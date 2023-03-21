#!/usr/bin/python3
"""
A script that deletes state objects with 'a'
in thier name
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # Assign arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db = sys.argv[3]

    # Create the engine
    engine = create_engine('mysql+mysqldb://%s:%s@localhost/%s' %
                           (mysql_username, mysql_password, mysql_db),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session to query the db
    Session = sessionmaker(bind=engine)

    # Instantiate the session
    session = Session()

    # Delete Record
    results = session.query(State).filter(
        State.name.ilike("%a%")).delete()
    session.commit()
    print(results)

    # Close Session
    session.close()
