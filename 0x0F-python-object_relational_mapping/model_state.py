#!/usr/bin/python3
"""
Definition of State class and an instance Base = declarative_base():
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Defines State class, a subclass of Base,
    which creates an SQL table with  the name 'states' and columns,
    id and name
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
