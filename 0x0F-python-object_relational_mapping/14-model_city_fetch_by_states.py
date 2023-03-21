#!/usr/bin/python3
"""
A script that fetches cities
by states
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
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

    results = session.query(State, City).join(City).order_by(City.id).all()
    # Results contains tuple of two objects, state and city
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()

    # Close Session
    session.close()
