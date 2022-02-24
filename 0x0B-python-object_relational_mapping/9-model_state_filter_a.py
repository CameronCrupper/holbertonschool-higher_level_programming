#!/usr/bin/python3
"""
list all State objects that contain the letter a
from database htbn_0e_0_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    """
    takes 3 arguments, uses module SQLAlchemy, importState
    and Base from model_state - from model_state import Base, State
    , connects to localhost at port 3306, sorted in ascending 
    order by states.id, not executed when imported
    """
    datab = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(datab)
    Session = sessionmaker(bind=engine)
    sesh = Session()
    for isinstance in sesh.query(State).filter(State.name.contains("a")):
        print("{0}: {1}".format(isinstance.id, isinstance.name))
