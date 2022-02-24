#!/usr/bin/python3
"""
list all State objects from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    takes 3 arguments, uses module SQLAlchemy, import
    State and Base from model_state - from model_state import
    Base, State, connect to localhost at port 3306,
    results sorted in ascending order by state.id,
    not executed when imported
    """
    datab = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(datab)
    Session = sessionmaker(bind=engine)
    sesh = Session()
    for instance in sesh.query(State).order_by(State.id):
        print('{0}: {1}'.format(instance.id, instance.name))
