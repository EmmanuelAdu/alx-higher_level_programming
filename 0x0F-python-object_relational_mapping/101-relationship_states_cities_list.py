#!/usr/bin/python3
""" This script prints out all `states` and their corresponding
`cities` from the database
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Connect to the database
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    create_session = sessionmaker(bind=engine)
    Session = create_session()

    for St in Session.query(State).order_by(State.id):
        print(St.id, St.name, sep=": ")
        for Ct in St.cities:
            print("    ", end="")
            print(Ct.id, Ct.name, sep=": ")
