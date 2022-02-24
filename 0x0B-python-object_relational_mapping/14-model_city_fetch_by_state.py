#!/usr/bin/python3
"""
prints all City objects from db htbn_0e_14_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv
from model_city import City

if __name__ == "__main__":
    """
    takes 3 arguments, uses module SQLAlchemy, imports State and Base
    from model_state - from model_state import Base, State, connects
    to localhost at port 3306, results sorted in ascending order by
    cities.id, does not execute when imported, results look like
    <state name>: (<city id>) <city name>
    """
    datab = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(datab)
    Session = sessionmaker(bind=engine)
    sesh = Session()
    query = sesh.query(City, State).join(State)
    for _c, _s in query.all():
        print("{}: ({:d}) {}".format(_s.name, _c.id, _c.name))
    sesh.commit()
    sesh.close()
