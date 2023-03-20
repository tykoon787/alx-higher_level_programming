#!/usr/bin/python3
"""
This module contains a state class

Classes:
    States
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

if __name__ == "__main__":

    # Assign Script Arguments
    user_name = sys.argv[1]
    user_pass = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine
    engine = create_engine('mysql+mysqldb://%s:%s@localhost/%s' %
                           (user_name, user_pass, db_name), pool_pre_ping=True)

    # Base
    Base = declarative_base()

    # Class Definition for State

    class State(Base):
        """
        Definition for the states table
        Attributes:
            id (int): The PK of the states
            name (string): Name of the states
        """
        __tablename__ = 'states'

        id = Column(Integer, primary_key=True, autoincrement=True,
                    unique=True, nullable=False)
        name = Column(String(128), nullable=False)

    # Create the schema
    Base.metadata.create_all(engine)
