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
    cstring = f'mysql+pymysql://{username}:{password}@localhost/{dbname}'

    # Create the engine
    engine = create_engine(cstring)

    # Bind the engine to the Base metadata
    Base.metadata.bind = engine

    # Create a Session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Step 1: Query for the specific State object you want to update
    target_state = session.query(State).filter(State.id == 2).first()
    
    if target_state:
        # Step 2: Modify its attributes to the new values
        target_state.name = 'New Mexico'  # Replace 'NewStateName' with the new name you want to assign

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
