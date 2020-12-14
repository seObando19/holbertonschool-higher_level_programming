#!/usr/bin/python3
'''
script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
'''
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
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
    query = session.query(State)
    """ #order data """
    column = query.filter(State.name.like('%a%')).order_by(State.id)

    for row in column:
        print("{}: {}".format(row.id, row.name))
