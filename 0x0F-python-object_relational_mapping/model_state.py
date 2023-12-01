#!/usr/bin/python3
"""
This script defines a `Base` Class and a `State` Class to
work with MySQLAlchemy ORM
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class

    Attributes:
              __tablename__ (str): name of table for the State class
              id (int):  state id of the class
              name (str): state name of the class
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
