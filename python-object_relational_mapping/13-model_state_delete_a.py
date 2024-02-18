#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, dbname):
    """
    Lists all states from the database.
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

    # States with a name attribute that contain the letter 'a'
    delete_states = session.query(State)\
        .filter(State.name.like('%a%'))\
        .delete(synchronize_session='fetch')

    # Step 3: Commit the session to save changes to the database
    session.commit()

    # Close the session
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        list_states(username, password, dbname)
