#!/usr/bin/python3
"""
lists all State objects that
contain the letter a from the
database hbtn_0e_6_usa:
take 3 arguments: mysql username,
mysql password and database name
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
     take 3 arguments: mysql username,
     mysql password and database name
    """

    engine = create_engine("mysql+mysqldb://{}:{}@localhst/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session()

    for state in session.query(State).order_by(State.id):
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))
