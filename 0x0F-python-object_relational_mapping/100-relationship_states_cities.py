#!/usr/bin/python3
""" This script creates the State "California" with
the City "San Francisco" from a DB
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    create_session = sessionmaker(bind=engine)
    Session = create_session()
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    Session.add(new_state)
    Session.commit()

    new_state.cities.append(new_city)
    Session.add(new_city)
    Session.commit()
