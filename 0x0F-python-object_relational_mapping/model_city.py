#!/usr/bin/python3
"""
This script defines `class City` module inherited from `Base`
in SQLAlchemy and links to `cities` in the database
"""

from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represents `cities` in a database

    Attributes:
             __tablename__ (str): name of table
             id (int): id of city
             name (str): the city's name
             state_id (int): the state id of city
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
