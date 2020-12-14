#!/usr/bin/python3
'''
script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
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

    """ Add new object """
    obj1 = State(name='Louisiana')
    session.add(obj1)
    session.commit()

    """ #query """
    query = session.query(State)
    """ #order data """
    column = query.filter(State.name == 'Louisiana').first()

    if column:
        print("{}".format(column.id))
    else:
        print("Not found")
