#!/usr/bin/python3
"""
script 14-model_city_fetch_by_state.py that prints
all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """ #create connection to engine to db """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    """ #create metadata """
    Base.metadata.create_all(engine)

    """ #create instance for engine """
    Session = sessionmaker(bind=engine)

    """ #initialize """
    session = Session()

    """ #query """
    query = session.query(City, State)
    """ #order data """
    relation = query.filter(State.id == City.state_id).order_by(City.id).all()

    for city, state in relation:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
