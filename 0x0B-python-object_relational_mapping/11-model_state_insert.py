#!/usr/bin/python3
"""
adds the State object "Louisiana" to the db
htbn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    """
    takes 3 arguments, uses module SQLAlchemy, imports State and Base
    from model_state - from model_state import Base, State, connects
    to localhost at port 3306, prints new states.id after creation,
    does not execute when imported
    """
    datab = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(datab)
    Session = sessionmaker(bind=engine)
    sesh = Session()
    louisa = State(name="Louisiana")
    sesh.add(louisa)
    sesh.commit()
    print("{0}".format(louisa.id))
    sesh.close()
