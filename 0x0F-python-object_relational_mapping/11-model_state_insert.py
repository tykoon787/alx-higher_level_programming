#!/usr/bin/python3
"""
A script that inserts a state objects
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

    # To add data, create an instance of the state object
    lousiana = State(name="Louisiana")

    # Add the data
    session.add(lousiana)

    # Commit the changes
    session.commit()

    # Print the id of the newly created state
    print(lousiana.id)

    # Close Session
    session.close()
