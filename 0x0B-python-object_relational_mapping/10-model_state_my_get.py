#!/usr/bin/python3
"""
prints the State object with the name passed as
an argument from the database htbn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    """
    takes 4 arguments, uses SQLAlchemy, import State and Base
    from model_state - from model_state import Base, State,
    connects to localhost at port 3306, assume you have one
    record with the state name to search, displays the states.id
    , does not execute when imported, if not state has the name
    you searched for display Not Found
    """

    datab = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(datab)
    Session = sessionmaker(bind=engine)
    sesh = Session()
    isinstance = sesh.query(State).filter(State.name == argv[4]).first()
    if isinstance is None:
        print("Not found")
    else:
        print("{0}".format(isinstance.id))
