#!/usr/bin/python3
"""
A script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, dbname):
    """
    Connects to a database and lists all State objects from the database.
    """

    # Construct the connection string
    cstring = f'mysql+mysqldb://{username}:{password}@localhost/{dbname}'

    # Create the engine
    engine = create_engine(cstring)

    # Bind the engine to the Base metadata
    Base.metadata.bind = engine

    # Create a Session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Query first state
    first_state = session.query(State).order_by(State.id).first()

    # Print first state
    print(f"{first_state.id}: {first_state.name}")



if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        list_states(username, password, dbname)
    else:
        print("Usage: ./list_states.py <mysql username>"
              "<mysql password> <database name>")
