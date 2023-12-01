#!/usr/bin/python3
"""
This script uses SQLAlchemy module to print the all `states`
that contains `a' in the name of the `states`
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Access the db and list all the states present
    """
    connect_db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])

    engine = create_engine(connect_db)
    create_session = sessionmaker(bind=engine)

    Session = create_session()
    allStates = Session.query(State).filter(State.name.contains('a'))
    if allStates is not None:
        for state in allStates:
            print("{0}: {1}".format(state.id, state.name))
