#!/usr/bin/python3
"""
This script defines a relationship between Class `City`
and  `State` Class to work with MySQLAlchemy ORM
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """State class

    Attributes:
              __tablename__ (str): name of table for the State class
              id (int):  state id of the class
              name (str): state name of the class
              cities (relation): links each `City` to a particular `State`
    """

    __tablename__ = 'states'
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="State")
