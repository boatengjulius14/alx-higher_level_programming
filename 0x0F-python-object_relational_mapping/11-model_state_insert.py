#!/usr/bin/python3
"""
Adds the State object “Louisiana” to the database hbtn_0e_6_usa
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

    ins_state = State(name="Louisiana")
    local_session.add(ins_state)
    local_session.commit()
    print(ins_state.id)
