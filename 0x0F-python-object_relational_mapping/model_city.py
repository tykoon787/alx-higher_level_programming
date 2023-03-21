#!/usr/bin/python3
"""
This module contains the model for the
city class

Classes:
    City
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    Class to represent the cities table
    Attributes:
        id (int): Id of the state
        name (string): Name of the city
        state_id (int): Foreign Key
    """
    __tablename__ = 'cities'

    id = Column(Integer,
                primary_key=True,
                unique=True,
                autoincrement=True,
                nullable=False)

    name = Column(String(128),
                  nullable=False)

    state_id = Column(Integer,
                      ForeignKey("states.id", ondelete='CASCADE'),
                      nullable=False)
