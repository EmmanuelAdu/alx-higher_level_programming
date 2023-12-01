#!/usr/bin/python3
"""
This script uses SQLAlchemy module to list all the `states`
in the database `hbtn_0e_6_usa` order by `state id`
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
    for instance in Session.query(State).order_by(State.id):
        print("{0}: {1}".format(instance.id, instance.name))
