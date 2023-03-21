#!/usr/bin/python3
"""
A script that updates a state objects
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

    # Update the record, first I query
    session.query(State).filter_by(id=2).update({'name': "New Mexico"})
    session.commit()

    # Close Session
    session.close()
