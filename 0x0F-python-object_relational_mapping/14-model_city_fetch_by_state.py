#!/usr/bin/python3
""" This script displays all `cities` from database
`hbtn_0e_14_usa` passed as argument
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ Connect to database using
    SQLAlchemy
    """

    connect_db = "mysql+mysqldb://{}:{}@localhost/{}".format(
            argv[1], argv[2], argv[3])

    engine = create_engine(connect_db)
    create_session = sessionmaker(bind=engine)
    Session = create_session()

    query = Session.query(State, City).filter(State.id == City.state_id).all()
    for state, city in query:
        print("{0}: ({1}) {2}".format(state.name, city.id, city.name))
    Session.close()
