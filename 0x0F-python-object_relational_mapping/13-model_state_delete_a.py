#!/usr/bin/python3
"""
This script uses SQLAlchemy module to delete all name of
`states` object that contains letter 'a'
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
    del_state = Session.query(State).filter(State.name.contains('a'))

    if del_state is not None:
        for state in del_state:
            Session.delete(state)

    Session.commit()
    Session.close()
