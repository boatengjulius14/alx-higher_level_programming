#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State
import sys


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    local_session = Session()

    _state = local_session.query(State).order_by(State.id).first()

    if _state:
        print("{}: {}".format(_state.id, _state.name))
    else:
        print("Nothing")

    local_session.close()
