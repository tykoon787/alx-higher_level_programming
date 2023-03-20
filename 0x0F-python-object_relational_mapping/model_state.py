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
