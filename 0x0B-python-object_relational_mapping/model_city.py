#!/usr/bin/python3
"""
contains the definition of a city
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State

class City(Base):
    """
    inherits from Base(imported from model_state)
    links to MySQL table cities
    class attribute id that represents a column of an auto-generated
    unique integer, cant be null and is a primary key
    class attribute name that represents a column of a string of 128
    characters and cant be null
    class attribute state_id that represents a column of an integer,
    cant be null and is a foreign key to states.id
    must us module SQLAlchemy
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
