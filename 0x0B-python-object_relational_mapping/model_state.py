#!/usr/bin/python3
"""
contain the class definition of a state and an
instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    inherits from base
    links to MySQL table state
    class attribute id represents a column of auto-generated
    uniquie integer and it cant be null and is a primary key
    name represents a column of string max 128 characters
    and cant be null
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
