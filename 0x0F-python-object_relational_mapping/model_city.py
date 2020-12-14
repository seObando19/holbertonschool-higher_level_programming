#!/usr/bin/python3
'''
Write a Python file similar to model_state.py named model_city.py
that contains the class definition of a City.
'''
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    '''
    Class representing the `cities` table.
    Columns:
        id (int): /NOT NULL/AUTO_INCREMENT/PRIMARY_KEY/
        name (string): /VARCHAR(128)/NOT NULL/
        state_id (int): /NOT NULL/FOREING_KEY
    '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)
