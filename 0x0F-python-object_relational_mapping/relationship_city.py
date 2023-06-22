#!/usr/bin/python3
"""
Definition of the class City
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from relationship_state import Base


class City(Base):
    """Defines City class, a subclass of Base,
    which creates an SQL table with  the name 'states' and columns,
    id, name and state_id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
