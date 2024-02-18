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
    cstring = f'mysql+pymysql://{username}:{password}@localhost/{dbname}'

    # Create the engine
    engine = create_engine(cstring)

    # Bind the engine to the Base metadata
    Base.metadata.bind = engine

    # Create a Session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # States with a name attribute that contain the letter 'a'
    states_with_a = session.query(State)\
        .filter(State.name.like('%a%'))\
        .order_by(State.id)\
        .all()

    # Print states
    for state in states_with_a:
        print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        list_states(username, password, dbname)
    else:
        print("Usage: ./list_states.py <mysql username>"
              "<mysql password> <database name>")
