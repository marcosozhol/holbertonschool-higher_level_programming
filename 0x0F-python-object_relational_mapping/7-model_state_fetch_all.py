#!/usr/bin/python3
"""
lists all State objects
from the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhst/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session()
    states = session.query(State).order_by(State.id)

    for state in states:
        print("{}: {}".format(state.id, state.name))
