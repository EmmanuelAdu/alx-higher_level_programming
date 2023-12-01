#!/usr/bin/python3
"""
This script uses SQLAlchemy module to add a new `states` object
passed as argument to the database
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
    new_state = State(name="Louisiana")
    Session.add(new_state)
    Session.commit()

    print("{0}".format(new_state.id))
    Session.close()
