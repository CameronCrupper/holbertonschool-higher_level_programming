#!/usr/bin/python3
"""
print the first Stateobject from the database
hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    """
    takes 3 arguments, uses module SQLAlchemy, imports state
    and Base from model_state - from model_state import Base, State
    connects to locahost at port 3306, displayed state must be first
    in states.id, can't fetch all states from db before displaying
    results, if states table is empty print nothing with newline,
    not executed when imported
    """
    datab = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(datab)
    Session = sessionmaker(bind=engine)
    sesh = Session()
    isinstance = sesh.query(State).order_by(State.id).first()
    if isinstance is None:
        print('Nothing')
    else:
        print('{0}: {1}'.format(isinstance.id, isinstance.name))
