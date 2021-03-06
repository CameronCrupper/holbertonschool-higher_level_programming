#!/usr/bin/python3
"""
contains the class definition of a state and an
instance Base = declarative_base():
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    """
    State class:
    inherits from Base Tips
    links to the MySQL table states
    class attribute id that represents a column of
    an auto-generated, unique integer, cant be null
    and is a primary key class attribute name that represents
    a column of a string with maximum 128 characters and cant be null
    You must use the module SQLAlchemy
    Your script should connect to a MySQL server running on
    localhost at port 3306
    WARNING: all classes who inherit from Base must be
    imported before calling Base.metadata.create_all(engine)
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
